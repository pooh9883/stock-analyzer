# -*- coding: utf-8 -*-
"""
deep.py
=======
โมดูลวิเคราะห์เชิงลึกเพิ่มเติม — ชุดสัญญาณเสริมจากข้อมูลฟรีของ yfinance
ที่ advanced.py ยังไม่ได้ใช้: momentum หลายช่วงเวลา, relative strength,
implied volatility skew, ช่วงคาดการณ์นักวิเคราะห์, ประวัติ earnings surprise,
ตำแหน่งในกรอบ 52 สัปดาห์, และ sentiment ข่าวแบบคร่าวๆ

⚠️ news sentiment เป็น keyword-based ธรรมดา ไม่ใช่ NLP model จริง
   ใช้เป็นสัญญาณเสริมเบาๆ เท่านั้น ไม่ควรให้น้ำหนักสูง
"""

import yfinance as yf
import pandas as pd
import numpy as np


# ---------------------------------------------------------------
# 1) Momentum หลายช่วงเวลา + ตำแหน่งในกรอบ 52 สัปดาห์
# ---------------------------------------------------------------
def analyze_momentum(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="1y")
        if hist.empty or len(hist) < 30:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอ"}

        close = hist["Close"]
        current = close.iloc[-1]

        def pct_change(days):
            if len(close) <= days:
                return None
            past = close.iloc[-days - 1]
            return (current - past) / past * 100

        periods = {"1 สัปดาห์": 5, "1 เดือน": 21, "3 เดือน": 63, "6 เดือน": 126, "1 ปี": 251}
        changes = {label: pct_change(d) for label, d in periods.items()}

        high_52w = close.max()
        low_52w = close.min()
        range_position = (current - low_52w) / (high_52w - low_52w) * 100 if high_52w > low_52w else None

        notes = []
        momentum_score = 0
        n_valid = 0
        for label, chg in changes.items():
            if chg is not None:
                notes.append(f"{label}: {chg:+.1f}%")
                momentum_score += 1 if chg > 0 else (-1 if chg < 0 else 0)
                n_valid += 1

        if range_position is not None:
            if range_position > 85:
                notes.append(f"ราคาปัจจุบันอยู่ที่ {range_position:.0f}% ของกรอบ 52 สัปดาห์ — ใกล้จุดสูงสุดรอบปี")
            elif range_position < 15:
                notes.append(f"ราคาปัจจุบันอยู่ที่ {range_position:.0f}% ของกรอบ 52 สัปดาห์ — ใกล้จุดต่ำสุดรอบปี")
            else:
                notes.append(f"ราคาปัจจุบันอยู่ที่ {range_position:.0f}% ของกรอบ 52 สัปดาห์")

        momentum_norm = (momentum_score / n_valid) if n_valid > 0 else 0

        return {
            "available": True,
            "changes": changes,
            "range_position": range_position,
            "momentum_score": momentum_norm,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 2) Relative Strength เทียบ S&P500 (SPY) — หุ้นนี้แรงกว่าตลาดไหม
# ---------------------------------------------------------------
def analyze_relative_strength(ticker_symbol: str) -> dict:
    try:
        stock_hist = yf.Ticker(ticker_symbol).history(period="3mo")["Close"]
        spy_hist = yf.Ticker("SPY").history(period="3mo")["Close"]

        if stock_hist.empty or spy_hist.empty or len(stock_hist) < 10:
            return {"available": False, "reason": "ข้อมูลไม่พอเปรียบเทียบ"}

        stock_return = (stock_hist.iloc[-1] - stock_hist.iloc[0]) / stock_hist.iloc[0] * 100
        spy_return = (spy_hist.iloc[-1] - spy_hist.iloc[0]) / spy_hist.iloc[0] * 100
        relative = stock_return - spy_return

        notes = []
        if relative > 5:
            notes.append(f"หุ้นนี้ทำผลตอบแทน {stock_return:+.1f}% ใน 3 เดือน แรงกว่า S&P500 ({spy_return:+.1f}%) อยู่ {relative:+.1f} จุด — Outperform")
        elif relative < -5:
            notes.append(f"หุ้นนี้ทำผลตอบแทน {stock_return:+.1f}% ใน 3 เดือน แพ้ S&P500 ({spy_return:+.1f}%) อยู่ {relative:+.1f} จุด — Underperform")
        else:
            notes.append(f"หุ้นนี้ทำผลตอบแทนใกล้เคียงตลาดรวม ({stock_return:+.1f}% vs S&P500 {spy_return:+.1f}%)")

        return {"available": True, "stock_return_3m": stock_return, "spy_return_3m": spy_return,
                "relative_strength": relative, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 3) Implied Volatility Skew — ตลาด option กลัวขาลงมากกว่าขาขึ้นไหม
