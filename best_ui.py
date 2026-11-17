# -*- coding: utf-8 -*-
"""TOP PICKS · หุ้นที่ดีที่สุด — สรุปรวมหลายเลนส์ให้เหลือ 10 ตัวที่ผ่านเกณฑ์ดีที่สุด
ต่อยอดจากเครื่องมือเดิมใน screener.py (คุณภาพ · เติบโต · ราคา · แรงตลาด) ใช้แคชงบชุดเดียวกัน
ไม่ใช่สัญญาณซื้อ — เป็นรายชื่อ "น่าศึกษา" ตามเกณฑ์ที่เปิดเผยไว้ในหน้า"""
import datetime as _dt
import html as _h
import json
import os
import time
from pathlib import Path

import pandas as pd
import streamlit as st

import screener as S
import stage as STG

try:
    import yfinance as yf
except Exception:      # pragma: no cover
    yf = None

LOG = Path(__file__).with_name("best_picks_log.json")
TOPN = 10          # แสดงกี่ตัว
CAND = 80          # ดึงงบเฉพาะผู้เข้ารอบจากแรงตลาดสูงสุดกี่ตัว (ไม่ดึงทั้งตลาดให้ช้า)
_PILLARS = [("q_score", "คุณภาพ", "#00f0ff"), ("g_score", "เติบโต", "#19f5a5"),
            ("v_score", "ราคา", "#fcee0a"), ("m_score", "แรงตลาด", "#ff2a6d")]

_CSS = """<style>
.bp-hud{border:1px solid rgba(0,240,255,.3);border-left:4px solid #fcee0a;background:rgba(10,12,22,.78);padding:9px 13px;margin:4px 0 12px;
 clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}
.bp-top{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:13px;letter-spacing:1.5px;color:#5ee7ff!important;-webkit-text-fill-color:#5ee7ff}
.bp-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.bp-chip{--c:#00f0ff;border:1px solid var(--c);background:rgba(255,255,255,.04);padding:3px 11px;min-width:92px}
.bp-chip small{display:block;font-family:'Share Tech Mono',ui-monospace,monospace;font-size:10.5px;letter-spacing:2px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6}
.bp-chip b{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:20px;color:var(--c)!important;-webkit-text-fill-color:var(--c);text-shadow:0 0 9px var(--c);font-weight:400}
.bp-note{font-size:12.5px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4;margin-top:7px;line-height:1.55}
.bp-card{--c:#fcee0a;display:grid;grid-template-columns:62px 1fr 230px;gap:12px;align-items:center;border:1px solid rgba(255,255,255,.1);border-left:4px solid var(--c);
 background:linear-gradient(120deg,rgba(255,255,255,.05),rgba(10,12,22,.82) 55%);padding:10px 14px;margin:8px 0;
 clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px))}
.bp-rank{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:30px;color:var(--c)!important;-webkit-text-fill-color:var(--c);text-shadow:0 0 12px var(--c);text-align:center;line-height:1}
.bp-rank small{display:block;font-size:10px;letter-spacing:2px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6;text-shadow:none;margin-top:3px}
.bp-sym{font-size:20px;font-weight:700;color:#fff!important;-webkit-text-fill-color:#fff;letter-spacing:1px}
.bp-sym span{font-size:12.5px;font-weight:400;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4;margin-left:8px}
.bp-why{font-size:13px;color:#e6f1ff!important;-webkit-text-fill-color:#e6f1ff;margin-top:4px;line-height:1.6}
.bp-flag{font-size:12.5px;color:#ff9f43!important;-webkit-text-fill-color:#ff9f43;margin-top:2px}
.bp-plan{font-size:12.5px;color:#5ee7ff!important;-webkit-text-fill-color:#5ee7ff;margin-top:4px;line-height:1.55}
.bp-st{display:inline-block;--s:#19f5a5;border:1px solid var(--s);color:var(--s)!important;-webkit-text-fill-color:var(--s);padding:0 8px;margin-left:10px;
 font-family:'Share Tech Mono',ui-monospace,monospace;font-size:11.5px;font-weight:400;letter-spacing:1px;vertical-align:3px}
.bp-sum{--s:#19f5a5;font-size:13.5px;color:#fff!important;-webkit-text-fill-color:#fff;margin-top:6px;line-height:1.6;border-left:3px solid var(--s);padding-left:9px;background:linear-gradient(90deg,rgba(255,255,255,.05),transparent)}
.bp-sum b{color:var(--s)!important;-webkit-text-fill-color:var(--s)}
.bp-adv{font-size:12.5px;color:#c8d3f0!important;-webkit-text-fill-color:#c8d3f0;margin-top:4px;line-height:1.55;border-left:2px solid #3a4468;padding-left:8px}
.bp-bars{display:grid;gap:5px}
.bp-bar{display:grid;grid-template-columns:54px 1fr 28px;gap:6px;align-items:center;font-size:12px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4}
.bp-bar i{display:block;height:7px;background:rgba(255,255,255,.08)}
.bp-bar i u{display:block;height:7px;background:var(--c);box-shadow:0 0 8px var(--c);text-decoration:none}
.bp-bar b{font-family:'Share Tech Mono',ui-monospace,monospace;font-weight:400;text-align:right;color:var(--c)!important;-webkit-text-fill-color:var(--c)}
.bp-card{grid-template-columns:64px 1fr 215px;align-items:start;padding:15px 17px;margin:14px 0;gap:16px}
.bp-rank{align-self:center}
.bp-bars{align-self:start;margin-top:4px}
.bp-head{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 10px}
.bp-head .bp-sym{font-size:25px;line-height:1.1}
.bp-nm{font-size:13px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4}
.bp-head .bp-st{margin-left:2px}
.bp-pills{display:flex;flex-wrap:wrap;gap:6px;margin:9px 0 2px}
.bp-pill{font-size:12px;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.05);padding:1px 9px;color:#c8d3f0!important;-webkit-text-fill-color:#c8d3f0}
.bp-pill.hot{border-color:#ff9f43;color:#ff9f43!important;-webkit-text-fill-color:#ff9f43}
.bp-two{display:grid;grid-template-columns:1.3fr 1fr;gap:10px;margin-top:10px}
.bp-col{background:rgba(0,0,0,.30);border:1px solid rgba(255,255,255,.07);border-top:2px solid #19f5a5;padding:9px 12px}
.bp-col.warn{border-top-color:#ff9f43}
.bp-ct{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:12px;letter-spacing:1.5px;margin-bottom:5px;color:#19f5a5!important;-webkit-text-fill-color:#19f5a5}
.bp-col.warn .bp-ct{color:#ff9f43!important;-webkit-text-fill-color:#ff9f43}
.bp-li{font-size:13.5px;line-height:1.65;color:#e6f1ff!important;-webkit-text-fill-color:#e6f1ff;padding-left:15px;position:relative;margin:2px 0}
.bp-li:before{content:'▸';position:absolute;left:0;color:#19f5a5}
.bp-col.warn .bp-li:before{color:#ff9f43}
.bp-hl{font-size:12px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4;margin-top:9px;line-height:1.55;border-top:1px dashed rgba(255,255,255,.12);padding-top:7px}
.bp-h{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:14px;letter-spacing:1.5px;color:#5ee7ff!important;-webkit-text-fill-color:#5ee7ff;border-left:3px solid #fcee0a;padding-left:9px;margin:16px 0 6px}
@media (max-width:900px){.bp-card{grid-template-columns:52px 1fr}.bp-bars{grid-column:1 / -1}.bp-two{grid-template-columns:1fr}}
</style>"""


