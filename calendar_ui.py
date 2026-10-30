# -*- coding: utf-8 -*-
"""
calendar_ui.py  [calendar v1]
=============================
ปฏิทินเหตุการณ์ของหุ้นที่ติดตาม รวมไว้หน้าเดียว เรียงตามวัน:
  • 📊 วันประกาศงบ (ประมาณการจาก Yahoo — อาจเลื่อนได้)
  • 💰 วันขึ้นเครื่องหมาย XD (Ex-Dividend) และวันจ่ายปันผล (ถ้า Yahoo มีข้อมูล)
  • 🏦 วันประชุมเฟด FOMC (ตารางที่เฟดประกาศไว้ล่วงหน้า — วันตัดสินใจคือวันที่ 2 ของการประชุม)
ข้อจำกัด: ข้อมูลปันผล/งบมาจาก Yahoo บางหุ้นไม่มี และวันที่อาจเปลี่ยนได้ ควรเช็กกับประกาศบริษัทอีกครั้ง
"""
import html
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from urllib.request import Request, urlopen

import pandas as pd
import streamlit as st
import yfinance as yf

import home_ui

# ตารางประชุม FOMC (วันเริ่ม, วันตัดสินใจ, มี SEP/แผนภูมิจุด ไหม) — แหล่ง: ตารางที่ Federal Reserve ประกาศ
# ปี 2027 เป็นตารางเบื้องต้น (tentative) อาจถูกปรับภายหลัง
FOMC = [
    (date(2026, 1, 27), date(2026, 1, 28), False), (date(2026, 3, 17), date(2026, 3, 18), True),
    (date(2026, 4, 28), date(2026, 4, 29), False), (date(2026, 6, 16), date(2026, 6, 17), True),
    (date(2026, 7, 28), date(2026, 7, 29), False), (date(2026, 9, 15), date(2026, 9, 16), True),
    (date(2026, 10, 27), date(2026, 10, 28), False), (date(2026, 12, 8), date(2026, 12, 9), True),
    (date(2027, 1, 26), date(2027, 1, 27), False), (date(2027, 3, 16), date(2027, 3, 17), True),
    (date(2027, 4, 27), date(2027, 4, 28), False), (date(2027, 6, 8), date(2027, 6, 9), True),
    (date(2027, 7, 27), date(2027, 7, 28), False), (date(2027, 9, 14), date(2027, 9, 15), True),
    (date(2027, 10, 26), date(2027, 10, 27), False), (date(2027, 12, 7), date(2027, 12, 8), True),
]

_TH_M = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
_TH_D = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]
TYPES = {
    "earn": ("📊 ประกาศงบ", "#fcee0a"),
    "exdiv": ("💰 XD (ขึ้นเครื่องหมายไม่รับปันผล)", "#19f5a5"),
    "paydiv": ("💰 จ่ายปันผล", "#19f5a5"),
    "fomc": ("🏦 ประชุมเฟด", "#ff2a6d"),
}


def _e(x):
    return html.escape(str(x if x is not None else ""), quote=True)


def _to_date(x):
    if x is None:
        return None
    try:
        if isinstance(x, (list, tuple)):
            x = x[0] if x else None
            if x is None:
                return None
        ts = pd.Timestamp(x)
        return None if pd.isna(ts) else ts.date()
    except Exception:
        return None


def _one(sym: str) -> dict:
    out = {"earn": None, "exdiv": None, "paydiv": None, "name": sym}
    try:
        t = yf.Ticker(sym)
        cal = t.calendar
        if isinstance(cal, dict):
            out["earn"] = _to_date(cal.get("Earnings Date"))
            out["exdiv"] = _to_date(cal.get("Ex-Dividend Date"))
            out["paydiv"] = _to_date(cal.get("Dividend Date"))
        try:
            out["name"] = (t.info or {}).get("shortName") or sym
        except Exception:
            pass
    except Exception:
        pass
    return out


@st.cache_data(ttl=6 * 3600, show_spinner=False)
def _fetch(symbols: tuple) -> dict:
    res = home_ui._pmap(_one, symbols)
    return {s: (r or {"earn": None, "exdiv": None, "paydiv": None, "name": s}) for s, r in zip(symbols, res)}


