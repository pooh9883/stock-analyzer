# -*- coding: utf-8 -*-
"""
drivers.py
==========
"ปัจจัยที่ทำให้หุ้นขึ้นหรือลง" 10 หัวข้อ แต่ละหัวข้อสรุปเป็นสถานะ หนุน / กลาง / กด พร้อมคำอธิบายภาษาง่าย

ตัวบริษัท     : กำไรสุทธิ & EPS · P/E · เงินปันผล · การจัดการหุ้น (buyback/ออกหุ้นเพิ่ม/insider)
เงินไหล+เทคนิค : Fund Flow (ตัวแทน) · Technical Indicators
เศรษฐกิจมหภาค : อัตราดอกเบี้ยนโยบาย · เงินเฟ้อ (CPI/PCE) · GDP · อัตราว่างงาน (ข้อมูลจาก FRED)

⚠️ ข้อจำกัดสำคัญ:
- ข้อมูลฟรี (Yahoo/FRED) อาจดีเลย์ และบางหุ้นไม่มีข้อมูลครบทุกหัวข้อ (จะขึ้น "ไม่มีข้อมูล")
- Fund Flow จริง (เงินไหลเข้า-ออกกองทุน) ไม่มีฟรี จึงใช้ตัวแทน: Chaikin Money Flow, OBV, สถาบันถือเพิ่ม/ลด
- เกณฑ์หนุน/กลาง/กดเป็นกฎหัวแม่มือ ไม่ใช่การทำนายว่าหุ้นจะขึ้นหรือลง
- ปัจจัยมหภาคเหมือนกันทุกหุ้น แต่กระทบแต่ละกลุ่มไม่เท่ากัน (หุ้นเติบโต/เทคโนโลยีไวต่อดอกเบี้ยมากกว่า)
"""

import io
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd
import yfinance as yf

STATUS_TH = {"good": "หนุน", "mid": "กลาง", "bad": "กด", "na": "ไม่มีข้อมูล"}

# ใช้ทั้งในหน้าสอน (UI) และไว้อ้างอิง
FACTOR_GUIDE = [
    ("eps", "กำไรสุทธิ & EPS", "กำไรโตต่อเนื่อง ชนะประมาณการนักวิเคราะห์", "กำไรหด ขาดทุน หรือแพ้ประมาณการ"),
    ("pe", "P/E (ราคาเทียบกำไร)", "ถูกเทียบกลุ่มเดียวกัน/เทียบการเติบโต (PEG ต่ำ)", "แพงเกินการเติบโต ผิดหวังนิดเดียวราคาลงแรง"),
    ("dividend", "เงินปันผล", "จ่ายสม่ำเสมอ โตต่อเนื่อง จ่ายไม่เกินกำไร", "ลดปันผล หรือจ่ายเกินกำไรที่หาได้"),
    ("shares", "การจัดการหุ้น", "ซื้อหุ้นคืน (จำนวนหุ้นลดลง) ผู้บริหารซื้อเพิ่ม", "ออกหุ้นเพิ่มจนเจือจาง ผู้บริหารขายต่อเนื่อง"),
    ("flow", "Fund Flow (เงินไหล)", "เงินไหลเข้า สถาบันถือเพิ่ม ปริมาณหนุนราคา", "เงินไหลออก สถาบันลดการถือ"),
    ("technical", "Technical Indicators", "RSI/MACD/ค่าเฉลี่ยชี้ขึ้นพร้อมกัน", "หลายตัวชี้ลง หรือร้อนเกินไปแล้ว"),
    ("rate", "ดอกเบี้ยนโยบาย", "ธนาคารกลางลดดอกเบี้ย", "ขึ้นดอกเบี้ย (กดหุ้นเติบโตแรงสุด)"),
    ("inflation", "เงินเฟ้อ CPI/PCE", "เงินเฟ้อลดลงใกล้เป้า 2%", "เงินเฟ้อสูงและยังไม่ลด (ธนาคารกลางต้องคงดอกเบี้ยสูง)"),
    ("gdp", "เศรษฐกิจโต (GDP)", "โตต่อเนื่อง กำไรบริษัทมักโตตาม", "หดตัว/ใกล้ถดถอย"),
    ("unemployment", "อัตราว่างงาน", "ต่ำและนิ่ง = คนมีงานทำ ใช้จ่ายต่อ", "ว่างงานพุ่งเร็ว (สัญญาณถดถอย)"),
]


# ---------------------------------------------------------------
# ตัวช่วย
# ---------------------------------------------------------------
def _factor(key, group, icon, name, status, headline, meaning, details=None, chart=None, table=None):
    return {
        "key": key, "group": group, "icon": icon, "name": name, "status": status,
        "headline": headline, "meaning": meaning, "details": details or [],
        "chart": chart, "table": table,
    }


def _na(key, group, icon, name, reason):
    return _factor(key, group, icon, name, "na", "ไม่มีข้อมูล", reason)


def _f(x):
    try:
        v = float(x)
        return None if np.isnan(v) else v
    except Exception:
        return None


def _money(x) -> str:
    x = float(x)
    a = abs(x)
    if a >= 1e9:
        return f"{x/1e9:,.2f} พันล้านดอลลาร์"
    if a >= 1e6:
        return f"{x/1e6:,.1f} ล้านดอลลาร์"
    return f"{x:,.0f} ดอลลาร์"


def _row(df, names):
    if df is None or getattr(df, "empty", True):
        return None
    for n in names:
        if n in df.index:
            s = pd.to_numeric(df.loc[n], errors="coerce").dropna()
            if len(s):
                s.index = pd.to_datetime(s.index)
                return s.sort_index()
    return None


