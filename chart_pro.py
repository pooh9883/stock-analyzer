# -*- coding: utf-8 -*-
"""
chart_pro.py
============
หน้ากราฟโปร (รอบที่ 1): แท่งเทียน + EMA 9/21/50/200 + volume + RSI 14 + เส้นแนวรับ/แนวต้านพร้อมป้ายราคา
ฝั่งขวา: เครื่องมือคำนวณ (ราคาเข้า/ตัดขาดทุน/เป้า/งบ) · อ่านกราฟให้ฟัง · รายการเส้นอ้างอิง

เรียกใช้จาก app.py:  chart_pro.render_chart_pro()

เทคนิค: ฝัง TradingView Lightweight Charts (v4.2.0 โหลดจาก CDN ต้องมีอินเทอร์เน็ต) ผ่าน components.html
ข้อมูลทั้งหมดมาจาก yfinance (ฟรี ดีเลย์ราว 15 นาที) · แนวรับ/แนวต้านใช้ rocket.find_levels

⚠️ เส้นแนวรับ/แนวต้านเป็น "โซนที่ราคาเคยมีปฏิกิริยา" ไม่ใช่เส้นที่ราคาจะหยุดแน่นอน · ไม่ใช่คำแนะนำซื้อ-ขาย
Lightweight Charts™ © TradingView, Inc. (ตามไลเซนส์ ต้องคงเครดิตที่มุมกราฟไว้)
"""

import json
import math

import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf

import rocket
import tools_ui

GOLD, GREEN, RED, TEXT, GREY = "#fcee0a", "#19f5a5", "#ff2a6d", "#e6f1ff", "#7d86a6"
LIB_URL = "https://cdn.jsdelivr.net/npm/lightweight-charts@4.2.0/dist/lightweight-charts.standalone.production.js"

RANGES = {"1 สัปดาห์": 7, "2 สัปดาห์": 14, "1 เดือน": 30, "3 เดือน": 91, "6 เดือน": 182, "1 ปี": 365, "5 ปี": 1826, "ทั้งหมด": None}
INTRA_RANGES = {"1 วัน": 1, "2 วัน": 2, "3 วัน": 3, "5 วัน": 5, "ทั้งหมดที่มี": None}
HOURLY_RANGES = {"1 สัปดาห์": 7, "2 สัปดาห์": 14, "1 เดือน": 30, "3 เดือน": 91, "6 เดือน": 182, "ทั้งหมดที่มี": None}
TFS = {"1 นาที (1m)": "1m", "5 นาที (5m)": "5m", "1 ชั่วโมง (1h)": "1h", "วัน (D)": "D", "สัปดาห์ (W)": "W"}
RANGES_BY_TF = {"1m": INTRA_RANGES, "5m": INTRA_RANGES, "1h": HOURLY_RANGES, "D": RANGES, "W": RANGES}
DEFAULT_RNG = {"1m": 0, "5m": 2, "1h": 2, "D": 2, "W": 3}
INTRA_CFG = {"1m": ("7d", "1m"), "5m": ("60d", "5m"), "1h": ("730d", "1h")}  # ข้อจำกัดของ Yahoo
EMAS = [(9, "#fcee0a"), (21, "#00f0ff"), (50, "#b388ff"), (200, "#ff9f1c")]


# ---------------------------------------------------------------
# ข้อมูล
# ---------------------------------------------------------------
@st.cache_data(ttl=300, show_spinner=False)
def _load_daily(sym: str) -> pd.DataFrame:
    d = yf.Ticker(sym).history(period="5y", interval="1d", auto_adjust=False)
    if d is None or d.empty:
        return pd.DataFrame()
    d = d.copy()
    d.index = pd.to_datetime(d.index).tz_localize(None).normalize()
    return d.dropna(subset=["Open", "High", "Low", "Close"])


@st.cache_data(ttl=30, show_spinner=False)
def _ext_quote(sym: str) -> dict:
    """ราคาช่วงก่อน/หลังตลาด จาก Yahoo: {"state","price","pct","label","regular"}"""
    try:
        info = yf.Ticker(sym).info or {}
    except Exception:
        return {}
    state = str(info.get("marketState", "")).upper()
    reg = info.get("regularMarketPrice") or info.get("currentPrice")
    post, pre = info.get("postMarketPrice"), info.get("preMarketPrice")
    out = {"state": state, "regular": reg}
    if state in ("POST", "POSTPOST", "CLOSED") and post:
        out.update(price=float(post), pct=info.get("postMarketChangePercent"), label="หลังตลาดปิด")
    elif state in ("PRE", "PREPRE") and pre:
        out.update(price=float(pre), pct=info.get("preMarketChangePercent"), label="ก่อนตลาดเปิด")
    elif state == "REGULAR":
        out["label"] = "ตลาดเปิดอยู่"
    return out


@st.cache_data(ttl=30, show_spinner=False)
def _load_intra(sym: str, tf: str, ext: bool = True) -> pd.DataFrame:
    """แท่งนาที/ชั่วโมง (เวลาแปลงเป็นเวลาไทย ดีเลย์ราว 15 นาที) ext=True รวมช่วงก่อน/หลังตลาด"""
    period, interval = INTRA_CFG[tf]
    try:
        d = yf.Ticker(sym).history(period=period, interval=interval, auto_adjust=False, prepost=ext)
    except Exception:
        return pd.DataFrame()
    if d is None or d.empty:
        return pd.DataFrame()
    d = d.copy()
    d.index = pd.to_datetime(d.index).tz_convert("Asia/Bangkok").tz_localize(None)
    return d.dropna(subset=["Open", "High", "Low", "Close"])


@st.cache_data(ttl=3600, show_spinner=False)
def _load_earnings(sym: str) -> list:
    try:
        ed = yf.Ticker(sym).get_earnings_dates(limit=20)
        if ed is None or len(ed) == 0:
            return []
        idx = pd.to_datetime(ed.index).tz_localize(None).normalize()
        return sorted(set(idx))
    except Exception:
        return []


def _to_weekly(d: pd.DataFrame) -> pd.DataFrame:
    w = d.resample("W").agg({"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"})
    return w.dropna(subset=["Close"])


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _num(x):
    try:
        v = float(x)
        return None if math.isnan(v) or math.isinf(v) else round(v, 4)
    except Exception:
        return None


