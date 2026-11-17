# -*- coding: utf-8 -*-
"""DROP DX · วินิจฉัยการปรับฐานของหุ้น — แยก "ราคาพักฐาน" ออกจาก "ธุรกิจมีปัญหา"

ตอบคำถามเดียว: หุ้นตัวนี้ราคาลงจากจุดสูง เพราะอะไร? ใน 4 ภาพ
  1) Healthy Correction        พักฐานตามปกติ พื้นฐานยังแข็งแรง
  2) Profit Taking             แรงขายทำกำไรหลังวิ่งแรง
  3) Valuation Risk            ราคาแพงเกินพื้นฐาน เปราะง่าย
  4) Fundamental Deterioration พื้นฐานธุรกิจเริ่มอ่อนแอ

หลักการ (ตามเงื่อนไขที่ตั้งไว้)
  • ห้ามตัดสินจากราคาลงอย่างเดียว — ต้องมีหลักฐานนอกราคา (งบ/มูลค่า/วอลุ่ม/กลุ่ม) และบอกระดับความเชื่อมั่น
  • แสดงตัวเลขทุกข้อ ✅ = เข้าข่าย · ⚠️ = ไม่เข้าข่าย · — = ไม่มีข้อมูล (ไม่นับเป็นคะแนน แต่ลดความเชื่อมั่น)
  • "แรงขายปลายปี" ไม่ใช้เป็นคำอธิบาย ถ้าไม่มีหลักฐานครบ (ดูกล่องปลายปี)
  • ทุกเกณฑ์เป็นกฎหัวแม่มือ ไม่ใช่มาตรฐาน · ไม่ใช่คำแนะนำซื้อขาย

analyze() เป็น pandas ล้วน ทดสอบแยกได้ · render(sym) ต่อกับหน้า Deep Insight"""
import datetime as _dt
import html as _html

import numpy as np
import pandas as pd

try:
    import streamlit as st
except Exception:  # pragma: no cover
    st = None
try:
    import yfinance as yf
except Exception:  # pragma: no cover
    yf = None
try:
    import stage as STG
except Exception:  # pragma: no cover
    STG = None

SCEN = [
    ("healthy", "พักฐานตามปกติ", "Healthy Correction", "#19f5a5"),
    ("profit", "แรงขายทำกำไร", "Profit Taking", "#fcee0a"),
    ("valuation", "ราคาแพงเกินพื้นฐาน", "Valuation Risk", "#ff9f43"),
    ("fund", "พื้นฐานธุรกิจอ่อนแอลง", "Fundamental Deterioration", "#ff2a6d"),
]
FUND_LENSES = ("quality", "margin", "forward", "cash", "surprise")   # เลนส์งบจาก insight.py


def _e(x):
    return _html.escape(str(x), quote=True)


def _ok(x):
    return isinstance(x, (int, float, np.floating)) and not (isinstance(x, float) and np.isnan(x))


def _ret(s, n):
    try:
        return (float(s.iloc[-1]) / float(s.iloc[-1 - n]) - 1) * 100 if len(s) > n else None
    except Exception:
        return None


