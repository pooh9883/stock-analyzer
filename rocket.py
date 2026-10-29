# -*- coding: utf-8 -*-
"""
rocket.py
=========
Watchlist Scanner: แนวรับ/แนวต้านรวมเป็นโซน + RSI (รายวัน/รายชั่วโมง) + โมเมนตัม + จังหวะเข้า (R:R)

แนวคิด: ให้ผู้ใช้ใส่รายชื่อหุ้นของตัวเอง แล้วกรองด้วยเงื่อนไข RSI และระยะห่างจากแนวรับ/แนวต้าน
เสริมด้วยคะแนนโมเมนตัม (momentum.py), อัตราส่วนผลตอบแทนต่อความเสี่ยง (R:R) และคะแนนจังหวะ "เด้ง"/"ทะลุ"

แนวรับ/แนวต้านมาจากจุดที่ราคาเคยกลับตัวจริง (swing high/low), ค่าเฉลี่ย SMA50/SMA200, Bollinger,
จุดสูง-ต่ำ 3 เดือน/52 สัปดาห์, Pivot ของวันก่อน และเลขกลม แล้วรวมจุดที่อยู่ใกล้กันเป็น "โซน" ให้คะแนนความแข็ง

⚠️ ข้อจำกัดสำคัญ:
- แนวรับ/แนวต้านเป็นโซนที่ราคาเคยมีปฏิกิริยา ไม่ใช่เส้นที่ราคาจะหยุดแน่นอน หลุดแนวรับได้เสมอ
- คะแนนเด้ง/ทะลุเป็นกฎหัวแม่มือ ไม่ได้ผ่านการทดสอบย้อนหลังว่าให้ผลดีกว่าเดาสุ่ม
- ข้อมูลฟรีจาก Yahoo อาจดีเลย์ ~15 นาที ปริมาณซื้อขายวันนี้ระหว่างตลาดเปิดยังไม่ครบ
"""

import numpy as np
import pandas as pd
import yfinance as yf

import momentum

DEFAULT_WATCHLIST = ["NVDA", "AAPL", "MSFT", "TSLA", "AMD", "MU", "META", "GOOGL", "AMZN", "AVGO"]


# ---------------------------------------------------------------
# ตัวช่วย
# ---------------------------------------------------------------
def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    gain = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + gain / loss.replace(0, np.nan))


def _clip01(x: float) -> float:
    return float(max(0.0, min(1.0, x)))


def _pick(data, sym):
    if data is None or getattr(data, "empty", True):
        return None
    try:
        d = data[sym]
    except KeyError:
        d = data
    if isinstance(d, pd.Series):
        return None
    d = d.dropna(how="all")
    return d if len(d) else None


def load_daily(symbols) -> dict:
    """ดึงรายวัน 2 ปีของทุกตัวในคำขอเดียว คืน {symbol: DataFrame OHLCV (index ไม่มี timezone)}"""
    syms = list(dict.fromkeys(symbols))
    data = yf.download(" ".join(syms), period="2y", interval="1d", group_by="ticker", progress=False, threads=True)
    out = {}
    for s in syms:
        d = _pick(data, s)
        if d is None or "Close" not in d.columns:
            continue
        d = d.copy()
        d.index = pd.to_datetime(d.index).tz_localize(None).normalize()
        out[s] = d.dropna(subset=["Close"])
    return out


def load_hourly(symbols) -> dict:
    """ดึงราคารายชั่วโมง 1 เดือน ใช้หาราคาล่าสุด + RSI รายชั่วโมง คืน {symbol: Series ราคาปิด}"""
    syms = list(dict.fromkeys(symbols))
    data = yf.download(" ".join(syms), period="1mo", interval="60m", group_by="ticker", progress=False, threads=True)
    out = {}
    for s in syms:
        d = _pick(data, s)
        if d is None or "Close" not in d.columns:
            continue
        c = d["Close"].dropna()
        if len(c):
            out[s] = c
    return out


