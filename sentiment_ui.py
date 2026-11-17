# -*- coding: utf-8 -*-
"""
sentiment_ui.py
===============
มาตรวัด "ฝูงชนกลัวหรือโลภ" + คะแนนพื้นฐาน

แอปอ่านใจคนไม่ได้ แต่วัด "ร่องรอยของอารมณ์" จากข้อมูลจริงได้ (RSI, ระยะห่างจากจุดสูงสุด, ปริมาณซื้อขาย, Put/Call,
Short interest, ราคาเป้าหมายนักวิเคราะห์, VIX) แล้วสรุปเป็นคะแนน 0-100 (0 = กลัวสุดขีด, 100 = โลภสุดขีด)
จับคู่กับคะแนนพื้นฐานของบริษัท เพื่อตอบ 2 คำถาม: "ตัวนี้ดีไหม" + "ตอนนี้ฝูงชนอยู่โซนไหน"

เรียกใช้:
  sentiment_ui.render_market_mood()              # หน้าแรก: อารมณ์ของทั้งตลาด
  sentiment_ui.render_stock_mood(ticker, info)   # หน้าวิเคราะห์รายตัว
ไม่ใช่เครื่องทำนายราคา และไม่ใช่คำแนะนำซื้อขาย
"""

import html as _html

import pandas as pd
import streamlit as st
import yfinance as yf

# ---------------------------------------------------------------
# เครื่องมือเล็กๆ
# ---------------------------------------------------------------


def _clamp(x, lo=0.0, hi=100.0):
    return max(lo, min(hi, x))


def _interp(x, pts):
    """แปลงค่า x เป็นคะแนนด้วยเส้นตรงต่อจุด (pts เรียงจากน้อยไปมาก) · เกินช่วง = ค่าปลายทาง"""
    if x <= pts[0][0]:
        return float(pts[0][1])
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return float(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
    return float(pts[-1][1])


def _rsi(close, n=14):
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1.0 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1.0 / n, adjust=False).mean()
    rs = up / dn.replace(0, float("nan"))
    return 100 - 100 / (1 + rs)


def _mood_label(s):
    if s < 25:
        return "กลัวสุดขีด", "#ff2a6d"
    if s < 45:
        return "กลัว", "#ff7a45"
    if s <= 55:
        return "กลางๆ", "#fcee0a"
    if s <= 75:
        return "โลภ", "#8be84a"
    return "โลภสุดขีด", "#19f5a5"


def _score_color(s):
    return "hsl(%d,92%%,56%%)" % int(_clamp(s) * 1.2)       # 0 = แดง · 50 = เหลือง · 100 = เขียว


def _e(t):
    return _html.escape(str(t), quote=True)