# ---------------------------------------------------------------- วิเคราะห์ (pure)
def analyze(df, bench, info, lens_stances, peer_fpe=None, today=None):
    """df: DataFrame (Close, Volume) ราคาปรับแล้วของหุ้น · bench: {'SPY':Series,'QQQ':Series,'SEC':Series} ·
    info: dict ของ Yahoo · lens_stances: {key: good/mid/bad/na} จาก insight.py · คืน dict ผลทั้งหมด"""
    today = today or _dt.date.today()
    info = info or {}
    c = df["Close"].dropna().astype(float)
    v = df["Volume"].reindex(c.index).fillna(0).astype(float)
    if len(c) < 130:
        return None
    px = float(c.iloc[-1])
    ath = float(c.max())
    ath_date = c.idxmax()
    w52 = c.iloc[-252:]
    hi52 = float(w52.max())
    d52 = w52.idxmax()
    m = {
        "px": px, "ath": ath, "ath_date": ath_date, "dd_ath": (px / ath - 1) * 100,
        "hi52": hi52, "dd52": (px / hi52 - 1) * 100,
        "days_hi": int((c.index[-1] - d52).days),
        "r1": _ret(c, 21), "r3": _ret(c, 63), "r6": _ret(c, 126), "r12": _ret(c, 252),
        "years": len(c) / 252.0,
    }
    spy, sec = bench.get("SPY"), bench.get("SEC")
    for k, n in (("1", 21), ("3", 63), ("6", 126), ("12", 252)):
        m["spy" + k] = _ret(spy, n) if spy is not None else None
        m["sec" + k] = _ret(sec, n) if sec is not None else None
    # วิ่งแรงแค่ไหน "ก่อนถึงจุดสูง" (วัดจาก 6 เดือนก่อนจุดสูง → จุดสูง) เพราะตอนนี้ราคาอาจลงมาแล้ว
    pos_hi = c.index.get_loc(d52)
    m["run"] = (hi52 / float(c.iloc[pos_hi - 126]) - 1) * 100 if pos_hi >= 126 else None
    # ---- ปริมาณซื้อขาย
    ret = c.pct_change()
    last25 = ret.iloc[-25:]
    vprev = v.shift(1)
    m["dist"] = int(((last25 <= -0.002) & (v.iloc[-25:] > vprev.iloc[-25:])).sum())
    r20, v20 = ret.iloc[-20:], v.iloc[-20:]
    dn, up = v20[r20 < 0], v20[r20 > 0]
    m["dn_up"] = float(dn.mean() / up.mean()) if len(dn) >= 3 and len(up) >= 3 and up.mean() > 0 else None
    # ---- แนวโน้ม
    sma200 = c.rolling(200).mean()
    m["above200"] = bool(px > float(sma200.iloc[-1])) if not np.isnan(sma200.iloc[-1]) else None
    s200_prev = sma200.iloc[-21] if len(sma200) > 221 else np.nan
    m["s200_slope"] = (float(sma200.iloc[-1]) / float(s200_prev) - 1) * 100 if _ok(s200_prev) and not np.isnan(sma200.iloc[-1]) else None
    m["stage"] = STG.classify(c, v) if STG else None
    # ---- มูลค่า
    peg = info.get("trailingPegRatio")
    if not _ok(peg):
        peg = info.get("pegRatio")
    m["pe"], m["fpe"] = info.get("trailingPE"), info.get("forwardPE")
    m["ps"], m["peg"], m["peer_fpe"] = info.get("priceToSalesTrailing12Months"), peg, peer_fpe
    for k in ("pe", "fpe", "ps", "peg", "peer_fpe"):
        if not _ok(m[k]) or m[k] <= 0:
            m[k] = None
    # ---- งบ (จากเลนส์ของ insight.py)
    ls = {k: lens_stances.get(k, "na") for k in FUND_LENSES}
    used = [s for s in ls.values() if s in ("good", "mid", "bad")]
    m["lens_n"] = len(used)
    m["lens_bad"] = sum(1 for s in used if s == "bad")
    m["lens_good"] = sum(1 for s in used if s == "good")
    m["val_lens"] = lens_stances.get("valuation", "na")
    m["bad_names"] = [k for k, s in ls.items() if s == "bad"]
    # ---- มีการปรับฐานไหม
    m["correction"] = bool(m["dd52"] <= -5 or (m["r1"] is not None and m["r1"] <= -7))
    m["mkt_down"] = bool(m["spy1"] is not None and m["spy1"] <= -3)
    m["sec_down"] = bool(m["sec1"] is not None and m["sec1"] <= -3)

    R = {k: [] for k, *_ in SCEN}

    def rule(key, label, w, val, score, why):
        R[key].append({"label": label, "w": w, "val": val, "s": score, "why": why})

    f = lambda x, d=1, s=False: "—" if x is None else (("%+." + str(d) + "f%%") % x if s else ("%." + str(d) + "f") % x)
    stg = m["stage"]
    # ===== 1) Healthy Correction
    dd = m["dd52"]
    rule("healthy", "ถอยจากจุดสูงอยู่ในช่วงพักฐาน (5–25%)", 2, "ถอยจากจุดสูง 52 สัปดาห์ %s" % f(dd, 1, True),
         1.0 if -25 <= dd <= -5 else (0.4 if -30 <= dd < -25 else 0.0), "พักฐานปกติมักไม่ลึกเกิน ~25%")
    up_trend = None
    if stg:
        up_trend = 1.0 if stg["stage"] == 2 else (0.5 if stg["stage"] == 3 else 0.0)
    elif m["above200"] is not None:
        up_trend = 1.0 if (m["above200"] and (m["s200_slope"] or 0) > 0) else 0.0
    rule("healthy", "แนวโน้มใหญ่ยังขึ้น", 2,
         ("Stage %d (%s)" % (stg["stage"], {1: "พักฐาน", 2: "ขาขึ้น", 3: "ใกล้ยอด", 4: "ขาลง"}[stg["stage"]])) if stg else
         ("เหนือ SMA200" if m["above200"] else "ใต้ SMA200") if m["above200"] is not None else "—",
         up_trend, "ถ้าแนวโน้มใหญ่ยังขึ้น การลงมักเป็นแค่พัก")
    rule("healthy", "งบ/พื้นฐานไม่มีเลนส์ที่แย่", 2,
         "เลนส์งบแย่ %d จาก %d" % (m["lens_bad"], m["lens_n"]) if m["lens_n"] >= 3 else "ข้อมูลงบไม่พอ",
         (1.0 if m["lens_bad"] == 0 else (0.3 if m["lens_bad"] == 1 else 0.0)) if m["lens_n"] >= 3 else None,
         "ต้องมีเลนส์งบอย่างน้อย 3 ด้านถึงจะตัดสินได้")
    quiet = None
    if m["dn_up"] is not None:
        quiet = 1.0 if (m["dist"] <= 3 and m["dn_up"] <= 1.1) else (0.4 if m["dist"] <= 4 else 0.0)
    rule("healthy", "แรงขายไม่หนาแน่น (วอลุ่มวันลง ไม่เกินวันขึ้น)", 1.5,
         "วันขายหนัก %d ใน 25 วัน · วอลุ่มวันลง÷วันขึ้น %s เท่า" % (m["dist"], f(m["dn_up"], 2)), quiet, "การพักฐานจริงมักวอลุ่มเบา")
    rule("healthy", "ไม่ใช่ราคาแพงจนเปราะ", 1, "PEG %s · P/E ล่วงหน้า %s" % (f(m["peg"], 2), f(m["fpe"], 1)),
         None if (m["peg"] is None and m["fpe"] is None) else (0.0 if ((m["peg"] or 0) > 2.5 or (m["fpe"] or 0) > 45) else 1.0),
         "ของแพงเวลาตลาดกลัวมักลงแรงกว่า")
    gp = None
    if m["spy1"] is not None or m["sec1"] is not None:
        gp = 1.0 if (m["mkt_down"] or m["sec_down"]) else 0.0
    rule("healthy", "ลงตามตลาด/กลุ่ม ไม่ใช่เรื่องเฉพาะตัว", 1,
         "SPY 1 เดือน %s · ETF กลุ่ม %s · หุ้น %s" % (f(m["spy1"], 1, True), f(m["sec1"], 1, True), f(m["r1"], 1, True)), gp,
         "ถ้าทั้งตลาด/กลุ่มลงด้วย มักเป็นเรื่องภาพรวม")

    # ===== 2) Profit Taking
    big_run = None
    run = max([x for x in (m["run"], m["r6"]) if x is not None] or [None]) if (m["run"] is not None or m["r6"] is not None) else None
    if run is not None or m["r12"] is not None:
        big_run = 1.0 if ((run or 0) >= 30 or (m["r12"] or 0) >= 60) else (0.5 if ((run or 0) >= 20 or (m["r12"] or 0) >= 40) else 0.0)
    rule("profit", "วิ่งแรงมาก่อนหน้า (6 เดือนก่อนถึงจุดสูง ≥30% หรือ 12 เดือน ≥60%)", 2,
         "ขึ้น %s ใน 6 เดือนก่อนจุดสูง · 3 เดือนล่าสุด %s · 12 เดือน %s" % (f(m["run"], 0, True), f(m["r3"], 0, True), f(m["r12"], 0, True)), big_run,
         "คนที่มีกำไรเยอะมักล็อกกำไรก่อน")
    rule("profit", "เพิ่งลงจากจุดสูง (ภายใน ~2 เดือน)", 2, "ถอย %s จากจุดสูงเมื่อ %d วันก่อน" % (f(dd, 1, True), m["days_hi"]),
         1.0 if (-25 <= dd <= -5 and m["days_hi"] <= 60) else (0.3 if -25 <= dd <= -5 else 0.0), "แรงขายทำกำไรมักเกิดทันทีหลังขึ้นสุด")
    heavy = None
    if m["dn_up"] is not None:
        heavy = 1.0 if (m["dist"] >= 4 or m["dn_up"] >= 1.25) else (0.4 if m["dist"] == 3 or m["dn_up"] >= 1.1 else 0.0)
    rule("profit", "แรงขายหนาแน่น (วอลุ่มวันลงสูงกว่าวันขึ้น)", 2,
         "วันขายหนัก %d ใน 25 วัน · วอลุ่มวันลง÷วันขึ้น %s เท่า" % (m["dist"], f(m["dn_up"], 2)), heavy,
         "มีคนขายออกแรงๆ ไม่ใช่แค่ไม่มีคนซื้อ")
    rule("profit", "พื้นฐานยังไม่เสีย", 1.5, "เลนส์งบแย่ %d จาก %d" % (m["lens_bad"], m["lens_n"]) if m["lens_n"] >= 3 else "ข้อมูลงบไม่พอ",
         (1.0 if m["lens_bad"] <= 1 else 0.0) if m["lens_n"] >= 3 else None, "ขายทำกำไรต่างจากขายหนีปัญหา")
    gap = (m["r1"] - m["sec1"]) if (m["r1"] is not None and m["sec1"] is not None) else None
    rule("profit", "ลงแรงกว่ากลุ่มเดียวกัน", 1, "หุ้น %s เทียบ ETF กลุ่ม %s" % (f(m["r1"], 1, True), f(m["sec1"], 1, True)),
         None if gap is None else (1.0 if gap <= -3 else 0.0), "แรงขายเฉพาะตัวมากกว่าภาพรวม")

    # ===== 3) Valuation Risk
    ratio = (m["fpe"] / m["peer_fpe"]) if (m["fpe"] and m["peer_fpe"]) else None
    rule("valuation", "P/E ล่วงหน้าสูงกว่ามัธยฐานของหุ้นในกลุ่ม ≥1.4 เท่า", 2,
         "P/E ล่วงหน้า %s · มัธยฐานกลุ่ม %s · ratio %s" % (f(m["fpe"], 1), f(m["peer_fpe"], 1), f(ratio, 2)),
         None if ratio is None else (1.0 if ratio >= 1.4 else (0.4 if ratio >= 1.15 else 0.0)), "แพงกว่าคู่แข่งมาก = ต้องโตกว่าถึงจะคุ้ม")
    rule("valuation", "PEG สูง (>2)", 2, "PEG %s" % f(m["peg"], 2),
         None if m["peg"] is None else (1.0 if m["peg"] > 2 else (0.4 if m["peg"] > 1.5 else 0.0)), "จ่ายแพงเมื่อเทียบการเติบโต")
    rule("valuation", "P/E ล่วงหน้าสูงแบบสัมบูรณ์ (>40)", 1.5, "P/E ล่วงหน้า %s · P/E ย้อนหลัง %s" % (f(m["fpe"], 1), f(m["pe"], 1)),
         None if (m["fpe"] is None and m["pe"] is None) else (1.0 if ((m["fpe"] or 0) > 40 or (m["pe"] or 0) > 60) else (0.4 if ((m["fpe"] or 0) > 30) else 0.0)),
         "ตัวคูณสูงมาก ราคาพึ่งความฝันเยอะ")
    rule("valuation", "Price/Sales สูงมาก (>12)", 1, "P/S %s" % f(m["ps"], 1),
         None if m["ps"] is None else (1.0 if m["ps"] > 12 else (0.4 if m["ps"] > 8 else 0.0)), "เกณฑ์หยาบ: กลุ่มซอฟต์แวร์อาจสูงกว่ากลุ่มอื่นเป็นปกติ")
    rule("valuation", "เส้นอ้างอิงจากพันธบัตร (เลนส์ราคาของเว็บ) ชี้ว่าแพง", 1.5,
         {"bad": "แพงเทียบเส้นอ้างอิง", "mid": "พอประมาณ", "good": "ใกล้เส้นอ้างอิง"}.get(m["val_lens"], "ไม่มีข้อมูล"),
         {"bad": 1.0, "mid": 0.3, "good": 0.0}.get(m["val_lens"]), "ใช้เลนส์เดียวกับในหน้านี้")

    # ===== 4) Fundamental Deterioration
    fscore = None
    if m["lens_n"] >= 3:
        fscore = 1.0 if m["lens_bad"] >= 2 else (0.5 if m["lens_bad"] == 1 else 0.0)
    bn = {"quality": "คุณภาพกำไร", "margin": "มาร์จิ้น", "forward": "แนวทางข้างหน้า", "cash": "เงินสด", "surprise": "ทำเกินคาด"}
    rule("fund", "เลนส์งบแย่ตั้งแต่ 2 ด้านขึ้นไป", 3,
         ("แย่ %d จาก %d: %s" % (m["lens_bad"], m["lens_n"], ", ".join(bn[k] for k in m["bad_names"]) or "ไม่มี")) if m["lens_n"] >= 3 else "ข้อมูลงบไม่พอ",
         fscore, "นี่คือหลักฐานตรงที่สุดว่าธุรกิจมีปัญหา")
    dtr = None
    if stg:
        dtr = 1.0 if stg["stage"] == 4 else (0.4 if stg["stage"] == 3 else 0.0)
    elif m["above200"] is not None:
        dtr = 1.0 if (not m["above200"] and (m["s200_slope"] or 0) < 0) else 0.0
    rule("fund", "แนวโน้มใหญ่เป็นขาลง", 2,
         ("Stage %d" % stg["stage"]) if stg else ("ใต้ SMA200" if m["above200"] is False else "เหนือ SMA200") if m["above200"] is not None else "—",
         dtr, "ธุรกิจเสียมักทำให้แนวโน้มใหญ่กลับทิศ")
    rule("fund", "ลงลึก (≥30% จากจุดสูง 52 สัปดาห์)", 1.5, "ถอย %s" % f(dd, 1, True), 1.0 if dd <= -30 else (0.4 if dd <= -22 else 0.0),
         "ลงลึกมาก ตลาดอาจรู้อะไรที่เรายังไม่เห็น")
    rel3 = (m["r3"] - m["spy3"]) if (m["r3"] is not None and m["spy3"] is not None) else None
    rule("fund", "แพ้ตลาดชัดเจน 3 เดือน (ต่ำกว่า SPY ≥15 จุด)", 1.5, "หุ้น %s · SPY %s" % (f(m["r3"], 0, True), f(m["spy3"], 0, True)),
         None if rel3 is None else (1.0 if rel3 <= -15 else (0.4 if rel3 <= -8 else 0.0)), "แพ้ทั้งตลาดและกลุ่ม ไม่ใช่เรื่องภาพรวม")

    # ประตูกั้น: "ขายทำกำไร" ต้องมีกำไรให้ขายก่อน — ถ้าไม่ได้วิ่งแรงมาก่อน คะแนนไม่เกิน 30
    gate_profit = (big_run is not None and big_run < 0.5)
    # ---- รวมคะแนน
    scen = []
    tot_w = av_w = 0.0
    for key, th, en, col in SCEN:
        rs = R[key]
        W = sum(r["w"] for r in rs)
        A = sum(r["w"] for r in rs if r["s"] is not None)
        S = sum(r["w"] * r["s"] for r in rs if r["s"] is not None)
        tot_w += W
        av_w += A
        sc_ = (100.0 * S / A) if (A >= 0.4 * W and not (key == "fund" and m["lens_n"] < 3)) else None
        if key == "profit" and gate_profit and sc_ is not None:
            sc_ = min(sc_, 30.0)
        scen.append({"key": key, "th": th, "en": en, "col": col, "rules": rs, "cov": A / W if W else 0,
                     "score": sc_,
                     "blocked": bool(key == "fund" and m["lens_n"] < 3)})
    cov = av_w / tot_w if tot_w else 0
    ranked = sorted([s for s in scen if s["score"] is not None], key=lambda s: -s["score"])
    # "พื้นฐานอ่อนแอลง" ไม่มีคะแนนถ้าเลนส์งบน้อยกว่า 3 ด้าน (ราคาลงอย่างเดียวห้ามตัดสินว่าธุรกิจเสีย)
    verdict = {"top": None, "second": None, "gap": None, "mixed": False, "none": False}
    if ranked:
        verdict["top"] = ranked[0]
        if len(ranked) > 1:
            verdict["second"], verdict["gap"] = ranked[1], ranked[0]["score"] - ranked[1]["score"]
        verdict["mixed"] = bool(len(ranked) > 1 and verdict["gap"] < 8 and ranked[1]["score"] >= 40)
        verdict["none"] = bool(ranked[0]["score"] < 35)
    top_s = ranked[0]["score"] if ranked else 0
    gapv = verdict["gap"] if verdict["gap"] is not None else 0
    if cov >= 0.8 and gapv >= 20 and top_s >= 55 and m["lens_n"] >= 3:
        conf = "สูง"
    elif cov >= 0.6 and (gapv >= 10 or top_s >= 60):
        conf = "กลาง"
    else:
        conf = "ต่ำ"
    if m["lens_n"] < 3 and conf == "สูง":
        conf = "กลาง"
    m.update({"cov": cov, "conf": conf})
    return {"m": m, "scen": scen, "verdict": verdict, "yearend": _yearend(df, m, today), "conf": conf, "cov": cov}


