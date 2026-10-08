# -*- coding: utf-8 -*-
"""
scoring.py
==========
ระบบให้คะแนนหุ้น 10 มิติ ด้วยสูตรคณิตศาสตร์ล้วนๆ
- ไม่ต้องมี API key
- ไม่มีวันหมดอายุ / โดนตัด quota
- ข้อมูลทั้งหมดดึงจาก yfinance (ฟรี ไม่จำกัด)

หลักการ: แต่ละมิติให้คะแนน 0-100 ตามเกณฑ์ทั่วไปที่นักลงทุนใช้จริง
พร้อมคำอธิบายเป็นภาษาไทยว่า "ทำไม" ถึงได้คะแนนนั้น
"""

import yfinance as yf
import pandas as pd
import numpy as np


# ---------------------------------------------------------------
# ฟังก์ชันช่วยเหลือ: ดึงข้อมูลราคาย้อนหลัง + คำนวณ technical indicators
# ---------------------------------------------------------------
def get_technical_data(ticker_symbol: str):
    """ดึงราคาย้อนหลัง 1 ปี แล้วคำนวณ SMA50, SMA200, RSI14 เอง (ไม่ใช้ไลบรารีเสริม)"""
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="1y")

    if hist.empty or len(hist) < 30:
        return None

    close = hist["Close"]

    # Simple Moving Average
    sma50 = close.rolling(window=50).mean().iloc[-1] if len(close) >= 50 else None
    sma200 = close.rolling(window=200).mean().iloc[-1] if len(close) >= 200 else None
    current_price = close.iloc[-1]

    # RSI 14 วัน (คำนวณเอง ไม่ต้องใช้ ta-lib)
    delta = close.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))
    rsi_latest = rsi.iloc[-1] if not rsi.empty else None

    # Volatility (annualized, จาก daily returns)
    daily_returns = close.pct_change().dropna()
    volatility = daily_returns.std() * np.sqrt(252) * 100 if len(daily_returns) > 1 else None

    return {
        "current_price": current_price,
        "sma50": sma50,
        "sma200": sma200,
        "rsi14": rsi_latest,
        "volatility_annual_pct": volatility,
        "history": hist,
    }


def _safe_get(info: dict, key: str, default=None):
    val = info.get(key, default)
    if val is None:
        return default
    return val


# ---------------------------------------------------------------
# มิติที่ 1: โมเดลธุรกิจและการสร้างรายได้
# ---------------------------------------------------------------
def score_business_model(info: dict) -> dict:
    revenue_growth = _safe_get(info, "revenueGrowth")
    gross_margin = _safe_get(info, "grossMargins")
    sector = _safe_get(info, "sector", "ไม่ทราบ")
    industry = _safe_get(info, "industry", "ไม่ทราบ")

    score = 50
    notes = []

    if revenue_growth is not None:
        if revenue_growth > 0.20:
            score += 25
            notes.append(f"รายได้เติบโต {revenue_growth*100:.1f}% YoY — เติบโตแรงมาก")
        elif revenue_growth > 0.05:
            score += 10
            notes.append(f"รายได้เติบโต {revenue_growth*100:.1f}% YoY — เติบโตปกติ")
        elif revenue_growth > 0:
            notes.append(f"รายได้เติบโตช้า ({revenue_growth*100:.1f}% YoY)")
        else:
            score -= 20
            notes.append(f"รายได้ติดลบ ({revenue_growth*100:.1f}% YoY) — ต้องระวัง")
    else:
        notes.append("ไม่มีข้อมูลการเติบโตของรายได้")

    if gross_margin is not None:
        if gross_margin > 0.5:
            score += 15
            notes.append(f"Gross margin {gross_margin*100:.1f}% — สูง โมเดลธุรกิจแข็งแรง")
        elif gross_margin > 0.25:
            score += 5
            notes.append(f"Gross margin {gross_margin*100:.1f}% — ปานกลาง")
        else:
            notes.append(f"Gross margin {gross_margin*100:.1f}% — ต่ำ ธุรกิจแข่งขันด้วยราคา")

    score = max(0, min(100, score))
    return {
        "score": score,
        "summary": f"ธุรกิจอยู่ในกลุ่ม {sector} / {industry}",
        "details": notes,
    }


