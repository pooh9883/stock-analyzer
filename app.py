# -*- coding: utf-8 -*-
"""
app.py — Quant Stock Analyzer (ฟรีตลอด)
=========================================
โครงสร้าง:
1. ระบบให้คะแนน 10 มิติ (scoring.py) = หลัก, ฟรี 100%, ไม่ต้องมี API key
2. ปุ่ม "สรุปผลด้วย AI" = เสริม, ใช้ Gemini free tier เบื้องหลัง (กดเมื่อต้องการเท่านั้น)
   ถ้า provider error/หมด quota แอปยังทำงานได้ปกติด้วยระบบคะแนน
   (คำว่า "Gemini" ใช้แค่ในคอมเมนต์โค้ดกับ README เท่านั้น ไม่โชว์ในหน้า UI)
"""

import streamlit as st
from urllib.parse import urlparse
import scoring    # ไฟล์ scoring.py ที่อยู่โฟลเดอร์เดียวกัน
import advanced   # ไฟล์ advanced.py — options chain, insider, institution, analyst, technical ขั้นสูง
import deep       # ไฟล์ deep.py — momentum, relative strength, IV skew, target dispersion, earnings, news
import backtest   # ไฟล์ backtest.py — ทดสอบย้อนหลังความแม่นยำของสัญญาณ technical
import macro      # ไฟล์ macro.py — VIX, อัตราผลตอบแทนพันธบัตร 10 ปี
import news_radar # ไฟล์ news_radar.py — ดึงหัวข้อข่าวจริงให้ AI อ่านตอนสรุป
import levels     # ไฟล์ levels.py — ราคาสดแบบอัปเดตอัตโนมัติ + โซนราคาอ้างอิง