# ---------------------------------------------------------------- แรงขายปลายปี (ต้องมีหลักฐาน)
def _yearend(df, m, today):
    c = df["Close"].dropna().astype(float)
    inwin = (today.month == 12) or (today.month == 11 and today.day >= 15)
    winner = (m["r12"] is not None and m["r12"] >= 40) or (m["run"] is not None and m["run"] >= 25)
    heavy = (m["dist"] >= 4) or (m["dn_up"] is not None and m["dn_up"] >= 1.25)
    falling = m["correction"]
    # สถิติของหุ้นตัวนี้เอง: 10 พ.ย. → 31 ธ.ค. ของปีก่อนๆ
    rets = []
    try:
        for y in range(today.year - 10, today.year):
            a = c[(c.index >= pd.Timestamp(y, 11, 10))].head(1)
            b = c[(c.index <= pd.Timestamp(y, 12, 31))].tail(1)
            if len(a) and len(b) and a.index[0] < b.index[0] and (a.index[0] - pd.Timestamp(y, 11, 10)).days <= 6:
                rets.append((float(b.iloc[0]) / float(a.iloc[0]) - 1) * 100)
    except Exception:
        rets = []
    hist = None
    if len(rets) >= 5:
        hist = {"n": len(rets), "neg": sum(1 for r in rets if r < 0), "avg": float(np.mean(rets))}
    if not inwin:
        status, txt = "n/a", "ตอนนี้ไม่ได้อยู่ในช่วงปลายปี (15 พ.ย.–31 ธ.ค.) จึงไม่นำเหตุผลนี้มาพิจารณา"
    elif winner and heavy and falling:
        status, txt = "evidence", "มีหลักฐานครบ 3 ข้อ: ช่วงปลายปี + หุ้นขึ้นมามาก + แรงขายหนาแน่นหลังราคาปรับลง — เข้าข่ายถูกขายปรับพอร์ต/ล็อกกำไรได้ (ยังเป็นการประเมิน ไม่ใช่ข้อเท็จจริงยืนยัน)"
    elif winner and (heavy or falling):
        status, txt = "partial", "มีหลักฐานบางส่วน (ครบไม่ถึง 3 ข้อ) — พูดได้แค่ว่า \"อาจมีส่วน\" ห้ามสรุปว่าลงเพราะปลายปี"
    else:
        status, txt = "none", "ไม่พบหลักฐานแรงขายปลายปี — อย่าอธิบายราคาที่ลงด้วยเหตุผลปลายปี ให้ดูเหตุผลอื่นแทน"
    items = [("อยู่ในช่วงปลายปี (15 พ.ย.–31 ธ.ค.)", inwin, "วันนี้ %s" % today.strftime("%d/%m/%Y")),
             ("เป็นหุ้นที่ขึ้นมามาก (12 เดือน ≥40% หรือ 6 เดือนก่อนจุดสูง ≥25%)", winner,
              "12 เดือน %s · 6 เดือนก่อนจุดสูง %s" % ("—" if m["r12"] is None else "%+.0f%%" % m["r12"], "—" if m["run"] is None else "%+.0f%%" % m["run"])),
             ("มีแรงขายหนาแน่น (วันขายหนัก ≥4 ใน 25 วัน หรือวอลุ่มวันลง ≥1.25 เท่าวันขึ้น)", heavy,
              "วันขายหนัก %d · วอลุ่มลง÷ขึ้น %s" % (m["dist"], "—" if m["dn_up"] is None else "%.2f" % m["dn_up"])),
             ("ราคาปรับลงจากจุดสูงแล้ว", falling, "ถอย %+.1f%% จากจุดสูง 52 สัปดาห์" % m["dd52"])]
    return {"status": status, "text": txt, "items": items, "hist": hist}