def _e(x):
    return _h.escape(str(x))


def _hud(title, chips, note=""):
    cs = "".join("<div class='bp-chip' style='--c:%s'><small>%s</small><b>%s</b></div>" % (c, lb, v) for lb, v, c in chips)
    return (_CSS + "<div class='bp-hud'><div class='bp-top'>&gt; " + title + "</div><div class='bp-chips'>" + cs + "</div>"
            + ("<div class='bp-note'>" + note + "</div>" if note else "") + "</div>")


def _th():
    base = dict(S.DEFAULT_TH)
    pre = S.PRESETS.get("มาตรฐาน (ตามบทความแรก)") or next(iter(S.PRESETS.values()))
    for k in ("rev", "gp", "ni", "nm", "roic", "de"):
        if k in pre:
            base[k] = pre[k]
    return base


# ---------------- ราคาปัจจุบัน + บันทึกผลย้อนหลัง ----------------
@st.cache_data(ttl=600, show_spinner=False)
def _now_prices(symbols):
    out = {}
    if yf is None or not symbols:
        return out
    try:
        d = yf.download(" ".join(symbols), period="7d", interval="1d", group_by="ticker", progress=False, auto_adjust=True, threads=True)
    except Exception:
        return out
    for s in symbols:
        try:
            sub = d[s] if len(symbols) > 1 else d
            c = sub["Close"].dropna()
            if len(c):
                out[s] = float(c.iloc[-1])
        except Exception:
            continue
    return out


