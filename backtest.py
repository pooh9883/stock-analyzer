# -*- coding: utf-8 -*-
"""
backtest.py
===========
ทดสอบย้อนหลังจริง (backtest) ว่าสัญญาณ Technical ที่ระบบใช้อยู่ (MACD cross, Golden/Death cross)
ถ้าเชื่อสัญญาณนี้ในอดีตจริงๆ จะ "แม่น" แค่ไหน — เทียบกับการเดาสุ่ม 50%

⚠️ ข้อจำกัดสำคัญ:
- Backtest ได้เฉพาะสัญญาณ Technical เท่านั้น เพราะเป็นข้อมูลเดียวที่มีประวัติย้อนหลังให้คำนวณซ้ำได้
- Options Chain, Insider Transactions, Institutional Holders, Analyst Recommendations
  เป็นข้อมูล "สแนปช็อตปัจจุบัน" เท่านั้น yfinance ไม่มีประวัติย้อนหลังแบบ point-in-time
  ให้ backtest ได้ — จึงบอกความแม่นยำของสัญญาณเหล่านั้นในอดีตไม่ได้
- ผลจากอดีตไม่ได้รับประกันผลในอนาคต (past performance ≠ future results)
"""

import yfinance as yf
import pandas as pd
import numpy as np


def _compute_macd_signal_series(close: pd.Series):
    """คำนวณ MACD signal (bullish/bearish/neutral) ทุกวันจากข้อมูลราคาที่มีอยู่ ณ วันนั้นเท่านั้น"""
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    macd_hist = macd_line - signal_line
    return macd_hist


def _compute_golden_death_cross_series(close: pd.Series):
    sma50 = close.rolling(50).mean()
    sma200 = close.rolling(200).mean()
    return sma50, sma200


def backtest_technical_signal(ticker_symbol: str, holding_days: int = 5, lookback_period: str = "2y") -> dict:
    """
    เดินย้อนหลังทีละวัน: ถ้า MACD histogram เป็นบวก (สัญญาณ bullish) ในวันนั้น
    เช็คว่าราคาอีก holding_days วันข้างหน้าขึ้นจริงไหม (และในทางกลับกันสำหรับ bearish)
    คำนวณ accuracy % เทียบกับการเดาสุ่ม 50%
    """
    try:
        hist = yf.Ticker(ticker_symbol).history(period=lookback_period)
        if hist.empty or len(hist) < 260:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอสำหรับ backtest (ต้องการอย่างน้อย ~2 ปี)"}

        close = hist["Close"].reset_index(drop=True)
        macd_hist = _compute_macd_signal_series(close)
        sma50, sma200 = _compute_golden_death_cross_series(close)

        n = len(close)
        start_idx = 200  # ต้องรอให้ SMA200 มีค่าก่อนเริ่มทดสอบ
        end_idx = n - holding_days  # ต้องเหลือวันพอให้เช็คผลลัพธ์ข้างหน้า

        if end_idx <= start_idx:
            return {"available": False, "reason": "ช่วงเวลาไม่พอสำหรับ backtest"}

        results = {"bullish_correct": 0, "bullish_total": 0, "bearish_correct": 0, "bearish_total": 0}
        trade_log = []

        for i in range(start_idx, end_idx):
            price_now = close.iloc[i]
            price_future = close.iloc[i + holding_days]
            actual_up = price_future > price_now

            # สัญญาณจาก MACD histogram (บวก = bullish, ลบ = bearish)
            signal_bullish = macd_hist.iloc[i] > 0
            signal_bearish = macd_hist.iloc[i] < 0

            if signal_bullish:
                results["bullish_total"] += 1
                if actual_up:
                    results["bullish_correct"] += 1
            elif signal_bearish:
                results["bearish_total"] += 1
                if not actual_up:
                    results["bearish_correct"] += 1

        bullish_acc = (results["bullish_correct"] / results["bullish_total"] * 100) if results["bullish_total"] > 0 else None
        bearish_acc = (results["bearish_correct"] / results["bearish_total"] * 100) if results["bearish_total"] > 0 else None

        total_signals = results["bullish_total"] + results["bearish_total"]
        total_correct = results["bullish_correct"] + results["bearish_correct"]
        overall_acc = (total_correct / total_signals * 100) if total_signals > 0 else None

        notes = []
        if overall_acc is not None:
            edge = overall_acc - 50
            notes.append(f"ทดสอบสัญญาณ MACD ย้อนหลัง {total_signals} ครั้ง ในช่วง {lookback_period} ที่ผ่านมา")
            notes.append(f"ความแม่นยำรวม: {overall_acc:.1f}% (เทียบกับเดาสุ่ม 50% — ได้เปรียบ {edge:+.1f} จุด)")
            if bullish_acc is not None:
                notes.append(f"สัญญาณ Bullish แม่นยำ {bullish_acc:.1f}% ({results['bullish_correct']}/{results['bullish_total']} ครั้ง)")
            if bearish_acc is not None:
                notes.append(f"สัญญาณ Bearish แม่นยำ {bearish_acc:.1f}% ({results['bearish_correct']}/{results['bearish_total']} ครั้ง)")

            if edge > 10:
                notes.append("✅ สัญญาณนี้ในอดีตดีกว่าการเดาสุ่มพอสมควร — แต่ยังไม่รับประกันผลอนาคต")
            elif edge > 0:
                notes.append("สัญญาณนี้ในอดีตดีกว่าเดาสุ่มเล็กน้อย — ควรใช้ร่วมกับสัญญาณอื่นเสมอ ไม่ควรเชื่อเดี่ยวๆ")
            else:
                notes.append("⚠️ สัญญาณนี้ในอดีต 'ไม่ดีไปกว่า' การเดาสุ่มสำหรับหุ้นตัวนี้ — ควรระวังเป็นพิเศษ ไม่ควรให้น้ำหนักสูง")
        else:
            notes.append("ไม่มีสัญญาณเพียงพอในช่วงเวลานี้สำหรับคำนวณ")

        return {
            "available": True,
            "overall_accuracy": overall_acc,
            "bullish_accuracy": bullish_acc,
            "bearish_accuracy": bearish_acc,
            "total_signals": total_signals,
            "holding_days": holding_days,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}