_CSS = (
    "<style>"
    ".mm-wrap{margin:6px 0 4px}"
    ".mm-top{display:flex;align-items:flex-end;gap:18px;flex-wrap:wrap;margin-bottom:10px}"
    ".mm-big{font-size:44px;font-weight:800;line-height:1;font-family:var(--mono,monospace)}"
    ".mm-lab{font-size:19px;font-weight:700;padding-bottom:5px}"
    ".mm-sub{font-size:13px;color:#9aa4c4;padding-bottom:6px}"
    ".mm-bar{position:relative;height:14px;border-radius:7px;"
    "background:linear-gradient(90deg,#ff2a6d 0%,#ff7a45 25%,#fcee0a 50%,#8be84a 75%,#19f5a5 100%);margin:6px 0 4px;"
    "box-shadow:0 0 12px rgba(0,240,255,.12)}"
    ".mm-bar i{position:absolute;top:-6px;width:4px;height:26px;background:#fff;border-radius:2px;"
    "box-shadow:0 0 8px #fff,0 0 2px #000;transform:translateX(-2px)}"
    ".mm-ends{display:flex;justify-content:space-between;font-size:11.5px;color:#7d86a6;letter-spacing:.5px}"
    ".mm-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px;margin-top:12px}"
    ".mm-c{background:rgba(12,14,28,.82);border:1px solid rgba(0,240,255,.22);padding:10px 12px;"
    "clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px))}"
    ".mm-c b{display:block;font-size:12.5px;color:#9aa4c4;font-weight:600;margin-bottom:2px}"
    ".mm-c .v{font-size:17px;font-weight:700;color:#e6f1ff}"
    ".mm-c .m{height:5px;background:rgba(125,134,166,.2);border-radius:3px;margin:6px 0 5px;overflow:hidden}"
    ".mm-c .m u{display:block;height:100%;border-radius:3px;text-decoration:none}"
    ".mm-c p{margin:0;font-size:12.5px;color:#b8c0dc;line-height:1.45}"
    ".fd-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}"
    ".fd-chip{font-size:13px;padding:5px 10px;border:1px solid rgba(0,240,255,.25);background:rgba(12,14,28,.82);color:#dfe7ff}"
    ".fd-chip em{font-style:normal;font-weight:700;margin-right:5px}"
    ".vd{margin-top:14px;padding:13px 16px;border-left:4px solid var(--c,#fcee0a);background:rgba(12,14,28,.88)}"
    ".vd h5{margin:0 0 5px;font-size:16px;color:var(--c,#fcee0a)}"
    ".vd p{margin:0;font-size:14px;color:#cfd7f2;line-height:1.6}"
    ".mm-wrap{padding:18px 20px 16px;border:1px solid rgba(0,240,255,.18);background:linear-gradient(160deg,rgba(0,240,255,.05),rgba(12,14,28,.82) 45%)}"
    ".mm-big{text-shadow:none;letter-spacing:-1px}"
    ".mm-bar{height:16px;border-radius:8px;margin:10px 0 6px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}"
    ".mm-bar s{position:absolute;top:3px;bottom:3px;width:1px;background:rgba(5,6,13,.55)}"
    ".mm-bar i{top:-7px;width:5px;height:30px;border-radius:3px;box-shadow:0 0 0 1px rgba(0,0,0,.55)}"
    ".mm-grid{grid-template-columns:repeat(auto-fit,minmax(185px,1fr));gap:12px;margin-top:16px}"
    ".mm-c{position:relative;display:flex;flex-direction:column;padding:12px 14px 12px;border-top:2px solid var(--ac,#00f0ff);background:linear-gradient(180deg,rgba(255,255,255,.04),rgba(12,14,28,.88) 50%);transition:transform .2s}"
    ".mm-c:hover{transform:translateY(-2px)}"
    ".mm-c .v{font-size:21px;font-weight:800;font-family:var(--mono,monospace);margin:2px 0 0;line-height:1.2}"
    ".mm-c .v small{display:block;font-size:12.5px;font-weight:500;font-family:inherit;color:#aab3d1;margin-top:3px;line-height:1.4}"
    ".mm-c .m{height:7px;border-radius:4px;background:#171a2b;margin:9px 0 7px}"
    ".mm-c .m u{border-radius:4px}"
    ".mm-c .z{align-self:flex-start;font-size:11.5px;font-weight:700;letter-spacing:.5px;padding:0 9px;line-height:18px;margin-bottom:7px}"
    ".mm-c p{flex:1}"
    ".mm-c p strong{display:block;font-size:13.5px;font-weight:600;line-height:1.5;color:#e6f1ff}"
    ".mm-c p em{display:block;margin-top:6px;padding-top:6px;border-top:1px dashed rgba(125,134,166,.25);font-style:normal;font-size:12px;line-height:1.5;color:#8d97b8}"
    "</style>"
)


def _gauge(score, big_label=None):
    lab, col = _mood_label(score)
    return (
        '<div class="mm-top"><div class="mm-big" style="color:%s">%d</div>'
        '<div class="mm-lab" style="color:%s">%s</div>'
        '<div class="mm-sub">%s</div></div>'
        '<div class="mm-bar"><s style="left:25%%"></s><s style="left:50%%"></s><s style="left:75%%"></s><i style="left:%.1f%%"></i></div>'
        '<div class="mm-ends"><span>◀ กลัวสุดขีด</span><span>กลางๆ</span><span>โลภสุดขีด ▶</span></div>'
    ) % (col, round(score), col, lab, _e(big_label or "คะแนน 0-100"), _clamp(score))


_UP, _DN = "#19f5a5", "#ff4d6d"


def _sign_color(txt):
    """ขึ้นต้นด้วย + → เขียว, - → แดง, ไม่มีเครื่องหมาย → None"""
    txt = txt.strip()
    if txt[:1] == "+":
        return _UP
    if txt[:1] in ("-", "\u2212"):
        return _DN
    return None


def _tint(col, a=0.14):
    if col.startswith("hsl("):
        return col.replace("hsl(", "hsla(").replace(")", ",%s)" % a)
    return col