def _load_log():
    try:
        return json.loads(LOG.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save_log(data):
    try:
        tmp = LOG.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        os.replace(tmp, LOG)
    except Exception:
        pass


def _log_today(top):
    """จดรายชื่อวันนี้ไว้ 1 ครั้ง/วัน เพื่อย้อนดูว่า 5–10 วันต่อมาเป็นยังไง"""
    today = _dt.date.today().isoformat()
    log = _load_log()
    if not top or any(x.get("date") == today for x in log):
        return
    spy = _now_prices(("SPY",)).get("SPY")
    log.append({"date": today, "spy": spy,
                "picks": [{"sym": r["sym"], "px": r.get("price")} for r in top if r.get("price")]})
    _save_log(log[-120:])


def _track():
    log = _load_log()
    st.markdown("<div class='section-label'>ผลย้อนหลังของรายชื่อที่เคยคัดไว้</div>", unsafe_allow_html=True)
    if not log:
        st.caption("ยังไม่มีบันทึก · เว็บจะจดรายชื่อ 10 ตัวไว้ให้ทุกวันที่เปิดหน้านี้ แล้วกลับมาเทียบกับราคาปัจจุบัน (อย่างน้อย 5 วันถึงจะเริ่มสรุปได้)")
        return
    syms = sorted({p["sym"] for x in log for p in x["picks"]})
    now = _now_prices(tuple(syms + ["SPY"]))
    rows, ok_rets, ok_spy = [], [], []
    today = _dt.date.today()
    for x in log:
        age = (today - _dt.date.fromisoformat(x["date"])).days
        rets = [(now[p["sym"]] / p["px"] - 1) * 100 for p in x["picks"] if p.get("px") and p["sym"] in now]
        if not rets:
            continue
        avg = sum(rets) / len(rets)
        spy_r = (now["SPY"] / x["spy"] - 1) * 100 if x.get("spy") and "SPY" in now else None
        rows.append({"วันที่คัด": x["date"], "ผ่านมา (วัน)": age, "ตัวที่ติดตามได้": len(rets),
                     "เฉลี่ยของ 10 ตัว %": round(avg, 1), "S&P 500 (SPY) %": None if spy_r is None else round(spy_r, 1)})
        if age >= 5 and spy_r is not None:
            ok_rets.append(avg)
            ok_spy.append(spy_r)
    if ok_rets:
        n = len(ok_rets)
        win = sum(1 for a, b in zip(ok_rets, ok_spy) if a > b)
        st.markdown(_hud("TRACK.RECORD", [("รอบที่ครบ 5 วัน", n, "#00f0ff"), ("ชนะ SPY", "%d/%d" % (win, n), "#19f5a5"),
                                         ("เฉลี่ยต่อรอบ", "%+.1f%%" % (sum(ok_rets) / n), "#fcee0a"),
                                         ("SPY เฉลี่ย", "%+.1f%%" % (sum(ok_spy) / n), "#7d86a6")],
                         "รอบน้อยมากยังสรุปอะไรไม่ได้ ต้องสะสมหลายสัปดาห์ถึงจะพอเชื่อได้ · ตัวเลขนี้ไม่รวมค่าธรรมเนียมและภาษี"),
                    unsafe_allow_html=True)
    else:
        st.caption("ยังไม่มีรอบที่ผ่านมาครบ 5 วัน ให้กลับมาดูใหม่ภายหลัง")
    if rows:
        with st.expander("ดูรายละเอียดทุกรอบ"):
            st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)


# ---------------- Stage 1–4 (วัฏจักรหุ้น) ----------------
@st.cache_data(ttl=3600, show_spinner=False)
def _stages(symbols):
    """ดึงราคา 14 เดือนของผู้เข้ารอบแล้วจัด Stage ให้ · ดึงไม่ได้ตัวไหนก็ข้ามตัวนั้น"""
    out = {}
    if yf is None or not symbols:
        return out
    symbols = list(symbols)
    for i in range(0, len(symbols), 80):
        chunk = symbols[i:i + 80]
        try:
            d = yf.download(" ".join(chunk), period="14mo", interval="1d", group_by="ticker", progress=False,
                            threads=True, auto_adjust=True)
        except Exception:
            continue
        for s in chunk:
            try:
                sub = d[s] if len(chunk) > 1 else d
                r = STG.classify(sub["Close"], sub["Volume"])
                if r:
                    out[s] = r
            except Exception:
                continue
    return out


# ---------------- บริบทเสริม: อารมณ์ตลาด · วันงบ · แนวรับ/ต้าน ----------------
@st.cache_data(ttl=600, show_spinner=False)
def _vix():
    if yf is None:
        return None
    try:
        c = yf.download("^VIX", period="5d", interval="1d", progress=False, auto_adjust=True)["Close"]
        c = c.iloc[:, 0] if hasattr(c, "columns") else c
        return float(c.dropna().iloc[-1])
    except Exception:
        return None


def _mood(v):
    """ข้อความอารมณ์ตลาดจาก VIX (เกณฑ์ 16/22/30 เป็นเกณฑ์ของเว็บนี้เอง ไม่ใช่มาตรฐานตลาด)"""
    if v is None:
        return None
    if v < 16:
        return ("นิ่ง", "#19f5a5", "ตลาดสงบ ราคามักแกว่งไม่แรง ใช้ขนาดไม้ตามแผนปกติได้")
    if v < 22:
        return ("เริ่มระแวง", "#fcee0a", "ตลาดเริ่มระวังตัว ควรตั้งจุดตัดขาดทุนทุกตัว")
    if v < 30:
        return ("ตื่นกลัว", "#ff9f43", "ตลาดตื่นกลัว ราคาแกว่งแรง ควรลดขนาดไม้หรือทยอยเข้า")
    return ("ตื่นกลัวสูงมาก", "#ff2a6d", "ตลาดตื่นตระหนก ราคาแกว่งหนักมาก ควรชะลอและลงเบาที่สุด")


def _extras(syms):
    """ข้อมูลเสริมของ 10 ตัวที่ติดอันดับ: วันงบ + แนวรับ/แนวต้าน/R:R จากราคารายวัน (ดึงไม่ได้ก็ข้ามไป ไม่กระทบอันดับ)"""
    out = {s: {} for s in syms}
    try:
        import fast_ui
        today = _dt.date.today()
        for s, d in (fast_ui._earn_map(tuple(syms)) or {}).items():
            if d is not None:
                out[s]["earn"] = (d - today).days
    except Exception:
        pass
    try:
        import rocket
        daily = rocket.load_daily(tuple(list(syms) + ["SPY"]))
        rows, _ = rocket.build_rows(list(syms), daily, {})
        for r in rows:
            out.setdefault(r["symbol"], {})["lv"] = r
    except Exception:
        pass
    return out


