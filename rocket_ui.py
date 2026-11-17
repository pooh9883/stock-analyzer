# -*- coding: utf-8 -*-
"""
rocket_ui.py
============
หน้าจอ Watchlist Scanner — ใส่รายชื่อหุ้นเอง กรองด้วย RSI + แนวรับ/แนวต้าน + โมเมนตัม + R:R
เรียกใช้จาก app.py:  rocket_ui.render_scanner(refresh_interval)
"""

import json
import math
import re
from pathlib import Path

import pandas as pd
import streamlit as st

import rocket

GOLD, GREEN, RED, TEXT, GREY = "#fcee0a", "#19f5a5", "#ff2a6d", "#e6f1ff", "#7d86a6"
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
_TH_MON = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]


def _level_chart_svg(hist: pd.Series, price: float, sups: list, ress: list) -> str:
    """กราฟราคา + แนวรับ/แนวต้านใกล้สุด วาดเป็น SVG เอง: แกนราคาไม่เริ่มที่ 0 (เห็นการขยับชัด) · ป้ายราคาอยู่ขวามือ ไม่ซ้อนกัน"""
    W, H, L, R, T, B = 1000, 340, 10, 150, 14, 28
    vals = [float(v) for v in hist.values]
    lv = [("s", float(x["price"])) for x in sups] + [("r", float(x["price"])) for x in ress]
    lo = min(vals + [p for _, p in lv] + [price])
    hi = max(vals + [p for _, p in lv] + [price])
    pad = (hi - lo) * 0.07 or hi * 0.02
    lo, hi = lo - pad, hi + pad
    iw, ih = W - L - R, H - T - B

    nx = len(vals)          # จุดที่ nx = ราคาล่าสุดตอนนี้ (ต่อจากราคาปิดรายวันตัวสุดท้าย)

    def X(i):
        return L + iw * i / max(nx, 1)

    def Y(v):
        return T + ih * (1 - (v - lo) / (hi - lo))

    o = ['<svg viewBox="0 0 %d %d" style="width:100%%;height:auto;display:block;font-family:inherit" xmlns="http://www.w3.org/2000/svg">' % (W, H)]
    o.append('<defs><linearGradient id="rkg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00f0ff" stop-opacity=".22"/>'
             '<stop offset="1" stop-color="#00f0ff" stop-opacity="0"/></linearGradient></defs>')
    # ตัวเลขแกนราคาใช้เลขกลมๆ (เช่น 280, 300, 320) อ่านง่าย ไม่ชนกับตัวเลขแนวรับ/แนวต้านที่เป็นทศนิยม
    rough = (hi - lo) / 4.0
    mag = 10 ** math.floor(math.log10(rough)) if rough > 0 else 1
    step = mag
    for m in (1, 2, 2.5, 5, 10):
        step = m * mag
        if step >= rough:
            break
    v = math.ceil(lo / step) * step
    while v <= hi:
        y = Y(v)
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#1b2033" stroke-width="1"/>' % (L, y, W - R, y))
        o.append('<text x="%d" y="%.1f" fill="#6f7898" font-size="12" text-anchor="start">%s</text>'
                 % (L + 4, y - 4, format(v, ",.0f") if step >= 1 else format(v, ",.2f")))
        v += step
    # แกนเวลา
    idx = list(hist.index)
    for k in range(6):
        i = int(round(nx * k / 5))
        try:
            lab = "ล่าสุด" if i >= nx else "%d %s" % (idx[i].day, _TH_MON[idx[i].month - 1])
        except Exception:
            lab = ""
        anc = "start" if k == 0 else ("end" if k == 5 else "middle")
        o.append('<text x="%.1f" y="%d" fill="#6f7898" font-size="12" text-anchor="%s">%s</text>' % (X(i), H - 8, anc, lab))
    # พื้นที่ใต้เส้นราคา + เส้นราคา
    pts = " ".join("%.1f,%.1f" % (X(i), Y(v)) for i, v in enumerate(vals))
    o.append('<polygon points="%.1f,%.1f %s %.1f,%.1f" fill="url(#rkg)"/>' % (X(0), T + ih, pts, X(nx - 1), T + ih))
    # เส้นแนวรับ/แนวต้าน (ตัวใกล้สุดเข้มกว่า)
    labels = []
    cnt = {"s": 0, "r": 0}
    for kind, p in lv:
        col = "#19f5a5" if kind == "s" else "#ff4d8d"
        near = cnt[kind] == 0
        cnt[kind] += 1
        y = Y(p)
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="%s" stroke-dasharray="7 5" opacity="%s"/>'
                 % (L, y, W - R, y, col, "1.8" if near else "1.1", "1" if near else ".55"))
        labels.append([y, ("แนวรับ " if kind == "s" else "แนวต้าน ") + format(p, ",.2f"), col, near, y])
    o.append('<polyline points="%s" fill="none" stroke="#e6f1ff" stroke-width="2" stroke-linejoin="round"/>' % pts)
    # ช่วงสุดท้าย: จากราคาปิดรายวันล่าสุด → ราคาตอนนี้ (เส้นประสีฟ้า เพราะมาจากข้อมูลรายชั่วโมง คนละชุดกับรายวัน)
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#00f0ff" stroke-width="2" stroke-dasharray="3 3"/>'
             % (X(nx - 1), Y(vals[-1]), X(nx), Y(price)))
    # จุด + ป้ายราคาตอนนี้
    yc = Y(price)
    o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#00f0ff" stroke="#05060d" stroke-width="2"/>' % (X(nx), yc))
    labels.append([yc, "ตอนนี้ " + format(price, ",.2f"), "#00f0ff", True, yc])
    # ป้ายด้านขวา: ไล่ดันไม่ให้ซ้อนกัน
    labels.sort(key=lambda t: t[0])
    gap = 22
    for i in range(1, len(labels)):
        if labels[i][0] - labels[i - 1][0] < gap:
            labels[i][0] = labels[i - 1][0] + gap
    over = labels[-1][0] - (H - B - 4)
    if over > 0:
        for t in labels:
            t[0] -= over
    for y, txt, col, strong, y0 in labels:
        if abs(y - y0) > 1.5:      # ป้ายถูกดันหนีจากเส้นจริง → ลากเส้นเชื่อมสั้นๆ ให้รู้ว่าป้ายนี้ของเส้นไหน
            o.append('<polyline points="%d,%.1f %d,%.1f %d,%.1f" fill="none" stroke="%s" stroke-opacity=".8" stroke-width="1.2"/>'
                     % (W - R, y0, W - R + 3, y0, W - R + 6, y, col))
        o.append('<rect x="%d" y="%.1f" width="%d" height="18" fill="%s" fill-opacity="%s" stroke="%s" stroke-opacity=".7"/>'
                 % (W - R + 6, y - 9, R - 58 + 6, col, ".16" if strong else ".07", col))
        o.append('<text x="%d" y="%.1f" fill="%s" font-size="12.5" font-weight="%s">%s</text>'
                 % (W - R + 12, y + 4.5, col, "700" if strong else "400", txt))
    o.append("</svg>")
    leg = ('<div style="display:flex;gap:18px;flex-wrap:wrap;font-size:12.5px;color:#9aa4c4;margin:4px 0 10px">'
           '<span><b style="color:#e6f1ff">━</b> ราคา</span>'
           '<span><b style="color:#19f5a5">┅</b> แนวรับ (ราคาเคยลงมาแล้วเด้งขึ้น)</span>'
           '<span><b style="color:#ff4d8d">┅</b> แนวต้าน (ราคาเคยขึ้นไปแล้วโดนดันกลับ)</span>'
           '<span><b style="color:#00f0ff">●</b> ราคาตอนนี้ (เส้นประฟ้า = ต่อจากราคาปิดรายวันล่าสุด)</span>'
           '<span style="color:#6f7898">เส้นเข้ม = ใกล้ราคาที่สุด · แกนราคาไม่เริ่มที่ 0 เพื่อให้เห็นการขยับชัด</span></div>')
    return "".join(o) + leg


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