def _qlabel(ts) -> str:
    ts = pd.Timestamp(ts)
    return f"{ts.year}-Q{(ts.month - 1) // 3 + 1}"


def _rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    gain = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + gain / loss.replace(0, np.nan))


# ===============================================================
# ตัวบริษัท
# ===============================================================
def _factor_eps(t, info):
    G, I, N = "company", "💰", "กำไรสุทธิ & EPS"
    q = None
    try:
        q = t.quarterly_income_stmt
    except Exception:
        pass
    ni = _row(q, ["Net Income", "Net Income Common Stockholders"])
    eps = _row(q, ["Diluted EPS", "Basic EPS"])

    ni_yoy = eps_yoy = None
    if ni is not None and len(ni) >= 5 and ni.iloc[-5] != 0:
        ni_yoy = (ni.iloc[-1] - ni.iloc[-5]) / abs(ni.iloc[-5]) * 100
    if eps is not None and len(eps) >= 5 and eps.iloc[-5] != 0:
        eps_yoy = (eps.iloc[-1] - eps.iloc[-5]) / abs(eps.iloc[-5]) * 100
    if ni_yoy is None:
        eg = _f(info.get("earningsGrowth"))
        ni_yoy = None if eg is None else eg * 100

    growth = eps_yoy if eps_yoy is not None else ni_yoy
    last_ni = None if ni is None else float(ni.iloc[-1])
    if last_ni is None:
        pm = _f(info.get("profitMargins"))
        loss = pm is not None and pm < 0
    else:
        loss = last_ni <= 0

    if growth is None and last_ni is None:
        return _na("eps", G, I, N, "ดึงงบรายไตรมาสไม่ได้ (บางหุ้นหรือบางช่วงเวลา Yahoo ไม่ส่งข้อมูล)")

    if loss:
        status, meaning = "bad", "บริษัทยังขาดทุนสุทธิ ราคาหุ้นพึ่งความหวังในอนาคตมากกว่ากำไรจริง เสี่ยงผันผวนสูง"
    elif growth is not None and growth >= 10:
        status, meaning = "good", "กำไรโตเร็วกว่าปีก่อนชัดเจน กำไรที่โตคือแรงหนุนราคาระยะยาวที่แข็งแรงที่สุด"
    elif growth is not None and growth >= -10:
        status, meaning = "mid", "กำไรทรงตัว ไม่ได้โตและไม่ได้หด ราคาจึงต้องพึ่งปัจจัยอื่นช่วย"
    else:
        status, meaning = "bad", "กำไรหดลงเทียบปีก่อน มักกดดันราคา เว้นแต่ตลาดมองว่าเป็นแค่ชั่วคราว"

    parts = []
    if eps is not None:
        parts.append(f"EPS ล่าสุด {eps.iloc[-1]:.2f}" + (f" ({eps_yoy:+.0f}% เทียบปีก่อน)" if eps_yoy is not None else ""))
    if last_ni is not None:
        parts.append(f"กำไรสุทธิ {_money(last_ni)}" + (f" ({ni_yoy:+.0f}%)" if ni_yoy is not None else ""))
    headline = " · ".join(parts) if parts else (f"กำไรโต {growth:+.0f}%" if growth is not None else "-")

    details = []
    te, fe = _f(info.get("trailingEps")), _f(info.get("forwardEps"))
    if te and fe and te > 0 and fe > 0:
        details.append(f"EPS 12 เดือนล่าสุด {te:.2f} → ประมาณการปีหน้า {fe:.2f} ({(fe/te-1)*100:+.0f}% นักวิเคราะห์คาดว่าจะโต)")
    try:
        eh = t.earnings_history
        if eh is not None and not eh.empty and {"epsActual", "epsEstimate"} <= set(eh.columns):
            last4 = eh.tail(4)
            beats = int((last4["epsActual"] > last4["epsEstimate"]).sum())
            details.append(f"ชนะประมาณการนักวิเคราะห์ {beats}/{len(last4)} ไตรมาสล่าสุด")
    except Exception:
        pass
    details.append("วิธีดู: ดูว่ากำไรโตขึ้นต่อเนื่องหลายไตรมาสไหม และชนะประมาณการไหม ราคามักตอบสนองต่อ 'ต่างจากที่คาด' มากกว่าตัวเลขกำไรเอง")

    chart = None
    if eps is not None and len(eps) >= 2:
        chart = {"kind": "bar", "title": "EPS รายไตรมาส",
                 "df": pd.DataFrame({"EPS": eps.values}, index=[_qlabel(i) for i in eps.index])}
    return _factor("eps", G, I, N, status, headline, meaning, details, chart)


def _peer_forward_pe(info, ticker):
    try:
        key = info.get("sectorKey")
        if not key:
            return None
        top = yf.Sector(key).top_companies
        vals = []
        for sym in [str(x) for x in list(top.index)[:7] if str(x).upper() != ticker.upper()][:6]:
            try:
                v = _f(yf.Ticker(sym).info.get("forwardPE"))
                if v and 0 < v < 200:
                    vals.append(v)
            except Exception:
                continue
        return float(np.median(vals)) if len(vals) >= 3 else None
    except Exception:
        return None


