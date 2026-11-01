# -*- coding: utf-8 -*-
"""
compare_ui.py  [compare v1]
===========================
เทียบหุ้น 2–3 ตัวข้างกัน: ภาพรวมราคา · คะแนน 10 มิติ (ตารางสีไล่ระดับ) · แนวรับ/แนวต้านใกล้สุด · ข่าวล่าสุดแปลไทย
ใช้ข้อมูลชุดเดียวกับหน้าอื่นทั้งหมด (scoring / chart_pro / rocket / news_feed) ไม่มีสูตรใหม่
⚠️ เป็นการ "วางข้อมูลเทียบกัน" ไม่ใช่คำแนะนำซื้อ-ขาย
"""
import html

import pandas as pd
import streamlit as st

import chart_pro
import news_feed
import rocket
import scoring

GREEN, RED, YELLOW, CYAN, MUTED, TEXT = "#19f5a5", "#ff2a6d", "#fcee0a", "#5ee7ff", "#7d86a6", "#e6f1ff"


def _e(x):
    return html.escape(str(x if x is not None else ""), quote=True)


def _heat(score: float) -> str:
    """สีไล่ตามคะแนน 0-100: แดง → เหลือง → เขียว"""
    import colorsys
    r, g, b = colorsys.hls_to_rgb(max(0, min(100, score)) * 1.2 / 360, 0.56, 0.9)
    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))


@st.cache_data(ttl=600, show_spinner=False)
def _bundle(sym: str) -> dict:
    """รวมข้อมูลหุ้น 1 ตัว (cache 10 นาที) — ถ้าพลาดคืน {"error": ...}"""
    a = scoring.full_analysis(sym)
    if "error" in a:
        return {"error": a["error"]}
    info = a["info"]
    out = {"sym": sym, "a": a, "name": info.get("shortName") or sym}
    daily = chart_pro._load_daily(sym)
    price, chg, rsi_v, vs200 = None, None, None, None
    levels = []
    if daily is not None and not daily.empty and len(daily) >= 60:
        close = daily["Close"].astype(float)
        price = float(close.iloc[-1])
        chg = (price / float(close.iloc[-2]) - 1) * 100
        try:
            rsi_v = float(rocket.rsi(close).iloc[-1])
        except Exception:
            pass
        if len(close) >= 200:
            vs200 = (price / float(close.rolling(200).mean().iloc[-1]) - 1) * 100
        try:
            levels = chart_pro.pick_levels(daily, price)
        except Exception:
            levels = []
    if price is None:
        p = info.get("currentPrice", info.get("regularMarketPrice"))
        price = float(p) if isinstance(p, (int, float)) else None
    out.update({"price": price, "chg": chg, "rsi": rsi_v, "vs200": vs200, "levels": levels})
    return out


def _num(v, fmt="{:,.2f}", pre="", suf=""):
    return pre + fmt.format(v) + suf if isinstance(v, (int, float)) else "—"


def _near_levels(price, levels):
    sup = sorted([z for z in levels if z["kind"] == "support" and z["price"] < price], key=lambda z: -z["price"])
    res = sorted([z for z in levels if z["kind"] == "resistance" and z["price"] > price], key=lambda z: z["price"])
    return (sup[0] if sup else None), (res[0] if res else None)