# ---------------------------------------------------------------
# มิติที่ 2: Economic Moat (คูเมือง)
# ---------------------------------------------------------------
def score_moat(info: dict) -> dict:
    operating_margin = _safe_get(info, "operatingMargins")
    roe = _safe_get(info, "returnOnEquity")

    score = 50
    notes = []

    if operating_margin is not None:
        if operating_margin > 0.25:
            score += 25
            notes.append(f"Operating margin {operating_margin*100:.1f}% — สูงมาก บ่งบอกความได้เปรียบทางการแข่งขัน")
        elif operating_margin > 0.10:
            score += 10
            notes.append(f"Operating margin {operating_margin*100:.1f}% — ปานกลาง")
        else:
            score -= 10
            notes.append(f"Operating margin {operating_margin*100:.1f}% — ต่ำ อาจไม่มี moat ชัดเจน")

    if roe is not None:
        if roe > 0.20:
            score += 25
            notes.append(f"ROE {roe*100:.1f}% — สูงมาก ใช้เงินทุนได้มีประสิทธิภาพ")
        elif roe > 0.10:
            score += 10
            notes.append(f"ROE {roe*100:.1f}% — ปานกลาง")
        else:
            notes.append(f"ROE {roe*100:.1f}% — ต่ำ")

    score = max(0, min(100, score))
    return {"score": score, "summary": "วัดจาก Operating Margin และ ROE", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 3: ความแข็งแกร่งทางการเงิน
# ---------------------------------------------------------------
def score_financial_health(info: dict) -> dict:
    current_ratio = _safe_get(info, "currentRatio")
    debt_to_equity = _safe_get(info, "debtToEquity")
    free_cashflow = _safe_get(info, "freeCashflow")

    score = 50
    notes = []

    if current_ratio is not None:
        if current_ratio > 1.5:
            score += 15
            notes.append(f"Current ratio {current_ratio:.2f} — สภาพคล่องดี")
        elif current_ratio > 1.0:
            score += 5
            notes.append(f"Current ratio {current_ratio:.2f} — พอใช้")
        else:
            score -= 15
            notes.append(f"Current ratio {current_ratio:.2f} — ต่ำกว่า 1 ต้องระวังสภาพคล่อง")

    if debt_to_equity is not None:
        if debt_to_equity < 50:
            score += 20
            notes.append(f"Debt/Equity {debt_to_equity:.1f} — หนี้สินต่ำ ปลอดภัย")
        elif debt_to_equity < 100:
            score += 5
            notes.append(f"Debt/Equity {debt_to_equity:.1f} — ปานกลาง")
        else:
            score -= 15
            notes.append(f"Debt/Equity {debt_to_equity:.1f} — หนี้สินสูง มีความเสี่ยง")

    if free_cashflow is not None:
        if free_cashflow > 0:
            score += 15
            notes.append("Free Cash Flow เป็นบวก — ธุรกิจสร้างเงินสดได้จริง")
        else:
            score -= 20
            notes.append("Free Cash Flow ติดลบ — เผาเงินสด ต้องระวัง")

    score = max(0, min(100, score))
    return {"score": score, "summary": "วัดจาก Current Ratio, Debt/Equity, Free Cash Flow", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 4: ความเสี่ยง Disruption (ใช้ volatility + beta เป็น proxy)
# ---------------------------------------------------------------
def score_disruption_risk(info: dict, tech_data: dict) -> dict:
    beta = _safe_get(info, "beta")
    score = 60
    notes = []

    if beta is not None:
        if beta > 1.8:
            score -= 25
            notes.append(f"Beta {beta:.2f} — ผันผวนสูงกว่าตลาดมาก มักเจอในธุรกิจที่มีความไม่แน่นอนสูง")
        elif beta > 1.2:
            score -= 10
            notes.append(f"Beta {beta:.2f} — ผันผวนกว่าตลาดปานกลาง")
        else:
            score += 10
            notes.append(f"Beta {beta:.2f} — ผันผวนใกล้เคียงหรือต่ำกว่าตลาด")

    if tech_data and tech_data.get("volatility_annual_pct"):
        vol = tech_data["volatility_annual_pct"]
        notes.append(f"ความผันผวนรายปี ~{vol:.1f}%")
        if vol > 60:
            score -= 15
            notes.append("→ ผันผวนสูงมาก อาจสะท้อนความไม่แน่นอนของอนาคตธุรกิจ")

    notes.append("หมายเหตุ: นี่เป็นการประเมินทางอ้อมจากความผันผวนเท่านั้น ไม่ได้วิเคราะห์ปัจจัย disruption จริง ควรอ่านข่าวอุตสาหกรรมประกอบ")

    score = max(0, min(100, score))
    return {"score": score, "summary": "ประเมินทางอ้อมจาก Beta และความผันผวน", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 5: Capital Allocation & Governance
# ---------------------------------------------------------------
def score_capital_allocation(info: dict) -> dict:
    roe = _safe_get(info, "returnOnEquity")
    payout_ratio = _safe_get(info, "payoutRatio")
    insider_pct = _safe_get(info, "heldPercentInsiders")

    score = 50
    notes = []

    if roe is not None:
        if roe > 0.15:
            score += 20
            notes.append(f"ROE {roe*100:.1f}% — จัดสรรเงินทุนมีประสิทธิภาพ")
        else:
            notes.append(f"ROE {roe*100:.1f}%")

    if payout_ratio is not None:
        if 0 < payout_ratio < 0.6:
            score += 15
            notes.append(f"Payout ratio {payout_ratio*100:.1f}% — จ่ายปันผลสมดุล เหลือเงินไปลงทุนต่อ")
        elif payout_ratio >= 0.6:
            score -= 5
            notes.append(f"Payout ratio {payout_ratio*100:.1f}% — จ่ายปันผลเยอะ เหลือเงินลงทุนต่อน้อย")

    if insider_pct is not None:
        if insider_pct > 0.05:
            score += 10
            notes.append(f"ผู้บริหารถือหุ้น {insider_pct*100:.1f}% — มี skin in the game")

    score = max(0, min(100, score))
    return {"score": score, "summary": "วัดจาก ROE, Payout Ratio, สัดส่วนผู้บริหารถือหุ้น", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 6: Catalysts (ปัจจัยเร่ง)
# ---------------------------------------------------------------
def score_catalysts(info: dict) -> dict:
    earnings_date = _safe_get(info, "earningsTimestamp")
    target_price = _safe_get(info, "targetMeanPrice")
    current_price = _safe_get(info, "currentPrice", _safe_get(info, "regularMarketPrice"))

    notes = []
    score = 50

    if target_price and current_price:
        upside = (target_price - current_price) / current_price * 100
        if upside > 20:
            score += 25
            notes.append(f"นักวิเคราะห์ให้ราคาเป้าหมายสูงกว่าราคาปัจจุบัน {upside:.1f}% — upside น่าสนใจ")
        elif upside > 0:
            score += 10
            notes.append(f"ราคาเป้าหมายสูงกว่าราคาปัจจุบัน {upside:.1f}%")
        else:
            score -= 15
            notes.append(f"ราคาเป้าหมายต่ำกว่าราคาปัจจุบัน {upside:.1f}% — นักวิเคราะห์มองว่าแพงไปแล้ว")

    if earnings_date:
        notes.append("มีวันประกาศผลประกอบการใกล้ๆ นี้ — ราคามักผันผวนแรงช่วงนั้น (ดูวันที่แน่นอนในหน้าหลัก)")

    score = max(0, min(100, score))
    return {"score": score, "summary": "วัดจาก Analyst Target Price และวัน Earnings", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 7: Valuation
# ---------------------------------------------------------------
def score_valuation(info: dict) -> dict:
    pe = _safe_get(info, "trailingPE")
    forward_pe = _safe_get(info, "forwardPE")
    peg = _safe_get(info, "pegRatio")

    score = 50
    notes = []

    if pe is not None:
        if pe < 15:
            score += 20
            notes.append(f"Trailing P/E {pe:.1f} — ถูกเทียบกับกำไร")
        elif pe < 30:
            score += 5
            notes.append(f"Trailing P/E {pe:.1f} — ปานกลาง")
        else:
            score -= 15
            notes.append(f"Trailing P/E {pe:.1f} — แพงเทียบกับกำไรปัจจุบัน")

    if forward_pe is not None and pe is not None:
        if forward_pe < pe:
            score += 10
            notes.append(f"Forward P/E ({forward_pe:.1f}) ต่ำกว่า Trailing P/E — ตลาดคาดกำไรจะโตขึ้น")

    if peg is not None:
        if peg < 1:
            score += 15
            notes.append(f"PEG Ratio {peg:.2f} — ต่ำกว่า 1 ถือว่าราคาถูกเทียบกับการเติบโต")
        elif peg < 2:
            notes.append(f"PEG Ratio {peg:.2f} — ปานกลาง")
        else:
            score -= 10
            notes.append(f"PEG Ratio {peg:.2f} — สูง ราคาอาจแพงเทียบกับการเติบโต")

    score = max(0, min(100, score))
    return {"score": score, "summary": "วัดจาก P/E, Forward P/E, PEG Ratio", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 8: Red Flags
# ---------------------------------------------------------------
def score_red_flags(info: dict, tech_data: dict) -> dict:
    short_pct = _safe_get(info, "shortPercentOfFloat")
    debt_to_equity = _safe_get(info, "debtToEquity")
    free_cashflow = _safe_get(info, "freeCashflow")

    score = 80  # เริ่มสูงแล้วหักตามความเสี่ยงที่เจอ
    notes = []
    flags = []

    if short_pct is not None and short_pct > 0.15:
        score -= 25
        flags.append(f"⚠️ Short interest สูง ({short_pct*100:.1f}% ของ float) — มีคนเดิมพันว่าหุ้นจะลงเยอะ")

    if debt_to_equity is not None and debt_to_equity > 150:
        score -= 20
        flags.append(f"⚠️ หนี้สินสูงมาก (D/E {debt_to_equity:.0f}) — ความเสี่ยงทางการเงิน")

    if free_cashflow is not None and free_cashflow < 0:
        score -= 20
        flags.append("⚠️ Free Cash Flow ติดลบ — เผาเงินสดต่อเนื่อง")

    if tech_data and tech_data.get("rsi14") is not None:
        rsi = tech_data["rsi14"]
        if rsi > 75:
            score -= 10
            flags.append(f"⚠️ RSI {rsi:.0f} — overbought (ซื้อมากเกินไป) ระยะสั้นอาจปรับฐาน")

    if not flags:
        notes.append("ไม่พบสัญญาณอันตรายชัดเจนจากข้อมูลที่มี")
    else:
        notes = flags

    score = max(0, min(100, score))
    return {"score": score, "summary": "ยิ่งคะแนนสูง = ยิ่งเจอ red flag น้อย", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 9: Bargaining Power & Concentration Risk
# ---------------------------------------------------------------
def score_bargaining_power(info: dict) -> dict:
    gross_margin = _safe_get(info, "grossMargins")
    market_cap = _safe_get(info, "marketCap")

    score = 50
    notes = []

    if gross_margin is not None:
        if gross_margin > 0.4:
            score += 20
            notes.append(f"Gross margin {gross_margin*100:.1f}% สูง — มักบ่งบอกว่าตั้งราคาเองได้ ไม่ถูกกดราคาจากคู่ค้า")
        else:
            notes.append(f"Gross margin {gross_margin*100:.1f}% — อาจมีอำนาจต่อรองจำกัด")

    if market_cap is not None:
        if market_cap > 100_000_000_000:
            score += 15
            notes.append("Market cap ใหญ่ระดับแสนล้าน — มักมีอำนาจต่อรองกับซัพพลายเออร์สูง")

    notes.append("หมายเหตุ: ข้อมูลนี้ประเมินทางอ้อมเท่านั้น ควรอ่านรายงานประจำปี (10-K) เพื่อดูสัดส่วนลูกค้ารายใหญ่จริง")

    score = max(0, min(100, score))
    return {"score": score, "summary": "ประเมินทางอ้อมจาก Gross Margin และ Market Cap", "details": notes}


# ---------------------------------------------------------------
# มิติที่ 10: Cyclicality & Pricing Power
# ---------------------------------------------------------------
def score_cyclicality(info: dict, tech_data: dict) -> dict:
    beta = _safe_get(info, "beta")
    gross_margin = _safe_get(info, "grossMargins")

    score = 50
    notes = []

    if beta is not None:
        if beta > 1.3:
            notes.append(f"Beta {beta:.2f} สูง — มักเป็นหุ้นวัฏจักร (cyclical) ขยับแรงตามเศรษฐกิจ")
            score -= 5
        else:
            notes.append(f"Beta {beta:.2f} — ไม่ผันผวนตามวัฏจักรเศรษฐกิจมากนัก")
            score += 10

    if gross_margin is not None and gross_margin > 0.45:
        score += 15
        notes.append("Gross margin สูง — มักมี pricing power สามารถขึ้นราคาได้โดยไม่เสียลูกค้ามาก")

    score = max(0, min(100, score))
    return {"score": score, "summary": "ประเมินจาก Beta และ Gross Margin", "details": notes}


# ---------------------------------------------------------------
# ฟังก์ชันหลัก: รวมทั้ง 10 มิติ
# ---------------------------------------------------------------
DIMENSION_NAMES_TH = {
    "business_model": "1. โมเดลธุรกิจและการสร้างรายได้",
    "moat": "2. Economic Moat (คูเมือง)",
    "financial_health": "3. ความแข็งแกร่งทางการเงิน",
    "disruption_risk": "4. ความเสี่ยง Disruption",
    "capital_allocation": "5. Capital Allocation & Governance",
    "catalysts": "6. ปัจจัยเร่ง (Catalysts)",
    "valuation": "7. Valuation & Margin of Safety",
    "red_flags": "8. Red Flags & Exit Criteria",
    "bargaining_power": "9. Bargaining Power & Concentration Risk",
    "cyclicality": "10. Cyclicality & Pricing Power",
}


def full_analysis(ticker_symbol: str) -> dict:
    """คืนค่า dict ที่มีคะแนนครบทั้ง 10 มิติ + ข้อมูลดิบ + คะแนนรวม"""
    stock = yf.Ticker(ticker_symbol)
    info = stock.info

    if not info or "symbol" not in info and "shortName" not in info:
        return {"error": f"ไม่พบข้อมูลหุ้น {ticker_symbol} กรุณาตรวจสอบชื่อ ticker อีกครั้ง"}

    tech_data = get_technical_data(ticker_symbol)

    dims = {
        "business_model": score_business_model(info),
        "moat": score_moat(info),
        "financial_health": score_financial_health(info),
        "disruption_risk": score_disruption_risk(info, tech_data),
        "capital_allocation": score_capital_allocation(info),
        "catalysts": score_catalysts(info),
        "valuation": score_valuation(info),
        "red_flags": score_red_flags(info, tech_data),
        "bargaining_power": score_bargaining_power(info),
        "cyclicality": score_cyclicality(info, tech_data),
    }

    overall_score = round(sum(d["score"] for d in dims.values()) / len(dims), 1)

    if overall_score >= 70:
        overall_label = "น่าสนใจ (Bullish tilt)"
    elif overall_score >= 45:
        overall_label = "กลางๆ (Hold / ต้องดูเพิ่ม)"
    else:
        overall_label = "ควรระวัง (Bearish tilt)"

    return {
        "ticker": ticker_symbol.upper(),
        "info": info,
        "tech_data": tech_data,
        "dimensions": dims,
        "overall_score": overall_score,
        "overall_label": overall_label,
    }