def _rsi_note(r, who="หุ้นตัวนี้"):
    if r <= 30:
        m = "%sถูกขายหนักเกินไป ราคาลงเร็วจนมักมีคนเข้าช้อนซื้อ" % who
    elif r < 45:
        m = "ราคาลงมาเล็กน้อย คนเริ่มระวังตัว แต่ยังไม่ถึงขั้นตื่นตระหนก"
    elif r <= 55:
        m = "คนซื้อและคนขายสมดุลกัน ไม่ร้อนไม่เย็น"
    elif r < 70:
        m = "ราคาขึ้นมาค่อนข้างแรง คนเริ่มมั่นใจ แต่ยังไม่ร้อนเกินไป"
    else:
        m = "%sร้อนแรงเกินไป ราคาขึ้นเร็วจนอาจพักตัว" % who
    return m + "|RSI วัดว่าช่วงสองสัปดาห์ที่ผ่านมามีคนซื้อหรือคนขายมากกว่ากัน (ต่ำกว่า 30 = ขายหนัก · สูงกว่า 70 = ซื้อหนัก)"


def _cell(title, value, score, note):
    import re as _re
    col = _score_color(score)
    zlab, _ = _mood_label(score)
    head, sep, tail = value.partition("<small")
    sc = _sign_color(_re.sub(r"<[^>]+>", "", head)) or col       # เลขมีเครื่องหมาย: บวกเขียว ลบแดง · ไม่มี: ใช้สีตามโซน
    inner = head
    if sep:
        tail = _re.sub(r"([+\-\u2212]\d+(?:\.\d+)?%)",
                       lambda m: "<span style='color:%s!important;font-weight:700'>%s</span>" % (_sign_color(m.group(1)), m.group(1)), tail)
        inner = head + "<small" + tail
    meaning, _, what = note.partition("|")
    ntxt = "<strong>%s</strong>" % _e(meaning.strip())
    if what.strip():
        ntxt += "<em>%s</em>" % _e(what.strip())
    return (
        '<div class="mm-c" style="--ac:%s"><b>%s</b><div class="v" style="color:%s!important">%s</div>'
        '<div class="m"><u style="width:%.0f%%;background:%s"></u></div>'
        '<div class="z" style="color:%s!important;border:1px solid %s;background:%s">%s</div><p>%s</p></div>'
    ) % (col, _e(title), sc, inner, _clamp(score), col, col, col, _tint(col), _e(zlab), ntxt)


# ---------------------------------------------------------------
# อารมณ์ของทั้งตลาด (หน้าแรก)
# ---------------------------------------------------------------
@st.cache_data(ttl=600, show_spinner=False)
def _market_inputs():
    data = yf.download("^VIX SPY", period="1y", interval="1d", group_by="ticker", progress=False, threads=True, auto_adjust=True)

    def col(sym):
        try:
            d = data[sym]["Close"].dropna()
        except Exception:
            d = pd.Series(dtype=float)
        return d

    vix, spy = col("^VIX"), col("SPY")
    out = {}
    if len(spy) >= 130:
        px = float(spy.iloc[-1])
        ma125 = float(spy.tail(125).mean())
        hi = float(spy.tail(252).max())
        out["spy"] = px
        out["mom_pct"] = (px / ma125 - 1) * 100
        out["dd_pct"] = (px / hi - 1) * 100
        out["rsi"] = float(_rsi(spy).iloc[-1])
    if len(vix) >= 5:
        out["vix"] = float(vix.iloc[-1])
        out["vix_prev"] = float(vix.iloc[-6]) if len(vix) >= 6 else float(vix.iloc[0])
    return out


