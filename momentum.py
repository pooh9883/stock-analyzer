# -*- coding: utf-8 -*-
"""
momentum.py
===========
โมเมนตัมตามงานวิจัยวิชาการ — คำนวณคะแนน 0-100 + ปัจจัยที่อธิบายได้ + ธงเตือนความเสี่ยง

ปัจจัยที่ใช้ (ทุกตัวคำนวณจากราคารายวันล่าสุด ไม่ใช้ backtest):
 1) แข็งกว่าตลาดหลายช่วง (3 / 6 / 12 เดือน)     — Jegadeesh & Titman (1993)
 2) เทรนด์ขาขึ้น (SMA50, SMA200, SMA200 ชี้ขึ้น)   — Moskowitz, Ooi & Pedersen (2012)
 3) ใกล้จุดสูงสุด 52 สัปดาห์                       — George & Hwang (2004)
 4) ขึ้นอย่างสม่ำเสมอ (ไม่ใช่พุ่งทีเดียว)           — Da, Gurun & Warachka (2014)
 5) ความผันผวนต่ำ / ไม่ตกหนัก                      — Barroso & Santa-Clara (2015)
 + ธงเตือน: เดือนล่าสุดมักกลับตัวสั้น ๆ (Jegadeesh 1990) จึงตัดเดือนล่าสุดออกจากโมเมนตัม 12 เดือนเป็นค่าเริ่มต้น

⚠️ ข้อจำกัดสำคัญ:
- งานวิจัยพบ "ค่าเฉลี่ยของหุ้นจำนวนมาก" ไม่ใช่การรับประกันหุ้นรายตัว
- โมเมนตัมเคยพังหนักช่วงตลาดกลับตัวแรง (momentum crash) เช่นปี 2009
- คะแนนสูง = มีแรงส่งตามงานวิจัย ไม่ใช่คำสั่งซื้อ
"""

import numpy as np
import pandas as pd
import yfinance as yf

DEFAULT_WEIGHTS = {"rs": 35, "trend": 25, "high52": 15, "consistency": 15, "risk": 10}
TRADING_DAYS_YEAR = 252


# ---------------------------------------------------------------
# โหลดราคา (batch คำขอเดียว)
# ---------------------------------------------------------------
def load_closes(symbols, period: str = "2y") -> pd.DataFrame:
    syms = list(dict.fromkeys([s.strip().upper() for s in symbols if s and str(s).strip()]))
    if not syms:
        return pd.DataFrame()
    data = yf.download(" ".join(syms), period=period, group_by="ticker", progress=False, threads=True)
    if data is None or data.empty:
        return pd.DataFrame()

    out = {}
    for s in syms:
        try:
            try:
                ser = data[s]["Close"]
            except KeyError:
                ser = data["Close"]
            if isinstance(ser, pd.DataFrame):
                ser = ser.iloc[:, 0]
            ser = ser.dropna()
            if len(ser) > 0:
                out[s] = ser
        except Exception:
            continue
    if not out:
        return pd.DataFrame()
    df = pd.DataFrame(out)
    df.index = pd.to_datetime(df.index).tz_localize(None).normalize()
    return df


# ---------------------------------------------------------------
# แกนคำนวณ
# ---------------------------------------------------------------
def _clip01(x: float) -> float:
    return float(max(0.0, min(1.0, x)))


