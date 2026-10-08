# -*- coding: utf-8 -*-
"""
market_overview.py
===================
ภาพรวมตลาดจากหุ้นตัวใหญ่ที่คัดมาล่วงหน้า (ไม่สามารถสแกนทั้งตลาดฟรีได้จริง)
ใช้ yf.download แบบ batch (ดึงหลายตัวพร้อมกันในคำขอเดียว) ลดความเสี่ยงโดน rate-limit
เทียบกับการเรียก yf.Ticker() ทีละตัวหลายสิบครั้ง
"""

import yfinance as yf
import pandas as pd

# รายชื่อหุ้นตัวใหญ่ที่คัดมาล่วงหน้า แบ่งตามกลุ่มอุตสาหกรรม
SECTOR_LEADERS = {
    "เทคโนโลยี": ["AAPL", "MSFT", "NVDA"],
    "การเงิน": ["JPM", "V", "MA"],
    "สุขภาพ": ["UNH", "LLY", "JNJ"],
    "พลังงาน": ["XOM", "CVX"],
    "สินค้าอุปโภคบริโภค": ["AMZN", "WMT", "PG"],
    "อุตสาหกรรม": ["CAT", "HON"],
    "สื่อสาร/บันเทิง": ["GOOGL", "NFLX", "DIS"],
    "ยานยนต์": ["TSLA"],
}

WATCH_UNIVERSE = sorted({t for lst in SECTOR_LEADERS.values() for t in lst})


def get_market_snapshot() -> dict:
    """ดึงราคาล่าสุด + % เปลี่ยนแปลงของหุ้นทั้งหมดใน WATCH_UNIVERSE แบบ batch คำขอเดียว"""
    try:
        data = yf.download(
            tickers=" ".join(WATCH_UNIVERSE),
            period="5d",
            group_by="ticker",
            progress=False,
            threads=True,
        )
        if data.empty:
            return {"available": False, "reason": "ไม่มีข้อมูลตอบกลับ"}

        results = {}
        for t in WATCH_UNIVERSE:
            try:
                closes = data[t]["Close"].dropna() if len(WATCH_UNIVERSE) > 1 else data["Close"].dropna()
                if len(closes) < 2:
                    continue
                last = float(closes.iloc[-1])
                prev = float(closes.iloc[-2])
                chg_pct = (last - prev) / prev * 100
                results[t] = {"price": last, "change_pct": chg_pct}
            except Exception:
                continue

        if not results:
            return {"available": False, "reason": "ดึงข้อมูลไม่สำเร็จสักตัว (อาจโดน rate-limit ชั่วคราว)"}

        return {"available": True, "data": results}
    except Exception as e:
        return {"available": False, "reason": str(e)}


def top_movers(snapshot: dict, n: int = 5):
    """คืนค่า (gainers, losers) เรียงจากขึ้นแรงสุด/ลงแรงสุด จาก snapshot ที่ดึงมาแล้ว"""
    if not snapshot.get("available"):
        return [], []
    items = [(t, v["change_pct"], v["price"]) for t, v in snapshot["data"].items()]
    items.sort(key=lambda x: x[1], reverse=True)
    gainers = items[:n]
    losers = items[-n:][::-1]  # เรียงจากลงแรงสุดก่อน
    return gainers, losers


def get_normalized_history(tickers: list, period: str = "1mo") -> dict:
    """ดึงราคาปิดย้อนหลังของหลายตัวพร้อมกัน (batch คำขอเดียว) แล้วแปลงเป็น % เทียบวันแรก
    เพื่อให้หุ้นราคาต่างกันมากวาดเทียบในกราฟเส้นเดียวกันได้"""
    try:
        tickers = list(dict.fromkeys(tickers))
        data = yf.download(
            tickers=" ".join(tickers),
            period=period,
            group_by="ticker",
            progress=False,
            threads=True,
        )
        if data.empty:
            return {"available": False, "reason": "ไม่มีข้อมูลตอบกลับ"}

        cols = {}
        for t in tickers:
            try:
                closes = data[t]["Close"].dropna() if len(tickers) > 1 else data["Close"].dropna()
                if len(closes) < 2:
                    continue
                cols[t] = (closes / closes.iloc[0] - 1) * 100
            except Exception:
                continue

        if not cols:
            return {"available": False, "reason": "ดึงข้อมูลย้อนหลังไม่สำเร็จสักตัว"}

        df = pd.DataFrame(cols)
        df.index = pd.to_datetime(df.index).tz_localize(None)
        return {"available": True, "df": df}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ===============================================================
