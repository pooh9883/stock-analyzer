# -*- coding: utf-8 -*-
"""
momentum_ui.py
==============
หน้าจอ Streamlit สำหรับโมเมนตัม + โซน "หุ้นเขียว ตลาดแดง" พร้อมคำอธิบายสอนวิธีอ่านในหน้าเว็บ

ฟังก์ชันที่ app.py เรียกใช้:
- render_green_red_guide()         กล่องสอนวิธีอ่าน "หุ้นเขียว ตลาดแดง" (พับได้)
- render_zone_settings() -> dict   ช่องปรับเกณฑ์โซน คืนค่า params
- render_zone_card(stock, market, params)  การ์ดโซนใหญ่ ๆ
- render_scorecard(ticker)         สกอร์การ์ดโมเมนตัมของหุ้น 1 ตัว (มีคำอธิบาย + ปรับค่าได้)
- render_scan(symbols)             จัดอันดับโมเมนตัมหลายตัว
"""

import pandas as pd
import streamlit as st

import momentum

GOLD, GREEN, RED, TEXT, GREY = "#d4af37", "#3ecf6e", "#e5534b", "#f4f0e6", "#9a9aa8"


def _show_df(df, **kw):
    """st.dataframe แบบเต็มความกว้าง รองรับทั้ง Streamlit รุ่นเก่า (use_container_width) และรุ่นใหม่ (width="stretch")"""
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


def _html(s: str) -> str:
    """ลบการเว้นวรรคหน้าบรรทัดและบรรทัดว่าง กัน markdown มองเป็นโค้ดบล็อก"""
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


@st.cache_data(ttl=600, show_spinner=False)
def _cached_scorecard(ticker, benchmark, skip, weights_tuple):
    w = dict(zip(["rs", "trend", "high52", "consistency", "risk"], weights_tuple))
    return momentum.momentum_scorecard(ticker, benchmark=benchmark, skip_recent_month=skip, weights=w)


@st.cache_data(ttl=900, show_spinner=False)
def _cached_scan(symbols_tuple, benchmark, skip):
    return momentum.momentum_scan(list(symbols_tuple), benchmark=benchmark, skip_recent_month=skip)


# ===============================================================
# หุ้นเขียว ตลาดแดง: คำอธิบาย + ปรับเกณฑ์ + การ์ดโซน
# ===============================================================
def render_green_red_guide():
    with st.expander("📖 วิธีอ่านกล่องนี้ (อ่าน 30 วินาที)", expanded=False):
        st.markdown(
            """
**ไอเดียง่าย ๆ:** ตลาดแดง = คนส่วนใหญ่ขายหุ้น ถ้าหุ้นตัวไหน *ยังเขียวอยู่* แสดงว่ามีคนอยากซื้อมันจริง ๆ จึงถือว่า "แข็งกว่าตลาด"

**ดู 3 ขั้นตามลำดับ**
1. **ดูป้ายใหญ่ก่อน** 🟢 โซนกำลังดี · 🟡 พอใช้ · ⚪ ยังไม่ชัด · 🟠 ระวังไล่ราคา · 🔴 ตลาดแดงหนัก
2. **ดูกล่องเล็กด้านล่าง** ว่าช่วง 30 นาที / 1 ชั่วโมง / 5 วัน หุ้นก็แข็งกว่าตลาดด้วยไหม ยิ่งเขียวหลายช่วงยิ่งน่าเชื่อ เขียววันเดียวอาจเป็นแค่เด้ง
3. **ดูเช็กลิสต์และโมเมนตัมด้านล่าง** ว่าเทรนด์ใหญ่ยังดีไหม

**ตัวเลข "กำลังดี"** (กฎหัวแม่มือ ปรับได้ในช่อง ⚙️)

| | ตลาด (SPY) | หุ้น | ส่วนต่าง |
|---|---|---|---|
| 🟢 กำลังดี | ลบ 0.3% ถึง 1% | บวก 1% ถึง 3% | ≥ 1.5 จุด |
| 🟡 พอใช้ | ลบ 0.3% ถึง 2% | บวก 1% ถึง 6% | ≥ 1.5 จุด |
| 🟠 ระวัง | — | บวกเกิน 6% | ขึ้นแรงเกิน ระวังไล่ราคา |
| 🔴 หนัก | ลบเกิน 2% | — | หุ้นดีก็โดนลากตามได้ |

**ตัวอย่าง**
- ตลาด -0.5% หุ้น +1.5% → 🟢 กำลังดี
- ตลาด +0.2% หุ้น +1.5% → ⚪ ตลาดยังไม่แดงจริง (ขยับนิดเดียวคือแกว่งปกติ)
- ตลาด -0.5% หุ้น +7% → 🟠 ขึ้นแรงเกิน ควรเช็กข่าว
- ตลาด -2.5% หุ้น +1.5% → 🔴 ตลาดแดงหนัก ระวัง

⚠️ ตัวเลขเหล่านี้เป็นกฎหัวแม่มือที่ตั้งขึ้นมา **ไม่ได้ผ่านการพิสูจน์ว่าได้ผลดีกว่าช่วงอื่น** และผลย้อนหลังของหุ้นรายตัวเคยออกมาใกล้โยนเหรียญ ใช้กรองว่า "สัญญาณชัดพอจะสนใจไหม" ไม่ใช่ตัวบอกว่าจะขึ้น
"""
        )