def _metrics(stock: pd.Series, bench: pd.Series, skip: int, weights: dict):
    df = pd.concat([stock.rename("s"), bench.rename("b")], axis=1).dropna()
    n = len(df)
    if n < 130:
        return None
    s, m = df["s"], df["b"]

    def pct(series, k):
        return float(series.iloc[-1] / series.iloc[-1 - k] - 1) * 100 if n > k else None

    # ----- ผลตอบแทนเทียบตลาด -----
    rets = []
    for key, label, k in [("1m", "1 เดือน", 21), ("3m", "3 เดือน", 63), ("6m", "6 เดือน", 126)]:
        sr, mr = pct(s, k), pct(m, k)
        rets.append({"key": key, "label": label, "stock": sr, "bench": mr,
                     "diff": None if sr is None or mr is None else sr - mr})

    if n > TRADING_DAYS_YEAR + skip:
        lab = "12 เดือน (ไม่รวมเดือนล่าสุด)" if skip else "12 เดือน"
        a, b = -1 - TRADING_DAYS_YEAR, -1 - skip
        sr = float(s.iloc[b] / s.iloc[a] - 1) * 100
        mr = float(m.iloc[b] / m.iloc[a] - 1) * 100
        rets.append({"key": "12m", "label": lab, "stock": sr, "bench": mr, "diff": sr - mr})

    # ----- เทรนด์ -----
    sma50 = s.rolling(50).mean()
    sma200 = s.rolling(200).mean()
    last = float(s.iloc[-1])
    trend_flags = []
    above200 = above50 = golden = rising200 = None
    if n >= 200:
        above200 = last > float(sma200.iloc[-1])
        golden = float(sma50.iloc[-1]) > float(sma200.iloc[-1])
        trend_flags += [above200, golden]
        s200 = sma200.dropna()
        if len(s200) > 21:
            rising200 = float(s200.iloc[-1]) > float(s200.iloc[-22])
            trend_flags.append(rising200)
    if n >= 50:
        above50 = last > float(sma50.iloc[-1])
    ext50 = (last / float(sma50.iloc[-1]) - 1) * 100 if n >= 50 else None

    # ----- ใกล้จุดสูงสุด 52 สัปดาห์ -----
    win = min(n, TRADING_DAYS_YEAR)
    high52 = float(s.iloc[-win:].max())
    ratio52 = last / high52

    # ----- ความสม่ำเสมอ -----
    r = s.pct_change().dropna()
    used = r.iloc[-TRADING_DAYS_YEAR:len(r) - skip] if skip else r.iloc[-TRADING_DAYS_YEAR:]
    pos_days = float((used > 0).mean()) if len(used) > 20 else None
    wins = total = 0
    for i in range(12):
        end = n - 1 - 21 * i
        start = end - 21
        if start < 0:
            break
        total += 1
        if s.iloc[end] / s.iloc[start] > m.iloc[end] / m.iloc[start]:
            wins += 1
    months_ratio = wins / total if total >= 6 else None

    # ----- ความเสี่ยง -----
    vol = float(r.iloc[-60:].std() * np.sqrt(TRADING_DAYS_YEAR) * 100)
    seg = s.iloc[-win:]
    mdd = float((seg / seg.cummax() - 1).min() * 100)

    # ----- คะแนนรายปัจจัย (0-1) -----
    comps = {}
    rs_parts = [_clip01(0.5 + x["diff"] / 40) for x in rets if x["key"] in ("3m", "6m", "12m") and x["diff"] is not None]
    comps["rs"] = float(np.mean(rs_parts)) if rs_parts else None
    comps["trend"] = float(np.mean(trend_flags)) if trend_flags else None
    comps["high52"] = _clip01((ratio52 - 0.70) / 0.30)
    cparts = []
    if months_ratio is not None:
        cparts.append(months_ratio)
    if pos_days is not None:
        cparts.append(_clip01((pos_days - 0.45) / 0.15))
    comps["consistency"] = float(np.mean(cparts)) if cparts else None
    comps["risk"] = float(np.mean([_clip01(1 - abs(mdd) / 50), _clip01(1 - (vol - 20) / 60)]))

    num = den = 0.0
    for k, w in weights.items():
        if comps.get(k) is not None and w > 0:
            num += comps[k] * w
            den += w
    score = round(num / den * 100) if den > 0 else None

    return {
        "n": n, "last": last, "rets": rets, "score": score, "comps": comps,
        "above200": above200, "above50": above50, "golden": golden, "rising200": rising200,
        "trend_flags": trend_flags, "ext50": ext50, "ratio52": ratio52, "high52": high52,
        "pos_days": pos_days, "months_wins": wins, "months_total": total,
        "vol": vol, "mdd": mdd,
    }


def _verdict(score):
    if score is None:
        return "ประเมินไม่ได้", "#9a9aa8", "⚪", "ข้อมูลไม่พอ"
    if score >= 75:
        return "โมเมนตัมแข็งแรงมาก", "#3ecf6e", "🟢", "แรงส่งเป็นใจ"
    if score >= 60:
        return "โมเมนตัมแข็งแรง", "#7ddc9b", "🟢", "แรงส่งค่อนข้างดี"
    if score >= 40:
        return "โมเมนตัมเป็นกลาง", "#d4af37", "🟡", "ยังไม่ชัด รอดูก่อน"
    if score >= 25:
        return "โมเมนตัมอ่อนแอ", "#f0a35e", "🟠", "แรงส่งไม่เป็นใจ"
    return "โมเมนตัมอ่อนแอมาก", "#e5534b", "🔴", "สวนเทรนด์"