_HUD_CSS = """<style>
.rk-hud{border:1px solid rgba(0,240,255,.3);border-left:4px solid #00f0ff;background:rgba(10,12,22,.78);padding:9px 13px;margin:6px 0 10px;
 clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}
.rk-top{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:13px;letter-spacing:1.5px;color:#5ee7ff!important;-webkit-text-fill-color:#5ee7ff}
.rk-top i{display:inline-block;width:8px;height:13px;background:#00f0ff;vertical-align:-2px;margin-left:5px;animation:rkb 1.1s steps(2) infinite}
@keyframes rkb{50%{opacity:0}}
.rk-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.rk-chip{--c:#00f0ff;border:1px solid var(--c);background:rgba(255,255,255,.04);padding:3px 11px;min-width:92px}
.rk-chip small{display:block;font-family:'Share Tech Mono',ui-monospace,monospace;font-size:10.5px;letter-spacing:2px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6}
.rk-chip b{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:20px;color:var(--c)!important;-webkit-text-fill-color:var(--c);text-shadow:0 0 9px var(--c);font-weight:400}
.rk-note{font-size:12.5px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4;margin-top:7px;line-height:1.55}
@media (prefers-reduced-motion:reduce){.rk-top i{animation:none}}
</style>"""


def _hud(title, chips, note=""):
    """แถบสถานะสไตล์ HUD: หัวข้อ + ชิปตัวเลข [(ป้าย, ค่า, สี)] + หมายเหตุภาษาไทย"""
    cs = "".join("<div class='rk-chip' style='--c:%s'><small>%s</small><b>%s</b></div>" % (c, lb, v) for lb, v, c in chips)
    return (_HUD_CSS + "<div class='rk-hud'><div class='rk-top'>&gt; " + title + "<i></i></div><div class='rk-chips'>" + cs + "</div>"
            + ("<div class='rk-note'>" + note + "</div>" if note else "") + "</div>")