def render_zone_settings() -> dict:
    d = momentum.DEFAULT_ZONE_PARAMS
    with st.expander("⚙️ ปรับเกณฑ์โซน (ไม่บังคับ)", expanded=False):
        c1, c2 = st.columns(2)
        mkt_min = c1.number_input("ตลาดต้องลบอย่างน้อย (%) ถึงนับว่าแดง", 0.0, 3.0, d["mkt_min"], 0.1, key="zone_mkt_min")
        mkt_sweet = c2.number_input("ตลาดลบไม่เกิน (%) จึงเป็นโซนกำลังดี", 0.1, 5.0, d["mkt_sweet_max"], 0.1, key="zone_mkt_sweet")
        mkt_avoid = c1.number_input("ตลาดลบเกิน (%) ถือว่าแดงหนัก", 0.5, 10.0, d["mkt_avoid"], 0.1, key="zone_mkt_avoid")
        stock_min = c2.number_input("หุ้นต้องบวกอย่างน้อย (%)", 0.0, 5.0, d["stock_min"], 0.1, key="zone_stock_min")
        stock_sweet = c1.number_input("หุ้นบวกไม่เกิน (%) จึงเป็นโซนกำลังดี", 0.5, 10.0, d["stock_sweet_max"], 0.1, key="zone_stock_sweet")
        stock_hot = c2.number_input("หุ้นบวกเกิน (%) ถือว่าขึ้นแรงเกิน", 1.0, 20.0, d["stock_hot"], 0.5, key="zone_stock_hot")
        spread_min = c1.number_input("หุ้นต้องแข็งกว่าตลาดอย่างน้อย (จุด)", 0.0, 5.0, d["spread_min"], 0.1, key="zone_spread_min")
        st.caption("ค่าเริ่มต้นคือกฎหัวแม่มือ ปรับตามสไตล์ได้ แต่ยิ่งตั้งเข้มจะยิ่งขึ้นสัญญาณน้อย")
    return {
        "mkt_min": mkt_min, "mkt_sweet_max": mkt_sweet, "mkt_avoid": mkt_avoid,
        "stock_min": stock_min, "stock_sweet_max": stock_sweet, "stock_hot": stock_hot,
        "spread_min": spread_min,
    }


def render_zone_card(stock_pct: float, market_pct: float, params: dict = None, confirm_5d: str = None):
    z = momentum.green_red_zone(stock_pct, market_pct, params)
    c = z["color"]
    extra = f'<div style="color:{GREY};font-size:13px;margin-top:6px;">{confirm_5d}</div>' if confirm_5d else ""
    st.markdown(_html(f"""
        <div style="border:1px solid {c}66;background:linear-gradient(135deg,{c}22,#12141c);border-radius:14px;padding:18px 22px;margin-bottom:10px;">
        <div style="color:{GREY};font-size:12px;letter-spacing:.5px;">สถานการณ์ตอนนี้ (เทียบราคาปิดเมื่อวาน)</div>
        <div style="font-size:26px;font-weight:800;color:{c};margin:4px 0;">{z['icon']} {z['label']}</div>
        <div style="color:{TEXT};font-size:15px;">หุ้น <b>{stock_pct:+.2f}%</b> · ตลาด (SPY) <b>{market_pct:+.2f}%</b> · แข็งกว่าตลาด <b>{z['spread']:+.2f} จุด</b></div>
        <div style="color:#c9c5b8;font-size:14px;margin-top:6px;">{z['detail']}</div>
        {extra}
        </div>
    """), unsafe_allow_html=True)