# ---------------------------------------------------------------
def analyze_iv_skew(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        expirations = stock.options
        if not expirations:
            return {"available": False, "reason": "ไม่มีข้อมูล options"}

        chain = stock.option_chain(expirations[0])
        calls, puts = chain.calls, chain.puts

        current_price = stock.fast_info.get("lastPrice", None)
        if current_price is None or calls.empty or puts.empty:
            return {"available": False, "reason": "ข้อมูลไม่พอคำนวณ"}

        # หา strike ที่ใกล้ราคาปัจจุบันที่สุด (at-the-money)
        calls_near = calls.iloc[(calls["strike"] - current_price).abs().argsort()[:3]]
        puts_near = puts.iloc[(puts["strike"] - current_price).abs().argsort()[:3]]

        call_iv = calls_near["impliedVolatility"].mean()
        put_iv = puts_near["impliedVolatility"].mean()

        if pd.isna(call_iv) or pd.isna(put_iv) or call_iv == 0:
            return {"available": False, "reason": "ไม่มีข้อมูล implied volatility"}

        skew = (put_iv - call_iv) / call_iv * 100

        notes = []
        if skew > 15:
            notes.append(f"Put IV สูงกว่า Call IV {skew:.0f}% — ตลาดยอมจ่ายพรีเมียมป้องกันขาลงเยอะกว่าปกติ (ตลาดระวังความเสี่ยงขาลง)")
        elif skew < -5:
            notes.append(f"Call IV สูงกว่า Put IV — ตลาดคาดความผันผวนขาขึ้นมากกว่าปกติ")
        else:
            notes.append(f"IV Skew ใกล้เคียงปกติ ({skew:+.0f}%) — ไม่มีสัญญาณกลัวขาลงผิดปกติ")

        return {"available": True, "call_iv": call_iv, "put_iv": put_iv, "skew_pct": skew, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 4) ช่วงคาดการณ์นักวิเคราะห์ (Analyst Target Dispersion)
# ---------------------------------------------------------------
def analyze_target_dispersion(ticker_symbol: str) -> dict:
    try:
        info = yf.Ticker(ticker_symbol).info
        high = info.get("targetHighPrice")
        low = info.get("targetLowPrice")
        mean = info.get("targetMeanPrice")
        median = info.get("targetMedianPrice")
        current = info.get("currentPrice", info.get("regularMarketPrice"))
        n_analysts = info.get("numberOfAnalystOpinions")

        if not all([high, low, mean, current]):
            return {"available": False, "reason": "ข้อมูลราคาเป้าหมายไม่ครบ"}

        dispersion_pct = (high - low) / mean * 100 if mean else None
        upside_mean = (mean - current) / current * 100

        notes = []
        if n_analysts:
            notes.append(f"อิงจากนักวิเคราะห์ {n_analysts} คน")
        notes.append(f"ราคาเป้าหมาย: ต่ำสุด ${low:.0f} — เฉลี่ย ${mean:.0f} — สูงสุด ${high:.0f}")
        notes.append(f"Upside เฉลี่ยจากราคาปัจจุบัน: {upside_mean:+.1f}%")

        if dispersion_pct is not None:
            if dispersion_pct > 60:
                notes.append(f"ช่วงคาดการณ์กว้างมาก ({dispersion_pct:.0f}%) — นักวิเคราะห์เห็นไม่ตรงกัน ความไม่แน่นอนสูง")
            else:
                notes.append(f"ช่วงคาดการณ์ค่อนข้างแคบ ({dispersion_pct:.0f}%) — นักวิเคราะห์ค่อนข้างเห็นตรงกัน")

        return {"available": True, "high": high, "low": low, "mean": mean,
                "upside_mean_pct": upside_mean, "dispersion_pct": dispersion_pct, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 5) ประวัติ Earnings Surprise (8 ไตรมาสล่าสุด — เพิ่มขนาดตัวอย่างเพื่อลด noise)
# ---------------------------------------------------------------
def analyze_earnings_surprise(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        eps_hist = stock.earnings_history  # DataFrame: epsEstimate, epsActual, surprisePercent

        if eps_hist is None or eps_hist.empty:
            return {"available": False, "reason": "ไม่มีข้อมูล earnings history"}

        recent = eps_hist.tail(8)
        beats = (recent["surprisePercent"] > 0).sum()
        total = len(recent)

        notes = [f"เอาชนะคาดการณ์นักวิเคราะห์ {beats}/{total} ไตรมาสล่าสุด"]
        avg_surprise = recent["surprisePercent"].mean()
        notes.append(f"Surprise เฉลี่ย {avg_surprise:+.1f}%")

        if beats == total and total >= 5:
            notes.append("ทำได้ดีกว่าคาดต่อเนื่องทุกไตรมาส — track record ดี")
        elif beats == 0 and total >= 5:
            notes.append("ต่ำกว่าคาดต่อเนื่อง — ควรระวัง")

        return {"available": True, "beats": int(beats), "total": int(total),
                "avg_surprise_pct": avg_surprise, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 6) News Sentiment แบบคร่าวๆ (keyword-based เท่านั้น — ไม่ใช่ NLP จริง)
# ---------------------------------------------------------------
_POSITIVE_WORDS = [
    "beat", "surge", "soar", "upgrade", "record", "growth", "rally", "outperform",
    "strong", "boost", "gain", "rise", "jump", "bullish", "buy", "positive", "profit",
]
_NEGATIVE_WORDS = [
    "miss", "plunge", "downgrade", "cut", "lawsuit", "probe", "decline", "fall",
    "weak", "loss", "bearish", "sell", "warn", "concern", "risk", "drop", "layoff",
]


def analyze_news_sentiment(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        news = stock.news
        if not news:
            return {"available": False, "reason": "ไม่มีข่าวล่าสุด"}

        headlines = []
        for item in news[:10]:
            title = item.get("content", {}).get("title") or item.get("title", "")
            if title:
                headlines.append(title)

        if not headlines:
            return {"available": False, "reason": "ไม่พบหัวข้อข่าว"}

        pos_count = neg_count = 0
        for h in headlines:
            h_lower = h.lower()
            pos_count += sum(1 for w in _POSITIVE_WORDS if w in h_lower)
            neg_count += sum(1 for w in _NEGATIVE_WORDS if w in h_lower)

        notes = [f"วิเคราะห์จากหัวข้อข่าวล่าสุด {len(headlines)} ข่าว (แบบคร่าวๆ ไม่ใช่ NLP model จริง)"]
        net = pos_count - neg_count
        if net > 1:
            notes.append(f"โทนข่าวเอียงบวก (พบคำเชิงบวก {pos_count} vs เชิงลบ {neg_count})")
        elif net < -1:
            notes.append(f"โทนข่าวเอียงลบ (พบคำเชิงลบ {neg_count} vs เชิงบวก {pos_count})")
        else:
            notes.append("โทนข่าวค่อนข้างเป็นกลาง")

        notes.append(f"ตัวอย่างหัวข้อล่าสุด: \"{headlines[0][:80]}\"")

        return {"available": True, "positive_hits": pos_count, "negative_hits": neg_count,
                "net_score": net, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 7) แนวโน้มระยะยาว (กรอบเวลา ~1 เดือน) — รวม momentum, catalyst ที่จะมาถึง, analyst upside
# ---------------------------------------------------------------
def analyze_one_month_horizon(ticker_symbol: str) -> dict:
    try:
        momentum = analyze_momentum(ticker_symbol)
        target_disp = analyze_target_dispersion(ticker_symbol)

        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        earnings_ts = info.get("earningsTimestamp")

        notes = []
        score = 0.0
        max_score = 0.0

        # โมเมนตัม 1 เดือนกับ 3 เดือน — ให้คะแนนตามสัดส่วนขนาดจริง ไม่ใช่แค่ทิศทาง (+1/-1)
        # เพื่อป้องกันการชนเพดาน 100% ง่ายเกินไปทั้งที่โมเมนตัมอาจไม่ได้แรงขนาดนั้นจริง
        if momentum.get("available"):
            chg_1m = momentum["changes"].get("1 เดือน")
            chg_3m = momentum["changes"].get("3 เดือน")
            if chg_1m is not None:
                notes.append(f"ราคาช่วง 1 เดือนที่ผ่านมา: {chg_1m:+.1f}%")
                # ปรับสเกล: ±15% ถือว่าโมเมนตัมแรงสุดขั้วแล้ว (=คะแนนเต็ม ±1.0)
                score += max(-1.0, min(1.0, chg_1m / 15))
                max_score += 1.0
            if chg_3m is not None:
                notes.append(f"ราคาช่วง 3 เดือนที่ผ่านมา: {chg_3m:+.1f}% (บ่งชี้ทิศทางต่อเนื่อง)")
                # ปรับสเกล: ±30% ถือว่าโมเมนตัม 3 เดือนแรงสุดขั้วแล้ว
                score += 0.6 * max(-1.0, min(1.0, chg_3m / 30))
                max_score += 0.6

        # Earnings ภายใน 30 วันข้างหน้า = catalyst สำคัญที่ต้องรู้
        earnings_within_month = False
        if earnings_ts:
            try:
                earnings_date = datetime.fromtimestamp(earnings_ts)
                days_until = (earnings_date - datetime.now()).days
                if 0 <= days_until <= 30:
                    earnings_within_month = True
                    notes.append(f"⚠️ มีวันประกาศผลประกอบการในอีก {days_until} วัน ({earnings_date.strftime('%d %b %Y')}) — ราคามักผันผวนแรงช่วงนี้ ถือเป็นทั้งโอกาสและความเสี่ยง")
            except Exception:
                pass

        # Analyst upside ในกรอบเวลาที่ใกล้เคียง 1 เดือน (ใช้เป็นตัวชี้ทิศทางเชิงคุณภาพ)
        if target_disp.get("available"):
            upside = target_disp["upside_mean_pct"]
            notes.append(f"Upside เฉลี่ยจากนักวิเคราะห์: {upside:+.1f}% (เป้าหมายระยะกลาง-ยาว ไม่ใช่เฉพาะ 1 เดือน)")
            # ปรับสเกล: ±30% upside ถือว่าสุดขั้วแล้ว
            score += 0.4 * max(-1.0, min(1.0, upside / 30))
            max_score += 0.4

        lean_pct = round(max(-100, min(100, (score / max_score) * 100)), 1) if max_score > 0 else 0

        # ถ้ามี earnings ภายในเดือนนี้ = ความไม่แน่นอนสูงขึ้น ลดความมั่นใจของตัวเลขลงเล็กน้อย
        # (ไม่เปลี่ยนทิศทาง แค่ทำให้ตัวเลขไม่สุดขั้วเกินจริงในช่วงที่มีความไม่แน่นอนสูง)
        if earnings_within_month:
            lean_pct = round(lean_pct * 0.85, 1)

        if lean_pct > 25:
            verdict = "โน้มเอียงขึ้นในกรอบ 1 เดือน"
        elif lean_pct < -25:
            verdict = "โน้มเอียงลงในกรอบ 1 เดือน"
        else:
            verdict = "กลางๆ ในกรอบ 1 เดือน"

        return {
            "available": True,
            "lean_pct": lean_pct,
            "verdict": verdict,
            "earnings_within_month": earnings_within_month,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# ฟังก์ชันหลัก: รวมทุกสัญญาณเชิงลึกเป็นภาพรวมเดียว
# ---------------------------------------------------------------
def deep_outlook(ticker_symbol: str) -> dict:
    momentum = analyze_momentum(ticker_symbol)
    rel_strength = analyze_relative_strength(ticker_symbol)
    iv_skew = analyze_iv_skew(ticker_symbol)
    target_disp = analyze_target_dispersion(ticker_symbol)
    earnings = analyze_earnings_surprise(ticker_symbol)
    news = analyze_news_sentiment(ticker_symbol)

    total_score = 0
    max_possible = 0
    sources = []

    if momentum.get("available"):
        total_score += momentum["momentum_score"] * 1.5
        max_possible += 1.5
        sources.append(("โมเมนตัมราคา หลายช่วงเวลา (Momentum)", momentum["notes"]))

    if rel_strength.get("available"):
        rs = rel_strength["relative_strength"]
        pts = 1 if rs > 5 else (-1 if rs < -5 else 0)
        total_score += pts
        max_possible += 1
        sources.append(("ความแข็งแกร่งเทียบตลาด S&P500 (Relative Strength)", rel_strength["notes"]))

    if iv_skew.get("available"):
        skew = iv_skew["skew_pct"]
        pts = -1 if skew > 15 else (0.5 if skew < -5 else 0)
        total_score += pts
        max_possible += 1
        sources.append(("ความเบ้ของความผันผวนแฝง (IV Skew)", iv_skew["notes"]))

    if target_disp.get("available"):
        upside = target_disp["upside_mean_pct"]
        pts = 1 if upside > 15 else (-1 if upside < -5 else 0.3)
        total_score += pts
        max_possible += 1
        sources.append(("ช่วงคาดการณ์ราคาของนักวิเคราะห์ (Target Dispersion)", target_disp["notes"]))

    if earnings.get("available"):
        beats, total = earnings["beats"], earnings["total"]
        pts = ((beats / total) - 0.5) * 2 if total > 0 else 0  # -1 ถึง +1
        total_score += pts
        max_possible += 1
        sources.append(("ประวัติผลประกอบการเทียบคาดการณ์ (Earnings Surprise)", earnings["notes"]))

    if news.get("available"):
        net = news["net_score"]
        pts = max(-1, min(1, net * 0.3))
        total_score += pts * 0.5  # น้ำหนักน้อยเพราะเป็นแค่ keyword-based
        max_possible += 0.5
        sources.append(("อารมณ์ข่าว ประเมินคร่าวๆ (News Sentiment)", news["notes"]))

    lean_pct = round(max(-100, min(100, (total_score / max_possible) * 100)), 1) if max_possible > 0 else 0

    if lean_pct > 25:
        verdict = "โน้มเอียงขึ้น (Bullish Tilt)"
    elif lean_pct < -25:
        verdict = "โน้มเอียงลง (Bearish Tilt)"
    else:
        verdict = "กลางๆ ไม่มีสัญญาณชัดเจน (Neutral)"

    return {
        "lean_pct": lean_pct,
        "verdict": verdict,
        "sources": sources,
        "raw": {
            "momentum": momentum, "relative_strength": rel_strength, "iv_skew": iv_skew,
            "target_dispersion": target_disp, "earnings": earnings, "news": news,
        },
    }