def _flags(m: dict) -> list:
    out = []
    one_m = next((x for x in m["rets"] if x["key"] == "1m"), None)
    if m["ext50"] is not None and m["ext50"] > 15:
        out.append(("warn", f"ราคาห่าง SMA50 อยู่ {m['ext50']:+.0f}% — วิ่งไกลจากค่าเฉลี่ยมาก มีโอกาสย่อสั้น ๆ"))
    if one_m and one_m["stock"] is not None and one_m["stock"] > 25:
        out.append(("warn", f"ขึ้นแรง {one_m['stock']:+.0f}% ใน 1 เดือน — งานวิจัยพบว่าเดือนล่าสุดมักกลับตัวสั้น ๆ"))
    if one_m and one_m["diff"] is not None and one_m["diff"] < 0:
        longer = [x for x in m["rets"] if x["key"] in ("3m", "6m", "12m") and x["diff"] is not None]
        if longer and all(x["diff"] > 0 for x in longer):
            out.append(("info", "ช่วง 1 เดือนล่าสุดอ่อนกว่าตลาด แต่ช่วงยาวยังแข็ง — อาจเป็นแค่พักตัว"))
    longer = [x for x in m["rets"] if x["key"] in ("3m", "6m", "12m") and x["diff"] is not None]
    if longer and all(x["diff"] < 0 for x in longer):
        out.append(("warn", "อ่อนกว่าตลาดทั้ง 3 ช่วงยาว — โมเมนตัมเป็นลบชัดเจน"))
    if m["mdd"] < -40:
        out.append(("warn", f"เคยตกหนักสุด {m['mdd']:.0f}% ในรอบ 1 ปี — ผันผวนสูงมาก"))
    if m["vol"] > 60:
        out.append(("warn", f"ความผันผวนสูง {m['vol']:.0f}% ต่อปี — ราคาแกว่งแรง"))
    return out