def render_market_mood():
    st.markdown("#### 🧭 อารมณ์ตลาดตอนนี้ — กลัวหรือโลภ")
    try:
        m = _market_inputs()
    except Exception as e:
        st.caption("ดึงข้อมูลอารมณ์ตลาดไม่ได้: " + str(e))
        return
    cells, scores = [], []
    if "vix" in m:
        s = _interp(m["vix"], [(12, 92), (16, 70), (20, 50), (25, 28), (30, 14), (40, 2)])
        ch = m["vix"] - m["vix_prev"]
        v = m["vix"]
        note = ("ตลาดกำลังตื่นตระหนก" if v >= 30 else ("ตลาดเริ่มกังวล" if v >= 20 else ("ตลาดสงบมาก บางทีอาจชะล่าใจ" if v < 15 else "ตลาดอยู่ในอารมณ์ปกติ")))
        note += "|VIX = ดัชนีวัดความกลัวของตลาด ยิ่งสูงยิ่งกลัว (เกิน 30 = ตื่นตระหนก · ต่ำกว่า 15 = ชะล่าใจ)"
        cells.append(_cell("ความผันผวน (VIX)", "%.1f <small style='color:#9aa4c4'>(%+.1f ใน 5 วัน)</small>" % (m["vix"], ch), s, note))
        scores.append(s)
    if "mom_pct" in m:
        s = _interp(m["mom_pct"], [(-10, 0), (-3, 45), (3, 55), (10, 100)])
        note = ("ราคาตลาดอยู่เหนือค่าเฉลี่ยมาก คนมั่นใจ" if m["mom_pct"] > 3 else ("ราคาตลาดต่ำกว่าค่าเฉลี่ย คนเริ่มถอย" if m["mom_pct"] < -3 else "ราคาตลาดอยู่ใกล้ค่าเฉลี่ย ยังไม่เอียงไปทางไหน")) + "|เทียบราคา S&P 500 (SPY) กับค่าเฉลี่ย 125 วัน (ราว 6 เดือน)"
        cells.append(_cell("แรงส่งของตลาด", "%+.1f%% <small style='color:#9aa4c4'>จากเส้นเฉลี่ย 125 วัน</small>" % m["mom_pct"], s, note))
        scores.append(s)
    if "dd_pct" in m:
        s = _interp(m["dd_pct"], [(-20, 0), (-10, 25), (-3, 60), (0, 100)])
        note = ("ตลาดอยู่ใกล้จุดสูงสุดของปี คนมั่นใจ" if m["dd_pct"] > -3 else ("ตลาดตกลงมาลึก คนเริ่มกลัว" if m["dd_pct"] < -10 else "ตลาดย่อลงมาพอประมาณ")) + "|ดูว่า S&P 500 ต่ำกว่าจุดสูงสุดในรอบ 1 ปีเท่าไร"
        cells.append(_cell("ห่างจากจุดสูงสุด 52 สัปดาห์", "%.1f%%" % m["dd_pct"], s, note))
        scores.append(s)
    if "rsi" in m:
        s = _interp(m["rsi"], [(20, 0), (30, 20), (45, 42), (55, 58), (70, 80), (80, 100)])
        note = _rsi_note(m["rsi"], "ตลาด")
        cells.append(_cell("RSI ของตลาด (14 วัน)", "%.0f" % m["rsi"], s, note))
        scores.append(s)
    if not scores:
        st.caption("ยังไม่มีข้อมูลพอคำนวณ (ลองรีเฟรชอีกครั้ง)")
        return
    sc = sum(scores) / len(scores)
    lab, _ = _mood_label(sc)
    tip = {
        "กลัวสุดขีด": "ตลาดตื่นตระหนก — ในอดีตช่วงนี้มักตามด้วยการเด้งสั้นๆ ได้ แต่ถ้าข่าวร้ายจริงก็ลงต่อได้เหมือนกัน",
        "กลัว": "ตลาดระวังตัว — ผู้คนถือเงินสดมากขึ้น ราคาหุ้นดีๆ อาจถูกลงเกินไปในบางตัว",
        "กลางๆ": "ตลาดไม่ได้กลัวหรือโลภเกินไป — ให้ดูรายกลุ่ม/รายตัวเป็นหลัก",
        "โลภ": "ตลาดมั่นใจ — เทรนด์ยังเอื้อ แต่ระวังไล่ราคาตอนวิ่งไปไกลแล้ว",
        "โลภสุดขีด": "ตลาดชะล่าใจมาก — ในอดีตช่วงนี้มักตามด้วยการพักตัวได้ แต่ไม่ได้แปลว่าจะลงทันที",
    }[lab]
    st.markdown(
        _CSS + '<div class="mm-wrap">' + _gauge(sc, "คะแนนรวมของตลาด (เฉลี่ย %d ตัวชี้วัด)" % len(scores))
        + '<div class="mm-grid">' + "".join(cells) + "</div></div>",
        unsafe_allow_html=True,
    )
    st.caption(
        "อ่านว่า: " + tip + " · สีบอกแค่ \"อารมณ์ของฝูงชน\" ไม่ได้บอกว่าดีหรือไม่ดี · "
        "เป็นเข็มทิศบอกโซน ไม่ใช่เครื่องทำนายว่าตลาดจะขึ้นหรือลง · ไม่ใช่คำแนะนำซื้อขาย")