def _atr(d: pd.DataFrame, n: int = 14) -> float:
    h, l, c = d["High"].astype(float), d["Low"].astype(float), d["Close"].astype(float)
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1)
    v = float(tr.rolling(n).mean().iloc[-1])
    return v if v == v and v > 0 else float(c.iloc[-1]) * 0.02


def _swing_pivots(d: pd.DataFrame, atr: float, k: int = 4, look: int = 12, min_prom: float = 1.0, provisional: bool = False) -> list:
    """หา swing high/low ที่ 'มีนัยสำคัญ' (ราคาถอยออกจากจุดนั้นอย่างน้อย min_prom เท่า ATR ทั้งสองฝั่ง)"""
    o, h, l, c = (d[x].astype(float).values for x in ("Open", "High", "Low", "Close"))
    v = d["Volume"].astype(float).values
    vavg = pd.Series(v).rolling(50, min_periods=10).mean().bfill().values
    n = len(d)
    last_i = n - 1
    out = []
    for i in range(k, n - k):
        lo_w, hi_w = i - k, i + k + 1
        is_high = h[i] >= h[lo_w:hi_w].max()
        is_low = l[i] <= l[lo_w:hi_w].min()
        if not (is_high or is_low):
            continue
        a, b = max(0, i - look), min(n, i + look + 1)
        if is_high:
            prom = h[i] - max(l[a:i + 1].min(), l[i:b].min())
            if prom >= min_prom * atr:
                p = 0.5 * (h[i] + max(o[i], c[i]))  # ผสมไส้เทียนกับตัวเทียน ลดอคติจากไส้ยาว
                out.append({"i": i, "p": p, "hi": True, "prom": prom / atr, "vol": v[i] / vavg[i] if vavg[i] else 1.0, "age": last_i - i})
        if is_low:
            prom = min(h[a:i + 1].max(), h[i:b].max()) - l[i]
            if prom >= min_prom * atr:
                p = 0.5 * (l[i] + min(o[i], c[i]))
                out.append({"i": i, "p": p, "hi": False, "prom": prom / atr, "vol": v[i] / vavg[i] if vavg[i] else 1.0, "age": last_i - i})
    if provisional:
        # จุดกลับตัว "รอยืนยัน": ท้ายกราฟที่มีแท่งตามหลังไม่ครบ k แท่ง แต่ราคาเด้ง/ย่อออกมาแล้วอย่างน้อย min_prom เท่า ATR
        for i in range(max(k, n - k), n - 1):
            if i - k < 0:
                continue
            a = max(0, i - look)
            if l[i] <= l[i - k:].min():
                prom = min(h[a:i + 1].max(), h[i:].max()) - l[i]
                if prom >= min_prom * atr:
                    p = 0.5 * (l[i] + min(o[i], c[i]))
                    out.append({"i": i, "p": p, "hi": False, "prom": prom / atr, "vol": v[i] / vavg[i] if vavg[i] else 1.0,
                                "age": last_i - i, "pending": True})
            if h[i] >= h[i - k:].max():
                prom = max(l[a:i + 1].min(), l[i:].min())
                prom = h[i] - prom
                if prom >= min_prom * atr:
                    p = 0.5 * (h[i] + max(o[i], c[i]))
                    out.append({"i": i, "p": p, "hi": True, "prom": prom / atr, "vol": v[i] / vavg[i] if vavg[i] else 1.0,
                                "age": last_i - i, "pending": True})
    return out


def _age_text(days: int) -> str:
    if days < 14:
        return "ไม่กี่วันก่อน"
    if days < 60:
        return f"{round(days / 7)} สัปดาห์ก่อน"
    if days < 700:
        return f"{round(days / 30)} เดือนก่อน"
    return f"{days / 365:.1f} ปีก่อน"


