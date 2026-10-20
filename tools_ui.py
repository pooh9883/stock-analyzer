# -*- coding: utf-8 -*-
"""
tools_ui.py
===========
เครื่องมือคำนวณ 4 อย่าง (ใช้ได้เลยไม่ต้องล็อกอิน ปรับตัวเลขได้ทุกช่อง):
1) ต้นทุนเฉลี่ย / กำไร-ขาดทุน เมื่อซื้อเพิ่มหรือขายออก
2) รอซื้อที่แนวรับ ประหยัดได้เท่าไหร่ (เป็นบาท) เทียบกับซื้อตอนนี้
3) ขนาดตำแหน่งตามความเสี่ยง (ยอมเสียกี่ % ของพอร์ต)
4) มูลค่าที่เหมาะสมแบบ DCF พร้อมตารางความไว

เรียกใช้จาก app.py:  tools_ui.render_tools()

⚠️ ทุกผลลัพธ์ขึ้นกับตัวเลขที่คุณใส่ DCF โดยเฉพาะไวต่อสมมติฐานมาก ไม่ใช่คำแนะนำซื้อ-ขาย
"""

import pandas as pd
import streamlit as st
import yfinance as yf

import rocket

GOLD, GREEN, RED, TEXT, GREY = "#d4af37", "#3ecf6e", "#e5534b", "#f4f0e6", "#9a9aa8"


def _show_df(df, **kw):
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


@st.cache_data(ttl=600, show_spinner=False)
def _fx() -> float:
    try:
        v = yf.Ticker("THB=X").fast_info.get("lastPrice")
        if v and 20 < float(v) < 60:
            return float(v)
    except Exception:
        pass
    return 35.0


@st.cache_data(ttl=300, show_spinner=False)
def _quote(sym: str):
    try:
        v = yf.Ticker(sym).fast_info.get("lastPrice")
        return float(v) if v else None
    except Exception:
        return None


@st.cache_data(ttl=900, show_spinner=False)
def _levels_row(sym: str):
    daily = rocket.load_daily((sym, "SPY"))
    if sym not in daily or "SPY" not in daily:
        return None
    row = rocket.compute_row(sym, daily[sym], None, daily["SPY"]["Close"].astype(float), None)
    if row:
        row.pop("history", None)
    return row


@st.cache_data(ttl=3600, show_spinner=False)
def _dcf_inputs(sym: str):
    t = yf.Ticker(sym)
    info = {}
    try:
        info = t.info or {}
    except Exception:
        pass
    fcf = None
    try:
        cf = t.cashflow
        if cf is not None and not cf.empty:
            for name in ["Free Cash Flow"]:
                if name in cf.index:
                    s = pd.to_numeric(cf.loc[name], errors="coerce").dropna()
                    if len(s):
                        fcf = float(s.iloc[0])
            if fcf is None and "Operating Cash Flow" in cf.index and "Capital Expenditure" in cf.index:
                o = pd.to_numeric(cf.loc["Operating Cash Flow"], errors="coerce").dropna()
                c = pd.to_numeric(cf.loc["Capital Expenditure"], errors="coerce").dropna()
                if len(o) and len(c):
                    fcf = float(o.iloc[0] + c.iloc[0])  # capex เป็นค่าลบ
    except Exception:
        pass
    if fcf is None and info.get("freeCashflow"):
        fcf = float(info["freeCashflow"])
    debt, cash = info.get("totalDebt") or 0, info.get("totalCash") or 0
    return {
        "fcf": fcf, "shares": info.get("sharesOutstanding"), "net_debt": float(debt) - float(cash),
        "price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "growth": info.get("earningsGrowth") or info.get("revenueGrowth"),
        "name": info.get("shortName", sym),
    }