# ---------------------------------------------------------------
# แนวรับ/แนวต้านแบบรวมเป็นโซน
# ---------------------------------------------------------------
def find_levels(d: pd.DataFrame, price: float, window: int = 5, lookback: int = 260) -> list:
    d = d.dropna(subset=["High", "Low", "Close"]).tail(lookback)
    n = len(d)
    if n < 40:
        return []
    h, l, c = d["High"].values.astype(float), d["Low"].values.astype(float), d["Close"].values.astype(float)

    prev_c = np.concatenate([[c[0]], c[:-1]])
    tr = np.maximum.reduce([h - l, np.abs(h - prev_c), np.abs(l - prev_c)])
    atr = float(tr[-14:].mean())

    cands = []  # (ราคา, ชื่อ, น้ำหนัก, เป็น swing ไหม)

    for i in range(window, n - window):
        rec = 0.5 * i / n  # จุดใหม่กว่าให้น้ำหนักมากกว่า
        if h[i] == h[i - window:i + window + 1].max():
            cands.append((float(h[i]), "สวิงสูง", 1.0 + rec, True))
        if l[i] == l[i - window:i + window + 1].min():
            cands.append((float(l[i]), "สวิงต่ำ", 1.0 + rec, True))

    close = pd.Series(c)
    if n >= 50:
        cands.append((float(close.rolling(50).mean().iloc[-1]), "SMA50", 1.5, False))
    if n >= 200:
        cands.append((float(close.rolling(200).mean().iloc[-1]), "SMA200", 2.0, False))
    if n >= 20:
        m20, s20 = close.rolling(20).mean().iloc[-1], close.rolling(20).std().iloc[-1]
        cands.append((float(m20 + 2 * s20), "Bollinger บน", 1.0, False))
        if m20 - 2 * s20 > 0:
            cands.append((float(m20 - 2 * s20), "Bollinger ล่าง", 1.0, False))
    cands.append((float(h.max()), "สูงสุด 52 สัปดาห์", 2.0, False))
    cands.append((float(l.min()), "ต่ำสุด 52 สัปดาห์", 2.0, False))
    if n >= 63:
        cands.append((float(h[-63:].max()), "สูงสุด 3 เดือน", 1.2, False))
        cands.append((float(l[-63:].min()), "ต่ำสุด 3 เดือน", 1.2, False))
    if n >= 3:  # Pivot จากแท่งวันก่อน (แท่งล่าสุดอาจยังไม่จบ)
        ph, pl, pc = h[-2], l[-2], c[-2]
        p = (ph + pl + pc) / 3
        cands.append((float(p), "Pivot", 0.8, False))
        cands.append((float(2 * p - pl), "Pivot R1", 1.0, False))
        cands.append((float(2 * p - ph), "Pivot S1", 1.0, False))
    step = 10 ** (np.floor(np.log10(max(price, 0.01))) - 1)
    base = np.floor(price / step) * step
    cands.append((float(base), "เลขกลม", 0.6, False))
    cands.append((float(base + step), "เลขกลม", 0.6, False))

    cands = [x for x in cands if x[0] > 0 and np.isfinite(x[0])]
    cands.sort(key=lambda x: x[0])
    tol = max(0.008 * price, 0.5 * atr)

    clusters = []
    for p, name, w, swing in cands:
        if clusters:
            cl = clusters[-1]
            if abs(p - cl["sum_pw"] / cl["sum_w"]) <= tol:
                cl["sum_w"] += w
                cl["sum_pw"] += p * w
                cl["items"].append((name, w, swing))
                continue
        clusters.append({"sum_w": w, "sum_pw": p * w, "items": [(name, w, swing)]})

    levels = []
    for cl in clusters:
        center = cl["sum_pw"] / cl["sum_w"]
        swings = sum(1 for _, _, s in cl["items"] if s)
        names = []
        for name, w, s in sorted(cl["items"], key=lambda x: -x[1]):
            if name in ("สวิงสูง", "สวิงต่ำ"):
                label = f"สวิง ×{swings}"
            else:
                label = name
            if label not in names:
                names.append(label)
        strength = cl["sum_w"]
        if abs(center / price - 1) <= 0.003:
            kind = "at"
        elif center < price:
            kind = "support"
        else:
            kind = "resistance"
        levels.append({
            "price": float(center), "strength": float(strength), "kind": kind,
            "label": " · ".join(names[:4]), "dist_pct": float((center / price - 1) * 100),
            "touches": swings,
        })
    return levels


def strength_label(s: float) -> str:
    return "แข็งมาก" if s >= 5 else ("แข็ง" if s >= 3 else "พอใช้")


