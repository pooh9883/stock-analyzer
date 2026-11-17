# -*- coding: utf-8 -*-
"""
advanced.py
===========
โมดูลวิเคราะห์ขั้นสูง — รวมสัญญาณจากหลายแหล่งข้อมูลจริงที่ yfinance ให้ฟรี
เพื่อประเมิน "แนวโน้มระยะสั้น" ของหุ้น (ขึ้น/ลง/กลางๆ)

⚠️ ข้อจำกัดที่ต้องรู้:
- นี่คือการประเมินเชิงสถิติจากข้อมูลสาธารณะ ไม่ใช่ข้อมูล real-time options flow
  แบบ Unusual Whales / Quiver Quantitative / AltIndex ที่ต้องเสียเงินสมัคร
- ไม่มีเครื่องมือไหนในโลก "ทำนาย" ราคาหุ้นได้แม่นยำ 100% รวมถึงระบบนี้ด้วย
- ใช้เป็นข้อมูลประกอบการตัดสินใจ ไม่ใช่คำแนะนำซื้อ-ขาย
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# ---------------------------------------------------------------
# 1) Options Chain จริง — ทดแทนแนวคิด "Options Flow" ของ Unusual Whales
#    (ไม่ใช่ real-time sweep/block trade แต่เป็น open interest + volume จริง ณ ปัจจุบัน)
# ---------------------------------------------------------------
def analyze_options_chain(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        expirations = stock.options
        if not expirations:
            return {"available": False, "reason": "หุ้นนี้ไม่มีการซื้อขาย options"}

        # เลือกวันหมดอายุที่ใกล้ที่สุด
        nearest_exp = expirations[0]
        chain = stock.option_chain(nearest_exp)
        calls, puts = chain.calls, chain.puts

        call_vol = calls["volume"].fillna(0).sum()
        put_vol = puts["volume"].fillna(0).sum()
        call_oi = calls["openInterest"].fillna(0).sum()
        put_oi = puts["openInterest"].fillna(0).sum()

        pc_ratio_vol = (put_vol / call_vol) if call_vol > 0 else None
        pc_ratio_oi = (put_oi / call_oi) if call_oi > 0 else None

        # หา strike ที่มี OI สูงสุด (มักเป็นแนวรับ/แนวต้านทางจิตวิทยา)
        current_price = stock.fast_info.get("lastPrice", None)
        top_call_strike = calls.loc[calls["openInterest"].idxmax(), "strike"] if not calls.empty else None
        top_put_strike = puts.loc[puts["openInterest"].idxmax(), "strike"] if not puts.empty else None

        notes = []
        if pc_ratio_vol is not None:
            if pc_ratio_vol < 0.7:
                notes.append(f"Put/Call Volume Ratio {pc_ratio_vol:.2f} — เอียงไปทาง Call (bullish tilt)")
            elif pc_ratio_vol > 1.3:
                notes.append(f"Put/Call Volume Ratio {pc_ratio_vol:.2f} — เอียงไปทาง Put (bearish tilt)")
            else:
                notes.append(f"Put/Call Volume Ratio {pc_ratio_vol:.2f} — ใกล้เคียงสมดุล")

        if top_call_strike:
            notes.append(f"Call OI สูงสุดที่ strike ${top_call_strike:.0f} — อาจเป็นแนวต้านทางจิตวิทยา")
        if top_put_strike:
            notes.append(f"Put OI สูงสุดที่ strike ${top_put_strike:.0f} — อาจเป็นแนวรับทางจิตวิทยา")

        return {
            "available": True,
            "expiration_used": nearest_exp,
            "call_volume": int(call_vol),
            "put_volume": int(put_vol),
            "call_oi": int(call_oi),
            "put_oi": int(put_oi),
            "put_call_ratio_volume": pc_ratio_vol,
            "put_call_ratio_oi": pc_ratio_oi,
            "top_call_strike": top_call_strike,
            "top_put_strike": top_put_strike,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 2) Insider Transactions — ทดแทนแนวคิด Quiver Insider/Congress
#    (เฉพาะ insider จริง ไม่ใช่ ส.ส./ส.ว. เพราะ yfinance ไม่มีข้อมูล congress)
# ---------------------------------------------------------------
def analyze_insider_activity(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        insiders = stock.insider_transactions

        if insiders is None or insiders.empty:
            return {"available": False, "reason": "ไม่มีข้อมูล insider transactions"}

        # กรองเฉพาะ 90 วันล่าสุด ถ้ามีคอลัมน์วันที่
        recent = insiders.head(15)  # เอา 15 รายการล่าสุด (yfinance เรียงใหม่สุดก่อนอยู่แล้ว)

        buys = recent[recent["Text"].str.contains("Purchase|Buy", case=False, na=False)] \
            if "Text" in recent.columns else pd.DataFrame()
        sells = recent[recent["Text"].str.contains("Sale|Sell", case=False, na=False)] \
            if "Text" in recent.columns else pd.DataFrame()

        buy_count = len(buys)
        sell_count = len(sells)

        notes = []
        if buy_count > sell_count:
            notes.append(f"ผู้บริหารซื้อหุ้นตัวเอง {buy_count} ครั้ง เทียบกับขาย {sell_count} ครั้ง (ในรายการล่าสุด) — สัญญาณบวก")
        elif sell_count > buy_count:
            notes.append(f"ผู้บริหารขายหุ้นตัวเอง {sell_count} ครั้ง เทียบกับซื้อ {buy_count} ครั้ง (ในรายการล่าสุด) — ควรสังเกต (อาจเป็นแค่ diversify พอร์ตส่วนตัวก็ได้)")
        else:
            notes.append("จำนวนครั้งซื้อ-ขายของผู้บริหารใกล้เคียงกัน")

        return {
            "available": True,
            "buy_count": buy_count,
            "sell_count": sell_count,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 3) Institutional Holders — ทดแทนแนวคิด Quiver "Whale Activity"
# ---------------------------------------------------------------
def analyze_institutional_holders(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        inst_pct = info.get("heldPercentInstitutions")
        insider_pct = info.get("heldPercentInsiders")

        notes = []
        score_hint = 0

        if inst_pct is not None:
            if inst_pct > 0.7:
                notes.append(f"สถาบันถือหุ้น {inst_pct*100:.1f}% ของทั้งหมด — สูงมาก สถาบันเชื่อมั่นในหุ้นนี้")
                score_hint += 1
            elif inst_pct > 0.4:
                notes.append(f"สถาบันถือหุ้น {inst_pct*100:.1f}% — ปานกลาง")
            else:
                notes.append(f"สถาบันถือหุ้น {inst_pct*100:.1f}% — ค่อนข้างต่ำ")

        if insider_pct is not None and insider_pct > 0.05:
            notes.append(f"ผู้บริหารถือหุ้นเอง {insider_pct*100:.1f}% — มี skin in the game")
            score_hint += 1

        return {"available": True, "institution_pct": inst_pct, "insider_pct": insider_pct, "notes": notes, "score_hint": score_hint}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 4) Analyst Recommendation Trend — ทดแทนแนวคิดคะแนนรวม AltIndex
# ---------------------------------------------------------------
def analyze_analyst_trend(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        rec_summary = stock.recommendations_summary  # DataFrame: period, strongBuy, buy, hold, sell, strongSell

        if rec_summary is None or rec_summary.empty:
            return {"available": False, "reason": "ไม่มีข้อมูลคำแนะนำนักวิเคราะห์"}

        current = rec_summary.iloc[0]  # แถวแรกมักเป็นช่วงปัจจุบัน (0m)
        prior = rec_summary.iloc[1] if len(rec_summary) > 1 else None  # เดือนก่อน (-1m)

        def bullish_score(row):
            total = row["strongBuy"] + row["buy"] + row["hold"] + row["sell"] + row["strongSell"]
            if total == 0:
                return None
            weighted = (row["strongBuy"] * 2 + row["buy"] * 1 + row["hold"] * 0
                        - row["sell"] * 1 - row["strongSell"] * 2)
            return weighted / total

        cur_score = bullish_score(current)
        prior_score = bullish_score(prior) if prior is not None else None

        notes = []
        if cur_score is not None:
            if cur_score > 0.5:
                notes.append(f"นักวิเคราะห์ส่วนใหญ่แนะนำ Buy/Strong Buy (คะแนนความเชื่อมั่น {cur_score:.2f})")
            elif cur_score > 0:
                notes.append(f"นักวิเคราะห์เอียงไปทาง Buy เล็กน้อย (คะแนน {cur_score:.2f})")
            elif cur_score > -0.3:
                notes.append(f"นักวิเคราะห์ค่อนข้างกลางๆ (คะแนน {cur_score:.2f})")
            else:
                notes.append(f"นักวิเคราะห์เอียงไปทาง Sell (คะแนน {cur_score:.2f}) — ควรระวัง")

        trend = None
        if cur_score is not None and prior_score is not None:
            diff = cur_score - prior_score
            if diff > 0.1:
                trend = "upgrade"
                notes.append("แนวโน้มดีขึ้นเทียบเดือนก่อน — มีการอัปเกรดคำแนะนำ")
            elif diff < -0.1:
                trend = "downgrade"
                notes.append("แนวโน้มแย่ลงเทียบเดือนก่อน — มีการดาวน์เกรดคำแนะนำ")
            else:
                trend = "stable"

        return {
            "available": True,
            "current_score": cur_score,
            "trend": trend,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 5) Technical ขั้นสูง — MACD, Bollinger, Golden/Death Cross, Volume Trend
# ---------------------------------------------------------------
def analyze_technical_advanced(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="1y")
        if hist.empty or len(hist) < 50:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอคำนวณ"}

        close = hist["Close"]
        volume = hist["Volume"]

        # MACD (12, 26, 9)
        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()
        macd_line = ema12 - ema26
        signal_line = macd_line.ewm(span=9, adjust=False).mean()
        macd_hist = macd_line - signal_line
        macd_latest = macd_line.iloc[-1]
        signal_latest = signal_line.iloc[-1]
        macd_cross_bullish = macd_hist.iloc[-1] > 0 and macd_hist.iloc[-2] <= 0
        macd_cross_bearish = macd_hist.iloc[-1] < 0 and macd_hist.iloc[-2] >= 0

        # Bollinger Bands (20, 2)
        sma20 = close.rolling(20).mean()
        std20 = close.rolling(20).std()
        upper_band = sma20 + 2 * std20
        lower_band = sma20 - 2 * std20
        current_price = close.iloc[-1]
        bb_position = None
        if not pd.isna(upper_band.iloc[-1]) and not pd.isna(lower_band.iloc[-1]):
            band_width = upper_band.iloc[-1] - lower_band.iloc[-1]
            if band_width > 0:
                bb_position = (current_price - lower_band.iloc[-1]) / band_width  # 0=ล่างสุด, 1=บนสุด

        # Golden Cross / Death Cross (SMA50 vs SMA200)
        sma50 = close.rolling(50).mean()
        sma200 = close.rolling(200).mean() if len(close) >= 200 else None
        golden_cross = death_cross = False
        if sma200 is not None and not sma200.isna().all():
            if sma50.iloc[-1] > sma200.iloc[-1] and sma50.iloc[-2] <= sma200.iloc[-2]:
                golden_cross = True
            elif sma50.iloc[-1] < sma200.iloc[-1] and sma50.iloc[-2] >= sma200.iloc[-2]:
                death_cross = True

        # Volume trend (10 วันล่าสุด เทียบ 50 วันก่อนหน้า)
        recent_vol_avg = volume.tail(10).mean()
        longer_vol_avg = volume.tail(50).mean()
        volume_surge = (recent_vol_avg / longer_vol_avg) if longer_vol_avg > 0 else None

        notes = []
        signal_score = 0  # รวมคะแนนสัญญาณ (บวก=bullish, ลบ=bearish)

        if macd_cross_bullish:
            notes.append("MACD เพิ่งตัดขึ้นเหนือ Signal Line — สัญญาณ bullish ระยะสั้น")
            signal_score += 1
        elif macd_cross_bearish:
            notes.append("MACD เพิ่งตัดลงใต้ Signal Line — สัญญาณ bearish ระยะสั้น")
            signal_score -= 1
        elif macd_latest > signal_latest:
            notes.append("MACD อยู่เหนือ Signal Line — โมเมนตัมเป็นบวก")
            signal_score += 0.5
        else:
            notes.append("MACD อยู่ใต้ Signal Line — โมเมนตัมเป็นลบ")
            signal_score -= 0.5

        if bb_position is not None:
            if bb_position > 0.95:
                notes.append("ราคาชนขอบบน Bollinger Band — อาจ overbought ระยะสั้น")
                signal_score -= 0.5
            elif bb_position < 0.05:
                notes.append("ราคาชนขอบล่าง Bollinger Band — อาจ oversold ระยะสั้น (มีโอกาสเด้ง)")
                signal_score += 0.5

        if golden_cross:
            notes.append("🌟 เพิ่งเกิด Golden Cross (SMA50 ตัดขึ้นเหนือ SMA200) — สัญญาณ bullish ระยะยาวที่สำคัญ")
            signal_score += 2
        elif death_cross:
            notes.append("⚠️ เพิ่งเกิด Death Cross (SMA50 ตัดลงใต้ SMA200) — สัญญาณ bearish ระยะยาวที่สำคัญ")
            signal_score -= 2

        if volume_surge is not None:
            if volume_surge > 1.5:
                notes.append(f"Volume เฉลี่ย 10 วันสูงกว่าปกติ {volume_surge:.1f}x — มีความสนใจเทรดเพิ่มขึ้นชัดเจน")
            elif volume_surge < 0.6:
                notes.append(f"Volume เฉลี่ย 10 วันต่ำกว่าปกติ ({volume_surge:.1f}x) — ความสนใจเทรดลดลง")

        return {
            "available": True,
            "macd": macd_latest,
            "signal": signal_latest,
            "bb_position": bb_position,
            "golden_cross": golden_cross,
            "death_cross": death_cross,
            "volume_surge_ratio": volume_surge,
            "signal_score": signal_score,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# 6) Google Trends (optional — ต้องติดตั้ง pytrends เพิ่ม)
#    ไม่ใช่ official API ของ Google อาจโดน rate-limit ได้ ใช้แบบ best-effort
# ---------------------------------------------------------------
def analyze_google_trends(query: str) -> dict:
    try:
        from pytrends.request import TrendReq
    except ImportError:
        return {"available": False, "reason": "ยังไม่ได้ติดตั้ง pytrends (pip install pytrends)"}

    try:
        pytrends = TrendReq(hl="th-TH", tz=420)
        pytrends.build_payload([query], timeframe="today 3-m")
        data = pytrends.interest_over_time()
        if data.empty:
            return {"available": False, "reason": "ไม่มีข้อมูล Google Trends สำหรับคำนี้"}

        recent_avg = data[query].tail(7).mean()
        prior_avg = data[query].iloc[-30:-7].mean() if len(data) > 30 else data[query].head(len(data) // 2).mean()

        notes = []
        if prior_avg > 0:
            change_pct = (recent_avg - prior_avg) / prior_avg * 100
            if change_pct > 20:
                notes.append(f"ความสนใจค้นหาเพิ่มขึ้น {change_pct:.0f}% ใน 7 วันล่าสุด เทียบกับก่อนหน้า")
            elif change_pct < -20:
                notes.append(f"ความสนใจค้นหาลดลง {abs(change_pct):.0f}% ใน 7 วันล่าสุด")
            else:
                notes.append("ความสนใจค้นหาค่อนข้างคงที่")

        return {"available": True, "recent_avg": recent_avg, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": f"ดึงข้อมูลไม่สำเร็จ (อาจโดน rate-limit ชั่วคราว): {e}"}


# ---------------------------------------------------------------
# ฟังก์ชันหลัก: รวมทุกสัญญาณเป็นภาพรวมแนวโน้ม
# ---------------------------------------------------------------
def forward_outlook(ticker_symbol: str) -> dict:
    options_data = analyze_options_chain(ticker_symbol)
    insider_data = analyze_insider_activity(ticker_symbol)
    institution_data = analyze_institutional_holders(ticker_symbol)
    analyst_data = analyze_analyst_trend(ticker_symbol)
    technical_data = analyze_technical_advanced(ticker_symbol)

    total_score = 0
    max_possible = 0
    all_notes = []

    # น้ำหนักแต่ละแหล่ง (ปรับได้ตามความสำคัญที่เชื่อถือได้)
    if options_data.get("available") and options_data.get("put_call_ratio_volume") is not None:
        pc = options_data["put_call_ratio_volume"]
        pts = 1.5 if pc < 0.7 else (-1.5 if pc > 1.3 else 0)
        total_score += pts
        max_possible += 1.5
        all_notes.append(("ห่วงโซ่ออปชัน (Options Chain)", options_data["notes"]))

    if insider_data.get("available"):
        pts = 1 if insider_data["buy_count"] > insider_data["sell_count"] else (
            -1 if insider_data["sell_count"] > insider_data["buy_count"] else 0
        )
        total_score += pts
        max_possible += 1
        all_notes.append(("การซื้อขายของผู้บริหาร (Insider)", insider_data["notes"]))

    if institution_data.get("available"):
        total_score += institution_data.get("score_hint", 0) * 0.5
        max_possible += 1
        all_notes.append(("ผู้ถือหุ้นสถาบัน (Institutional Holders)", institution_data["notes"]))

    if analyst_data.get("available") and analyst_data.get("current_score") is not None:
        total_score += analyst_data["current_score"] * 1.5
        max_possible += 1.5
        all_notes.append(("คำแนะนำนักวิเคราะห์ (Analyst Recommendations)", analyst_data["notes"]))

    if technical_data.get("available"):
        total_score += technical_data.get("signal_score", 0) * 0.7
        max_possible += 2.8  # normalize คร่าวๆ
        all_notes.append(("การวิเคราะห์ทางเทคนิค (Technical Analysis)", technical_data["notes"]))

    # แปลงเป็นเปอร์เซ็นต์เอียง (-100 ถึง +100)
    if max_possible > 0:
        lean_pct = max(-100, min(100, (total_score / max_possible) * 100))
    else:
        lean_pct = 0

    if lean_pct > 25:
        verdict = "โน้มเอียงขึ้น (Bullish Tilt)"
    elif lean_pct < -25:
        verdict = "โน้มเอียงลง (Bearish Tilt)"
    else:
        verdict = "กลางๆ ไม่มีสัญญาณชัดเจน (Neutral)"

    return {
        "lean_pct": round(lean_pct, 1),
        "verdict": verdict,
        "sources": all_notes,
        "raw": {
            "options": options_data,
            "insider": insider_data,
            "institution": institution_data,
            "analyst": analyst_data,
            "technical": technical_data,
        },
    }
