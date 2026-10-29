# -*- coding: utf-8 -*-
"""
rocket_ui.py
============
หน้าจอ Watchlist Scanner — ใส่รายชื่อหุ้นเอง กรองด้วย RSI + แนวรับ/แนวต้าน + โมเมนตัม + R:R
เรียกใช้จาก app.py:  rocket_ui.render_scanner(refresh_interval)
"""

import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st

import rocket

GOLD, GREEN, RED, TEXT, GREY = "#d4af37", "#3ecf6e", "#e5534b", "#f4f0e6", "#9a9aa8"
WATCH_FILE = Path(__file__).with_name("watchlist.json")
MAX_SYMBOLS = 40

PRESETS = {
    "📋 ทั้งหมด": (lambda r: True, "mom"),
    "🟢 ใกล้แนวรับ + RSI ต่ำ (จังหวะเด้ง)": (lambda r: r["dist_sup"] is not None and r["dist_sup"] <= 3 and r["rsi_d"] <= 40, "rebound"),
    "🚀 ใกล้/ทะลุแนวต้าน + โมเมนตัมแรง (จังหวะทะลุ)": (
        lambda r: (r["broke_up"] or (r["dist_res"] is not None and r["dist_res"] <= 2)) and (r["mom"] or 0) >= 60, "breakout"),
    "💪 เขียวสวนตลาดแดง": (lambda r: r["mkt_red_green"], "spread"),
    "⭐ โมเมนตัมแรงสุด": (lambda r: (r["mom"] or 0) >= 60, "mom"),
    "⚠️ ระวัง RSI ร้อน / หลุดต่ำสุด 20 วัน": (lambda r: r["rsi_d"] >= 70 or r["broke_dn"], "rsi_hot"),
}

SORTS = {
    "ตามพรีเซ็ต": None,
    "คะแนนเด้ง (มาก→น้อย)": ("rebound", True),
    "คะแนนทะลุ (มาก→น้อย)": ("breakout", True),
    "โมเมนตัม (มาก→น้อย)": ("mom", True),
    "RSI รายวัน (ต่ำ→สูง)": ("rsi_d", False),
    "ใกล้แนวรับสุด": ("dist_sup", False),
    "R:R สูงสุด": ("rr", True),
    "% วันนี้ (มาก→น้อย)": ("chg", True),
}


def _show_df(df, **kw):
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


# ---------------------------------------------------------------
# รายชื่อ watchlist (เก็บไฟล์ watchlist.json ข้าง app.py)
# ---------------------------------------------------------------
def _load_watch() -> list:
    try:
        data = json.loads(WATCH_FILE.read_text(encoding="utf-8"))
        if isinstance(data, list) and data:
            return [str(x) for x in data]
    except Exception:
        pass
    return list(rocket.DEFAULT_WATCHLIST)


def _save_watch(symbols: list) -> bool:
    try:
        WATCH_FILE.write_text(json.dumps(symbols, ensure_ascii=False), encoding="utf-8")
        return True
    except Exception:
        return False


def _parse(text: str) -> list:
    out = []
    for tok in re.split(r"[,\s;]+", text.upper()):
        tok = tok.strip()
        if tok and re.fullmatch(r"[A-Z0-9.\-]{1,10}", tok) and tok not in out:
            out.append(tok)
    return out


def _reset_text():
    st.session_state["rk_text"] = ", ".join(rocket.DEFAULT_WATCHLIST)


@st.cache_data(ttl=900, show_spinner=False)
def _daily_cached(symbols_tuple):
    return rocket.load_daily(symbols_tuple)


@st.cache_data(ttl=120, show_spinner=False)
def _hourly_cached(symbols_tuple):
    return rocket.load_hourly(symbols_tuple)