# สแกนกว้างทั้งตลาดสหรัฐ (ใช้ Yahoo Screener + Sector ของ yfinance)
# ต้องใช้ yfinance รุ่นใหม่: pip install -U yfinance
# ถ้าใช้ไม่ได้ ฝั่งแอปจะถอยกลับไปใช้รายชื่อหุ้นที่คัดไว้ด้านบนเอง
# ===============================================================
SECTOR_TH = {
    "technology": "เทคโนโลยี",
    "financial-services": "การเงิน",
    "healthcare": "สุขภาพ",
    "energy": "พลังงาน",
    "consumer-cyclical": "ค้าปลีก/สินค้าฟุ่มเฟือย",
    "consumer-defensive": "สินค้าจำเป็น",
    "industrials": "อุตสาหกรรม",
    "communication-services": "สื่อสาร/บันเทิง",
    "basic-materials": "วัตถุดิบ/เหมืองแร่",
    "real-estate": "อสังหาริมทรัพย์",
    "utilities": "สาธารณูปโภค",
}


def _run_screen(sort_field: str, ascending: bool, size: int, min_cap: float, min_volume: int) -> list:
    from yfinance import EquityQuery as Q
    query = Q("and", [
        Q("eq", ["region", "us"]),
        Q("gte", ["intradaymarketcap", min_cap]),
        Q("gte", ["intradayprice", 5]),
        Q("gt", ["dayvolume", min_volume]),
    ])
    resp = yf.screen(query, size=size, sortField=sort_field, sortAsc=ascending)
    out = []
    for q in (resp or {}).get("quotes", []):
        sym = q.get("symbol")
        price = q.get("regularMarketPrice")
        chg = q.get("regularMarketChangePercent")
        if not sym or price is None or chg is None:
            continue
        out.append({
            "symbol": sym,
            "name": q.get("shortName") or q.get("longName") or sym,
            "price": float(price),
            "change_pct": float(chg),
            "volume": q.get("regularMarketVolume"),
            "market_cap": q.get("marketCap"),
        })
    return out


def get_market_movers(size: int = 10, min_cap: float = 2e9, min_volume: int = 100000) -> dict:
    """หุ้นขึ้นแรง/ลงแรง/ซื้อขายคึกคักสุด จากทั้งตลาดสหรัฐ (กรองบริษัทเล็กและหุ้นไม่มีสภาพคล่องออก)"""
    try:
        gainers = _run_screen("percentchange", False, size, min_cap, min_volume)
        losers = _run_screen("percentchange", True, size, min_cap, min_volume)
        actives = _run_screen("dayvolume", False, size, min_cap, min_volume)
        if not gainers and not losers:
            return {"available": False, "reason": "Yahoo Screener ไม่ส่งข้อมูลกลับมา"}
        return {"available": True, "gainers": gainers, "losers": losers, "actives": actives}
    except Exception as e:
        return {"available": False, "reason": str(e)}


def get_sector_leaders(top_n: int = 5) -> dict:
    """หุ้นใหญ่สุด top_n ตัวของทั้ง 11 กลุ่มอุตสาหกรรม (ตาม Yahoo) พร้อมราคาและ % วันนี้"""
    try:
        sector_symbols = {}
        for key in SECTOR_TH:
            try:
                top = yf.Sector(key).top_companies
                if top is not None and len(top) > 0:
                    sector_symbols[key] = [str(x) for x in list(top.index)[:top_n]]
            except Exception:
                continue
        if not sector_symbols:
            return {"available": False, "reason": "ดึงรายชื่อหุ้นใหญ่ของกลุ่มไม่สำเร็จ"}

        all_syms = sorted({t for lst in sector_symbols.values() for t in lst})
        data = yf.download(
            tickers=" ".join(all_syms), period="5d", group_by="ticker",
            progress=False, threads=True,
        )
        if data.empty:
            return {"available": False, "reason": "ไม่มีข้อมูลราคาตอบกลับ"}

        sectors = {}
        for key, syms in sector_symbols.items():
            rows = []
            for t in syms:
                try:
                    closes = data[t]["Close"].dropna() if len(all_syms) > 1 else data["Close"].dropna()
                    if len(closes) < 2:
                        continue
                    last, prev = float(closes.iloc[-1]), float(closes.iloc[-2])
                    rows.append({"symbol": t, "price": last, "change_pct": (last - prev) / prev * 100})
                except Exception:
                    continue
            if rows:
                avg = sum(r["change_pct"] for r in rows) / len(rows)
                sectors[SECTOR_TH[key]] = {"stocks": rows, "avg_change": avg}

        if not sectors:
            return {"available": False, "reason": "คำนวณราคากลุ่มไม่สำเร็จ"}
        return {"available": True, "sectors": sectors}
    except Exception as e:
        return {"available": False, "reason": str(e)}