# ---------------------------------------------------------------- HTML
_CSS = """<style>
.dx{font-family:'Chakra Petch',sans-serif}
.dx *{box-sizing:border-box}
.dx .hud{border:1px solid rgba(0,240,255,.25);border-left:3px solid #fcee0a;background:rgba(10,12,22,.7);padding:11px 14px;margin:8px 0}
.dx .chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.dx .chip{border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.04);padding:3px 10px;font-size:12.5px;color:#c8d3f0!important;-webkit-text-fill-color:#c8d3f0}
.dx .chip b{display:block;font-size:16px;color:#fff!important;-webkit-text-fill-color:#fff;font-weight:600}
.dx .ver{--c:#19f5a5;border:1px solid var(--c);border-left:4px solid var(--c);background:linear-gradient(90deg,rgba(255,255,255,.06),transparent);padding:13px 16px;margin:12px 0}
.dx .ver .k{font-family:'Share Tech Mono',monospace;letter-spacing:2px;font-size:12px;color:var(--c)!important;-webkit-text-fill-color:var(--c)}
.dx .ver .t{font-size:21px;font-weight:700;color:#fff!important;-webkit-text-fill-color:#fff;margin:2px 0}
.dx .ver .t small{font-size:13px;font-weight:400;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4;margin-left:8px}
.dx .ver p{margin:5px 0 0;font-size:14px;line-height:1.7;color:#e6f1ff!important;-webkit-text-fill-color:#e6f1ff}
.dx .conf{display:inline-block;border:1px solid var(--c);color:var(--c)!important;-webkit-text-fill-color:var(--c);padding:0 9px;font-size:12px;margin:0 10px 0 8px;letter-spacing:1px}
.dx details{border:1px solid rgba(255,255,255,.09);border-left:3px solid var(--c);background:rgba(10,12,22,.55);margin:8px 0;padding:0}
.dx summary{cursor:pointer;list-style:none;padding:10px 14px;display:grid;grid-template-columns:1fr 150px 48px;gap:12px;align-items:center}
.dx summary::-webkit-details-marker{display:none}
.dx .nm{font-size:15px;font-weight:600;color:#fff!important;-webkit-text-fill-color:#fff}
.dx .nm small{display:block;font-size:11.5px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6;font-weight:400;letter-spacing:.5px}
.dx .bar{height:7px;background:#232738;position:relative}
.dx .bar i{position:absolute;left:0;top:0;bottom:0;background:var(--c);box-shadow:0 0 8px var(--c)}
.dx .sc{font-family:'Share Tech Mono',monospace;font-size:17px;text-align:right;color:var(--c)!important;-webkit-text-fill-color:var(--c)}
.dx .ev{padding:2px 14px 12px;border-top:1px dashed rgba(255,255,255,.1)}
.dx .row{display:grid;grid-template-columns:26px 1.3fr 1fr;gap:8px;padding:5px 0;font-size:13px;line-height:1.55;border-bottom:1px solid rgba(255,255,255,.05);color:#d7def4!important;-webkit-text-fill-color:#d7def4}
.dx .row .v{color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4}
.dx .row small{display:block;color:#6f7899!important;-webkit-text-fill-color:#6f7899;font-size:11.5px}
.dx .ye{border:1px solid rgba(255,255,255,.12);border-left:3px solid var(--c);padding:11px 14px;margin:12px 0;background:rgba(10,12,22,.55)}
.dx .ye h4{margin:0 0 4px;font-size:14px;color:var(--c)!important;-webkit-text-fill-color:var(--c);font-family:'Share Tech Mono',monospace;letter-spacing:1.5px}
.dx .ye p{margin:4px 0;font-size:13.5px;line-height:1.65;color:#e6f1ff!important;-webkit-text-fill-color:#e6f1ff}
.dx .note{font-size:12px;line-height:1.65;color:#8892b3!important;-webkit-text-fill-color:#8892b3;margin-top:10px}
.dx .easy{--c:#19f5a5;border:1px solid var(--c);border-left:5px solid var(--c);background:linear-gradient(120deg,rgba(255,255,255,.07),rgba(10,12,22,.6));padding:15px 18px;margin:6px 0 12px}
.dx .easy .k{font-family:'Share Tech Mono',monospace;letter-spacing:2px;font-size:12px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4}
.dx .easy .big{font-size:24px;font-weight:700;line-height:1.4;margin:3px 0 4px;color:var(--c)!important;-webkit-text-fill-color:var(--c)}
.dx .easy .say{font-size:15.5px;line-height:1.75;color:#f0f5ff!important;-webkit-text-fill-color:#f0f5ff;margin:4px 0 10px}
.dx .easy .facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:8px;margin:8px 0}
.dx .easy .fc{border:1px solid rgba(255,255,255,.12);background:rgba(5,6,13,.55);padding:8px 11px}
.dx .easy .fc b{display:block;font-size:12px;letter-spacing:1px;color:#8d97b8!important;-webkit-text-fill-color:#8d97b8;font-weight:500;margin-bottom:2px}
.dx .easy .fc span{font-size:14px;line-height:1.55;color:#e6ecff!important;-webkit-text-fill-color:#e6ecff}
.dx .easy .nx{margin:10px 0 2px;font-size:14px;line-height:1.7;color:#e6ecff!important;-webkit-text-fill-color:#e6ecff}
.dx .easy .nx b{color:#fcee0a!important;-webkit-text-fill-color:#fcee0a}
.dx .easy .mem{margin-top:10px;font-size:13px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4}
@media (max-width:700px){.dx summary{grid-template-columns:1fr 70px 40px}.dx .row{grid-template-columns:24px 1fr}.dx .row .v{grid-column:2}}
</style>"""