def _card(b):
    a, info = b["a"], b["a"]["info"]
    score = a["overall_score"]
    col = _heat(score)
    chg = b["chg"]
    chg_html = (f'<span style="color:{GREEN if chg >= 0 else RED};font-weight:700">{"↗" if chg >= 0 else "↘"} {abs(chg):.2f}%</span>'
                if chg is not None else "")
    target = info.get("targetMeanPrice")
    upside = (target / b["price"] - 1) * 100 if isinstance(target, (int, float)) and b["price"] else None
    rows = [
        ("P/E (ย้อนหลัง)", _num(info.get("trailingPE"), "{:.1f}")),
        ("P/E (คาดการณ์)", _num(info.get("forwardPE"), "{:.1f}")),
        ("เป้านักวิเคราะห์", _num(target, pre="$") + (f" ({upside:+.0f}%)" if upside is not None else "")),
        ("RSI 14 วัน", _num(b["rsi"], "{:.0f}")),
        ("เทียบเฉลี่ย 200 วัน", _num(b["vs200"], "{:+.1f}", suf="%")),
    ]
    trs = "".join(f'<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(125,134,166,.14);'
                  f'font-size:13px"><span style="color:{MUTED}">{_e(k)}</span><span style="color:{TEXT};font-weight:600">{_e(v)}</span></div>'
                  for k, v in rows)
    return (
        f'<div style="background:rgba(12,14,28,.85);border:1px solid rgba(0,240,255,.2);border-top:3px solid {col};padding:14px 16px;">'
        f'<div style="display:flex;align-items:baseline;gap:8px"><span style="font-family:monospace;font-weight:700;color:{YELLOW};font-size:20px">{_e(b["sym"])}</span>'
        f'<span style="color:{MUTED};font-size:12px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{_e(b["name"])}</span></div>'
        f'<div style="margin:6px 0 2px 0;font-size:26px;color:{TEXT};font-family:monospace">{_num(b["price"], pre="$")} {chg_html}</div>'
        f'<div style="font-size:12px;color:{MUTED}">คะแนนรวม 10 มิติ</div>'
        f'<div style="font-size:24px;font-weight:700;color:{col};font-family:monospace">{score:.1f}<span style="font-size:13px;color:{MUTED}"> /100</span></div>'
        f'<div style="font-size:12px;color:{col};margin-bottom:8px">{_e(a["overall_label"])}</div>{trs}</div>'
    )


def _dim_table(bs):
    names = scoring.DIMENSION_NAMES_TH
    head = "".join(f'<th style="padding:8px 10px;color:{YELLOW};font-family:monospace;text-align:center">{_e(b["sym"])}</th>' for b in bs)
    body = []
    wins = {b["sym"]: 0 for b in bs}
    for key, nm in names.items():
        vals = [b["a"]["dimensions"][key]["score"] for b in bs]
        best = max(vals)
        cells = []
        for b, v in zip(bs, vals):
            star = " ★" if v == best and vals.count(best) < len(vals) else ""
            if star:
                wins[b["sym"]] += 1
            c = _heat(v)
            cells.append(f'<td style="padding:6px 10px;text-align:center"><span style="display:inline-block;min-width:64px;padding:3px 8px;'
                         f'background:{c}22;border:1px solid {c};color:{c};font-weight:700;font-family:monospace">{v:.0f}{star}</span></td>')
        body.append(f'<tr style="border-bottom:1px solid rgba(125,134,166,.14)"><td style="padding:6px 10px;color:{TEXT};font-size:13px">{_e(nm)}</td>{"".join(cells)}</tr>')
    tbl = (f'<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;background:rgba(12,14,28,.7)">'
           f'<thead><tr style="border-bottom:1px solid rgba(0,240,255,.25)"><th style="padding:8px 10px;text-align:left;color:{MUTED};font-weight:500">มิติ</th>{head}</tr></thead>'
           f'<tbody>{"".join(body)}</tbody></table></div>')
    return tbl, wins


