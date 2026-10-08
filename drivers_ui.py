# -*- coding: utf-8 -*-
"""
drivers_ui.py
=============
หน้าจอ "ปัจจัยที่ทำให้หุ้นขึ้นหรือลง" — สรุปบนสุดอ่านจบใน 5 วินาที ไล่ลงไปดูรายละเอียดได้ทีละหัวข้อ
เรียกใช้จาก app.py:  drivers_ui.render_drivers(ticker)
"""

import pandas as pd
import streamlit as st

import drivers

GOLD, GREEN, RED, TEXT, GREY = "#d4af37", "#3ecf6e", "#e5534b", "#f4f0e6", "#9a9aa8"
def _show_df(df, **kw):
    """st.dataframe แบบเต็มความกว้าง รองรับทั้ง Streamlit รุ่นเก่า (use_container_width) และรุ่นใหม่ (width="stretch")"""
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


STATUS_STYLE = {
    "good": ("🟢", "หนุน", GREEN),
    "mid": ("🟡", "กลาง", GOLD),
    "bad": ("🔴", "กดดัน", RED),
    "na": ("⚪", "ไม่มีข้อมูล", GREY),
}
GROUPS = [
    ("company", "🏢 ตัวบริษัท", "ผลงานและการบริหารของบริษัทเอง"),
    ("flow", "🌊 เงินไหล & กราฟเทคนิค", "แรงซื้อ-ขายจริงในตลาด"),
    ("macro", "🌎 เศรษฐกิจมหภาค", "เหมือนกันทุกหุ้น แต่กระทบแต่ละกลุ่มไม่เท่ากัน (หุ้นเติบโต/เทคโนโลยีไวต่อดอกเบี้ยมากกว่า)"),
]