def _sym_of(s):
    return "—" if s is None else ("✅" if s >= 0.7 else ("🔸" if s >= 0.3 else "⚠️"))


_EASY = {
    "healthy": ("🟢", "พักฐานตามปกติ — ธุรกิจยังไม่เสีย", "#19f5a5",
                "ราคาลงมาแต่ยังไม่เห็นสัญญาณว่าธุรกิจมีปัญหา และแรงขายไม่หนาแน่น เหมือนหุ้นแค่พักหายใจระหว่างขึ้น",
                ["ถ้าราคาลงต่อจนหลุดเส้นเฉลี่ย 200 วัน พร้อมวอลุ่มวันลงหนักขึ้น → ภาพจะเริ่มเปลี่ยนไปทางไม่ดี",
                 "ถ้างบรอบหน้าอ่อนลงหลายด้าน → กลับมาประเมินใหม่"]),
    "profit": ("🟡", "ถูกขายทำกำไร — ไม่ใช่ธุรกิจเสีย", "#fcee0a",
               "หุ้นวิ่งแรงมาก่อน คนที่มีกำไรเลยทยอยขายออก วอลุ่มวันที่ราคาลงสูง แต่ตัวเลขงบยังไม่เสีย",
               ["ถ้าวอลุ่มวันลงเบาลงและราคาหยุดลง → เข้าข่ายแค่พักฐาน",
                "ถ้างบรอบหน้าแย่ลง หรือราคาหลุดเส้นเฉลี่ย 200 วัน → ภาพอาจเปลี่ยนเป็นปัญหาของธุรกิจ"]),
    "valuation": ("🟠", "ราคาแพงเกินพื้นฐาน เลยลงง่าย", "#ff9f43",
                  "ราคาวิ่งนำหน้าตัวธุรกิจไปไกลเมื่อเทียบกำไร/การเติบโต พอตลาดกังวลก็ลงแรงกว่าหุ้นทั่วไป ไม่ได้แปลว่าธุรกิจเสีย",
                  ["ดูงบรอบหน้าว่ากำไรโตทันราคาที่จ่ายไปหรือไม่",
                   "ระวังว่าหุ้นแพงมักผันผวนแรงจากข่าวเล็กน้อย"]),
    "fund": ("🔴", "ธุรกิจเริ่มอ่อนแอลง — ควรตรวจงบก่อน", "#ff2a6d",
             "ตัวเลขงบหลายด้านอ่อนลง และแนวโน้มราคาตามลงด้วย ไม่ใช่แค่ราคาพักฐาน",
             ["เปิดดูกล่องเลนส์งบด้านบนว่าด้านไหนอ่อน และอ่อนเพราะอะไร",
              "ตรวจให้ชัดก่อนตัดสินใจอะไร อย่าเดาจากราคา"]),
}


def headline(res):
    """(ไอคอน, หัวข้อสั้น, สี, ประโยคอธิบาย, [ดูอะไรต่อ], key) — ใช้ทั้งกล่องวินิจฉัยและกล่องสรุปบนสุดของหน้า"""
    m, V = res["m"], res["verdict"]
    top = V["top"]
    P = lambda x, d=0: "—" if x is None else ("%+." + str(d) + "f%%") % x
    key = "none"
    if top is None or (V["none"] and m["correction"]):
        ic, big, col, say, nx = "⚪", "ยังสรุปสาเหตุไม่ได้", "#ff9f43", "หลักฐานที่มีไม่ชี้ไปทางไหนชัดเจน จึงไม่เดาสาเหตุ", ["รอข้อมูลงบ/ราคาเพิ่ม แล้วดูใหม่"]
    elif not m["correction"]:
        ic, big, col, key = "🔵", "ยังไม่ได้ปรับฐานชัดเจน", "#00f0ff", "nodrop"
        say = "ราคายังอยู่ใกล้จุดสูง (ห่าง %s) จึงยังไม่มีการลงให้ต้องอธิบาย" % P(m["dd52"], 1)
        nx = ["ดูคะแนน \"ราคาแพงเกินพื้นฐาน\" ด้านล่าง เพราะหุ้นที่แพงมักลงแรงถ้าเกิดปรับฐาน"]
    elif V["mixed"]:
        a_, b_ = _EASY[top["key"]], _EASY[V["second"]["key"]]
        ic, big, col, key = "🟡", "ผสมกัน: %s + %s" % (top["th"], V["second"]["th"]), "#fcee0a", "mixed"
        say = "หลักฐานชี้ได้สองทางใกล้กัน (%.0f กับ %.0f คะแนน) · %s · อีกทาง: %s" % (top["score"], V["second"]["score"], a_[3], b_[3])
        nx = a_[4][:1] + b_[4][:1]
    else:
        ic, big, col, say, nx = _EASY[top["key"]]
        key = top["key"]
        if m["lens_n"] < 3 and top["key"] in ("healthy", "profit"):      # ไม่มีข้อมูลงบ ห้ามพูดว่า "ธุรกิจไม่เสีย"
            big = big.split(" — ")[0] + " — แต่ยังเช็กธุรกิจไม่ได้ (ข้อมูลงบไม่พอ)"
            say = say.replace("แต่ตัวเลขงบยังไม่เสีย", "").replace("และยังไม่เห็นสัญญาณว่าธุรกิจมีปัญหา", "").strip(" ,") or say
    return ic, big, col, say, nx, key


_TREND = {
    "healthy": "ถ้าเป็นการพักฐานจริง ราคามักนิ่งและวอลุ่มเบาลงก่อน แล้วค่อยหาทิศทาง · ถ้าวอลุ่มวันลงกลับหนักขึ้น แปลว่าไม่ใช่แค่พัก",
    "profit": "แรงขายทำกำไรมักหมดเมื่อคนที่อยากขายขายออกไปแล้ว ราคาจึงมักนิ่งก่อน · แต่ถ้าวอลุ่มวันลงยังหนักต่อเนื่อง แปลว่าแรงขายยังไม่จบ",
    "valuation": "หุ้นที่แพงมักแกว่งแรงตามข่าว ราคาจะนิ่งได้เมื่อกำไรโตตามทันราคาที่จ่ายไป",
    "fund": "ถ้างบรอบหน้ายังอ่อน ราคามักถูกกดต่อ · ถ้าตัวเลขกลับมาดี ภาพจะเปลี่ยนเป็นแค่พักฐานได้",
    "mixed": "สาเหตุยังผสมกัน ภาพจะชัดขึ้นเมื่อมีข้อมูลใหม่ เช่น งบรอบหน้า หรือวอลุ่มวันลงเปลี่ยนไป",
    "nodrop": "ยังไม่มีการปรับฐานให้ประเมิน · ถ้าราคาแพงอยู่ การปรับฐานครั้งหน้ามักลงแรงกว่าหุ้นทั่วไป",
    "none": "ยังไม่มีทิศทางที่ชัด รอข้อมูลงบ/ราคาเพิ่มก่อน",
}