# ---------------------------------------------------------------
# อารมณ์ของหุ้นรายตัว
# ---------------------------------------------------------------
@st.cache_data(ttl=600, show_spinner=False)
def _stock_inputs(sym):
    out = {}
    t = yf.Ticker(sym)
    h = t.history(period="1y", interval="1d", auto_adjust=True)
    if h is not None and len(h) >= 30:
        c, v = h["Close"].dropna(), h["Volume"].fillna(0)
        out["px"] = float(c.iloc[-1])
        out["rsi"] = float(_rsi(c).iloc[-1])
        out["dd_pct"] = (float(c.iloc[-1]) / float(c.tail(252).max()) - 1) * 100
        out["chg"] = (float(c.iloc[-1]) / float(c.iloc[-2]) - 1) * 100
        avg20 = float(v.iloc[-21:-1].mean()) if len(v) >= 21 else 0.0
        if avg20 > 0:
            out["vol_ratio"] = float(v.iloc[-1]) / avg20
    try:
        exps = list(t.options or [])
        if exps:
            # ใช้วันหมดอายุแรกที่เหลืออย่างน้อย ~5 วัน (ตัวที่ใกล้หมดอายุมากข้อมูลจะบิดเบี้ยว)
            today = pd.Timestamp.today().normalize()
            pick = next((e for e in exps if (pd.Timestamp(e) - today).days >= 5), exps[0])
            oc = t.option_chain(pick)
            co, po = float(oc.calls["openInterest"].fillna(0).sum()), float(oc.puts["openInterest"].fillna(0).sum())
            if co > 0 and (co + po) >= 200:
                out["pc"] = po / co
                out["pc_exp"] = pick
    except Exception:
        pass
    return out


def _fund_points(info):
    """คะแนนพื้นฐานแบบง่าย: แต่ละข้อ 0/1/2 แต้ม · คืน (รายการ, คะแนน 0-100 หรือ None)"""
    rows = []

    def add(name, valtxt, pts, why):
        rows.append((name, valtxt, pts, why))

    g = info.get("revenueGrowth")
    if isinstance(g, (int, float)):
        add("รายได้โต", "%+.0f%%" % (g * 100), 2 if g >= 0.12 else (1 if g >= 0.03 else 0), "รายได้โตเร็วกว่า 12% = ดี")
    m = info.get("profitMargins")
    if isinstance(m, (int, float)):
        add("กำไรสุทธิ", "%.0f%%" % (m * 100), 2 if m >= 0.15 else (1 if m >= 0.05 else 0), "ขายของ 100 เหลือกำไรกี่บาท · เกิน 15% = ดี")
    r = info.get("returnOnEquity")
    if isinstance(r, (int, float)):
        add("ROE", "%.0f%%" % (r * 100), 2 if r >= 0.15 else (1 if r >= 0.07 else 0), "ใช้เงินผู้ถือหุ้นสร้างกำไรได้เก่งแค่ไหน · เกิน 15% = ดี")
    d = info.get("debtToEquity")
    if isinstance(d, (int, float)):
        add("หนี้ต่อทุน", "%.0f%%" % d, 2 if d <= 60 else (1 if d <= 150 else 0), "ต่ำกว่า 60% = หนี้น้อย · เกิน 150% = หนี้เยอะ (ธนาคารมักสูงเป็นปกติ)")
    f = info.get("freeCashflow")
    if isinstance(f, (int, float)):
        add("กระแสเงินสดอิสระ", "บวก" if f > 0 else "ลบ", 2 if f > 0 else 0, "ธุรกิจเหลือเงินสดจริงไหม")
    pe = info.get("forwardPE")
    if isinstance(pe, (int, float)) and pe > 0:
        add("P/E ล่วงหน้า", "%.1f" % pe, 2 if pe <= 18 else (1 if pe <= 30 else 0), "ต่ำ = ถูกกว่า (ควรเทียบกลุ่มเดียวกัน)")
    if not rows:
        return rows, None
    sc = sum(p for _, _, p, _ in rows) / (2.0 * len(rows)) * 100
    return rows, sc


