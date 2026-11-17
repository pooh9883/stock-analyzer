# -*- coding: utf-8 -*-
"""
home_ui.py
==========
หน้าแรก (Dashboard): ดัชนีตลาด · Sector Rotation · และข้อมูลของหุ้นใน Watchlist ของคุณ
(ปฏิทินงบ · ราคาเป้าหมายนักวิเคราะห์ · Insider ซื้อ-ขาย · ข่าว)

เรียกใช้จาก app.py:  home_ui.render_home()
ใช้รายชื่อ Watchlist เดียวกับโหมดสแกนเนอร์ (watchlist.json)

⚠️ ข้อมูลฟรีจาก Yahoo / Google News อาจดีเลย์หรือไม่ครบทุกหุ้น ไม่ใช่คำแนะนำซื้อ-ขาย
"""

from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import streamlit as st
import yfinance as yf

import news_radar
import rocket
import rocket_ui

GOLD, GREEN, RED, TEXT, GREY = "#fcee0a", "#19f5a5", "#ff2a6d", "#e6f1ff", "#7d86a6"

MARKETS = [("S&P 500", "^GSPC"), ("Nasdaq 100", "^NDX"), ("ทองคำ", "GC=F"),
           ("Bitcoin", "BTC-USD"), ("USD/THB", "THB=X"), ("SET", "^SET.BK")]

SECTORS = [("เทคโนโลยี", "XLK"), ("การเงิน", "XLF"), ("สุขภาพ", "XLV"), ("พลังงาน", "XLE"),
           ("ค้าปลีก/สินค้าฟุ่มเฟือย", "XLY"), ("สินค้าจำเป็น", "XLP"), ("อุตสาหกรรม", "XLI"),
           ("สื่อสาร/บันเทิง", "XLC"), ("วัตถุดิบ", "XLB"), ("สาธารณูปโภค", "XLU"), ("อสังหาริมทรัพย์", "XLRE")]

REC_TH = {"strong_buy": "ซื้อแรง", "buy": "ซื้อ", "hold": "ถือ", "underperform": "ต่ำกว่าตลาด", "sell": "ขาย", "strong_sell": "ขายแรง"}


def _html(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


def _show_df(df, **kw):
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


def _pmap(fn, items, workers=8):
    def safe(x):
        try:
            return fn(x)
        except Exception:
            return None
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(safe, items))


def _watchlist() -> list:
    if "rk_text" in st.session_state:
        syms = rocket_ui._parse(st.session_state["rk_text"])
    else:
        syms = rocket_ui._load_watch()
    return syms[:rocket_ui.MAX_SYMBOLS]


# ===============================================================
# ดัชนีตลาด
# ===============================================================
@st.cache_data(ttl=120, show_spinner=False)
def _markets():
    syms = [s for _, s in MARKETS]
    data = yf.download(" ".join(syms), period="5d", interval="1d", group_by="ticker", progress=False, threads=True)
    out = {}
    for name, s in MARKETS:
        d = rocket._pick(data, s)
        if d is None or "Close" not in d.columns:
            out[name] = None
            continue
        c = d["Close"].dropna()
        out[name] = (float(c.iloc[-1]), float((c.iloc[-1] / c.iloc[-2] - 1) * 100)) if len(c) >= 2 else None
    return out


def _render_markets():
    st.markdown("#### 🌐 ดัชนีตลาด")
    try:
        mk = _markets()
    except Exception as e:
        st.caption(f"ดึงดัชนีไม่ได้: {e}")
        return
    for row in (MARKETS[:3], MARKETS[3:]):
        cols = st.columns(3)
        for col, (name, _) in zip(cols, row):
            v = mk.get(name)
            if v:
                col.metric(name, f"{v[0]:,.2f}", f"{v[1]:+.2f}%")
            else:
                col.metric(name, "—", help="ดึงข้อมูลไม่ได้ (บางดัชนีอาจไม่มีใน Yahoo)")