def _easy(res):
    """สรุปง่ายๆ ภาษาคน: ตอนนี้เป็นแบบไหน · ธุรกิจ/ราคา/แรงขาย/มูลค่า · ดูอะไรต่อ"""
    m, V = res["m"], res["verdict"]
    top = V["top"]
    P = lambda x, d=0: "—" if x is None else ("%+." + str(d) + "f%%") % x
    sc = {s["key"]: s["score"] for s in res["scen"]}
    ic, big, col, say, nx, _k = headline(res)
    trend = _TREND.get(_k, "")
    # --- ข้อเท็จจริง 4 ช่อง
    if m["lens_n"] >= 3:
        bn = {"quality": "คุณภาพกำไร", "margin": "มาร์จิ้น", "forward": "แนวทางข้างหน้า", "cash": "เงินสด", "surprise": "ทำเกินคาด"}
        if m["lens_bad"] == 0:
            biz = "✅ ยังแข็งแรง — งบเสีย 0 จาก %d ด้าน" % m["lens_n"]
        elif m["lens_bad"] == 1:
            biz = "🔸 มีจุดอ่อน 1 ด้าน (%s) จาก %d ด้าน" % (bn[m["bad_names"][0]], m["lens_n"])
        else:
            biz = "⚠️ อ่อนลง — งบเสีย %d จาก %d ด้าน (%s)" % (m["lens_bad"], m["lens_n"], ", ".join(bn[k] for k in m["bad_names"]))
    else:
        biz = "— ข้อมูลงบไม่พอ (มี %d จาก 5 ด้าน) บอกไม่ได้ว่าธุรกิจเสียหรือไม่" % m["lens_n"]
    stg = m["stage"]
    trend = ""
    if stg:
        trend = " · แนวโน้มใหญ่: %s" % {1: "พักฐาน", 2: "ยังขึ้น", 3: "ใกล้ยอด", 4: "ขาลง"}[stg["stage"]]
    price = "ลง %.0f%% จากจุดสูง 52 สัปดาห์%s" % (abs(m["dd52"]), trend)
    if m["run"] is not None and m["run"] >= 20:
        price += " · ก่อนหน้านั้นวิ่งมา %s" % P(m["run"], 0)
    heavy = (m["dist"] >= 4) or (m["dn_up"] is not None and m["dn_up"] >= 1.25)
    sell = ("%s แรงขายหนาแน่น" if heavy else "%s แรงขายปกติ") % ("⚠️" if heavy else "✅")
    sell += " — วันขายหนัก %d ใน 25 วัน" % m["dist"] + ("" if m["dn_up"] is None else " · วอลุ่มวันลง ≈ %.1f เท่าของวันขึ้น" % m["dn_up"])
    vs = sc.get("valuation")
    val = "— ไม่มีข้อมูลพอ" if vs is None else ("⚠️ ค่อนข้างแพง" if vs >= 60 else ("🔸 ค่อนข้างสูง" if vs >= 35 else "✅ ไม่แพงนัก"))
    if vs is not None and m["fpe"]:
        val += " — P/E ล่วงหน้า %.1f" % m["fpe"]
    facts = [("ธุรกิจ", biz), ("ราคา", price), ("แรงขาย", sell), ("มูลค่า", val)]
    fh = "".join("<div class='fc'><b>%s</b><span>%s</span></div>" % (_e(a), _e(b)) for a, b in facts)
    # --- ความเชื่อมั่น (ภาษาคน)
    cf = {"สูง": "เชื่อถือได้ค่อนข้างดี", "กลาง": "พอใช้ประกอบการตัดสินใจ แต่อย่าฟันธง", "ต่ำ": "ใช้เป็นแค่ข้อสังเกต"}[res["conf"]]
    sec = ""
    if top is not None and not V["mixed"] and V["second"] is not None and V["second"]["score"] >= 60 and m["correction"] and not V["none"]:
        sec = " · ภาพรองที่ใกล้เคียง: <b>%s</b> (%.0f คะแนน) — สองภาพนี้เป็นจริงพร้อมกันได้" % (_e(V["second"]["th"]), V["second"]["score"])
    nxh = "".join("<li>%s</li>" % _e(x) for x in nx)
    return ("<div class='easy' style='--c:%s'><div class='k'>สรุปง่ายๆ · อ่านแค่ตรงนี้ก็พอ</div><div class='big'>%s %s</div><div class='say'>%s</div>"
            "<div class='facts'>%s</div><div class='nx'><b>ความเชื่อมั่น: %s</b> — %s%s</div>"
            "%s<div class='nx'><b>ดูอะไรต่อ</b><ul style='margin:4px 0 0 18px;padding:0'>%s</ul></div>"
            "<div class='mem'>จำสั้นๆ: ราคาลง ≠ ธุรกิจเสีย · นี่คือการประเมินจากตัวเลข ไม่ใช่การยืนยันสาเหตุ และไม่ใช่คำแนะนำซื้อขาย</div></div>"
            % (col, ic, _e(big), _e(say), fh, res["conf"], cf, sec,
               ("<div class='nx'><b>ถ้าเป็นแบบนี้ต่อไป (จากตัวเลข ไม่ใช่ทำนาย)</b> %s</div>" % _e(trend)) if trend else "", nxh))