# ---------------------------------------------------------------
# คำอธิบายสอนวิธีอ่าน
# ---------------------------------------------------------------
def _render_guide():
    with st.expander("📖 วิธีใช้และวิธีอ่านตารางนี้ (อ่าน 1 นาที)", expanded=False):
        st.markdown(
            """
**หน้านี้ทำอะไร:** ใส่รายชื่อหุ้นที่สนใจ แล้วแอปคำนวณ **แนวรับ/แนวต้าน + RSI + โมเมนตัม** ให้ทุกตัวพร้อมกัน แล้วกรองเอาเฉพาะตัวที่เข้าเงื่อนไขที่คุณตั้ง

**ใช้ 3 ขั้น**
1. **ใส่รายชื่อหุ้น** (คั่นด้วยคอมมา) แล้วกด 💾 บันทึก ครั้งหน้าเปิดมาก็ยังอยู่
2. **เลือกพรีเซ็ต** เช่น "จังหวะเด้ง" หรือ "จังหวะทะลุ" (หรือปรับตัวกรองเองด้านล่าง)
3. **ดูตารางและกดเลือกหุ้น** เพื่อดูกราฟพร้อมเส้นแนวรับ/แนวต้านและสรุปเป็นประโยค

**คำศัพท์ที่ต้องรู้**
- **แนวรับ** = ระดับราคาที่ราคาเคยหยุดลงและเด้งกลับ · **แนวต้าน** = ระดับที่เคยขึ้นไปชนแล้วถูกขายลงมา
- **ความแข็ง** = มีหลักฐานซ้อนกันหลายอย่างในระดับนั้น (เช่น เคยกลับตัวหลายครั้ง + ตรงกับ SMA200) ยิ่งซ้อนมาก ยิ่ง "แข็ง" (พอใช้ → แข็ง → แข็งมาก)
- **RSI** วัดว่าราคาขึ้น/ลงเร็วแค่ไหน · ต่ำกว่า 30 = ขายหนักแล้ว (อาจเด้ง) · สูงกว่า 70 = ซื้อหนักแล้ว (อาจพัก) · มี 2 ค่า: รายวัน และรายชั่วโมง (ไวกว่า)
- **R:R** = กำไรที่หวังได้ (ระยะถึงแนวต้าน) ÷ ความเสี่ยง (ระยะถึงแนวรับ) · เกิน 2 ถือว่าคุ้มกว่า แต่ต้องมีแนวรับที่ยืนได้จริง
- **โมเมนตัม** = คะแนน 0-100 จากงานวิจัย (คำนวณแบบเดียวกับหน้าวิเคราะห์รายตัว)
- **คะแนนเด้ง** = ใกล้แนวรับ + RSI ต่ำ + R:R ดี + ยังอยู่เหนือ SMA200 · **คะแนนทะลุ** = ใกล้/ทะลุแนวต้าน + โมเมนตัมแรง + ปริมาณ + RSI 50-70

**พรีเซ็ตที่มีให้**

| พรีเซ็ต | เงื่อนไข |
|---|---|
| 🟢 จังหวะเด้ง | ห่างแนวรับไม่เกิน 3% และ RSI รายวัน ≤ 40 |
| 🚀 จังหวะทะลุ | ใกล้แนวต้านไม่เกิน 2% หรือทะลุสูงสุด 20 วัน และโมเมนตัม ≥ 60 |
| 💪 เขียวสวนตลาดแดง | SPY ลบ ≥ 0.3% แต่หุ้นตัวนั้นเขียว |
| ⚠️ ระวัง | RSI ≥ 70 หรือหลุดต่ำสุด 20 วัน |

⚠️ **ข้อควรรู้:** แนวรับ/แนวต้านคือ "โซนที่ราคาเคยมีปฏิกิริยา" ไม่ใช่เส้นที่ราคาจะหยุดแน่นอน หลุดแนวรับได้เสมอ · คะแนนเด้ง/ทะลุเป็นกฎหัวแม่มือ **ไม่ได้ผ่านการทดสอบว่าให้ผลดีกว่าเดาสุ่ม** · ข้อมูลฟรีอาจดีเลย์ราว 15 นาที ปริมาณวันนี้ระหว่างตลาดเปิดยังไม่ครบ · ใช้ตารางนี้เพื่อ "คัดตัวที่น่าสนใจ" แล้วศึกษาต่อ ไม่ใช่คำสั่งซื้อ-ขาย
"""
        )