UNI_TOP = 40          # โหมดสแกนทั้งกลุ่ม: ดึงรายชั่วโมงละเอียดเฉพาะตัวที่ผ่านคัดรอบแรกสูงสุดกี่ตัว
_CHUNK = 100


@st.cache_data(ttl=900, show_spinner=False)
def _daily_big(symbols_tuple):
    """ดึงรายวันของหุ้นทั้งกลุ่มทีละ 100 ตัว (กันคำขอใหญ่เกินจนล้มทั้งชุด) · ชุดไหนล้มก็ข้ามชุดนั้น"""
    syms = list(dict.fromkeys(symbols_tuple))
    out = {}
    for i in range(0, len(syms), _CHUNK):
        try:
            out.update(rocket.load_daily(tuple(syms[i:i + _CHUNK])))
        except Exception:
            continue
    return out


def _passes(r, params):
    pred, _ = PRESETS[params["preset"]]
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


def _sort_rows(shown, params):
    _, preset_sort = PRESETS[params["preset"]]
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
    return shown


@st.cache_data(ttl=900, show_spinner=False)
def _stage1(symbols_tuple, params_items):
    """รอบแรก: คัดจากข้อมูลรายวันทั้งกลุ่ม (ยังไม่มี RSI รายชั่วโมง) เหลือตัวที่น่าดูสูงสุด UNI_TOP ตัว
    คืน (รายชื่อที่ผ่านคัด, จำนวนที่สแกนได้, จำนวนที่ผ่านเงื่อนไขรอบแรก, ตัวที่ดึงข้อมูลไม่ได้)"""
    params = dict(params_items)
    params["rsi_h"] = (0, 100)          # รอบแรกยังไม่มี RSI รายชั่วโมง → ไม่กรองด้วยตัวนี้
    daily = _daily_big(tuple(list(symbols_tuple) + ["SPY"]))
    rows, _ = rocket.build_rows(list(symbols_tuple), daily, {})
    shown = _sort_rows([r for r in rows if _passes(r, params)], params)
    miss = [s for s in symbols_tuple if s not in daily]
    return [r["symbol"] for r in shown[:UNI_TOP]], len(rows), len(shown), miss


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
def _render_results(symbols: tuple, params: dict, universe: bool = False):
    uni_info = None
    if universe:
        with st.spinner("กำลังแจ็คอินข้อมูลทั้งกลุ่ม ... (รอบแรกอาจใช้เวลา 1–2 นาที หลังจากนี้เก็บไว้ 15 นาที)"):
            short, n_scan, n_pass, miss0 = _stage1(tuple(symbols), tuple(sorted(
                (k, v) for k, v in params.items())))
        uni_info = (len(symbols), n_scan, n_pass, len(short))
        if not short:
            st.warning("ไม่มีหุ้นในกลุ่มที่ผ่านเงื่อนไขรอบแรกตอนนี้ ลองผ่อนตัวกรอง หรือเลือกพรีเซ็ต 📋 ทั้งหมด"
                       + (f" · ดึงข้อมูลไม่ได้ {len(miss0)} ตัว" if miss0 else ""))
            return
        symbols = tuple(short)

    syms_all = tuple(list(symbols) + ["SPY"])
    with st.spinner(f"กำลังคำนวณ {len(symbols)} ตัว..."):
        daily = _daily_big(syms_all) if universe else _daily_cached(syms_all)
        hourly = _hourly_cached(syms_all)
        rows, spy_chg = rocket.build_rows(list(symbols), daily, hourly)

    missing = [s for s in symbols if s not in daily]
    if uni_info:
        st.markdown(_hud("SCAN.RESULT // S&amp;P 500 + NASDAQ 100", [
            ("NODES", uni_info[0], "#00f0ff"), ("DATA OK", uni_info[1], "#19f5a5"),
            ("PASS 1", uni_info[2], "#fcee0a"), ("DEEP SCAN", uni_info[3], "#ff2a6d")],
            "สแกน %d ตัว (ข้อมูลครบ %d) → ผ่านคัดรอบแรก %d ตัว → ดูละเอียด (RSI รายชั่วโมง) %d ตัวที่น่าสนใจที่สุดตามการเรียงที่เลือก" % uni_info),
            unsafe_allow_html=True)
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

    shown = _sort_rows([r for r in rows if _passes(r, params)], params)

    st.markdown('<div class="section-label">ผลสแกน · ผ่านเงื่อนไข %d จาก %d ตัว</div>' % (len(shown), len(rows)), unsafe_allow_html=True)
    if missing:
        st.caption("ดึงข้อมูลไม่ได้: " + ", ".join(missing))
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

    if "rk_view" not in st.session_state:
        st.session_state["rk_view"] = "ง่าย (แนะนำ)"
    st.session_state["rk_view"] = st.session_state["rk_view"]
    view = st.radio("มุมมองตาราง", ["ง่าย (แนะนำ)", "ละเอียดทุกคอลัมน์"], horizontal=True, key="rk_view")

    if view.startswith("ง่าย"):
        def _rsi_txt(v):
            v = round(v)
            return f"{v} 🟢 ขายมากไป" if v <= 30 else (f"{v} 🔴 ซื้อมากไป" if v >= 70 else f"{v}")

        def _lvl(lv, dist, word):
            if not lv:
                return "—"
            return f"{lv['price']:,.2f}  ({word} {abs(dist):.1f}%)" if dist is not None else f"{lv['price']:,.2f}"

        def _rr(v):
            if v is None:
                return "—"
            return f"{v:.1f} " + ("✅ คุ้ม" if v >= 2 else ("➖ พอได้" if v >= 1 else "⚠️ ไม่คุ้ม"))

        simple = pd.DataFrame([{
            "หุ้น": r["symbol"],
            "ราคา": f"{r['price']:,.2f}",
            "วันนี้": ("🟢 +" if r["chg"] >= 0 else "🔴 ") + f"{r['chg']:.2f}%",
            "RSI (ร้อนแรงไหม)": _rsi_txt(r["rsi_d"]),
            "แนวรับใกล้สุด (ราคาตกมาเจอ)": _lvl(r["sup"], r["dist_sup"], "ต่ำกว่า"),
            "แนวต้านใกล้สุด (ราคาขึ้นไปเจอ)": _lvl(r["res"], r["dist_res"], "สูงกว่า"),
            "คุ้มเสี่ยงไหม (R:R)": _rr(r["rr"]),
            "จังหวะเด้ง": r["rebound"],
            "จังหวะทะลุ": r["breakout"],
            "สัญญาณ": " · ".join(r["flags"]),
        } for r in shown])
        _show_df(
            simple, hide_index=True,
            column_config={
                "จังหวะเด้ง": st.column_config.ProgressColumn("จังหวะเด้ง", min_value=0, max_value=100, format="%d",
                                                              help="ยิ่งสูง = ใกล้แนวรับ + RSI ต่ำ + คุ้มเสี่ยง (กฎหัวแม่มือ)"),
                "จังหวะทะลุ": st.column_config.ProgressColumn("จังหวะทะลุ", min_value=0, max_value=100, format="%d",
                                                              help="ยิ่งสูง = ใกล้/ทะลุแนวต้าน + โมเมนตัมดี (กฎหัวแม่มือ)"),
            },
        )
        st.caption("RSI ≤30 = ขายหนักเกินไปอาจเด้ง · ≥70 = ซื้อหนักเกินไปอาจพัก · R:R = กำไรที่หวัง ÷ ความเสี่ยง (ตั้งแต่ 2 ขึ้นไปคือคุ้ม) · อยากเห็นตัวเลขครบให้เลือกมุมมองละเอียด")
    else:
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
    # แสดงเฉพาะแนวรับ/แนวต้านที่ใกล้ราคาที่สุดด้านละ 2 เส้น (ตัวที่เหลือดูในตารางด้านล่าง) เพื่อให้กราฟไม่รก
    st.markdown(_level_chart_svg(hist, price, sups[:2], ress[:2]), unsafe_allow_html=True)

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

    src = st.radio("สแกนจาก", ["🌐 S&P 500 + Nasdaq 100 (ราว 520 ตัว)", "⭐ Watchlist ของฉัน"],
                   horizontal=True, key="rk_src")
    universe = src.startswith("🌐")
    if universe:
        import screener
        symbols = [s for s in screener.universe("both") if s != "SPY"]
        st.markdown(_hud("SCAN.TARGET // S&amp;P 500 + NASDAQ 100", [("NODES", len(symbols), "#00f0ff"), ("DEEP SCAN", UNI_TOP, "#ff2a6d")],
                         "หุ้นใหญ่ซื้อขายคล่องของสหรัฐ %d ตัว · คัดรอบแรกจากราคารายวัน แล้วดูรายชั่วโมงละเอียดเฉพาะ %d ตัวที่น่าสนใจที่สุด · "
                         "รอบแรกอาจช้า 1–2 นาที ข้อมูล Yahoo ฟรีอาจดีเลย์" % (len(symbols), UNI_TOP)), unsafe_allow_html=True)
    else:
        import watchlist
        st.markdown('<div class="section-label">⭐ หุ้นที่สแกน · Watchlist กลาง</div>', unsafe_allow_html=True)
        symbols = watchlist.get()
        symbols = symbols[:MAX_SYMBOLS]
        st.markdown(watchlist.chips(symbols), unsafe_allow_html=True)
        st.caption(f"{len(symbols)} ตัว (สูงสุด {MAX_SYMBOLS}) · รายชื่อนี้ใช้ร่วมกับหน้าปฏิทิน เทียบหุ้น เรดาร์ข่าวด้วย")
        watchlist.editor()
        symbols = watchlist.get()[:MAX_SYMBOLS]

    if not symbols:
        st.info("เปิดกล่อง ✏️ แก้ไขรายชื่อหุ้น ด้านบนแล้วใส่รหัสหุ้นอย่างน้อย 1 ตัวครับ")
        return

    st.markdown('<div class="section-label">🎯 ตัวกรอง</div>', unsafe_allow_html=True)
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
    st.fragment(_render_results, run_every=refresh_interval)(tuple(symbols), params, universe)