def build_html(res, sym=""):
    m, V = res["m"], res["verdict"]
    P = lambda x, d=0: "—" if x is None else ("%+." + str(d) + "f%%") % x
    ath_d = m["ath_date"].strftime("%m/%Y") if hasattr(m["ath_date"], "strftime") else ""
    chips = [("ราคาล่าสุด", "%.2f" % m["px"]), ("จุดสูงสุดตลอดกาล", "%.2f (%s)" % (m["ath"], ath_d)), ("ห่างจากจุดสูงสุดตลอดกาล", P(m["dd_ath"], 1)),
             ("ห่างจากจุดสูง 52 สัปดาห์", P(m["dd52"], 1)), ("3 เดือน", "%s · SPY %s" % (P(m["r3"]), P(m["spy3"]))),
             ("6 เดือน", "%s · SPY %s" % (P(m["r6"]), P(m["spy6"]))), ("12 เดือน", "%s · SPY %s" % (P(m["r12"]), P(m["spy12"])))]
    h = ["<div class='dx'>", _easy(res), "<div class='hud'><div class='chips'>" + "".join("<div class='chip'>%s<b>%s</b></div>" % (_e(a), _e(b)) for a, b in chips) + "</div>",
         "<div class='note' style='margin-top:6px'>ราคาที่ใช้ปรับปันผล/แตกพาร์แล้ว จุดสูงสุดตลอดกาลวัดจากข้อมูลย้อนหลังเท่าที่ Yahoo มี (%.0f ปี)</div></div>" % m["years"]]
    cc = {"สูง": "#19f5a5", "กลาง": "#fcee0a", "ต่ำ": "#ff9f43"}[res["conf"]]
    top = V["top"]
    if top is None or (V["none"] and m["correction"]):
        why = "ข้อมูลที่ดึงได้น้อยเกินไปจะแยกสาเหตุได้อย่างน่าเชื่อถือ" if top is None else "ไม่มีภาพใดได้คะแนนถึง 35/100 — หลักฐานไม่ชี้ไปทางไหนชัดๆ ห้ามเดาสาเหตุ"
        if m["lens_n"] < 3:
            why += " · ข้อมูลงบมีแค่ %d จาก 5 ด้าน จึงยังบอกไม่ได้ว่าธุรกิจมีปัญหาหรือไม่" % m["lens_n"]
        h.append("<div class='ver' style='--c:#ff9f43'><div class='k'>VERDICT · DROP DIAGNOSIS</div><div class='t'>ยังสรุปสาเหตุไม่ได้<small>ความเชื่อมั่น: ต่ำ</small></div><p>%s</p></div>" % _e(why))
    else:
        if not m["correction"]:
            title, sub = "ยังไม่ได้ปรับฐานชัดเจน", "ราคายังอยู่ใกล้จุดสูง (ห่าง %s)" % P(m["dd52"], 1)
            body = ("ตอนนี้ไม่มีการลงที่ต้องอธิบาย จึงไม่ตัดสินว่าเป็นการพักฐานหรือไม่ · สิ่งที่ควรดูตอนราคาอยู่สูงคือ <b>ความเสี่ยงด้านมูลค่า</b> (คะแนนด้านล่าง) "
                    "เพราะถ้าเกิดปรับฐาน หุ้นที่แพงมักลงแรงกว่า")
            col = "#00f0ff"
        else:
            col = top["col"]
            if V["mixed"]:
                title, sub = "%s + %s" % (top["th"], V["second"]["th"]), "ผสมกัน — คะแนน %.0f และ %.0f ใกล้กันมาก" % (top["score"], V["second"]["score"])
            else:
                title, sub = top["th"], "%s · คะแนน %.0f/100" % (top["en"], top["score"])
            body = {
                "healthy": "ราคาลงแต่พื้นฐานและแนวโน้มใหญ่ยังไม่เสีย แรงขายไม่หนาแน่น — เข้าข่ายพักฐานตามปกติมากที่สุด",
                "profit": "หุ้นวิ่งแรงมาก่อน แล้วเพิ่งถูกขายลงพร้อมวอลุ่มที่หนาแน่น ขณะที่พื้นฐานยังไม่เสีย — เข้าข่ายแรงขายทำกำไรมากที่สุด",
                "valuation": "ราคาสูงเมื่อเทียบพื้นฐานและเมื่อเทียบหุ้นในกลุ่ม ทำให้เปราะต่อการปรับฐาน — เข้าข่ายความเสี่ยงด้านมูลค่ามากที่สุด",
                "fund": "เลนส์งบหลายด้านอ่อนลงและแนวโน้มราคาตามมา — เข้าข่ายพื้นฐานธุรกิจอ่อนแอลงมากที่สุด ควรตรวจงบรายตัวก่อนตัดสินใจ",
            }[top["key"]]
            if V["mixed"]:
                body += " · อีกภาพที่ใกล้เคียง: " + V["second"]["th"]
        why_low = ""
        if res["conf"] == "ต่ำ":
            why_low = " · เหตุผล: ข้อมูลบางส่วนหายหรือคะแนนของภาพต่างๆ ใกล้กัน"
        if m["lens_n"] < 3:
            why_low += " · ข้อมูลงบไม่พอ (มีเลนส์งบ %d จาก 5) จึงแยก \"ราคาลง\" ออกจาก \"ธุรกิจมีปัญหา\" ได้ไม่เต็มที่" % m["lens_n"]
        h.append("<div class='ver' style='--c:%s'><div class='k'>รายละเอียดทางเทคนิค · VERDICT</div><div class='t'>%s<small>%s</small></div>"
                 "<span class='conf' style='--c:%s'>ความเชื่อมั่น: %s</span><span class='note'>ข้อมูลครอบคลุม %.0f%%%s</span><p>%s</p></div>"
                 % (col, _e(title), _e(sub), cc, res["conf"], res["cov"] * 100, _e(why_low), body))
    # ---- 4 ภาพ
    for s in res["scen"]:
        sc = s["score"]
        rows = ""
        for r in s["rules"]:
            rows += ("<div class='row'><div>%s</div><div>%s<small>%s</small></div><div class='v'>%s</div></div>"
                     % (_sym_of(r["s"]), _e(r["label"]), _e(r["why"]), _e(r["val"])))
        h.append("<details style='--c:%s'><summary><div class='nm'>%s<small>%s</small></div><div class='bar'><i style='width:%d%%'></i></div><div class='sc'>%s</div></summary>"
                 "<div class='ev'>%s%s<div class='note'>ข้อมูลครบ %.0f%% ของเกณฑ์ในภาพนี้ · ✅ เข้าข่าย · 🔸 เข้าข่ายบางส่วน · ⚠️ ไม่เข้าข่าย · — ไม่มีข้อมูล (ไม่นับคะแนน)</div></div></details>"
                 % (s["col"], _e(s["th"]), _e(s["en"]), 0 if sc is None else int(sc), "—" if sc is None else "%.0f" % sc, rows,
                    "<div class='note'>⛔ ไม่ให้คะแนนภาพนี้: ต้องมีเลนส์งบอย่างน้อย 3 ด้านก่อน — ราคาลงอย่างเดียวห้ามสรุปว่าธุรกิจเสีย</div>" if s.get("blocked") else "",
                    s["cov"] * 100))
    # ---- ปลายปี
    Y = res["yearend"]
    ycol = {"evidence": "#ff9f43", "partial": "#fcee0a", "none": "#19f5a5", "n/a": "#7d86a6"}[Y["status"]]
    ylab = {"evidence": "มีหลักฐานครบ", "partial": "หลักฐานบางส่วน", "none": "ไม่พบหลักฐาน", "n/a": "ไม่เกี่ยวข้องตอนนี้"}[Y["status"]]
    yi = "".join("<div class='row'><div>%s</div><div>%s</div><div class='v'>%s</div></div>" % ("✅" if ok else "—", _e(a), _e(b)) for a, ok, b in Y["items"])
    hist = ""
    if Y["hist"]:
        hh = Y["hist"]
        hist = ("<p class='note'>ย้อนหลังของหุ้นตัวนี้เอง: ช่วง 10 พ.ย.–31 ธ.ค. ลงมา %d จาก %d ปี เฉลี่ย %+.1f%% — ตัวอย่างน้อยมาก ใช้เป็นแค่บริบท ไม่ใช่หลักฐานว่าปีนี้จะซ้ำ</p>"
                % (hh["neg"], hh["n"], hh["avg"]))
    if Y["status"] == "n/a":
        h.append("<div class='ye' style='--c:%s'><h4>YEAR-END FLOW · แรงขายปรับพอร์ตปลายปี — %s</h4><p>%s</p></div>" % (ycol, ylab, _e(Y["text"])))
    else:
        inner = "%s%s<div class='note'>เว็บมองไม่เห็นคำสั่งปรับพอร์ตของกองทุนจริง จึงใช้ตัวแทนจากราคาและวอลุ่มเท่านั้น</div>" % (yi, hist)
        if Y["status"] == "none":
            inner = "<details style='border:0;background:none;margin:4px 0 0'><summary style='display:block;padding:2px 0;color:#8d97b8;font-size:12.5px'>ดูรายการตรวจ</summary>%s</details>" % inner
        h.append("<div class='ye' style='--c:%s'><h4>YEAR-END FLOW · แรงขายปรับพอร์ตปลายปี — %s</h4><p>%s</p>%s</div>" % (ycol, ylab, _e(Y["text"]), inner))
    h.append("<div class='note'>ข้อจำกัด: เกณฑ์ทั้งหมดเป็นกฎหัวแม่มือ ไม่ใช่มาตรฐานตลาด · \"กลุ่มเดียวกัน\" ใช้ ETF ของกลุ่มเป็นตัวแทน (ไม่ได้ดูหุ้นแต่ละตัวในกลุ่ม) · "
             "ไม่มีค่า P/E เฉลี่ยย้อนหลังของหุ้นตัวนี้ จึงเทียบกับหุ้นในกลุ่มแทน · ผลนี้ไม่ใช่คำแนะนำซื้อขาย</div></div>")
    return "".join(h)