st.set_page_config(
    page_title="Quant Stock Analyzer",
    page_icon="◆",
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
        background: radial-gradient(circle at top left, #12141c 0%, #0a0b10 60%);
        color: #e8e6e0 !important;
    }

    /* บังคับสีตัวหนังสือให้สว่างชัดเจนทุกจุด กันปัญหาอ่านยากบนมือถือ
       (สำคัญเพราะ browser บางตัวยังใช้สีข้อความเริ่มต้นที่มืดเกินไปบนพื้นมืด) */
    .stApp, .stApp p, .stApp li, .stApp span, .stApp label,
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span,
    div[data-testid="stExpanderDetails"], div[data-testid="stExpanderDetails"] p,
    div[data-testid="stCaptionContainer"] {
        color: #e8e6e0 !important;
    }
    .stCaption, div[data-testid="stCaptionContainer"] p {
        color: #a8a6b0 !important;
    }

    .app-header {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 6px 0 2px 0;
        border-bottom: 1px solid rgba(212, 175, 55, 0.25);
        margin-bottom: 6px;
    }
    .app-header .mark {
        font-size: 30px;
        color: #d4af37;
        line-height: 1;
    }
    .app-header .title-text h1 {
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: 0.5px;
        color: #f4f0e6;
    }
    .app-header .title-text p {
        margin: 2px 0 0 0;
        font-size: 13px;
        color: #8a8a98;
        letter-spacing: 0.3px;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #16181f, #0f1116);
        border: 1px solid rgba(212, 175, 55, 0.18);
        border-radius: 10px;
        padding: 14px 16px 10px 16px;
    }
    div[data-testid="stMetricLabel"] {
        color: #9a9aa8 !important;
        font-size: 12px !important;
        letter-spacing: 0.4px;
        text-transform: uppercase;
    }
    div[data-testid="stMetricValue"] {
        color: #f4f0e6 !important;
        font-family: 'IBM Plex Mono', monospace;
    }

    section[data-testid="stSidebar"] {
        background: #0d0e13;
        border-right: 1px solid rgba(212, 175, 55, 0.15);
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #d4af37 !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #d4af37, #b8912c);
        color: #14151b;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        letter-spacing: 0.3px;
        transition: 0.15s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #e6c34f, #c9a13a);
        transform: translateY(-1px);
    }

    .stLinkButton > a {
        border-radius: 8px !important;
        border: 1px solid rgba(212, 175, 55, 0.35) !important;
        color: #d4af37 !important;
        background: transparent !important;
        font-weight: 500 !important;
    }
    .stLinkButton > a:hover {
        background: rgba(212, 175, 55, 0.08) !important;
    }

    details[data-testid="stExpander"] {
        background: #14161d;
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 10px;
        margin-bottom: 8px;
    }

    hr {
        border-color: rgba(212, 175, 55, 0.15) !important;
    }

    .section-label {
        color: #d4af37;
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


# =================================================================
# ฟังก์ชันเรียก AI สรุปผล (เสริม, เรียกเฉพาะตอนกดปุ่ม)
# หมายเหตุ: ใช้ Gemini เบื้องหลัง แต่ผู้ใช้ไม่จำเป็นต้องรู้ชื่อ provider
# ใช้ SDK ใหม่ google-genai (ของเก่า google-generativeai เลิกซัพพอร์ตแล้ว)
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
def cached_forward_outlook(ticker: str):
    return advanced.forward_outlook(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_deep_outlook(ticker: str):
    return deep.deep_outlook(ticker)


@st.cache_data(ttl=600, show_spinner=False)
def cached_one_month_horizon(ticker: str):
    return deep.analyze_one_month_horizon(ticker)


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
    color = "#3ecf6e" if (chg_pct or 0) > 0 else ("#e5534b" if (chg_pct or 0) < 0 else "#d4af37")
    chg_txt = f"{chg:+,.2f} ({chg_pct:+.2f}%)" if chg_pct is not None else "—"

    zone_txt = ""
    if zones_result and zones_result.get("available") and zones_result.get("nearest_below"):
        nb = zones_result["nearest_below"]
        gap = (price_now - nb["price"]) / price_now * 100
        zone_txt = (
            f"<span style='color:#9a9aa8; font-size:13px; margin-left:18px;'>แนวรับอ้างอิงใกล้สุด:</span> "
            f"<span style='color:#d4af37; font-weight:600;'>\\${nb['price']:,.2f}</span> "
            f"<span style='color:#9a9aa8; font-size:13px;'>(ห่างลงไป {gap:.1f}% · {nb['name']})</span>"
        )

    st.markdown(
        f"""
        <div style="background:#14161d; border:1px solid rgba(212,175,55,0.3); border-radius:10px; padding:12px 18px; margin-bottom:10px;">
            <span style="color:#9a9aa8; font-size:13px;">ราคาล่าสุด {ticker}</span>
            <span style="font-size:26px; font-weight:700; color:#f4f0e6; font-family:'IBM Plex Mono', monospace; margin-left:8px;">\\${price_now:,.2f}</span>
            <span style="color:{color}; font-weight:600; margin-left:10px;">{chg_txt}</span>
            {zone_txt}
            <div style="color:#8a8a98; font-size:11px; margin-top:4px;">อัปเดตอัตโนมัติ · ข้อมูลฟรีจาก Yahoo อาจช้ากว่าราคาจริงเล็กน้อย</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =================================================================
# Sidebar
# =================================================================
with st.sidebar:
    st.markdown("### ⚙ ตั้งค่า")

    mode = st.radio(
        "โหมดการใช้งาน",
        ["🔍 วิเคราะห์หุ้นรายตัว", "📰 เรดาร์ข่าว (Watchlist)"],
        index=0,
    )

    st.markdown("---")

    ticker_input = st.text_input("รหัสหุ้น (Ticker)", value="NVDA").upper().strip()
    btn_analyze = st.button("▶  วิเคราะห์หุ้น", use_container_width=True)

    refresh_choice = st.selectbox(
        "อัปเดตราคาอัตโนมัติทุก",
        ["60 วินาที", "30 วินาที", "120 วินาที", "ปิดการอัปเดตอัตโนมัติ"],
        index=0,
        help="ถี่เกินไปอาจโดน Yahoo จำกัดการเรียก แนะนำ 60 วินาทีขึ้นไป",
    )
    _refresh_map = {"30 วินาที": "30s", "60 วินาที": "60s", "120 วินาที": "120s", "ปิดการอัปเดตอัตโนมัติ": None}
    refresh_interval = _refresh_map[refresh_choice]

    st.markdown("---")
    st.caption("ส่วนเสริม — ไม่บังคับ")
    ai_key = st.text_input(
        "คีย์เสริมสำหรับสรุปผลด้วย AI",
        type="password",
        help="ใช้เชื่อมต่อบริการสรุปข้อความอัตโนมัติ (ฟรี) — ไม่ใส่ก็ใช้แอปได้ครบทุกฟีเจอร์หลัก",
    )
    st.caption("ระบบคะแนนหลักด้านล่างทำงานได้ฟรีเสมอ ไม่ว่าจะใส่คีย์นี้หรือไม่")


# =================================================================
# โหมด: เรดาร์ข่าว (Watchlist) — แยกออกจากการวิเคราะห์หุ้นรายตัวโดยสิ้นเชิง
# ถ้าอยู่โหมดนี้ จะ render หน้านี้แล้วหยุด (st.stop) ไม่รันโค้ดวิเคราะห์หุ้นด้านล่างต่อ
# =================================================================
if mode.startswith("📰"):
    st.markdown(
        """
        <div class="app-header">
            <div class="mark">◆</div>
            <div class="title-text">
                <h1>เรดาร์ข่าว — NEWS RADAR</h1>
                <p>ติดตามข่าว + วัน earnings ของหุ้นที่คุณเฝ้าดู โดยไม่ต้องค้นหาทีละตัว</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    st.caption(
        "⚠️ ไม่สามารถสแกนข่าว/หุ้นทั้งตลาดโลกอัตโนมัติได้ฟรี — ใส่รายชื่อหุ้นที่อยากเฝ้าดูเอง (สูงสุด 15 ตัว) "
        "ระบบจะดึงข่าวจริงจาก Google News + Yahoo Finance ให้ทุกตัว"
    )

    watchlist_input = st.text_area(
        "รายชื่อหุ้นที่อยากเฝ้าดู (คั่นด้วยจุลภาค หรือขึ้นบรรทัดใหม่)",
        value="NVDA, AAPL, SNDK, TSLA",
        height=80,
    )
    if not ai_key:
        st.caption("💡 ใส่คีย์เสริม AI ที่ด้านบนก่อนสแกน จะได้คำอธิบายสั้นๆ ต่อท้ายทุกข่าว ไม่ใส่ก็สแกนได้ปกติ แค่ไม่มีคำอธิบาย")

    btn_scan = st.button("📡 สแกนเรดาร์ข่าว", use_container_width=False)

    if btn_scan:
        tickers = [t.strip() for t in watchlist_input.replace("\n", ",").split(",") if t.strip()][:15]
        if not tickers:
            st.error("กรุณาใส่ชื่อหุ้นอย่างน้อย 1 ตัวครับ")
        else:
            with st.spinner(f"กำลังสแกนข่าวและวัน earnings ของ {len(tickers)} หุ้น..."):
                radar = news_radar.build_news_radar(tickers)

            if ai_key:
                with st.spinner("กำลังให้ AI อธิบายข่าวแต่ละอันสั้นๆ..."):
                    for t, data in radar["per_ticker"].items():
                        headlines = [n["title"] for n in data["news"]]
                        if headlines:
                            explanations = explain_headlines_with_ai(ai_key, t, headlines)
                            for n, exp in zip(data["news"], explanations):
                                n["explanation"] = exp

            st.session_state.radar_result = radar

    radar = st.session_state.get("radar_result")

    if radar is None:
        st.info("ใส่รายชื่อหุ้นแล้วกด 📡 สแกนเรดาร์ข่าว ได้เลยครับ")
    else:
        # ---------- กลุ่มหุ้นที่อาจได้อานิสงส์ร่วมกัน (sector เดียวกันภายใน watchlist) ----------
        if radar["related_groups"]:
            st.markdown('<div class="section-label">กลุ่มหุ้นที่อยู่อุตสาหกรรมเดียวกัน (อาจขยับตามกันได้)</div>', unsafe_allow_html=True)
            for sector, tks in radar["related_groups"].items():
                st.write(f"**{sector}**: {', '.join(tks)}")
            st.caption("⚠️ การจับกลุ่มนี้ทำได้แค่ภายในรายชื่อที่คุณใส่ ไม่ใช่การสแกนทั้งตลาด")
            st.markdown("---")

        # ---------- เรียงตามวัน earnings ใกล้สุดก่อน ----------
        st.markdown('<div class="section-label">เรียงตามความเร่งด่วน — วัน Earnings ใกล้สุดก่อน</div>', unsafe_allow_html=True)

        for t in radar["sorted_by_earnings"]:
            data = radar["per_ticker"][t]
            tone = data["overall_tone"]
            tone_color = "#3ecf6e" if "บวก" in tone else ("#e5534b" if "ลบ" in tone else "#d4af37")

            earnings_str = "ไม่ทราบวันที่"
            if data["earnings_date"] is not None:
                try:
                    earnings_str = str(data["earnings_date"])
                except Exception:
                    pass

            with st.expander(f"**{t}** — {data['name']} · {data['sector']} · {tone}"):
                st.markdown(
                    f"""
                    <div style="background:#14161d; border:1px solid rgba(212,175,55,0.2); border-radius:8px; padding:10px 14px; margin-bottom:10px;">
                        <span style="color:#9a9aa8; font-size:13px;">วัน Earnings ถัดไป:</span>
                        <span style="color:{tone_color}; font-weight:600; margin-left:6px;">{earnings_str}</span>
                        <span style="color:#9a9aa8; font-size:13px; margin-left:16px;">โทนข่าวรวม:</span>
                        <span style="color:{tone_color}; font-weight:600; margin-left:6px;">{tone}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if not data["news"]:
                    st.caption("ไม่พบข่าวล่าสุดสำหรับหุ้นนี้")
                else:
                    for n in data["news"]:
                        sentiment_tag = "🟢" if n["sentiment_score"] > 0 else ("🔴" if n["sentiment_score"] < 0 else "⚪")
                        if n.get("link"):
                            st.markdown(f"{sentiment_tag} [{n['title']}]({n['link']})  \n<span style='color:#9a9aa8; font-size:12px;'>{n['source']}</span>", unsafe_allow_html=True)
                        else:
                            st.write(f"{sentiment_tag} {n['title']} — _{n['source']}_")
                        explanation = n.get("explanation", "")
                        if explanation:
                            st.markdown(f"<span style='color:#d4af37; font-size:13px;'>↳ {explanation}</span>", unsafe_allow_html=True)
                        st.write("")

        st.caption(
            "⚠️ ข่าวดึงจาก Google News RSS (ฟรี ไม่มี API key) — เป็นแค่หัวข้อ+ลิงก์ ไม่ใช่เนื้อข่าวเต็ม "
            "sentiment เป็นแบบ keyword-based คร่าวๆ ไม่ใช่ NLP model จริง"
        )

    st.stop()  # หยุดตรงนี้ ไม่รันโค้ดวิเคราะห์หุ้นรายตัวด้านล่างต่อ


# =================================================================
# โหมด: วิเคราะห์หุ้นรายตัว (โหมดหลัก — โค้ดเดิมทั้งหมดด้านล่างนี้ไม่เปลี่ยนแปลง)
# =================================================================

# =================================================================
# หัวเรื่องหลัก
# =================================================================
st.markdown(
    """
    <div class="app-header">
        <div class="mark">◆</div>
        <div class="title-text">
            <h1>QUANT STOCK ANALYZER</h1>
            <p>ระบบให้คะแนน 10 มิติจากข้อมูลจริง · ประมวลผลด้วยสูตรเชิงปริมาณ · ไม่ต้องมีคีย์ใดๆ</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "ai_summary" not in st.session_state:
    st.session_state.ai_summary = None

if btn_analyze:
    if not ticker_input:
        st.error("กรุณาพิมพ์ชื่อหุ้นก่อนครับ")
    else:
        with st.spinner(f"กำลังประมวลผล {ticker_input} ..."):
            result = cached_full_analysis(ticker_input)
        st.session_state.analysis = result
        st.session_state.ai_summary = None  # เคลียร์สรุปเก่าเมื่อดูหุ้นใหม่

analysis = st.session_state.analysis

if analysis is None:
    st.info("พิมพ์รหัสหุ้นที่แถบด้านซ้าย แล้วกด ▶ วิเคราะห์หุ้น ได้เลยครับ")
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

    st.markdown("---")
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
        st.write(f"ราคาปัจจุบัน: **\\${cur:,.2f}**")

        for z in zones_res["zones"]:
            below = z["price"] < cur
            marker = "⬇️ ต่ำกว่าราคาตอนนี้" if below else "⬆️ สูงกว่าราคาตอนนี้"
            st.markdown(
                f"**\\${z['price']:,.2f}** ({z['gap_pct']:+.1f}%) — {z['name']}  \n"
                f"<span style='color:#9a9aa8; font-size:13px;'>{marker} · {z['note']}</span>",
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

    st.markdown("---")
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
            st.progress(score / 100)
            st.caption(dim["summary"])
            for note in dim["details"]:
                st.write(f"• {note}")

    st.markdown("---")
    # ---------- Backtest: ทดสอบย้อนหลังความแม่นยำของสัญญาณ Technical ----------
    st.markdown('<div class="section-label">◆ ขั้นที่ 3 — เชื่อ Technical ได้ไหม (ทดสอบย้อนหลัง Backtest)</div>', unsafe_allow_html=True)

    with st.spinner("กำลังทดสอบย้อนหลัง 2 ปี... (อาจใช้เวลาสักครู่)"):
        bt_result = cached_backtest(ticker)

    backtest_note_for_ai = None
    if bt_result.get("available"):
        acc = bt_result["overall_accuracy"]
        if acc is not None:
            bt_color = "#3ecf6e" if acc > 55 else ("#e5534b" if acc < 48 else "#d4af37")
            st.markdown(
                f"""
                <div style="background:#14161d; border:1px solid rgba(212,175,55,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                    <div style="font-size:13px; color:#9a9aa8; letter-spacing:0.5px;">ความแม่นยำของสัญญาณ MACD ย้อนหลัง 2 ปี (ถือ {bt_result['holding_days']} วันทำการ)</div>
                    <div style="font-size:28px; font-weight:700; color:{bt_color}; font-family:'IBM Plex Mono', monospace;">
                        {acc:.1f}%
                    </div>
                    <div style="font-size:13px; color:#9a9aa8; margin-top:2px;">เทียบกับเดาสุ่ม 50% · ทดสอบทั้งหมด {bt_result['total_signals']} ครั้ง</div>
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

    st.markdown("---")
    # ---------- แนวโน้มระยะสั้น (รวมสัญญาณจากหลายแหล่ง) ----------
    st.markdown('<div class="section-label">◆ ขั้นที่ 4 — คนอื่นกำลังทำอะไร (Options, Insider, สถาบัน, นักวิเคราะห์, Technical)</div>', unsafe_allow_html=True)

    with st.spinner("กำลังประมวลผล Options Chain, Insider, สถาบัน, นักวิเคราะห์ และ Technical..."):
        outlook = cached_forward_outlook(ticker)

    lean = outlook["lean_pct"]
    verdict = outlook["verdict"]

    if lean > 25:
        verdict_color = "#3ecf6e"
    elif lean < -25:
        verdict_color = "#e5534b"
    else:
        verdict_color = "#d4af37"

    st.markdown(
        f"""
        <div style="background:#14161d; border:1px solid rgba(212,175,55,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
            <div style="font-size:13px; color:#9a9aa8; letter-spacing:0.5px;">ผลรวมสัญญาณ (เอียงลบ = ลง, เอียงบวก = ขึ้น)</div>
            <div style="font-size:28px; font-weight:700; color:{verdict_color}; font-family:'IBM Plex Mono', monospace;">
                {lean:+.1f}%
            </div>
            <div style="font-size:15px; color:#f4f0e6; margin-top:2px;">{verdict}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress((lean + 100) / 200)

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
        deep_color = "#3ecf6e"
    elif deep_lean < -25:
        deep_color = "#e5534b"
    else:
        deep_color = "#d4af37"

    combined_lean = round((lean + deep_lean) / 2, 1)
    if combined_lean > 25:
        combined_verdict, combined_color = "โน้มเอียงขึ้น (Bullish Tilt)", "#3ecf6e"
    elif combined_lean < -25:
        combined_verdict, combined_color = "โน้มเอียงลง (Bearish Tilt)", "#e5534b"
    else:
        combined_verdict, combined_color = "กลางๆ ไม่มีสัญญาณชัดเจน (Neutral)", "#d4af37"

    st.markdown(
        f"""
        <div style="background:#14161d; border:1px solid rgba(212,175,55,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
            <div style="font-size:13px; color:#9a9aa8; letter-spacing:0.5px;">ผลรวมสัญญาณชุดเจาะลึก (11 แหล่งข้อมูลรวมกัน)</div>
            <div style="font-size:28px; font-weight:700; color:{deep_color}; font-family:'IBM Plex Mono', monospace;">
                {deep_lean:+.1f}%
            </div>
            <div style="font-size:15px; color:#f4f0e6; margin-top:2px;">{deep_verdict}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress((deep_lean + 100) / 200)

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
        om_color = "#3ecf6e" if om_lean > 25 else ("#e5534b" if om_lean < -25 else "#d4af37")

        st.markdown(
            f"""
            <div style="background:#14161d; border:1px solid rgba(212,175,55,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
                <div style="font-size:13px; color:#9a9aa8; letter-spacing:0.5px;">แนวโน้มในกรอบเวลา ~1 เดือนข้างหน้า</div>
                <div style="font-size:28px; font-weight:700; color:{om_color}; font-family:'IBM Plex Mono', monospace;">
                    {om_lean:+.1f}%
                </div>
                <div style="font-size:15px; color:#f4f0e6; margin-top:2px;">{om_verdict}</div>
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
    macro_color = "#3ecf6e" if macro_lean > 25 else ("#e5534b" if macro_lean < -25 else "#d4af37")
    st.markdown(
        f"""
        <div style="background:#14161d; border:1px solid rgba(212,175,55,0.25); border-radius:10px; padding:16px 20px; margin-bottom:12px;">
            <div style="font-size:13px; color:#9a9aa8; letter-spacing:0.5px;">บรรยากาศตลาดโดยรวมตอนนี้</div>
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
        combined_verdict, combined_color = "โน้มเอียงขึ้น (Bullish Tilt)", "#3ecf6e"
    elif combined_lean < -25:
        combined_verdict, combined_color = "โน้มเอียงลง (Bearish Tilt)", "#e5534b"
    else:
        combined_verdict, combined_color = "กลางๆ ไม่มีสัญญาณชัดเจน (Neutral)", "#d4af37"

    st.markdown(
        f"""
        <div style="background:linear-gradient(145deg, #1a1c24, #101218); border:1px solid rgba(212,175,55,0.4); border-radius:12px; padding:20px 24px; margin-bottom:12px;">
            <div style="font-size:13px; color:#d4af37; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">สรุปรวมสัญญาณตลาด+เทคนิค ({combined_source_count} แหล่งข้อมูล)</div>
            <div style="font-size:36px; font-weight:700; color:{combined_color}; font-family:'IBM Plex Mono', monospace;">
                {combined_lean:+.1f}%
            </div>
            <div style="font-size:16px; color:#f4f0e6; margin-top:4px;">{combined_verdict}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        "⚠️ ตัวเลขนี้คือค่าเฉลี่ยของสัญญาณสถิติด้านตลาด/เทคนิคทั้งหมด ยังไม่รวมพื้นฐานธุรกิจ (10 มิติด้านล่าง) "
        "ไม่ใช่การรับประกันทิศทางราคา และไม่ควรใช้เป็นเหตุผลเดียวในการตัดสินใจซื้อ-ขาย"
    )

    st.markdown("---")
    # ---------- สรุปผลรวมทั้งหมด (fundamentals + สัญญาณตลาด/เทคนิคทั้งหมด) ----------
    st.markdown(f'<div class="section-label">◆ สรุปสุดท้าย — รวมทุกขั้นเป็นตัวเลขเดียว — {ticker}</div>', unsafe_allow_html=True)

    fundamental_lean = (analysis["overall_score"] - 50) * 2  # แปลง 0-100 -> -100..100
    master_lean = round((fundamental_lean + combined_lean + macro_lean) / 3, 1)

    if master_lean > 25:
        master_verdict, master_color = "ภาพรวมเอียงบวก (Bullish)", "#3ecf6e"
    elif master_lean < -25:
        master_verdict, master_color = "ภาพรวมเอียงลบ (Bearish)", "#e5534b"
    else:
        master_verdict, master_color = "ภาพรวมกลางๆ ยังไม่มีสัญญาณชัดเจน (Neutral)", "#d4af37"

    # หาจุดแข็งสุด/จุดอ่อนสุดจาก 10 มิติ
    dim_items = [(scoring.DIMENSION_NAMES_TH[k], v["score"]) for k, v in analysis["dimensions"].items()]
    strongest = max(dim_items, key=lambda x: x[1])
    weakest = min(dim_items, key=lambda x: x[1])
    n_green = sum(1 for _, s in dim_items if s >= 70)
    n_red = sum(1 for _, s in dim_items if s < 45)

    st.markdown(
        f"""
        <div style="background:linear-gradient(145deg, #1a1c24, #101218); border:1px solid rgba(212,175,55,0.5); border-radius:14px; padding:24px 28px; margin-bottom:14px;">
            <div style="font-size:13px; color:#d4af37; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:8px;">คะแนนสรุปสุดท้าย — รวมพื้นฐานธุรกิจ + สัญญาณตลาดทั้งหมด</div>
            <div style="font-size:42px; font-weight:700; color:{master_color}; font-family:'IBM Plex Mono', monospace;">
                {master_lean:+.1f}%
            </div>
            <div style="font-size:17px; color:#f4f0e6; margin-top:4px;">{master_verdict}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("**อ่านสรุปเป็นข้อความ:**")
    summary_lines = [
        f"พื้นฐานธุรกิจ (10 มิติ) อยู่ที่ {analysis['overall_score']}/100 — {analysis['overall_label']} "
        f"(มี {n_green} มิติที่แข็งแกร่ง และ {n_red} มิติที่ต้องระวัง)",
        f"จุดแข็งที่สุด: **{strongest[0]}** ({strongest[1]}/100)",
        f"จุดที่ควรระวังที่สุด: **{weakest[0]}** ({weakest[1]}/100)",
        f"สัญญาณตลาด+เทคนิครวม (Options, Insider, Institution, Analyst, Technical, Momentum, "
        f"Relative Strength, IV Skew, Earnings, News): {combined_lean:+.1f}% — {combined_verdict}",
    ]
    if one_month.get("available"):
        summary_lines.append(f"แนวโน้มในกรอบ 1 เดือนข้างหน้า: {om_lean:+.1f}% — {one_month['verdict']}")
        if one_month.get("earnings_within_month"):
            summary_lines.append("⚠️ มีวันประกาศผลประกอบการอยู่ในกรอบเดือนนี้ — เป็นทั้งโอกาสและความเสี่ยงที่ควรจับตาเป็นพิเศษ")

    summary_lines.append(f"บรรยากาศตลาดโดยรวม (VIX + อัตราผลตอบแทนพันธบัตร): {macro_lean:+.1f}%")

    if bt_result.get("available") and bt_result.get("overall_accuracy") is not None:
        summary_lines.append(
            f"ทดสอบย้อนหลัง: สัญญาณ Technical แม่นยำ {bt_result['overall_accuracy']:.1f}% "
            f"ในอดีต (เทียบเดาสุ่ม 50%) — ใช้ประกอบการตัดสินใจว่าควรเชื่อสัญญาณ technical ของหุ้นตัวนี้มากแค่ไหน"
        )

    for line in summary_lines:
        st.write(f"• {line}")

    st.caption(
        "⚠️ นี่คือการสรุปผลจากสูตรคณิตศาสตร์รวมทุกข้อมูลที่ระบบหาได้ฟรี ไม่ใช่คำแนะนำซื้อ-ขาย "
        "และไม่มีระบบใดทำนายราคาหุ้นได้แม่นยำ 100% ควรศึกษาข้อมูลเพิ่มเติมด้วยตัวเองเสมอก่อนตัดสินใจ"
    )

    st.markdown("---")
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

    st.markdown("---")
    st.caption(
        "ข้อมูลทั้งหมดนี้เป็นการวิเคราะห์เชิงปริมาณจากสูตรคณิตศาสตร์ ไม่ใช่คำแนะนำการลงทุน "
        "ควรใช้ประกอบการตัดสินใจร่วมกับการศึกษาข้อมูลด้วยตัวเองเสมอ"
    )
