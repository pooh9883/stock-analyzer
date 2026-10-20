# -*- coding: utf-8 -*-
"""
themes_ui.py
============
ไอเดียตามธีม: จัดหุ้นเป็นกลุ่มตามเรื่องที่ตลาดสนใจ ดูว่ากลุ่มไหนร้อน กลุ่มไหนใกล้แนวรับ
แล้วกดเข้าไปดูหุ้นแต่ละตัวพร้อม RSI แนวรับ/แนวต้าน โมเมนตัม

เรียกใช้จาก app.py:  themes_ui.render_themes()

⚠️ ธีมตั้งต้นผมรวบรวมจากความรู้ทั่วไป รายชื่ออาจไม่ตรงปัจจุบัน/ไม่ครบ แก้ไขได้เองในหน้านี้ (บันทึกที่ themes.json)
ไม่ใช่คำแนะนำซื้อ-ขาย
"""

import hashlib
import json
from pathlib import Path

import pandas as pd
import streamlit as st

import rocket
import rocket_ui

THEMES_FILE = Path(__file__).with_name("themes.json")
MAX_PER_THEME = 20

DEFAULT_THEMES = {
    "ชิป AI": {"desc": "ผู้ผลิตชิปและอุปกรณ์ที่อยู่เบื้องหลังการเติบโตของ AI", "symbols": ["NVDA", "AMD", "AVGO", "TSM", "MU", "ASML", "ARM", "MRVL", "INTC"]},
    "ซอฟต์แวร์ & คลาวด์": {"desc": "บริษัทซอฟต์แวร์และคลาวด์ที่ขายบริการรายเดือน", "symbols": ["MSFT", "ORCL", "CRM", "NOW", "SNOW", "ADBE", "PLTR", "DDOG", "CRWD"]},
    "ตัวใหญ่ Mega Cap": {"desc": "บริษัทมูลค่าตลาดใหญ่สุดที่ขยับดัชนี", "symbols": ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]},
    "นิวเคลียร์ & ไฟฟ้าป้อน AI": {"desc": "ผู้ผลิตไฟฟ้าและพลังงานที่รองรับดาต้าเซ็นเตอร์", "symbols": ["CEG", "VST", "GEV", "OKLO", "SMR", "NRG", "TLN", "BE"]},
    "ธนาคารใหญ่": {"desc": "ธนาคารและวาณิชธนกิจ ไวต่อดอกเบี้ยและเศรษฐกิจ", "symbols": ["JPM", "BAC", "WFC", "C", "GS", "MS", "USB", "PNC"]},
    "สุขภาพ & ยา": {"desc": "ยา เวชภัณฑ์ และประกันสุขภาพ ธุรกิจที่ค่อนข้างทนทานต่อเศรษฐกิจ", "symbols": ["LLY", "UNH", "JNJ", "ABBV", "MRK", "PFE", "TMO", "ISRG", "NVO"]},
    "พลังงาน": {"desc": "น้ำมันและก๊าซ ผันตามราคาน้ำมัน", "symbols": ["XOM", "CVX", "COP", "SLB", "EOG", "OXY", "MPC"]},
    "ป้องกันประเทศ & อวกาศ": {"desc": "อุตสาหกรรมกลาโหมและอวกาศ", "symbols": ["LMT", "RTX", "NOC", "GD", "BA", "RKLB", "LHX"]},
    "ค้าปลีก & ผู้บริโภค": {"desc": "ร้านค้าและแบรนด์ที่วัดกำลังซื้อของคนทั่วไป", "symbols": ["WMT", "COST", "HD", "TGT", "NKE", "MCD", "SBUX", "LOW"]},
    "คริปโต": {"desc": "บริษัทที่ผูกกับราคาคริปโต", "symbols": ["COIN", "MSTR", "MARA", "RIOT", "HOOD", "CLSK"]},
    "รถยนต์ไฟฟ้า": {"desc": "ผู้ผลิตรถยนต์ไฟฟ้าและค่ายรถเดิม", "symbols": ["TSLA", "RIVN", "LCID", "NIO", "XPEV", "F", "GM"]},
    "จ่ายปันผลสม่ำเสมอ": {"desc": "บริษัทใหญ่ที่จ่ายปันผลมานาน", "symbols": ["KO", "PEP", "PG", "JNJ", "MCD", "VZ", "T", "CVX"]},
    "ดอกเบี้ยลงได้อานิสงส์": {"desc": "บ้าน อสังหาริมทรัพย์ และกลุ่มที่ไวต่อดอกเบี้ยขาลง", "symbols": ["DHI", "LEN", "PHM", "O", "PLD", "AMT"]},
}


def _show_df(df, **kw):
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