# ---------------------------------------------------------------
# ฟังก์ชันหลัก: สกอร์การ์ดของหุ้น 1 ตัว
# ---------------------------------------------------------------
def momentum_scorecard(ticker_symbol: str, benchmark: str = "SPY", skip_recent_month: bool = True,
                       weights: dict = None) -> dict:
    try:
        weights = {**DEFAULT_WEIGHTS, **(weights or {})}
        t, b = ticker_symbol.strip().upper(), (benchmark or "SPY").strip().upper()
        if t == b:
            return {"available": False, "reason": "หุ้นกับตัวเทียบเป็นตัวเดียวกัน เลือกตัวเทียบอื่น เช่น SPY หรือ QQQ"}
        closes = load_closes([t, b], period="2y")
        if t not in closes.columns or b not in closes.columns:
            return {"available": False, "reason": f"ดึงราคา {t} หรือ {b} ไม่ได้"}
        skip = 21 if skip_recent_month else 0
        m = _metrics(closes[t], closes[b], skip, weights)
        if m is None:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอ (ต้องการอย่างน้อย ~130 วันทำการ)"}

        label, color, icon, signal = _verdict(m["score"])
        rets = m["rets"]
        longer = [x for x in rets if x["key"] in ("3m", "6m", "12m") and x["diff"] is not None]
        k_pos = sum(1 for x in longer if x["diff"] > 0)

        reasons = []
        if longer:
            reasons.append(f"แข็งกว่าตลาด {k_pos}/{len(longer)} ช่วง")
        if m["trend_flags"]:
            reasons.append("เทรนด์ขาขึ้นครบ" if all(m["trend_flags"]) else f"เทรนด์ผ่าน {sum(m['trend_flags'])}/{len(m['trend_flags'])} ข้อ")
        reasons.append(f"อยู่ที่ {m['ratio52']*100:.0f}% ของจุดสูงสุด 52 สัปดาห์")

        def status(v, good, mid):
            return "good" if v >= good else ("mid" if v >= mid else "bad")

        factors = []
        if m["comps"]["rs"] is not None:
            st_ = "good" if k_pos == len(longer) else ("bad" if k_pos == 0 else "mid")
            factors.append({
                "name": "แข็งกว่าตลาดหลายช่วง", "ref": "Jegadeesh & Titman (1993)",
                "status": st_, "value": f"ชนะ {b} {k_pos}/{len(longer)} ช่วง",
                "meaning": "หุ้นที่ชนะตลาดต่อเนื่อง 3-12 เดือน มักชนะต่ออีกเล็กน้อย",
            })
        if m["comps"]["trend"] is not None:
            tf = m["trend_flags"]
            factors.append({
                "name": "เทรนด์ขาขึ้น", "ref": "Moskowitz, Ooi & Pedersen (2012)",
                "status": status(m["comps"]["trend"], 0.99, 0.5),
                "value": f"ผ่าน {sum(tf)}/{len(tf)} ข้อ (เหนือ SMA200, SMA50 เหนือ SMA200, SMA200 ชี้ขึ้น)",
                "meaning": "สินทรัพย์ที่อยู่ในขาขึ้นของตัวเอง มักขึ้นต่อมากกว่าตัวที่อยู่ในขาลง",
            })
        factors.append({
            "name": "ใกล้จุดสูงสุด 52 สัปดาห์", "ref": "George & Hwang (2004)",
            "status": status(m["ratio52"], 0.90, 0.75),
            "value": f"อยู่ที่ {m['ratio52']*100:.0f}% ของจุดสูงสุด ({m['high52']:,.2f})",
            "meaning": "หุ้นที่ใกล้จุดสูงสุดมักไปต่อ ส่วนที่ห่างมากมักอ่อนแรง",
        })
        if m["comps"]["consistency"] is not None:
            parts = []
            if m["months_total"] >= 6:
                parts.append(f"ชนะตลาด {m['months_wins']}/{m['months_total']} เดือน")
            if m["pos_days"] is not None:
                parts.append(f"วันที่ขึ้น {m['pos_days']*100:.0f}%")
            factors.append({
                "name": "ขึ้นอย่างสม่ำเสมอ", "ref": "Da, Gurun & Warachka (2014)",
                "status": status(m["comps"]["consistency"], 0.65, 0.4),
                "value": " · ".join(parts),
                "meaning": "ขึ้นทีละนิดสม่ำเสมอ ต่อได้ดีกว่าพุ่งทีเดียวจากข่าวเดียว",
            })
        factors.append({
            "name": "ไม่ผันผวน/ตกหนักเกินไป", "ref": "Barroso & Santa-Clara (2015)",
            "status": status(m["comps"]["risk"], 0.65, 0.4),
            "value": f"ผันผวน {m['vol']:.0f}%/ปี · ตกหนักสุด {m['mdd']:.0f}% ใน 1 ปี",
            "meaning": "โมเมนตัมที่ผันผวนต่ำ เสี่ยงโดนกลับตัวแรง (momentum crash) น้อยกว่า",
        })

        return {
            "available": True, "ticker": t, "benchmark": b, "skip": skip,
            "score": m["score"], "label": label, "color": color, "icon": icon, "signal": signal,
            "reasons": reasons, "flags": _flags(m), "rets": rets, "factors": factors,
            "risk": {"vol": m["vol"], "mdd": m["mdd"], "ext50": m["ext50"], "ratio52": m["ratio52"]},
            "weights": weights,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# สแกนหลายตัว จัดอันดับโมเมนตัม
# ---------------------------------------------------------------
def momentum_scan(symbols, benchmark: str = "SPY", skip_recent_month: bool = True) -> dict:
    try:
        b = (benchmark or "SPY").strip().upper()
        syms = [s for s in dict.fromkeys([x.strip().upper() for x in symbols if x]) if s != b]
        if not syms:
            return {"available": False, "reason": "ไม่มีรายชื่อหุ้นให้สแกน"}
        closes = load_closes(syms + [b], period="2y")
        if b not in closes.columns:
            return {"available": False, "reason": f"ดึงราคา {b} ไม่ได้"}
        skip = 21 if skip_recent_month else 0

        rows = []
        for s in syms:
            if s not in closes.columns:
                continue
            m = _metrics(closes[s], closes[b], skip, DEFAULT_WEIGHTS)
            if m is None or m["score"] is None:
                continue
            get = lambda k: next((x["diff"] for x in m["rets"] if x["key"] == k), None)
            flags = _flags(m)
            rows.append({
                "symbol": s, "score": m["score"], "label": _verdict(m["score"])[0],
                "rs3m": get("3m"), "rs6m": get("6m"), "rs12m": get("12m"),
                "ratio52": m["ratio52"] * 100, "vol": m["vol"],
                "warn": sum(1 for lv, _ in flags if lv == "warn"),
                "warn_text": " · ".join(t for lv, t in flags if lv == "warn")[:140],
            })
        if not rows:
            return {"available": False, "reason": "คำนวณคะแนนไม่สำเร็จสักตัว"}
        rows.sort(key=lambda r: r["score"], reverse=True)
        return {"available": True, "rows": rows, "benchmark": b, "skip": skip}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# โซน "หุ้นเขียว ตลาดแดง" แบบกำลังดี (กฎหัวแม่มือ ปรับเกณฑ์ได้ ไม่ได้ผ่านการ backtest)
# ใช้กับการขยับรายวัน (ตอนนี้เทียบราคาปิดเมื่อวาน)
# ---------------------------------------------------------------
DEFAULT_ZONE_PARAMS = {
    "mkt_min": 0.3,        # ตลาดต้องลบอย่างน้อยเท่านี้ ถึงนับว่า "แดงจริง"
    "mkt_sweet_max": 1.0,  # ตลาดลบไม่เกินเท่านี้ ถึงอยู่ในโซนกำลังดี
    "mkt_avoid": 2.0,      # ตลาดลบเกินเท่านี้ ถือว่าแดงหนัก ระวัง
    "stock_min": 1.0,      # หุ้นต้องบวกอย่างน้อยเท่านี้
    "stock_sweet_max": 3.0,  # หุ้นบวกไม่เกินเท่านี้ ถึงอยู่ในโซนกำลังดี
    "stock_hot": 6.0,      # หุ้นบวกเกินเท่านี้ ถือว่าขึ้นแรงเกิน ระวังไล่ราคา
    "spread_min": 1.5,     # หุ้นต้องแข็งกว่าตลาดอย่างน้อยเท่านี้ (จุด)
}


def green_red_zone(stock_pct: float, market_pct: float, params: dict = None) -> dict:
    p = {**DEFAULT_ZONE_PARAMS, **(params or {})}
    spread = stock_pct - market_pct

    def out(zone, icon, label, color, detail):
        return {"zone": zone, "icon": icon, "label": label, "color": color, "detail": detail, "spread": spread}

    if market_pct > -p["mkt_min"]:
        return out("none", "⚪", "ยังไม่เข้าสถานการณ์", "#9a9aa8",
                   f"ตลาดขยับแค่ {market_pct:+.2f}% ถือว่าแกว่งปกติ ยังไม่ใช่ 'ตลาดแดง' จริง")
    if stock_pct <= 0:
        return out("none", "🔴", "หุ้นแดงตามตลาด", "#e5534b",
                   f"ตลาดแดง {market_pct:+.2f}% และหุ้นก็ลบ {stock_pct:+.2f}% ไม่ใช่หุ้นที่ยืนได้")
    if market_pct <= -p["mkt_avoid"]:
        return out("avoid", "🔴", "ตลาดแดงหนัก ระวัง", "#e5534b",
                   f"ตลาดลบ {market_pct:+.2f}% แรงมาก หุ้นดีก็มักโดนลากลงตามกัน ต่อให้วันนี้หุ้นเขียว")
    if stock_pct >= p["stock_hot"]:
        return out("caution", "🟠", "ขึ้นแรงเกิน ระวังไล่ราคา", "#f0a35e",
                   f"หุ้นบวก {stock_pct:+.2f}% ในวันเดียว ระยะสั้นมักกลับตัว ควรเช็กข่าวว่าขึ้นเพราะอะไร")
    if stock_pct < p["stock_min"] or spread < p["spread_min"]:
        return out("weak", "⚪", "เขียวแต่ยังไม่ชัด", "#9a9aa8",
                   f"หุ้นแข็งกว่าตลาด {spread:.1f} จุด ยังน้อยกว่าเกณฑ์ ({p['spread_min']:.1f} จุด) อาจเป็นแรงสุ่ม")
    if market_pct >= -p["mkt_sweet_max"] and stock_pct <= p["stock_sweet_max"]:
        return out("sweet", "🟢", "โซนกำลังดี", "#3ecf6e",
                   f"ตลาดแดงพอเห็น ({market_pct:+.2f}%) หุ้นเขียวไม่แรงเกิน ({stock_pct:+.2f}%) แข็งกว่าตลาด {spread:.1f} จุด")
    return out("ok", "🟡", "พอใช้", "#d4af37",
               f"หุ้นแข็งกว่าตลาด {spread:.1f} จุด แต่ตัวเลขอยู่นอกโซนกำลังดี (ตลาดลบมากหรือหุ้นขึ้นค่อนข้างแรง)")