# ---------------------------------------------------------------
# ค้นหางบที่กำลังจะประกาศ "ทั้งตลาด" อัตโนมัติ (ปฏิทินงบสาธารณะของ Nasdaq — ฟรี ไม่ต้องมีคีย์)
# ---------------------------------------------------------------
def _money(s) -> float:
    try:
        return float(str(s).replace("$", "").replace(",", "").strip() or 0)
    except Exception:
        return 0.0


@st.cache_data(ttl=3 * 3600, show_spinner=False)
def _nasdaq_day(day_iso: str) -> list:
    try:
        req = Request(
            f"https://api.nasdaq.com/api/calendar/earnings?date={day_iso}",
            headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json, text/plain, */*",
                     "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"},
        )
        with urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode("utf-8"))
        rows = (data.get("data") or {}).get("rows") or []
        out = []
        for x in rows:
            sym = (x.get("symbol") or "").strip().upper()
            if not sym:
                continue
            out.append({"sym": sym, "name": x.get("name") or sym, "cap": _money(x.get("marketCap")),
                        "time": x.get("time") or "", "eps": x.get("epsForecast") or "",
                        "qtr": x.get("fiscalQuarterEnding") or "", "date": day_iso})
        return out
    except Exception:
        return []


_TIME_TH = {"time-pre-market": "ก่อนตลาดเปิด", "time-after-hours": "หลังตลาดปิด"}


def auto_earnings(horizon_days: int, min_cap: float, today: date = None, limit: int = 80) -> list:
    """งบที่จะประกาศในช่วงข้างหน้า เฉพาะบริษัทที่มูลค่าตลาด >= min_cap เรียงตามวัน แล้วตามขนาดบริษัท"""
    today = today or date.today()
    days = [today + timedelta(days=i) for i in range(horizon_days + 1)]
    days = [d for d in days if d.weekday() < 5]
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(lambda d: _nasdaq_day(d.isoformat()), days))
    events = []
    for d, rows in zip(days, res):
        for r in rows:
            if r["cap"] < min_cap:
                continue
            bits = []
            if r["time"] in _TIME_TH:
                bits.append(_TIME_TH[r["time"]])
            if r["eps"]:
                bits.append(f"คาด EPS {r['eps']}")
            if r["qtr"]:
                bits.append(f"งวด {r['qtr']}")
            if r["cap"]:
                bits.append("มูลค่าตลาด " + (f"${r['cap'] / 1e12:.2f}T" if r["cap"] >= 1e12 else f"${r['cap'] / 1e9:,.0f}B"))
            events.append({"date": d, "kind": "earn", "sym": r["sym"], "name": r["name"],
                           "note": " · ".join(bits), "cap": r["cap"]})
    events.sort(key=lambda e: (e["date"], -e.get("cap", 0)))
    # จำกัดจำนวนต่อวันไม่ให้ล้น: เอาตัวใหญ่สุดก่อน รวมแล้วไม่เกิน limit
    keep, total = [], 0
    for e in sorted(events, key=lambda e: -e.get("cap", 0)):
        if total < limit:
            keep.append(e)
            total += 1
    keep.sort(key=lambda e: (e["date"], -e.get("cap", 0)))
    return keep


def th_date(d: date) -> str:
    return f"{_TH_D[d.weekday()]} {d.day} {_TH_M[d.month - 1]} {d.year + 543}"


def build_events(symbols: tuple, kinds: set, horizon_days: int, today: date = None) -> list:
    today = today or date.today()
    events = []
    data = _fetch(symbols) if symbols and kinds & {"earn", "exdiv", "paydiv"} else {}
    for s, d in data.items():
        for k in ("earn", "exdiv", "paydiv"):
            if k in kinds and d.get(k):
                events.append({"date": d[k], "kind": k, "sym": s, "name": d["name"], "note": ""})
    if "fomc" in kinds:
        for start, decide, sep in FOMC:
            events.append({"date": decide, "kind": "fomc", "sym": "FOMC", "name": "Federal Reserve",
                           "note": f"ประชุม {start.day}–{decide.day} {_TH_M[decide.month - 1]} · ประกาศอัตราดอกเบี้ยวันนี้"
                                   + (" · มีแผนภูมิจุด (SEP)" if sep else "")
                                   + (" · ตารางปี 2027 เป็นแบบเบื้องต้น" if decide.year >= 2027 else "")})
    out = [e for e in events if 0 <= (e["date"] - today).days <= horizon_days]
    out.sort(key=lambda e: (e["date"], e["kind"], e["sym"]))
    return out


def _card(e, today):
    days = (e["date"] - today).days
    label, color = TYPES[e["kind"]]
    when = "วันนี้" if days == 0 else ("พรุ่งนี้" if days == 1 else f"อีก {days} วัน")
    hot = days <= 7
    note = e["note"] or ("ช่วงใกล้ประกาศงบราคามักแกว่งแรง" if e["kind"] == "earn" else "")
    return (
        f'<div style="display:flex;gap:14px;padding:11px 12px;margin-bottom:8px;background:rgba(12,14,28,.82);'
        f'border:1px solid rgba(0,240,255,.16);border-left:3px solid {color}">'
        f'<div style="min-width:112px"><div style="color:#e6f1ff;font-weight:700;font-size:14px">{_e(th_date(e["date"]))}</div>'
        f'<div style="color:{"#ff2a6d" if hot else "#7d86a6"};font-size:12px;font-weight:{"700" if hot else "400"}">{"⏰ " if hot else ""}{when}</div></div>'
        f'<div style="flex:1;min-width:0"><div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">'
        f'<span style="font-family:monospace;font-weight:700;color:#fcee0a;font-size:15px">{_e(e["sym"])}</span>'
        f'<span style="color:{color};font-size:12px;border:1px solid {color};padding:1px 7px">{_e(label)}</span>'
        f'<span style="color:#7d86a6;font-size:12px">{_e(e["name"] if e["kind"] != "fomc" else "")}</span></div>'
        f'<div style="color:#9aa4c4;font-size:12px;margin-top:3px">{_e(note)}</div></div></div>'
    )


def render_calendar():
    st.caption("รวมวันประกาศงบ · วัน XD/จ่ายปันผล · วันประชุมเฟด ของหุ้นที่คุณติดตาม เรียงตามวันที่ใกล้สุดก่อน")
    src = st.radio("แหล่งหุ้น", ["🌐 ค้นหาให้อัตโนมัติ (หุ้นที่จะประกาศงบเร็วๆ นี้ ทั้งตลาด)", "⭐ เฉพาะหุ้นที่ฉันติดตาม"],
                   horizontal=True, key="cal_src")
    auto = src.startswith("🌐")
    if "cal_text" not in st.session_state:
        try:
            st.session_state["cal_text"] = ", ".join(home_ui._watchlist())
        except Exception:
            st.session_state["cal_text"] = "NVDA, AAPL, MSFT, TSLA"
    if auto:
        txt = st.session_state["cal_text"]
        cap_pick = st.radio("ขนาดบริษัท", ["ใหญ่มาก (≥ $100B)", "ใหญ่ (≥ $10B)", "กลางขึ้นไป (≥ $2B)"],
                            horizontal=True, key="cal_cap", index=1)
        min_cap = {"ใหญ่มาก (≥ $100B)": 100e9, "ใหญ่ (≥ $10B)": 10e9, "กลางขึ้นไป (≥ $2B)": 2e9}[cap_pick]
    else:
        txt = st.text_area("หุ้นที่ติดตาม (คั่นด้วยจุลภาค สูงสุด 25 ตัว) — แก้แล้วกด Ctrl+Enter หรือคลิกที่อื่น", key="cal_text", height=70)
        min_cap = 0
    kind_pick = st.radio("ประเภทเหตุการณ์", ["ทั้งหมด", "📊 ประกาศงบ", "💰 ปันผล", "🏦 ประชุมเฟด"],
                         horizontal=True, key="cal_kind")
    c2, c3 = st.columns([1.4, 1], vertical_alignment="bottom")
    horizon = c2.selectbox("ช่วงเวลา", [14, 30, 60, 90], index=1, format_func=lambda d: f"ใน {d} วันข้างหน้า")
    if c3.button("🔄 รีเฟรชข้อมูลล่าสุด", use_container_width=True):
        _fetch.clear()
        _nasdaq_day.clear()

    syms = []
    for t in txt.replace("\n", ",").split(","):
        t = t.strip().upper()
        if t and t not in syms:
            syms.append(t)
    syms = syms[:25]
    kinds = {"ทั้งหมด": {"earn", "exdiv", "paydiv", "fomc"}, "📊 ประกาศงบ": {"earn"},
             "💰 ปันผล": {"exdiv", "paydiv"}, "🏦 ประชุมเฟด": {"fomc"}}[kind_pick]

    with st.spinner("กำลังรวบรวมเหตุการณ์..."):
        if auto:
            # โหมดอัตโนมัติ: งบทั้งตลาดจาก Nasdaq (+ ประชุมเฟด) — ปันผลต้องใช้โหมด "หุ้นที่ฉันติดตาม"
            events = build_events((), kinds & {"fomc"}, int(horizon))
            if "earn" in kinds:
                horizon_cap = min(int(horizon), 30)  # ดึงทีละวัน จำกัด 30 วันเพื่อไม่ให้ช้า
                events += auto_earnings(horizon_cap, min_cap)
                events.sort(key=lambda e: (e["date"], -e.get("cap", 0), e["kind"], e["sym"]))
                if int(horizon) > 30:
                    st.caption("โหมดค้นหาอัตโนมัติดูงบล่วงหน้าได้สูงสุด 30 วัน (ประชุมเฟดยังแสดงตามช่วงที่เลือก)")
            if kinds & {"exdiv", "paydiv"} and not kinds & {"earn", "fomc"}:
                st.info("ปันผลดูได้เฉพาะโหมด ⭐ เฉพาะหุ้นที่ฉันติดตาม (ต้องรู้ชื่อหุ้นก่อน)")
        else:
            events = build_events(tuple(syms), kinds, int(horizon))
    today = date.today()
    if auto and "earn" in kinds and not any(e["kind"] == "earn" for e in events):
        st.warning("ดึงปฏิทินงบทั้งตลาดไม่สำเร็จหรือไม่มีบริษัทในเกณฑ์นี้ ลองเลือกขนาดบริษัทเล็กลง กด 🔄 รีเฟรช "
                   "หรือสลับไปโหมด ⭐ เฉพาะหุ้นที่ฉันติดตามครับ")
    if not events:
        st.info("ไม่พบเหตุการณ์ในช่วงนี้ ลองขยายช่วงเวลา หรือเพิ่มประเภทเหตุการณ์ครับ")
        return

    soon = [e for e in events if (e["date"] - today).days <= 7]
    m1, m2, m3 = st.columns(3)
    m1.metric("เหตุการณ์ทั้งหมด", len(events))
    m2.metric("ภายใน 7 วัน", len(soon))
    nxt = events[0]
    m3.metric("ใกล้ที่สุด", f'{nxt["sym"]} · {nxt["date"].day} {_TH_M[nxt["date"].month - 1]}')

    last = None
    for e in events:
        key = (e["date"].year, e["date"].month)
        if key != last:
            st.markdown(f'<div class="section-label">{_TH_M[e["date"].month - 1]} {e["date"].year + 543}</div>', unsafe_allow_html=True)
            last = key
        st.markdown(_card(e, today), unsafe_allow_html=True)

    st.caption("⚠️ วันประกาศงบ/ปันผลเป็นข้อมูลจากแหล่งสาธารณะ (Nasdaq/Yahoo Finance) (บางหุ้นไม่มี และอาจเลื่อน) ควรเช็กกับประกาศบริษัท · "
               "วันประชุมเฟดอ้างอิงตารางที่ Federal Reserve ประกาศ (ปี 2027 เป็นแบบเบื้องต้น) ตรวจได้ที่ federalreserve.gov · ไม่ใช่คำแนะนำซื้อ-ขาย")