def dcf_value(fcf0, g1, g2, gt, r, shares, net_debt, years1=5, years2=5):
    """DCF 2 ช่วงการเติบโต + มูลค่าปลายทาง คืน (มูลค่าต่อหุ้น, PV กระแสเงินสด, PV มูลค่าปลายทาง)"""
    if r <= gt:
        raise ValueError("อัตราคิดลดต้องมากกว่าการเติบโตระยะยาว")
    f, pv = fcf0, 0.0
    n = years1 + years2
    for t in range(1, n + 1):
        f *= 1 + (g1 if t <= years1 else g2)
        pv += f / (1 + r) ** t
    tv = f * (1 + gt) / (r - gt)
    pv_tv = tv / (1 + r) ** n
    equity = pv + pv_tv - net_debt
    return equity / shares, pv, pv_tv


# ---------------------------------------------------------------
# 1) ต้นทุนเฉลี่ย / กำไร-ขาดทุน
# ---------------------------------------------------------------
def _tab_position(fx):
    st.caption("คำนวณต้นทุนเฉลี่ยใหม่ถ้าซื้อเพิ่ม และกำไร-ขาดทุนถ้าขายออก (ใส่ค่าธรรมเนียมได้)")
    c1, c2, c3 = st.columns(3)
    sym = c1.text_input("รหัสหุ้น (ไม่บังคับ ใช้ดึงราคาปัจจุบัน)", value="NVDA", key="tl_pos_sym").strip().upper()
    live = _quote(sym) if sym else None
    cur = c2.number_input("ราคาปัจจุบัน ($)", min_value=0.0, value=float(live or 100.0), step=0.5, key=f"tl_pos_cur_{sym}")
    fee = c3.number_input("ค่าธรรมเนียมต่อรายการ (%)", min_value=0.0, value=0.0, step=0.05, key="tl_pos_fee")

    a, b = st.columns(2)
    with a:
        st.markdown("**ที่ถืออยู่ตอนนี้**")
        s0 = st.number_input("จำนวนหุ้น", min_value=0.0, value=10.0, step=1.0, key="tl_s0")
        a0 = st.number_input("ต้นทุนเฉลี่ย ($/หุ้น)", min_value=0.0, value=float(round((live or 100.0) * 0.95, 2)), step=0.5, key=f"tl_a0_{sym}")
    with b:
        st.markdown("**ซื้อเพิ่ม**")
        n1 = st.number_input("จำนวนหุ้นที่ซื้อเพิ่ม", min_value=0.0, value=5.0, step=1.0, key="tl_n1")
        p1 = st.number_input("ราคาที่ซื้อเพิ่ม ($)", min_value=0.0, value=float(cur), step=0.5, key=f"tl_p1_{sym}")

    cost0 = s0 * a0
    cost1 = n1 * p1 * (1 + fee / 100)
    tot_s = s0 + n1
    new_avg = (cost0 + cost1) / tot_s if tot_s else 0.0
    pl = (cur - new_avg) * tot_s
    pl_pct = (cur / new_avg - 1) * 100 if new_avg else 0.0
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ต้นทุนเฉลี่ยใหม่", f"${new_avg:,.2f}", f"{(new_avg / a0 - 1) * 100:+.1f}% เทียบเดิม" if a0 else None, delta_color="inverse")
    m2.metric("จำนวนหุ้นรวม", f"{tot_s:,.2f}")
    m3.metric("เงินลงทุนรวม", f"${cost0 + cost1:,.0f}", f"≈ ฿{(cost0 + cost1) * fx:,.0f}", delta_color="off")
    m4.metric("กำไร/ขาดทุนที่ราคาปัจจุบัน", f"${pl:,.0f}", f"{pl_pct:+.1f}% · ≈ ฿{pl * fx:,.0f}")
    st.caption("ราคาที่ต้องขึ้นไปถึงเพื่อเท่าทุน (รวมค่าธรรมเนียมขาย): "
               f"**${new_avg * (1 + fee / 100):,.2f}**")

    st.markdown("**ถ้าขายออก**")
    d1, d2 = st.columns(2)
    n_sell = d1.number_input("จำนวนหุ้นที่ขาย", min_value=0.0, max_value=float(max(tot_s, 0.0)), value=min(5.0, float(tot_s)), step=1.0, key="tl_nsell")
    p_sell = d2.number_input("ราคาที่ขาย ($)", min_value=0.0, value=float(cur), step=0.5, key=f"tl_psell_{sym}")
    realized = (p_sell * (1 - fee / 100) - new_avg) * n_sell
    r1, r2, r3 = st.columns(3)
    r1.metric("กำไร/ขาดทุนที่รับรู้", f"${realized:,.0f}", f"≈ ฿{realized * fx:,.0f}")
    r2.metric("หุ้นที่เหลือ", f"{tot_s - n_sell:,.2f}")
    r3.metric("ต้นทุนเฉลี่ยที่เหลือ", f"${new_avg:,.2f}", help="การขายบางส่วนไม่เปลี่ยนต้นทุนเฉลี่ยต่อหุ้นที่เหลือ")