# ===============================================================
# Sector Rotation
# ===============================================================
@st.cache_data(ttl=300, show_spinner=False)
def _sectors():
    etfs = [e for _, e in SECTORS]
    data = yf.download(" ".join(etfs), period="1mo", interval="1d", group_by="ticker", progress=False, threads=True)
    out = {}
    for name, e in SECTORS:
        d = rocket._pick(data, e)
        if d is None or "Close" not in d.columns:
            continue
        c = d["Close"].dropna()
        if len(c) < 6:
            continue
        out[name] = {"1d": float((c.iloc[-1] / c.iloc[-2] - 1) * 100),
                     "5d": float((c.iloc[-1] / c.iloc[-6] - 1) * 100),
                     "1m": float((c.iloc[-1] / c.iloc[0] - 1) * 100)}
    return out


def _sector_bars(items):
    """แถบซ้าย-ขวาจากจุดกลาง: items = [(ชื่อกลุ่ม, เปอร์เซ็นต์)] เรียงมาก→น้อย"""
    if not items:
        return
    mx = max(abs(x) for _, x in items) or 1
    html = ""
    for name, x in items:
        w = abs(x) / mx * 50
        col = GREEN if x >= 0 else RED
        left = 50 if x >= 0 else 50 - w
        html += f"""
            <div style="display:flex;align-items:center;gap:12px;padding:6px 0;border-bottom:1px solid #1d2030;">
            <div style="width:170px;color:{TEXT};font-size:14px;">{name}</div>
            <div style="flex:1;position:relative;height:10px;background:#242733;border-radius:5px;">
            <div style="position:absolute;left:50%;top:-2px;width:2px;height:14px;background:#5a5d6b;"></div>
            <div style="position:absolute;left:{left}%;width:{w}%;height:10px;background:{col};border-radius:5px;"></div>
            </div>
            <div style="width:70px;text-align:right;color:{col};font-weight:700;">{x:+.2f}%</div>
            </div>"""
    st.markdown(_html(html), unsafe_allow_html=True)


# ---------------------------------------------------------------
# ก่อนตลาดเปิด: ดูว่ากลุ่มไหนเริ่มขยับตั้งแต่ก่อนเปิด
# ---------------------------------------------------------------
@st.cache_data(ttl=60, show_spinner=False)
def _premarket():
    """ราคานอกเวลาทำการของ ETF ตัวแทนกลุ่ม (ก่อนเปิด/หลังปิด) เทียบราคาปิดปกติ + ฟิวเจอร์สดัชนี"""
    def one(it):
        name, sym = it
        info = yf.Ticker(sym).info or {}
        state = str(info.get("marketState", "")).upper()
        reg = info.get("regularMarketPrice")
        if sym.endswith("=F"):                       # ฟิวเจอร์สซื้อขายเกือบตลอดวัน ใช้ % เทียบราคาปิดก่อนหน้า
            pct = info.get("regularMarketChangePercent")
            return {"name": name, "state": state, "pct": float(pct) if pct is not None else None}
        ext = None
        if state in ("PRE", "PREPRE"):
            ext = info.get("preMarketPrice")
        elif state in ("POST", "POSTPOST", "CLOSED"):
            ext = info.get("postMarketPrice") or info.get("preMarketPrice")
        pct = (float(ext) / float(reg) - 1) * 100 if ext and reg else None
        return {"name": name, "state": state, "pct": pct}
    items = [(n, e) for n, e in SECTORS] + [("S&P 500", "ES=F"), ("Nasdaq 100", "NQ=F")]
    res = _pmap(one, items)
    sec = {r["name"]: r for r in res[:len(SECTORS)] if r}
    fut = {r["name"]: r for r in res[len(SECTORS):] if r}
    state = next((r["state"] for r in sec.values() if r.get("state")), "")
    return {"state": state, "sectors": sec, "fut": fut}


def _et_session_dates():
    """คืน (วันเทรดถัดไปตามเวลาสหรัฐ, วันเทรดก่อนหน้า, ใช้เวลาออมแสงไหม)"""
    import calendar_ui
    from datetime import datetime, timedelta
    dst = calendar_ui._us_dst(datetime.utcnow().date())
    et = datetime.utcnow() - timedelta(hours=4 if dst else 5)
    d = et.date()
    if et.hour >= 16:
        d += timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    prev = d - timedelta(days=1)
    while prev.weekday() >= 5:
        prev -= timedelta(days=1)
    return d, prev, dst