def _level_table(bs):
    rows = []
    for b in bs:
        if b["price"] is None:
            continue
        s, r = _near_levels(b["price"], b["levels"])

        def cell(z, color):
            if not z:
                return f'<span style="color:{MUTED}">—</span>'
            d = (z["price"] / b["price"] - 1) * 100
            return (f'<span style="color:{color};font-weight:700;font-family:monospace">${z["price"]:,.2f}</span> '
                    f'<span style="color:{MUTED};font-size:12px">({d:+.1f}%) · {_e(z["label"])}</span>')
        rows.append(f'<tr style="border-bottom:1px solid rgba(125,134,166,.14)"><td style="padding:8px 10px;color:{YELLOW};font-family:monospace;font-weight:700">{_e(b["sym"])}</td>'
                    f'<td style="padding:8px 10px">{cell(s, GREEN)}</td><td style="padding:8px 10px">{cell(r, RED)}</td></tr>')
    return (f'<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;background:rgba(12,14,28,.7)">'
            f'<thead><tr style="border-bottom:1px solid rgba(0,240,255,.25)"><th style="padding:8px 10px;text-align:left;color:{MUTED};font-weight:500">หุ้น</th>'
            f'<th style="padding:8px 10px;text-align:left;color:{GREEN};font-weight:600">แนวรับใกล้สุด</th>'
            f'<th style="padding:8px 10px;text-align:left;color:{RED};font-weight:600">แนวต้านใกล้สุด</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


def render_compare(ai_key: str = ""):
    st.caption("ใส่หุ้น 2–3 ตัว ระบบวางข้อมูลชุดเดียวกับหน้าอื่นเทียบกันข้างๆ (ไม่ใช่คำแนะนำซื้อ-ขาย)")
    if "cmp_tickers" not in st.session_state:
        try:
            import watchlist as _w
            _l = _w.get()[:3]
            st.session_state["cmp_tickers"] = ", ".join(_l) if len(_l) >= 2 else "NVDA, AMD, AVGO"
        except Exception:
            st.session_state["cmp_tickers"] = "NVDA, AMD, AVGO"
    with st.form("cmp_form", border=False):
        c1, c2 = st.columns([3, 1], vertical_alignment="bottom")
        raw = c1.text_input("รหัสหุ้น 2–3 ตัว (คั่นด้วยจุลภาค)", key="cmp_tickers")
        go = c2.form_submit_button("⚖️  เทียบเลย", use_container_width=True)

    syms = []
    for t in raw.replace("\n", ",").split(","):
        t = t.strip().upper()
        if t and t not in syms:
            syms.append(t)
    syms = syms[:3]

    if go:
        if len(syms) < 2:
            st.error("ใส่อย่างน้อย 2 ตัวครับ")
        else:
            with st.spinner(f"กำลังดึงและคำนวณ {', '.join(syms)} ..."):
                st.session_state["cmp_result"] = {"syms": syms, "b": [_bundle(s) for s in syms]}
    res = st.session_state.get("cmp_result")
    if not res:
        st.info("ใส่หุ้นแล้วกด ⚖️ เทียบเลย ได้เลยครับ")
        return

    bundles = res["b"]
    for b, s in zip(bundles, res["syms"]):
        if "error" in b:
            st.warning(f"{s}: {b['error']}")
    bs = [b for b in bundles if "error" not in b]
    if len(bs) < 2:
        st.error("ต้องมีข้อมูลอย่างน้อย 2 ตัวถึงจะเทียบได้ ลองตรวจรหัสหุ้นอีกครั้ง")
        return

    cols = st.columns(len(bs))
    for col, b in zip(cols, bs):
        col.markdown(_card(b), unsafe_allow_html=True)

    st.markdown('<div class="section-label">คะแนน 10 มิติ — ตัวเลขสูง = ดีกว่า (★ = สูงสุดในแถว)</div>', unsafe_allow_html=True)
    tbl, wins = _dim_table(bs)
    st.markdown(tbl, unsafe_allow_html=True)
    top = sorted(wins.items(), key=lambda kv: -kv[1])
    st.caption("จำนวนมิติที่ได้ ★ (นำหน้ากลุ่ม): " + " · ".join(f"{s} {n} มิติ" for s, n in top) +
               " — ดูเป็นภาพรวมเท่านั้น ราคาของหุ้นแต่ละตัวต่างกันที่ปัจจัยหลายอย่างนอกเหนือจากคะแนนนี้")

    st.markdown('<div class="section-label">แนวรับ / แนวต้านใกล้ราคาปัจจุบัน</div>', unsafe_allow_html=True)
    st.markdown(_level_table(bs), unsafe_allow_html=True)

    st.markdown('<div class="section-label">ข่าวล่าสุด (แปลเป็นไทย)</div>', unsafe_allow_html=True)
    try:
        feed = news_feed.build_feed(tuple(b["sym"] for b in bs), ai_key or "", 3)
        ncols = st.columns(len(bs))
        for col, b in zip(ncols, bs):
            items = [x for x in feed["feed"] if x["ticker"] == b["sym"]][:3]
            if not items:
                col.caption(f"{b['sym']}: ไม่พบข่าวช่วง 3 วันนี้")
                continue
            per = feed["per"].get(b["sym"], {})
            tone_col = {"บวก": "#19f5a5", "ลบ": "#ff2a6d", "กลาง": "#fcee0a"}
            overall = per.get("overall", "เป็นกลาง")
            oc = "#19f5a5" if overall == "เอียงบวก" else ("#ff2a6d" if overall == "เอียงลบ" else "#fcee0a")
            summ = ""
            if feed.get("ai") and per.get("overview"):
                summ = (f'<div style="background:rgba(0,240,255,.06);border-left:3px solid {oc};padding:8px 10px;margin:4px 0 6px;'
                        f'font-size:13.5px;line-height:1.55;color:{TEXT}">'
                        f'<b>สรุป:</b> {_e(per["overview"])}</div>')
            head = (f'<div style="display:flex;gap:8px;align-items:center;margin-bottom:2px">'
                    f'<span style="color:{YELLOW};font-family:monospace;font-weight:700">{_e(b["sym"])}</span>'
                    f'<span style="color:{oc};font-size:12px;border:1px solid {oc};padding:0 6px">ข่าว{_e(overall)} '
                    f'(+{per.get("pos", 0)} / -{per.get("neg", 0)})</span></div>')
            lis = ""
            for x in items:
                tc = tone_col.get(x.get("tone"), "#fcee0a")
                sm = (f'<div style="color:#b9c4e4;font-size:12.5px;line-height:1.5;margin-top:3px">{_e(x["sum"])}</div>'
                      if x.get("sum") else "")
                lis += (f'<div style="padding:8px 0 8px 9px;border-bottom:1px solid rgba(125,134,166,.14);border-left:3px solid {tc}">'
                        f'<a href="{_e(x["link"])}" target="_blank" rel="noopener" style="color:{TEXT};text-decoration:none;font-weight:600;font-size:14px;line-height:1.45">{_e(x["th"])}</a>'
                        f'{sm}'
                        f'<div style="color:{MUTED};font-size:12px;margin-top:2px">{_e(x["source"])} · {_e(news_feed.ago(x["ts"]) if x["ts"] else "")}</div></div>')
            col.markdown(head + summ + lis, unsafe_allow_html=True)
        if not feed.get("ai"):
            st.caption("💡 ตอนนี้เป็นการแปลหัวข้อข่าวอัตโนมัติ (ยังไม่มีสรุป) — ใส่คีย์ AI ในแถบข้างช่อง \"คีย์เสริมสำหรับสรุปผลด้วย AI\" "
                       "จะได้สรุปภาพรวมรายหุ้น + สรุปประเด็นทีละข่าวเป็นภาษาไทยแบบหน้าเรดาร์ข่าว")
    except Exception:
        st.caption("ดึงข่าวไม่สำเร็จตอนนี้ ลองกดเทียบใหม่อีกครั้ง")

    st.caption("⚠️ ข้อมูลจาก Yahoo Finance (ดีเลย์ราว 15 นาที) · คะแนน 10 มิติคำนวณจากสูตรเดียวกับหน้า Deep Scan · ไม่ใช่คำแนะนำซื้อ-ขาย")