def _factor_pe(info, ticker, include_peers=True):
    G, I, N = "company", "🏷️", "P/E (ราคาเทียบกำไร)"
    tpe, fpe = _f(info.get("trailingPE")), _f(info.get("forwardPE"))
    peg = _f(info.get("trailingPegRatio")) or _f(info.get("pegRatio"))
    ps, pb = _f(info.get("priceToSalesTrailing12Months")), _f(info.get("priceToBook"))

    if not tpe and not fpe:
        return _factor("pe", G, I, N, "bad", "ไม่มี P/E",
                       "บริษัทยังไม่มีกำไรให้เทียบ ราคาตั้งอยู่บนความคาดหวังล้วน ๆ", 
                       ["วิธีดู: ถ้าไม่มี P/E ให้ดู P/S (ราคาเทียบยอดขาย) และดูว่าเมื่อไหร่จะเริ่มมีกำไร"])
    peer = _peer_forward_pe(info, ticker) if (include_peers and fpe and fpe > 0) else None

    status, meaning = "mid", "ราคาอยู่ในระดับไม่ถูกไม่แพงเมื่อเทียบกับเกณฑ์ที่ใช้"
    basis = ""
    if peer and fpe and fpe > 0:
        ratio = fpe / peer
        basis = f"เทียบ P/E ปีหน้าของหุ้นใหญ่ในกลุ่มเดียวกัน (มัธยฐาน {peer:.1f})"
        if ratio <= 0.85:
            status, meaning = "good", "ถูกกว่าหุ้นใหญ่ในกลุ่มเดียวกันพอสมควร (แต่ต้องดูว่าถูกเพราะอะไร ไม่ใช่ถูกเพราะธุรกิจแย่)"
        elif ratio <= 1.25:
            status, meaning = "mid", "ราคาใกล้เคียงหุ้นใหญ่ในกลุ่มเดียวกัน"
        else:
            status, meaning = "bad", "แพงกว่าหุ้นใหญ่ในกลุ่มเดียวกันชัดเจน ตลาดคาดหวังสูง ถ้าผิดหวังราคาจะลงแรง"
    elif peg:
        basis = f"ใช้ PEG {peg:.2f} (P/E เทียบการเติบโต)"
        if peg < 1:
            status, meaning = "good", "ราคาถูกเมื่อเทียบกับอัตราการเติบโตของกำไร"
        elif peg <= 2:
            status, meaning = "mid", "ราคาสมเหตุสมผลเมื่อเทียบการเติบโต"
        else:
            status, meaning = "bad", "แพงเมื่อเทียบการเติบโตของกำไร"
    elif tpe and fpe and fpe > 0:
        basis = "เทียบ P/E ปีหน้ากับ P/E ปัจจุบัน"
        if fpe < tpe * 0.8:
            status, meaning = "good", "นักวิเคราะห์คาดกำไรปีหน้าโตแรง ทำให้ P/E ปีหน้าต่ำลง (เป็นแค่ประมาณการ)"
        elif fpe > tpe * 1.1:
            status, meaning = "bad", "P/E ปีหน้าสูงกว่าปัจจุบัน แปลว่าคาดกำไรลดลง"

    head = []
    if tpe:
        head.append(f"P/E ปัจจุบัน {tpe:.1f}")
    if fpe:
        head.append(f"P/E ปีหน้า {fpe:.1f}")
    if peg:
        head.append(f"PEG {peg:.2f}")
    details = [basis] if basis else []
    if ps:
        details.append(f"ราคา/ยอดขาย (P/S) {ps:.1f}")
    if pb:
        details.append(f"ราคา/มูลค่าบัญชี (P/B) {pb:.1f}")
    details.append("วิธีดู: P/E ต่ำไม่ได้แปลว่าน่าซื้อเสมอ อาจต่ำเพราะตลาดกลัวกำไรจะหด ต้องเทียบกับกลุ่มเดียวกันและดูการเติบโตคู่กัน")
    return _factor("pe", G, I, N, status, " · ".join(head), meaning, details)


def _factor_dividend(t, info):
    G, I, N = "company", "🪙", "เงินปันผล"
    try:
        div = t.dividends
    except Exception:
        div = None
    if div is None or len(div) == 0:
        return _factor("dividend", G, I, N, "mid", "ไม่จ่ายเงินปันผล",
                       "บริษัทเติบโตมักเก็บกำไรไปลงทุนต่อ ไม่ใช่ข้อเสีย แต่ไม่มีเงินปันผลเป็นกันชนเวลาราคาลง",
                       ["วิธีดู: ถ้าสนใจรายได้ประจำให้ดูหุ้นที่จ่ายปันผลสม่ำเสมอและ payout ratio ไม่เกิน ~60%"])
    div = div.copy()
    div.index = pd.to_datetime(div.index).tz_localize(None)
    last_date = div.index.max()
    ttm = float(div[div.index > last_date - pd.Timedelta(days=365)].sum())
    price = _f(info.get("currentPrice")) or _f(info.get("regularMarketPrice")) or _f(info.get("previousClose"))
    yld = ttm / price * 100 if price else None
    payout = _f(info.get("payoutRatio"))

    yearly = div.groupby(div.index.year).sum()
    complete = yearly[yearly.index < pd.Timestamp.today().year]
    cut = False
    cagr = None
    streak = 0
    if len(complete) >= 2:
        cut = float(complete.iloc[-1]) < float(complete.iloc[-2]) * 0.95
        for i in range(len(complete) - 1, 0, -1):
            if float(complete.iloc[i]) >= float(complete.iloc[i - 1]) * 0.999:
                streak += 1
            else:
                break
    if len(complete) >= 4 and float(complete.iloc[-4]) > 0:
        cagr = ((float(complete.iloc[-1]) / float(complete.iloc[-4])) ** (1 / 3) - 1) * 100

    if cut or (payout is not None and payout > 1.0):
        status = "bad"
        meaning = "เคยลดปันผล หรือจ่ายเกินกำไรที่หาได้ ปันผลอาจไม่ยั่งยืน"
    elif payout is not None and payout <= 0.6 and (cagr is None or cagr >= 0):
        status = "good"
        meaning = "จ่ายปันผลโดยใช้กำไรไม่ถึงครึ่ง ยังมีเหลือเติบโตต่อ และปันผลมักโตตามกำไร"
    else:
        status = "mid"
        meaning = "จ่ายปันผลปกติ แต่สัดส่วนการจ่ายหรือการเติบโตยังไม่โดดเด่น"

    head = [f"ปันผลย้อนหลัง 12 เดือน {ttm:.2f}/หุ้น"]
    if yld is not None:
        head.append(f"ผลตอบแทน {yld:.2f}%")
    if payout is not None:
        head.append(f"จ่ายออก {payout*100:.0f}% ของกำไร")
    details = []
    if cagr is not None:
        details.append(f"ปันผลโตเฉลี่ย {cagr:+.1f}% ต่อปี (3 ปีล่าสุด)")
    if streak:
        details.append(f"ไม่ลดปันผลมาแล้วอย่างน้อย {streak} ปี")
    if yld is not None and yld > 6:
        details.append("⚠️ ผลตอบแทนสูงเกิน 6% มักแปลว่าราคาตกมาก ให้ระวังว่าปันผลจะถูกลด")
    details.append("วิธีดู: ปันผลสูงอย่างเดียวไม่พอ ดูว่าจ่ายไม่เกินกำไร และไม่เคยลดปันผล")
    chart = None
    if len(complete) >= 2:
        chart = {"kind": "bar", "title": "ปันผลรายปีต่อหุ้น",
                 "df": pd.DataFrame({"ปันผล/หุ้น": complete.values}, index=[str(i) for i in complete.index])}
    return _factor("dividend", G, I, N, status, " · ".join(head), meaning, details, chart)


