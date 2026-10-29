# -*- coding: utf-8 -*-
"""
macro.py
========
ข้อมูลเศรษฐกิจมหภาคที่กระทบตลาดหุ้นโดยรวม (ไม่เจาะจงหุ้นตัวใดตัวหนึ่ง)
ดึงฟรีจาก yfinance โดยใช้ ticker ของดัชนี:
- ^VIX = CBOE Volatility Index (ดัชนีความกลัวของตลาด)
- ^TNX = US 10-Year Treasury Yield (อัตราผลตอบแทนพันธบัตรรัฐบาล 10 ปี)
"""

import yfinance as yf
import pandas as pd


def analyze_vix() -> dict:
    try:
        hist = yf.Ticker("^VIX").history(period="6mo")
        if hist.empty:
            return {"available": False, "reason": "ไม่มีข้อมูล VIX"}

        current = hist["Close"].iloc[-1]
        avg_6mo = hist["Close"].mean()

        notes = []
        if current > 30:
            notes.append(f"VIX อยู่ที่ {current:.1f} — สูงมาก ตลาดกำลังกลัว/ผันผวนหนัก (มักเกิดช่วงวิกฤต)")
            market_signal = -1.5
        elif current > 20:
            notes.append(f"VIX อยู่ที่ {current:.1f} — สูงกว่าปกติ ตลาดมีความกังวลระดับหนึ่ง")
            market_signal = -0.5
        elif current < 15:
            notes.append(f"VIX อยู่ที่ {current:.1f} — ต่ำ ตลาดค่อนข้างสงบ/มั่นใจ")
            market_signal = 0.5
        else:
            notes.append(f"VIX อยู่ที่ {current:.1f} — อยู่ในระดับปกติ")
            market_signal = 0

        notes.append(f"ค่าเฉลี่ย 6 เดือนที่ผ่านมา: {avg_6mo:.1f}")

        return {"available": True, "current": current, "avg_6mo": avg_6mo,
                "market_signal": market_signal, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


def analyze_treasury_yield() -> dict:
    try:
        hist = yf.Ticker("^TNX").history(period="3mo")
        if hist.empty or len(hist) < 20:
            return {"available": False, "reason": "ไม่มีข้อมูลอัตราผลตอบแทนพันธบัตร"}

        current = hist["Close"].iloc[-1]
        month_ago = hist["Close"].iloc[-21] if len(hist) > 21 else hist["Close"].iloc[0]
        change = current - month_ago

        notes = [f"US 10-Year Treasury Yield ปัจจุบัน: {current:.2f}%"]

        market_signal = 0
        if change > 0.3:
            notes.append(f"เพิ่มขึ้น {change:+.2f} จุดใน 1 เดือน — อัตราดอกเบี้ยขาขึ้น มักกดดันหุ้นกลุ่มเติบโต/เทคโนโลยี")
            market_signal = -0.5
        elif change < -0.3:
            notes.append(f"ลดลง {change:+.2f} จุดใน 1 เดือน — อัตราดอกเบี้ยขาลง มักเป็นบวกต่อหุ้นกลุ่มเติบโต")
            market_signal = 0.5
        else:
            notes.append(f"ค่อนข้างคงที่ ({change:+.2f} จุดใน 1 เดือน)")

        return {"available": True, "current": current, "change_1m": change,
                "market_signal": market_signal, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


def macro_snapshot() -> dict:
    """สรุปภาพรวม macro — ใช้ประกอบการตัดสินใจ ไม่เจาะจงหุ้นตัวใดตัวหนึ่ง"""
    vix = analyze_vix()
    yield10y = analyze_treasury_yield()

    signal = 0
    max_signal = 0
    sources = []

    if vix.get("available"):
        signal += vix["market_signal"]
        max_signal += 1.5
        sources.append(("VIX — ดัชนีความกลัวตลาด", vix["notes"]))

    if yield10y.get("available"):
        signal += yield10y["market_signal"]
        max_signal += 0.5
        sources.append(("อัตราผลตอบแทนพันธบัตร 10 ปี (US Treasury Yield)", yield10y["notes"]))

    lean_pct = round(max(-100, min(100, (signal / max_signal) * 100)), 1) if max_signal > 0 else 0

    return {"lean_pct": lean_pct, "sources": sources}