# ---------------------------------------------------------------
# 2) รอซื้อที่แนวรับ
# ---------------------------------------------------------------
def _tab_wait(fx):
    st.caption("ถ้ารอซื้อที่แนวรับแทนซื้อตอนนี้ จะประหยัดได้เท่าไหร่ และถ้าราคาไม่ลงมาจะเสียอะไร")
    c1, c2 = st.columns(2)
    sym = c1.text_input("รหัสหุ้น", value="NVDA", key="tl_wait_sym").strip().upper()
    budget = c2.number_input("งบที่จะลงทุน (บาท)", min_value=1000.0, value=100000.0, step=5000.0, key="tl_wait_budget")
    if not sym:
        return
    with st.spinner("กำลังคำนวณแนวรับ..."):
        row = _levels_row(sym)
    if not row:
        st.warning("ดึงข้อมูลหุ้นตัวนี้ไม่ได้ (ตรวจรหัสหุ้น)")
        return
    live = _quote(sym)
    price = live or row["price"]
    sups = sorted([x for x in row["levels"] if x["kind"] == "support" and x["strength"] >= 2.0 and x["price"] < price],
                  key=lambda x: -x["price"])[:3]
    ress = sorted([x for x in row["levels"] if x["kind"] == "resistance" and x["strength"] >= 2.0], key=lambda x: x["price"])[:1]
    if not sups:
        st.info("ไม่พบแนวรับที่ชัดเจนใต้ราคาปัจจุบัน")
        return

    budget_usd = budget / fx
    shares_now = budget_usd / price
    rows = []
    for x in sups:
        sp = x["price"]
        shares_s = budget_usd / sp
        rows.append({
            "แนวรับ ($)": round(sp, 2),
            "ห่างจากราคาตอนนี้": f"{(sp / price - 1) * 100:.1f}%",
            "ความแข็ง": rocket.strength_label(x["strength"]),
            "ประหยัดได้ (หุ้นจำนวนเท่าเดิม)": f"฿{shares_now * (price - sp) * fx:,.0f}",
            "ได้หุ้นเพิ่มขึ้น (งบเท่าเดิม)": f"+{(price / sp - 1) * 100:.1f}%  ({shares_s:,.2f} vs {shares_now:,.2f})",
            "ประกอบด้วย": x["label"],
        })
    st.markdown(f"ราคาตอนนี้ **${price:,.2f}** · งบ ฿{budget:,.0f} ≈ ${budget_usd:,.0f} · ซื้อตอนนี้ได้ **{shares_now:,.2f} หุ้น** (อัตรา {fx:.2f} บาท/ดอลลาร์)")
    _show_df(pd.DataFrame(rows), hide_index=True)

    if ress:
        rp = ress[0]["price"]
        miss = shares_now * (rp - price) * fx
        st.warning(
            f"⚠️ **ด้านกลับของการรอ:** ถ้าราคาไม่ลงมาแตะแนวรับ แต่ขึ้นไปแนวต้านที่ ${rp:,.2f} แทน "
            f"คุณจะพลาดกำไรราว ฿{miss:,.0f} (ถ้าซื้อตอนนี้) · และถ้าราคา **หลุด** แนวรับลงไปอีก การรอก็ยังไม่การันตีว่าซื้อได้ถูกกว่าตอนหลุด"
        )
    st.caption("แนวรับเป็นโซนที่ราคาเคยมีปฏิกิริยา ไม่ใช่เส้นที่ราคาจะหยุดแน่นอน · ทางลดความเสี่ยงคือทยอยซื้อเป็นงวด เช่น ครึ่งหนึ่งตอนนี้ อีกครึ่งที่แนวรับ")