# ---------------------------------------------------------------
# ผลลัพธ์ (อยู่ใน fragment อัปเดตอัตโนมัติได้)
# ---------------------------------------------------------------
def _render_results(symbols: tuple, params: dict):
    syms_all = tuple(list(symbols) + ["SPY"])
    with st.spinner(f"กำลังคำนวณ {len(symbols)} ตัว..."):
        daily = _daily_cached(syms_all)
        hourly = _hourly_cached(syms_all)
        rows, spy_chg = rocket.build_rows(list(symbols), daily, hourly)

    missing = [s for s in symbols if s not in daily]
    if not rows:
        st.error("ดึงข้อมูลไม่สำเร็จสักตัว (ตรวจรหัสหุ้นและอินเทอร์เน็ต หรืออาจโดน rate-limit ชั่วคราว)")
        return

    if spy_chg is not None:
        if spy_chg <= -0.3:
            st.error(f"🔴 วันนี้ตลาดแดง (SPY {spy_chg:+.2f}%) — ตัวที่ติด 💪 คือเขียวสวนตลาด")
        elif spy_chg >= 0.3:
            st.success(f"🟢 วันนี้ตลาดเขียว (SPY {spy_chg:+.2f}%)")
        else:
            st.info(f"⚪ ตลาดแกว่งปกติ (SPY {spy_chg:+.2f}%)")

    pred, preset_sort = PRESETS[params["preset"]]

    def passes(r):
        if not pred(r):
            return False
        if not (params["rsi_d"][0] <= r["rsi_d"] <= params["rsi_d"][1]):
            return False
        if params["rsi_h"] != (0, 100):
            if r["rsi_h"] is None or not (params["rsi_h"][0] <= r["rsi_h"] <= params["rsi_h"][1]):
                return False
        if params["max_sup"] < 20 and (r["dist_sup"] is None or r["dist_sup"] > params["max_sup"]):
            return False
        if params["min_res"] > 0 and (r["dist_res"] is None or r["dist_res"] < params["min_res"]):
            return False
        if params["min_rr"] > 0 and (r["rr"] is None or r["rr"] < params["min_rr"]):
            return False
        if params["min_mom"] > 0 and (r["mom"] or 0) < params["min_mom"]:
            return False
        if params["only200"] and not r["above200"]:
            return False
        if params["only_green"] and r["chg"] <= 0:
            return False
        return True

    shown = [r for r in rows if passes(r)]

    # ----- เรียงลำดับ -----
    sort_cfg = SORTS[params["sort"]]
    if sort_cfg is None:
        key, desc = {"mom": ("mom", True), "rebound": ("rebound", True), "breakout": ("breakout", True),
                     "spread": ("spread", True), "rsi_hot": ("rsi_d", True)}[preset_sort]
    else:
        key, desc = sort_cfg

    def sort_val(r):
        v = r.get(key)
        return (-1e9 if desc else 1e9) if v is None else v

    shown.sort(key=sort_val, reverse=desc)

    st.markdown(f"**ผ่านเงื่อนไข {len(shown)} จาก {len(rows)} ตัว**" + (f" · ดึงข้อมูลไม่ได้: {', '.join(missing)}" if missing else ""))
    if not shown:
        st.caption("ไม่มีหุ้นที่ผ่านเงื่อนไขตอนนี้ ลองผ่อนตัวกรอง หรือเลือกพรีเซ็ต 📋 ทั้งหมด")
        return

    df = pd.DataFrame([{
        "หุ้น": r["symbol"],
        "ราคา": round(r["price"], 2),
        "วันนี้ %": round(r["chg"], 2),
        "RSI วัน": round(r["rsi_d"]),
        "RSI 1ชม.": None if r["rsi_h"] is None else round(r["rsi_h"]),
        "แนวรับ": None if not r["sup"] else round(r["sup"]["price"], 2),
        "รับ ห่าง %": None if r["dist_sup"] is None else round(r["dist_sup"], 1),
        "รับ แข็ง": "" if not r["sup"] else rocket.strength_label(r["sup"]["strength"]),
        "แนวต้าน": None if not r["res"] else round(r["res"]["price"], 2),
        "ต้าน ห่าง %": None if r["dist_res"] is None else round(r["dist_res"], 1),
        "ต้าน แข็ง": "" if not r["res"] else rocket.strength_label(r["res"]["strength"]),
        "R:R": None if r["rr"] is None else round(r["rr"], 1),
        "โมเมนตัม": r["mom"],
        "เด้ง": r["rebound"],
        "ทะลุ": r["breakout"],
        "สัญญาณ": " · ".join(r["flags"]),
    } for r in shown])

    _show_df(
        df, hide_index=True,
        column_config={
            "โมเมนตัม": st.column_config.ProgressColumn("โมเมนตัม", min_value=0, max_value=100, format="%d"),
            "เด้ง": st.column_config.ProgressColumn("เด้ง", min_value=0, max_value=100, format="%d",
                                                   help="คะแนนจังหวะเด้ง: ใกล้แนวรับ + RSI ต่ำ + R:R ดี (กฎหัวแม่มือ)"),
            "ทะลุ": st.column_config.ProgressColumn("ทะลุ", min_value=0, max_value=100, format="%d",
                                                   help="คะแนนจังหวะทะลุ: ใกล้/ทะลุแนวต้าน + โมเมนตัม + ปริมาณ (กฎหัวแม่มือ)"),
            "ราคา": st.column_config.NumberColumn("ราคา", format="%.2f"),
            "แนวรับ": st.column_config.NumberColumn("แนวรับ", format="%.2f"),
            "แนวต้าน": st.column_config.NumberColumn("แนวต้าน", format="%.2f"),
        },
    )
    st.caption("ราคาและ RSI 1ชม. มาจากแท่งรายชั่วโมงล่าสุด (ดีเลย์ได้) · แนวรับ/แนวต้านคำนวณจากรายวัน 1 ปี · คะแนนเป็นกฎหัวแม่มือ ไม่ใช่คำแนะนำซื้อ-ขาย")

    # ----- รายละเอียดหุ้นที่เลือก -----
    st.markdown("#### 🔎 ดูรายละเอียดหุ้น")
    pick = st.selectbox("เลือกหุ้น", [r["symbol"] for r in shown], key="rk_detail")
    r = next(x for x in shown if x["symbol"] == pick)

    st.markdown(f"**{r['symbol']}** — {rocket.plain_summary(r)}")
    if r["flags"]:
        st.caption("สัญญาณ: " + " · ".join(r["flags"]))

    # กราฟ + เส้นแนวรับ/แนวต้านที่สำคัญ
    hist = r["history"]["Close"].astype(float).tail(130)
    price = r["price"]
    sig = [x for x in r["levels"] if x["strength"] >= 2.0 and abs(x["dist_pct"]) <= 20]
    sups = sorted([x for x in sig if x["kind"] == "support"], key=lambda x: -x["price"])[:3]
    ress = sorted([x for x in sig if x["kind"] == "resistance"], key=lambda x: x["price"])[:3]
    chart = pd.DataFrame({"ราคา": hist})
    colors = [TEXT]
    for i, x in enumerate(sups):
        chart[f"แนวรับ {x['price']:,.2f}"] = x["price"]
        colors.append(["#3ecf6e", "#7ddc9b", "#2a9d56"][i])
    for i, x in enumerate(ress):
        chart[f"แนวต้าน {x['price']:,.2f}"] = x["price"]
        colors.append(["#e5534b", "#ee8a84", "#b83a33"][i])
    st.line_chart(chart, color=colors, height=320)

    if sig:
        kind_th = {"support": "🟢 แนวรับ", "resistance": "🧱 แนวต้าน", "at": "📍 ราคาอยู่ในโซนนี้"}
        lv = pd.DataFrame([{
            "ประเภท": kind_th[x["kind"]],
            "ราคา": round(x["price"], 2),
            "ห่างจากราคาตอนนี้ %": round(x["dist_pct"], 1),
            "ความแข็ง": f"{rocket.strength_label(x['strength'])} ({x['strength']:.1f})",
            "ประกอบด้วย": x["label"],
        } for x in sorted(sig, key=lambda x: -x["price"])])
        _show_df(lv, hide_index=True)
        st.caption("ความแข็ง: ผลรวมน้ำหนักหลักฐานในโซนนั้น (จุดกลับตัวที่ใหม่กว่าน้ำหนักมากกว่า, SMA200 และจุดสูง/ต่ำ 52 สัปดาห์น้ำหนักสูง)")