# ---------------------------------------------------------------- ต่อกับ Streamlit
if st is not None:
    @st.cache_data(ttl=3600, show_spinner=False)
    def _hist(sym):
        d = yf.download(sym, period="max", interval="1d", auto_adjust=True, progress=False)
        if d is None or d.empty:
            return None
        if hasattr(d.columns, "levels"):
            d.columns = [c[0] if isinstance(c, tuple) else c for c in d.columns]
        d = d[["Close", "Volume"]].dropna(subset=["Close"])
        d.index = pd.to_datetime(d.index).tz_localize(None)
        return d

    @st.cache_data(ttl=3600, show_spinner=False)
    def _bench(etf):
        names = ["SPY", "QQQ"] + ([etf] if etf and etf not in ("SPY", "QQQ") else [])
        d = yf.download(" ".join(names), period="2y", interval="1d", group_by="ticker", auto_adjust=True, progress=False)
        out = {}
        for n in names:
            try:
                out[n] = d[n]["Close"].dropna()
            except Exception:
                pass
        b = {"SPY": out.get("SPY"), "QQQ": out.get("QQQ"), "SEC": out.get(etf) if etf else None}
        return b


    @st.cache_data(ttl=6 * 3600, show_spinner=False)
    def _peer(sym, sector_key):
        import drivers
        return drivers._peer_forward_pe({"sectorKey": sector_key}, sym)


def run(sym, D=None, lenses=None):
    """ดึงข้อมูล (แคช 1 ชม.) แล้ววิเคราะห์ · ใช้ร่วมกันทั้งกล่องวินิจฉัยและบรรทัดสรุปด้านบน เพื่อให้ผลตรงกันเสมอ"""
    import insight
    df = _hist(sym)
    if df is None:
        return None
    D = D or insight._load(sym)
    info = D.get("info") or {}
    lenses = lenses or insight.build_lenses(D)
    stances = {l["key"]: l["stance"] for l in lenses}
    bench = _bench(insight._sector_etf(info, sym))
    peer = None
    try:
        if info.get("sectorKey"):
            peer = _peer(sym, info.get("sectorKey"))
    except Exception:
        peer = None
    return analyze(df, bench, info, stances, peer)


def summary_line(sym, D=None, lenses=None):
    """บรรทัดเดียวสำหรับกล่องสรุปบนสุด: ราคาลงเพราะอะไร (คืน None ถ้าไม่ได้ปรับฐาน/ข้อมูลไม่พอ)"""
    if st is None or yf is None:
        return None
    res = run(sym, D, lenses)
    if not res or not res["m"]["correction"]:
        return None
    m, V = res["m"], res["verdict"]
    base = "ราคาลงเพราะอะไร: ลง %.0f%% จากจุดสูง 52 สัปดาห์" % abs(m["dd52"])
    if V["top"] is None or V["none"]:
        return base + " · หลักฐานยังไม่ชี้ชัดว่าเป็นเพราะอะไร (ความเชื่อมั่นต่ำ) — ดูกล่อง \"วินิจฉัยการปรับฐาน\" ด้านล่าง"
    t = "ภาพที่ใกล้เคียงที่สุดคือ \"%s\"" % V["top"]["th"]
    if V["mixed"]:
        t += " ผสมกับ \"%s\"" % V["second"]["th"]
    return base + " · %s (คะแนน %.0f/100, ความเชื่อมั่น%s) — เป็นการประเมินจากตัวเลข ไม่ใช่การยืนยันสาเหตุ · ดูหลักฐานในกล่องด้านล่าง" % (t, V["top"]["score"], res["conf"])


def render(sym):
    """แสดงกล่องวินิจฉัยการปรับฐานของ sym (เรียกจากหน้า Deep Insight · พลาดตรงไหนข้ามเงียบๆ ไม่กระทบหน้าหลัก)"""
    if st is None or yf is None:
        return
    try:
        st.markdown('<div class="section-label">◆ วินิจฉัยการปรับฐาน — DROP DIAGNOSIS</div>', unsafe_allow_html=True)
        st.caption("ตอบว่าราคาที่ลงจากจุดสูงเป็น \"พักฐานปกติ / ขายทำกำไร / ราคาแพง / พื้นฐานอ่อนลง\" พร้อมตัวเลขและระดับความเชื่อมั่น — ไม่ตัดสินจากราคาลงอย่างเดียว")
        with st.spinner("กำลังวินิจฉัยการปรับฐาน ..."):
            res = run(sym)
        if not res:
            st.info("ข้อมูลราคาย้อนหลังไม่พอสำหรับวินิจฉัย (ต้องมีอย่างน้อยประมาณ 6 เดือน)")
            return
        st.markdown(_CSS + build_html(res, sym), unsafe_allow_html=True)
        with st.expander("📖 วิธีอ่านกล่องนี้ (กันลืม)", expanded=False):
            st.markdown(
                "**อ่านตามลำดับ:** ① แถบตัวเลขด้านบน → ② VERDICT (ภาพที่ใกล้เคียงที่สุด + ความเชื่อมั่น) → ③ กดเปิดแต่ละภาพดูหลักฐาน → ④ กล่องปลายปี\n\n"
                "- **คะแนนแต่ละภาพ** = เกณฑ์ที่เข้าข่ายถ่วงน้ำหนัก ÷ เกณฑ์ที่มีข้อมูล · ภาพเดียวไม่ได้ชนะขาดเสมอ ถ้าคะแนนใกล้กันจะขึ้นว่า \"ผสม\"\n"
                "- **ความเชื่อมั่น** ขึ้นกับข้อมูลครบแค่ไหน และภาพที่ชนะนำภาพอื่นมากแค่ไหน · ต่ำ = ใช้เป็นแค่ข้อสังเกต\n"
                "- **วันขายหนัก** = วันที่ราคาลง ≥0.2% และวอลุ่มสูงกว่าวันก่อน (นับใน 25 วันล่าสุด) · 4 วันขึ้นไปถือว่าหนาแน่น\n"
                "- **ห้ามสรุปเอง:** ถ้าราคาลงแต่ข้อมูลงบไม่พอ ระบบจะไม่ให้ \"พื้นฐานอ่อนแอลง\" ชนะ และจะบอกว่าข้อมูลไม่พอ\n"
                "- **ปลายปี** ใช้อธิบายได้ก็ต่อเมื่อมีหลักฐานครบ 3 ข้อ ไม่งั้นให้ดูเหตุผลอื่น\n\n"
                "**จำสั้นๆ:** *ราคาลง ≠ ธุรกิจเสีย · ดูหลักฐานนอกราคาก่อนเสมอ*")
    except Exception as ex:  # pragma: no cover
        st.caption("ส่วน \"วินิจฉัยการปรับฐาน\" แสดงไม่ได้ตอนนี้: %s" % ex)