def _fund_label(s):
    if s is None:
        return "ไม่มีข้อมูลพอ", "#7d86a6"
    if s >= 70:
        return "พื้นฐานดี", "#19f5a5"
    if s >= 40:
        return "พื้นฐานกลางๆ", "#fcee0a"
    return "พื้นฐานอ่อน", "#ff2a6d"


def _verdict(fund, mood):
    """จับคู่ พื้นฐาน × อารมณ์ฝูงชน → ข้อความอ่านง่าย (ไม่ใช่คำแนะนำ)"""
    if fund is None:
        fk = "mid"
    else:
        fk = "good" if fund >= 70 else ("mid" if fund >= 40 else "weak")
    mk = "fear" if mood < 45 else ("greed" if mood > 55 else "calm")
    T = {
        ("good", "fear"): ("พื้นฐานดี + ฝูงชนกลัว", "#19f5a5",
                           "เป็นคู่ที่นักลงทุนสายมูลค่าชอบมอง: ธุรกิจดี แต่คนกำลังกลัวจึงอาจถูกกดราคาเกินไป "
                           "ก่อนสรุปให้เช็กข่าวว่ากลัวเพราะอะไร ถ้าเป็นแค่ตลาดรวมแดงก็น่าเฝ้าดู แต่ถ้าธุรกิจมีปัญหาจริงราคาถูกอาจเป็นกับดัก"),
        ("good", "calm"): ("พื้นฐานดี + อารมณ์กลางๆ", "#8be84a",
                           "ธุรกิจดีและฝูงชนไม่ได้ตื่นเต้นเกินไป ไม่มีสัญญาณอารมณ์สุดขีดมาช่วยจับจังหวะ ให้ดูแนวรับ/แนวต้านและข่าวประกอบ"),
        ("good", "greed"): ("พื้นฐานดี + ฝูงชนโลภ", "#fcee0a",
                            "ธุรกิจดีก็จริง แต่คนกำลังแห่ซื้อ ราคาอาจวิ่งนำหน้าไปแล้ว ระวังไล่ราคา การรอจังหวะพักตัวมักเข้าได้ในราคาดีกว่า"),
        ("mid", "fear"): ("พื้นฐานกลางๆ + ฝูงชนกลัว", "#fcee0a",
                          "ราคาอาจถูกกดจากอารมณ์ แต่ธุรกิจไม่ได้เด่นพอให้มั่นใจว่าจะกลับมา ถ้าเทรดสั้นอาจมีเด้ง แต่ควรกำหนดจุดตัดขาดทุนให้ชัด"),
        ("mid", "calm"): ("พื้นฐานกลางๆ + อารมณ์กลางๆ", "#9aa4c4",
                          "ยังไม่มีอะไรเด่นทั้งสองด้าน ใช้เป็นแค่ข้อมูลประกอบ ให้ตัดสินใจจากแนวรับ/แนวต้านและข่าวเป็นหลัก"),
        ("mid", "greed"): ("พื้นฐานกลางๆ + ฝูงชนโลภ", "#ff7a45",
                           "ราคากำลังร้อนแรงโดยที่ธุรกิจไม่ได้แข็งแรงเป็นพิเศษ ถ้าเข้าไปเล่นตามกระแส ต้องพร้อมออกเร็วเมื่อกระแสเปลี่ยน"),
        ("weak", "fear"): ("พื้นฐานอ่อน + ฝูงชนกลัว", "#ff7a45",
                           "ความกลัวอาจมีเหตุผล อย่าเพิ่งมองว่า \"ราคาถูก\" ธุรกิจที่อ่อนแอแล้วราคาตกต่อได้อีก"),
        ("weak", "calm"): ("พื้นฐานอ่อน + อารมณ์กลางๆ", "#ff7a45",
                           "ธุรกิจยังไม่แข็งแรง และไม่มีสัญญาณอารมณ์ช่วยจับจังหวะ ควรระวัง"),
        ("weak", "greed"): ("พื้นฐานอ่อน + ฝูงชนโลภ", "#ff2a6d",
                            "คู่ที่เสี่ยงที่สุด: ราคาถูกดันด้วยความโลภมากกว่าตัวธุรกิจ ถ้ากระแสหมดอาจลงแรง ระวังเป็นพิเศษ"),
    }
    return T[(fk, mk)]