def find_smart_levels(daily: pd.DataFrame, price: float, intraday: bool = False) -> list:
    """
    แนวรับ/แนวต้านแบบหลายปัจจัย:
      1) หา swing high/low ที่ราคาถอยออกชัดเจน (กรองด้วย ATR ปรับตามความผันผวนของหุ้นแต่ละตัว)
      2) จัดกลุ่มจุดที่ใกล้กันเป็น 'โซน' (กว้างตาม ATR) โดยรวมจุดสูง+ต่ำเข้าด้วยกัน เพราะแนวต้านเก่ากลายเป็นแนวรับได้
      3) ให้คะแนน: จำนวนครั้งที่ราคาเคยกลับตัว · ความใหม่ (ครึ่งชีวิต ~8 เดือน) · แรงของการกลับตัว · วอลุ่ม ·
         เคยสลับบทบาทต้าน↔รับ · ตรงกับ SMA50/200
      4) เลือกโซนที่แข็งที่สุดด้านละ 2 โซน ห่างกันพอ ไม่กระจุก
    """
    d = daily.dropna(subset=["Open", "High", "Low", "Close"]).tail(1260)
    if len(d) < 80:
        return []
    atr = min(_atr(d), 0.04 * price)  # หุ้นผันผวนสูงมาก: จำกัดสเกลไม่ให้โซนกว้างจนเส้นหายไปหมด
    f = min(1.0, atr / (0.008 * price))  # ตัวคูณเพดาน/พื้น % ให้เล็กลงตามแท่งสั้น (กราฟนาทีขยับน้อยกว่ารายวันมาก)
    half = max(60.0, 0.25 * len(d)) if intraday else 170.0
    # Fractal 2 สเกล: N=5 (สวิงทั่วไป) และ N=10 (สวิงใหญ่ ให้น้ำหนักมากกว่า)
    pv = {(x["i"], x["hi"]): x for x in _swing_pivots(d, atr, k=5, look=12, min_prom=1.0, provisional=True)}
    for x in _swing_pivots(d, atr, k=10, look=20, min_prom=1.5):
        pv[(x["i"], x["hi"])] = dict(x, big=True)
    piv = list(pv.values())
    if not piv:
        return []
    H, L = d["High"].astype(float).values, d["Low"].astype(float).values

    width = max(0.9 * atr, 0.012 * price * f)
    piv.sort(key=lambda x: x["p"])
    clusters, cur = [], [piv[0]]
    for p in piv[1:]:
        if p["p"] - cur[0]["p"] <= width:
            cur.append(p)
        else:
            clusters.append(cur)
            cur = [p]
    clusters.append(cur)

    close = d["Close"].astype(float)
    sma = {n: float(close.rolling(n).mean().iloc[-1]) for n in (50, 200) if len(close) >= n}

    zones = []
    for cl in clusters:
        ws = []
        for x in cl:
            rec = 0.5 ** (x["age"] / half)                         # ความใหม่: ครึ่งชีวิตราว 170 แท่ง (~8 เดือนถ้ารายวัน)
            strength = min(x["prom"], 4.0) / 2.0                 # ยิ่งเด้ง/ร่วงแรง ยิ่งน่าเชื่อ
            vol = 1.0 + 0.25 * min(max(x["vol"] - 1.0, 0.0), 2.0)  # วอลุ่มสูงกว่าปกติ = หนักแน่นขึ้น
            ws.append(rec * (0.6 + strength) * vol * (1.3 if x.get("big") else 1.0))
        wsum = sum(ws)
        center = sum(w * x["p"] for w, x in zip(ws, cl)) / wsum
        touches = len(cl)
        newest = min(x["age"] for x in cl)
        both = any(x["hi"] for x in cl) and any(not x["hi"] for x in cl)
        score = wsum * (1.25 if both else 1.0)
        near_ma = [f"SMA{n}" for n, m in sma.items() if abs(m - center) <= width * 0.6]
        if near_ma:
            score += 0.6
        # นับ "การแตะ" จากแท่งเทียนทุกแท่งที่วิ่งเข้าโซน (ครั้งละหนึ่งรอบ เว้นห่างอย่างน้อย 3 แท่ง)
        tol = 0.15 * atr
        inz = (H >= min(x["p"] for x in cl) - tol) & (L <= max(x["p"] for x in cl) + tol)
        events, gapn = 0, 99
        for flag in inz:
            if flag:
                if gapn >= 3:
                    events += 1
                gapn = 0
            else:
                gapn += 1
        score += 0.2 * min(events, 10)
        strong_single = touches == 1 and cl[0]["prom"] >= 3.0 and newest <= 120
        if (touches < 2 or events < 3) and not strong_single:
            continue
        zones.append({"center": center, "lo": min(x["p"] for x in cl), "hi": max(x["p"] for x in cl),
                      "touches": max(touches, events), "newest": newest, "both": both, "ma": near_ma, "score": score,
                      "pending": any(x.get("pending") for x in cl)})

    side_min = max(0.5 * atr, 0.015 * price * f)   # ห่างราคาปัจจุบันพอสมควร ไม่งั้นแทบไม่มีความหมาย
    gap = max(0.9 * atr, 0.02 * price * f)

    def choose(cands, n=3):
        # ให้น้ำหนักโซนที่อยู่ใกล้ราคาปัจจุบันมากกว่าเล็กน้อย แล้วคัดโซนที่ซ้อน/ชิดกันออก
        cands = sorted(cands, key=lambda z: -z["score"] / (1 + abs(z["center"] / price - 1) / (0.10 * max(f, 0.1))))
        out = []
        for z in cands:
            if abs(z["center"] / price - 1) > 0.35 * max(f, 0.1) or abs(z["center"] - price) < side_min:
                continue
            if all(abs(z["center"] - o["center"]) >= gap for o in out):
                out.append(z)
            if len(out) == n:
                break
        return out

    sups = choose([z for z in zones if z["center"] < price])
    ress = choose([z for z in zones if z["center"] > price])

    zmax = max([z["score"] for z in sups + ress] or [1.0])

    def label_of(z):  # เทียบกับโซนที่แข็งสุดของหุ้นตัวนี้ ไม่ให้ขึ้น "แข็งมาก" ทุกเส้น
        r = z["score"] / zmax
        if r >= 0.85 and z["touches"] >= 4:
            lb = "แข็งมาก"
        elif r >= 0.6:
            lb = "แข็ง"
        elif r >= 0.35:
            lb = "ปานกลาง"
        else:
            lb = "อ่อน"
        return lb + (" · รอยืนยัน" if z.get("pending") else "")

    def reason_of(z, role):
        t = f"ราคาเคยกลับตัวตรงโซนนี้ {z['touches']} ครั้ง" + ("" if intraday else f" ล่าสุด {_age_text(z['newest'])}")
        if z.get("pending"):
            t += " · มีจุดกลับตัวล่าสุดที่ยังรอแท่งถัดไปยืนยัน"
        if z["both"]:
            t += " · เคยสลับบทบาทต้าน↔รับ (ยิ่งน่าเชื่อ)"
        if z["ma"]:
            t += " · ตรงกับ " + "/".join(z["ma"])
        return t

    out = []
    for role, lst, nm in (("resistance", ress, "แนวต้าน"), ("support", sups, "แนวรับ")):
        lst = sorted(lst, key=lambda z: abs(z["center"] - price))
        for i, z in enumerate(lst):
            out.append({"kind": role, "name": f"{nm} {i + 1}", "price": round(z["center"], 2),
                        "lo": round(z["lo"], 2), "hi": round(z["hi"], 2), "strength": round(z["score"], 2),
                        "touches": z["touches"], "label": label_of(z), "reason": reason_of(z, role)})
    if not ress:  # ราคาอยู่จุดสูงสุดใหม่ ไม่มีประวัติด้านบน → คาดการณ์จากการขยายคลื่นราคา + เลขกลม
        out += _projected_resistance(d, price, atr, [o["price"] for o in out], f)
    return sorted(out, key=lambda z: -z["price"])


def _projected_resistance(d: pd.DataFrame, price: float, atr: float, taken: list, f: float = 1.0) -> list:
    lo = float(d["Low"].astype(float).tail(120).min())
    hi = float(d["High"].astype(float).tail(120).max())
    cand = []
    for r, nm in ((1.272, "Fib 1.272"), (1.618, "Fib 1.618")):
        p = lo + (hi - lo) * r
        if p > price:
            cand.append((p, f"คาดการณ์จากการขยายคลื่นขาขึ้นล่าสุด ({nm}) — ไม่มีประวัติที่ราคาเคยถูกกด"))
    mag = 10 ** math.floor(math.log10(price))
    step = mag / 2 if price / mag < 5 else mag
    rnd = math.floor(price / step) * step + step
    cand.append((rnd, "เลขกลมที่นักลงทุนมักใช้เป็นเป้า/จุดขายทำกำไร"))
    cand = [c for c in cand if c[0] - price >= 0.5 * atr and c[0] / price - 1 <= 0.35 * max(f, 0.1)]
    cand.sort(key=lambda c: c[0])
    out = []
    for p, why in cand:
        if all(abs(p - t) >= max(1.2 * atr, 0.02 * price * f) for t in taken + [o["price"] for o in out]):
            out.append({"kind": "resistance", "name": f"แนวต้านคาดการณ์ {len(out) + 1}", "price": round(p, 2),
                        "lo": round(p, 2), "hi": round(p, 2), "strength": 0.0, "touches": 0, "label": "คาดการณ์",
                        "reason": why, "proj": True})
        if len(out) == 2:
            break
    return out