# ---------------------------------------------------------------
# 3) ขนาดตำแหน่งตามความเสี่ยง
# ---------------------------------------------------------------
def _tab_risk(fx):
    st.caption("กำหนดก่อนซื้อว่ายอมเสียกี่ % ของพอร์ตถ้าผิดทาง แล้วให้สูตรบอกว่าซื้อได้กี่หุ้น")
    c1, c2, c3 = st.columns(3)
    acct = c1.number_input("เงินในพอร์ต (บาท)", min_value=1000.0, value=500000.0, step=10000.0, key="tl_risk_acct")
    risk_pct = c2.number_input("ยอมเสียได้ต่อครั้ง (% ของพอร์ต)", min_value=0.1, max_value=10.0, value=1.0, step=0.1, key="tl_risk_pct")
    fee = c3.number_input("ค่าธรรมเนียมต่อรายการ (%)", min_value=0.0, value=0.0, step=0.05, key="tl_risk_fee")
    d1, d2, d3 = st.columns(3)
    entry = d1.number_input("ราคาเข้าซื้อ ($)", min_value=0.01, value=100.0, step=0.5, key="tl_risk_entry")
    stop = d2.number_input("ราคายอมขาดทุน / Stop ($)", min_value=0.0, value=95.0, step=0.5, key="tl_risk_stop")
    target = d3.number_input("ราคาเป้าหมาย ($)", min_value=0.0, value=112.0, step=0.5, key="tl_risk_target")

    if stop >= entry:
        st.warning("ราคา Stop ต้องต่ำกว่าราคาเข้าซื้อ")
        return
    risk_usd = acct / fx * risk_pct / 100
    per_share_loss = (entry - stop) + entry * fee / 100 * 2
    shares = risk_usd / per_share_loss
    value = shares * entry
    pct_acct = value / (acct / fx) * 100
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ซื้อได้", f"{shares:,.1f} หุ้น")
    m2.metric("มูลค่าตำแหน่ง", f"${value:,.0f}", f"≈ ฿{value * fx:,.0f}", delta_color="off")
    m3.metric("คิดเป็นของพอร์ต", f"{pct_acct:.0f}%")
    m4.metric("เสียสูงสุดถ้าแตะ Stop", f"฿{risk_usd * fx:,.0f}", f"-{risk_pct:.1f}% ของพอร์ต", delta_color="inverse")
    if target > entry:
        rr = (target - entry) / (entry - stop)
        gain = shares * (target - entry) * fx
        (st.success if rr >= 2 else st.info)(f"R:R = {rr:.1f} · ถ้าถึงเป้าหมายได้กำไรราว ฿{gain:,.0f}" + ("" if rr >= 2 else " (ต่ำกว่า 2 ผลตอบแทนไม่ค่อยคุ้มความเสี่ยง)"))
    if pct_acct > 40:
        st.warning("⚠️ ตำแหน่งนี้ใหญ่เกิน 40% ของพอร์ต แม้จะจำกัดการขาดทุนด้วย Stop แต่ราคาอาจกระโดดข้าม Stop (gap) ได้ ควรกระจายหลายตัว")
    st.caption("Stop ไม่การันตีว่าจะขายได้ที่ราคานั้นเสมอ (เช่นข่าวหลังตลาดปิดทำให้เปิดต่ำกว่า Stop) · ตั้ง Stop ตามแนวรับที่ราคาไม่ควรหลุด ไม่ใช่ตามจำนวนเงินที่อยากเสีย")


