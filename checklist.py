# -*- coding: utf-8 -*-
"""
checklist.py
============
เช็กลิสต์หลายเงื่อนไขก่อนซื้อ + ทดสอบย้อนหลังว่า "ถ้าผ่านครบทุกข้อ" ในอดีตวันถัดไปขึ้นจริงบ่อยแค่ไหน

1) run_checklist(ticker)       — เช็กเงื่อนไขของวันนี้ (เงื่อนไขราคา/ตลาด + เงื่อนไขพื้นฐานปัจจุบัน)
2) backtest_checklist(ticker)  — ทดสอบเฉพาะเงื่อนไขราคา/ตลาด (ที่มีข้อมูลย้อนหลังจริง) กับประวัติ 5 ปี

⚠️ สำคัญ:
- ผ่านครบทุกข้อ ไม่ได้แปลว่าพรุ่งนี้ขึ้นแน่ ผลย้อนหลังคือตัวบอกว่าเงื่อนไขชุดนี้ "เคยได้เปรียบ" จริงไหม
- เงื่อนไขยิ่งเยอะ วันที่ผ่านครบจะยิ่งน้อย (ตัวอย่างน้อย = ผลเชื่อถือได้น้อย)
- เงื่อนไขพื้นฐาน (เป้าหมายนักวิเคราะห์, P/E, หนี้) เป็นข้อมูลปัจจุบัน ไม่มีประวัติย้อนหลัง จึง backtest ไม่ได้
"""

import numpy as np
import pandas as pd
import yfinance as yf


# ---------------------------------------------------------------
# ตัวช่วยคำนวณ
# ---------------------------------------------------------------
def _rsi(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _load(ticker: str, period: str = "5y"):
    """ดึงหุ้น + SPY + VIX ในคำขอเดียว คืนค่า (ohlcv, spy_close, vix_close)"""
    syms = list(dict.fromkeys([ticker, "SPY", "^VIX"]))
    data = yf.download(" ".join(syms), period=period, group_by="ticker", progress=False, threads=True)
    if data is None or data.empty:
        return None

    def pick(sym):
        d = data[sym].dropna(how="all")
        d.index = pd.to_datetime(d.index).tz_localize(None).normalize()
        return d

    stock = pick(ticker)
    spy = pick("SPY")["Close"]
    vix = pick("^VIX")["Close"]
    return stock, spy, vix


def _price_conditions(d: pd.DataFrame, spy: pd.Series, vix: pd.Series) -> pd.DataFrame:
    """คืน DataFrame ค่า True/False ของแต่ละเงื่อนไข ทุกวัน (ใช้ข้อมูล ณ วันนั้นเท่านั้น ไม่แอบดูอนาคต)"""
    c, h, l, v = d["Close"], d["High"], d["Low"], d["Volume"]
    spy = spy.reindex(c.index).ffill()
    vix = vix.reindex(c.index).ffill()

    sma50 = c.rolling(50).mean()
    sma200 = c.rolling(200).mean()
    ema12 = c.ewm(span=12, adjust=False).mean()
    ema26 = c.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    macd_hist = macd - macd.ewm(span=9, adjust=False).mean()
    rsi = _rsi(c)
    rng = (h - l).replace(0, np.nan)

    conds = {
        "วันนี้แข็งกว่าตลาด (SPY)": c.pct_change(1) > spy.pct_change(1),
        "5 วันล่าสุดแข็งกว่าตลาด": c.pct_change(5) > spy.pct_change(5),
        "20 วันล่าสุดแข็งกว่าตลาด": c.pct_change(20) > spy.pct_change(20),
        "ราคาอยู่เหนือ SMA200 (ขาขึ้นใหญ่)": c > sma200,
        "ราคาอยู่เหนือ SMA50": c > sma50,
        "SMA50 อยู่เหนือ SMA200": sma50 > sma200,
        "ไม่วิ่งไกลเกินไป (ห่าง SMA50 ไม่เกิน 10%)": (c / sma50 - 1) < 0.10,
        "RSI อยู่ในช่วง 40-70 (ไม่ร้อนแรง/ไม่อ่อนแรงเกินไป)": rsi.between(40, 70),
        "MACD histogram เป็นบวก (โมเมนตัมขึ้น)": macd_hist > 0,
        "ปริมาณซื้อขายไม่น้อยกว่าค่าเฉลี่ย 20 วัน": v >= v.rolling(20).mean(),
        "ปิดในครึ่งบนของกรอบราคาวันนั้น (แรงซื้อชนะ)": ((c - l) / rng) > 0.5,
        "VIX ต่ำกว่า 30 (ตลาดยังไม่ตื่นตระหนก)": vix < 30,
    }
    return pd.DataFrame(conds)


# ---------------------------------------------------------------
# เช็กลิสต์ของวันนี้
# ---------------------------------------------------------------
def _fmt(x, nd=2):
    return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:,.{nd}f}"