def _factor_shares(t, info):
    G, I, N = "company", "🏛️", "การจัดการหุ้น"
    shares = None
    try:
        sf = t.get_shares_full(start=(pd.Timestamp.today() - pd.Timedelta(days=800)).strftime("%Y-%m-%d"))
        if sf is not None and len(sf) > 5:
            sf = pd.to_numeric(sf, errors="coerce").dropna()
            sf.index = pd.to_datetime(sf.index).tz_localize(None)
            shares = sf.sort_index()
    except Exception:
        pass

    chg = None
    if shares is not None and len(shares) > 5:
        now = float(shares.iloc[-1])
        past = shares[shares.index <= shares.index[-1] - pd.Timedelta(days=330)]
        if len(past):
            chg = (now / float(past.iloc[-1]) - 1) * 100

    buyback = None
    try:
        cf = t.quarterly_cashflow
        rep = _row(cf, ["Repurchase Of Capital Stock", "Common Stock Payments"])
        if rep is not None and len(rep) >= 1:
            buyback = -float(rep.tail(4).sum())
    except Exception:
        pass

    if chg is None and buyback is None:
        return _na("shares", G, I, N, "ดึงข้อมูลจำนวนหุ้นไม่ได้")

    if chg is not None and chg <= -1:
        status, meaning = "good", "จำนวนหุ้นลดลง (ซื้อหุ้นคืน) ทำให้กำไรต่อหุ้นสูงขึ้นโดยอัตโนมัติ และสะท้อนว่าผู้บริหารมั่นใจ"
    elif chg is not None and chg >= 2:
        status, meaning = "bad", "ออกหุ้นเพิ่มจนจำนวนหุ้นโตเร็ว ส่วนแบ่งกำไรของผู้ถือเดิมถูกเจือจาง"
    else:
        status, meaning = "mid", "จำนวนหุ้นแทบไม่เปลี่ยน ไม่ได้ช่วยหรือเจือจางกำไรต่อหุ้นมากนัก"

    head = []
    if chg is not None:
        head.append(f"จำนวนหุ้น {chg:+.1f}% ใน 1 ปี")
    if buyback is not None and buyback > 0:
        head.append(f"ซื้อหุ้นคืน {_money(buyback)} (12 เดือน)")
    elif buyback is not None:
        head.append("ไม่มีการซื้อหุ้นคืนชัดเจน")

    details = []
    # insider (best effort — รูปแบบข้อมูลเปลี่ยนตามเวอร์ชัน yfinance)
    try:
        ins = t.insider_transactions
        if ins is not None and not ins.empty:
            text_col = next((c for c in ["Text", "Transaction"] if c in ins.columns), None)
            date_col = next((c for c in ["Start Date", "Date"] if c in ins.columns), None)
            if text_col and date_col:
                d = ins.copy()
                d[date_col] = pd.to_datetime(d[date_col], errors="coerce")
                d = d[d[date_col] >= pd.Timestamp.today() - pd.Timedelta(days=180)]
                txt = d[text_col].astype(str).str.lower()
                buys = int(txt.str.contains("purchase|buy").sum())
                sells = int(txt.str.contains("sale|sell").sum())
                details.append(f"ผู้บริหาร/insider 6 เดือนล่าสุด: ซื้อ {buys} รายการ · ขาย {sells} รายการ (ขายอาจเป็นแผนขายล่วงหน้าตามปกติ)")
    except Exception:
        pass
    si = _f(info.get("shortPercentOfFloat"))
    if si is not None:
        details.append(f"ยอดขายชอร์ต {si*100:.1f}% ของหุ้นที่ซื้อขายได้ (สูงเกิน ~10% = มีคนเดิมพันว่าราคาจะลง)")
    hi, hs = _f(info.get("heldPercentInstitutions")), _f(info.get("heldPercentInsiders"))
    if hi is not None:
        details.append(f"สถาบันถือ {hi*100:.0f}%" + (f" · ผู้บริหารถือ {hs*100:.1f}%" if hs is not None else ""))
    details.append("วิธีดู: จำนวนหุ้นลด = ดี · จำนวนหุ้นเพิ่มเร็ว = ระวัง · ผู้บริหารซื้อด้วยเงินตัวเองคือสัญญาณบวกกว่าการขาย")

    chart = None
    if shares is not None and len(shares) > 5:
        try:
            m = shares.resample("ME").last().dropna()
        except Exception:
            m = shares.resample("M").last().dropna()
        chart = {"kind": "line", "title": "จำนวนหุ้นที่ออกจำหน่าย", "df": pd.DataFrame({"จำนวนหุ้น": m.values}, index=m.index)}
    return _factor("shares", G, I, N, status, " · ".join(head), meaning, details, chart)


