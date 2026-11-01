# -*- coding: utf-8 -*-
"""
chart_page.py
=============
หน้ากราฟเส้นสำหรับ AI Stock Analyzer (ไม่ต้องติดตั้งไลบรารีเพิ่ม ใช้ st.line_chart ของ Streamlit)

วิธีใช้ (วางไฟล์นี้ไว้โฟลเดอร์เดียวกับ levels.py):
1) รันแยกเดี่ยว:     streamlit run chart_page.py
2) เรียกใช้ใน app.py:  from chart_page import render_charts
                       render_charts("NVDA")

มี 3 แท็บ: กราฟราคา (SMA + Bollinger + โซนราคาอ้างอิงจาก levels.py), กราฟ VIX, กราฟ US 10-Year Yield
"""

import pandas as pd
import streamlit as st
import yfinance as yf

try:
    from levels import price_zones
except Exception:  # ถ้าไม่มี levels.py ก็ยังวาดกราฟราคาได้
    price_zones = None

PERIODS = {"3 เดือน": "3mo", "6 เดือน": "6mo", "1 ปี": "1y", "2 ปี": "2y", "5 ปี": "5y"}


@st.cache_data(ttl=300, show_spinner=False)
def _load_history(symbol: str, period: str) -> pd.DataFrame:
    hist = yf.Ticker(symbol).history(period=period)
    if not hist.empty:
        hist.index = pd.to_datetime(hist.index).tz_localize(None)
    return hist


def _download_button(df: pd.DataFrame, name: str):
    st.download_button(
        "⬇️ ดาวน์โหลดข้อมูลกราฟ (CSV)",
        df.to_csv().encode("utf-8-sig"),
        file_name=f"{name}.csv",
        mime="text/csv",
    )


def price_chart(ticker: str, period: str = "1y", show_zones: bool = True):
    # ดึงข้อมูลเกินช่วงที่เลือก เพื่อให้ SMA200 มีค่าตั้งแต่ต้นกราฟ
    fetch_period = "5y" if period in ("2y", "5y") else "2y"
    hist = _load_history(ticker, fetch_period)
    if hist.empty:
        st.warning("ไม่มีข้อมูลราคาสำหรับวาดกราฟ")
        return

    close = hist["Close"]
    df = pd.DataFrame({"ราคาปิด": close})
    df["SMA50"] = close.rolling(50).mean()
    df["SMA200"] = close.rolling(200).mean()
    sma20 = close.rolling(20).mean()
    std20 = close.rolling(20).std()
    df["Bollinger บน"] = sma20 + 2 * std20
    df["Bollinger ล่าง"] = sma20 - 2 * std20

    # ตัดให้เหลือเฉพาะช่วงที่ผู้ใช้เลือก
    days = {"3mo": 63, "6mo": 126, "1y": 252, "2y": 504, "5y": 1260}[period]
    df = df.tail(days)

    if show_zones and price_zones is not None:
        zones = price_zones(ticker)
        if zones.get("available"):
            for z in zones["zones"]:
                if z["name"].startswith(("ค่าเฉลี่ย", "Bollinger")):
                    continue  # สองกลุ่มนี้มีเส้นในกราฟอยู่แล้ว
                df[z["name"]] = z["price"]

    st.line_chart(df)
    st.caption("เส้นแนวนอนคือโซนราคาอ้างอิง ไม่ใช่คำแนะนำซื้อ-ขาย ข้อมูล Yahoo อาจดีเลย์")
    _download_button(df, f"{ticker}_price_chart")


def index_chart(symbol: str, label: str, period: str = "1y"):
    hist = _load_history(symbol, period)
    if hist.empty:
        st.warning(f"ไม่มีข้อมูล {label}")
        return
    df = pd.DataFrame({label: hist["Close"]})
    df["ค่าเฉลี่ย 20 วัน"] = df[label].rolling(20).mean()
    st.line_chart(df)
    _download_button(df, f"{label}_chart".replace(" ", "_"))


def render_charts(ticker: str):
    ticker = ticker.strip().upper()
    period_label = st.radio("ช่วงเวลา", list(PERIODS.keys()), index=2, horizontal=True)
    period = PERIODS[period_label]

    tab_price, tab_vix, tab_yield = st.tabs(["📈 ราคา", "😨 VIX", "🏦 Yield 10 ปี"])
    with tab_price:
        show_zones = st.checkbox("แสดงโซนราคาอ้างอิง", value=True)
        price_chart(ticker, period, show_zones)
    with tab_vix:
        index_chart("^VIX", "VIX", period)
    with tab_yield:
        index_chart("^TNX", "US 10Y Yield (%)", period)


if __name__ == "__main__":
    st.set_page_config(page_title="กราฟหุ้น", layout="wide")
    st.title("📈 กราฟเส้นหุ้น")
    sym = st.text_input("ชื่อหุ้น (ticker)", value="NVDA")
    if sym.strip():
        render_charts(sym)