def _big_earnings_by_sector(min_cap=50e9):
    """หุ้นตัวใหญ่ที่ประกาศงบรอบนี้ แยกตามกลุ่ม: หลังปิดวันเทรดก่อนหน้า (ประกาศไปแล้ว) · ก่อนเปิด/หลังปิดวันเทรดถัดไป"""
    import calendar_ui
    sess, prev, _ = _et_session_dates()
    rows = []
    for d, want in ((prev, "time-after-hours"), (sess, "time-pre-market"), (sess, "time-after-hours")):
        for r in calendar_ui._nasdaq_day(d.isoformat()):
            if r["time"] == want and r["cap"] >= min_cap:
                rows.append(dict(r, d=d))
    if not rows:
        return {}
    secs = calendar_ui._sector_batch(tuple(sorted({r["sym"] for r in rows})))
    etf2name = {e: n for n, e in SECTORS}
    out = {}
    for r in sorted(rows, key=lambda r: -r["cap"]):
        etf = calendar_ui._YF_SECTOR_ETF.get((secs.get(r["sym"]) or {}).get("sector", ""))
        name = etf2name.get(etf)
        if name:
            out.setdefault(name, []).append(r)
    return out


def _render_premarket():
    try:
        d = _premarket()
    except Exception as e:
        st.caption(f"ดึงข้อมูลก่อนตลาดเปิดไม่ได้: {e}")
        return
    state = d.get("state", "")
    if state == "REGULAR":
        st.info("ตลาดสหรัฐเปิดอยู่ตอนนี้ ดูผลจริงที่แท็บ **วันนี้** ได้เลยครับ แท็บนี้ใช้ตอนก่อนตลาดเปิดหรือหลังตลาดปิด")
        return
    label = {"PRE": "ก่อนตลาดเปิด", "PREPRE": "ก่อนตลาดเปิด"}.get(state, "หลังตลาดปิด / รอเปิด")
    try:
        sess, prev, dst = _et_session_dates()
        open_th = "20:30" if dst else "21:30"
        pre_th = "15:00" if dst else "16:00"
        post_end = "07:00" if dst else "08:00"
        st.caption(f"สถานะตอนนี้: **{label}** · ช่วงก่อนตลาดเปิดเริ่มประมาณ {pre_th} น. · ตลาดเปิด {open_th} น. (เวลาไทย) · ช่วงหลังตลาดปิดจบประมาณ {post_end} น.")
    except Exception:
        st.caption(f"สถานะตอนนี้: **{label}**")
    fut = d.get("fut", {})
    if fut:
        cols = st.columns(len(fut))
        for col, (name, r) in zip(cols, fut.items()):
            col.metric(name + " ฟิวเจอร์ส", f"{r['pct']:+.2f}%" if r.get("pct") is not None else "—",
                       help="ซื้อขายเกือบตลอดวัน บอกทิศทางของตลาดรวมก่อนเปิด (ไม่แยกกลุ่ม)")
    items = sorted([(n, r["pct"]) for n, r in d.get("sectors", {}).items() if r.get("pct") is not None], key=lambda kv: kv[1], reverse=True)
    if not items:
        st.caption("ยังไม่มีราคานอกเวลาทำการของ ETF กลุ่มต่างๆ (Yahoo อาจยังไม่ส่งข้อมูล ลองใหม่หลังประมาณ 16:00 น. ไทย)")
    else:
        st.markdown("**ราคานอกเวลาทำการของ ETF แต่ละกลุ่ม เทียบราคาปิดปกติ**")
        _sector_bars(items)
    try:
        by = _big_earnings_by_sector()
    except Exception:
        by = {}
    if by:
        _mn = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
        _tm = {"time-after-hours": "หลังปิด", "time-pre-market": "ก่อนเปิด"}
        rows = ""
        for name, lst in by.items():
            chips = "".join(
                '<span style="display:inline-block;margin:2px 6px 2px 0;padding:1px 8px;border:1px solid rgba(154,164,196,.35);font-size:12.5px;color:#c0c9e4">'
                f'<b style="color:{GOLD}">{r["sym"]}</b> {_tm.get(r["time"], "")} {r["d"].day} {_mn[r["d"].month - 1]}</span>'
                for r in lst[:4])
            rows += (f'<div style="display:flex;gap:12px;padding:5px 0;border-bottom:1px solid #1d2030;align-items:baseline">'
                     f'<div style="width:170px;color:{TEXT};font-size:14px">{name}</div><div style="flex:1">{chips}</div></div>')
        st.markdown("**หุ้นตัวใหญ่ที่ประกาศงบรอบนี้ (มูลค่าตลาด ≥ $50B) แยกตามกลุ่ม** · ตัวใหญ่ขยับแรงหลังงบ มักดึงทั้งกลุ่ม")
        st.markdown(_html(rows), unsafe_allow_html=True)
    st.caption("⚠️ ช่วงก่อนเปิด/หลังปิดมีคนซื้อขายน้อย ราคากระโดดง่ายและมักไม่ไปต่อหลังตลาดเปิด ใช้ดูว่ากลุ่มไหนเริ่มผิดปกติ ไม่ใช่ตัวทำนายผลทั้งวัน · ไม่ใช่คำแนะนำซื้อ-ขาย")