def _html(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


@st.cache_data(ttl=3600, show_spinner=False)
def _company(ticker, include_peers):
    return drivers.company_drivers(ticker, include_peers=include_peers)


@st.cache_data(ttl=300, show_spinner=False)
def _flow_tech(ticker):
    return drivers.flow_tech_drivers(ticker)


@st.cache_data(ttl=21600, show_spinner=False)
def _macro():
    return drivers.macro_drivers()


def _render_guide():
    with st.expander("📖 วิธีอ่านส่วนนี้ (อ่าน 30 วินาที)", expanded=False):
        st.markdown(
            """
**แต่ละหัวข้อสรุปเป็น 3 สถานะ:** 🟢 หนุน (เป็นแรงหนุนราคา) · 🟡 กลาง · 🔴 กดดัน (เป็นแรงกดราคา)

**ดู 3 ขั้น**
1. **ป้ายสรุปบนสุด** นับว่ามีปัจจัยหนุน/กลาง/กดดันกี่ข้อ
2. **ไล่ดูทีละกลุ่ม** ตัวบริษัท → เงินไหล/เทคนิค → เศรษฐกิจมหภาค อ่านบรรทัด "แปลว่า" ก็เข้าใจแล้ว
3. **กด "ดูรายละเอียด/กราฟ"** เมื่ออยากรู้เหตุผลและวิธีดูตัวเลขต่อ

**สรุปว่าอะไรทำให้ขึ้น/ลง**

| ปัจจัย | ขึ้นเมื่อ | ลงเมื่อ |
|---|---|---|
"""
            + "\n".join(f"| {n} | {up} | {down} |" for _, n, up, down in drivers.FACTOR_GUIDE)
            + """

**ข้อควรรู้**
- ราคาหุ้นระยะสั้นมักตอบสนองต่อ **"ต่างจากที่ตลาดคาด"** มากกว่าตัวเลขดี/แย่ในตัวมันเอง (เช่น กำไรดีแต่ต่ำกว่าที่คาด ราคาก็ลงได้)
- ปัจจัยมหภาคเปลี่ยนช้า (รายเดือน/รายไตรมาส) ไม่ได้บอกเหตุการณ์รายวัน
- การนับ "หนุน/กดดัน" เป็นกฎหัวแม่มือ ไม่ใช่การทำนายว่าจะขึ้นหรือลง และแต่ละข้อน้ำหนักไม่เท่ากัน
"""
        )


def _summary_card(summary: dict):
    c = summary["color"]
    total = max(summary["good"] + summary["mid"] + summary["bad"], 1)
    seg = lambda n, col: f'<div style="flex:{n};background:{col};height:12px;"></div>' if n else ""
    bar = f'<div style="display:flex;border-radius:6px;overflow:hidden;margin-top:12px;background:#242733;">{seg(summary["good"], GREEN)}{seg(summary["mid"], GOLD)}{seg(summary["bad"], RED)}</div>'
    st.markdown(_html(f"""
        <div style="border:1px solid {c}66;background:linear-gradient(135deg,{c}22,#12141c);border-radius:14px;padding:20px 26px;margin-bottom:6px;">
        <div style="font-size:24px;font-weight:800;color:{c};">{summary['icon']} {summary['label']}</div>
        <div style="color:{TEXT};font-size:15px;margin-top:4px;">{summary['detail']}</div>
        {bar}
        <div style="color:{GREY};font-size:12px;margin-top:8px;">นับจากกฎหัวแม่มือ ไม่ใช่การทำนายว่าหุ้นจะขึ้นหรือลง</div>
        </div>
    """), unsafe_allow_html=True)


def _render_factor(f: dict):
    icon, label, col = STATUS_STYLE[f["status"]]
    st.markdown(_html(f"""
        <div style="padding:12px 16px;margin-top:10px;border-left:5px solid {col};background:#14161f;border-radius:6px;">
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
        <div style="font-size:16px;font-weight:700;color:{TEXT};">{f['icon']} {f['name']}</div>
        <div style="background:{col}22;color:{col};border:1px solid {col}66;border-radius:12px;padding:1px 10px;font-size:12px;font-weight:700;">{icon} {label}</div>
        </div>
        <div style="color:{col if f['status'] != 'na' else GREY};font-size:14px;margin-top:4px;">{f['headline']}</div>
        <div style="color:#c9c5b8;font-size:13px;margin-top:3px;">แปลว่า: {f['meaning']}</div>
        </div>
    """), unsafe_allow_html=True)

    if f["details"] or f["chart"] or f["table"] is not None:
        with st.expander(f"ดูรายละเอียด/กราฟ — {f['name']}", expanded=False):
            for line in f["details"]:
                st.markdown(f"- {line}")
            ch = f["chart"]
            if ch and ch.get("df") is not None and len(ch["df"]):
                st.caption(ch.get("title", ""))
                if ch["kind"] == "bar":
                    st.bar_chart(ch["df"], height=220)
                else:
                    st.line_chart(ch["df"], height=220)
            if f["table"] is not None and len(f["table"]):
                _show_df(f["table"], hide_index=True)


def render_drivers(ticker: str):
    _render_guide()
    include_peers = st.checkbox("เทียบ P/E กับหุ้นใหญ่ในกลุ่มเดียวกัน (ช้าลงเล็กน้อย)", value=True, key="drv_peers")

    with st.spinner("กำลังรวบรวมปัจจัยทั้ง 10 ข้อ..."):
        company = _company(ticker, include_peers)
        flow_tech = _flow_tech(ticker)
        macro = _macro()

    all_f = company + flow_tech + macro
    _summary_card(drivers.summarize(all_f))

    by_group = {"company": company, "flow": flow_tech, "macro": macro}
    for key, title, sub in GROUPS:
        st.markdown(f"#### {title}")
        st.caption(sub)
        for f in by_group[key]:
            _render_factor(f)

    st.caption(
        "ข้อมูลจาก Yahoo Finance และ FRED (ฟรี อาจดีเลย์/ไม่ครบทุกหุ้น) · Fund Flow ใช้ตัวแทนจากราคา-ปริมาณและการถือครองของสถาบัน "
        "ไม่ใช่เงินไหลเข้า-ออกกองทุนจริง · นี่ไม่ใช่คำแนะนำซื้อ-ขาย"
    )