# ---------------- ตัวคัด ----------------
def _verdict(ev):
    ps = [(ev[k], n) for k, n, _c in _PILLARS if ev.get(k) is not None]
    why = "คะแนนรวม %.0f" % ev["total"]
    if ps:
        hi, lo = max(ps), min(ps)
        why = "เด่นที่ <b>%s</b> (%.0f) · อ่อนที่สุดคือ <b>%s</b> (%.0f)" % (hi[1], hi[0], lo[1], lo[0])
    fl = []
    if ev.get("passed") is not None and ev["passed"] < 7:
        fl.append("ไม่ผ่านเกณฑ์คุณภาพ %d ข้อ" % (7 - ev["passed"]))
    if ev.get("mos") is not None and ev["mos"] < -30:
        fl.append("ราคาสูงกว่ามูลค่าที่คำนวณ (DCF) ราว %.0f%% · DCF เป็นการประมาณหยาบ" % (-ev["mos"]))
    elif ev.get("v_score") is not None and ev["v_score"] < 40:
        fl.append("ราคาค่อนข้างแพงเมื่อเทียบการเติบโต")
    if ev.get("fscore") is not None and ev["fscore"] <= 4:
        fl.append("คะแนนสุขภาพการเงิน (F-Score) %d/9 ค่อนข้างต่ำ" % ev["fscore"])
    return why, fl


def _lvp(v):
    """ราคาของแนวรับ/แนวต้าน (rocket ส่งมาเป็น dict ที่มีคีย์ price)"""
    if isinstance(v, dict):
        v = v.get("price")
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _wait(x):
    """ระดับอ้างอิงสำหรับรอซื้อ: เส้น MA30 สัปดาห์ + แนวรับใกล้สุด (ไม่ใช้ R:R เพราะแนวต้านเล็กๆ ทำให้เพี้ยน)"""
    try:
        bits = []
        sg = (x or {}).get("stg")
        if sg and sg.get("ma") and sg.get("px"):
            gap = (1 - sg["ma"] / sg["px"]) * 100
            bits.append("เส้น MA30 สัปดาห์ ≈ %.2f (%s)" % (sg["ma"], "ราคาอยู่ติดเส้นแล้ว" if gap < 3 else "ต่ำกว่าราคา %.0f%%" % gap))
        lv = (x or {}).get("lv")
        if lv:
            sp = _lvp(lv.get("sup"))
            if sp and lv.get("dist_sup") is not None:
                bits.append("แนวรับใกล้สุด %.2f (ต่ำกว่าราคา %.1f%%)" % (sp, float(lv["dist_sup"])))
        return ("<div class='bp-plan'>📐 ระดับที่ใช้รอ: " + " · ".join(bits) + "</div>") if bits else ""
    except Exception:
        return ""


def _summary(ev, x):
    """บรรทัดสรุปเดียว รวมจังหวะ (Stage) + ราคาแพงไหม + งบใกล้ออกไหม · คืน (ข้อความ, สี)"""
    sg = (x or {}).get("stg")
    if not sg:
        return None
    sub = sg.get("sub")
    expensive = (ev.get("mos") is not None and ev["mos"] < -30) or (ev.get("v_score") is not None and ev["v_score"] < 40)
    earn = (x or {}).get("earn")
    soon = earn is not None and 0 <= earn <= 7
    cav = []
    if expensive:
        cav.append("ราคาค่อนข้างแพง")
    if ev.get("fscore") is not None and ev["fscore"] <= 4:
        cav.append("คะแนนสุขภาพการเงินต่ำ")
    if soon:
        cav.append("งบออกใน %d วัน" % earn)
    cv = (" แต่" + " และ".join(cav)) if cav else ""
    if sub == "early":
        if cav:
            return "ขึ้นมาไม่ไกลจากเส้น จังหวะดี%s → ถ้าจะเข้าให้ลงเบา ตั้งจุดตัดขาดทุนก่อน" % cv, "#fcee0a"
        return "ผ่านเกณฑ์คุณภาพ + ขึ้นมาไม่ไกลจากเส้น → จังหวะน่าสนใจ ทยอยเข้าตามแผนได้ (ตั้งจุดตัดขาดทุนก่อนเสมอ)", "#19f5a5"
    if sub == "mid":
        return "ผ่านเกณฑ์คุณภาพ แต่ห่างเส้น %.0f%% แล้ว%s → ลิสต์รอย่อ ถ้าจะเข้าก็ไม้เล็กๆ ไม่ไล่ราคา" % (sg["ext"], (" และ" + " และ".join(cav)) if cav else ""), "#ff9f43"
    if sub == "far":
        return "ผ่านเกณฑ์คุณภาพ แต่วิ่งไกลจากเส้น %.0f%% แล้ว%s → ลิสต์รอย่อ ไม่ไล่ราคา" % (sg["ext"], (" และ" + " และ".join(cav)) if cav else ""), "#ff2a6d"
    return None