def company_drivers(ticker: str, include_peers: bool = True) -> list:
    t = yf.Ticker(ticker)
    info = {}
    try:
        info = t.info or {}
    except Exception:
        pass
    out = []
    for fn, args in [
        (_factor_eps, (t, info)),
        (_factor_pe, (info, ticker, include_peers)),
        (_factor_dividend, (t, info)),
        (_factor_shares, (t, info)),
    ]:
        try:
            out.append(fn(*args))
        except Exception as e:
            key = {"_factor_eps": "eps", "_factor_pe": "pe", "_factor_dividend": "dividend", "_factor_shares": "shares"}[fn.__name__]
            nm = next(n for k, n, _, _ in FACTOR_GUIDE if k == key)
            out.append(_na(key, "company", "•", nm, f"คำนวณไม่ได้ ({e})"))
    return out


# ===============================================================
# เงินไหล + เทคนิค
# ===============================================================
def flow_tech_drivers(ticker: str) -> list:
    G = "flow"
    out = []
    t = yf.Ticker(ticker)
    try:
        h = t.history(period="1y")
    except Exception:
        h = None
    if h is None or h.empty or len(h) < 60:
        reason = "ข้อมูลราคาย้อนหลังไม่พอ"
        return [_na("flow", G, "🌊", "Fund Flow (เงินไหล)", reason), _na("technical", G, "📐", "Technical Indicators", reason)]
    h = h.copy()
    h.index = pd.to_datetime(h.index).tz_localize(None)
    c, hi, lo, v = h["Close"], h["High"], h["Low"], h["Volume"]

    # ----- Fund flow (ตัวแทน) -----
    try:
        rng = (hi - lo).replace(0, np.nan)
        mfm = (((c - lo) - (hi - c)) / rng).fillna(0)
        cmf_series = (mfm * v).rolling(20).sum() / v.rolling(20).sum()
        cmf = _f(cmf_series.iloc[-1])
        obv = (np.sign(c.diff().fillna(0)) * v).cumsum()
        obv_up = float(obv.iloc[-1]) > float(obv.iloc[-21])
        price_up = float(c.iloc[-1]) > float(c.iloc[-21])
        vol_ratio = float(v.tail(5).mean() / v.tail(20).mean()) if v.tail(20).mean() else None

        inst_chg = None
        try:
            ih = t.institutional_holders
            if ih is not None and not ih.empty and "pctChange" in ih.columns:
                w = ih["pctHeld"] if "pctHeld" in ih.columns else pd.Series(1.0, index=ih.index)
                inst_chg = float((ih["pctChange"] * w).sum() / w.sum() * 100)
        except Exception:
            pass

        sigs = []
        if cmf is not None:
            sigs.append(cmf > 0.05 if abs(cmf) > 0.05 else None)
        sigs.append(obv_up)
        if inst_chg is not None:
            sigs.append(inst_chg > 0)
        sigs_ok = [s for s in sigs if s is not None]
        pos = sum(1 for s in sigs_ok if s)
        ratio = pos / len(sigs_ok) if sigs_ok else 0.5
        if ratio >= 0.67:
            status, meaning = "good", "เงินมีแนวโน้มไหลเข้า แรงซื้อชนะแรงขายในช่วงที่ผ่านมา"
        elif ratio <= 0.33:
            status, meaning = "bad", "เงินมีแนวโน้มไหลออก แรงขายชนะแรงซื้อ ราคาอาจอ่อนแรงต่อ"
        else:
            status, meaning = "mid", "สัญญาณเงินไหลผสมกัน ยังไม่ชี้ไปทางใดทางหนึ่ง"

        head = []
        if cmf is not None:
            head.append(f"CMF 20 วัน {cmf:+.2f}")
        head.append("OBV " + ("ขึ้น" if obv_up else "ลง"))
        if inst_chg is not None:
            head.append(f"สถาบันถือ {inst_chg:+.1f}%")
        details = [
            "CMF (Chaikin Money Flow): บวก = ปิดใกล้จุดสูงของวันพร้อมปริมาณ = เงินไหลเข้า · ลบ = เงินไหลออก (เกิน ±0.05 ถึงนับว่าชัด)",
            "OBV: ปริมาณสะสมที่เพิ่มตามวันที่ราคาขึ้น ถ้า OBV ขึ้นขณะที่ราคาขึ้น = ขาขึ้นมีแรงซื้อจริงหนุน",
        ]
        if obv_up != price_up:
            details.append("⚠️ ราคากับ OBV ไปคนละทาง (divergence) มักเป็นสัญญาณเตือนว่าแนวโน้มอาจกลับตัว")
        if vol_ratio is not None:
            details.append(f"ปริมาณซื้อขาย 5 วันล่าสุดเทียบค่าเฉลี่ย 20 วัน = {vol_ratio:.2f} เท่า")
        details.append("หมายเหตุ: Fund Flow จริง (เงินไหลเข้า-ออกกองทุน) ไม่มีข้อมูลฟรี จึงใช้ตัวแทนจากราคา-ปริมาณและการถือครองของสถาบัน")
        chart = {"kind": "line", "title": "CMF 20 วัน (เหนือ 0 = เงินไหลเข้า)",
                 "df": pd.DataFrame({"CMF": cmf_series.dropna().tail(120)})}
        out.append(_factor("flow", G, "🌊", "Fund Flow (เงินไหล)", status, " · ".join(head), meaning, details, chart))
    except Exception as e:
        out.append(_na("flow", G, "🌊", "Fund Flow (เงินไหล)", f"คำนวณไม่ได้ ({e})"))

    # ----- Technical indicators -----
    try:
        last = float(c.iloc[-1])
        rsi = float(_rsi(c).iloc[-1])
        ema12, ema26 = c.ewm(span=12, adjust=False).mean(), c.ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        hist = float((macd - macd.ewm(span=9, adjust=False).mean()).iloc[-1])
        sma50 = float(c.rolling(50).mean().iloc[-1])
        sma200 = float(c.rolling(200).mean().iloc[-1]) if len(c) >= 200 else None
        s20, sd20 = c.rolling(20).mean(), c.rolling(20).std()
        pb = float(((c - (s20 - 2 * sd20)) / (4 * sd20)).iloc[-1])
        lo14, hi14 = lo.rolling(14).min(), hi.rolling(14).max()
        stoch = float(((c - lo14) / (hi14 - lo14) * 100).iloc[-1])
        atr_pct = float((pd.concat([hi - lo, (hi - c.shift()).abs(), (lo - c.shift()).abs()], axis=1).max(axis=1).rolling(14).mean() / c).iloc[-1] * 100)

        rows = []

        def add(name, value, reading, note):
            rows.append({"ตัวชี้วัด": name, "ค่า": value, "อ่านได้ว่า": reading, "ความหมาย": note})

        def tag(sig):
            return {"bull": "🟢 ขึ้น", "bear": "🔴 ลง", "neu": "🟡 กลาง"}[sig]

        sigs = []
        s = "bull" if 50 <= rsi <= 70 else ("bear" if rsi < 40 else "neu")
        sigs.append(s)
        add("RSI 14", f"{rsi:.0f}", tag(s), "ร้อนเกิน (>70) · ปกติแข็ง (50-70) · อ่อน (<40)" + (" · ตอนนี้ร้อนเกิน อาจพักตัว" if rsi > 70 else ""))
        s = "bull" if hist > 0 else "bear"
        sigs.append(s)
        add("MACD", f"{hist:+.2f}", tag(s), "histogram บวก = โมเมนตัมระยะสั้นขึ้น")
        s = "bull" if last > sma50 else "bear"
        sigs.append(s)
        add("ราคา vs SMA50", f"{(last/sma50-1)*100:+.1f}%", tag(s), "เหนือ = แนวโน้มระยะกลางขึ้น")
        if sma200:
            s = "bull" if last > sma200 else "bear"
            sigs.append(s)
            add("ราคา vs SMA200", f"{(last/sma200-1)*100:+.1f}%", tag(s), "เหนือ = ขาขึ้นใหญ่")
        s = "bull" if 0.5 <= pb <= 1.0 else ("bear" if pb < 0.2 else "neu")
        sigs.append(s)
        add("Bollinger %B", f"{pb:.2f}", tag(s), "0.5-1.0 = ครึ่งบนของกรอบ (แข็ง) · เกิน 1 = ราคาวิ่งเกินกรอบ · ต่ำกว่า 0.2 = อ่อน")
        s = "bull" if 50 <= stoch <= 80 else "neu"
        sigs.append(s)
        add("Stochastic %K", f"{stoch:.0f}", tag(s), "เกิน 80 = ร้อน · ต่ำกว่า 20 = ขายมากเกิน (อาจเด้ง)")
        add("ATR (ความแกว่งรายวัน)", f"{atr_pct:.1f}%", "ℹ️ ข้อมูล", "ยิ่งสูง ราคาแกว่งแรงต่อวัน ควรตั้งจุดยอมขาดทุนให้กว้างขึ้น")

        bull, bear = sigs.count("bull"), sigs.count("bear")
        n = len(sigs)
        if bull >= n - 2 and bear <= 1:
            status, meaning = "good", "ตัวชี้วัดส่วนใหญ่ชี้ขึ้นพร้อมกัน แนวโน้มระยะสั้น-กลางเป็นใจ"
        elif bear >= 3:
            status, meaning = "bad", "ตัวชี้วัดหลายตัวชี้ลง แนวโน้มอ่อนแรง"
        else:
            status, meaning = "mid", "ตัวชี้วัดผสมกัน ยังไม่เป็นเอกฉันท์"
        details = ["วิธีดู: อย่าดูตัวเดียว ให้ดูว่าหลายตัวชี้ไปทางเดียวกันไหม · RSI/Stochastic เกินร้อนไม่ได้แปลว่าต้องลงทันที แค่เพิ่มโอกาสพักตัว"]
        out.append(_factor("technical", G, "📐", "Technical Indicators", status,
                           f"ชี้ขึ้น {bull} · กลาง {sigs.count('neu')} · ชี้ลง {bear} (จาก {n} ตัว)", meaning, details,
                           table=pd.DataFrame(rows)))
    except Exception as e:
        out.append(_na("technical", G, "📐", "Technical Indicators", f"คำนวณไม่ได้ ({e})"))
    return out