def _render_sectors():
    st.markdown("#### 🔄 Sector Rotation — เงินไหลไปกลุ่มไหน")
    hz = st.radio("ช่วงเวลา", ["วันนี้", "5 วัน", "1 เดือน", "ก่อนตลาดเปิด"], horizontal=True, key="home_sec_h", label_visibility="collapsed")
    if hz == "ก่อนตลาดเปิด":
        _render_premarket()
        return
    key = {"วันนี้": "1d", "5 วัน": "5d", "1 เดือน": "1m"}[hz]
    try:
        data = _sectors()
    except Exception as e:
        st.caption(f"ดึงข้อมูลกลุ่มอุตสาหกรรมไม่ได้: {e}")
        return
    if not data:
        st.caption("ดึงข้อมูลกลุ่มอุตสาหกรรมไม่ได้")
        return
    _sector_bars(sorted([(n, v[key]) for n, v in data.items()], key=lambda kv: kv[1], reverse=True))
    st.caption("วัดจาก ETF ตัวแทนแต่ละกลุ่ม (SPDR Select Sector) · กลุ่มที่นำตลาดต่อเนื่องหลายช่วงมักสะท้อนเงินที่ไหลเข้า")


# ===============================================================
# ข้อมูลของหุ้นใน Watchlist
# ===============================================================
def _earn(sym):
    cal = yf.Ticker(sym).calendar
    ed = None
    if isinstance(cal, dict):
        v = cal.get("Earnings Date")
        ed = v[0] if isinstance(v, (list, tuple)) and v else v
    return None if ed is None else pd.Timestamp(ed)


@st.cache_data(ttl=21600, show_spinner=False)
def _earnings(symbols: tuple):
    res = _pmap(_earn, symbols)
    return {s: r for s, r in zip(symbols, res)}


def _target(sym):
    i = yf.Ticker(sym).info
    price = i.get("currentPrice") or i.get("regularMarketPrice")
    tm = i.get("targetMeanPrice")
    if not price or not tm:
        return None
    return {"price": float(price), "mean": float(tm), "high": i.get("targetHighPrice"), "low": i.get("targetLowPrice"),
            "n": i.get("numberOfAnalystOpinions"), "rec": i.get("recommendationKey")}


@st.cache_data(ttl=3600, show_spinner=False)
def _targets(symbols: tuple):
    res = _pmap(_target, symbols)
    return {s: r for s, r in zip(symbols, res)}


def _insider(sym):
    ins = yf.Ticker(sym).insider_transactions
    if ins is None or ins.empty:
        return None
    text_col = next((c for c in ["Text", "Transaction"] if c in ins.columns), None)
    date_col = next((c for c in ["Start Date", "Date"] if c in ins.columns), None)
    if not text_col or not date_col:
        return None
    d = ins.copy()
    d[date_col] = pd.to_datetime(d[date_col], errors="coerce")
    d = d[d[date_col] >= pd.Timestamp.today() - pd.Timedelta(days=90)].sort_values(date_col, ascending=False)
    txt = d[text_col].astype(str).str.lower()
    d = d.assign(_buy=txt.str.contains("purchase|buy"), _sell=txt.str.contains("sale|sell"))
    rows = []
    for _, r in d.head(8).iterrows():
        rows.append({
            "วันที่": r[date_col].strftime("%Y-%m-%d") if pd.notna(r[date_col]) else "",
            "ผู้บริหาร": str(r.get("Insider", "")), "ตำแหน่ง": str(r.get("Position", "")),
            "รายการ": "🟢 ซื้อ" if r["_buy"] else ("🔴 ขาย" if r["_sell"] else "อื่น ๆ"),
            "หุ้น": r.get("Shares"), "มูลค่า ($)": r.get("Value"),
        })
    return {"buys": int(d["_buy"].sum()), "sells": int(d["_sell"].sum()), "rows": rows}