# ===============================================================
# สกอร์การ์ดโมเมนตัม
# ===============================================================
def _bar_html(diff):
    if diff is None:
        return ""
    width = min(abs(diff), 50) / 50 * 50
    color = GREEN if diff >= 0 else RED
    left = 50 if diff >= 0 else 50 - width
    return (
        f'<div style="position:relative;height:10px;background:#242733;border-radius:5px;width:100%;">'
        f'<div style="position:absolute;left:50%;top:-2px;width:2px;height:14px;background:#5a5d6b;"></div>'
        f'<div style="position:absolute;left:{left}%;width:{width}%;height:10px;background:{color};border-radius:5px;"></div>'
        f'</div>'
    )


def render_scorecard(ticker: str):
    with st.expander("📖 วิธีอ่านโมเมนตัม (อ่าน 30 วินาที)", expanded=False):
        st.markdown(
            """
**โมเมนตัม = หุ้นที่กำลังแข็งแรง มักแข็งแรงต่ออีกพักหนึ่ง** งานวิจัยวิชาการหลายชิ้นพบแบบนี้กับหุ้นจำนวนมาก (เป็นค่าเฉลี่ย ไม่ใช่รับประกันรายตัว)

**ดู 3 ขั้น**
1. **คะแนนใหญ่ 0-100** ยิ่งสูงยิ่งมีแรงส่งตามงานวิจัย (75+ แข็งแรงมาก · 60+ แข็งแรง · 40-60 เป็นกลาง · ต่ำกว่า 40 อ่อน)
2. **ธงเตือน ⚠️** ถ้ามี ให้อ่านก่อนตัดสินใจ เช่น ราคาวิ่งไกลเกินหรือเพิ่งขึ้นแรงใน 1 เดือน
3. **5 ปัจจัย** ดูว่าคะแนนมาจากอะไร ✅ ดี · 🟡 กลาง · ❌ ไม่ดี

**ทำไมตัดเดือนล่าสุดออกจากโมเมนตัม 12 เดือน?** งานวิจัยพบว่าหุ้นที่ขึ้นแรงในเดือนล่าสุดมักกลับตัวสั้น ๆ จึงวัดจาก 12 เดือนก่อนถึง 1 เดือนก่อนแทน (ปิดได้ในช่อง ⚙️)

⚠️ คะแนนสูง = มีแรงส่ง ไม่ใช่คำสั่งซื้อ โมเมนตัมเคยพังหนักช่วงตลาดกลับตัวแรง (เช่นปี 2009) และไม่ได้รวมข่าวหรืองบการเงิน
"""
        )

    with st.expander("⚙️ ปรับค่า (ไม่บังคับ)", expanded=False):
        c1, c2 = st.columns(2)
        bench = c1.text_input("หุ้น/ดัชนีที่ใช้เทียบ", value="SPY", key="mom_bench",
                              help="เช่น SPY (S&P500), QQQ (Nasdaq100), IWM (หุ้นเล็ก), XLK (กลุ่มเทคโนโลยี)").strip().upper() or "SPY"
        skip = c2.checkbox("ตัดเดือนล่าสุดออกจากโมเมนตัม 12 เดือน (ตามงานวิจัย)", value=True, key="mom_skip")
        st.caption("น้ำหนักของแต่ละปัจจัยในคะแนนรวม (ปรับตามสไตล์ได้)")
        w1, w2, w3, w4, w5 = st.columns(5)
        wd = momentum.DEFAULT_WEIGHTS
        w_rs = w1.slider("แข็งกว่าตลาด", 0, 100, wd["rs"], key="mom_w_rs")
        w_tr = w2.slider("เทรนด์", 0, 100, wd["trend"], key="mom_w_trend")
        w_hi = w3.slider("ใกล้จุดสูงสุด", 0, 100, wd["high52"], key="mom_w_high")
        w_cs = w4.slider("สม่ำเสมอ", 0, 100, wd["consistency"], key="mom_w_cons")
        w_rk = w5.slider("ความนิ่ง", 0, 100, wd["risk"], key="mom_w_risk")

    with st.spinner("กำลังคำนวณโมเมนตัม..."):
        r = _cached_scorecard(ticker, bench, skip, (w_rs, w_tr, w_hi, w_cs, w_rk))

    if not r.get("available"):
        st.caption(f"คำนวณโมเมนตัมไม่ได้: {r.get('reason', 'ไม่ทราบสาเหตุ')}")
        return

    # ----- 1) ป้ายคะแนนใหญ่ -----
    c = r["color"]
    score_txt = "-" if r["score"] is None else r["score"]
    st.markdown(_html(f"""
        <div style="border:1px solid {c}66;background:linear-gradient(135deg,{c}22,#12141c);border-radius:14px;padding:22px 26px;display:flex;gap:28px;align-items:center;flex-wrap:wrap;">
        <div style="text-align:center;min-width:120px;">
        <div style="font-size:60px;font-weight:800;color:{c};line-height:1;">{score_txt}</div>
        <div style="color:{GREY};font-size:12px;">จาก 100</div>
        </div>
        <div style="flex:1;min-width:240px;">
        <div style="font-size:24px;font-weight:700;color:{TEXT};">{r['icon']} {r['label']}</div>
        <div style="color:{c};font-size:15px;margin-top:2px;">{r['signal']}</div>
        <div style="color:#c9c5b8;font-size:14px;margin-top:8px;">{' · '.join(r['reasons'])}</div>
        </div>
        </div>
    """), unsafe_allow_html=True)

    # ----- 2) ธงเตือน -----
    for level, text in r["flags"]:
        (st.warning if level == "warn" else st.info)(("⚠️ " if level == "warn" else "ℹ️ ") + text)

    # ----- 3) แข็งกว่าตลาดแค่ไหน -----
    st.markdown(f"**แข็งกว่าตลาดแค่ไหน (เทียบ {r['benchmark']})** — แท่งเขียวไปทางขวา = ชนะตลาด · แดงไปทางซ้าย = แพ้ตลาด")
    rows_html = ""
    for x in r["rets"]:
        if x["diff"] is None:
            continue
        dcol = GREEN if x["diff"] >= 0 else RED
        rows_html += f"""
            <div style="display:flex;align-items:center;gap:14px;padding:7px 0;border-bottom:1px solid #1d2030;flex-wrap:wrap;">
            <div style="width:190px;color:{TEXT};font-size:14px;">{x['label']}</div>
            <div style="width:170px;color:{GREY};font-size:13px;">หุ้น {x['stock']:+.1f}% · {r['benchmark']} {x['bench']:+.1f}%</div>
            <div style="flex:1;min-width:140px;">{_bar_html(x['diff'])}</div>
            <div style="width:90px;text-align:right;color:{dcol};font-weight:700;">{x['diff']:+.1f} จุด</div>
            </div>"""
    st.markdown(_html(f'<div style="margin:4px 0 14px 0;">{rows_html}</div>'), unsafe_allow_html=True)

    # ----- 4) 5 ปัจจัยตามงานวิจัย -----
    st.markdown("**5 ปัจจัยตามงานวิจัย** — ดูว่าคะแนนมาจากอะไร")
    icon_map = {"good": ("✅", GREEN), "mid": ("🟡", GOLD), "bad": ("❌", RED)}
    f_html = ""
    for f in r["factors"]:
        ic, col = icon_map[f["status"]]
        f_html += f"""
            <div style="padding:10px 14px;margin-bottom:8px;border-left:4px solid {col};background:#14161f;border-radius:6px;">
            <div style="color:{TEXT};font-size:15px;font-weight:700;">{ic} {f['name']} <span style="color:{GREY};font-size:12px;font-weight:400;">· {f['ref']}</span></div>
            <div style="color:{col};font-size:14px;margin-top:2px;">{f['value']}</div>
            <div style="color:#c9c5b8;font-size:13px;margin-top:2px;">แปลว่า: {f['meaning']}</div>
            </div>"""
    st.markdown(_html(f_html), unsafe_allow_html=True)

    # ----- 5) ความเสี่ยง -----
    k = r["risk"]
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ผันผวนต่อปี", f"{k['vol']:.0f}%", help="ยิ่งสูง ราคายิ่งแกว่งแรง")
    m2.metric("ตกหนักสุดใน 1 ปี", f"{k['mdd']:.0f}%", help="จากจุดสูงสุดลงมาจุดต่ำสุดในรอบ 1 ปี")
    m3.metric("ห่างจาก SMA50", "-" if k["ext50"] is None else f"{k['ext50']:+.0f}%", help="ห่างมากเกิน ~15% มักมีโอกาสย่อ")
    m4.metric("เทียบจุดสูงสุด 52 สัปดาห์", f"{k['ratio52']*100:.0f}%", help="100% = อยู่ที่จุดสูงสุดพอดี")

    st.caption(
        "ที่มา: งานวิจัยโมเมนตัมของ Jegadeesh & Titman (1993), Moskowitz et al. (2012), George & Hwang (2004), "
        "Da et al. (2014), Barroso & Santa-Clara (2015) ผลวิจัยเป็นค่าเฉลี่ยของหุ้นจำนวนมาก ไม่ใช่การรับประกันรายตัว "
        "และข้อมูลฟรีอาจดีเลย์ นี่ไม่ใช่คำแนะนำซื้อ-ขาย"
    )