def render_stock_mood(ticker, info):
    info = info or {}
    st.markdown('<div class="section-label">◆ อารมณ์ฝูงชน + พื้นฐาน — %s</div>' % _e(ticker), unsafe_allow_html=True)
    try:
        d = _stock_inputs(ticker)
    except Exception as e:
        st.caption("ดึงข้อมูลอารมณ์ฝูงชนไม่ได้: " + str(e))
        d = {}

    cells, scores = [], []
    if "rsi" in d:
        s = _interp(d["rsi"], [(25, 0), (50, 50), (75, 100)])
        note = _rsi_note(d["rsi"])
        cells.append(_cell("RSI 14 วัน", "%.0f" % d["rsi"], s, note))
        scores.append(s)
    if "dd_pct" in d:
        s = _clamp(100 + 4 * d["dd_pct"])
        note = ("ราคาอยู่ใกล้จุดสูงสุดของปีนี้ คนส่วนใหญ่มั่นใจ" if d["dd_pct"] > -3 else ("ราคาตกลงมาลึกจากจุดสูงสุด คนเริ่มหมดความเชื่อมั่น" if d["dd_pct"] < -20 else "ราคาย่อลงมา %.0f%% จากจุดสูงสุดของปีนี้ ยังไม่ลึกมาก" % abs(d["dd_pct"]))) + "|ดูว่าราคาตอนนี้ต่ำกว่าจุดสูงสุดในรอบ 1 ปีเท่าไร"
        cells.append(_cell("ห่างจากจุดสูงสุด 52 สัปดาห์", "%.1f%%" % d["dd_pct"], s, note))
        scores.append(s)
    if "vol_ratio" in d:
        vr, ch = d["vol_ratio"], d["chg"]
        s = _clamp(50 + _clamp(ch * 6, -30, 30) * min(max(vr, 0.7), 2.0))
        if vr >= 1.5 and ch > 0:
            note = "วันนี้มีคนแห่ซื้อ ปริมาณซื้อขายมากกว่าปกติและราคาขึ้น|ปริมาณสูงผิดปกติ = มีเรื่องที่คนสนใจ ต้องดูคู่กับราคาว่าขึ้นหรือลง"
        elif vr >= 1.5 and ch < 0:
            note = "วันนี้มีคนแห่ขาย ปริมาณซื้อขายมากกว่าปกติและราคาลง|ปริมาณสูงผิดปกติ = มีเรื่องที่คนสนใจ ต้องดูคู่กับราคาว่าขึ้นหรือลง"
        else:
            note = "ปริมาณซื้อขายใกล้เคียงปกติ ยังไม่มีใครแห่ซื้อหรือแห่ขายชัดเจน|ปริมาณสูงผิดปกติ = มีเรื่องที่คนสนใจ ต้องดูคู่กับราคาว่าขึ้นหรือลง"
        cells.append(_cell("ปริมาณซื้อขายวันล่าสุด", "%.1f× <small style='color:#9aa4c4'>ของค่าเฉลี่ย 20 วัน · ราคา %+.1f%%</small>" % (vr, ch), s, note))
        scores.append(s)
    if "pc" in d:
        s = _interp(d["pc"], [(0.4, 92), (0.6, 75), (0.8, 55), (1.0, 38), (1.3, 15), (1.8, 4)])
        note = ("คนซื้อ \"ประกันขาลง\" (Put) มากกว่าฝั่งขาขึ้น แปลว่ากลัวราคาตก" if d["pc"] > 1.0 else ("คนเดิมพันขาขึ้น (Call) มากกว่า แปลว่ามั่นใจว่าราคาจะขึ้น" if d["pc"] < 0.6 else "ฝั่งเดิมพันขึ้นและลงสมดุลกัน")) + "|Put/Call เกิน 1 = เดิมพันขาลงมากกว่าขาขึ้น (ดูจากสัญญา options ที่ยังค้างอยู่)"
        cells.append(_cell("Put/Call (สัญญาที่ค้างอยู่)", "%.2f <small style='color:#9aa4c4'>(หมดอายุ %s)</small>" % (d["pc"], _e(d.get("pc_exp", ""))), s, note))
        scores.append(s)
    sp = info.get("shortPercentOfFloat")
    if isinstance(sp, (int, float)) and sp > 0:
        pct = sp * 100
        s = _interp(pct, [(1, 70), (3, 58), (6, 45), (10, 30), (20, 12)])
        note = ("มีคนยืมหุ้นมาขายเยอะ เพราะเชื่อว่าราคาจะลง" if pct >= 10 else ("แทบไม่มีคนเดิมพันว่าราคาจะลง" if pct < 3 else "มีคนเดิมพันขาลงปานกลาง")) + "|Short interest = สัดส่วนหุ้นที่ถูกยืมมาขายเก็งกำไรขาลง ยิ่งสูงยิ่งมีคนมองลบ"
        cells.append(_cell("Short interest", "%.1f%% <small style='color:#9aa4c4'>ของหุ้นที่ซื้อขายได้</small>" % pct, s, note))
        scores.append(s)
    tgt, px = info.get("targetMeanPrice"), info.get("currentPrice", info.get("regularMarketPrice"))
    if isinstance(tgt, (int, float)) and isinstance(px, (int, float)) and px > 0:
        up = (tgt / px - 1) * 100
        s = _interp(up, [(-10, 8), (0, 32), (10, 52), (25, 78), (50, 95)])
        note = ("นักวิเคราะห์มองว่าราคายังขึ้นได้อีกมาก" if up >= 20 else ("นักวิเคราะห์มองว่าราคาตอนนี้สูงกว่าที่ควรจะเป็น" if up < 0 else "นักวิเคราะห์มองว่าราคาใกล้เคียงมูลค่าที่เหมาะสม")) + "|ค่าเฉลี่ยราคาเป้าหมายจากนักวิเคราะห์หลายสำนัก มองไปข้างหน้าราว 12 เดือน"
        cells.append(_cell("ราคาเป้าหมายนักวิเคราะห์", "&#36;%s <small style='color:#9aa4c4'>(%+.0f%% จากราคาตอนนี้)</small>" % (format(tgt, ",.2f"), up), s, note))
        scores.append(s)

    fund_rows, fund_sc = _fund_points(info)

    if not scores and fund_sc is None:
        st.caption("ยังไม่มีข้อมูลพอสำหรับหุ้นตัวนี้ (หุ้นเล็กหรือหุ้นนอกสหรัฐมักมีข้อมูลไม่ครบ)")
        return

    html = _CSS + '<div class="mm-wrap">'
    mood = None
    if scores:
        mood = sum(scores) / len(scores)
        html += _gauge(mood, "อารมณ์ฝูงชนต่อหุ้นตัวนี้ (เฉลี่ย %d ตัวชี้วัด)" % len(scores))
        html += '<div class="mm-grid">' + "".join(cells) + "</div>"
    if fund_sc is not None:
        flab, fcol = _fund_label(fund_sc)
        html += '<div style="margin-top:16px;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap">'
        html += '<span style="font-size:15px;color:#9aa4c4">คะแนนพื้นฐานแบบเร็ว</span>'
        html += '<span style="font-size:26px;font-weight:800;color:%s;font-family:var(--mono,monospace)">%d/100</span>' % (fcol, round(fund_sc))
        html += '<span style="font-size:16px;font-weight:700;color:%s">%s</span></div>' % (fcol, flab)
        html += '<div class="fd-row">'
        for name, val, pts, why in fund_rows:
            mark, mc = ("✓", "#19f5a5") if pts == 2 else (("~", "#fcee0a") if pts == 1 else ("✗", "#ff2a6d"))
            html += '<span class="fd-chip" title="%s"><em style="color:%s">%s</em>%s %s</span>' % (_e(why), mc, mark, _e(name), _e(val))
        html += "</div>"
    if mood is not None:
        title, vcol, text = _verdict(fund_sc, mood)
        html += '<div class="vd" style="--c:%s"><h5>%s</h5><p>%s</p></div>' % (vcol, _e(title), _e(text))
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
    st.caption(
        "คะแนนอารมณ์ 0 = กลัวสุดขีด · 100 = โลภสุดขีด (สีบอกอารมณ์ ไม่ได้บอกว่าดี/ไม่ดี) · "
        "คะแนนพื้นฐานเป็นแบบเร็วจากตัวเลขที่ Yahoo ให้มา ควรเทียบกับหุ้นกลุ่มเดียวกัน (เช่น ธนาคารมีหนี้สูงเป็นปกติ) · "
        "อารมณ์ฝูงชนช่วยบอกว่าตอนนี้ตลาดอยู่ในโซนไหน ไม่ได้ทำนายว่าราคาจะขึ้นหรือลง · ไม่ใช่คำแนะนำซื้อขาย")