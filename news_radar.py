# -*- coding: utf-8 -*-
"""
news_radar.py
=============
ดึงข่าวจากหลายแหล่งฟรีสำหรับหุ้นใน watchlist ที่ผู้ใช้กำหนดเอง

⚠️ ข้อจำกัดสำคัญ:
- Bloomberg ไม่มี API ฟรี ไม่สามารถดึงเนื้อข่าว Bloomberg โดยตรงได้
- ใช้ Google News RSS แทน (ฟรี ไม่ต้องมี API key) ซึ่งรวมหัวข้อข่าวจากหลายสำนัก
  รวมถึง Bloomberg ด้วย — แต่ได้แค่ "หัวข้อ + ลิงก์" ไม่ใช่เนื้อข่าวเต็ม (ติดลิขสิทธิ์)
- ไม่สามารถสแกน "ทุกหุ้นในตลาดโลก" อัตโนมัติได้ ต้องระบุ watchlist เอง
- การจับกลุ่ม "หุ้นที่ได้อานิสงส์ร่วม" ทำได้แค่ภายใน watchlist ที่ผู้ใช้ใส่ไว้เท่านั้น
"""

import yfinance as yf
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
from urllib.parse import quote
from datetime import datetime


_POSITIVE_WORDS = [
    "beat", "surge", "soar", "upgrade", "record", "growth", "rally", "outperform",
    "strong", "boost", "gain", "rise", "jump", "bullish", "invest", "partnership",
    "deal", "acquisition", "expand", "launch", "approve", "profit", "positive",
]
_NEGATIVE_WORDS = [
    "miss", "plunge", "downgrade", "cut", "lawsuit", "probe", "decline", "fall",
    "weak", "loss", "bearish", "warn", "concern", "risk", "drop", "layoff",
    "recall", "investigation", "fraud", "delay", "shortage",
]


def _score_headline(title: str) -> int:
    t = title.lower()
    pos = sum(1 for w in _POSITIVE_WORDS if w in t)
    neg = sum(1 for w in _NEGATIVE_WORDS if w in t)
    return pos - neg


# ---------------------------------------------------------------
# ดึงข่าวจาก Google News RSS (ฟรี ไม่ต้อง API key)
# ---------------------------------------------------------------
def fetch_google_news(query: str, max_items: int = 8) -> list:
    try:
        url = f"https://news.google.com/rss/search?q={quote(query)}&hl=en-US&gl=US&ceid=US:en"
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=8) as resp:
            data = resp.read()

        root = ET.fromstring(data)
        items = []
        for item in root.findall(".//item")[:max_items]:
            title = item.findtext("title", default="")
            link = item.findtext("link", default="")
            pub_date = item.findtext("pubDate", default="")
            source_el = item.find("{http://news.google.com/rss}source")
            source = source_el.text if source_el is not None else "ไม่ทราบแหล่ง"

            items.append({
                "title": title,
                "link": link,
                "source": source,
                "pub_date": pub_date,
                "sentiment_score": _score_headline(title),
            })
        return items
    except Exception:
        return []


# ---------------------------------------------------------------
# ดึงข่าวจาก yfinance (เสริม)
# ---------------------------------------------------------------
def fetch_yfinance_news(ticker_symbol: str, max_items: int = 5) -> list:
    try:
        stock = yf.Ticker(ticker_symbol)
        news = stock.news or []
        items = []
        for n in news[:max_items]:
            title = n.get("content", {}).get("title") or n.get("title", "")
            link = n.get("content", {}).get("canonicalUrl", {}).get("url") or n.get("link", "")
            if title:
                items.append({
                    "title": title,
                    "link": link,
                    "source": "Yahoo Finance aggregator",
                    "pub_date": "",
                    "sentiment_score": _score_headline(title),
                })
        return items
    except Exception:
        return []


# ---------------------------------------------------------------
# ดึงวัน earnings ที่ใกล้ที่สุด (ใช้เรียงลำดับความเร่งด่วน)
# ---------------------------------------------------------------
def get_next_earnings_date(ticker_symbol: str):
    try:
        stock = yf.Ticker(ticker_symbol)
        cal = stock.calendar
        if cal and "Earnings Date" in cal:
            dates = cal["Earnings Date"]
            if isinstance(dates, list) and dates:
                return dates[0]
            return dates
        return None
    except Exception:
        return None


# ---------------------------------------------------------------
# ฟังก์ชันหลัก: สร้างเรดาร์ข่าวสำหรับ watchlist ทั้งหมด
# ---------------------------------------------------------------
def build_news_radar(tickers: list) -> dict:
    """
    tickers: list ของ ticker symbol เช่น ["NVDA", "SNDK", "AAPL"]
    คืนค่า: dict ที่มีข่าวแยกตามหุ้น + วัน earnings เรียงตามความเร่งด่วน + การจับกลุ่ม sector
    """
    results = {}
    sector_map = {}  # sector -> [tickers]

    for t in tickers:
        t = t.strip().upper()
        if not t:
            continue

        google_news = fetch_google_news(f"{t} stock", max_items=6)
        yf_news = fetch_yfinance_news(t, max_items=4)
        all_news = google_news + yf_news

        # เรียงข่าวที่ sentiment แรงสุด (บวกหรือลบ) ไว้บนสุด
        all_news.sort(key=lambda x: abs(x["sentiment_score"]), reverse=True)

        earnings_date = get_next_earnings_date(t)

        try:
            info = yf.Ticker(t).info
            sector = info.get("sector", "ไม่ทราบกลุ่มธุรกิจ")
            short_name = info.get("shortName", t)
        except Exception:
            sector = "ไม่ทราบกลุ่มธุรกิจ"
            short_name = t

        sector_map.setdefault(sector, []).append(t)

        net_sentiment = sum(n["sentiment_score"] for n in all_news)
        if net_sentiment > 1:
            overall_tone = "ข่าวเอียงบวก"
        elif net_sentiment < -1:
            overall_tone = "ข่าวเอียงลบ"
        else:
            overall_tone = "ข่าวเป็นกลาง"

        results[t] = {
            "name": short_name,
            "sector": sector,
            "earnings_date": earnings_date,
            "news": all_news[:8],
            "overall_tone": overall_tone,
            "net_sentiment": net_sentiment,
        }

    # หากลุ่ม sector ที่มีมากกว่า 1 หุ้น (อาจได้อานิสงส์ร่วมกัน)
    related_groups = {sec: tks for sec, tks in sector_map.items() if len(tks) > 1}

    # เรียง ticker ตามวัน earnings ใกล้สุดก่อน (ถ้ามีข้อมูล)
    def earnings_sort_key(t):
        d = results[t]["earnings_date"]
        if d is None:
            return datetime.max.date() if hasattr(datetime, "max") else None
        try:
            return d
        except Exception:
            return datetime.max.date()

    sorted_tickers = sorted(results.keys(), key=earnings_sort_key)

    return {
        "per_ticker": results,
        "sorted_by_earnings": sorted_tickers,
        "related_groups": related_groups,
    }