def _nearest(levels, kind):
    pool = [x for x in levels if x["kind"] == kind]
    strong = [x for x in pool if x["strength"] >= 2.0]
    pool = strong or pool
    if not pool:
        return None
    return max(pool, key=lambda x: x["price"]) if kind == "support" else min(pool, key=lambda x: x["price"])


# ---------------------------------------------------------------
# สร้างแถวผลลัพธ์ของหุ้น 1 ตัว
# ---------------------------------------------------------------
def compute_row(sym: str, d: pd.DataFrame, hourly: pd.Series, spy_daily: pd.Series, spy_live_chg: float):
    if d is None or len(d) < 60:
        return None
    c = d["Close"].astype(float)

    # ราคาสด: ใช้แท่งรายชั่วโมงล่าสุดถ้าใหม่กว่าแท่งรายวัน
    price, prev_close = float(c.iloc[-1]), float(c.iloc[-2])
    rsi_h = None
    if hourly is not None and len(hourly) >= 20:
        live_date = pd.Timestamp(hourly.index[-1]).tz_localize(None).normalize() if pd.Timestamp(hourly.index[-1]).tzinfo else pd.Timestamp(hourly.index[-1]).normalize()
        last_daily = c.index[-1]
        if live_date >= last_daily:
            price = float(hourly.iloc[-1])
            prev_close = float(c.iloc[-2]) if live_date == last_daily else float(c.iloc[-1])
        rsi_h = float(rsi(hourly.astype(float)).iloc[-1])

    chg = (price / prev_close - 1) * 100
    rsi_d = float(rsi(c).iloc[-1])
    levels = find_levels(d, price)
    sup, res = _nearest(levels, "support"), _nearest(levels, "resistance")

    dist_sup = (price - sup["price"]) / price * 100 if sup else None
    dist_res = (res["price"] - price) / price * 100 if res else None
    rr = None
    if sup and res and price > sup["price"]:
        rr = (res["price"] - price) / (price - sup["price"])

    high20 = float(d["High"].iloc[-21:-1].max()) if len(d) > 21 else None
    low20 = float(d["Low"].iloc[-21:-1].min()) if len(d) > 21 else None
    broke_up = high20 is not None and price >= high20
    broke_dn = low20 is not None and price <= low20
    vol_ratio = None
    if "Volume" in d.columns and len(d) > 21:
        avg = float(d["Volume"].iloc[-21:-1].mean())
        vol_ratio = float(d["Volume"].iloc[-1] / avg) if avg > 0 else None
    sma200 = float(c.rolling(200).mean().iloc[-1]) if len(c) >= 200 else None
    above200 = None if sma200 is None else price > sma200

    mom = None
    try:
        m = momentum._metrics(c, spy_daily, 21, momentum.DEFAULT_WEIGHTS)
        mom = None if m is None else m["score"]
    except Exception:
        pass

    # ----- คะแนนจังหวะ (กฎหัวแม่มือ) -----
    prox_sup = 0.0 if dist_sup is None else _clip01(1 - dist_sup / 6)
    rsi_low = _clip01((55 - rsi_d) / 25)
    rr_s = 0.0 if rr is None else _clip01((rr - 1) / 2)
    rebound = round(100 * (0.40 * prox_sup + 0.25 * rsi_low + 0.25 * rr_s + 0.10 * (1 if above200 else 0)))

    prox_res = 1.0 if broke_up else (0.0 if dist_res is None else _clip01(1 - dist_res / 4))
    mom_s = 0.5 if mom is None else mom / 100
    vol_s = 0.3 if vol_ratio is None else _clip01((vol_ratio - 0.8) / 1.2)
    rsi_ok = 1.0 if 50 <= rsi_d <= 70 else (0.5 if (45 <= rsi_d < 50 or 70 < rsi_d <= 75) else 0.0)
    breakout = round(100 * (0.35 * prox_res + 0.30 * mom_s + 0.20 * vol_s + 0.15 * rsi_ok))

    # ----- สัญญาณ -----
    flags = []
    if dist_sup is not None and dist_sup <= 2:
        flags.append("📍 ใกล้แนวรับ")
    if dist_res is not None and dist_res <= 2:
        flags.append("🧱 ใกล้แนวต้าน")
    if rsi_d <= 30:
        flags.append("🟢 RSI ต่ำ")
    if rsi_d >= 70:
        flags.append("🔥 RSI ร้อน")
    if broke_up:
        flags.append("🚀 ทะลุสูงสุด 20 วัน")
    if broke_dn:
        flags.append("⚠️ หลุดต่ำสุด 20 วัน")
    if vol_ratio is not None and vol_ratio >= 1.5:
        flags.append("📊 ปริมาณพุ่ง")
    mkt_red_green = spy_live_chg is not None and spy_live_chg <= -0.3 and chg > 0
    if mkt_red_green:
        flags.append("💪 เขียวสวนตลาดแดง")

    return {
        "symbol": sym, "price": price, "chg": chg, "rsi_d": rsi_d, "rsi_h": rsi_h,
        "sup": sup, "res": res, "dist_sup": dist_sup, "dist_res": dist_res, "rr": rr,
        "mom": mom, "rebound": rebound, "breakout": breakout, "vol_ratio": vol_ratio,
        "above200": above200, "broke_up": broke_up, "broke_dn": broke_dn,
        "mkt_red_green": mkt_red_green, "spread": None if spy_live_chg is None else chg - spy_live_chg,
        "flags": flags, "levels": levels, "history": d,
    }