# ===============================================================
# มหภาค (FRED — ไม่ต้องมี API key)
# ===============================================================
FRED_IDS = {
    "fedfunds": "FEDFUNDS", "cpi": "CPIAUCSL", "core_cpi": "CPILFESL",
    "pce": "PCEPI", "core_pce": "PCEPILFE", "gdp": "A191RL1Q225SBEA", "unrate": "UNRATE",
}


def _fred(series_id: str) -> pd.Series:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=10) as r:
        data = r.read()
    df = pd.read_csv(io.BytesIO(data))
    s = pd.Series(pd.to_numeric(df.iloc[:, 1], errors="coerce").values, index=pd.to_datetime(df.iloc[:, 0]))
    return s.dropna()


def _yoy(s: pd.Series) -> pd.Series:
    return (s / s.shift(12) - 1).dropna() * 100


def _fetch_macro() -> dict:
    def get(item):
        k, sid = item
        try:
            return k, _fred(sid)
        except Exception:
            return k, None

    with ThreadPoolExecutor(max_workers=7) as ex:
        return dict(ex.map(get, FRED_IDS.items()))


def macro_drivers() -> list:
    G = "macro"
    data = _fetch_macro()
    out = []

    # ----- ดอกเบี้ยนโยบาย -----
    ff = data.get("fedfunds")
    I, N = "🏦", "อัตราดอกเบี้ยนโยบาย (Fed Funds)"
    if ff is not None and len(ff) > 8:
        now, past = float(ff.iloc[-1]), float(ff.iloc[-7])
        d = now - past
        if d <= -0.25:
            status, meaning = "good", "ธนาคารกลางกำลังลดดอกเบี้ย ต้นทุนเงินถูกลง มักหนุนหุ้น โดยเฉพาะหุ้นเติบโต/เทคโนโลยี"
        elif d >= 0.25:
            status, meaning = "bad", "ธนาคารกลางกำลังขึ้นดอกเบี้ย ต้นทุนเงินสูงขึ้น มักกดหุ้น โดยเฉพาะหุ้นเติบโตที่ราคาแพง"
        else:
            status = "mid"
            meaning = "ดอกเบี้ยนิ่ง" + (" แต่อยู่ระดับสูง ยังเป็นแรงกดต่อหุ้นราคาแพง" if now >= 4.5 else " ไม่ได้เป็นแรงหนุนหรือกดชัดเจน")
        out.append(_factor("rate", G, I, N, status, f"{now:.2f}% ({d:+.2f} จุดใน 6 เดือน)", meaning,
                           ["วิธีดู: ทิศทางสำคัญกว่าระดับ ตลาดมักวิ่งล่วงหน้าไปก่อนธนาคารกลางจะประกาศจริง (ข้อมูลรายเดือน)"],
                           {"kind": "line", "title": "ดอกเบี้ยนโยบาย 5 ปี (%)", "df": pd.DataFrame({"Fed Funds": ff.tail(60)})}))
    else:
        proxy = None
        try:
            h = yf.Ticker("^IRX").history(period="8mo")["Close"].dropna()
            if len(h) > 100:
                proxy = (float(h.iloc[-1]), float(h.iloc[-1] - h.iloc[-126]))
        except Exception:
            pass
        if proxy:
            now, d = proxy
            status = "good" if d <= -0.25 else ("bad" if d >= 0.25 else "mid")
            meaning = {"good": "ผลตอบแทนระยะสั้นลดลง สะท้อนว่าตลาดคาดดอกเบี้ยลง", "bad": "ผลตอบแทนระยะสั้นสูงขึ้น สะท้อนดอกเบี้ยขาขึ้น", "mid": "ดอกเบี้ยระยะสั้นนิ่ง"}[status]
            out.append(_factor("rate", G, I, N, status, f"ตัวแทน: T-bill 3 เดือน {now:.2f}% ({d:+.2f} จุดใน 6 เดือน)", meaning,
                               ["ดึงข้อมูล Fed Funds จาก FRED ไม่ได้ จึงใช้ผลตอบแทนตั๋วเงินคลัง 3 เดือนเป็นตัวแทน"]))
        else:
            out.append(_na("rate", G, I, N, "ดึงข้อมูลจาก FRED ไม่ได้ (เช็กอินเทอร์เน็ต/ไฟร์วอลล์)"))

    # ----- เงินเฟ้อ -----
    I, N = "🛒", "เงินเฟ้อ (CPI / PCE)"
    infl = {}
    for k, label in [("cpi", "CPI"), ("core_cpi", "Core CPI"), ("pce", "PCE"), ("core_pce", "Core PCE")]:
        s = data.get(k)
        if s is not None and len(s) > 16:
            infl[label] = _yoy(s)
    if infl:
        main_key = "Core PCE" if "Core PCE" in infl else list(infl)[0]
        y = infl[main_key]
        now = float(y.iloc[-1])
        dirn = now - float(y.iloc[-4])
        if now <= 2.5:
            status, meaning = "good", "เงินเฟ้อใกล้เป้า 2% ธนาคารกลางมีที่ว่างจะไม่ขึ้นดอกเบี้ยหรือลดลง เป็นผลดีต่อหุ้น"
        elif now <= 3.5:
            status = "good" if dirn <= -0.3 else "mid"
            meaning = "เงินเฟ้อเหนือเป้าเล็กน้อยแต่" + (" กำลังลดลง เป็นสัญญาณดี" if status == "good" else " ยังไม่ลดชัด ธนาคารกลางยังไม่รีบลดดอกเบี้ย")
        else:
            status = "mid" if dirn <= -0.5 else "bad"
            meaning = "เงินเฟ้อสูง" + (" แต่เริ่มลดเร็ว" if status == "mid" else " และยังไม่ลด ธนาคารกลางต้องคงดอกเบี้ยสูง กดดันหุ้น")
        head = " · ".join(f"{k} {float(v.iloc[-1]):.1f}%" for k, v in infl.items())
        details = [f"ตัวเลขคือเงินเฟ้อเทียบปีก่อน (YoY) · ใช้ {main_key} ตัดสินสถานะ (ธนาคารกลางสหรัฐดู PCE เป็นหลัก)",
                   f"{main_key} เปลี่ยนจาก 3 เดือนก่อน {dirn:+.1f} จุด",
                   "วิธีดู: เงินเฟ้อที่ 'ลดลงเข้าใกล้ 2%' คือข่าวดีต่อหุ้น เพราะดอกเบี้ยมีโอกาสลง"]
        out.append(_factor("inflation", G, I, N, status, head, meaning, details,
                           {"kind": "line", "title": "เงินเฟ้อ YoY 3 ปี (%)", "df": pd.DataFrame({k: v.tail(36) for k, v in infl.items()})}))
    else:
        out.append(_na("inflation", G, I, N, "ดึงข้อมูลจาก FRED ไม่ได้ (เช็กอินเทอร์เน็ต/ไฟร์วอลล์)"))

    # ----- GDP -----
    I, N = "🏭", "การเติบโตทางเศรษฐกิจ (GDP)"
    g = data.get("gdp")
    if g is not None and len(g) >= 2:
        now, prev = float(g.iloc[-1]), float(g.iloc[-2])
        if now >= 2.0:
            status, meaning = "good", "เศรษฐกิจโตแข็งแรง ยอดขายและกำไรบริษัทโดยรวมมักโตตาม"
        elif now >= 0.5:
            status, meaning = "mid", "เศรษฐกิจโตช้า ยังไม่ถึงขั้นน่ากังวล"
        else:
            status, meaning = "bad", "เศรษฐกิจหดตัวหรือแทบไม่โต เสี่ยงถดถอย กำไรบริษัทมักถูกกดดัน"
        out.append(_factor("gdp", G, I, N, status, f"GDP จริงล่าสุด {now:+.1f}% ต่อปี (ไตรมาสก่อน {prev:+.1f}%)", meaning,
                           ["วิธีดู: ตัวเลขประกาศรายไตรมาสและล่าช้า ตลาดมักสนใจแนวโน้มมากกว่าตัวเลขเดียว"],
                           {"kind": "bar", "title": "GDP จริงรายไตรมาส (% annualized)", "df": pd.DataFrame({"GDP": g.tail(12).values}, index=[_qlabel(i) for i in g.tail(12).index])}))
    else:
        out.append(_na("gdp", G, I, N, "ดึงข้อมูลจาก FRED ไม่ได้ (เช็กอินเทอร์เน็ต/ไฟร์วอลล์)"))

    # ----- ว่างงาน -----
    I, N = "👷", "อัตราการว่างงาน"
    u = data.get("unrate")
    if u is not None and len(u) > 16:
        now = float(u.iloc[-1])
        u3 = u.rolling(3).mean().dropna()
        sahm = float(u3.iloc[-1] - u3.iloc[-13:-1].min())
        if sahm >= 0.5:
            status, meaning = "bad", "ว่างงานพุ่งเร็วจนถึงเกณฑ์ Sahm Rule (≥0.5 จุด) ซึ่งในอดีตมักตรงกับช่วงเศรษฐกิจถดถอย"
        elif sahm >= 0.3:
            status, meaning = "mid", "ว่างงานเริ่มสูงขึ้นเร็วกว่าปกติ ควรจับตา"
        elif now < 5.0:
            status, meaning = "good", "ว่างงานต่ำและนิ่ง คนมีงานทำและใช้จ่ายต่อ เป็นพื้นฐานที่ดีของกำไรบริษัท"
        else:
            status, meaning = "mid", "ว่างงานค่อนข้างสูงแต่ไม่ได้เร่งขึ้นเร็ว"
        out.append(_factor("unemployment", G, I, N, status, f"{now:.1f}% · ตัวชี้ Sahm {sahm:+.2f} จุด", meaning,
                           ["Sahm Rule: ถ้าค่าเฉลี่ย 3 เดือนของอัตราว่างงานสูงกว่าจุดต่ำสุดในรอบ 12 เดือนที่ผ่านมาเกิน 0.5 จุด = สัญญาณเริ่มถดถอย",
                            "วิธีดู: ระดับต่ำไม่ได้สำคัญเท่า 'ความเร็วที่เพิ่มขึ้น'"],
                           {"kind": "line", "title": "อัตราว่างงาน 5 ปี (%)", "df": pd.DataFrame({"ว่างงาน": u.tail(60)})}))
    else:
        out.append(_na("unemployment", G, I, N, "ดึงข้อมูลจาก FRED ไม่ได้ (เช็กอินเทอร์เน็ต/ไฟร์วอลล์)"))
    return out