# ---------------------------------------------------------------
# หน้าหลัก
# ---------------------------------------------------------------
def render_scanner(refresh_interval=None):
    _render_guide()

    if "rk_text" not in st.session_state:
        st.session_state["rk_text"] = ", ".join(_load_watch())

    st.markdown("**📝 รายชื่อหุ้น (Watchlist)**")
    st.text_area("พิมพ์รหัสหุ้น คั่นด้วยคอมมาหรือเว้นวรรค", key="rk_text", height=80, label_visibility="collapsed",
                 placeholder="เช่น NVDA, AAPL, MU, TSLA")
    symbols = _parse(st.session_state["rk_text"])
    cut = len(symbols) > MAX_SYMBOLS
    symbols = symbols[:MAX_SYMBOLS]

    b1, b2, b3 = st.columns([1, 1, 4])
    if b1.button("💾 บันทึก", key="rk_save"):
        ok = _save_watch(symbols)
        (b3.success if ok else b3.warning)(f"บันทึก {len(symbols)} ตัวแล้ว" if ok else "บันทึกไฟล์ไม่ได้ (ไม่มีสิทธิ์เขียนไฟล์ในโฟลเดอร์)")
    b2.button("↺ รายชื่อตั้งต้น", key="rk_reset", on_click=_reset_text)
    st.caption(f"{len(symbols)} ตัว (สูงสุด {MAX_SYMBOLS})" + (" · ตัดส่วนเกินออกแล้ว" if cut else ""))

    if not symbols:
        st.info("ใส่รหัสหุ้นอย่างน้อย 1 ตัวด้านบนครับ")
        return

    st.markdown("**🎯 ตัวกรอง**")
    c1, c2 = st.columns(2)
    preset = c1.selectbox("พรีเซ็ต", list(PRESETS.keys()), key="rk_preset")
    sort = c2.selectbox("เรียงตาม", list(SORTS.keys()), key="rk_sort")

    with st.expander("⚙️ ตัวกรองละเอียด (ไม่บังคับ)", expanded=False):
        f1, f2 = st.columns(2)
        rsi_d = f1.slider("RSI รายวัน", 0, 100, (0, 100), key="rk_rsi_d")
        rsi_h = f2.slider("RSI รายชั่วโมง", 0, 100, (0, 100), key="rk_rsi_h")
        g1, g2, g3, g4 = st.columns(4)
        max_sup = g1.slider("ห่างแนวรับไม่เกิน (%)", 0.0, 20.0, 20.0, 0.5, key="rk_max_sup", help="เลื่อนสุดขวา = ไม่กรอง")
        min_res = g2.slider("ห่างแนวต้านอย่างน้อย (%)", 0.0, 20.0, 0.0, 0.5, key="rk_min_res", help="ใช้หาตัวที่ยังมีที่ว่างให้ขึ้น")
        min_rr = g3.slider("R:R ขั้นต่ำ", 0.0, 5.0, 0.0, 0.1, key="rk_min_rr")
        min_mom = g4.slider("โมเมนตัมขั้นต่ำ", 0, 100, 0, key="rk_min_mom")
        h1, h2 = st.columns(2)
        only200 = h1.checkbox("เฉพาะที่ราคาอยู่เหนือ SMA200", key="rk_only200")
        only_green = h2.checkbox("เฉพาะที่วันนี้เขียว", key="rk_only_green")
        st.caption("ตัวกรองทั้งหมดทำงานร่วมกับพรีเซ็ต (ต้องผ่านทุกข้อ) · ค่าเริ่มต้นคือไม่กรอง")

    params = {
        "preset": preset, "sort": sort, "rsi_d": tuple(rsi_d), "rsi_h": tuple(rsi_h),
        "max_sup": max_sup, "min_res": min_res, "min_rr": min_rr, "min_mom": min_mom,
        "only200": only200, "only_green": only_green,
    }

    if refresh_interval:
        st.caption(f"🔄 อัปเดตอัตโนมัติทุก {refresh_interval.replace('s', '')} วินาที (ปรับได้ที่แถบซ้าย) — ข้อมูลรายวันแคช 15 นาที, รายชั่วโมงแคช 2 นาที")
    st.fragment(_render_results, run_every=refresh_interval)(tuple(symbols), params)