def build_rows(symbols, daily_map: dict, hourly_map: dict, bench: str = "SPY"):
    spy_d = daily_map.get(bench)
    if spy_d is None:
        return [], None
    spy_close = spy_d["Close"].astype(float)
    spy_chg = None
    sh = hourly_map.get(bench)
    spy_price, spy_prev = float(spy_close.iloc[-1]), float(spy_close.iloc[-2])
    if sh is not None and len(sh):
        live_date = pd.Timestamp(sh.index[-1]).tz_localize(None).normalize() if pd.Timestamp(sh.index[-1]).tzinfo else pd.Timestamp(sh.index[-1]).normalize()
        if live_date >= spy_close.index[-1]:
            spy_price = float(sh.iloc[-1])
            spy_prev = float(spy_close.iloc[-2]) if live_date == spy_close.index[-1] else float(spy_close.iloc[-1])
    spy_chg = (spy_price / spy_prev - 1) * 100

    rows = []
    for s in symbols:
        if s == bench or s not in daily_map:
            continue
        try:
            r = compute_row(s, daily_map[s], hourly_map.get(s), spy_close, spy_chg)
        except Exception:
            r = None
        if r:
            rows.append(r)
    return rows, spy_chg


def plain_summary(r: dict) -> str:
    """สรุปจังหวะเป็นประโยคเดียว อ่านแล้วเข้าใจทันที"""
    parts = [f"ราคา {r['price']:,.2f}"]
    if r["sup"]:
        parts.append(f"แนวรับ {r['sup']['price']:,.2f} (ห่าง {r['dist_sup']:.1f}% · {strength_label(r['sup']['strength'])})")
    if r["res"]:
        parts.append(f"แนวต้าน {r['res']['price']:,.2f} (ห่าง {r['dist_res']:.1f}% · {strength_label(r['res']['strength'])})")
    near_sup = r["dist_sup"] is not None and r["dist_sup"] <= 3
    near_res = r["dist_res"] is not None and r["dist_res"] <= 3
    if near_sup and near_res:
        verdict = "ราคาอยู่ระหว่างแนวรับและแนวต้านที่ใกล้กันมาก กรอบแคบ รอดูว่าจะหลุดทางไหน"
    elif near_sup:
        verdict = "ราคาใกล้แนวรับ ถ้ายืนได้มีจุดอ้างอิงตั้งจุดยอมขาดทุนใกล้ ๆ แต่ถ้าหลุดแนวรับต้องยอมรับว่าผิดทาง"
    elif near_res:
        verdict = "ราคาใกล้แนวต้าน มักเจอแรงขายหรือชะลอ ถ้าทะลุพร้อมปริมาณถึงถือว่าแข็งแรง"
    else:
        verdict = "ราคาอยู่กลางทาง ไม่ใกล้แนวรับหรือแนวต้าน จังหวะเข้าที่คุ้มความเสี่ยงยังไม่ชัด"
    if r["rr"] is not None:
        parts.append(f"R:R {r['rr']:.1f}")
    parts.append(f"RSI {r['rsi_d']:.0f}")
    return " · ".join(parts) + " → " + verdict