def pick_levels(daily: pd.DataFrame, price: float, per_side: int = 2, intraday: bool = False) -> list:
    """แนวรับ/แนวต้านที่ 'แข็งพอ' ใกล้ราคาปัจจุบัน (เรียงจากราคาสูงไปต่ำ)"""
    try:
        return find_smart_levels(daily, price, intraday)
    except Exception:
        return []


def build_payload(daily: pd.DataFrame, timeframe: str, range_label: str, levels: list, earnings: list, intra=None) -> dict:
    """แปลงข้อมูลเป็น JSON สำหรับกราฟ (EMA/RSI คำนวณจากข้อมูลทั้งชุดก่อน แล้วค่อยกำหนดช่วงที่เห็น)"""
    intraday = intra is not None
    if intraday:
        bars = intra
        t = [int(x) for x in ((bars.index - pd.Timestamp("1970-01-01")) // pd.Timedelta("1s"))]
    else:
        bars = _to_weekly(daily) if timeframe == "W" else daily
        t = [x.strftime("%Y-%m-%d") for x in bars.index]
    close = bars["Close"].astype(float)

    candles = [{"time": t[i], "open": _num(r.Open), "high": _num(r.High), "low": _num(r.Low), "close": _num(r.Close)}
               for i, r in enumerate(bars.itertuples())]
    volume = [{"time": t[i], "value": _num(r.Volume) or 0,
               "color": "rgba(25,245,165,.38)" if r.Close >= r.Open else "rgba(255,42,109,.38)"}
              for i, r in enumerate(bars.itertuples())]

    emas = {}
    for n, color in EMAS:
        s = _ema(close, n)
        # EMA ช่วงแรกยังไม่นิ่ง ตัดทิ้งช่วง warm-up
        pts = [{"time": t[i], "value": _num(v)} for i, v in enumerate(s.values) if i >= n - 1 and _num(v) is not None]
        emas[str(n)] = {"color": color, "data": pts}

    r = rocket.rsi(close)
    rsi = []
    for i, v in enumerate(r.values):
        nv = _num(v)
        rsi.append({"time": t[i], "value": nv} if nv is not None else {"time": t[i]})  # ไม่มีค่า = ช่องว่าง (ให้แกนเวลาตรงกับกราฟราคา)

    markers = []
    seen = set()
    dclose = daily["Close"].astype(float)
    didx = daily.index
    for d in earnings:
        if d > didx[-1] or d < didx[0]:
            continue
        pos = int(didx.searchsorted(d))  # แท่งแรกที่ >= วันประกาศ
        if pos < 1:
            continue
        end = min(pos + 1, len(dclose) - 1)  # เผื่อประกาศหลังตลาดปิด ราคาจะตอบสนองวันถัดไป
        react = (dclose.iloc[end] / dclose.iloc[pos - 1] - 1) * 100
        j = int(bars.index.searchsorted(d))
        if j >= len(bars) or t[j] in seen:
            continue
        seen.add(t[j])
        markers.append({"time": t[j], "position": "belowBar", "color": "#ff2a6d", "shape": "circle",
                        "text": f"งบ {react:+.1f}%"})

    markers.sort(key=lambda m: m["time"])  # ไลบรารีบังคับให้เรียงเวลาจากเก่าไปใหม่

    last = bars.index[-1]
    months = RANGES_BY_TF[timeframe][range_label]
    first = bars.index[0] if months is None else max(bars.index[0], last - pd.Timedelta(days=months))
    if intraday:
        from_v = int(t[int(bars.index.searchsorted(first))]) if len(t) else 0
    else:
        from_v = first.strftime("%Y-%m-%d")
    return {
        "candles": candles, "volume": volume, "emas": emas, "rsi": rsi, "markers": markers,
        "levels": [{"price": round(z["price"], 2), "lo": z.get("lo"), "hi": z.get("hi"), "title": f'{z["name"]} · {z["label"]}', "kind": z["kind"], "proj": bool(z.get("proj"))} for z in levels],
        "last_price": _num(close.iloc[-1]),
        "from": from_v, "intraday": intraday,
    }


# ---------------------------------------------------------------
# กราฟ (HTML + Lightweight Charts)
# ---------------------------------------------------------------
_HTML = """
<style>
  html,body{margin:0;padding:0;background:#05060d;color:#e6f1ff;font-family:'Chakra Petch','IBM Plex Sans Thai',system-ui,sans-serif;}
  #legend{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:center;padding:6px 8px 4px 8px;font-size:12px;min-height:22px;}
  #legend .ohlc{color:#c9ced9;font-variant-numeric:tabular-nums;margin-right:6px;}
  #legend .chip{display:inline-flex;align-items:center;gap:6px;padding:2px 8px;border:1px solid rgba(255,255,255,.12);
    border-radius:6px;background:rgba(255,255,255,.04);font-variant-numeric:tabular-nums;}
  #legend .dot{width:8px;height:3px;border-radius:2px;display:inline-block;}
  #price{width:100%;height:440px;}
  #vol{width:100%;height:90px;border-top:1px solid rgba(255,255,255,.08);}
  #rsiwrap{position:relative;border-top:1px solid rgba(255,255,255,.08);}
  #rsilabel{position:absolute;left:8px;top:4px;z-index:3;font-size:11px;color:#00f0ff;}
  #rsi{width:100%;height:150px;}
  #fail{display:none;padding:40px 20px;color:#ff5470;font-size:14px;}
</style>
<div id="fail">โหลดไลบรารีกราฟไม่สำเร็จ — ตรวจอินเทอร์เน็ต (ต้องโหลดจาก cdn.jsdelivr.net)</div>
<div id="legend"></div>
<div id="price"></div>
<div id="vol"></div>
<div id="rsiwrap"><div id="rsilabel">RSI 14</div><div id="rsi"></div></div>
<script src="__LIB__" onerror="document.getElementById('fail').style.display='block'"></script>
<script>
(function(){
  if (typeof LightweightCharts === 'undefined') { document.getElementById('fail').style.display='block'; return; }
  var D = __DATA__;
  var UP='#19f5a5', DOWN='#ff2a6d';
  var base = {
    layout:{background:{type:'solid',color:'#05060d'},textColor:'#7d86a6',fontSize:11},
    grid:{vertLines:{color:'rgba(0,240,255,.045)'},horzLines:{color:'rgba(0,240,255,.045)'}},
    rightPriceScale:{borderColor:'rgba(255,255,255,.10)',minimumWidth:78},
    timeScale:{borderColor:'rgba(255,255,255,.10)',rightOffset:4,timeVisible:!!D.intraday,secondsVisible:false},
    crosshair:{mode:0},
    localization:{locale:'th-TH'}
  };
  var pEl=document.getElementById('price'), rEl=document.getElementById('rsi');
  var pc = LightweightCharts.createChart(pEl, Object.assign({}, base, {width:pEl.clientWidth,height:pEl.clientHeight}));
  var rc = LightweightCharts.createChart(rEl, Object.assign({}, base, {width:rEl.clientWidth,height:rEl.clientHeight,
            timeScale:Object.assign({}, base.timeScale, {visible:false})}));

  var candle = pc.addCandlestickSeries({upColor:UP,downColor:DOWN,borderUpColor:UP,borderDownColor:DOWN,wickUpColor:UP,wickDownColor:DOWN,
                 priceLineVisible:true, priceLineColor:'#00f0ff', priceLineStyle:3, priceLineWidth:1, lastValueVisible:true});
  candle.setData(D.candles);
  pc.priceScale('right').applyOptions({scaleMargins:{top:0.06,bottom:0.06}});
  if (D.markers.length) candle.setMarkers(D.markers);

  var vEl=document.getElementById('vol');
  var vc = LightweightCharts.createChart(vEl, Object.assign({}, base, {width:vEl.clientWidth,height:vEl.clientHeight,
            timeScale:Object.assign({}, base.timeScale, {visible:false})}));
  var vol = vc.addHistogramSeries({priceFormat:{type:'volume'},lastValueVisible:false,priceLineVisible:false});
  vol.setData(D.volume);
  vc.priceScale('right').applyOptions({scaleMargins:{top:0.1,bottom:0}});

  var emaSeries = {};
  Object.keys(D.emas).forEach(function(n){
    var s = pc.addLineSeries({color:D.emas[n].color,lineWidth:n==='200'?2:1,priceLineVisible:false,lastValueVisible:false,crosshairMarkerVisible:false});
    s.setData(D.emas[n].data); emaSeries[n]=s;
  });

  function Zone(lo,hi,color){this.lo=lo;this.hi=hi;this.color=color;}
  Zone.prototype.attached=function(p){this.series=p.series;};
  Zone.prototype.detached=function(){};
  Zone.prototype.updateAllViews=function(){};
  Zone.prototype.paneViews=function(){
    var z=this;
    return [{zOrder:function(){return 'bottom';},renderer:function(){return {draw:function(target){
      target.useBitmapCoordinateSpace(function(sc){
        var a=z.series.priceToCoordinate(z.hi), b=z.series.priceToCoordinate(z.lo);
        if(a==null||b==null) return;
        var top=Math.min(a,b)*sc.verticalPixelRatio, h=Math.max(Math.abs(b-a)*sc.verticalPixelRatio,3*sc.verticalPixelRatio);
        sc.context.fillStyle=z.color; sc.context.fillRect(0,top,sc.bitmapSize.width,h);
      });}};}}];
  };
  D.levels.forEach(function(l){
    if(l.lo!=null && l.hi!=null && !l.proj){
      try{ candle.attachPrimitive(new Zone(l.lo,l.hi,l.kind==='support'?'rgba(25,245,165,.15)':'rgba(255,42,109,.15)')); }catch(e){}
    }
    var c = l.proj ? '#fcee0a' : (l.kind==='support' ? UP : DOWN);
    candle.createPriceLine({price:l.price,color:c,lineWidth:1,lineStyle:l.proj?1:2,axisLabelVisible:true,title:l.title});
  });

  var rs = rc.addLineSeries({color:'#00f0ff',lineWidth:2,priceLineVisible:false,lastValueVisible:true,
            autoscaleInfoProvider:function(){return {priceRange:{minValue:0,maxValue:100}};}});
  rs.setData(D.rsi);
  rc.priceScale('right').applyOptions({scaleMargins:{top:0.04,bottom:0.04}});
  rs.createPriceLine({price:70,color:DOWN,lineWidth:1,lineStyle:2,axisLabelVisible:true,title:'70'});
  rs.createPriceLine({price:30,color:UP,lineWidth:1,lineStyle:2,axisLabelVisible:true,title:'30'});

  // ซิงก์การเลื่อน/ซูมและเส้นกากบาทของสองกราฟ
  var charts=[pc,vc,rc], busy=false;
  charts.forEach(function(a){a.timeScale().subscribeVisibleLogicalRangeChange(function(r){
    if(busy||!r) return; busy=true;
    charts.forEach(function(b){ if(b!==a) b.timeScale().setVisibleLogicalRange(r); });
    busy=false;});});
  pc.subscribeCrosshairMove(function(p){ if(p.time) rc.setCrosshairPosition(NaN,p.time,rs); else rc.clearCrosshairPosition(); upd(p); });

  // แถบข้อมูลบนกราฟ: OHLC + ค่า EMA ของแท่งที่ชี้ (ถ้าไม่ชี้ ใช้แท่งล่าสุด)
  var lg=document.getElementById('legend');
  function f(x){return (x==null||isNaN(x))?'-':Number(x).toFixed(2);}
  var lastBar = D.candles[D.candles.length-1];
  function upd(p){
    var bar = lastBar, vals={};
    if(p && p.time && p.seriesData){
      var b=p.seriesData.get(candle); if(b) bar=b;
      Object.keys(emaSeries).forEach(function(n){var v=p.seriesData.get(emaSeries[n]); vals[n]=v?v.value:null;});
    } else {
      Object.keys(D.emas).forEach(function(n){var d=D.emas[n].data; vals[n]=d.length?d[d.length-1].value:null;});
    }
    var h='<span class="ohlc">เปิด '+f(bar.open)+' สูง '+f(bar.high)+' ต่ำ '+f(bar.low)+' ปิด '+f(bar.close)+'</span>';
    Object.keys(D.emas).forEach(function(n){
      h+='<span class="chip"><span class="dot" style="background:'+D.emas[n].color+'"></span>EMA'+n+' '+f(vals[n])+'</span>';});
    lg.innerHTML=h;
  }
  upd(null);

  var i0=0; for(var i=0;i<D.candles.length;i++){ if(D.candles[i].time>=D.from){ i0=i; break; } }
  pc.timeScale().setVisibleLogicalRange({from:i0, to:D.candles.length-1+4});

  window.addEventListener('resize',function(){
    pc.applyOptions({width:pEl.clientWidth}); vc.applyOptions({width:vEl.clientWidth}); rc.applyOptions({width:rEl.clientWidth});});
})();
</script>
"""


def _chart_html(payload: dict) -> str:
    return _HTML.replace("__LIB__", LIB_URL).replace("__DATA__", json.dumps(payload, ensure_ascii=False))


# ---------------------------------------------------------------
# อ่านกราฟให้ฟัง (กฎตายตัว ไม่ใช้ AI)
# ---------------------------------------------------------------
def narrate(sym: str, price: float, levels: list, rsi_v: float, above200) -> dict:
    sups = sorted([z for z in levels if z["kind"] == "support" and z["price"] < price], key=lambda z: -z["price"])
    ress = sorted([z for z in levels if z["kind"] == "resistance" and z["price"] > price], key=lambda z: z["price"])
    sup, res = (sups[0] if sups else None), (ress[0] if ress else None)
    d_sup = (price - sup["price"]) / price * 100 if sup else None
    d_res = (res["price"] - price) / price * 100 if res else None

    parts = [f"{sym} ตอนนี้ ${price:,.2f}"]
    if sup and res:
        parts.append(f"อยู่เหนือแนวรับหลัก ${sup['price']:,.2f} ราว {d_sup:.1f}% และห่างแนวต้าน ${res['price']:,.2f} อีก {d_res:.1f}%")
    elif sup:
        parts.append(f"อยู่เหนือแนวรับหลัก ${sup['price']:,.2f} ราว {d_sup:.1f}% และยังไม่เจอแนวต้านชัดเจนด้านบน")
    elif res:
        parts.append(f"ต่ำกว่าแนวรับที่คำนวณได้ทุกจุด ห่างแนวต้าน ${res['price']:,.2f} อีก {d_res:.1f}%")
    if rsi_v >= 70:
        rtxt = f"RSI {rsi_v:.0f} ร้อนแรง อาจพักตัวได้"
    elif rsi_v <= 30:
        rtxt = f"RSI {rsi_v:.0f} ขายหนักแล้ว อาจเด้งได้ แต่ไม่ใช่เสมอไป"
    elif rsi_v <= 40:
        rtxt = f"RSI {rsi_v:.0f} ค่อนข้างอ่อน"
    else:
        rtxt = f"RSI {rsi_v:.0f} ยังปกติ ไม่ร้อนแรง"
    text = " — ".join(parts[:1] + parts[1:2]) + f" · {rtxt}" if len(parts) > 1 else f"{parts[0]} · {rtxt}"
    if above200 is True:
        text += " · ราคายังอยู่เหนือ SMA200"
    elif above200 is False:
        text += " · ราคาอยู่ใต้ SMA200"

    if d_sup is not None and d_sup <= 3 and d_res is not None and d_res <= 3:
        tag, col = "กรอบแคบ", GOLD
    elif d_sup is not None and d_sup <= 3:
        tag, col = "ใกล้แนวรับ", GREEN
    elif d_res is not None and d_res <= 2:
        tag, col = "ใกล้แนวต้าน", RED
    elif rsi_v >= 70:
        tag, col = "RSI ร้อน", RED
    else:
        tag, col = "กลางทาง", GREY
    return {"text": text, "tag": tag, "color": col}


def _html(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


# ---------------------------------------------------------------
# เครื่องมือคำนวณด้านขวา
# ---------------------------------------------------------------
def _set(key, val):
    st.session_state[key] = round(float(val), 2)


def _pick_chip(key, chips, target):
    """เลือกราคาอ้างอิงจากตัวเลือก แล้วเติมลงช่องราคาเข้า (รีเซ็ตตัวเลือกให้กดซ้ำได้)"""
    v = st.session_state.get(key)
    if v in chips:
        st.session_state[target] = round(float(chips[v]), 2)
    st.session_state[key] = None


def _calculator(sym: str, price: float, levels: list, fx: float):

    k_in, k_sl, k_tp = f"cp_entry_{sym}", f"cp_stop_{sym}", f"cp_target_{sym}"
    for k, v in ((k_in, round(price, 2)), (k_sl, 0.0), (k_tp, 0.0)):
        st.session_state.setdefault(k, v)

    sups = sorted([z for z in levels if z["kind"] == "support"], key=lambda z: -z["price"])
    ress = sorted([z for z in levels if z["kind"] == "resistance"], key=lambda z: z["price"])
    chips = {f"{nm} {pv:,.2f}": pv for nm, pv in [("ปัจจุบัน", price)] + [(z["name"], z["price"]) for z in sups + ress]}
    st.selectbox("เติมราคาเข้าจากเส้นอ้างอิง", list(chips.keys()), index=None, placeholder="เลือกเส้น...",
                 key=f"cp_chip_{sym}", on_change=_pick_chip, args=(f"cp_chip_{sym}", chips, k_in))

    entry = st.number_input("ราคาเข้า (USD)", min_value=0.0, step=0.5, format="%.2f", key=k_in)
    stop = st.number_input("จุดตัดขาดทุน (USD) ราคาที่คุณจะยอมขายถ้าตลาดผิดทาง", min_value=0.0, step=0.5, format="%.2f", key=k_sl)
    target = st.number_input("เป้าขาย (USD)", min_value=0.0, step=0.5, format="%.2f", key=k_tp)
    b1, b2 = st.columns([2, 1])
    budget = b1.number_input("งบซื้อ", min_value=0.0, step=100.0, value=0.0, key=f"cp_budget_{sym}")
    unit = b2.selectbox("หน่วย", ["USD", "บาท"], key="cp_unit", label_visibility="collapsed")
    risk_cap = st.number_input("ยอมขาดทุนได้ไม่เกิน (USD) — ไม่บังคับ", min_value=0.0, step=10.0, value=0.0, key=f"cp_risk_{sym}",
                               help="ใส่แล้วระบบจะจำกัดจำนวนหุ้นให้ขาดทุนไม่เกินจำนวนนี้ ถ้าราคาแตะจุดตัดขาดทุน (ต้องใส่จุดตัดขาดทุนด้วย)")

    if entry <= 0:
        st.info("กรอกราคาเข้าเพื่อเริ่มคำนวณ")
        return
    if stop > 0 and stop >= entry:
        st.warning("จุดตัดขาดทุนต้องต่ำกว่าราคาเข้า")
        stop = 0.0

    budget_usd = budget / fx if unit == "บาท" else budget
    shares, how = None, ""
    if budget_usd > 0:
        shares, how = budget_usd / entry, "ตามงบ"
    if risk_cap > 0 and stop > 0:
        s_risk = risk_cap / (entry - stop)
        if shares is None or s_risk < shares:
            shares, how = s_risk, "ตามเพดานขาดทุน"
    if shares is None:
        st.caption("ใส่งบซื้อ หรือเพดานขาดทุน เพื่อดูจำนวนหุ้น")
        return
    shares = math.floor(shares * 10000) / 10000  # ปัดลง 4 ตำแหน่ง

    value = shares * entry
    m1, m2 = st.columns(2)
    m1.metric("ซื้อได้", f"{shares:,.4f} หุ้น", how, delta_color="off")
    m2.metric("มูลค่า", f"${value:,.2f}", f"≈ ฿{value * fx:,.0f}", delta_color="off")
    if stop > 0:
        loss = shares * (entry - stop)
        st.metric("ถ้าแตะจุดตัดขาดทุน", f"-${loss:,.2f}", f"-{(entry - stop) / entry * 100:.1f}% · ≈ ฿{loss * fx:,.0f}", delta_color="inverse")
    if target > entry:
        gain = shares * (target - entry)
        st.metric("ถ้าถึงเป้าขาย", f"+${gain:,.2f}", f"+{(target / entry - 1) * 100:.1f}% · ≈ ฿{gain * fx:,.0f}")
        if stop > 0:
            rr = (target - entry) / (entry - stop)
            (st.success if rr >= 2 else st.info)(f"R:R = {rr:.1f}" + ("" if rr >= 2 else " (ต่ำกว่า 2 ผลตอบแทนไม่ค่อยคุ้มความเสี่ยง)"))
    st.caption(f"อัตราแลกเปลี่ยน {fx:.2f} บาท/ดอลลาร์ · ยังไม่รวมค่าธรรมเนียม · ตัวเลขคำนวณจากราคาที่คุณกรอก ไม่ใช่คำแนะนำการลงทุน · "
               "จุดตัดขาดทุนไม่การันตีว่าจะขายได้ที่ราคานั้น (ราคาอาจกระโดดข้าม)")


# ---------------------------------------------------------------
# หน้าหลัก
# ---------------------------------------------------------------
def render_chart_pro():
    h1, h2, h3 = st.columns([1.2, 1, 3])
    if "cp_sym" not in st.session_state:  # ค่าเริ่มต้นตอนเปิดแอป (ตั้งครั้งเดียว ห้ามเปลี่ยน default ทุกรอบ)
        st.session_state["cp_sym"] = st.session_state.get("cp_sym_last", "SNDK")
    sym = h1.text_input("รหัสหุ้น", key="cp_sym").strip().upper()
    if not sym:
        st.info("พิมพ์รหัสหุ้น เช่น AAPL, NVDA, TSLA")
        return
    st.session_state["cp_sym_last"] = sym

    with st.spinner(f"กำลังโหลด {sym} ..."):
        daily = _load_daily(sym)
    if daily.empty or len(daily) < 60:
        st.error(f"ดึงข้อมูล {sym} ไม่ได้หรือข้อมูลไม่พอ (ตรวจรหัสหุ้นและอินเทอร์เน็ต หรืออาจโดน rate-limit ชั่วคราว)")
        return

    close = daily["Close"].astype(float)
    price, prev = float(close.iloc[-1]), float(close.iloc[-2])
    chg = (price / prev - 1) * 100
    xq = _ext_quote(sym)
    if xq.get("price"):
        xp = xq["price"]
        xpct = xq.get("pct")
        xpct = float(xpct) if xpct is not None else (xp / price - 1) * 100
        h2.metric(f"{sym} · {xq['label']}", f"${xp:,.2f}", f"{xpct:+.2f}%")
        h2.caption(f"ปิดปกติ ${price:,.2f} ({chg:+.2f}%)")
    else:
        h2.metric(sym, f"${price:,.2f}", f"{chg:+.2f}%")
    h3.caption("[chart_pro v16] ข้อมูลจาก Yahoo Finance อาจดีเลย์ราว 15 นาที · กราฟรายวัน/สัปดาห์ = ราคาปิดปกติ · กราฟนาที/ชั่วโมงรวมก่อน-หลังตลาดได้ (สวิตช์ด้านล่าง)")

    c1, c2 = st.columns([1, 2])
    tf_label = c1.selectbox("กรอบเวลาแท่ง", list(TFS.keys()), index=2, key="cp_tf2")  # เริ่มที่ 1 ชั่วโมง
    tf = TFS[tf_label]
    intraday = tf in INTRA_CFG
    rng = c2.selectbox("ช่วงที่แสดง", list(RANGES_BY_TF[tf].keys()), index=DEFAULT_RNG[tf], key=f"cp_rng_{tf}")
    auto, ext = False, True
    if intraday:
        t1, t2 = st.columns(2)
        auto = t1.toggle("รีเฟรชกราฟอัตโนมัติทุก 60 วินาที", value=True, key="cp_auto")
        if "cp_ext" not in st.session_state:
            st.session_state["cp_ext"] = True
        st.session_state["cp_ext"] = st.session_state["cp_ext"]
        ext = t2.toggle("รวมช่วงก่อน/หลังตลาด (Pre/Post)", key="cp_ext")

    # กราฟนาที/ชั่วโมง: คำนวณเส้นจากแท่งสั้นนั้นเอง (ไม่งั้นเส้นรายวันห่างราคาไกลเกินใช้)
    lv_src, lv_price, lv_intra = daily, price, False
    if intraday:
        ib = _load_intra(sym, tf, ext)
        if not ib.empty and len(ib) >= 120:
            lv_src, lv_price, lv_intra = ib, float(ib["Close"].iloc[-1]), True
    levels = pick_levels(lv_src, lv_price, intraday=lv_intra)
    if lv_intra:
        price = lv_price
    earnings = _load_earnings(sym)

    def _chart_block():
        if intraday:
            bars = _load_intra(sym, tf, ext)
            if bars.empty or len(bars) < 30:
                st.warning("ไม่มีข้อมูลแท่งสั้นตอนนี้ (ตลาดอาจปิดอยู่ หรือ Yahoo ไม่ส่งข้อมูล) ลองกรอบเวลาอื่น")
                return
            payload = build_payload(daily, tf, rng, levels, [], intra=bars)
        else:
            payload = build_payload(daily, tf, rng, levels, earnings)
        components.html(_chart_html(payload), height=730, scrolling=False)

    left, right = st.columns([2.6, 1.3], gap="medium")
    with left:
        if intraday and auto:
            try:
                st.fragment(run_every=60)(_chart_block)()
            except TypeError:  # Streamlit เก่า ไม่รองรับ run_every
                _chart_block()
        else:
            _chart_block()
        st.caption("เลื่อนซ้าย-ขวา/ซูมด้วยเมาส์ได้ · เส้นประเขียว = แนวรับ · เส้นประแดง = แนวต้าน · ไม่ใช่คำแนะนำซื้อ-ขาย")
        with st.expander("📖 วิธีอ่านกราฟ และความหมายของศัพท์"):
            st.markdown(
                "- **แนวรับ / แนวต้าน** — โซนที่ราคาเคยมีปฏิกิริยา (เด้งขึ้น/ถูกกดลง) ไม่ใช่เส้นที่ราคาจะหยุดแน่นอน\n"
                "- **EMA 9/21/50/200** — เส้นค่าเฉลี่ยราคา ตัวเลขคือจำนวนแท่งที่เฉลี่ย เส้นสั้นตอบสนองไว เส้นยาวบอกแนวโน้มใหญ่\n"
                "- **RSI 14** — วัดว่าราคาขึ้น/ลงแรงแค่ไหน เกิน 70 = ร้อนแรง อาจพักตัว · ต่ำกว่า 30 = ขายหนัก อาจเด้ง (ไม่ใช่เสมอไป)\n"
                "- **Volume** — ปริมาณซื้อขาย แท่งสูงผิดปกติ = มีคนสนใจมาก\n"
                "- **จุดม่วง** — วันประกาศงบ (% คือราคาขยับรอบวันประกาศ)\n"
                "- **R:R** — อัตราส่วนกำไรที่หวังต่อความเสี่ยง ควรตั้งแต่ 2 ขึ้นไป\n"
                "- **แท่งสีเขียว/แดง** — ปิดสูงกว่า/ต่ำกว่าราคาเปิด\n\n"
                "แนวรับ/แนวต้านเป็นเพียงข้อมูลอ้างอิงจากอดีต ไม่ใช่คำแนะนำซื้อ-ขาย")

    with right:
        fx = tools_ui._fx()
        with st.expander("🧮 เครื่องมือคำนวณ — ซื้อได้กี่หุ้น · ถ้าเสียเท่าไร · ถ้าถึงเป้าได้เท่าไร", expanded=False):
            _calculator(sym, price, levels, fx)

        st.markdown("---")
        rsi_v = float(rocket.rsi(close).iloc[-1])
        sma200 = float(close.rolling(200).mean().iloc[-1]) if len(close) >= 200 else None
        nar = narrate(sym, price, levels, rsi_v, None if sma200 is None else price > sma200)
        st.markdown(_html(f"""
            <div style="border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 16px;background:rgba(255,255,255,.035);">
            <div style="font-weight:700;font-size:15px;">อ่านกราฟให้ฟัง</div>
            <div style="color:{GREY};font-size:12px;margin-bottom:8px;">สรุปจากเส้นและตัวชี้วัดบนกราฟ ไม่ใช่การทำนาย</div>
            <div style="font-size:14px;line-height:1.55;">{nar['text'].replace('$', '&#36;')}</div>
            <div style="margin-top:10px;display:inline-block;padding:3px 12px;border-radius:999px;font-size:12px;font-weight:700;
            color:{nar['color']};border:1px solid {nar['color']}66;background:{nar['color']}1f;">{nar['tag']}</div>
            </div>
        """), unsafe_allow_html=True)

        with st.expander("📌 เส้นอ้างอิงบนกราฟ — กดปุ่มเพื่อเอาราคาเส้นนั้นไปใส่ช่องคำนวณ", expanded=False):
            k_in, k_sl, k_tp = f"cp_entry_{sym}", f"cp_stop_{sym}", f"cp_target_{sym}"
            if not levels:
                st.caption("ยังไม่พบเส้นที่แข็งพอใกล้ราคานี้")
            elif any(z.get("proj") for z in levels):
                st.caption("ราคาอยู่ใกล้จุดสูงสุดใหม่ จึงไม่มีแนวต้านจากอดีต — เส้นสีเหลืองคือระดับคาดการณ์ ไม่ใช่จุดที่ราคาเคยถูกกด")
            for i, z in enumerate(levels):
                col = GREEN if z["kind"] == "support" else RED
                st.markdown(_html(f"""
                    <div style="font-size:14px;margin-top:6px;"><span style="color:{col};">●</span> {z['name']}
                    <b style="margin-left:6px;">{z['price']:,.2f}</b>
                    <span style="color:{GREY};font-size:12px;margin-left:6px;">{z['label']}</span><div style="color:{GREY};font-size:12px;margin:2px 0 0 20px;">{z['reason']} · โซน {z['lo']:,.2f}–{z['hi']:,.2f}</div></div>
                """), unsafe_allow_html=True)
                b = c = st.container()
                b.button("ใช้เป็นราคาเข้า", key=f"cp_ln_in_{sym}_{i}", on_click=_set, args=(k_in, z["price"]), use_container_width=True)
                if z["kind"] == "support":
                    c.button("ใช้เป็นจุดตัดขาดทุน", key=f"cp_ln_sl_{sym}_{i}", on_click=_set, args=(k_sl, z["price"]), use_container_width=True)
                else:
                    c.button("ใช้เป็นเป้าขาย", key=f"cp_ln_tp_{sym}_{i}", on_click=_set, args=(k_tp, z["price"]), use_container_width=True)