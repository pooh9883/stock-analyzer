# -*- coding: utf-8 -*-
"""
app.py — Quant Stock Analyzer (ฟรีตลอด)
=========================================
โครงสร้าง:
1. ระบบให้คะแนน 10 มิติ (scoring.py) = หลัก, ฟรี 100%, ไม่ต้องมี API key
2. ปุ่ม "สรุปผลด้วย AI" = เสริม, ใช้ Claude (Anthropic API) เบื้องหลัง ต้องมี API key (กดเมื่อต้องการเท่านั้น)
   ถ้า provider error/หมด quota แอปยังทำงานได้ปกติด้วยระบบคะแนน
   (ชื่อ provider ใช้แค่ในคอมเมนต์โค้ดกับ README ไม่โชว์ในหน้า UI)
"""

import streamlit as st
import pandas as pd
from urllib.parse import urlparse
import scoring    # ไฟล์ scoring.py ที่อยู่โฟลเดอร์เดียวกัน
import advanced   # ไฟล์ advanced.py — options chain, insider, institution, analyst, technical ขั้นสูง
import deep       # ไฟล์ deep.py — momentum, relative strength, IV skew, target dispersion, earnings, news
import backtest   # ไฟล์ backtest.py — ทดสอบย้อนหลังความแม่นยำของสัญญาณ technical
import macro      # ไฟล์ macro.py — VIX, อัตราผลตอบแทนพันธบัตร 10 ปี
import news_feed  # ไฟล์ news_feed.py — เรดาร์ข่าวภาษาไทย (แปล+สรุป)
import news_radar # ไฟล์ news_radar.py — ดึงหัวข้อข่าวจริงให้ AI อ่านตอนสรุป
import levels     # ไฟล์ levels.py — ราคาสดแบบอัปเดตอัตโนมัติ + โซนราคาอ้างอิง
import momentum_ui  # momentum_ui.py — โมเมนตัมตามงานวิจัย + โซนหุ้นเขียวตลาดแดง + สอนวิธีอ่าน
import rocket_ui    # rocket_ui.py — Watchlist Scanner: แนวรับ/แนวต้าน + RSI + โมเมนตัม + R:R
import drivers_ui   # drivers_ui.py — ปัจจัยที่ทำให้หุ้นขึ้นหรือลง 10 ข้อ
import checklist  # checklist.py — เช็กลิสต์หลายเงื่อนไข + backtest เช็กลิสต์
import market_overview  # ไฟล์ market_overview.py — ภาพรวมตลาด: หุ้นขึ้น/ลงแรงสุด, หุ้นใหญ่แต่ละกลุ่ม
from pathlib import Path
import theme      # theme.py — ดีไซน์ทั้งเว็บ (CSS, hero, แถบราคาเลื่อน, สถานะตลาด)
import home_ui    # home_ui.py — หน้าแรก: ดัชนี, Sector Rotation, ข้อมูล Watchlist
import themes_ui  # themes_ui.py — ไอเดียตามธีม
import tools_ui   # tools_ui.py — เครื่องมือคำนวณ (ต้นทุน, รอแนวรับ, ขนาดตำแหน่ง, DCF)
import calendar_ui  # calendar_ui.py — ปฏิทินเหตุการณ์ (งบ/ปันผล/เฟด)
import compare_ui  # compare_ui.py — เทียบหุ้น 2–3 ตัวข้างกัน
import watchlist  # watchlist.py — Watchlist กลางที่แถบข้าง
import fx  # fx.py — เลเยอร์เอฟเฟกต์ Cyberpunk Edgerunner
import market_events  # market_events.py - เหตุการณ์ตลาดที่ขยับหลายตัวพร้อมกัน
import market_brief  # market_brief.py - สรุปตลาดวันนี้ (ตัวเลขสด + ธีมข่าว + กระทบคุณยังไง)
import fast_ui  # fast_ui.py — หน้าหุ้นซิ่ง: สแกน · ปริมาณ · ATR · คำนวณขนาดไม้
import insight  # insight.py — มุมมองเชิงลึกหลายแง่ (คุณภาพกำไร · มาร์จิ้น · แนวทางข้างหน้า · บันไดราคา)
import screener  # screener.py — คัดกรองหุ้นคุณภาพ+เติบโต (S&P 500 / Nasdaq 100)
import chart_pro  # chart_pro.py — กราฟโปร: แท่งเทียน + EMA + RSI + แนวรับ/แนวต้าน + เครื่องมือคำนวณ

try:  # ไอคอนแท็บเบราว์เซอร์ = โลโก้ใหม่
    import base64 as _b64, io as _io
    from PIL import Image as _PILImage
    import logo_asset as _la
    _page_icon = _PILImage.open(_io.BytesIO(_b64.b64decode(_la.LOGO_ICON)))
except Exception:
    _page_icon = "◆"

st.set_page_config(
    page_title="Quant Stock Analyzer",
    page_icon=_page_icon,
    layout="wide",
    initial_sidebar_state="expanded",
)


# =================================================================
# CUSTOM CSS — โทนมืด/ทอง ดูเป็นทางการแบบ terminal การเงิน
# =================================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans Thai', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at top left, #0c0e1c 0%, #05060d 60%);
        color: #e6f1ff !important;
    }

    /* บังคับสีตัวหนังสือให้สว่างชัดเจนทุกจุด กันปัญหาอ่านยากบนมือถือ
       (สำคัญเพราะ browser บางตัวยังใช้สีข้อความเริ่มต้นที่มืดเกินไปบนพื้นมืด) */
    .stApp, .stApp p, .stApp li, .stApp span, .stApp label,
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span,
    div[data-testid="stExpanderDetails"], div[data-testid="stExpanderDetails"] p,
    div[data-testid="stCaptionContainer"] {
        color: #e6f1ff !important;
    }
    .stCaption, div[data-testid="stCaptionContainer"] p {
        color: #9aa4c4 !important;
    }

    .app-header {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 6px 0 2px 0;
        border-bottom: 1px solid rgba(0,240,255, 0.25);
        margin-bottom: 6px;
    }
    .app-header .mark {
        font-size: 30px;
        color: #5ee7ff;
        line-height: 1;
    }
    .app-header .title-text h1 {
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: 0.5px;
        color: #e6f1ff;
    }
    .app-header .title-text p {
        margin: 2px 0 0 0;
        font-size: 13px;
        color: #7d86a6;
        letter-spacing: 0.3px;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #0c0e1c, #080a16);
        border: 1px solid rgba(0,240,255, 0.18);
        border-radius: 10px;
        padding: 14px 16px 10px 16px;
    }
    div[data-testid="stMetricLabel"] {
        color: #7d86a6 !important;
        font-size: 12px !important;
        letter-spacing: 0.4px;
        text-transform: uppercase;
    }
    div[data-testid="stMetricValue"] {
        color: #e6f1ff !important;
        font-family: 'IBM Plex Mono', monospace;
    }

    section[data-testid="stSidebar"] {
        background: #080a16;
        border-right: 1px solid rgba(0,240,255, 0.15);
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #5ee7ff !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #5ee7ff, #00b8c8);
        color: #0c0e1c;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        letter-spacing: 0.3px;
        transition: 0.15s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #fff25c, #c9bc00);
        transform: translateY(-1px);
    }

    .stLinkButton > a {
        border-radius: 8px !important;
        border: 1px solid rgba(0,240,255, 0.35) !important;
        color: #5ee7ff !important;
        background: transparent !important;
        font-weight: 500 !important;
    }
    .stLinkButton > a:hover {
        background: rgba(0,240,255, 0.08) !important;
    }

    details[data-testid="stExpander"] {
        background: #0c0e1c;
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 10px;
        margin-bottom: 8px;
    }

    hr {
        border-color: rgba(0,240,255, 0.15) !important;
    }

    .section-label {
        color: #5ee7ff;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ดีไซน์ชุดใหม่ (วางทับ CSS เดิม) + ติดตั้งธีมเข้มของ Streamlit อัตโนมัติ
theme.inject()

# ---------- ตรวจว่า rocket.py ที่โหลดอยู่เป็นเวอร์ชันถูกต้อง (กันไฟล์เก่าค้าง/ชื่อซ้ำ) ----------
import rocket as _rk
_need = [n for n in ("rsi", "load_daily", "_pick") if not hasattr(_rk, n)]
if _need:
    st.error(
        f"ไฟล์ rocket.py ที่ระบบโหลดอยู่เป็นเวอร์ชันเก่าหรือผิดไฟล์ — ขาดฟังก์ชัน: {', '.join(_need)}\n\n"
        f"ตำแหน่งไฟล์ที่ถูกโหลด: {getattr(_rk, '__file__', 'ไม่ทราบ')}\n\n"
        "วิธีแก้: วาง rocket.py ตัวล่าสุดทับไฟล์นั้น (ชื่อต้องเป็น rocket.py เป๊ะๆ) แล้วลบโฟลเดอร์ __pycache__ และรันใหม่"
    )
    st.stop()

# ---------- กันค่าในช่องรหัสหุ้นหาย เวลาสลับไปหน้าอื่น (Streamlit ล้างค่าของช่องที่ไม่ได้แสดงในรอบนั้น) ----------
for _k in list(st.session_state.keys()):
    if _k in ("deep_ticker", "cp_sym", "cp_tf2", "cp_auto", "cp_ext", "sec_period", "sec_start", "cmp_tickers", "cal_text", "nf_wl") or str(_k).startswith("cp_rng_"):
        st.session_state[_k] = st.session_state[_k]


def colored_bar(frac: float):
    """แถบความคืบหน้าไล่สีตามค่าจริง: ต่ำ = แดง → กลาง = เหลือง → สูง = เขียว"""
    f = max(0.0, min(1.0, float(frac)))
    col = f"hsl({int(f * 120)}, 95%, 56%)"
    st.markdown(
        f'<div style="height:10px; background:rgba(125,134,166,.18); margin:6px 0 10px 0; border-radius:2px;">'
        f'<div style="width:{f * 100:.1f}%; height:100%; background:{col}; border-radius:2px; box-shadow:0 0 10px {col};"></div></div>',
        unsafe_allow_html=True,
    )

if theme.ensure_streamlit_theme(Path(__file__).resolve().parent):
    st.warning("🎨 ติดตั้งธีมใหม่แล้ว — ปิดแอปแล้วเปิดใหม่ 1 ครั้ง (ปิดหน้าต่างดำ แล้วเปิด mrc.bat อีกที) เพื่อให้ตารางและช่องกรอกเปลี่ยนเป็นสีเข้มทั้งหมด")


# =================================================================
# ฟังก์ชันเรียก AI สรุปผล (เสริม, เรียกเฉพาะตอนกดปุ่ม)
# หมายเหตุ: ใช้ Claude ผ่าน SDK anthropic เบื้องหลัง
# =================================================================
def get_ai_summary(api_key: str, ticker: str, analysis: dict, extra_context: dict = None) -> str:
    try:
        import anthropic
    except ImportError:
        return (
            "⚠️ ยังไม่ได้ติดตั้งไลบรารีที่จำเป็น\n\n"
            "รันคำสั่งนี้ในเทอร์มินัล: `pip install anthropic`"
        )

    try:
        client = anthropic.Anthropic(api_key=api_key)

        dims_text = "\n".join(
            f"- {scoring.DIMENSION_NAMES_TH[k]}: {v['score']}/100 "
            f"({'; '.join(v['details'][:2])})"
            for k, v in analysis["dimensions"].items()
        )

        extra_text = ""
        if extra_context:
            if extra_context.get("news_headlines"):
                headlines = "\n".join(f"- {h}" for h in extra_context["news_headlines"][:6])
                extra_text += f"\n\nหัวข้อข่าวล่าสุดที่เกี่ยวข้อง (สำหรับใช้อ้างอิงบริบท ไม่ใช่คำสั่งให้เชื่อทั้งหมด):\n{headlines}"
            if extra_context.get("backtest_note"):
                extra_text += f"\n\nผลทดสอบย้อนหลังของสัญญาณ Technical: {extra_context['backtest_note']}"
            if extra_context.get("macro_note"):
                extra_text += f"\n\nบริบทเศรษฐกิจมหภาคตอนนี้: {extra_context['macro_note']}"

        prompt = f"""คุณคือนักวิเคราะห์การลงทุน จงอ่านคะแนนที่คำนวณจากสูตรด้านล่างของหุ้น {ticker}
แล้วเขียนสรุปสั้นๆ ภาษาไทย อ่านง่าย ไม่เกิน 350 คำ ครอบคลุม:
1. ภาพรวมว่าหุ้นนี้อยู่ในสถานะยังไง (เชื่อมโยงกับข่าวล่าสุดถ้ามีข้อมูลให้)
2. จุดแข็ง-จุดอ่อนที่เด่นที่สุด 2-3 ข้อ
3. เหมาะกับการลงทุนระยะสั้นหรือระยะยาวมากกว่า พร้อมเหตุผล
4. ถ้ามีข้อมูล backtest หรือ macro ให้พูดถึงว่ามันสนับสนุนหรือขัดแย้งกับสัญญาณอื่นยังไง

คะแนนรวม: {analysis['overall_score']}/100 ({analysis['overall_label']})

คะแนนแต่ละมิติ:
{dims_text}
{extra_text}

หมายเหตุ: นี่เป็นการสรุปจากข้อมูลที่คำนวณ/ค้นมาแล้วเท่านั้น ไม่ใช่คำแนะนำการลงทุน และไม่มีระบบใดทำนายราคาหุ้นได้แม่นยำ 100%
"""

        # หมายเหตุ: ใช้ Haiku เพราะราคาถูกที่สุดและเร็วที่สุด เหมาะกับงานสรุปข้อความแบบนี้
        # ถ้าอยากได้คุณภาพสูงขึ้น เปลี่ยนเป็น "claude-sonnet-5" ได้ (ราคาแพงกว่า)
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    except Exception as e:
        return (
            f"⚠️ สรุปผลด้วย AI ไม่สำเร็จ ({e})\n\n"
            "ไม่เป็นไรครับ — ระบบคะแนนด้านบนยังใช้งานได้ปกติ "
            "อาจเป็นเพราะคีย์ไม่ถูกต้อง หรือยังไม่ได้เติมเครดิตในบัญชี ลองเช็คที่ console.anthropic.com"
        )


def explain_headlines_with_ai(api_key: str, ticker: str, headlines: list) -> list:
    """
    อธิบายหัวข้อข่าวแต่ละอันสั้นๆ (ไม่เกิน ~20 คำ) เป็นภาษาไทย โดย batch ทั้งหมดเป็น 1 คำขอต่อหุ้น
    เพื่อประหยัดค่าใช้จ่าย คืนค่า list ของคำอธิบาย เรียงตามลำดับเดียวกับ headlines ที่ส่งเข้ามา
    ถ้าไม่มีคีย์หรือ error คืนค่า list ว่างเปล่าเท่าจำนวน headlines (แปลว่าไม่มีคำอธิบาย)
    """
    if not api_key or not headlines:
        return ["" for _ in headlines]

    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)

        numbered = "\n".join(f"{i+1}. {h}" for i, h in enumerate(headlines))
        prompt = f"""นี่คือหัวข้อข่าวภาษาอังกฤษของหุ้น {ticker} จำนวน {len(headlines)} ข่าว:

{numbered}

จงเขียนอธิบายแต่ละข่าวเป็นภาษาไทย สั้นที่สุดเท่าที่จะทำได้ (ไม่เกิน 20 คำต่อข่าว) ว่าข่าวนี้เกี่ยวกับอะไร สำคัญยังไงกับหุ้นตัวนี้
ตอบเป็นรายการลำดับเลข ตรงกับลำดับข่าวด้านบนเป๊ะๆ (1 ถึง {len(headlines)}) ไม่ต้องมีคำนำหรือสรุปปิดท้าย
"""

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text

        # แยกคำตอบตามเลขลำดับ รองรับหลายรูปแบบ เช่น "1.", "1)", "**1.**", "1 -"
        import re
        explanations = ["" for _ in headlines]
        for line in text.split("\n"):
            line = line.strip().lstrip("*").strip()
            if not line:
                continue
            match = re.match(r"^(\d+)[\.\)\-:]\s*(.+)", line)
            if match:
                idx = int(match.group(1)) - 1
                if 0 <= idx < len(headlines):
                    explanations[idx] = match.group(2).strip()

        # ถ้า parse ไม่ได้เลยสักบรรทัด (รูปแบบไม่ตรงคาดเดาทั้งหมด) ใช้ fallback:
        # เอาบรรทัดที่ไม่ว่างเรียงตามลำดับแทน เผื่อจำนวนตรงกันพอดี
        if all(e == "" for e in explanations):
            non_empty_lines = [l.strip().lstrip("*").strip() for l in text.split("\n") if l.strip()]
            if len(non_empty_lines) == len(headlines):
                explanations = non_empty_lines

        return explanations
    except Exception:
        return ["" for _ in headlines]