# ---------------------------------------------------------------
# 4) DCF
# ---------------------------------------------------------------
def _tab_dcf(fx):
    st.caption("ประเมินมูลค่าที่เหมาะสมจากกระแสเงินสดอิสระ (FCF) ที่คาดว่าจะได้ในอนาคต ปรับสมมติฐานได้เอง")
    sym = st.text_input("รหัสหุ้น", value="AAPL", key="tl_dcf_sym").strip().upper()
    if not sym:
        return
    with st.spinner("กำลังดึงงบการเงิน..."):
        inp = _dcf_inputs(sym)
    if not inp["fcf"] or not inp["shares"]:
        st.warning("ดึงกระแสเงินสดอิสระหรือจำนวนหุ้นไม่ได้ ใส่ค่าเองด้านล่างได้")
    fcf_def = (inp["fcf"] or 1e9) / 1e9
    st.markdown(f"**{inp['name']}** · FCF ปีล่าสุด {'' if inp['fcf'] else '(ไม่พบ) '}{fcf_def:,.2f} พันล้านดอลลาร์ · หนี้สุทธิ {inp['net_debt']/1e9:,.1f} พันล้าน · หุ้น {((inp['shares'] or 1e9)/1e9):,.2f} พันล้านหุ้น")

    a, b, c = st.columns(3)
    fcf0 = a.number_input("FCF ปีล่าสุด (พันล้านดอลลาร์)", value=float(round(fcf_def, 2)), step=0.5, key=f"tl_dcf_fcf_{sym}") * 1e9
    shares = b.number_input("จำนวนหุ้น (พันล้านหุ้น)", min_value=0.001, value=float(round((inp["shares"] or 1e9) / 1e9, 3)), step=0.1, key=f"tl_dcf_sh_{sym}") * 1e9
    net_debt = c.number_input("หนี้สุทธิ (พันล้านดอลลาร์ ติดลบ = เงินสดเหลือ)", value=float(round(inp["net_debt"] / 1e9, 2)), step=1.0, key=f"tl_dcf_nd_{sym}") * 1e9

    g_def = inp["growth"]
    g_def = 10.0 if g_def is None else max(0.0, min(30.0, float(g_def) * 100))
    g1 = st.slider("การเติบโต FCF ต่อปี ปีที่ 1-5 (%)", -10.0, 40.0, float(round(g_def)), 0.5, key=f"tl_dcf_g1_{sym}")
    g2 = st.slider("การเติบโต FCF ต่อปี ปีที่ 6-10 (%)", -5.0, 25.0, float(round(g_def / 2)), 0.5, key=f"tl_dcf_g2_{sym}")
    e, f, g = st.columns(3)
    gt = e.slider("เติบโตระยะยาว (%)", 0.0, 4.0, 2.5, 0.1, key="tl_dcf_gt")
    r = f.slider("อัตราคิดลด (%)", 5.0, 15.0, 9.0, 0.5, key="tl_dcf_r")
    mos = g.slider("ส่วนเผื่อความปลอดภัย (%)", 0, 50, 20, 5, key="tl_dcf_mos")

    if fcf0 <= 0:
        st.error("FCF ติดลบหรือเป็นศูนย์ DCF แบบนี้ใช้ไม่ได้ (ธุรกิจยังเผาเงินสด) ลองใช้เครื่องมืออื่นแทน เช่น P/S หรือดูเส้นทางสู่กำไร")
        return
    try:
        val, pv, pv_tv = dcf_value(fcf0, g1 / 100, g2 / 100, gt / 100, r / 100, shares, net_debt)
    except ValueError as ex:
        st.error(str(ex))
        return

    price = _quote(sym) or inp["price"]
    m1, m2, m3 = st.columns(3)
    m1.metric("มูลค่าที่ประเมิน/หุ้น", f"${val:,.2f}", f"≈ ฿{val * fx:,.0f}", delta_color="off")
    buy_under = val * (1 - mos / 100)
    m2.metric(f"ราคาซื้อที่เผื่อ {mos}%", f"${buy_under:,.2f}")
    if price:
        diff = (val / price - 1) * 100
        m3.metric("ราคาปัจจุบัน", f"${price:,.2f}", f"มูลค่าสูงกว่าราคา {diff:+.0f}%", delta_color="normal")
        if price <= buy_under:
            st.success(f"ราคาปัจจุบันต่ำกว่าราคาซื้อที่เผื่อ {mos}% ตามสมมติฐานนี้ (แต่ถ้าสมมติฐานเกินจริง ผลนี้ก็เกินจริง)")
        elif price <= val:
            st.info("ราคาต่ำกว่ามูลค่าที่ประเมิน แต่ยังไม่มีส่วนเผื่อความปลอดภัยตามที่ตั้งไว้")
        else:
            st.warning("ราคาปัจจุบันสูงกว่ามูลค่าที่ประเมินตามสมมติฐานนี้ ตลาดคาดหวังการเติบโตมากกว่าที่คุณใส่")
    st.caption(f"สัดส่วนมูลค่าที่มาจากปลายทาง (ปีที่ 10 เป็นต้นไป): {pv_tv / (pv + pv_tv) * 100:.0f}% ยิ่งสูงยิ่งพึ่งสมมติฐานระยะไกลที่เดายาก")

    st.markdown("**ตารางความไว: มูลค่าต่อหุ้น ($) เมื่อเปลี่ยนอัตราคิดลดและการเติบโตระยะยาว**")
    rs = [r - 2, r - 1, r, r + 1, r + 2]
    gts = [max(0.0, gt - 1), max(0.0, gt - 0.5), gt, gt + 0.5, gt + 1]
    grid = {}
    for rr_ in rs:
        col = {}
        for gg in gts:
            try:
                col[f"โต {gg:.1f}%"] = round(dcf_value(fcf0, g1 / 100, g2 / 100, gg / 100, rr_ / 100, shares, net_debt)[0], 2)
            except ValueError:
                col[f"โต {gg:.1f}%"] = None
        grid[f"คิดลด {rr_:.1f}%"] = col
    _show_df(pd.DataFrame(grid).T)
    st.warning("DCF ไวต่อสมมติฐานมาก เปลี่ยนอัตราคิดลดแค่ 1% มูลค่าก็เปลี่ยนมาก ดูตารางด้านบน ใช้เป็น 'ช่วงที่เป็นไปได้' ไม่ใช่ราคาที่แน่นอน และ FCF ปีล่าสุดอาจไม่ใช่ตัวแทนอนาคต (เช่นปีที่ลงทุนหนักหรือมีรายการพิเศษ)")