@st.cache_data(ttl=3600, show_spinner=False)
def _insiders(symbols: tuple):
    res = _pmap(_insider, symbols)
    return {s: r for s, r in zip(symbols, res)}


@st.cache_data(ttl=600, show_spinner=False)
def _news(sym: str):
    return news_radar.fetch_google_news(f"{sym} stock", max_items=4)


def _render_watch_panels(symbols: list):
    st.markdown("#### ⭐ ข้อมูลของหุ้นใน Watchlist ของคุณ")
    st.caption(f"{len(symbols)} ตัว: {', '.join(symbols)} · แก้ไขรายชื่อได้ที่โหมด 🚀 สแกนเนอร์ Watchlist")
    view = st.radio("ดูข้อมูล", ["📅 ปฏิทินงบ", "🎯 ราคาเป้าหมาย", "🕵️ Insider ซื้อ-ขาย", "📰 ข่าว"],
                    horizontal=True, key="home_view", label_visibility="collapsed")
    syms = tuple(symbols)

    if view.startswith("📅"):
        with st.spinner("กำลังดึงวันประกาศงบ..."):
            earn = _earnings(syms)
        rows = []
        today = pd.Timestamp.today().normalize()
        for s, d in earn.items():
            if d is None:
                continue
            days = (d.normalize() - today).days
            if days >= -1:
                rows.append({"หุ้น": s, "วันประกาศงบ": d.strftime("%Y-%m-%d"), "อีกกี่วัน": days,
                             "": "⏰ ภายใน 7 วัน" if days <= 7 else ""})
        if rows:
            _show_df(pd.DataFrame(sorted(rows, key=lambda r: r["อีกกี่วัน"])), hide_index=True)
            st.caption("ช่วงใกล้ประกาศงบราคามักแกว่งแรงทั้งสองทาง · วันที่เป็นประมาณการจาก Yahoo อาจเลื่อนได้")
        else:
            st.caption("ไม่พบวันประกาศงบที่กำลังจะมาถึงของหุ้นใน Watchlist (หรือดึงข้อมูลไม่ได้)")

    if view.startswith("🎯"):
        with st.spinner("กำลังดึงราคาเป้าหมาย..."):
            tg = _targets(syms)
        rows = []
        for s, v in tg.items():
            if not v:
                continue
            rows.append({"หุ้น": s, "ราคาปัจจุบัน": round(v["price"], 2), "เป้าหมายเฉลี่ย": round(v["mean"], 2),
                         "ส่วนต่าง %": round((v["mean"] / v["price"] - 1) * 100, 1),
                         "ต่ำสุด": v["low"], "สูงสุด": v["high"], "จำนวนนักวิเคราะห์": v["n"],
                         "คำแนะนำ": REC_TH.get(v["rec"], v["rec"] or "")})
        if rows:
            _show_df(pd.DataFrame(sorted(rows, key=lambda r: -r["ส่วนต่าง %"])), hide_index=True)
            st.caption("ราคาเป้าหมายของนักวิเคราะห์มักตามหลังราคาจริงและมีอคติเชิงบวก ใช้เป็นภาพประกอบ ไม่ใช่ตัวทำนาย")
        else:
            st.caption("ดึงราคาเป้าหมายไม่ได้ (หรือหุ้นเหล่านี้ไม่มีนักวิเคราะห์ครอบคลุม)")

    if view.startswith("🕵"):
        with st.spinner("กำลังดึง Insider..."):
            ins = _insiders(syms)
        summary = [{"หุ้น": s, "ซื้อ (90 วัน)": v["buys"], "ขาย (90 วัน)": v["sells"],
                    "สุทธิ": "🟢 ซื้อมากกว่า" if v["buys"] > v["sells"] else ("🔴 ขายมากกว่า" if v["sells"] > v["buys"] else "เสมอ")}
                   for s, v in ins.items() if v and (v["buys"] or v["sells"])]
        if summary:
            _show_df(pd.DataFrame(summary), hide_index=True)
            pick = st.selectbox("ดูรายการล่าสุดของ", [r["หุ้น"] for r in summary], key="home_ins_pick")
            if ins.get(pick) and ins[pick]["rows"]:
                _show_df(pd.DataFrame(ins[pick]["rows"]), hide_index=True)
            st.caption("ผู้บริหารขายหุ้นมีเหตุผลได้หลายอย่าง (ภาษี แผนขายล่วงหน้า) ส่วนการซื้อด้วยเงินตัวเองมักเป็นสัญญาณที่มีน้ำหนักกว่า")
        else:
            st.caption("ไม่พบธุรกรรม insider ใน 90 วันล่าสุด (หรือดึงข้อมูลไม่ได้)")

    if view.startswith("📰"):
        pick = st.selectbox("เลือกหุ้น", symbols, key="home_news_pick")
        with st.spinner("กำลังดึงข่าว..."):
            items = _news(pick)
        if not items:
            st.caption("ไม่พบข่าว หรือดึงไม่ได้ตอนนี้")
        for it in items:
            tone = "🟢" if it["sentiment_score"] > 0 else ("🔴" if it["sentiment_score"] < 0 else "⚪")
            st.markdown(f"{tone} [{it['title']}]({it['link']}) — <span style='color:{GREY}'>{it['source']}</span>", unsafe_allow_html=True)
        st.caption("ได้แค่หัวข้อ + ลิงก์ (ไม่ใช่เนื้อข่าวเต็ม) · อารมณ์ข่าว 🟢/🔴 ประเมินจากคำสำคัญในหัวข้อ ไม่แม่นยำเต็มที่")