def run_checklist(ticker_symbol: str) -> dict:
    try:
        loaded = _load(ticker_symbol, period="2y")
        if loaded is None:
            return {"available": False, "reason": "ดึงข้อมูลราคาไม่ได้"}
        d, spy, vix = loaded
        if len(d) < 210:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอ (ต้องการอย่างน้อย ~210 วันทำการ)"}

        conds = _price_conditions(d, spy, vix)
        last = conds.iloc[-1]

        c = d["Close"]
        spy_a = spy.reindex(c.index).ffill()
        details = {
            "วันนี้แข็งกว่าตลาด (SPY)": f"หุ้น {c.pct_change(1).iloc[-1]*100:+.2f}% / SPY {spy_a.pct_change(1).iloc[-1]*100:+.2f}%",
            "5 วันล่าสุดแข็งกว่าตลาด": f"หุ้น {c.pct_change(5).iloc[-1]*100:+.2f}% / SPY {spy_a.pct_change(5).iloc[-1]*100:+.2f}%",
            "20 วันล่าสุดแข็งกว่าตลาด": f"หุ้น {c.pct_change(20).iloc[-1]*100:+.2f}% / SPY {spy_a.pct_change(20).iloc[-1]*100:+.2f}%",
            "ราคาอยู่เหนือ SMA200 (ขาขึ้นใหญ่)": f"ราคา {_fmt(c.iloc[-1])} / SMA200 {_fmt(c.rolling(200).mean().iloc[-1])}",
            "ราคาอยู่เหนือ SMA50": f"ราคา {_fmt(c.iloc[-1])} / SMA50 {_fmt(c.rolling(50).mean().iloc[-1])}",
            "SMA50 อยู่เหนือ SMA200": f"SMA50 {_fmt(c.rolling(50).mean().iloc[-1])} / SMA200 {_fmt(c.rolling(200).mean().iloc[-1])}",
            "ไม่วิ่งไกลเกินไป (ห่าง SMA50 ไม่เกิน 10%)": f"ห่าง SMA50 {(c.iloc[-1] / c.rolling(50).mean().iloc[-1] - 1)*100:+.1f}%",
            "RSI อยู่ในช่วง 40-70 (ไม่ร้อนแรง/ไม่อ่อนแรงเกินไป)": f"RSI {_fmt(_rsi(c).iloc[-1], 1)}",
            "MACD histogram เป็นบวก (โมเมนตัมขึ้น)": "",
            "ปริมาณซื้อขายไม่น้อยกว่าค่าเฉลี่ย 20 วัน": f"วันนี้ {d['Volume'].iloc[-1]/1e6:,.1f}M / เฉลี่ย {d['Volume'].rolling(20).mean().iloc[-1]/1e6:,.1f}M",
            "ปิดในครึ่งบนของกรอบราคาวันนั้น (แรงซื้อชนะ)": "",
            "VIX ต่ำกว่า 30 (ตลาดยังไม่ตื่นตระหนก)": f"VIX {_fmt(float(vix.iloc[-1]), 1)}",
        }
        price_checks = [(name, bool(last[name]), details.get(name, "")) for name in conds.columns]

        # ----- เงื่อนไขพื้นฐานปัจจุบัน (ไม่มีประวัติย้อนหลัง จึง backtest ไม่ได้) -----
        extra_checks = []
        price_now = float(c.iloc[-1])
        info = {}
        try:
            info = yf.Ticker(ticker_symbol).info or {}
        except Exception:
            pass

        tm = info.get("targetMeanPrice")
        if tm:
            up = (float(tm) / price_now - 1) * 100
            extra_checks.append(("ราคาเป้าหมายนักวิเคราะห์สูงกว่าราคาปัจจุบันเกิน 10%", up > 10, f"เป้าหมายเฉลี่ย {_fmt(float(tm))} ({up:+.1f}%)"))

        fpe, tpe = info.get("forwardPE"), info.get("trailingPE")
        if fpe and tpe and fpe > 0 and tpe > 0:
            extra_checks.append(("Forward P/E ต่ำกว่า Trailing P/E (ตลาดคาดกำไรโต)", fpe < tpe, f"Forward {_fmt(float(fpe))} / Trailing {_fmt(float(tpe))}"))

        de = info.get("debtToEquity")
        if de is not None:
            extra_checks.append(("หนี้สินต่อทุน (D/E) ไม่เกิน 150%", float(de) <= 150, f"D/E {_fmt(float(de), 1)}%"))

        eg = info.get("earningsGrowth")
        if eg is not None:
            extra_checks.append(("กำไรโตเป็นบวก", float(eg) > 0, f"กำไรโต {float(eg)*100:+.1f}%"))

        pm = info.get("profitMargins")
        if pm is not None:
            extra_checks.append(("อัตรากำไรสุทธิเป็นบวก", float(pm) > 0, f"อัตรากำไร {float(pm)*100:.1f}%"))

        try:
            import news_radar
            ed = news_radar.get_next_earnings_date(ticker_symbol)
            if ed is not None:
                ed_ts = pd.Timestamp(ed).tz_localize(None) if pd.Timestamp(ed).tzinfo else pd.Timestamp(ed)
                days = (ed_ts.normalize() - pd.Timestamp.today().normalize()).days
                extra_checks.append(("ไม่ใกล้วันประกาศงบ (เกิน 3 วัน)", not (0 <= days <= 3), f"ประกาศงบอีก {days} วัน" if days >= 0 else "ประกาศงบไปแล้ว"))
        except Exception:
            pass

        all_checks = price_checks + extra_checks
        passed = sum(1 for _, ok, _ in all_checks if ok)
        return {
            "available": True,
            "price_checks": price_checks,
            "extra_checks": extra_checks,
            "passed": passed,
            "total": len(all_checks),
            "price_passed": sum(1 for _, ok, _ in price_checks if ok),
            "price_total": len(price_checks),
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# Backtest เช็กลิสต์
# ---------------------------------------------------------------
def _stats(mask: pd.Series, next1: pd.Series, next5: pd.Series) -> dict:
    m1 = mask & next1.notna()
    m5 = mask & next5.notna()
    n = int(m1.sum())
    return {
        "days": n,
        "win_1d": float((next1[m1] > 0).mean() * 100) if n else None,
        "avg_1d": float(next1[m1].mean() * 100) if n else None,
        "win_5d": float((next5[m5] > 0).mean() * 100) if m5.sum() else None,
        "avg_5d": float(next5[m5].mean() * 100) if m5.sum() else None,
    }


def backtest_checklist(ticker_symbol: str, period: str = "5y") -> dict:
    """ทดสอบเฉพาะเงื่อนไขราคา/ตลาด เทียบ 'ผ่านครบทุกข้อ' กับ 'ทุกวัน' ในอดีต
    ผลลัพธ์วัดจากราคาปิดวันถัดไป และอีก 5 วันข้างหน้า เทียบกับราคาปิดวันที่สัญญาณขึ้น"""
    try:
        loaded = _load(ticker_symbol, period=period)
        if loaded is None:
            return {"available": False, "reason": "ดึงข้อมูลราคาไม่ได้"}
        d, spy, vix = loaded
        if len(d) < 400:
            return {"available": False, "reason": "ข้อมูลย้อนหลังไม่พอสำหรับ backtest (ต้องการอย่างน้อย ~2 ปี)"}

        conds = _price_conditions(d, spy, vix)
        c = d["Close"]
        next1 = c.shift(-1) / c - 1
        next5 = c.shift(-5) / c - 1

        valid = pd.Series(False, index=c.index)
        valid.iloc[200:] = True  # รอให้ SMA200 มีค่าก่อน

        total = conds.shape[1]
        count = conds.sum(axis=1)

        scenarios = {
            "ทุกวัน (ตัวเทียบ)": valid,
            f"ผ่านอย่างน้อย {total - 2} จาก {total} ข้อ": valid & (count >= total - 2),
            f"ผ่านอย่างน้อย {total - 1} จาก {total} ข้อ": valid & (count >= total - 1),
            f"ผ่านครบทั้ง {total} ข้อ": valid & (count >= total),
        }
        rows = [{"scenario": name, **_stats(mask, next1, next5)} for name, mask in scenarios.items()]

        base, full = rows[0], rows[-1]
        notes = []
        if full["days"] < 30:
            notes.append(f"⚠️ ผ่านครบทุกข้อแค่ {full['days']} วันใน 5 ปี ตัวอย่างน้อยเกินไป ผลนี้เชื่อถือไม่ได้")
        elif full["win_1d"] is not None and base["win_1d"] is not None:
            diff = full["win_1d"] - base["win_1d"]
            if diff > 5:
                notes.append(f"ผ่านครบทุกข้อ วันถัดไปขึ้น {full['win_1d']:.0f}% ของครั้ง เทียบกับ {base['win_1d']:.0f}% ของทุกวัน (ดีกว่า {diff:+.1f} จุด) แต่ยังไม่ใช่การรับประกัน")
            elif diff > 0:
                notes.append(f"ผ่านครบทุกข้อ ดีกว่าทุกวันเพียงเล็กน้อย ({diff:+.1f} จุด) ความต่างระดับนี้อาจเป็นแค่ความบังเอิญ")
            else:
                notes.append(f"ผ่านครบทุกข้อ ไม่ได้ดีกว่าทุกวันสำหรับหุ้นตัวนี้ ({diff:+.1f} จุด) เงื่อนไขชุดนี้ไม่ได้ช่วยในอดีต")
        notes.append("วันที่ผ่านเงื่อนไขมักติดกันหลายวัน จึงไม่ใช่ตัวอย่างอิสระ จำนวนวันที่เห็นจึงมากกว่าจำนวน 'เหตุการณ์จริง'")
        notes.append("ผลอดีตไม่รับประกันอนาคต และเงื่อนไขพื้นฐาน (เป้าหมายนักวิเคราะห์ ฯลฯ) ไม่ได้ถูกรวมในการทดสอบนี้")

        return {"available": True, "rows": rows, "total_conditions": total, "notes": notes}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# สัญญาณ "หุ้นเขียว ตลาดแดง" แบบเรียบง่าย + ทดสอบย้อนหลังเฉพาะสัญญาณนี้
# ---------------------------------------------------------------
def relative_signal(ticker_symbol: str, period: str = "5y") -> dict:
    """เทียบหุ้นกับตลาด (SPY) ใน 3 ช่วง (วันนี้/5 วัน/20 วัน) เป็น 4 สถานะ
    และทดสอบย้อนหลังว่า 'วันที่หุ้นเขียวตอนตลาดแดง' วันถัดไปหุ้นขึ้นบ่อยแค่ไหน"""
    try:
        loaded = _load(ticker_symbol, period=period)
        if loaded is None:
            return {"available": False, "reason": "ดึงข้อมูลราคาไม่ได้"}
        d, spy, _ = loaded
        c = d["Close"]
        s = spy.reindex(c.index).ffill()
        if len(c) < 60:
            return {"available": False, "reason": "ข้อมูลราคาย้อนหลังไม่พอ"}

        cards = []
        for n, label in [(1, "วันนี้"), (5, "5 วันล่าสุด"), (20, "20 วันล่าสุด")]:
            sr = float(c.pct_change(n).iloc[-1] * 100)
            mr = float(s.pct_change(n).iloc[-1] * 100)
            if sr > 0 and mr < 0:
                state = "green_vs_red"
            elif sr > 0:
                state = "both_green"
            elif mr < 0:
                state = "both_red"
            else:
                state = "red_vs_green"
            cards.append({"label": label, "stock": sr, "market": mr, "state": state})

        r1, m1 = c.pct_change(), s.pct_change()
        next1 = c.shift(-1) / c - 1
        next5 = c.shift(-5) / c - 1
        valid = pd.Series(True, index=c.index)
        valid.iloc[0] = False
        market_red = valid & (m1 < 0)
        green_red = market_red & (r1 > 0)

        rows = [
            {"scenario": "ทุกวัน (ตัวเทียบ)", **_stats(valid, next1, next5)},
            {"scenario": "เฉพาะวันที่ตลาดแดง", **_stats(market_red, next1, next5)},
            {"scenario": "หุ้นเขียว ตลาดแดง", **_stats(green_red, next1, next5)},
        ]

        base, mred, gr = rows[0], rows[1], rows[2]
        notes = []
        if gr["days"] < 30:
            notes.append(f"⚠️ เกิดสถานการณ์ 'หุ้นเขียว ตลาดแดง' แค่ {gr['days']} วัน ตัวอย่างน้อยเกินไป ผลนี้เชื่อถือไม่ได้")
        elif gr["win_1d"] is not None and mred["win_1d"] is not None:
            diff = gr["win_1d"] - mred["win_1d"]
            if diff > 5:
                notes.append(f"หลังวัน 'หุ้นเขียว ตลาดแดง' วันถัดไปขึ้น {gr['win_1d']:.0f}% ของครั้ง เทียบกับ {mred['win_1d']:.0f}% ของวันที่ตลาดแดงทั่วไป (ดีกว่า {diff:+.1f} จุด) แต่ไม่ใช่การรับประกัน")
            elif diff > 0:
                notes.append(f"หลังวัน 'หุ้นเขียว ตลาดแดง' ดีกว่าเล็กน้อย ({diff:+.1f} จุด) ความต่างระดับนี้อาจเป็นแค่ความบังเอิญ")
            else:
                notes.append(f"หลังวัน 'หุ้นเขียว ตลาดแดง' ไม่ได้ดีกว่าวันที่ตลาดแดงทั่วไปสำหรับหุ้นตัวนี้ ({diff:+.1f} จุด)")
        notes.append("ผลอดีตไม่รับประกันอนาคต และวันที่เข้าเงื่อนไขอาจติดกันเป็นช่วง จึงไม่ใช่ตัวอย่างอิสระทั้งหมด")

        return {"available": True, "cards": cards, "rows": rows, "notes": notes,
                "spy_today": cards[0]["market"]}
    except Exception as e:
        return {"available": False, "reason": str(e)}


# ---------------------------------------------------------------
# สัญญาณสด: หุ้นเทียบตลาดตอนนี้ (ไม่ใช้ backtest) ใช้ข้อมูลล่าสุดแบบ 5 นาที
# ---------------------------------------------------------------
def _state(sr: float, mr: float) -> str:
    if sr > 0 and mr < 0:
        return "green_vs_red"
    if sr > 0:
        return "both_green"
    if mr < 0:
        return "both_red"
    return "red_vs_green"


def live_relative(ticker_symbol: str) -> dict:
    """เทียบหุ้นกับ SPY แบบล่าสุด: ตอนนี้ (เทียบปิดเมื่อวาน), 30 นาที, 1 ชั่วโมง, 5 วัน"""
    try:
        syms = list(dict.fromkeys([ticker_symbol, "SPY"]))
        cards = []

        # 1) ตอนนี้ เทียบราคาปิดเมื่อวาน
        def quote_pct(sym):
            fi = yf.Ticker(sym).fast_info
            last, prev = fi.get("lastPrice"), fi.get("previousClose")
            if last is None or not prev:
                return None
            return (float(last) / float(prev) - 1) * 100

        sr, mr = quote_pct(ticker_symbol), quote_pct("SPY")
        if sr is not None and mr is not None:
            cards.append({"label": "ตอนนี้ (เทียบราคาปิดเมื่อวาน)", "stock": sr, "market": mr, "state": _state(sr, mr)})

        # 2) ช่วงสั้นจากแท่ง 5 นาที
        as_of = None
        stale = False
        intra = yf.download(" ".join(syms), period="5d", interval="5m", group_by="ticker", progress=False, threads=True)
        if intra is not None and not intra.empty:
            def closes(sym):
                s = intra[sym]["Close"].dropna() if len(syms) > 1 else intra["Close"].dropna()
                return s
            cs, cm = closes(ticker_symbol), closes("SPY")
            both = pd.concat([cs.rename("s"), cm.rename("m")], axis=1).dropna()
            if len(both) > 2:
                last_ts = both.index[-1]
                day = both[both.index.date == last_ts.date()]
                for bars, label in [(6, "30 นาทีล่าสุด"), (12, "1 ชั่วโมงล่าสุด")]:
                    n = min(bars, len(day) - 1)
                    if n < 1:
                        continue
                    sr2 = (day["s"].iloc[-1] / day["s"].iloc[-1 - n] - 1) * 100
                    mr2 = (day["m"].iloc[-1] / day["m"].iloc[-1 - n] - 1) * 100
                    suffix = "" if n == bars else f" (ตั้งแต่เปิดตลาด {n*5} นาที)"
                    cards.append({"label": label + suffix, "stock": float(sr2), "market": float(mr2), "state": _state(sr2, mr2)})
                as_of = last_ts
                try:
                    now_ny = pd.Timestamp.now(tz=last_ts.tzinfo)
                    stale = (now_ny - last_ts) > pd.Timedelta(minutes=30)
                except Exception:
                    stale = False

        # 3) 5 วันล่าสุด (รายวัน)
        daily = yf.download(" ".join(syms), period="1mo", interval="1d", group_by="ticker", progress=False, threads=True)
        if daily is not None and not daily.empty:
            def dcloses(sym):
                return daily[sym]["Close"].dropna() if len(syms) > 1 else daily["Close"].dropna()
            ds, dm = dcloses(ticker_symbol), dcloses("SPY")
            if len(ds) > 5 and len(dm) > 5:
                sr5 = float((ds.iloc[-1] / ds.iloc[-6] - 1) * 100)
                mr5 = float((dm.iloc[-1] / dm.iloc[-6] - 1) * 100)
                cards.append({"label": "5 วันล่าสุด", "stock": sr5, "market": mr5, "state": _state(sr5, mr5)})

        if not cards:
            return {"available": False, "reason": "ดึงข้อมูลล่าสุดไม่ได้"}
        return {
            "available": True,
            "cards": cards,
            "as_of": None if as_of is None else as_of.strftime("%d %b %H:%M"),
            "stale": stale,
        }
    except Exception as e:
        return {"available": False, "reason": str(e)}