def render_tools():
    with st.expander("📖 เครื่องมือเหล่านี้ใช้ยังไง", expanded=False):
        st.markdown(
            """
เครื่องมือ 4 ตัว ใช้ตอนที่เลือกหุ้นได้แล้ว และอยากวางแผนเงิน:
1. **ต้นทุน/กำไร** ซื้อเพิ่มแล้วต้นทุนเฉลี่ยเป็นเท่าไหร่ ต้องขึ้นไปที่ราคาไหนถึงเท่าทุน
2. **รอที่แนวรับ** ถ้ารอซื้อที่แนวรับแทนซื้อตอนนี้ ประหยัดได้กี่บาท (พร้อมด้านที่อาจเสียถ้าราคาไม่ลงมา)
3. **ขนาดตำแหน่ง** ตั้งว่ายอมเสียกี่ % ของพอร์ต แล้วสูตรบอกว่าซื้อกี่หุ้น
4. **DCF** ประเมินมูลค่าจากกระแสเงินสด พร้อมตารางว่าสมมติฐานเปลี่ยนแล้วมูลค่าเปลี่ยนแค่ไหน

ผลลัพธ์ทั้งหมดขึ้นกับตัวเลขที่คุณใส่ ปรับได้ทุกช่อง · ไม่ใช่คำแนะนำซื้อ-ขาย
"""
        )
    fx = st.number_input("อัตราแลกเปลี่ยน (บาท/ดอลลาร์)", min_value=20.0, max_value=60.0, value=float(round(_fx(), 2)), step=0.05, key="tl_fx")
    t1, t2, t3, t4 = st.tabs(["💱 ต้นทุน/กำไร", "🎯 รอที่แนวรับ", "📏 ขนาดตำแหน่ง", "💎 DCF"])
    with t1:
        _tab_position(fx)
    with t2:
        _tab_wait(fx)
    with t3:
        _tab_risk(fx)
    with t4:
        _tab_dcf(fx)
    st.caption("ไม่ใช่คำแนะนำการลงทุน การลงทุนมีความเสี่ยง ผู้ลงทุนต้องมีความรู้ความเข้าใจในการลงทุน")