def render_home():
    with st.expander("📖 หน้านี้ใช้ยังไง", expanded=False):
        st.markdown(
            """
หน้าแรกรวมสิ่งที่ควรเช็กทุกเช้าไว้ที่เดียว อ่านจากบนลงล่าง:
1. **ดัชนีตลาด** วันนี้ตลาดเขียวหรือแดง ทอง/บิตคอยน์/ค่าเงินบาทเป็นยังไง
2. **Sector Rotation** กลุ่มไหนนำ กลุ่มไหนตก (เลือกช่วงวันนี้/5 วัน/1 เดือนได้)
3. **ข้อมูลของหุ้นใน Watchlist** ปฏิทินงบ ราคาเป้าหมาย Insider และข่าว ของหุ้นที่คุณใส่ไว้

รายชื่อ Watchlist แก้ได้ที่โหมด 🚀 สแกนเนอร์ Watchlist · ข้อมูลฟรีอาจดีเลย์ ใช้ประกอบการตัดสินใจ ไม่ใช่คำแนะนำซื้อ-ขาย
"""
        )
    _render_markets()
    try:
        import sentiment_ui
        sentiment_ui.render_market_mood()
    except Exception as e:
        st.caption("อารมณ์ตลาดแสดงไม่ได้: " + str(e))
    st.markdown("---")
    _render_sectors()
    st.markdown("---")
    symbols = _watchlist()
    if symbols:
        # ยุบไว้ก่อน: สายซิ่งไม่ต้องดูทุกเช้า (งบสำคัญสรุปให้แล้วในกล่อง "สรุปเช้านี้") ติ๊กเมื่ออยากดู จะดึงข้อมูลตอนติ๊กเท่านั้น หน้าแรกจึงเร็วขึ้นด้วย
        if st.checkbox("\u2B50 แสดงข้อมูลหุ้นใน Watchlist (ปฏิทินงบ \u00b7 ราคาเป้าหมาย \u00b7 Insider \u00b7 ข่าว)", value=False, key="home_show_watch"):
            _render_watch_panels(symbols)
    else:
        st.info("ยังไม่มีหุ้นใน Watchlist ไปเพิ่มที่โหมด 🚀 สแกนเนอร์ Watchlist ก่อนครับ")
    st.caption("ไม่ใช่คำแนะนำการลงทุน การลงทุนมีความเสี่ยง ผู้ลงทุนต้องมีความรู้ความเข้าใจในการลงทุน")