def _reasons(ev, x):
    """เหตุผลที่น่าสนใจ เป็นภาษาง่ายๆ สร้างจากตัวเลขจริงของหุ้นตัวนั้น (เลือก 4 ข้อที่แรงสุด)"""
    out = []
    mom = ev.get("mom") or {}
    sg = (x or {}).get("stg")
    q, g, v, m = (ev.get(k) for k in ("q_score", "g_score", "v_score", "m_score"))
    p = ev.get("passed")
    if q is not None and q >= 60 and p is not None:
        out.append((q, "งบแข็งแรง: ผ่านเกณฑ์คุณภาพ %d จาก 7 ข้อ (กำไร หนี้ และเงินสดอยู่ในเกณฑ์ดี)" % p))
    if g is not None and g >= 70:
        out.append((g, "เติบโตเร็ว: ยอดขายและกำไรโตต่อเนื่อง (คะแนนเติบโต %d/100)" % round(g)))
    rs = mom.get("rs")
    if rs and rs >= 80:
        out.append((m if m is not None else rs, "แรงตลาดสูง: ราคาแข็งกว่าหุ้นราว %d%% ของทั้งตลาด (RS %d)" % (rs, rs)))
    if sg and sg.get("stage") == 2 and (sg.get("age") or 0) >= 30:
        out.append((65, "ขาขึ้นต่อเนื่อง: ราคาอยู่เหนือเส้นเฉลี่ย 30 สัปดาห์มา %d วัน และเส้นกำลังชี้ขึ้น%s"
                    % (sg["age"], " · ยังไม่วิ่งไกลจากเส้น" if sg.get("sub") == "early" else "")))
    mos, peg = ev.get("mos"), ev.get("peg")
    if mos is not None and mos >= 15:
        out.append((max(v or 0, 70), "ราคาต่ำกว่ามูลค่าที่ประมาณ (DCF) ราว %.0f%%" % mos))
    elif peg is not None and 0 < peg <= 1.5:
        out.append((max(v or 0, 60), "ราคาไม่แพงเมื่อเทียบการเติบโต (PEG %.2f ต่ำกว่า 1.5)" % peg))
    elif v is not None and v >= 70:
        out.append((v, "ราคายังอยู่ในเกณฑ์ไม่แพง (คะแนนราคา %d/100)" % round(v)))
    fs = ev.get("fscore")
    if fs is not None and fs >= 7:
        out.append((fs * 10, "สุขภาพการเงินดี (F-Score %d/9)" % fs))
    vr = mom.get("vol_ratio")
    if vr and vr >= 1.2:
        out.append((55, "ช่วงนี้มีคนซื้อขายมากกว่าปกติ (ปริมาณ ×%.1f เทียบค่าเฉลี่ย)" % vr))
    rel6 = mom.get("rel6")
    if rel6 is not None and rel6 >= 10:
        out.append((60, "6 เดือนที่ผ่านมาผลตอบแทนดีกว่าดัชนี SPY ราว %.0f%%" % rel6))
    out.sort(key=lambda z: -z[0])
    return [s for _k, s in out[:4]] or ["ผ่านเกณฑ์รวมของหน้านี้ แต่ไม่มีด้านใดเด่นมาก"]


def _card(i, ev, x=None):
    c = "#fcee0a" if i == 1 else "#00f0ff" if i <= 3 else "#8b5cf6"
    why, fl = _verdict(ev)
    x = x or {}
    sg = x.get("stg")
    stg_txt, stg_col = STG.label(sg)
    badge = "<span class='bp-st' style='--s:%s'>%s</span>" % (stg_col, _e(stg_txt)) if sg else ""
    sm = _summary(ev, x)
    summ = ("<div class='bp-sum' style='--s:%s'><b>🎯 สรุป:</b> %s</div>" % (sm[1], _e(sm[0]))) if sm else ""
    if x.get("earn") is not None and 0 <= x["earn"] <= 7:
        fl.insert(0, "งบประกาศใน %d วัน — ราคาอาจกระโดดแรง ควรรอหลังงบหรือลดขนาด" % x["earn"])
    if sg and sg.get("sub") in ("mid", "far"):
        fl.append("ห่างเส้น MA30 สัปดาห์ %.0f%% — ราคาวิ่งมาพอสมควรแล้ว ยังไม่ใช่จังหวะเข้าที่ดีที่สุด" % sg["ext"])
    bars = ""
    for k, n, col in _PILLARS:
        v = ev.get(k)
        bars += ("<div class='bp-bar' style='--c:%s'><span>%s</span><i><u style='width:%d%%'></u></i><b>%s</b></div>"
                 % (col, n, 0 if v is None else max(0, min(100, int(v))), "—" if v is None else "%d" % round(v)))
    rs = (ev.get("mom") or {}).get("rs")
    pills = []
    if ev.get("sector"):
        pills.append(("", _e(ev["sector"])))
    if rs:
        pills.append(("", "RS %d" % rs))
    if ev.get("passed") is not None:
        pills.append(("", "คุณภาพ %d/7" % ev["passed"]))
    if sg:
        pills.append(("", "ห่างเส้น MA30 %+.0f%%" % sg["ext"]))
        if sg["stage"] == 2 and sg.get("age"):
            pills.append(("", "เหนือเส้นมา %d วัน" % sg["age"]))
    if x.get("earn") is not None:
        pills.append(("hot" if x["earn"] <= 7 else "", "งบอีก %d วัน" % x["earn"]))
    pill_html = "".join("<span class='bp-pill %s'>%s</span>" % (k, v) for k, v in pills)
    oks = "".join("<div class='bp-li'>" + _e(s) + "</div>" for s in _reasons(ev, x))
    bad = "".join("<div class='bp-li'>" + _e(s) + "</div>" for s in fl) or "<div class='bp-li'>ไม่พบข้อควรระวังเด่นๆ ตามเกณฑ์ (ไม่ได้แปลว่าไม่มีความเสี่ยง)</div>"
    return ("<div class='bp-card' style='--c:%s'><div class='bp-rank'>%02d<small>SCORE %d</small></div>"
            "<div class='bp-main'><div class='bp-head'><span class='bp-sym'>%s</span><span class='bp-nm'>%s</span>%s</div>"
            "<div class='bp-pills'>%s</div>%s"
            "<div class='bp-two'><div class='bp-col'><div class='bp-ct'>✅ ทำไมถึงน่าสนใจ</div>%s</div>"
            "<div class='bp-col warn'><div class='bp-ct'>⚠️ ต้องระวัง</div>%s</div></div>%s</div>"
            "<div class='bp-bars'>%s<div class='bp-hl'>%s</div></div></div>") % (
        c, i, round(ev["total"]), _e(ev["sym"]), _e((ev.get("name") or "")[:34]), badge, pill_html, summ, oks, bad, _wait(x), bars, why)