def _load_themes() -> dict:
    try:
        data = json.loads(THEMES_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data:
            return data
    except Exception:
        pass
    return json.loads(json.dumps(DEFAULT_THEMES))


def _save_themes(themes: dict) -> bool:
    try:
        THEMES_FILE.write_text(json.dumps(themes, ensure_ascii=False, indent=1), encoding="utf-8")
        return True
    except Exception:
        return False


@st.cache_data(ttl=900, show_spinner=False)
def _daily(symbols_tuple):
    return rocket.load_daily(symbols_tuple)


def _theme_stats(themes: dict):
    all_syms = sorted({s for t in themes.values() for s in t["symbols"]})
    daily = _daily(tuple(all_syms + ["SPY"]))
    rows, _ = rocket.build_rows(all_syms, daily, {})
    by_sym = {r["symbol"]: r for r in rows}

    stats = {}
    for name, t in themes.items():
        members = []
        for s in t["symbols"]:
            r = by_sym.get(s)
            if not r:
                continue
            c = r["history"]["Close"].astype(float)
            m1 = float((c.iloc[-1] / c.iloc[-22] - 1) * 100) if len(c) > 22 else None
            members.append({"r": r, "m1": m1})
        if not members:
            continue
        m1s = [m["m1"] for m in members if m["m1"] is not None]
        stats[name] = {
            "desc": t.get("desc", ""), "n": len(members), "missing": len(t["symbols"]) - len(members),
            "m1": sum(m1s) / len(m1s) if m1s else None,
            "day": sum(m["r"]["chg"] for m in members) / len(members),
            "near": sum(1 for m in members if m["r"]["dist_sup"] is not None and m["r"]["dist_sup"] <= 2),
            "rsi": sum(m["r"]["rsi_d"] for m in members) / len(members),
            "members": members,
        }
    return stats


def _grad(name: str) -> str:
    h = int(hashlib.md5(name.encode()).hexdigest()[:4], 16) % 360
    return f"linear-gradient(135deg,hsl({h},55%,28%),hsl({(h+40)%360},60%,18%))"


def _html(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


def _render_editor(themes: dict):
    with st.expander("✏️ แก้ไข / เพิ่ม / ลบธีม", expanded=False):
        options = ["➕ ธีมใหม่"] + list(themes.keys())
        sel = st.selectbox("เลือกธีม", options, key="th_sel")
        cur = themes.get(sel, {"desc": "", "symbols": []})
        name = st.text_input("ชื่อธีม", value="" if sel == "➕ ธีมใหม่" else sel, key=f"th_name_{sel}")
        desc = st.text_input("คำอธิบายสั้น ๆ", value=cur.get("desc", ""), key=f"th_desc_{sel}")
        syms_text = st.text_area("รหัสหุ้น (คั่นด้วยคอมมา)", value=", ".join(cur.get("symbols", [])), key=f"th_syms_{sel}", height=70)
        c1, c2, c3 = st.columns([1, 1, 3])
        if c1.button("💾 บันทึกธีม", key="th_save"):
            syms = rocket_ui._parse(syms_text)[:MAX_PER_THEME]
            if not name.strip() or not syms:
                c3.warning("ต้องมีชื่อธีมและรหัสหุ้นอย่างน้อย 1 ตัว")
            else:
                new = dict(themes)
                if sel != "➕ ธีมใหม่" and sel != name.strip():
                    new.pop(sel, None)
                new[name.strip()] = {"desc": desc.strip(), "symbols": syms}
                c3.success("บันทึกแล้ว" if _save_themes(new) else "บันทึกไฟล์ไม่ได้ (ไม่มีสิทธิ์เขียนไฟล์)")
                st.cache_data.clear()
        if sel != "➕ ธีมใหม่" and c2.button("🗑️ ลบธีม", key="th_del"):
            new = {k: v for k, v in themes.items() if k != sel}
            if new:
                _save_themes(new)
                c3.success("ลบแล้ว (รีเฟรชหน้าเพื่อดูผล)")
            else:
                c3.warning("ต้องเหลืออย่างน้อย 1 ธีม")
        if st.button("↺ คืนค่าธีมตั้งต้นทั้งหมด", key="th_reset"):
            c3.success("คืนค่าแล้ว" if _save_themes(json.loads(json.dumps(DEFAULT_THEMES))) else "บันทึกไฟล์ไม่ได้")
        st.caption(f"ธีมตั้งต้นรวบรวมจากความรู้ทั่วไป รายชื่ออาจไม่ตรงปัจจุบัน ตรวจสอบและแก้ไขได้ · สูงสุด {MAX_PER_THEME} ตัวต่อธีม")


def render_themes():
    with st.expander("📖 หน้านี้ใช้ยังไง", expanded=False):
        st.markdown(
            """
**ไอเดียตามธีม** คือการจัดหุ้นเป็นกลุ่มตามเรื่องที่ตลาดสนใจ เพื่อให้เห็นภาพรวมก่อนเลือกตัว

**อ่านการ์ดแต่ละใบ**
- **ตัวเลขใหญ่ = ผลตอบแทนเฉลี่ย 1 เดือน** ของหุ้นในธีม (เขียว = กลุ่มขึ้น แดง = กลุ่มลง)
- **n ใกล้แนวรับ** = มีกี่ตัวที่ราคาอยู่ห่างแนวรับไม่เกิน 2% (กลุ่มที่ลงมาแล้วเริ่มใกล้จุดที่เคยมีแรงซื้อ)
- **RSI เฉลี่ย** ต่ำ ๆ แปลว่าทั้งกลุ่มขายหนัก · สูง ๆ แปลว่าร้อนแรง

**ใช้ยังไง:** เลือกธีมที่สนใจ → ดูตารางหุ้นข้างใน → ตัวที่ใกล้แนวรับ/RSI ต่ำ/โมเมนตัมสูงคือตัวที่น่าศึกษาต่อ

ธีมแก้ไขเองได้ทั้งหมดด้านล่าง ธีมตั้งต้นรวบรวมจากความรู้ทั่วไป อาจไม่ตรงปัจจุบัน · ไม่ใช่คำแนะนำซื้อ-ขาย
"""
        )

    themes = _load_themes()
    with st.spinner(f"กำลังคำนวณ {len(themes)} ธีม..."):
        try:
            stats = _theme_stats(themes)
        except Exception as e:
            st.error(f"คำนวณธีมไม่สำเร็จ: {e}")
            stats = {}
    if not stats:
        st.error("ดึงข้อมูลไม่สำเร็จ (ตรวจอินเทอร์เน็ต หรืออาจโดน rate-limit ชั่วคราว)")
        _render_editor(themes)
        return

    ordered = sorted(stats.items(), key=lambda kv: (kv[1]["m1"] is None, -(kv[1]["m1"] or 0)))
    st.markdown(f"**{len(ordered)} ธีม** เรียงจากผลตอบแทน 1 เดือนมากไปน้อย")
    for i in range(0, len(ordered), 2):
        cols = st.columns(2)
        for col, (name, s) in zip(cols, ordered[i:i + 2]):
            m1 = s["m1"]
            mcol = GREY if m1 is None else (GREEN if m1 >= 0 else RED)
            m1_txt = "—" if m1 is None else f"{m1:+.1f}%"
            col.markdown(_html(f"""
                <div style="background:{_grad(name)};border-radius:14px;padding:16px 18px;margin-bottom:10px;border:1px solid #ffffff22;">
                <div style="font-size:17px;font-weight:700;color:{TEXT};">{name}</div>
                <div style="color:#d6d2c6;font-size:12px;margin-top:2px;">{s['desc']}</div>
                <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:10px;">
                <div><div style="font-size:30px;font-weight:800;color:{mcol};line-height:1;">{m1_txt}</div>
                <div style="color:#d6d2c6;font-size:12px;">ผลตอบแทนเฉลี่ย 1 เดือน</div></div>
                <div style="text-align:right;color:{TEXT};font-size:13px;">{s['n']} ตัว<br>📍 {s['near']} ใกล้แนวรับ<br>RSI เฉลี่ย {s['rsi']:.0f}</div>
                </div></div>
            """), unsafe_allow_html=True)

    st.markdown("#### 🔎 ดูหุ้นในธีม")
    label = {name: f"{name} ({'—' if s['m1'] is None else format(s['m1'], '+.1f') + '%'})" for name, s in ordered}
    pick = st.selectbox("เลือกธีม", [n for n, _ in ordered], format_func=lambda n: label[n], key="th_pick")
    s = stats[pick]
    if s["missing"]:
        st.caption(f"ดึงข้อมูลไม่ได้ {s['missing']} ตัวในธีมนี้ (รหัสผิดหรือไม่มีข้อมูล)")
    df = pd.DataFrame([{
        "หุ้น": m["r"]["symbol"], "ราคา": round(m["r"]["price"], 2), "วันนี้ %": round(m["r"]["chg"], 2),
        "1 เดือน %": None if m["m1"] is None else round(m["m1"], 1),
        "RSI": round(m["r"]["rsi_d"]),
        "ห่างแนวรับ %": None if m["r"]["dist_sup"] is None else round(m["r"]["dist_sup"], 1),
        "ห่างแนวต้าน %": None if m["r"]["dist_res"] is None else round(m["r"]["dist_res"], 1),
        "โมเมนตัม": m["r"]["mom"], "สัญญาณ": " · ".join(m["r"]["flags"]),
    } for m in sorted(s["members"], key=lambda m: -(m["m1"] if m["m1"] is not None else -999))])
    _show_df(df, hide_index=True, column_config={
        "โมเมนตัม": st.column_config.ProgressColumn("โมเมนตัม", min_value=0, max_value=100, format="%d")})
    st.caption("ข้อมูลรายวันแคช 15 นาที · แนวรับ/แนวต้านเป็นโซนที่ราคาเคยมีปฏิกิริยา ไม่ใช่เส้นที่ราคาจะหยุดแน่นอน · ไม่ใช่คำแนะนำซื้อ-ขาย")

    _render_editor(themes)


GREEN, RED, TEXT, GREY = "#3ecf6e", "#e5534b", "#f4f0e6", "#9a9aa8"