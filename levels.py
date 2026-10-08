# -*- coding: utf-8 -*-
"""
levels.py
=========
1) get_live_quote  — ราคาล่าสุดแบบเบา ๆ สำหรับแผงราคาที่อัปเดตอัตโนมัติ
2) price_zones     — "โซนราคาอ้างอิง" จากข้อเท็จจริงที่คำนวณได้ (แนวรับทางเทคนิค,
                      ราคาเป้าหมายนักวิเคราะห์หักส่วนเผื่อความปลอดภัย, strike ที่มี Put OI สูงสุด)

⚠️ สำคัญ:
- ไม่มีสูตรไหนบอก "ราคาซื้อที่ถูกต้อง" ได้ นี่คือโซนอ้างอิงเพื่อประกอบการตัดสินใจเท่านั้น
  ไม่ใช่คำแนะนำซื้อ-ขาย และไม่รับประกันว่าราคาจะไม่ต่ำกว่าโซนเหล่านี้
- ข้อมูลฟรีจาก Yahoo อาจช้ากว่าราคาจริงเล็กน้อย (บางตลาดถึง ~15 นาที)
"""

import yfinance as yf
import pandas as pd


# ---------------------------------------------------------------
# ราคาล่าสุด (เบา ไม่ดึงข้อมูลหนัก)
# ---------------------------------------------------------------
def get_live_quote(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        fi = stock.fast_info
        last = fi.get("lastPrice")
        prev = fi.get("previousClose")
        if last is None:
            return {"available": False, "reason": "ไม่พบราคาล่าสุด"}

        change = None
        change_pct = None
        if prev:
            change = last - prev
            change_pct = change / prev * 100

        return {
            "available": True,
            "price": float(last),
            "prev_close": float(prev) if prev else None,
            "change": float(change) if change is not None else None,
            "change_pct": float(change_pct) if change_pct is not None else None,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# โซนราคาอ้างอิง
# ---------------------------------------------------------------
def price_zones(ticker_symbol: str, margin_of_safety: float = 0.20) -> dict:
    """
    margin_of_safety: ส่วนลดจากราคาเป้าหมายเฉลี่ยของนักวิเคราะห์ (0.20 = เผื่อไว้ 20%)
    คืนค่า dict: current, zones (เรียงจากราคาสูงไปต่ำ), nearest_below, notes
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="1y")
        if hist.empty or len(hist) < 30:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอ"}

        close = hist["Close"]
        current = float(close.iloc[-1])
        live = get_live_quote(ticker_symbol)
        if live.get("available"):
            current = live["price"]

        zones = []

        # แนวรับทางเทคนิค
        if len(close) >= 50:
            sma50 = float(close.rolling(50).mean().iloc[-1])
            zones.append(("ค่าเฉลี่ย 50 วัน (SMA50)", sma50, "แนวรับระยะกลาง"))
        if len(close) >= 200:
            sma200 = float(close.rolling(200).mean().iloc[-1])
            zones.append(("ค่าเฉลี่ย 200 วัน (SMA200)", sma200, "แนวรับระยะยาว มักถูกจับตามาก"))

        if len(close) >= 20:
            sma20 = close.rolling(20).mean()
            std20 = close.rolling(20).std()
            lower_band = float((sma20 - 2 * std20).iloc[-1])
            if lower_band > 0:
                zones.append(("Bollinger ขอบล่าง", lower_band, "ราคาชนขอบล่างมักเด้งระยะสั้น แต่ไม่เสมอไป"))

        if len(close) >= 63:
            low_3m = float(close.tail(63).min())
            zones.append(("ต่ำสุด 3 เดือน", low_3m, "จุดต่ำที่เคยเกิดขึ้นจริงในรอบ 3 เดือน"))

        # ราคาเป้าหมายนักวิเคราะห์ หักส่วนเผื่อ
        info = {}
        try:
            info = stock.info
        except Exception:
            pass
        target_mean = info.get("targetMeanPrice")
        if target_mean:
            mos_price = float(target_mean) * (1 - margin_of_safety)
            zones.append((
                f"เป้าหมายนักวิเคราะห์ หักเผื่อ {int(margin_of_safety * 100)}%",
                mos_price,
                f"เป้าหมายเฉลี่ย &#36;{float(target_mean):,.2f} — ราคาที่เผื่อพลาดไว้แล้ว",
            ))

        # Put OI สูงสุด (แนวรับทางจิตวิทยาจาก options)
        try:
            expirations = stock.options
            if expirations:
                puts = stock.option_chain(expirations[0]).puts
                if not puts.empty:
                    top_put = float(puts.loc[puts["openInterest"].idxmax(), "strike"])
                    zones.append(("Strike ที่มี Put OI สูงสุด", top_put, "จุดที่คนในตลาด options ป้องกันความเสี่ยงมากสุด"))
        except Exception:
            pass

        if not zones:
            return {"available": False, "reason": "คำนวณโซนไม่ได้"}

        zone_rows = []
        for name, price, note in zones:
            gap_pct = (price - current) / current * 100  # ลบ = ต่ำกว่าราคาปัจจุบัน
            zone_rows.append({"name": name, "price": price, "gap_pct": gap_pct, "note": note})
        zone_rows.sort(key=lambda z: z["price"], reverse=True)

        below = [z for z in zone_rows if z["price"] < current]
        nearest_below = below[0] if below else None

        notes = []
        if nearest_below:
            gap = abs(nearest_below["gap_pct"])
            if gap <= 3:
                notes.append(
                    f"ราคาตอนนี้อยู่ใกล้ {nearest_below['name']} (&#36;{nearest_below['price']:,.2f}) ห่างเพียง {gap:.1f}%"
                )
            else:
                notes.append(
                    f"แนวรับใกล้สุดใต้ราคาปัจจุบันคือ {nearest_below['name']} ที่ &#36;{nearest_below['price']:,.2f} "
                    f"(ต่ำกว่าราคาตอนนี้ {gap:.1f}%)"
                )
        else:
            notes.append("ราคาตอนนี้ต่ำกว่าโซนอ้างอิงทุกตัวที่คำนวณได้ — อาจหลุดแนวรับหลายจุดแล้ว ควรระวังเป็นพิเศษ")

        above = [z for z in zone_rows if z["price"] >= current]
        if above:
            notes.append(f"มีโซนอ้างอิง {len(above)} จุดที่อยู่เหนือราคาปัจจุบัน (ราคาเคลื่อนขึ้นไปหาได้ แต่ก็ทำหน้าที่เป็นแนวต้านได้เช่นกัน)")

        return {
            "available": True,
            "current": current,
            "zones": zone_rows,
            "nearest_below": nearest_below,
            "margin_of_safety": margin_of_safety,
            "notes": notes,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}