def render_best():
    st.markdown(_CSS, unsafe_allow_html=True)
    with st.expander("📖 หน้านี้คัดยังไง (อ่าน 1 นาที)", expanded=False):
        st.markdown(
            "**เป้าหมาย:** หาหุ้นที่ดีหลายด้านพร้อมกัน ไม่ใช่ดีด้านเดียว\n\n"
            "**ขั้นที่ 1:** ดูแรงตลาดของทั้ง S&P 500 + Nasdaq 100 (ราว 520 ตัว) เหลือตัวที่อยู่ในขาขึ้น แล้วจัดเข้า **Stage 1–4** (ดูจากเส้นค่าเฉลี่ย 30 สัปดาห์) เอาเฉพาะ **Stage 2** เลือก %d ตัวที่แข็งสุดไปตรวจงบ\n\n"
            "**ขั้นที่ 2:** ตรวจ 4 เสา คือ **คุณภาพ** (กำไร หนี้ เงินสด) · **เติบโต** (ยอดขาย กำไรโต) · **ราคา** (แพงไหม) · **แรงตลาด** (แข็งกว่าหุ้นอื่นไหม) เสาละ 0–100\n\n"
            "**ผ่านเข้ารอบ:** ผ่านเกณฑ์คุณภาพอย่างน้อย 5/7 ข้อ · ผ่านอย่างน้อย 3 จาก 4 เสา (คะแนนเสาละ 60 ขึ้นไป) · อยู่ Stage 2 แล้วเรียงตามคะแนนรวม เอา %d ตัวแรก\n\n"
            "**Stage ช่วยบอกจังหวะ:** ช่วงต้น (ห่างเส้นไม่เกิน 15%%) = น่าสนใจสุด · ช่วงกลาง (15–30%%) = อย่าไล่ · วิ่งไกลแล้ว (เกิน 30%%) = รอย่อ · เกณฑ์เหล่านี้เป็นกฎหัวแม่มือ ไม่ใช่มาตรฐาน\n\n"
            "**ข้อจำกัดที่ต้องรู้:** ดีที่สุด *ตามเกณฑ์เหล่านี้* ไม่ใช่การรับประกันผลตอบแทน · เพราะบังคับว่าอยู่ Stage 2 หุ้นดีที่กำลังพักตัว (Stage 1/3) จะไม่ติดรายชื่อ · การแยก Stage 1 กับ Stage 3 เป็นแค่ประมาณการ · "
            "ข้อมูลมาจาก Yahoo ฟรี อาจขาดหรือล่าช้า · DCF เป็นการประมาณหยาบ · หน้าด้านล่างจะจดรายชื่อและเทียบผลย้อนหลังให้ดูเอง" % (CAND, TOPN))

    with st.expander("🧭 วิธีอ่านการ์ด & วิธีใช้ทุกวัน (กันลืม)", expanded=False):
        _H = lambda s: st.markdown("<div class='bp-h'>" + s + "</div>", unsafe_allow_html=True)
        _H("&gt; อ่านการ์ด 1 ใบ จากบนลงล่าง")
        st.markdown(
            "1. **เลขใหญ่ซ้าย** = อันดับ + SCORE (คะแนนรวม 0–100 ของ 4 เสา)\n"
            "2. **ป้าย STAGE** = หุ้นอยู่ช่วงไหนของวงจร · *ช่วงต้น* ราคาอยู่ใกล้เส้น (น่าสนใจสุด) · *ช่วงกลาง* ห่างเส้น 15–30% · *วิ่งไกลแล้ว* เกิน 30%\n"
            "3. **แถบป้ายเล็กๆ** = กลุ่มธุรกิจ · RS (แข็งกว่าหุ้นอื่นแค่ไหน 1–99) · ผ่านเกณฑ์คุณภาพกี่ข้อจาก 7 · ห่างเส้น MA30 · เหนือเส้นมากี่วัน · งบอีกกี่วัน (ป้ายส้ม = งบใกล้ออก)\n"
            "4. **🎯 สรุป** = ข้อสรุปบรรทัดเดียว **อ่านบรรทัดนี้ก่อนเสมอ** (เขียว = น่าสนใจ · เหลือง = ระวัง · ส้ม/แดง = รอย่อ)\n"
            "5. **✅ ทำไมถึงน่าสนใจ** = เหตุผลที่หุ้นตัวนี้ติดอันดับ (เลือก 4 ข้อที่แรงสุดจากตัวเลขจริงของหุ้นตัวนั้น)\n"
            "6. **⚠️ ต้องระวัง** = ข้อเสียที่ต้องรู้ก่อนตัดสินใจ เช่น งบใกล้ออก · ราคาแพงกว่า DCF · วิ่งมาไกลแล้ว\n"
            "7. **📐 ระดับที่ใช้รอ** = เส้น MA30 และแนวรับใกล้สุด ใช้เป็นระดับอ้างอิงตอนรอย่อ ไม่ได้แปลว่าราคาจะย่อลงไปถึงจริง\n"
            "8. **แท่ง 4 สีด้านขวา** = คุณภาพ · เติบโต · ราคา · แรงตลาด (ยิ่งยาวยิ่งดี · ดูว่าเสาไหนสั้นสุด)")
        _H("&gt; แถบด้านบนหน้า")
        st.markdown(
            "- **MARKET.MOOD** = ตลาดกลัวแค่ไหน (VIX) · ตื่นกลัว = ลงไม้เล็กลง\n"
            "- **มุมมอง** = *ยังไม่วิ่งไกล* ตัดตัวที่ห่างเส้นเกิน 30% ออก · *Stage 2 ทั้งหมด* เห็นครบ ใช้เป็นลิสต์รอย่อ\n"
            "- **TRACK.RECORD** (ล่างสุด) = จดรายชื่อทุกวันที่เปิด แล้วเทียบกับ SPY ว่าชนะจริงไหม ต้องสะสมหลายสัปดาห์ถึงเชื่อได้")
        _H("&gt; วิธีใช้ทุกวัน (ประมาณ 3 นาที)")
        st.markdown(
            "1. ดู **MARKET.MOOD** ก่อน\n"
            "2. อ่านเฉพาะบรรทัด **🎯 สรุป** ของทุกใบ แยกเป็น 2 กอง: *น่าสนใจ* กับ *ลิสต์รอย่อ*\n"
            "3. ตัวที่สนใจ → อ่าน **✅ / ⚠️** แล้วเปิดหน้า **DEEP INSIGHT** ดูรายตัว\n"
            "4. ก่อนกดซื้อจริง → ตั้งจุดตัดขาดทุนและขนาดไม้ที่หน้า **FAST TRADE / TRADE LOG** (ตัว R)\n"
            "5. สัปดาห์ละครั้ง → ดู **TRACK.RECORD**")
        _H("&gt; 3 ข้อห้ามลืม")
        st.markdown(
            "1. นี่คือรายชื่อ *น่าศึกษา* ไม่ใช่สัญญาณซื้อ\n"
            "2. หุ้นดี ≠ จังหวะดี · ถ้าสรุปบอกให้รอย่อ ก็รอ\n"
            "3. เกณฑ์ทั้งหมด (15% / 30% / 5 ใน 7 ข้อ ฯลฯ) เป็นกฎหัวแม่มือ ไม่ใช่มาตรฐานตลาด\n\n"
            "**จำสั้นๆ:** *ตลาดกลัวไหม → อ่าน 🎯 → รอย่อหรือเข้า → ตั้งจุดตัดขาดทุน*")

    syms = [s for s in S.universe("both") if s != "SPY"]
    if not syms:
        st.warning("โหลดรายชื่อหุ้นไม่ได้ตอนนี้")
        return
    with st.spinner("กำลังสแกนแรงตลาดทั้ง %d ตัว ... (รอบแรกอาจใช้ 1–2 นาที หลังจากนั้นจำผลไว้ 1 ชั่วโมง)" % len(syms)):
        moms = S.momentum_batch(tuple(syms))
    pool = [(s, m) for s, m in moms.items() if m and m.get("trend") and m.get("score") is not None]
    pool.sort(key=lambda x: -x[1]["score"])
    stg, stage_ok = {}, False
    with st.spinner("กำลังจัด Stage 1–4 ของผู้เข้ารอบ ..."):
        stg = _stages(tuple(s for s, _m in pool[:CAND * 2]))
    if stg:
        stage_ok = True
        s2 = [s for s, _m in pool[:CAND * 2] if (stg.get(s) or {}).get("stage") == 2]
        cand = s2[:CAND]
    else:
        cand = [s for s, _m in pool[:CAND]]
    if not cand:
        st.warning("ดึงข้อมูลราคาไม่สำเร็จหรือไม่มีหุ้นอยู่ในขาขึ้นเลย ลองใหม่อีกครั้งภายหลัง")
        return

    cache = S._load_cache()
    now = time.time()
    fresh = [s for s in cand if s in cache and now - cache[s].get("t", 0) <= S.CACHE_TTL]
    need = [s for s in cand if s not in fresh]
    if need:
        if st.button("🏆 หาหุ้นที่ดีที่สุด (ดึงงบ %d ตัว · ครั้งแรกอาจใช้ 1–3 นาที ครั้งต่อไปไวกว่ามาก)" % len(need), key="bp_go"):
            bar = st.progress(0.0, text="กำลังเริ่ม ...")
            t0 = time.time()

            def prog(d, n, s):
                bar.progress(d / n, text="ดึงงบ %d/%d · %s · ผ่านไป %.0f วินาที" % (d, n, s, time.time() - t0))
            _, n_do, fail = S.fetch_many(need, progress=prog)
            bar.empty()
            st.success("เสร็จ — ดึงใหม่ %d ตัว%s" % (n_do, (" · ดึงไม่ได้ %d ตัว" % len(fail)) if fail else ""))
            cache = S._load_cache()
        elif not fresh:
            st.markdown(_hud("TOP.PICKS // S&amp;P 500 + NASDAQ 100",
                             [("สแกนแรงตลาด", len(syms), "#00f0ff"), ("ขาขึ้น", len(pool), "#19f5a5"), ("รอตรวจงบ", len(cand), "#fcee0a")],
                             "ยังไม่มีข้อมูลงบในเครื่อง กดปุ่มด้านบนเพื่อเริ่ม (ผลจะถูกจำไว้ 7 วัน)"), unsafe_allow_html=True)
            _track()
            return

    have = [s for s in cand if s in cache and cache[s].get("raw")]
    th = _th()
    evs = []
    for s in have:
        try:
            ev = S.evaluate(cache[s]["raw"], th, moms.get(s))
        except Exception:
            continue
        ev["sym"] = s
        evs.append(ev)
    ok = [e for e in evs if (e.get("known") or 0) >= 5 and (e.get("passed") or 0) >= 5 and (e.get("pillars_ok") or 0) >= 3
          and e.get("total") is not None]
    ok.sort(key=lambda e: -e["total"])
    top_all = ok[:TOPN]
    near = [e for e in ok if stg.get(e["sym"]) and stg[e["sym"]]["sub"] != "far"]
    _log_today(top_all)

    st.markdown(_hud("TOP.PICKS // S&amp;P 500 + NASDAQ 100",
                     [("สแกนแรงตลาด", len(syms), "#00f0ff"), ("ขาขึ้น", len(pool), "#19f5a5")]
                     + ([("Stage 2", len(cand), "#8b5cf6")] if stage_ok else [])
                     + [("ตรวจงบแล้ว", len(evs), "#fcee0a"), ("ผ่านเข้ารอบ", len(ok), "#ff2a6d")],
                     "ผ่านเข้ารอบ = ผ่านคุณภาพ ≥5/7 · ผ่าน ≥3 จาก 4 เสา · อยู่ %s · เรียงตามคะแนนรวม แสดง %d ตัวแรก%s" % (
                         "Stage 2" if stage_ok else "ขาขึ้น", TOPN, (" · ยังไม่ได้ดึงงบอีก %d ตัว" % len(need)) if need else "")),
                unsafe_allow_html=True)
    if not stage_ok:
        st.caption("⚠️ ตอนนี้จัด Stage ไม่ได้ (ดึงราคาไม่สำเร็จ) จึงคัดจากเงื่อนไขขาขึ้นเดิมไปก่อน")
    top = top_all
    if stage_ok and top_all:
        view = st.radio("มุมมอง", ["🟢 ยังไม่วิ่งไกล (ห่างเส้น ≤30%)",
                                   "📋 Stage 2 ทั้งหมด (รวมตัวที่วิ่งไกลแล้ว)"],
                        key="bp_view", horizontal=False)
        st.caption("ผ่านเข้ารอบ %d ตัว · ในนั้นยังไม่วิ่งไกล %d ตัว" % (len(ok), len(near)))
        if view.startswith("🟢"):
            top = near[:TOPN]
            if not top:
                st.info("ตอนนี้ตัวที่เข้าเกณฑ์ทั้งหมดวิ่งไกลจากเส้นแล้ว ลองสลับไปมุมมอง \"Stage 2 ทั้งหมด\" แล้วรอให้ราคาย่อ")
                _track()
                return
    if not top:
        st.info("ตอนนี้ไม่มีหุ้นที่ผ่านทุกเงื่อนไขพร้อมกัน ซึ่งเป็นเรื่องปกติเมื่อตลาดอ่อนแอ · ถ้าอยากผ่อนเกณฑ์ ไปที่หน้า QUALITY SCREEN เลือกชุดเกณฑ์ผ่อน")
        _track()
        return

    vx = _vix()
    md = _mood(vx)
    if md:
        st.markdown(_hud("MARKET.MOOD", [("VIX", "%.1f" % vx, md[1]), ("อารมณ์ตลาด", md[0], md[1])],
                         md[2] + " · เกณฑ์ VIX 16/22/30 เป็นเกณฑ์ของเว็บนี้ ไม่ใช่มาตรฐานตลาด"), unsafe_allow_html=True)
    with st.spinner("กำลังเช็ควันประกาศงบและแนวรับ/แนวต้านของ %d ตัวที่ติดอันดับ ..." % len(top)):
        ex = _extras([e["sym"] for e in top])
    for e in top:
        ex.setdefault(e["sym"], {})["stg"] = stg.get(e["sym"])
    st.markdown("<div class='section-label'>%d อันดับที่ดีที่สุดตามเกณฑ์</div>" % len(top), unsafe_allow_html=True)
    st.markdown("".join(_card(i, e, ex.get(e["sym"])) for i, e in enumerate(top, 1)), unsafe_allow_html=True)
    st.caption("⚠️ เป็นรายชื่อ \"น่าศึกษา\" ไม่ใช่สัญญาณซื้อ · ก่อนลงเงินจริงควรเปิดดูรายตัวในหน้า DEEP INSIGHT และตั้งจุดตัดขาดทุนในหน้า FAST TRADE / TRADE LOG")
    _track()