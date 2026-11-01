# -*- coding: utf-8 -*-
"""
sector_history.py  [sector_history v1]
======================================
คำนวณ "ผลตอบแทนย้อนหลัง" ของหุ้นในแต่ละกลุ่มอุตสาหกรรมตามช่วงที่เลือก (5 วัน, 1 เดือน, 3 เดือน, 6 เดือน, ต้นปี, 1 ปี หรือกำหนดวันเอง)
ใช้ราคาปิดรายวันจาก Yahoo Finance (ดึงทีเดียวทั้งชุด เก็บไว้ 15 นาที)
"""
from datetime import date

import pandas as pd
import streamlit as st
import yfinance as yf

# ช่วงที่เลือกได้ -> จำนวนวันทำการย้อนหลัง (None = กรณีพิเศษ)
PERIODS = {"วันนี้": 1, "5 วัน": 5, "1 เดือน": 21, "3 เดือน": 63, "6 เดือน": 126, "ต้นปี (YTD)": None, "1 ปี": 252, "กำหนดวันเอง": None}


@st.cache_data(ttl=900, show_spinner=False)
def _closes(symbols: tuple) -> pd.DataFrame:
    """ตารางราคาปิดรายวัน (คอลัมน์ = หุ้น) ย้อนหลัง 2 ปี"""
    syms = list(symbols)
    try:
        raw = yf.download(syms, period="2y", interval="1d", auto_adjust=False, progress=False, group_by="column", threads=True)
    except Exception:
        return pd.DataFrame()
    if raw is None or raw.empty:
        return pd.DataFrame()
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw[["Close"]].rename(columns={"Close": syms[0]})
    close = close.copy()
    close.index = pd.to_datetime(close.index).tz_localize(None).normalize()
    return close.dropna(how="all")


def _base_row(close: pd.DataFrame, period: str, start: date | None):
    """คืน (ตำแหน่งแถวฐาน, วันที่ฐาน) ที่ใช้เทียบกับราคาล่าสุด"""
    n = len(close)
    if period == "ต้นปี (YTD)":
        prev_year_end = pd.Timestamp(year=close.index[-1].year - 1, month=12, day=31)
        pos = close.index.searchsorted(prev_year_end, side="right") - 1
        pos = max(pos, 0)
    elif period == "กำหนดวันเอง" and start is not None:
        pos = close.index.searchsorted(pd.Timestamp(start), side="right") - 1
        pos = max(pos, 0)
    else:
        back = PERIODS.get(period) or 1
        pos = max(n - 1 - back, 0)
    return pos, close.index[pos].date()


def period_returns(symbols: tuple, period: str, start: date | None = None):
    """
    คืน (dict {symbol: {"price": ราคาล่าสุด, "pct": % ตลอดช่วง}}, วันที่ฐาน, วันที่ล่าสุด)
    ถ้าดึงไม่ได้คืน ({}, None, None)
    """
    close = _closes(tuple(sorted(set(symbols))))
    if close.empty or len(close) < 3:
        return {}, None, None
    pos, base_date = _base_row(close, period, start)
    base, last = close.iloc[pos], close.ffill().iloc[-1]
    out = {}
    for s in close.columns:
        b, l = base.get(s), last.get(s)
        if pd.notna(b) and pd.notna(l) and b > 0:
            out[s] = {"price": float(l), "pct": (float(l) / float(b) - 1) * 100}
    return out, base_date, close.index[-1].date()