# ===============================================================
# สรุปภาพรวม
# ===============================================================
def summarize(factors: list) -> dict:
    cnt = {"good": 0, "mid": 0, "bad": 0, "na": 0}
    for f in factors:
        cnt[f["status"]] += 1
    valid = cnt["good"] + cnt["mid"] + cnt["bad"]
    if valid == 0:
        return {**cnt, "label": "ประเมินไม่ได้", "color": "#9a9aa8", "icon": "⚪", "detail": "ดึงข้อมูลไม่สำเร็จ"}
    net = (cnt["good"] - cnt["bad"]) / valid
    if net >= 0.4:
        label, color, icon = "ปัจจัยส่วนใหญ่หนุน", "#3ecf6e", "🟢"
    elif net <= -0.4:
        label, color, icon = "ปัจจัยส่วนใหญ่กดดัน", "#e5534b", "🔴"
    else:
        label, color, icon = "ปัจจัยผสม ไม่ชัดไปทางใด", "#d4af37", "🟡"
    return {**cnt, "label": label, "color": color, "icon": icon,
            "detail": f"หนุน {cnt['good']} · กลาง {cnt['mid']} · กดดัน {cnt['bad']}" + (f" · ไม่มีข้อมูล {cnt['na']}" if cnt["na"] else "")}