# =================================================================
# Cache เพื่อลดจำนวนครั้งที่ยิง request ไปหา Yahoo Finance ซ้ำๆ
# (yfinance เจอปัญหา rate-limit บ่อยบน cloud IP ที่ใช้ร่วมกันหลายคน
#  การ cache ไว้ 10 นาที ช่วยลดโอกาสโดนบล็อกจากการเรียกซ้ำโดยไม่จำเป็น)
# =================================================================
@st.cache_data(ttl=600, show_spinner=False)
def cached_full_analysis(ticker: str):
    return scoring.full_analysis(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_checklist(ticker: str):
    return checklist.run_checklist(ticker)


@st.cache_data(ttl=20, show_spinner=False)
def cached_live_relative(ticker: str):
    return checklist.live_relative(ticker)


def render_live_relative(ticker: str, zone_params: dict = None):
    """หุ้นเทียบตลาดแบบสด: อัปเดตเฉพาะส่วนนี้ตามรอบที่ตั้งไว้ที่แถบซ้าย"""
    rs = cached_live_relative(ticker)
    if not rs.get("available"):
        st.caption(f"เทียบกับตลาดไม่ได้ตอนนี้: {rs.get('reason', 'ไม่ทราบสาเหตุ')} — จะลองใหม่รอบถัดไป")
        return

    # การ์ดโซนใหญ่ (ตัวเลขรายวัน เทียบกับเกณฑ์ที่ปรับได้)
    _now = next((c for c in rs["cards"] if c["label"].startswith("ตอนนี้")), None)
    _five = next((c for c in rs["cards"] if c["label"].startswith("5 วัน")), None)
    if _now:
        _confirm = None
        if _five:
            if _five["stock"] > _five["market"]:
                _confirm = f"✓ 5 วันล่าสุดหุ้นก็แข็งกว่าตลาดด้วย (หุ้น {_five['stock']:+.2f}% / SPY {_five['market']:+.2f}%) สัญญาณน่าเชื่อขึ้น"
            else:
                _confirm = f"⚠️ 5 วันล่าสุดหุ้นยังไม่แข็งกว่าตลาด (หุ้น {_five['stock']:+.2f}% / SPY {_five['market']:+.2f}%) วันนี้อาจเป็นแค่เด้งวันเดียว"
        momentum_ui.render_zone_card(_now["stock"], _now["market"], zone_params, _confirm)
    st.caption("ดูช่วงอื่นประกอบ — ยิ่งเขียวหลายช่วงยิ่งน่าเชื่อ")
    for card in rs["cards"]:
        txt = f"{card['label']}: หุ้น {card['stock']:+.2f}% / SPY {card['market']:+.2f}%"
        if card["state"] == "green_vs_red":
            st.success(f"🟢 หุ้นเขียว ตลาดแดง — แข็งกว่าตลาด · {txt}")
        elif card["state"] == "both_green":
            st.info(f"🟢 หุ้นเขียว ตลาดเขียว — ขึ้นตามตลาด · {txt}")
        elif card["state"] == "both_red":
            st.warning(f"🔴 หุ้นแดง ตลาดแดง — ลงตามตลาด · {txt}")
        else:
            st.error(f"🔴 หุ้นแดง ตลาดเขียว — อ่อนกว่าตลาด · {txt}")
    if rs.get("as_of"):
        note = "ตลาดสหรัฐปิดอยู่ แสดงข้อมูลของรอบซื้อขายล่าสุด" if rs.get("stale") else "ข้อมูลล่าสุด"
        st.caption(f"{note} · แท่งล่าสุด {rs['as_of']} (เวลาตลาดสหรัฐ) · ข้อมูลฟรีอาจดีเลย์")


@st.cache_data(ttl=3600, show_spinner=False)
def cached_checklist_backtest(ticker: str):
    return checklist.backtest_checklist(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_forward_outlook(ticker: str):
    return advanced.forward_outlook(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_deep_outlook(ticker: str):
    return deep.deep_outlook(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_one_month_horizon(ticker: str):
    return deep.analyze_one_month_horizon(ticker)


@st.cache_data(ttl=900, show_spinner=False)
def cached_vol_range(ticker: str):
    """ความผันผวนรายวันย้อนหลัง ~60 วันทำการ (ใช้ประมาณช่วงราคา 1 เดือนข้างหน้า)"""
    try:
        import numpy as np
        import yfinance as yf
        h = yf.Ticker(ticker).history(period="6mo", interval="1d", auto_adjust=True)["Close"].dropna()
        r = np.log(h / h.shift(1)).dropna().tail(60)
        if len(r) < 30:
            return {"available": False}
        return {"available": True, "daily_sd": float(r.std()), "n": int(len(r))}
    except Exception:
        return {"available": False}


@st.cache_data(ttl=300, show_spinner=False)
def cached_short_term(ticker: str):
    """ข้อมูลมุมมองระยะสั้น: ความผันผวนรายวัน 20/60 วัน, RSI14, EMA9/21, ผลตอบแทน 5 วัน, แนวรับ/แนวต้านใกล้สุด"""
    try:
        import numpy as np
        d = chart_pro._load_daily(ticker)
        if d is None or len(d) < 40:
            return {"available": False}
        c = d["Close"].astype(float)
        r = np.log(c / c.shift(1)).dropna()
        sd20, sd60 = float(r.tail(20).std()), float(r.tail(60).std())
        dl = c.diff()
        au = dl.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
        ad = (-dl.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
        last_ad = float(ad.iloc[-1])
        rsi = 100.0 if last_ad == 0 else float(100 - 100 / (1 + float(au.iloc[-1]) / last_ad))
        last = float(c.iloc[-1])
        lv = chart_pro.pick_levels(d, last) or []
        sup = [float(z["price"]) for z in lv if z.get("kind") == "support" and float(z["price"]) < last]
        res = [float(z["price"]) for z in lv if z.get("kind") == "resistance" and float(z["price"]) > last]
        if sd20 != sd20 or sd20 <= 0:
            return {"available": False}
        return {"available": True, "sd20": sd20, "sd60": sd60 if sd60 == sd60 else sd20, "rsi": rsi,
                "ema9": float(c.ewm(span=9, adjust=False).mean().iloc[-1]),
                "ema21": float(c.ewm(span=21, adjust=False).mean().iloc[-1]),
                "last": last, "ret5": last / float(c.iloc[-6]) - 1,
                "support": max(sup) if sup else None, "resistance": min(res) if res else None}
    except Exception:
        return {"available": False}


@st.cache_data(ttl=1800, show_spinner=False)
def cached_analyst_recent(ticker: str):
    """ความเคลื่อนไหวของนักวิเคราะห์ 30 วันล่าสุด: ปรับคำแนะนำขึ้น/ลง, ปรับเป้าราคาขึ้น/ลด, รายการล่าสุด"""
    try:
        import pandas as pd
        import yfinance as yf
        ud = yf.Ticker(ticker).upgrades_downgrades
        if ud is None or len(ud) == 0:
            return {"available": False}
        d = ud.copy()
        d.index = pd.DatetimeIndex(pd.to_datetime(d.index, utc=True)).tz_convert(None)
        d = d.sort_index(ascending=False)
        d = d[d.index >= pd.Timestamp.now("UTC").tz_convert(None) - pd.Timedelta(days=30)]
        act = d["Action"].astype(str).str.lower() if "Action" in d.columns else pd.Series([], dtype=str)
        raises = lowers = 0
        if "currentPriceTarget" in d.columns and "priorPriceTarget" in d.columns:
            cur = pd.to_numeric(d["currentPriceTarget"], errors="coerce")
            pri = pd.to_numeric(d["priorPriceTarget"], errors="coerce")
            ok = cur.notna() & pri.notna() & (pri > 0)
            raises, lowers = int(((cur > pri) & ok).sum()), int(((cur < pri) & ok).sum())
        elif "priceTargetAction" in d.columns:
            pa = d["priceTargetAction"].astype(str).str.lower()
            raises, lowers = int((pa == "raises").sum()), int((pa == "lowers").sum())
        latest = None
        if len(d):
            r0 = d.iloc[0]
            latest = {"firm": str(r0.get("Firm", "") or ""), "to": str(r0.get("ToGrade", "") or ""),
                      "action": str(r0.get("Action", "") or "").lower(), "month": int(d.index[0].month), "day": int(d.index[0].day)}
        return {"available": True, "n": int(len(d)), "up": int((act == "up").sum()), "down": int((act == "down").sum()),
                "raises": raises, "lowers": lowers, "latest": latest}
    except Exception:
        return {"available": False}


@st.cache_data(ttl=1800, show_spinner=False)
def cached_macro_snapshot():
    return macro.macro_snapshot()


@st.cache_data(ttl=3600, show_spinner=False)
def cached_backtest(ticker: str):
    return backtest.backtest_technical_signal(ticker, holding_days=5, lookback_period="2y")


@st.cache_data(ttl=20, show_spinner=False)
def cached_live_quote(ticker: str):
    # cache สั้นมาก (20 วินาที) กันไม่ให้หลายผู้ใช้/หลายรอบ refresh ยิง Yahoo ถี่เกินไป
    return levels.get_live_quote(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_price_zones(ticker: str, margin_of_safety: float):
    return levels.price_zones(ticker, margin_of_safety)


def render_live_panel(ticker: str, zones_result: dict = None):
    """แผงราคาสด: อัปเดตเฉพาะส่วนนี้ ไม่ทำให้ทั้งหน้ารันใหม่"""
    q = cached_live_quote(ticker)
    if not q.get("available"):
        st.caption(f"ยังดึงราคาสดไม่ได้ ({q.get('reason', 'ไม่ทราบสาเหตุ')}) — จะลองใหม่รอบถัดไป")
        return

    price_now = q["price"]
    chg_pct = q.get("change_pct")
    chg = q.get("change")
    color = "#19f5a5" if (chg_pct or 0) > 0 else ("#ff2a6d" if (chg_pct or 0) < 0 else "#fcee0a")
    chg_txt = f"{chg:+,.2f} ({chg_pct:+.2f}%)" if chg_pct is not None else "—"

    zone_txt = ""
    if zones_result and zones_result.get("available") and zones_result.get("nearest_below"):
        nb = zones_result["nearest_below"]
        gap = (price_now - nb["price"]) / price_now * 100
        zone_txt = (
            f"<span style='color:#7d86a6; font-size:13px; margin-left:18px;'>แนวรับอ้างอิงใกล้สุด:</span> "
            f"<span style='color:#5ee7ff; font-weight:600;'>&#36;{nb['price']:,.2f}</span> "
            f"<span style='color:#7d86a6; font-size:13px;'>(ห่างลงไป {gap:.1f}% · {nb['name']})</span>"
        )

    st.markdown(
        f"""
        <div style="background:#0c0e1c; border:1px solid rgba(0,240,255,0.3); border-radius:10px; padding:12px 18px; margin-bottom:10px;">
            <span style="color:#7d86a6; font-size:13px;">ราคาล่าสุด {ticker}</span>
            <span style="font-size:26px; font-weight:700; color:#e6f1ff; font-family:'IBM Plex Mono', monospace; margin-left:8px;">&#36;{price_now:,.2f}</span>
            <span style="color:{color}; font-weight:600; margin-left:10px;">{chg_txt}</span>
            {zone_txt}
            <div style="color:#7d86a6; font-size:11px; margin-top:4px;">อัปเดตอัตโนมัติ · ข้อมูลฟรีจาก Yahoo อาจช้ากว่าราคาจริงเล็กน้อย</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------- กล่องเทียบสี: หุ้นคุณ vs ตลาดรวม (SPY) — ดูปุ๊บเข้าใจเลย ----------
    spy_q = cached_live_quote("SPY") if ticker != "SPY" else q
    if spy_q.get("available") and chg_pct is not None and spy_q.get("change_pct") is not None:
        spy_pct = spy_q["change_pct"]
        stock_up = chg_pct > 0
        spy_up = spy_pct > 0

        stock_color = "#19f5a5" if stock_up else ("#ff2a6d" if chg_pct < 0 else "#7d86a6")
        spy_color = "#19f5a5" if spy_up else ("#ff2a6d" if spy_pct < 0 else "#7d86a6")
        stock_arrow = "🟢▲" if stock_up else ("🔴▼" if chg_pct < 0 else "⚪")
        spy_arrow = "🟢▲" if spy_up else ("🔴▼" if spy_pct < 0 else "⚪")

        if stock_up and not spy_up:
            verdict_text = "✅ หุ้นคุณเขียว ตลาดรวมแดง — แข็งแกร่งกว่าตลาดตอนนี้"
            verdict_bg, verdict_fg = "rgba(62,207,110,0.12)", "#19f5a5"
        elif (not stock_up) and spy_up:
            verdict_text = "⚠️ หุ้นคุณแดง ตลาดรวมเขียว — อ่อนแอกว่าตลาดตอนนี้"
            verdict_bg, verdict_fg = "rgba(229,83,75,0.12)", "#ff2a6d"
        else:
            gap = chg_pct - spy_pct                      # ทิศเดียวกัน → ดูว่าแรงกว่า/เบากว่าตลาดแค่ไหน (ต่างเกิน 1 จุด % ถึงนับว่าต่าง)
            if abs(gap) < 1.0:
                verdict_text = "➖ หุ้นคุณกับตลาดรวมไปทางเดียวกัน (แรงใกล้เคียงกัน)"
                verdict_bg, verdict_fg = "rgba(252,238,10,0.12)", "#fcee0a"
            elif stock_up:      # ขึ้นทั้งคู่
                better = gap > 0
                verdict_text = ("✅ ขึ้นทั้งคู่ แต่หุ้นคุณขึ้นแรงกว่าตลาด" if better else "➖ ขึ้นทั้งคู่ แต่หุ้นคุณขึ้นช้ากว่าตลาด")
                verdict_bg, verdict_fg = ("rgba(62,207,110,0.12)", "#19f5a5") if better else ("rgba(252,238,10,0.12)", "#fcee0a")
            else:               # ลงทั้งคู่
                worse = gap < 0
                verdict_text = ("⚠️ ลงทั้งคู่ แต่หุ้นคุณลงแรงกว่าตลาดมาก" if worse else "➖ ลงทั้งคู่ แต่หุ้นคุณลงน้อยกว่าตลาด")
                verdict_bg, verdict_fg = ("rgba(229,83,75,0.12)", "#ff2a6d") if worse else ("rgba(252,238,10,0.12)", "#fcee0a")

        st.markdown(
            f"""
            <div style="display:flex; gap:10px; margin-bottom:8px;">
                <div style="flex:1; background:#0c0e1c; border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; text-align:center;">
                    <div style="color:#7d86a6; font-size:13px; margin-bottom:4px;">หุ้นคุณ · {ticker}</div>
                    <div style="font-size:30px; font-weight:700; color:{stock_color}; font-family:'IBM Plex Mono', monospace;">{stock_arrow} {chg_pct:+.2f}%</div>
                </div>
                <div style="flex:1; background:#0c0e1c; border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; text-align:center;">
                    <div style="color:#7d86a6; font-size:13px; margin-bottom:4px;">ตลาดรวม · S&P500 (SPY)</div>
                    <div style="font-size:30px; font-weight:700; color:{spy_color}; font-family:'IBM Plex Mono', monospace;">{spy_arrow} {spy_pct:+.2f}%</div>
                </div>
            </div>
            <div style="background:{verdict_bg}; border:1px solid {verdict_fg}; border-radius:10px; padding:10px 16px; margin-bottom:4px; text-align:center;">
                <span style="color:{verdict_fg}; font-weight:700; font-size:16px;">{verdict_text}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("ตารางอธิบาย: หุ้นคุณ vs ตลาดรวม แปลว่าอะไรบ้าง"):
            st.markdown(
                """
| หุ้นคุณ | ตลาดรวม | แปลว่า |
|---|---|---|
| 🟢 เขียว | 🟢 เขียว | ขึ้นตามตลาด ปกติ |
| 🟢 เขียว | 🔴 แดง | **แข็งแกร่งกว่าตลาด** น่าสนใจ |
| 🔴 แดง | 🟢 เขียว | **อ่อนแอกว่าตลาด** ต้องระวัง |
| 🔴 แดง | 🔴 แดง | ลงตามตลาด ปกติ |
                """
            )
        st.write("")


# =================================================================
# Sidebar
# =================================================================
# ชื่อโหมดที่แสดงในเมนู (ค่าจริงของ mode ยังเป็นชื่อเดิมทุกอย่าง โค้ดส่วนอื่นไม่ต้องแก้)
MODE_LABELS = {
    "🏠 หน้าแรก": "🏠 HOME · หน้าแรก",
    "⚡ หุ้นซิ่ง": "⚡ FAST TRADE · หุ้นซิ่ง",
    "📓 สมุดเทรด": "📓 TRADE LOG · สมุดเทรด",
    "🔍 วิเคราะห์หุ้นรายตัว": "🔍 DEEP SCAN · รายตัว",
    "🧠 มุมมองเชิงลึก": "🧠 DEEP INSIGHT · มุมมองเชิงลึก",
    "🧭 คัดกรองหุ้นคุณภาพ": "🧭 QUALITY SCREEN · คัดกรองคุณภาพ",
    "📊 กราฟโปร": "📊 PRO CHART · กราฟโปร",
    "⚖️ เทียบหุ้น": "⚖️ VERSUS · เทียบหุ้น",
    "📅 ปฏิทินเหตุการณ์": "📅 CALENDAR · ปฏิทิน",
    "📈 ภาพรวมตลาด": "📈 MARKET GRID · ภาพรวมตลาด",
    "🚀 สแกนเนอร์ Watchlist": "🚀 SCANNER · สแกนเนอร์",
    "💡 ไอเดียตามธีม": "💡 THEMES · ไอเดียธีม",
    "🧮 เครื่องมือคำนวณ": "🧮 CALC LAB · เครื่องมือคำนวณ",
    "📰 เรดาร์ข่าว": "📰 NET WATCH · เรดาร์ข่าว",
    "🏆 หุ้นเด่น": "🏆 TOP PICKS · หุ้นที่ดีที่สุด",
    "📖 ศัพท์": "📖 CODEX · ศัพท์ & วิธีใช้",
}

with st.sidebar:
    theme.brand_sidebar()

    mode = st.radio(
        "โหมดการใช้งาน",
        ["🏠 หน้าแรก", "🏆 หุ้นเด่น", "⚡ หุ้นซิ่ง", "📓 สมุดเทรด", "📈 ภาพรวมตลาด", "🔍 วิเคราะห์หุ้นรายตัว", "🧠 มุมมองเชิงลึก", "🧭 คัดกรองหุ้นคุณภาพ", "📊 กราฟโปร", "🚀 สแกนเนอร์ Watchlist",
         "💡 ไอเดียตามธีม", "📅 ปฏิทินเหตุการณ์", "📰 เรดาร์ข่าว", "⚖️ เทียบหุ้น", "🧮 เครื่องมือคำนวณ", "📖 ศัพท์"],
        index=0,
        label_visibility="collapsed",
        format_func=lambda m: MODE_LABELS.get(m, m),
    )

    # อัปเดตราคาอัตโนมัติทุก 30 วินาทีเสมอ (ไม่มีตัวเลือกให้ปรับ) และไม่ใช้คีย์ AI ในแถบนี้
    refresh_interval = "30s"
    ai_key = ""

    fx.control()


# =================================================================
# แถบราคาเลื่อนด้านบน (ทุกโหมด) — ถ้าดึงไม่ได้ก็ข้ามเงียบ ๆ
# =================================================================
_mk = {}
try:
    _mk = home_ui._markets()
    theme.ticker_tape(_mk)
except Exception:
    pass
theme.hud(_mk)
fx.apply()

# =================================================================
# โหมด: หน้าแรก / ไอเดียตามธีม / เครื่องมือคำนวณ (แต่ละโหมด render แล้ว st.stop)
# =================================================================
if mode.startswith("🏠"):
    theme.hero("หน้าแรก — DASHBOARD", "ดัชนีตลาด · Sector Rotation · ปฏิทินงบ · ราคาเป้าหมาย · Insider · ข่าว ของหุ้นใน Watchlist", "LIVE")
    try:
        import morning_ui  # morning_ui.py - สรุปเช้านี้ (อ่านจบใน 1 นาที) วางบนสุดของหน้าแรก
        morning_ui.render_morning()
    except Exception as _e_mo:
        st.caption("สรุปเช้านี้แสดงไม่ได้ตอนนี้: " + str(_e_mo)[:80])
    home_ui.render_home()
    st.stop()

if mode.startswith("⚡"):
    theme.hero("หุ้นซิ่ง — FAST TRADE", "สแกนแรงวันนี้ · ปริมาณซื้อขาย · ความผันผวน ATR · ตัวคำนวณขนาดไม้ · ระยะตัดขาดทุน")
    fast_ui.render_fast()
    st.stop()

if mode.startswith("🧠"):
    theme.hero("มุมมองเชิงลึก — DEEP INSIGHT", "สรุปเข้าใจง่าย · 7 มุมมองจากงบและประมาณการ · แนวโน้มระยะสั้น/กลาง/ยาว · สิ่งที่น่าจะมีผลเร็วๆ นี้ · AI เรียบเรียงเป็นบทวิเคราะห์", "INSIGHT")
    if "ins_ticker" not in st.session_state:
        st.session_state["ins_ticker"] = st.session_state.get("_sb_ticker", "NVDA")
    if "ins_sym" not in st.session_state:
        st.session_state["ins_sym"] = st.session_state["ins_ticker"]

    with st.form("insight_form", border=False):
        _i1, _i2 = st.columns([3, 1], vertical_alignment="bottom")
        _it = _i1.text_input("รหัสหุ้น (Ticker)", key="ins_ticker", placeholder="เช่น NVDA, AMD, AAPL").upper().strip()
        _go = _i2.form_submit_button("▶  ดูมุมมองเชิงลึก", use_container_width=True)
    if _go and _it:
        st.session_state["ins_sym"] = _it
    _sym = st.session_state.get("ins_sym") or _it
    if not _sym:
        st.info("พิมพ์รหัสหุ้นแล้วกด ▶ ดูมุมมองเชิงลึก ครับ")
        st.stop()
    st.session_state["_sb_ticker"] = _sym
    _ai_later = insight.render_insight(_sym, ai_key, defer_ai=True)
    try:
        import dropdx
        dropdx.render(_sym)
    except Exception as _dx_err:
        st.caption("ส่วนวินิจฉัยการปรับฐานแสดงไม่ได้ตอนนี้: %s" % _dx_err)
    if callable(_ai_later):
        _ai_later()      # บทวิเคราะห์จาก AI อยู่ล่างสุดเสมอ
    st.stop()

if mode.startswith("🧭"):
    theme.hero("คัดกรองหุ้นคุณภาพ — QUALITY SCREEN", "S&P 500 / Nasdaq 100 · 7 เกณฑ์คุณภาพ+เติบโต · มูลค่า (PEG/DCF) · โมเมนตัม (RS) · F-Score · เปิดมุมมองเชิงลึกต่อได้", "SCREEN")
    screener.render_screener(ai_key)
    st.stop()

if mode.startswith("📊"):
    theme.hero("กราฟโปร — PRO CHART", "แท่งเทียน · EMA · Volume · RSI · แนวรับ/แนวต้าน · เครื่องมือคำนวณ · อ่านกราฟให้ฟัง", "CHART")
    chart_pro.render_chart_pro()
    st.stop()

if mode.startswith("⚖️"):
    theme.hero("เทียบหุ้น — VERSUS", "วางหุ้น 2–3 ตัวข้างกัน · คะแนน 10 มิติ · แนวรับ/แนวต้าน · ข่าวแปลไทย", "VERSUS")
    compare_ui.render_compare(ai_key)
    st.stop()

if mode.startswith("📅"):
    theme.hero("ปฏิทินเหตุการณ์ — CALENDAR", "วันประกาศงบ · XD/ปันผล · ประชุมเฟด ของหุ้นที่คุณติดตาม รวมไว้หน้าเดียว", "CALENDAR")
    calendar_ui.render_calendar()
    st.stop()

if mode.startswith("💡"):
    theme.hero("ไอเดียตามธีม — THEMES", "จัดหุ้นตามเรื่องที่ตลาดสนใจ · กลุ่มไหนร้อน กลุ่มไหนใกล้แนวรับ · แก้ไขธีมเองได้", "THEMES")
    themes_ui.render_themes()
    st.stop()

if mode.startswith("🏆"):
    theme.hero("TOP PICKS — หุ้นที่ดีที่สุด", "รวมคุณภาพ · การเติบโต · ราคา · แรงตลาด ให้เหลือ 10 ตัวที่ผ่านเกณฑ์ดีที่สุด · พร้อมบันทึกผลย้อนหลัง", "TOP")
    try:
        import best_ui
        best_ui.render_best()
    except Exception as _e_bp:
        st.error("หน้านี้แสดงไม่ได้ตอนนี้: " + str(_e_bp)[:160])
    st.stop()

if mode.startswith("📖"):
    theme.hero("ศัพท์ & วิธีใช้ — CODEX", "รวมคำที่เจอในเว็บ แปลเป็นภาษาง่ายๆ · เกณฑ์ดี/ระวัง · ค้นคำได้", "CODEX")
    try:
        import glossary_ui
        glossary_ui.render_glossary()
    except Exception as _e_gl:
        st.error("หน้าศัพท์แสดงไม่ได้ตอนนี้: " + str(_e_gl)[:120])
    st.stop()

if mode.startswith("📓"):
    theme.hero("สมุดเทรด — TRADE LOG", "จดไม้ที่เข้า · จุดตัดขาดทุน · กำไรขาดทุนสด · เตือน FLATLINE และวันงบ", "LOG")
    try:
        import journal_ui
        journal_ui.render_journal()
    except Exception as _e_tj:
        st.error("สมุดเทรดแสดงไม่ได้ตอนนี้: " + str(_e_tj)[:120])
    st.stop()

if mode.startswith("🧮"):
    theme.hero("เครื่องมือคำนวณ — TOOLKIT", "ต้นทุนเฉลี่ย · รอซื้อที่แนวรับ · ขนาดตำแหน่งตามความเสี่ยง · DCF", "TOOLS")
    tools_ui.render_tools()
    st.stop()

# =================================================================
# โหมด: สแกนเนอร์ Watchlist — แนวรับ/แนวต้านรวมเป็นโซน + RSI + โมเมนตัม + R:R
# ถ้าอยู่โหมดนี้ จะ render หน้านี้แล้วหยุด (st.stop)
# =================================================================
if mode.startswith("🚀"):
    theme.hero("สแกนเนอร์ — LEVEL SCANNER", "สแกน Watchlist ของคุณ หรือทั้ง S&P 500 + Nasdaq 100 · แนวรับ/แนวต้านรวมเป็นโซน · RSI วัน/ชั่วโมง · โมเมนตัม · R:R · กรองตามเงื่อนไข", "LIVE")
    rocket_ui.render_scanner(refresh_interval)
    st.stop()


# =================================================================
# โหมด: ภาพรวมตลาด — หุ้นขึ้นแรงสุด/ลงแรงสุด + หุ้นใหญ่แต่ละกลุ่มอุตสาหกรรม
# =================================================================
if mode.startswith("📈"):
    st.markdown(
        f"""
        <div class="app-header">
            {theme._mark("hero")}
            <div class="title-text">
                <h1>ภาพรวมตลาด — MARKET OVERVIEW</h1>
                <p>สแกนหุ้นสหรัฐทั้งตลาด + หุ้นใหญ่ของทั้ง 11 กลุ่มอุตสาหกรรม</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.caption("ข้อมูลฟรีจาก Yahoo อาจดีเลย์ราว 15 นาที ใช้ดูบรรยากาศตลาด ไม่ใช่คำแนะนำซื้อ-ขาย")

    @st.cache_data(ttl=300, show_spinner=False)
    def cached_market_snapshot():
        return market_overview.get_market_snapshot()

    @st.cache_data(ttl=300, show_spinner=False)
    def cached_movers():
        return market_overview.get_market_movers(size=10)

    @st.cache_data(ttl=900, show_spinner=False)
    def cached_sector_leaders():
        return market_overview.get_sector_leaders(top_n=5)

    with st.spinner("กำลังสแกนหุ้นทั้งตลาดสหรัฐ..."):
        movers = cached_movers()
        sector_data = cached_sector_leaders()
        snapshot = {"available": False}
        if not movers.get("available") or not sector_data.get("available"):
            snapshot = cached_market_snapshot()  # ตัวสำรอง: รายชื่อที่คัดไว้

    broad = movers.get("available", False)
    if not broad and not snapshot.get("available"):
        st.error(f"ดึงข้อมูลภาพรวมตลาดไม่สำเร็จ ({movers.get('reason', 'ไม่ทราบสาเหตุ')}) ลองรีเฟรชอีกครั้งในอีกสักครู่")
        st.stop()

    names = {}
    if broad:
        gainers = [(m["symbol"], m["change_pct"], m["price"]) for m in movers["gainers"]]
        losers = [(m["symbol"], m["change_pct"], m["price"]) for m in movers["losers"]]
        names = {m["symbol"]: m["name"] for m in movers["gainers"] + movers["losers"] + movers["actives"]}
        st.caption("สแกนจากหุ้นสหรัฐทั้งตลาด (เฉพาะบริษัทมูลค่าตลาด ≥ 2 พันล้านดอลลาร์ ราคา ≥ 5 ดอลลาร์) ไม่จำกัดรายชื่อ")
    else:
        gainers, losers = market_overview.top_movers(snapshot, n=5)
        st.caption("สแกนทั้งตลาดไม่สำเร็จ แสดงจากรายชื่อหุ้นที่คัดไว้แทน (ลอง pip install -U yfinance)")

    _lbl = "หุ้นขึ้นแรงสุด / ลงแรงสุด (ทั้งตลาดสหรัฐ)" if broad else "หุ้นขึ้นแรงสุด / ลงแรงสุด (จากกลุ่มที่คัดไว้)"
    st.markdown(f'<div class="section-label">{_lbl}</div>', unsafe_allow_html=True)

    _spy = cached_live_quote("SPY")
    if _spy.get("available") and _spy.get("change_pct") is not None:
        _sp = _spy["change_pct"]
        if _sp < 0:
            st.error(f"🔴 วันนี้ตลาดแดง (SPY {_sp:+.2f}%) — หุ้นเขียวด้านล่างคือตัวที่ขึ้นสวนตลาด")
        else:
            st.success(f"🟢 วันนี้ตลาดเขียว (SPY {_sp:+.2f}%)")

    col_g, col_l = st.columns(2)
    with col_g:
        st.markdown("**🟢 ขึ้นแรงสุด**")
        for t, chg, price in gainers:
            st.write(f"**{t}** {names.get(t, '')[:22]}  ·  &#36;{price:,.2f}  ·  :green[{chg:+.2f}%]")
    with col_l:
        st.markdown("**🔴 ลงแรงสุด**")
        for t, chg, price in losers:
            st.write(f"**{t}** {names.get(t, '')[:22]}  ·  &#36;{price:,.2f}  ·  :red[{chg:+.2f}%]")

    if broad and movers.get("actives"):
        with st.expander("🔥 ซื้อขายคึกคักสุดวันนี้ (ปริมาณซื้อขายสูงสุด)"):
            for m in movers["actives"]:
                col = "green" if m["change_pct"] >= 0 else "red"
                vol = (m.get("volume") or 0) / 1e6
                st.write(f"**{m['symbol']}** {m['name'][:22]}  ·  &#36;{m['price']:,.2f}  ·  :{col}[{m['change_pct']:+.2f}%]  ·  ปริมาณ {vol:,.1f} ล้านหุ้น")

    st.write("")
    chart_tickers = [t for t, _, _ in gainers] + [t for t, _, _ in losers]
    chart_values = [chg for _, chg, _ in gainers] + [chg for _, chg, _ in losers]

    @st.cache_data(ttl=300, show_spinner=False)
    def cached_history(tickers_tuple):
        return market_overview.get_normalized_history(list(tickers_tuple), period="1mo")

    st.markdown('<div class="section-label">ผลตอบแทนหุ้นใหญ่แต่ละกลุ่มอุตสาหกรรม · เลือกช่วงย้อนหลังได้ (เรียงจากกลุ่มที่แรงสุด)</div>', unsafe_allow_html=True)

    # รวมข้อมูลกลุ่มอุตสาหกรรมให้อยู่รูปเดียวกัน (ใช้ข้อมูลกว้างก่อน ถ้าไม่ได้ค่อยใช้รายชื่อที่คัดไว้)
    sector_view = {}
    if sector_data.get("available"):
        sector_view = sector_data["sectors"]
    elif snapshot.get("available"):
        for sector, tickers in market_overview.SECTOR_LEADERS.items():
            rows = [
                {"symbol": t, "price": snapshot["data"][t]["price"], "change_pct": snapshot["data"][t]["change_pct"]}
                for t in tickers if t in snapshot["data"]
            ]
            if rows:
                sector_view[sector] = {"stocks": rows, "avg_change": sum(r["change_pct"] for r in rows) / len(rows)}

    # ---- เลือกช่วงเวลาย้อนหลัง ----
    import sector_history as _sh
    _plist = list(_sh.PERIODS.keys())
    if "sec_period" not in st.session_state:
        st.session_state["sec_period"] = "วันนี้"
    st.session_state["sec_period"] = st.session_state["sec_period"]  # keep-alive ข้ามหน้า
    _period = st.radio("ดูผลตอบแทนย้อนหลัง", _plist, horizontal=True, key="sec_period")
    _start = None
    if _period == "กำหนดวันเอง":
        import datetime as _dt
        _start = st.date_input("เริ่มนับจากวันที่", value=_dt.date.today() - _dt.timedelta(days=90),
                               min_value=_dt.date.today() - _dt.timedelta(days=700), max_value=_dt.date.today(), key="sec_start")

    if _period != "วันนี้" and sector_view:
        _syms = tuple({r["symbol"] for i in sector_view.values() for r in i["stocks"]})
        with st.spinner("กำลังคำนวณผลตอบแทนย้อนหลัง..."):
            _ret, _bd, _ld = _sh.period_returns(_syms, _period, _start)
        if _ret:
            _new = {}
            for _sec, _inf in sector_view.items():
                _rows = [{"symbol": r["symbol"], "price": _ret[r["symbol"]]["price"], "change_pct": _ret[r["symbol"]]["pct"]}
                         for r in _inf["stocks"] if r["symbol"] in _ret]
                if _rows:
                    _new[_sec] = {"stocks": _rows, "avg_change": sum(r["change_pct"] for r in _rows) / len(_rows)}
            sector_view_show = _new
            st.caption(f"เทียบราคาปิดวันที่ {_bd:%d/%m/%Y} → ล่าสุด {_ld:%d/%m/%Y} (ปรับตามช่วงที่เลือก ไม่รวมปันผล)")
        else:
            sector_view_show = sector_view
            st.caption("ดึงข้อมูลย้อนหลังไม่สำเร็จ แสดงของวันนี้แทน")
    else:
        sector_view_show = sector_view

    # เรียงกลุ่มที่แข็งแรงสุดไว้บนสุด
    for sector, info in sorted(sector_view_show.items(), key=lambda kv: kv[1]["avg_change"], reverse=True):
        avg = info["avg_change"]
        icon = "🟢" if avg > 0 else ("🔴" if avg < 0 else "⚪")
        with st.expander(f"{icon} {sector}  ·  เฉลี่ย {avg:+.2f}%"):
            rows = info["stocks"]
            cols = st.columns(len(rows))
            for i, d in enumerate(rows):
                chg = d["change_pct"]
                color = "#19f5a5" if chg > 0 else ("#ff2a6d" if chg < 0 else "#7d86a6")
                cols[i].markdown(
                    f"""
                    <div style="text-align:center;">
                        <div style="color:#7d86a6; font-size:13px;">{d['symbol']}</div>
                        <div style="font-size:18px; font-weight:700; color:#e6f1ff;">&#36;{d['price']:,.2f}</div>
                        <div style="color:{color}; font-weight:600;">{chg:+.2f}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    if not sector_view:
        st.caption("ดึงข้อมูลกลุ่มอุตสาหกรรมไม่สำเร็จ ลองรีเฟรชอีกครั้ง")

    st.markdown("---")

    st.markdown('<div class="section-label">แนวโน้มราคา 1 เดือน (% เทียบวันแรก)</div>', unsafe_allow_html=True)
    hist_result = cached_history(tuple(chart_tickers))
    if hist_result.get("available"):
        hdf = hist_result["df"]
        options = [t for t in chart_tickers if t in hdf.columns]
        today_chg = {t: c for t, c, _ in gainers + losers}
        pick = st.selectbox(
            "เลือกหุ้นที่อยากดูกราฟ",
            options,
            format_func=lambda t: f"{t}  (วันนี้ {today_chg.get(t, 0):+.2f}%)",
        )
        series = hdf[pick].dropna()
        month_chg = float(series.iloc[-1])
        up = month_chg >= 0
        m1, m2 = st.columns(2)
        m1.metric("ราคาเปลี่ยนใน 1 เดือน", f"{month_chg:+.2f}%")
        m2.metric("วันนี้", f"{today_chg.get(pick, 0):+.2f}%")
        st.line_chart(
            series.rename(pick).to_frame(),
            color="#19f5a5" if up else "#ff2a6d",
            height=300,
        )
        st.caption("เส้นเริ่มที่ 0% ถ้าเส้นอยู่เหนือ 0 แปลว่าราคาสูงกว่าเมื่อเดือนก่อน")
    else:
        st.caption(f"วาดกราฟเส้นไม่ได้ ({hist_result.get('reason', 'ไม่ทราบสาเหตุ')}) แสดงกราฟแท่งแทน")
        chart_df = pd.DataFrame({"% เปลี่ยนแปลงวันนี้": chart_values}, index=chart_tickers)
        st.bar_chart(chart_df, color="#5ee7ff")


    st.markdown("---")
    st.markdown('<div class="section-label">🚀 สแกนโมเมนตัม — หุ้นแข็งแรงสุดตามงานวิจัย</div>', unsafe_allow_html=True)
    _scan_syms = []
    for _info in sector_view.values():
        _scan_syms += [_r["symbol"] for _r in _info["stocks"]]
    _scan_syms += [_t for _t, _, _ in gainers] + [_t for _t, _, _ in losers]
    momentum_ui.render_scan(_scan_syms)

    st.markdown("---")
    st.caption(
        "ข้อมูลนี้เป็นภาพรวมเร็วๆ เพื่อดูบรรยากาศตลาด ไม่ใช่คำแนะนำซื้อ-ขาย "
        "อยากวิเคราะห์เจาะลึกหุ้นตัวไหน สลับไปโหมด '🔍 วิเคราะห์หุ้นรายตัว' แล้วพิมพ์ชื่อหุ้นนั้นได้เลย"
    )

    st.stop()


# =================================================================
# โหมด: เรดาร์ข่าว (Watchlist) — แยกออกจากการวิเคราะห์หุ้นรายตัวโดยสิ้นเชิง
# ถ้าอยู่โหมดนี้ จะ render หน้านี้แล้วหยุด (st.stop) ไม่รันโค้ดวิเคราะห์หุ้นด้านล่างต่อ
# =================================================================
if mode.startswith("📰"):
    st.markdown(
        f"""
        <div class="app-header">
            {theme._mark("hero")}
            <div class="title-text">
                <h1>เรดาร์ข่าว — NEWS RADAR</h1>
                <p>ข่าวล่าสุดของหุ้นที่คุณเฝ้าดู แปล + สรุปเป็นภาษาไทย เรียงใหม่สุดก่อน</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    _nt0, _nt1, _nt2 = st.tabs(["📝 สรุปตลาดวันนี้", "🌐 เหตุการณ์ตลาด (ขยับหลายตัวพร้อมกัน)", "📰 ข่าวหุ้นใน Watchlist"])
    with _nt0:
        market_brief.render_market_brief(ai_key)
    with _nt1:
        market_events.render_market_events(ai_key)
    with _nt2:
        news_feed.render(ai_key)  # news_feed.py — ฟีดข่าวภาษาไทย แปล+สรุป

    st.stop()  # หยุดตรงนี้ ไม่รันโค้ดวิเคราะห์หุ้นรายตัวด้านล่างต่อ


# =================================================================
# โหมด: วิเคราะห์หุ้นรายตัว (โหมดหลัก — โค้ดเดิมทั้งหมดด้านล่างนี้ไม่เปลี่ยนแปลง)
# =================================================================

# =================================================================
# หัวเรื่องหลัก
# =================================================================
st.markdown(
    f"""
    <div class="app-header">
        {theme._mark("hero")}
        <div class="title-text">
            <h1>QUANT STOCK ANALYZER</h1>
            <p>ระบบให้คะแนน 10 มิติจากข้อมูลจริง · ประมวลผลด้วยสูตรเชิงปริมาณ · ไม่ต้องมีคีย์ใดๆ</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

with st.expander("📖 คู่มือดูหน้านี้ใน 1 นาที (กดอ่านก่อนถ้ายังไม่คุ้น)", expanded=False):
    st.markdown(
        """
**สรุปสั้นสุด:** ดูคะแนนใหญ่ตัวเดียวในกล่อง **"◆ สรุปสุดท้าย"** (อยู่บนสุดของผลลัพธ์ ใต้แถบราคา) —
เขียวมากกว่า +25% = น่าสนใจ, แดงน้อยกว่า -25% = ควรระวัง, อยู่กลางๆ = ยังไม่ชัดเจน
นั่นคือตัวเลขสำคัญที่สุด ไม่ต้องอ่านอย่างอื่นก็พอ

**ถ้าอยากรู้ว่าทำไมได้คะแนนแบบนั้น** ให้กดดูทีละแท็บด้านล่าง (① ถึง ⑦ เรียงเป็นขั้นให้แล้ว):

| ขั้น | ชื่อกล่องในหน้านี้ | ตอบคำถามว่า |
|---|---|---|
| 1 | โซนราคาอ้างอิง | ราคาตอนนี้ถูกหรือแพงเทียบกับอดีต |
| 2 | บทวิเคราะห์ 10 มิติ | ธุรกิจพื้นฐานดีไหม |
| 3 | ทดสอบย้อนหลัง (Backtest) | เชื่อกราฟเทคนิคได้แค่ไหน |
| 4 | แนวโน้มระยะสั้น | คนวงใน/สถาบัน/นักวิเคราะห์คิดยังไง |
| 5 | สัญญาณเสริม + ตลาดรวม | หุ้นนี้แรงกว่าตลาด S&P500 ไหม, มีข่าวใหญ่ใกล้ๆ ไหม |

**เทียบกับตลาดรวมวันนี้ยังไง?** ดูที่กล่อง **"ความแข็งแกร่งเทียบตลาด S&P500"** ในขั้นที่ 5
— ถ้าหุ้นคุณเขียวตอนตลาดรวมแดง = สัญญาณดี (แข็งแกร่งกว่าตลาด)

**ราคาสดอัปเดตเองไหม?** แผงราคาบนสุดอัปเดตอัตโนมัติ ไม่ต้องกด refresh —
ส่วนที่เหลือ (10 มิติ, Backtest ฯลฯ) เปลี่ยนช้า ไม่ต้องรออัปเดตเป็นวินาที

⚠️ ทุกตัวเลขในหน้านี้เป็นข้อมูลประกอบการตัดสินใจ ไม่ใช่คำแนะนำซื้อ-ขาย และไม่มีระบบไหนทำนายราคาได้แม่นยำ 100%
        """
    )

if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "ai_summary" not in st.session_state:
    st.session_state.ai_summary = None

# ช่องกรอกรหัสหุ้น + ปุ่มวิเคราะห์ อยู่ในหน้านี้ (กด Enter ในช่องก็วิเคราะห์ได้)
if "deep_ticker" not in st.session_state:  # ตั้งค่าเริ่มต้นครั้งเดียว (ห้ามเปลี่ยน default ทุกรอบ ไม่งั้นช่องรีเซ็ต)
    st.session_state["deep_ticker"] = st.session_state.get("_sb_ticker", "NVDA")
with st.form("deep_scan_form", border=False):
    _c1, _c2 = st.columns([3, 1], vertical_alignment="bottom")
    ticker_input = _c1.text_input(
        "รหัสหุ้น (Ticker)", key="deep_ticker", placeholder="เช่น NVDA, AAPL, TSLA"
    ).upper().strip()
    btn_analyze = _c2.form_submit_button("▶  วิเคราะห์หุ้น", use_container_width=True)
st.session_state["_sb_ticker"] = ticker_input

if btn_analyze:
    if not ticker_input:
        st.error("กรุณาพิมพ์ชื่อหุ้นก่อนครับ")
    else:
        with st.spinner(f"กำลังประมวลผล {ticker_input} ..."):
            result = cached_full_analysis(ticker_input)
        st.session_state.analysis = result
        st.session_state.ai_summary = None  # เคลียร์สรุปเก่าเมื่อดูหุ้นใหม่

analysis = st.session_state.analysis

_QR_GRAD = {
    "#00f0ff": ("#8ffaff", "#00c2e0"),   # ฟ้า (ข้อมูลทั่วไป)
    "#19f5a5": ("#8dffd0", "#00d17f"),   # เขียว (ดี)
    "#fcee0a": ("#fff59a", "#ffc400"),   # เหลือง (กลางๆ)
    "#ff9f1c": ("#ffd08a", "#ff8a00"),   # ส้ม (ระวัง)
    "#ff2a6d": ("#ff8aa8", "#ff2457"),   # แดง (ไม่ดี)
    "#7d86a6": ("#aab3d0", "#7d86a6"),   # เทา (ไม่มีข้อมูล)
}


def _qr_kv(rows):
    """แถวข้อมูลแบบ ป้าย | ค่า (ค่าเป็น HTML ที่ escape แล้ว)"""
    return '<div class="qr-kv">' + "".join('<span class="k">{}</span><span class="v">{}</span>'.format(k, v) for k, v in rows) + "</div>"


def _qr_chips(items, label=""):
    """ชิปโอกาส: [(ป้าย, ความน่าจะเป็น 0-1, ข้อความ)] พื้นหลังเติมไล่สีตามเปอร์เซ็นต์"""
    out = []
    for lab, p, txt in items:
        w = max(3.0, min(100.0, p * 100))
        out.append('<span class="qr-chip" style="--w:{:.0f}%"><i>{}</i><b>{}</b></span>'.format(w, lab, txt))
    lb = '<span class="qr-cl">{}</span>'.format(label) if label else ""
    return '<div class="qr-chips">' + lb + "".join(out) + "</div>"


def _qr_level(icon, name, price, rel, chips_html, cls="up"):
    return ('<div class="qr-lv"><div class="h"><span class="n">{} {}</span><b>${:,.2f}</b><em class="{}">{}</em></div>{}</div>'
            .format(icon, name, price, cls, rel, chips_html))


def _qr_range(lo, hi, px, lo_lbl="ต่ำสุดที่คาด", hi_lbl="สูงสุดที่คาด"):
    pos = 50.0 if hi <= lo else max(0.0, min(100.0, (px - lo) / (hi - lo) * 100))
    return ('<div class="qr-tk"><u style="left:{:.1f}%"></u></div>'
            '<div class="qr-rc"><div><span>{}</span><b>${:,.2f}</b><em class="dn">{:+.1f}%</em></div>'
            '<div class="c"><span>ตอนนี้</span><b>${:,.2f}</b></div>'
            '<div class="r"><span>{}</span><b>${:,.2f}</b><em class="up">{:+.1f}%</em></div></div>'
            ).format(pos, lo_lbl, lo, (lo / px - 1) * 100, px, hi_lbl, hi, (hi / px - 1) * 100)


def _qr_ud(up, dn):
    return '<span class="qr-ud up">▲ {}</span><span class="qr-ud dn">▼ {}</span>'.format(up, dn)


def _qr_tools(info: dict, price):
    """ตัวช่วยร่วมของการ์ดอ่านเร็ว: คืน (num, px, card, สี)"""
    import html as _h

    def num(k):
        v = info.get(k)
        return float(v) if isinstance(v, (int, float)) and v == v else None

    px = float(price) if isinstance(price, (int, float)) else num("regularMarketPrice")
    CY, GR, YE, OR, RD, GY = "#00f0ff", "#19f5a5", "#fcee0a", "#ff9f1c", "#ff2a6d", "#7d86a6"

    def card(title, verdict, color, sub, frac=None, mark=None, tip="", tag="", future=False):
        g1, g2 = _QR_GRAD.get(color, (color, color))
        bar = ""
        if frac is not None:
            f = max(0.0, min(1.0, frac)) * 100
            m = f"<b style=\"left:{max(0.0, min(1.0, mark)) * 100:.1f}%\"></b>" if mark is not None else ""
            bar = f'<div class="qr-bar"><i style="width:{f:.1f}%;background:linear-gradient(90deg,{g2},{g1});box-shadow:0 0 8px {g2}88"></i>{m}</div>'
        tag_html = ""
        if tag:
            tag_html = '<span class="qr-tag' + (" fut" if future else "") + '">' + _h.escape(tag) + "</span>"
        return (f'<div class="qr-card" style="--ac:{g2}" title="{_h.escape(tip, quote=True)}"><div class="qr-t"><span>{_h.escape(title)}</span>{tag_html}</div>'
                f'<div class="qr-v" style="background-image:linear-gradient(180deg,{g1},{g2});filter:drop-shadow(0 0 7px {g2}66)">{_h.escape(verdict)}</div>{bar}<div class="qr-s">{sub}</div></div>')
    return num, px, card, (CY, GR, YE, OR, RD, GY)


def _qr_emit(cards):
    """วาดการ์ดทั้งชุด"""
    css = ("<style>.qr-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:12px;margin:6px 0 14px}"
           ".qr-card{background:var(--panel,rgba(12,14,28,.78));border:1px solid var(--line,rgba(0,240,255,.17));padding:12px 14px 12px;"
           "clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}"
           ".qr-t{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;font-size:12px;letter-spacing:.04em;color:#7d86a6;margin-bottom:5px}"
           ".qr-tag{flex:0 0 auto;font-size:10.5px;letter-spacing:.02em;color:#7d86a6;border:1px solid rgba(125,134,166,.4);padding:0 6px;line-height:16px;white-space:nowrap}"
           ".qr-tag.fut{color:#00f0ff;border-color:rgba(0,240,255,.5)}"
           ".qr-v{font-size:1.15rem;font-weight:700;line-height:1.25;margin-bottom:8px;-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent;width:fit-content;max-width:100%}"
           ".qr-kv{display:grid;grid-template-columns:auto 1fr;gap:5px 12px;align-items:baseline}"
           ".qr-kv .k{color:#9aa4c4;font-size:12.5px;white-space:nowrap}.qr-kv .v{color:#f1f5ff;font-size:13px;text-align:right;line-height:1.45}"
           ".qr-ud{display:inline-block;margin-left:6px;padding:0 7px;font-size:12px;font-weight:700;line-height:18px;border:1px solid}"
           ".qr-ud:first-child{margin-left:0}.qr-ud.up{color:#19f5a5;border-color:rgba(25,245,165,.5);background:rgba(25,245,165,.10)}"
           ".qr-ud.dn{color:#ff5a85;border-color:rgba(255,42,109,.5);background:rgba(255,42,109,.10)}"
           ".qr-cap{margin-top:9px;padding-top:8px;border-top:1px dashed rgba(125,134,166,.28);font-size:12px;color:#9aa4c4;line-height:1.55}"
           ".qr-warn{margin-top:8px;padding:4px 8px;font-size:11.5px;color:#ffb347;background:rgba(255,179,71,.09);border-left:2px solid #ffb347}"
           ".qr-lv{margin:0 0 9px}.qr-lv:last-child{margin-bottom:0}"
           ".qr-lv .h{display:flex;align-items:baseline;gap:8px}.qr-lv .n{color:#c0c9e4;font-size:13px}"
           ".qr-lv .h b{font-size:1.02rem;color:#e6f1ff}.qr-lv .h em{margin-left:auto;font-style:normal;font-size:14px;font-weight:700;padding:0 8px;line-height:22px;border:1px solid}"
           ".qr-lv .h em.up{color:#19f5a5;border-color:rgba(25,245,165,.5);background:rgba(25,245,165,.10)}.qr-lv .h em.dn{color:#ff5a85;border-color:rgba(255,42,109,.5);background:rgba(255,42,109,.10)}"
           ".qr-chips{display:flex;flex-wrap:wrap;gap:5px;margin-top:5px;align-items:center}"
           ".qr-cl{flex-basis:100%;font-size:12px;color:#9aa4c4}"
           ".qr-chip{display:inline-flex;gap:5px;align-items:baseline;padding:2px 8px;font-size:12px;color:#c0c9e4;border:1px solid rgba(154,164,196,.35);background:rgba(255,255,255,.04)}"
           ".qr-chip i{font-style:normal;color:#c0c9e4}.qr-chip b{color:#fff;font-weight:700}"
           ".qr-tk{position:relative;height:5px;margin:8px 0 10px;background:linear-gradient(90deg,#ff2457,#ffc400 50%,#19f5a5)}"
           ".qr-tk u{position:absolute;top:-5px;width:3px;height:15px;background:#fff;box-shadow:0 0 6px #fff;margin-left:-1px}"
           ".qr-rc{display:grid;grid-template-columns:1fr auto 1fr;gap:8px}.qr-rc>div{display:flex;flex-direction:column;gap:1px}"
           ".qr-rc .c{align-items:center;text-align:center}.qr-rc .r{align-items:flex-end;text-align:right}"
           ".qr-rc span{font-size:12px;color:#9aa4c4}.qr-rc b{font-size:1.02rem;color:#fff;white-space:nowrap}"
           ".qr-rc em{font-style:normal;font-size:13px;font-weight:700}.qr-rc em.up{color:#19f5a5}.qr-rc em.dn{color:#ff5a85}"
           ".qr-bar{position:relative;height:5px;background:#1b1e2e;margin:0 0 8px}.qr-bar i{display:block;height:100%}"
           ".qr-bar b{position:absolute;top:-4px;width:3px;height:13px;background:#fff;box-shadow:0 0 6px #fff;margin-left:-1px}"
           ".qr-s{font-size:13px;color:#c0c9e4;line-height:1.5}.qr-s b{color:#e6f1ff;font-weight:600}.qr-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;align-items:stretch}@media (max-width:1100px){.qr-grid{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}}.qr-card{display:flex;flex-direction:column;padding:15px 17px 14px;border-top:2px solid var(--ac,#00f0ff);background:linear-gradient(180deg,rgba(0,240,255,.07),rgba(12,14,28,.88) 42%);transition:transform .2s}.qr-card:hover{transform:translateY(-2px)}.qr-s{flex:1}.qr-t{font-size:12.5px;color:#9aa4c4;margin-bottom:7px;padding-bottom:7px;border-bottom:1px dashed rgba(125,134,166,.25)}.qr-tag{border-radius:0;background:rgba(0,0,0,.25)}.qr-v{font-size:1.32rem;margin-bottom:11px;letter-spacing:.01em}.qr-bar{height:7px;border-radius:4px;background:#171a2b;margin-bottom:10px}.qr-bar i{border-radius:4px}.qr-bar b{top:-4px;height:15px;width:3px;border-radius:2px}.qr-chip{background:rgba(255,255,255,.05);border-color:rgba(154,164,196,.28);padding:2px 9px}.qr-lv .h b{font-size:1.1rem;font-family:var(--mono,monospace)}.qr-lv{padding-bottom:9px;border-bottom:1px solid rgba(125,134,166,.12)}.qr-lv:last-child{border-bottom:0;padding-bottom:0}.qr-rc b{font-family:var(--mono,monospace);font-size:1.1rem}.qr-tk{height:6px;border-radius:3px}</style>")
    st.markdown(css + '<div class="qr-grid">' + "".join(cards) + "</div>", unsafe_allow_html=True)


def render_quick_read(info: dict, price, one_month: dict = None, vol: dict = None):
    """อ่านเร็ว 3 ช่องแบบระยะยาว: ราคาเทียบ 1 ปี · นักวิเคราะห์ · คาดการณ์ 1 เดือน"""
    from math import exp as _math_exp
    num, px, card, (CY, GR, YE, OR, RD, GY) = _qr_tools(info, price)

    cards = []

    # 3) ราคาเทียบจุดสูง/ต่ำของรอบ 52 สัปดาห์ (แถบวัดแบบลอการิทึม: ช่วงราคากว้างหลายเท่าจะได้ไม่เพี้ยน)
    lo, hi = num("fiftyTwoWeekLow"), num("fiftyTwoWeekHigh")
    if px and lo and lo > 0 and hi and hi > lo:
        import math as _m
        from_hi = (px / hi - 1) * 100
        from_lo = (px / lo - 1) * 100
        pos = max(0.0, min(1.0, _m.log(px / lo) / _m.log(hi / lo)))
        if from_lo <= 10:
            v, c = "ใกล้ราคาต่ำสุดของปี", RD
        elif from_hi >= -5:
            v, c = "ใกล้ราคาสูงสุดของปี", YE
        elif from_hi >= -20:
            v, c = "ต่ำกว่าราคาสูงสุดเล็กน้อย", GR
        elif from_hi >= -40:
            v, c = "ลงมาจากราคาสูงสุดพอสมควร", CY
        else:
            v, c = "ลงมาจากราคาสูงสุดเยอะ", OR
        up_txt = f"{px / lo:.1f} เท่า" if from_lo >= 100 else f"{from_lo:.0f}%"
        down_txt = "ใกล้เคียงกัน" if abs(from_hi) < 0.5 else f"ต่ำกว่า {abs(from_hi):.0f}%"
        cards.append(card("ราคาเทียบ 1 ปีที่ผ่านมา", v, c,
                          _qr_kv([("สูงสุดของปี", "<b>${:,.0f}</b> · ตอนนี้{}".format(hi, down_txt)),
                                  ("ต่ำสุดของปี", "<b>${:,.0f}</b> · ตอนนี้สูงกว่า <b>{}</b>".format(lo, up_txt))]),
                          frac=pos, mark=pos,
                          tip="ขีดขาวบนแถบคือราคาตอนนี้ ซ้ายสุด = ราคาต่ำสุดของปี ขวาสุด = ราคาสูงสุดของปี (แถบวัดแบบลอการิทึม)", tag="ย้อนหลัง 52 สัปดาห์"))
    else:
        cards.append(card("ราคาเทียบ 1 ปีที่ผ่านมา", "ยังไม่มีข้อมูล", GY, "ไม่มีราคาสูงสุด/ต่ำสุดของปี"))

    # 4) นักวิเคราะห์มองยังไง
    tgt, n = num("targetMeanPrice"), num("numberOfAnalystOpinions")
    rec = str(info.get("recommendationKey") or "").lower()
    rec_th = {"strong_buy": ("ส่วนใหญ่แนะนำซื้อแรง", GR), "buy": ("ส่วนใหญ่แนะนำซื้อ", GR), "hold": ("ส่วนใหญ่แนะนำถือ", YE),
              "underperform": ("คาดว่าจะแย่กว่าตลาด", OR), "sell": ("ส่วนใหญ่แนะนำขาย", RD)}.get(rec)
    if tgt and px:
        up = (tgt / px - 1) * 100
        v, c = rec_th or (("ประเมินว่าราคายังขึ้นได้", GR) if up >= 5 else ("ราคาใกล้ที่ประเมินไว้แล้ว", YE) if up >= -5 else ("ราคาสูงกว่าที่ประเมินไว้", RD))
        rel = "สูงกว่าตอนนี้ <b>{:.0f}%</b>".format(up) if up >= 0 else "ต่ำกว่าตอนนี้ <b>{:.0f}%</b>".format(abs(up))
        _rows = [("ราคาที่ประเมิน", "เฉลี่ย <b>${:,.0f}</b> · {}".format(tgt, rel))]
        if n:
            _rows.append(("จากนักวิเคราะห์", "<b>{}</b> คน".format(int(n))))
        reach = ""
        _vv = vol if isinstance(vol, dict) and vol.get("available") else None
        if _vv and up > 0:
            # โอกาสที่ราคา "แตะเป้าอย่างน้อยครั้งหนึ่ง" ภายในเวลาที่กำหนด (แบบจำลองสุ่มไม่มีแนวโน้มขึ้น/ลง ใช้ความผันผวน 3 เดือนที่ผ่านมา)
            from math import erf as _erf, log as _log, sqrt as _sqrt
            sig = _vv["daily_sd"] * _sqrt(252)
            a_ = _log(tgt / px)
            def _p(yrs):
                z = a_ / (sig * _sqrt(yrs)) if sig > 0 else 99
                return min(0.99, max(0.0, 2 * (1 - 0.5 * (1 + _erf(z / _sqrt(2))))))
            reach = _qr_chips([("3 เดือน", _p(.25), "~{:.0f}%".format(_p(.25) * 100)),
                               ("6 เดือน", _p(.5), "~{:.0f}%".format(_p(.5) * 100)),
                               ("12 เดือน", _p(1), "~{:.0f}%".format(_p(1) * 100))],
                              "โอกาสที่ราคาจะแตะเป้า <b>${:,.0f}</b> ภายใน".format(tgt))
        cards.append(card("นักวิเคราะห์มองว่า", v, c, _qr_kv(_rows) + reach,
                          frac=max(up, 0) / 100,
                          tip="เป็นความเห็นของนักวิเคราะห์ ไม่ใช่ตัวเลขที่แน่นอน และอาจตามราคาจริงไม่ทัน · โดยทั่วไปเป็นเป้าราคาในอีกราว 12 เดือน · เปอร์เซ็นต์โอกาสแตะเป้าคำนวณจากความผันผวนที่ผ่านมาโดยสมมติว่าราคาไม่มีแนวโน้มขึ้นหรือลง เป็นการประมาณ ไม่ใช่คำทำนาย", tag="อีก ~12 เดือน", future=True))
    else:
        cards.append(card("นักวิเคราะห์มองว่า", "ยังไม่มีข้อมูล", GY, "Yahoo ไม่มีราคาที่นักวิเคราะห์ประเมินไว้ของหุ้นตัวนี้"))

    # 5) คาดการณ์ 1 เดือนข้างหน้า = ทิศทางที่โน้มเอียง (จากโมเมนตัม+เป้านักวิเคราะห์ในระบบเดิม) + ช่วงราคาจากความผันผวนย้อนหลัง
    om = one_month if isinstance(one_month, dict) and one_month.get("available") else None
    vv = vol if isinstance(vol, dict) and vol.get("available") else None
    if om or (vv and px):
        lean = om["lean_pct"] if om else None
        if lean is None:
            v, c = "ดูได้แต่ช่วงราคา", GY
        elif lean > 25:
            v, c = "โน้มเอียงไปทางขึ้น", GR
        elif lean < -25:
            v, c = "โน้มเอียงไปทางลง", RD
        else:
            v, c = "ยังไม่ชัด ไปได้ทั้งสองทาง", YE
        sub = ""
        if vv and px:
            sd = vv["daily_sd"] * (21 ** 0.5)          # 21 วันทำการ ≈ 1 เดือน
            sub += (_qr_range(px * _math_exp(-sd), px * _math_exp(sd), px)
                    + '<div class="qr-cap">เดือนหน้าราคาน่าจะอยู่ในช่วงนี้ (ถูกราว 2 ใน 3 ครั้ง) · คำนวณจากความผันผวน 3 เดือนที่ผ่านมา</div>')
        if om and om.get("earnings_within_month"):
            sub += '<div class="qr-warn">⚠️ มีประกาศงบภายใน 1 เดือน ช่วงจริงอาจกว้างกว่านี้</div>'
        cards.append(card("คาดการณ์ราคา", v, c, sub or "ข้อมูลไม่พอ",
                          tip="ไม่ใช่การทำนายว่าจะขึ้นหรือลงแน่นอน · ทิศทางมาจากโมเมนตัมและราคาเป้าหมายนักวิเคราะห์ · ช่วงราคามาจากความผันผวนที่ผ่านมา (±1 SD ≈ 68%) ถ้ามีข่าวใหญ่ราคาอาจออกนอกช่วงได้",
                          tag="ข้างหน้า 1 เดือน", future=True))
    else:
        cards.append(card("คาดการณ์ราคา", "ยังไม่มีข้อมูล", GY, "ข้อมูลราคาย้อนหลังไม่พอสำหรับคำนวณ", tag="ข้างหน้า 1 เดือน", future=True))

    _qr_emit(cards)


def render_quick_read_short(info: dict, price, sd: dict = None, ana: dict = None):
    """อ่านเร็ว 3 ช่องแบบระยะสั้น (ภายใน ~1 สัปดาห์ = 5 วันทำการ): เพดาน/พื้น · คาดการณ์ · นักวิเคราะห์"""
    from math import erf as _erf, exp as _exp, log as _log, sqrt as _sqrt
    num, px, card, (CY, GR, YE, OR, RD, GY) = _qr_tools(info, price)
    S = sd if isinstance(sd, dict) and sd.get("available") else None
    if S and (not px or px <= 0):
        px = S["last"]
    cards = []

    def _pf(p):
        return "&lt;1%" if p < 0.01 else "{:.0f}%".format(p * 100)

    def _hit(level, days):
        # โอกาสที่ราคาแตะระดับนี้อย่างน้อยครั้งหนึ่งภายใน N วันทำการ (แบบจำลองสุ่ม ไม่คิดแนวโน้ม)
        z = abs(_log(level / px)) / (S["sd20"] * _sqrt(days))
        return min(0.99, max(0.0, 2 * (1 - 0.5 * (1 + _erf(z / _sqrt(2))))))

    # 4) ใกล้แนวรับ/แนวต้านไหม + โอกาสแตะภายใน 1/3/5 วัน
    if S and px:
        sup, res = S["support"], S["resistance"]
        if sup is None and res is None:
            cards.append(card("เพดานใกล้สุด / พื้นใกล้สุด", "ยังไม่พบเพดาน/พื้นที่ชัด", GY, "ราคาอยู่นอกโซนที่เคยกลับตัวบ่อย", tag="ข้างหน้า 1 สัปดาห์", future=True))
        else:
            dsd1 = S["sd20"] * 100
            d_r = (res / px - 1) * 100 if res else None
            d_s = (1 - sup / px) * 100 if sup else None
            if d_r is not None and d_r <= dsd1 and (d_s is None or d_r <= d_s):
                v, c = "ใกล้เพดาน ขึ้นต่อยาก", OR
            elif d_s is not None and d_s <= dsd1:
                v, c = "ใกล้พื้น ถ้าหลุดอาจลงต่อ", CY
            else:
                v, c = "อยู่กลาง ไม่ชิดเพดานหรือพื้น", YE
            def _ch(lv):
                ps = [_hit(lv, 1), _hit(lv, 3), _hit(lv, 5)]
                return _qr_chips([("ภายใน 1 วัน", ps[0], _pf(ps[0])), ("3 วัน", ps[1], _pf(ps[1])), ("1 สัปดาห์", ps[2], _pf(ps[2]))],
                                 "โอกาสที่ราคาจะแตะ <b>${:,.2f}</b>".format(lv))
            rows = []
            if res:
                rows.append(_qr_level("⬆", "เพดาน", res, "+{:.1f}%".format(d_r), _ch(res), "up"))
            if sup:
                rows.append(_qr_level("⬇", "พื้น", sup, "−{:.1f}%".format(d_s), _ch(sup), "dn"))
            fr = None
            if res and sup and res > sup:
                fr = (px - sup) / (res - sup)
            cards.append(card("เพดานใกล้สุด / พื้นใกล้สุด", v, c, "".join(rows),
                              frac=fr, mark=fr,
                              tip="เพดาน = แนวต้าน (จุดที่ราคาเคยขึ้นไปแล้วโดนดันกลับ) · พื้น = แนวรับ (จุดที่ราคาเคยลงมาแล้วเด้งกลับ) · โอกาสไปถึงคำนวณจากความผันผวน 20 วันล่าสุด (แบบจำลองสุ่ม ไม่คิดข่าวหรือแนวโน้ม) ใช้เป็นแนวทางคร่าวๆ · ขีดขาวคือราคาตอนนี้ ซ้าย = พื้น ขวา = เพดาน",
                              tag="ข้างหน้า 1 สัปดาห์", future=True))
    else:
        cards.append(card("เพดานใกล้สุด / พื้นใกล้สุด", "ยังไม่มีข้อมูล", GY, "ข้อมูลราคาย้อนหลังไม่พอ", tag="ข้างหน้า 1 สัปดาห์", future=True))

    # 5) คาดการณ์ 1 สัปดาห์
    if S and px:
        score = 0.0
        if S["last"] > S["ema9"] > S["ema21"]:
            score += 1.0
        elif S["last"] < S["ema9"] < S["ema21"]:
            score -= 1.0
        if S["rsi"] > 75:
            score -= 0.5
        elif S["rsi"] < 25:
            score += 0.5
        score += max(-1.0, min(1.0, S["ret5"] / 0.10)) * 0.5
        if score >= 0.75:
            v, c = "มีแนวโน้มขึ้นมากกว่าลง", GR
        elif score <= -0.75:
            v, c = "มีแนวโน้มลงมากกว่าขึ้น", RD
        else:
            v, c = "ยังเดาทิศไม่ได้", YE
        sdw = S["sd20"] * _sqrt(5)
        sub = (_qr_range(px * _exp(-sdw), px * _exp(sdw), px)
               + '<div class="qr-cap">สัปดาห์หน้าราคาน่าจะอยู่ในช่วงนี้ · ถูกราว 2 ใน 3 ครั้ง อีก 1 ใน 3 อาจหลุดช่วงนี้</div>')
        try:
            import time as _t
            _now = _t.time()
            for _k in ("earningsTimestamp", "earningsTimestampStart", "earningsTimestampEnd"):
                _e = num(_k)
                if _e and _now - 86400 <= _e <= _now + 8 * 86400:
                    sub += '<div class="qr-warn">⚠️ มีประกาศงบสัปดาห์นี้ ราคาอาจกระโดดเกินช่วงนี้</div>'
                    break
        except Exception:
            pass
        cards.append(card("คาดการณ์ราคา", v, c, sub,
                          tip="ช่วงราคาคำนวณจากความแกว่งของราคา 20 วันล่าสุด · ทิศทางดูจากแนวโน้มราคา + แรงซื้อ-ขาย + ผล 5 วันล่าสุด เดาทิศ 1 สัปดาห์ได้แม่นไม่มาก ให้ดูช่วงราคาเป็นหลัก · ไม่ใช่คำแนะนำซื้อขาย",
                          tag="ข้างหน้า 1 สัปดาห์", future=True))
    else:
        cards.append(card("คาดการณ์ราคา", "ยังไม่มีข้อมูล", GY, "ข้อมูลราคาย้อนหลังไม่พอ", tag="ข้างหน้า 1 สัปดาห์", future=True))

    # 3) นักวิเคราะห์ช่วงนี้ (ย้อนหลัง 30 วัน) + เป้าราคาเฉลี่ย
    import html as _h
    A = ana if isinstance(ana, dict) and ana.get("available") else None
    tgt, n_an = num("targetMeanPrice"), num("numberOfAnalystOpinions")
    cons = ""
    if tgt and px:
        cons = "<b>${:,.0f}</b> · {}{:.0f}%{}".format(
            tgt, "สูงกว่า " if tgt >= px else "ต่ำกว่า ", abs(tgt / px - 1) * 100, " · {:.0f} คน".format(n_an) if n_an else "")
    if A and A["n"] > 0:
        sc = (A["up"] - A["down"]) + (A["raises"] - A["lowers"])
        if sc >= 2:
            v, c = "นักวิเคราะห์ช่วงนี้มองดีขึ้น", GR
        elif sc <= -2:
            v, c = "นักวิเคราะห์ช่วงนี้มองแย่ลง", RD
        else:
            v, c = "ความเห็นแทบไม่เปลี่ยน", YE
        rows = [("ปรับคำแนะนำ", _qr_ud(A["up"], A["down"]))]
        if A["raises"] or A["lowers"]:
            rows.append(("ปรับเป้าราคา", _qr_ud(A["raises"], A["lowers"])))
        L0 = A.get("latest")
        if L0 and L0.get("firm"):
            _mn = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
            _ac = {"up": "ปรับขึ้น", "down": "ปรับลง", "init": "เริ่มวิเคราะห์", "main": "คงเดิม", "reit": "ยืนยันเดิม"}.get(L0.get("action"), "")
            rows.append(("ล่าสุด", "{} → <b>{}</b>{} ({} {})".format(_h.escape(L0["firm"]), _h.escape(L0.get("to", "")),
                                                                " · " + _ac if _ac else "", L0["day"], _mn[L0["month"] - 1])))
        if cons:
            rows.append(("เป้าเฉลี่ย", cons))
        fr = max(0.0, min(1.0, (max(-6, min(6, sc)) + 6) / 12))
        cards.append(card("นักวิเคราะห์ช่วงนี้", v, c, _qr_kv(rows) + '<div class="qr-cap">นับ 30 วันที่ผ่านมา · เป้าราคาเฉลี่ยเป็นการมองไกลราว 12 เดือน</div>', frac=fr, mark=fr,
                          tip="นับจำนวนครั้งที่โบรกเกอร์ปรับคำแนะนำ (เช่น ถือ→ซื้อ) และปรับเป้าราคาใน 30 วันที่ผ่านมา · ขึ้นมากกว่าลง = มองดีขึ้น · นักวิเคราะห์มักปรับตามราคาที่ขึ้นลงไปแล้ว ใช้เป็นข้อมูลประกอบ ไม่ใช่สัญญาณซื้อขาย",
                          tag="ย้อนหลัง 30 วัน"))
    elif A:
        cards.append(card("นักวิเคราะห์ช่วงนี้", "เดือนนี้เงียบ ไม่มีใครปรับ", GY,
                          "30 วันที่ผ่านมาไม่มีโบรกเกอร์ปรับคำแนะนำหรือเป้าราคา" + (_qr_kv([("เป้าเฉลี่ย", cons)]) if cons else ""),
                          tip="ข้อมูลจาก Yahoo Finance · ไม่ใช่คำแนะนำซื้อขาย", tag="ย้อนหลัง 30 วัน"))
    else:
        rec = str(info.get("recommendationKey") or "").lower()
        rv = {"strong_buy": ("ส่วนใหญ่แนะนำซื้อแรง", GR), "buy": ("ส่วนใหญ่แนะนำซื้อ", GR), "hold": ("ส่วนใหญ่แนะนำถือ", YE),
              "underperform": ("คาดว่าจะแย่กว่าตลาด", OR), "sell": ("ส่วนใหญ่แนะนำขาย", RD)}.get(rec)
        if rv or cons:
            cards.append(card("นักวิเคราะห์โดยรวม", rv[0] if rv else "มีเป้าราคา", rv[1] if rv else CY,
                              "Yahoo ยังไม่มีรายการปรับคำแนะนำล่าสุด" + (_qr_kv([("เป้าเฉลี่ย", cons)]) if cons else ""),
                              tip="ข้อมูลจาก Yahoo Finance · ไม่ใช่คำแนะนำซื้อขาย", tag="ภาพรวมปัจจุบัน"))
        else:
            cards.append(card("นักวิเคราะห์ช่วงนี้", "ยังไม่มีข้อมูล", GY, "Yahoo ไม่มีข้อมูลนักวิเคราะห์ของหุ้นตัวนี้ (หุ้นเล็ก/หุ้นนอกสหรัฐมักไม่มี)", tag="ย้อนหลัง 30 วัน"))

    _qr_emit(cards)


if analysis is None:
    st.info("พิมพ์รหัสหุ้นในช่องด้านบน แล้วกด ▶ วิเคราะห์หุ้น (หรือกด Enter) ได้เลยครับ")
elif "error" in analysis:
    st.error(analysis["error"])
else:
    info = analysis["info"]
    ticker = analysis["ticker"]

    # ---------- แถบข้อมูลราคาบนสุด ----------
    price = info.get("currentPrice", info.get("regularMarketPrice", "N/A"))
    pe = info.get("trailingPE", "N/A")
    f_pe = info.get("forwardPE", "N/A")
    target = info.get("targetMeanPrice", "N/A")

    # ---------- แผงราคาสด (อัปเดตเองเฉพาะส่วนนี้ ไม่ต้อง refresh หน้า) ----------
    zones_for_live = cached_price_zones(ticker, 0.20)
    live_fragment = st.fragment(render_live_panel, run_every=refresh_interval)
    live_fragment(ticker, zones_for_live)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("ราคา ณ ตอนวิเคราะห์", f"${price:,.2f}" if isinstance(price, (int, float)) else "N/A")
    col2.metric("Trailing P/E", f"{pe:.2f}" if isinstance(pe, (int, float)) else str(pe))
    col3.metric("Forward P/E", f"{f_pe:.2f}" if isinstance(f_pe, (int, float)) else str(f_pe))
    col4.metric("ราคาเป้าหมาย", f"${target:,.2f}" if isinstance(target, (int, float)) else "N/A")
    col5.metric("คะแนนรวม", f"{analysis['overall_score']}/100", analysis["overall_label"])

    st.markdown(
        "<style>"
        ".st-key-qr_view [data-testid=\"stRadioGroup\"]{display:flex !important;flex-wrap:nowrap !important;gap:10px !important;width:100%;max-width:580px}"
        ".st-key-qr_view label[data-testid=\"stRadioOption\"]{flex:1 1 0;justify-content:center;padding:11px 16px !important;"
        "background:rgba(12,14,28,.85) !important;border:1px solid rgba(0,240,255,.32) !important;"
        "clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px)) !important;transition:background .2s,border-color .2s}"
        ".st-key-qr_view label[data-testid=\"stRadioOption\"] p{color:#aab3d0 !important;font-weight:600 !important;font-size:14.5px !important;"
        "text-align:center;white-space:normal !important}"
        ".st-key-qr_view label[data-testid=\"stRadioOption\"]:hover{border-color:#00f0ff !important;background:rgba(0,240,255,.09) !important}"
        ".st-key-qr_view label[data-testid=\"stRadioOption\"]:hover p{color:#fff !important}"
        ".st-key-qr_view label[data-testid=\"stRadioOption\"][data-selected=\"true\"]{"
        "background:linear-gradient(135deg,#5ef4ff,#00b7e6) !important;border-color:#5ef4ff !important}"
        ".st-key-qr_view label[data-testid=\"stRadioOption\"][data-selected=\"true\"] p{color:#031219 !important;font-weight:700 !important}"
        "</style>"
        '<div class="section-label">◆ อ่านเร็ว — เลือกกรอบเวลาที่สนใจ</div>',
        unsafe_allow_html=True)
    _qr_mode = st.radio("มุมมองอ่านเร็ว", ["⚡ ระยะสั้น · 1 สัปดาห์", "📅 ระยะยาว · 1 เดือน–1 ปี"],
                        horizontal=True, key="qr_view", label_visibility="collapsed")
    if _qr_mode.startswith("⚡"):
        with st.spinner("กำลังคำนวณมุมมองระยะสั้น..."):
            _st, _ana = cached_short_term(ticker), cached_analyst_recent(ticker)
        render_quick_read_short(info, price, _st, _ana)
    else:
        with st.spinner("กำลังคำนวณคาดการณ์ 1 เดือน..."):
            _om, _vol = cached_one_month_horizon(ticker), cached_vol_range(ticker)
        render_quick_read(info, price, _om, _vol)

    # ---------- อารมณ์ฝูงชน + พื้นฐาน ----------
    try:
        import sentiment_ui
        sentiment_ui.render_stock_mood(ticker, info)
    except Exception as e:
        st.caption("อารมณ์ฝูงชนแสดงไม่ได้: " + str(e))

    # ---------- สรุปสุดท้ายอยู่บนสุด (เติมข้อมูลตอนท้าย เพราะต้องรอผลจากทุกแท็บก่อน) ----------
    summary_slot = st.container()
    st.write("")
    tabs = st.tabs(["① โซนราคา", "② พื้นฐาน 10 มิติ", "③ Backtest", "④ สัญญาณตลาด", "⑤ เทียบตลาด · โมเมนตัม", "⑥ เช็กลิสต์", "⑦ AI · ลิงก์"])

    with tabs[0]:
        # ---------- โซนราคาอ้างอิง (ไม่ใช่คำแนะนำซื้อ) ----------
        st.markdown(f'<div class="section-label">◆ ขั้นที่ 1 — ราคาตอนนี้อยู่ตรงไหน (โซนราคาอ้างอิง) — {ticker}</div>', unsafe_allow_html=True)

        mos_pct = st.slider(
            "ส่วนเผื่อความปลอดภัยจากราคาเป้าหมายนักวิเคราะห์ (%)",
            min_value=5, max_value=40, value=20, step=5,
            help="ยิ่งเผื่อมาก โซนราคายิ่งต่ำลง = รอราคาต่ำกว่านี้ถึงจะเข้าโซน",
        )
        zones_res = cached_price_zones(ticker, mos_pct / 100)

        if zones_res.get("available"):
            cur = zones_res["current"]
            st.write(f"ราคาปัจจุบัน: **&#36;{cur:,.2f}**")

            for z in zones_res["zones"]:
                below = z["price"] < cur
                marker = "⬇️ ต่ำกว่าราคาตอนนี้" if below else "⬆️ สูงกว่าราคาตอนนี้"
                st.markdown(
                    f"**&#36;{z['price']:,.2f}** ({z['gap_pct']:+.1f}%) — {z['name']}  \n"
                    f"<span style='color:#7d86a6; font-size:13px;'>{marker} · {z['note']}</span>",
                    unsafe_allow_html=True,
                )
                st.write("")

            for n in zones_res["notes"]:
                st.write(f"• {n}")
        else:
            st.caption(f"คำนวณโซนราคาไม่ได้ ({zones_res.get('reason', 'ไม่ทราบสาเหตุ')})")

        st.caption(
            "⚠️ นี่คือ 'โซนอ้างอิง' ที่คำนวณจากข้อเท็จจริง (ค่าเฉลี่ย, ขอบ Bollinger, ต่ำสุดในอดีต, เป้าหมายนักวิเคราะห์, Put OI) "
            "ไม่ใช่ราคาที่ 'ควรซื้อ' — ไม่มีใครรู้ราคาที่ถูกต้อง และราคาหลุดโซนเหล่านี้ลงไปได้เสมอ "
            "ข้อมูลนี้ไม่ใช่คำแนะนำการลงทุน ควรพิจารณาร่วมกับความเสี่ยงและเงินทุนของตัวเอง"
        )


    with tabs[1]:
        # ---------- คะแนน 10 มิติ ----------
        st.markdown(f'<div class="section-label">◆ ขั้นที่ 2 — พื้นฐานธุรกิจดีไหม (10 มิติ) — {ticker}</div>', unsafe_allow_html=True)
        st.write("")

        for key, dim in analysis["dimensions"].items():
            title = scoring.DIMENSION_NAMES_TH[key]
            score = dim["score"]

            if score >= 70:
                tag = "🟢 แข็งแกร่ง"
            elif score >= 45:
                tag = "🟡 กลาง"
            else:
                tag = "🔴 ต้องระวัง"

            with st.expander(f"{title}  —  {score}/100  ·  {tag}"):
                colored_bar(score / 100)
                st.caption(dim["summary"])
                for note in dim["details"]:
                    st.write(f"• {note}")


    with tabs[2]:
        # ---------- Backtest: ทดสอบย้อนหลังความแม่นยำของสัญญาณ Technical ----------
        st.markdown('<div class="section-label">◆ ขั้นที่ 3 — เชื่อ Technical ได้ไหม (ทดสอบย้อนหลัง Backtest)</div>', unsafe_allow_html=True)

        with st.spinner("กำลังทดสอบย้อนหลัง 2 ปี... (อาจใช้เวลาสักครู่)"):
            bt_result = cached_backtest(ticker)

        backtest_note_for_ai = None
        if bt_result.get("available"):
            acc = bt_result["overall_accuracy"]
            if acc is not None:
                bt_color = "#19f5a5" if acc > 55 else ("#ff2a6d" if acc < 48 else "#fcee0a")
                st.markdown(
                    f"""
                    <div style="background:#0c0e1c; border:1px solid rgba(0,240,255,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                        <div style="font-size:13px; color:#7d86a6; letter-spacing:0.5px;">ความแม่นยำของสัญญาณ MACD ย้อนหลัง 2 ปี (ถือ {bt_result['holding_days']} วันทำการ)</div>
                        <div style="font-size:28px; font-weight:700; color:{bt_color}; font-family:'IBM Plex Mono', monospace;">
                            {acc:.1f}%
                        </div>
                        <div style="font-size:13px; color:#7d86a6; margin-top:2px;">เทียบกับเดาสุ่ม 50% · ทดสอบทั้งหมด {bt_result['total_signals']} ครั้ง</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                backtest_note_for_ai = "; ".join(bt_result["notes"])
            for n in bt_result["notes"]:
                st.write(f"• {n}")
        else:
            st.caption(f"ไม่สามารถ backtest ได้: {bt_result.get('reason', 'ไม่ทราบสาเหตุ')}")

        st.caption(
            "⚠️ Backtest ได้เฉพาะสัญญาณ Technical เท่านั้น เพราะ Options Chain/Insider/Institutional/Analyst "
            "เป็นข้อมูลสแนปช็อตปัจจุบัน ไม่มีประวัติย้อนหลังให้ทดสอบซ้ำได้ และผลในอดีตไม่รับประกันผลในอนาคต"
        )


    with tabs[3]:
        # ---------- แนวโน้มระยะสั้น (รวมสัญญาณจากหลายแหล่ง) ----------
        st.markdown('<div class="section-label">◆ ขั้นที่ 4 — คนอื่นกำลังทำอะไร (Options, Insider, สถาบัน, นักวิเคราะห์, Technical)</div>', unsafe_allow_html=True)

        with st.spinner("กำลังประมวลผล Options Chain, Insider, สถาบัน, นักวิเคราะห์ และ Technical..."):
            outlook = cached_forward_outlook(ticker)

        lean = outlook["lean_pct"]
        verdict = outlook["verdict"]

        if lean > 25:
            verdict_color = "#19f5a5"
        elif lean < -25:
            verdict_color = "#ff2a6d"
        else:
            verdict_color = "#fcee0a"

        st.markdown(
            f"""
            <div style="background:#0c0e1c; border:1px solid rgba(0,240,255,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                <div style="font-size:13px; color:#7d86a6; letter-spacing:0.5px;">ผลรวมสัญญาณ (เอียงลบ = ลง, เอียงบวก = ขึ้น)</div>
                <div style="font-size:28px; font-weight:700; color:{verdict_color}; font-family:'IBM Plex Mono', monospace;">
                    {lean:+.1f}%
                </div>
                <div style="font-size:15px; color:#e6f1ff; margin-top:2px;">{verdict}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        colored_bar((lean + 100) / 200)

        for source_name, notes in outlook["sources"]:
            with st.expander(f"▸ {source_name}"):
                for n in notes:
                    st.write(f"• {n}")

        unavailable = [
            name for name, key in [
                ("ห่วงโซ่ออปชัน", "options"), ("การซื้อขายของผู้บริหาร", "insider"),
                ("ผู้ถือหุ้นสถาบัน", "institution"), ("คำแนะนำนักวิเคราะห์", "analyst"),
                ("การวิเคราะห์ทางเทคนิค", "technical"),
            ] if not outlook["raw"][key].get("available")
        ]
        if unavailable:
            st.caption(f"ไม่มีข้อมูลเพียงพอสำหรับ: {', '.join(unavailable)} (หุ้นบางตัวอาจไม่มีข้อมูลบางประเภท)")

        st.caption(
            "⚠️ นี่คือการประเมินเชิงสถิติจากข้อมูลสาธารณะฟรี ไม่ใช่ข้อมูล real-time options flow "
            "แบบบริการเสียเงิน (Unusual Whales / Quiver / AltIndex) และไม่ใช่การทำนายราคาที่แม่นยำ 100% "
            "ตลาดหุ้นมีความไม่แน่นอนโดยธรรมชาติเสมอ"
        )

        st.markdown("---")
        # ---------- เจาะลึกขั้นสุดยอด (deep.py) ----------
        st.markdown('<div class="section-label">◆ ขั้นที่ 5 — สัญญาณเสริม (Momentum, Relative Strength, IV Skew ฯลฯ)</div>', unsafe_allow_html=True)

        with st.spinner("กำลังประมวลผล Momentum, Relative Strength, IV Skew, Earnings, News..."):
            deep_result = cached_deep_outlook(ticker)

        deep_lean = deep_result["lean_pct"]
        deep_verdict = deep_result["verdict"]

        if deep_lean > 25:
            deep_color = "#19f5a5"
        elif deep_lean < -25:
            deep_color = "#ff2a6d"
        else:
            deep_color = "#fcee0a"

        combined_lean = round((lean + deep_lean) / 2, 1)
        if combined_lean > 25:
            combined_verdict, combined_color = "โน้มเอียงขึ้น (Bullish Tilt)", "#19f5a5"
        elif combined_lean < -25:
            combined_verdict, combined_color = "โน้มเอียงลง (Bearish Tilt)", "#ff2a6d"
        else:
            combined_verdict, combined_color = "กลางๆ ไม่มีสัญญาณชัดเจน (Neutral)", "#fcee0a"

        st.markdown(
            f"""
            <div style="background:#0c0e1c; border:1px solid rgba(0,240,255,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                <div style="font-size:13px; color:#7d86a6; letter-spacing:0.5px;">ผลรวมสัญญาณชุดเจาะลึก (11 แหล่งข้อมูลรวมกัน)</div>
                <div style="font-size:28px; font-weight:700; color:{deep_color}; font-family:'IBM Plex Mono', monospace;">
                    {deep_lean:+.1f}%
                </div>
                <div style="font-size:15px; color:#e6f1ff; margin-top:2px;">{deep_verdict}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        colored_bar((deep_lean + 100) / 200)

        for source_name, notes in deep_result["sources"]:
            with st.expander(f"▸ {source_name}"):
                for n in notes:
                    st.write(f"• {n}")

        st.markdown("---")
        # ---------- แนวโน้มระยะยาว ไม่เกิน 1 เดือน ----------
        st.markdown('<div class="section-label">◆ ขั้นที่ 5 (ต่อ) — มีข่าวใหญ่ใกล้ๆ ไหม (แนวโน้ม 1 เดือน)</div>', unsafe_allow_html=True)

        with st.spinner("กำลังประมวลผลแนวโน้ม 1 เดือน..."):
            one_month = cached_one_month_horizon(ticker)

        if one_month.get("available"):
            om_lean = one_month["lean_pct"]
            om_verdict = one_month["verdict"]
            om_color = "#19f5a5" if om_lean > 25 else ("#ff2a6d" if om_lean < -25 else "#fcee0a")

            st.markdown(
                f"""
                <div style="background:#0c0e1c; border:1px solid rgba(0,240,255,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                    <div style="font-size:13px; color:#7d86a6; letter-spacing:0.5px;">แนวโน้มในกรอบเวลา ~1 เดือนข้างหน้า</div>
                    <div style="font-size:28px; font-weight:700; color:{om_color}; font-family:'IBM Plex Mono', monospace;">
                        {om_lean:+.1f}%
                    </div>
                    <div style="font-size:15px; color:#e6f1ff; margin-top:2px;">{om_verdict}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            for n in one_month["notes"]:
                st.write(f"• {n}")
        else:
            om_lean = 0
            st.caption(f"ไม่มีข้อมูลเพียงพอสำหรับแนวโน้ม 1 เดือน ({one_month.get('reason', 'ไม่ทราบสาเหตุ')})")

        st.caption(
            "⚠️ กรอบเวลา 1 เดือนยังคงเป็นการประเมินเชิงสถิติ ไม่ใช่การรับประกัน — "
            "เหตุการณ์ไม่คาดฝัน (ข่าวด่วน, สภาวะตลาดโลก) เปลี่ยนภาพนี้ได้เสมอ"
        )

        st.markdown("---")
        # ---------- เศรษฐกิจมหภาค (VIX + อัตราผลตอบแทนพันธบัตร) ----------
        st.markdown('<div class="section-label">◆ ขั้นที่ 5 (ต่อ) — บริบทตลาดรวม (VIX, พันธบัตร)</div>', unsafe_allow_html=True)

        with st.spinner("กำลังดึงข้อมูล VIX และอัตราผลตอบแทนพันธบัตร..."):
            macro_data = cached_macro_snapshot()

        macro_lean = macro_data["lean_pct"]
        macro_color = "#19f5a5" if macro_lean > 25 else ("#ff2a6d" if macro_lean < -25 else "#fcee0a")
        st.markdown(
            f"""
            <div style="background:#0c0e1c; border:1px solid rgba(0,240,255,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                <div style="font-size:13px; color:#7d86a6; letter-spacing:0.5px;">บรรยากาศตลาดโดยรวมตอนนี้</div>
                <div style="font-size:28px; font-weight:700; color:{macro_color}; font-family:'IBM Plex Mono', monospace;">
                    {macro_lean:+.1f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for source_name, notes in macro_data["sources"]:
            with st.expander(f"▸ {source_name}"):
                for n in notes:
                    st.write(f"• {n}")
        st.caption("⚠️ ข้อมูลนี้เป็นบรรยากาศตลาดรวม ใช้เป็นบริบทประกอบ ไม่ใช่สัญญาณเฉพาะหุ้นนี้โดยตรง")

        st.markdown("---")
        # ---------- สรุปรวมทั้งหมด (แนวโน้มระยะสั้น + เจาะลึก + 1 เดือน) ----------
        st.markdown('<div class="section-label">รวมขั้นที่ 4 + 5 เข้าด้วยกัน — สัญญาณตลาด/เทคนิคทั้งหมด</div>', unsafe_allow_html=True)
        if one_month.get("available"):
            combined_lean = round((lean + deep_lean + om_lean) / 3, 1)
            combined_source_count = "11 + 1 เดือน"
        else:
            combined_lean = round((lean + deep_lean) / 2, 1)
            combined_source_count = "11"

        if combined_lean > 25:
            combined_verdict, combined_color = "โน้มเอียงขึ้น (Bullish Tilt)", "#19f5a5"
        elif combined_lean < -25:
            combined_verdict, combined_color = "โน้มเอียงลง (Bearish Tilt)", "#ff2a6d"
        else:
            combined_verdict, combined_color = "กลางๆ ไม่มีสัญญาณชัดเจน (Neutral)", "#fcee0a"

        st.markdown(
            f"""
            <div style="background:linear-gradient(145deg, #12162a, #080a16); border:1px solid rgba(0,240,255,0.4); border-radius:12px; padding:20px 24px; margin-bottom:12px;">
                <div style="font-size:13px; color:#b9c4e4; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">สรุปรวมสัญญาณตลาด+เทคนิค ({combined_source_count} แหล่งข้อมูล)</div>
                <div style="font-size:36px; font-weight:700; color:{combined_color}; font-family:'IBM Plex Mono', monospace;">
                    {combined_lean:+.1f}%
                </div>
                <div style="font-size:16px; color:#e6f1ff; margin-top:4px;">{combined_verdict}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(
            "⚠️ ตัวเลขนี้คือค่าเฉลี่ยของสัญญาณสถิติด้านตลาด/เทคนิคทั้งหมด ยังไม่รวมพื้นฐานธุรกิจ (10 มิติด้านล่าง) "
            "ไม่ใช่การรับประกันทิศทางราคา และไม่ควรใช้เป็นเหตุผลเดียวในการตัดสินใจซื้อ-ขาย"
        )


    with tabs[4]:
        # ---------- หุ้นเขียว ตลาดแดง (สด อัปเดตอัตโนมัติ) ----------
        st.markdown(f'<div class="section-label">◆ หุ้นเขียว ตลาดแดง — เทียบกับตลาด (SPY) ตอนนี้ — {ticker}</div>', unsafe_allow_html=True)
        momentum_ui.render_green_red_guide()
        _zone_params = momentum_ui.render_zone_settings()
        st.fragment(render_live_relative, run_every=refresh_interval)(ticker, _zone_params)

        st.markdown("---")
        # ---------- โมเมนตัมตามงานวิจัย ----------
        st.markdown(f'<div class="section-label">◆ โมเมนตัมตามงานวิจัย — เข้าใจใน 5 วินาที — {ticker}</div>', unsafe_allow_html=True)
        momentum_ui.render_scorecard(ticker)

        st.markdown("---")
        # ---------- ปัจจัยที่ทำให้หุ้นขึ้นหรือลง ----------
        st.markdown(f'<div class="section-label">◆ ปัจจัยที่ทำให้หุ้นขึ้นหรือลง — 10 ข้อ — {ticker}</div>', unsafe_allow_html=True)
        drivers_ui.render_drivers(ticker)


    with tabs[5]:
        # ---------- เช็กลิสต์หลายเงื่อนไขก่อนซื้อ ----------
        st.markdown(f'<div class="section-label">◆ เช็กลิสต์ก่อนซื้อ — ผ่านกี่ข้อ — {ticker}</div>', unsafe_allow_html=True)
        with st.spinner("กำลังตรวจเงื่อนไขทั้งหมด..."):
            cl = cached_checklist(ticker)

        if not cl.get("available"):
            st.caption(f"ตรวจเช็กลิสต์ไม่ได้: {cl.get('reason', 'ไม่ทราบสาเหตุ')}")
        else:
            all_ok = cl["passed"] == cl["total"]
            c_a, c_b = st.columns([1, 2])
            c_a.metric("ผ่านเงื่อนไข", f"{cl['passed']} / {cl['total']} ข้อ")
            with c_b:
                colored_bar(cl["passed"] / cl["total"])
            if all_ok:
                st.success("ผ่านครบทุกข้อ — แต่ยังไม่ใช่การรับประกันว่าจะขึ้น ดูผลทดสอบย้อนหลังด้านล่างประกอบ")
            else:
                failed = [n for n, ok, _ in cl["price_checks"] + cl["extra_checks"] if not ok]
                st.info(f"ยังไม่ผ่าน {len(failed)} ข้อ: " + " · ".join(failed[:3]) + (" ..." if len(failed) > 3 else ""))

            st.markdown("**เงื่อนไขราคา/ตลาด** (ตามราคาปิดล่าสุด)")
            for name, ok, detail in cl["price_checks"]:
                st.write(f"{'✅' if ok else '❌'} {name}" + (f"  ·  <span style='color:#7d86a6'>{detail}</span>" if detail else ""), unsafe_allow_html=True)

            if cl["extra_checks"]:
                st.markdown("**เงื่อนไขพื้นฐานปัจจุบัน**")
                for name, ok, detail in cl["extra_checks"]:
                    st.write(f"{'✅' if ok else '❌'} {name}" + (f"  ·  <span style='color:#7d86a6'>{detail}</span>" if detail else ""), unsafe_allow_html=True)


    with tabs[6]:
        # ---------- ลิงก์ไปเว็บ alt-data ----------
        st.markdown('<div class="section-label">เจาะลึกเพิ่มเติม</div>', unsafe_allow_html=True)
        website = info.get("website", "")
        domain = urlparse(website).netloc.replace("www.", "") if website else f"{ticker.lower()}.com"

        urls = {
            "Google Trends": f"https://trends.google.com/trends/explore?q={ticker}",
            "Similarweb": f"https://www.similarweb.com/website/{domain}/",
            "Unusual Whales": f"https://unusualwhales.com/stock/{ticker}/overview",
            "Quiver Quant": f"https://www.quiverquant.com/stock/{ticker}/",
            "AltIndex": f"https://altindex.com/ticker/{ticker.lower()}/ai-stock-analysis",
            "TradingView": f"https://www.tradingview.com/symbols/{ticker}/",
        }
        link_cols = st.columns(len(urls))
        for i, (name, url) in enumerate(urls.items()):
            link_cols[i].link_button(name, url, use_container_width=True)

        st.write("")

        # ---------- ข่าว M&A ทั่วตลาด (ไม่ผูกกับหุ้นที่ค้นหา แยกออกมาต่างหาก) ----------
        st.markdown('<div class="section-label">ข่าวการควบรวมกิจการทั่วตลาด (ไม่จำกัดเฉพาะหุ้นนี้)</div>', unsafe_allow_html=True)
        st.link_button("Bloomberg Deals — ข่าว M&A ล่าสุดทั้งตลาด", "https://www.bloomberg.com/deals", use_container_width=True)

        st.markdown("---")

        # ---------- ปุ่มสรุปผลด้วย AI (เสริม ไม่บังคับ) ----------
        st.markdown('<div class="section-label">สรุปผลด้วย AI (ไม่บังคับ)</div>', unsafe_allow_html=True)

        if st.button("✦  สรุปผลด้วย AI"):
            if not ai_key:
                st.warning(
                    "ยังไม่ได้ใส่คีย์เสริมที่แถบด้านซ้ายครับ "
                    "หรือข้ามส่วนนี้ไปได้เลย เพราะคะแนน 10 มิติด้านบนใช้งานได้ครบแล้ว"
                )
            else:
                with st.spinner("กำลังดึงข่าวล่าสุด + ประมวลผลสรุป..."):
                    news_items = news_radar.fetch_google_news(f"{ticker} stock", max_items=6)
                    news_headlines = [n["title"] for n in news_items if n.get("title")]

                    macro_note = "; ".join(
                        n for _, notes in macro_data["sources"] for n in notes
                    ) if macro_data["sources"] else None

                    extra_context = {
                        "news_headlines": news_headlines,
                        "backtest_note": backtest_note_for_ai,
                        "macro_note": macro_note,
                    }
                    summary = get_ai_summary(ai_key, ticker, analysis, extra_context)
                st.session_state.ai_summary = summary

        if st.session_state.ai_summary:
            st.markdown(st.session_state.ai_summary)


    with summary_slot:
        # ---------- สรุปผลรวมทั้งหมด (fundamentals + สัญญาณตลาด/เทคนิคทั้งหมด) ----------
        st.markdown(f'<div class="section-label">◆ สรุปสุดท้าย — รวมทุกขั้นเป็นตัวเลขเดียว — {ticker}</div>', unsafe_allow_html=True)

        fundamental_lean = (analysis["overall_score"] - 50) * 2  # แปลง 0-100 -> -100..100
        master_lean = round((fundamental_lean + combined_lean + macro_lean) / 3, 1)

        if master_lean > 25:
            master_verdict, master_color = "ภาพรวมเอียงบวก (Bullish)", "#19f5a5"
        elif master_lean < -25:
            master_verdict, master_color = "ภาพรวมเอียงลบ (Bearish)", "#ff2a6d"
        else:
            master_verdict, master_color = "ภาพรวมกลางๆ ยังไม่มีสัญญาณชัดเจน (Neutral)", "#fcee0a"

        # หาจุดแข็งสุด/จุดอ่อนสุดจาก 10 มิติ
        dim_items = [(scoring.DIMENSION_NAMES_TH[k], v["score"]) for k, v in analysis["dimensions"].items()]
        strongest = max(dim_items, key=lambda x: x[1])
        weakest = min(dim_items, key=lambda x: x[1])
        n_green = sum(1 for _, s in dim_items if s >= 70)
        n_red = sum(1 for _, s in dim_items if s < 45)

        st.markdown(
            f"""
            <div style="background:linear-gradient(145deg, #12162a, #080a16); border:1px solid rgba(0,240,255,0.5); border-radius:14px; padding:24px 28px; margin-bottom:14px;">
                <div style="font-size:13px; color:#b9c4e4; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:8px;">คะแนนสรุปสุดท้าย — รวมพื้นฐานธุรกิจ + สัญญาณตลาดทั้งหมด</div>
                <div style="font-size:42px; font-weight:700; color:{master_color}; font-family:'IBM Plex Mono', monospace;">
                    {master_lean:+.1f}%
                </div>
                <div style="font-size:17px; color:#e6f1ff; margin-top:4px;">{master_verdict}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        _k1, _k2, _k3 = st.columns(3)
        _k1.metric("พื้นฐานธุรกิจ", f"{analysis['overall_score']}/100", analysis["overall_label"], delta_color="off")
        for _col, _ttl, _it, _clr in ((_k2, "จุดแข็งที่สุด", strongest, "#19f5a5"), (_k3, "ควรระวังที่สุด", weakest, "#ff2a6d")):
            _col.markdown(
                f"""<div style="background:rgba(12,14,28,.85); border:1px solid rgba(0,240,255,.2); border-left:3px solid {_clr}; padding:10px 14px; min-height:92px;">
                <div style="font-size:12px; color:#7d86a6;">{_ttl}</div>
                <div style="font-size:14px; color:#e6f1ff; font-weight:600; margin:4px 0; line-height:1.4;">{_it[0]}</div>
                <div style="font-size:18px; color:{_clr}; font-weight:700; font-family:'IBM Plex Mono', monospace;">{_it[1]}/100</div></div>""",
                unsafe_allow_html=True,
            )

        summary_lines = [
            f"พื้นฐานธุรกิจ (10 มิติ) อยู่ที่ {analysis['overall_score']}/100 — {analysis['overall_label']} "
            f"(มี {n_green} มิติที่แข็งแกร่ง และ {n_red} มิติที่ต้องระวัง)",
            f"จุดแข็งที่สุด: **{strongest[0]}** ({strongest[1]}/100)",
            f"จุดที่ควรระวังที่สุด: **{weakest[0]}** ({weakest[1]}/100)",
            f"สัญญาณตลาด+เทคนิครวม (Options, Insider, Institution, Analyst, Technical, Momentum, "
            f"Relative Strength, IV Skew, Earnings, News): {combined_lean:+.1f}% — {combined_verdict}",
        ]
        rel_strength_raw = deep_result.get("raw", {}).get("relative_strength", {})
        if rel_strength_raw.get("available") and rel_strength_raw.get("notes"):
            summary_lines.append("📊 **เทียบกับตลาดรวม (S&P500):** " + rel_strength_raw["notes"][0])

        if one_month.get("available"):
            summary_lines.append(f"แนวโน้มในกรอบ 1 เดือนข้างหน้า: {om_lean:+.1f}% — {one_month['verdict']}")
            if one_month.get("earnings_within_month"):
                summary_lines.append("⚠️ มีวันประกาศผลประกอบการอยู่ในกรอบเดือนนี้ — เป็นทั้งโอกาสและความเสี่ยงที่ควรจับตาเป็นพิเศษ")

        summary_lines.append(f"บรรยากาศตลาดรวมกว้างๆ (VIX + อัตราผลตอบแทนพันธบัตร — คนละอย่างกับเทียบ S&P500 ด้านบน): {macro_lean:+.1f}%")

        if bt_result.get("available") and bt_result.get("overall_accuracy") is not None:
            summary_lines.append(
                f"ทดสอบย้อนหลัง: สัญญาณ Technical แม่นยำ {bt_result['overall_accuracy']:.1f}% "
                f"ในอดีต (เทียบเดาสุ่ม 50%) — ใช้ประกอบการตัดสินใจว่าควรเชื่อสัญญาณ technical ของหุ้นตัวนี้มากแค่ไหน"
            )

        with st.expander("📋 อ่านสรุปเป็นข้อความ (จุดแข็ง · จุดอ่อน · รายละเอียดทุกด้าน)", expanded=False):
            for line in summary_lines:
                st.write(f"• {line}")

        st.caption(
            "⚠️ นี่คือการสรุปผลจากสูตรคณิตศาสตร์รวมทุกข้อมูลที่ระบบหาได้ฟรี ไม่ใช่คำแนะนำซื้อ-ขาย "
            "และไม่มีระบบใดทำนายราคาหุ้นได้แม่นยำ 100% ควรศึกษาข้อมูลเพิ่มเติมด้วยตัวเองเสมอก่อนตัดสินใจ"
        )


    st.markdown("---")
    st.caption(
        "ข้อมูลทั้งหมดนี้เป็นการวิเคราะห์เชิงปริมาณจากสูตรคณิตศาสตร์ ไม่ใช่คำแนะนำการลงทุน "
        "ควรใช้ประกอบการตัดสินใจร่วมกับการศึกษาข้อมูลด้วยตัวเองเสมอ"
    )