# ===============================================================
# สแกนโมเมนตัมหลายตัว
# ===============================================================
def render_scan(symbols):
    symbols = tuple(dict.fromkeys([s for s in symbols if s]))
    if not symbols:
        st.caption("ไม่มีรายชื่อหุ้นให้สแกน")
        return

    with st.expander("📖 วิธีอ่านตารางนี้", expanded=False):
        st.markdown(
            """
เรียงหุ้นตาม **คะแนนโมเมนตัม 0-100** (คำนวณแบบเดียวกับสกอร์การ์ดในหน้าวิเคราะห์รายตัว)
- **คะแนน** ยิ่งสูงยิ่งแข็งแรงตามงานวิจัย
- **3M / 6M / 12M** คือผลตอบแทนที่ *ชนะตลาดกี่จุด* (บวก = ชนะ)
- **% จากจุดสูงสุด** 100% = อยู่ที่จุดสูงสุด 52 สัปดาห์พอดี
- **⚠️** มีธงเตือน (เช่น วิ่งไกลเกิน/ขึ้นแรงเกินใน 1 เดือน) เอาเมาส์ชี้ดูรายละเอียด

สแกนเฉพาะหุ้นที่แสดงอยู่ในหน้านี้ (หุ้นใหญ่ 11 กลุ่ม + ตัวขึ้น/ลงแรงสุด) ไม่ใช่ทั้งตลาด
"""
        )

    c1, c2, c3 = st.columns(3)
    top_n = c1.slider("แสดงกี่ตัว", 5, 30, 10, key="scan_n")
    hide_warn = c2.checkbox("ซ่อนตัวที่มีธงเตือน", value=False, key="scan_hide")
    bench = c3.text_input("ตัวเทียบ", value="SPY", key="scan_bench").strip().upper() or "SPY"

    with st.spinner(f"กำลังสแกนโมเมนตัม {len(symbols)} ตัว..."):
        res = _cached_scan(symbols, bench, True)
    if not res.get("available"):
        st.caption(f"สแกนไม่สำเร็จ: {res.get('reason', 'ไม่ทราบสาเหตุ')}")
        return

    rows = [r for r in res["rows"] if not (hide_warn and r["warn"] > 0)][:top_n]
    if not rows:
        st.caption("ไม่มีหุ้นที่ผ่านเงื่อนไขที่เลือก")
        return

    df = pd.DataFrame([{
        "อันดับ": i + 1,
        "หุ้น": r["symbol"],
        "คะแนน": r["score"],
        "สถานะ": r["label"],
        "ชนะตลาด 3M (จุด)": None if r["rs3m"] is None else round(r["rs3m"], 1),
        "6M (จุด)": None if r["rs6m"] is None else round(r["rs6m"], 1),
        "12M (จุด)": None if r["rs12m"] is None else round(r["rs12m"], 1),
        "% จากจุดสูงสุด": round(r["ratio52"]),
        "⚠️": "⚠️" if r["warn"] else "",
        "รายละเอียดธงเตือน": r["warn_text"],
    } for i, r in enumerate(rows)])

    _show_df(
        df, hide_index=True,
        column_config={
            "คะแนน": st.column_config.ProgressColumn("คะแนน", min_value=0, max_value=100, format="%d"),
        },
    )
    st.caption(f"เทียบกับ {res['benchmark']} · ตัดเดือนล่าสุดออกจากโมเมนตัม 12 เดือน · ผลวิจัยเป็นค่าเฉลี่ยของหุ้นจำนวนมาก ไม่ใช่การรับประกัน")
