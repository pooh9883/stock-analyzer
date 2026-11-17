# -*- coding: utf-8 -*-
"""
calendar_ui.py  [calendar v1]
=============================
\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21 \u0e23\u0e27\u0e21\u0e44\u0e27\u0e49\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e40\u0e23\u0e35\u0e22\u0e07\u0e15\u0e32\u0e21\u0e27\u0e31\u0e19:
  \u2022 \U0001f4ca \u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a (\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e01\u0e32\u0e23\u0e08\u0e32\u0e01 Yahoo \u2014 \u0e2d\u0e32\u0e08\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e14\u0e49)
  \u2022 \U0001f4b0 \u0e27\u0e31\u0e19\u0e02\u0e36\u0e49\u0e19\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e2b\u0e21\u0e32\u0e22 XD (Ex-Dividend) \u0e41\u0e25\u0e30\u0e27\u0e31\u0e19\u0e08\u0e48\u0e32\u0e22\u0e1b\u0e31\u0e19\u0e1c\u0e25 (\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e08\u0e32\u0e01\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e02\u0e2d\u0e07 Nasdaq / \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21\u0e08\u0e32\u0e01 Yahoo)
  \u2022 \U0001f3e6 \u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14 FOMC (\u0e15\u0e32\u0e23\u0e32\u0e07\u0e17\u0e35\u0e48\u0e40\u0e1f\u0e14\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e44\u0e27\u0e49\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32 \u2014 \u0e27\u0e31\u0e19\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08\u0e04\u0e37\u0e2d\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 2 \u0e02\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21)
\u0e02\u0e49\u0e2d\u0e08\u0e33\u0e01\u0e31\u0e14: \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1b\u0e31\u0e19\u0e1c\u0e25/\u0e07\u0e1a\u0e21\u0e32\u0e08\u0e32\u0e01 Yahoo \u0e1a\u0e32\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e21\u0e48\u0e21\u0e35 \u0e41\u0e25\u0e30\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e44\u0e14\u0e49 \u0e04\u0e27\u0e23\u0e40\u0e0a\u0e47\u0e01\u0e01\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07
"""
import html
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from urllib.request import Request, urlopen

import pandas as pd
import streamlit as st
import yfinance as yf

import home_ui

# \u0e15\u0e32\u0e23\u0e32\u0e07\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21 FOMC (\u0e27\u0e31\u0e19\u0e40\u0e23\u0e34\u0e48\u0e21, \u0e27\u0e31\u0e19\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08, \u0e21\u0e35 SEP/\u0e41\u0e1c\u0e19\u0e20\u0e39\u0e21\u0e34\u0e08\u0e38\u0e14 \u0e44\u0e2b\u0e21) \u2014 \u0e41\u0e2b\u0e25\u0e48\u0e07: \u0e15\u0e32\u0e23\u0e32\u0e07\u0e17\u0e35\u0e48 Federal Reserve \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28
# \u0e1b\u0e35 2027 \u0e40\u0e1b\u0e47\u0e19\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e15\u0e49\u0e19 (tentative) \u0e2d\u0e32\u0e08\u0e16\u0e39\u0e01\u0e1b\u0e23\u0e31\u0e1a\u0e20\u0e32\u0e22\u0e2b\u0e25\u0e31\u0e07
FOMC = [
    (date(2026, 1, 27), date(2026, 1, 28), False), (date(2026, 3, 17), date(2026, 3, 18), True),
    (date(2026, 4, 28), date(2026, 4, 29), False), (date(2026, 6, 16), date(2026, 6, 17), True),
    (date(2026, 7, 28), date(2026, 7, 29), False), (date(2026, 9, 15), date(2026, 9, 16), True),
    (date(2026, 10, 27), date(2026, 10, 28), False), (date(2026, 12, 8), date(2026, 12, 9), True),
    (date(2027, 1, 26), date(2027, 1, 27), False), (date(2027, 3, 16), date(2027, 3, 17), True),
    (date(2027, 4, 27), date(2027, 4, 28), False), (date(2027, 6, 8), date(2027, 6, 9), True),
    (date(2027, 7, 27), date(2027, 7, 28), False), (date(2027, 9, 14), date(2027, 9, 15), True),
    (date(2027, 10, 26), date(2027, 10, 27), False), (date(2027, 12, 7), date(2027, 12, 8), True),
]

_TH_M = ["\u0e21.\u0e04.", "\u0e01.\u0e1e.", "\u0e21\u0e35.\u0e04.", "\u0e40\u0e21.\u0e22.", "\u0e1e.\u0e04.", "\u0e21\u0e34.\u0e22.", "\u0e01.\u0e04.", "\u0e2a.\u0e04.", "\u0e01.\u0e22.", "\u0e15.\u0e04.", "\u0e1e.\u0e22.", "\u0e18.\u0e04."]
_TH_D = ["\u0e08.", "\u0e2d.", "\u0e1e.", "\u0e1e\u0e24.", "\u0e28.", "\u0e2a.", "\u0e2d\u0e32."]
TYPES = {
    "earn": ("\U0001f4ca \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a", "#fcee0a"),
    "exdiv": ("\U0001f4b0 XD (\u0e02\u0e36\u0e49\u0e19\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e2b\u0e21\u0e32\u0e22\u0e44\u0e21\u0e48\u0e23\u0e31\u0e1a\u0e1b\u0e31\u0e19\u0e1c\u0e25)", "#19f5a5"),
    "paydiv": ("\U0001f4b0 \u0e08\u0e48\u0e32\u0e22\u0e1b\u0e31\u0e19\u0e1c\u0e25", "#19f5a5"),
    "fomc": ("\U0001f3e6 \u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14", "#ff2a6d"),
}


def _e(x):
    return html.escape(str(x if x is not None else ""), quote=True)


def _to_date(x):
    if x is None:
        return None
    try:
        if isinstance(x, (list, tuple)):
            x = x[0] if x else None
            if x is None:
                return None
        ts = pd.Timestamp(x)
        return None if pd.isna(ts) else ts.date()
    except Exception:
        return None


def _one(sym: str) -> dict:
    out = {"earn": None, "exdiv": None, "paydiv": None, "name": sym}
    try:
        t = yf.Ticker(sym)
        cal = t.calendar
        if isinstance(cal, dict):
            out["earn"] = _to_date(cal.get("Earnings Date"))
            out["exdiv"] = _to_date(cal.get("Ex-Dividend Date"))
            out["paydiv"] = _to_date(cal.get("Dividend Date"))
        try:
            out["name"] = (t.info or {}).get("shortName") or sym
        except Exception:
            pass
    except Exception:
        pass
    return out


@st.cache_data(ttl=6 * 3600, show_spinner=False)
def _fetch(symbols: tuple) -> dict:
    res = home_ui._pmap(_one, symbols)
    return {s: (r or {"earn": None, "exdiv": None, "paydiv": None, "name": s}) for s, r in zip(symbols, res)}


# ---------------------------------------------------------------
# \u0e04\u0e49\u0e19\u0e2b\u0e32\u0e07\u0e1a\u0e17\u0e35\u0e48\u0e01\u0e33\u0e25\u0e31\u0e07\u0e08\u0e30\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28 "\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14" \u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34 (\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e07\u0e1a\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e30\u0e02\u0e2d\u0e07 Nasdaq \u2014 \u0e1f\u0e23\u0e35 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e04\u0e35\u0e22\u0e4c)
# ---------------------------------------------------------------
def _money(s) -> float:
    try:
        return float(str(s).replace("$", "").replace(",", "").strip() or 0)
    except Exception:
        return 0.0


@st.cache_data(ttl=3 * 3600, show_spinner=False)
def _nasdaq_day(day_iso: str) -> list:
    try:
        req = Request(
            f"https://api.nasdaq.com/api/calendar/earnings?date={day_iso}",
            headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json, text/plain, */*",
                     "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"},
        )
        with urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode("utf-8"))
        rows = (data.get("data") or {}).get("rows") or []
        out = []
        for x in rows:
            sym = (x.get("symbol") or "").strip().upper()
            if not sym:
                continue
            out.append({"sym": sym, "name": x.get("name") or sym, "cap": _money(x.get("marketCap")),
                        "time": x.get("time") or "", "eps": x.get("epsForecast") or "",
                        "qtr": x.get("fiscalQuarterEnding") or "", "date": day_iso})
        return out
    except Exception:
        return []


_TIME_TH = {"time-pre-market": "\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e25\u0e32\u0e14\u0e40\u0e1b\u0e34\u0e14", "time-after-hours": "\u0e2b\u0e25\u0e31\u0e07\u0e15\u0e25\u0e32\u0e14\u0e1b\u0e34\u0e14"}


def _us_dst(d: date) -> bool:
    """\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32\u0e2d\u0e2d\u0e21\u0e41\u0e2a\u0e07\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e2d\u0e32\u0e17\u0e34\u0e15\u0e22\u0e4c\u0e17\u0e35\u0e48 2 \u0e02\u0e2d\u0e07\u0e21\u0e35\u0e19\u0e32\u0e04\u0e21 \u0e16\u0e36\u0e07\u0e2d\u0e32\u0e17\u0e34\u0e15\u0e22\u0e4c\u0e41\u0e23\u0e01\u0e02\u0e2d\u0e07\u0e1e\u0e24\u0e28\u0e08\u0e34\u0e01\u0e32\u0e22\u0e19"""
    def nth_sun(y, m, n):
        first = date(y, m, 1)
        return first + timedelta(days=(6 - first.weekday()) % 7 + 7 * (n - 1))
    return nth_sun(d.year, 3, 2) <= d < nth_sun(d.year, 11, 1)


def _th_time_txt(d: date, kind: str) -> str:
    """\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a\u0e42\u0e14\u0e22\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 \u0e40\u0e1b\u0e47\u0e19\u0e40\u0e27\u0e25\u0e32\u0e44\u0e17\u0e22 (d = \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e32\u0e21\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e2b\u0e23\u0e31\u0e10) \u2014 Nasdaq \u0e1a\u0e2d\u0e01\u0e41\u0e04\u0e48\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e1b\u0e34\u0e14/\u0e2b\u0e25\u0e31\u0e07\u0e1b\u0e34\u0e14 \u0e44\u0e21\u0e48\u0e1a\u0e2d\u0e01\u0e40\u0e27\u0e25\u0e32\u0e40\u0e1b\u0e4a\u0e30
    \u0e2b\u0e25\u0e31\u0e07\u0e15\u0e25\u0e32\u0e14\u0e1b\u0e34\u0e14\u0e2a\u0e48\u0e27\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28 16:00\u201317:00 \u0e19. ET \u00b7 \u0e01\u0e48\u0e2d\u0e19\u0e15\u0e25\u0e32\u0e14\u0e40\u0e1b\u0e34\u0e14\u0e2a\u0e48\u0e27\u0e19\u0e43\u0e2b\u0e0d\u0e48 06:00\u201308:30 \u0e19. ET"""
    if kind == "time-after-hours":
        h0, m0, h1, m1 = 16, 0, 17, 0
    elif kind == "time-pre-market":
        h0, m0, h1, m1 = 6, 0, 8, 30
    else:
        return ""
    diff = timedelta(hours=11 if _us_dst(d) else 12)       # ET -> \u0e40\u0e27\u0e25\u0e32\u0e44\u0e17\u0e22 (UTC+7)
    a = datetime(d.year, d.month, d.day, h0, m0) + diff
    b = datetime(d.year, d.month, d.day, h1, m1) + diff
    day = a.date()
    return "\u0e44\u0e17\u0e22\u0e23\u0e32\u0e27 {}\u2013{} \u0e19. ({} {} {})".format(a.strftime("%H:%M"), b.strftime("%H:%M"), _TH_D[day.weekday()], day.day, _TH_M[day.month - 1])


def auto_earnings(horizon_days: int, min_cap: float, today: date = None, limit: int = 80) -> list:
    """\u0e07\u0e1a\u0e17\u0e35\u0e48\u0e08\u0e30\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e49\u0e32\u0e07\u0e2b\u0e19\u0e49\u0e32 \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14 >= min_cap \u0e40\u0e23\u0e35\u0e22\u0e07\u0e15\u0e32\u0e21\u0e27\u0e31\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e15\u0e32\u0e21\u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17"""
    today = today or date.today()
    days = [today + timedelta(days=i) for i in range(horizon_days + 1)]
    days = [d for d in days if d.weekday() < 5]
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(lambda d: _nasdaq_day(d.isoformat()), days))
    events = []
    for d, rows in zip(days, res):
        for r in rows:
            if r["cap"] < min_cap:
                continue
            bits = []
            if r["time"] in _TIME_TH:
                bits.append(_TIME_TH[r["time"]] + " (" + _th_time_txt(d, r["time"]) + ")")
            if r["eps"]:
                bits.append(f"\u0e04\u0e32\u0e14 EPS {r['eps']}")
            if r["qtr"]:
                bits.append(f"\u0e07\u0e27\u0e14 {r['qtr']}")
            if r["cap"]:
                bits.append("\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14 " + (f"${r['cap'] / 1e12:.2f}T" if r["cap"] >= 1e12 else f"${r['cap'] / 1e9:,.0f}B"))
            events.append({"date": d, "kind": "earn", "sym": r["sym"], "name": r["name"],
                           "note": " \u00b7 ".join(bits), "cap": r["cap"]})
    events.sort(key=lambda e: (e["date"], -e.get("cap", 0)))
    # \u0e08\u0e33\u0e01\u0e31\u0e14\u0e08\u0e33\u0e19\u0e27\u0e19\u0e15\u0e48\u0e2d\u0e27\u0e31\u0e19\u0e44\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e25\u0e49\u0e19: \u0e40\u0e2d\u0e32\u0e15\u0e31\u0e27\u0e43\u0e2b\u0e0d\u0e48\u0e2a\u0e38\u0e14\u0e01\u0e48\u0e2d\u0e19 \u0e23\u0e27\u0e21\u0e41\u0e25\u0e49\u0e27\u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 limit
    keep, total = [], 0
    for e in sorted(events, key=lambda e: -e.get("cap", 0)):
        if total < limit:
            keep.append(e)
            total += 1
    keep.sort(key=lambda e: (e["date"], -e.get("cap", 0)))
    return keep


# ---------------------------------------------------------------
# \u0e1b\u0e31\u0e19\u0e1c\u0e25 "\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14" \u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34 (\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e30\u0e02\u0e2d\u0e07 Nasdaq \u2014 \u0e1f\u0e23\u0e35 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e04\u0e35\u0e22\u0e4c)
# \u0e14\u0e36\u0e07\u0e17\u0e35\u0e25\u0e30\u0e27\u0e31\u0e19 (\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 = \u0e27\u0e31\u0e19 XD) \u00b7 \u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e01\u0e23\u0e2d\u0e07\u0e42\u0e14\u0e22\u0e08\u0e31\u0e1a\u0e04\u0e39\u0e48\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e01\u0e31\u0e1a\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e17\u0e35\u0e48\u0e21\u0e35\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14 (\u0e14\u0e36\u0e07\u0e04\u0e23\u0e31\u0e49\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27/\u0e27\u0e31\u0e19)
# ---------------------------------------------------------------
_NQ_HEADERS = {"User-Agent": "Mozilla/5.0", "Accept": "application/json, text/plain, */*",
               "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}


def _nq_get(url: str, timeout: int = 12):
    req = Request(url, headers=_NQ_HEADERS)
    with urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def _us_date(x):
    """'02/10/2025' -> date \u00b7 \u0e04\u0e48\u0e32\u0e27\u0e48\u0e32\u0e07/N/A -> None"""
    try:
        return datetime.strptime(str(x).strip(), "%m/%d/%Y").date()
    except Exception:
        return None


@st.cache_data(ttl=24 * 3600, show_spinner=False)
def _cap_map() -> dict:
    """{\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19: \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14} \u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14 (ETF/\u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19\u0e44\u0e21\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e19\u0e35\u0e49 \u0e08\u0e36\u0e07\u0e16\u0e39\u0e01\u0e01\u0e23\u0e2d\u0e07\u0e2d\u0e2d\u0e01\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17)"""
    try:
        d = _nq_get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true", timeout=20)
        rows = ((d.get("data") or {}).get("rows")) or ((d.get("data") or {}).get("table") or {}).get("rows") or []
        out = {}
        for x in rows:
            sym = (x.get("symbol") or "").strip().upper()
            if sym:
                out[sym] = _money(x.get("marketCap"))
        return out
    except Exception:
        return {}


@st.cache_data(ttl=3 * 3600, show_spinner=False)
def _nasdaq_div_day(day_iso: str) -> list:
    try:
        d = _nq_get(f"https://api.nasdaq.com/api/calendar/dividends?date={day_iso}")
        data = d.get("data") or {}
        rows = (data.get("calendar") or {}).get("rows") or data.get("rows") or []
        out = []
        for x in rows:
            sym = (x.get("symbol") or "").strip().upper()
            if not sym:
                continue
            out.append({"sym": sym, "name": x.get("companyName") or x.get("name") or sym,
                        "ex": _us_date(x.get("dividend_Ex_Date")) or _us_date(day_iso) or None,
                        "pay": _us_date(x.get("payment_Date")), "rec": _us_date(x.get("record_Date")),
                        "rate": _money(x.get("dividend_Rate")), "annual": _money(x.get("indicated_Annual_Dividend"))})
        return out
    except Exception:
        return []


def _fmt_us(d):
    return f"{d.day} {_TH_M[d.month - 1]}" if d else "\u2014"


def auto_dividends(horizon_days: int, min_cap: float, kinds: set, today: date = None, limit: int = 120) -> tuple:
    """\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e02\u0e49\u0e32\u0e07\u0e2b\u0e19\u0e49\u0e32 \u2192 (\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c XD/\u0e08\u0e48\u0e32\u0e22\u0e1b\u0e31\u0e19\u0e1c\u0e25, \u0e21\u0e35\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14\u0e44\u0e2b\u0e21)"""
    today = today or date.today()
    days = [today + timedelta(days=i) for i in range(horizon_days + 1)]
    days = [d for d in days if d.weekday() < 5]
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(lambda d: _nasdaq_div_day(d.isoformat()), days))
    caps = _cap_map()
    have_caps = bool(caps)
    events, seen = [], set()
    for d, rows in zip(days, res):
        for r in rows:
            cap = caps.get(r["sym"], 0.0)
            if have_caps and cap < min_cap:
                continue
            ex_d = r["ex"] or d
            key = (r["sym"], ex_d)
            if key in seen:
                continue
            seen.add(key)
            bits = []
            if r["rate"]:
                bits.append(f"\u0e1b\u0e31\u0e19\u0e1c\u0e25 ${r['rate']:.4g}/\u0e2b\u0e38\u0e49\u0e19")
            if r["annual"]:
                bits.append(f"\u0e1b\u0e35\u0e25\u0e30\u0e23\u0e32\u0e27 ${r['annual']:.4g}")
            if r["rec"]:
                bits.append("\u0e27\u0e31\u0e19\u0e1b\u0e34\u0e14\u0e2a\u0e21\u0e38\u0e14 " + _fmt_us(r["rec"]))
            if r["pay"]:
                bits.append("\u0e08\u0e48\u0e32\u0e22\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 " + _fmt_us(r["pay"]))
            if cap:
                bits.append("\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14 " + (f"${cap / 1e12:.2f}T" if cap >= 1e12 else f"${cap / 1e9:,.0f}B"))
            note = " \u00b7 ".join(bits)
            if "exdiv" in kinds and 0 <= (ex_d - today).days <= horizon_days:
                events.append({"date": ex_d, "kind": "exdiv", "sym": r["sym"], "name": r["name"], "note": note, "cap": cap, "rate": r["annual"]})
            if "paydiv" in kinds and r["pay"] and 0 <= (r["pay"] - today).days <= horizon_days:
                events.append({"date": r["pay"], "kind": "paydiv", "sym": r["sym"], "name": r["name"],
                               "note": note.replace("\u0e08\u0e48\u0e32\u0e22\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 " + _fmt_us(r["pay"]), "").strip(" \u00b7"), "cap": cap, "rate": r["annual"]})
    # \u0e16\u0e49\u0e32\u0e21\u0e32\u0e01\u0e40\u0e01\u0e34\u0e19 \u0e40\u0e2d\u0e32\u0e15\u0e31\u0e27\u0e43\u0e2b\u0e0d\u0e48 (\u0e2b\u0e23\u0e37\u0e2d\u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14 \u0e40\u0e2d\u0e32\u0e17\u0e35\u0e48\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e2a\u0e39\u0e07) \u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19
    keep = sorted(events, key=lambda e: (-e.get("cap", 0), -e.get("rate", 0)))[:limit]
    keep.sort(key=lambda e: (e["date"], e["kind"], -e.get("cap", 0)))
    return keep, have_caps


def th_date(d: date) -> str:
    return f"{_TH_D[d.weekday()]} {d.day} {_TH_M[d.month - 1]} {d.year + 543}"


def build_events(symbols: tuple, kinds: set, horizon_days: int, today: date = None) -> list:
    today = today or date.today()
    events = []
    data = _fetch(symbols) if symbols and kinds & {"earn", "exdiv", "paydiv"} else {}
    for s, d in data.items():
        for k in ("earn", "exdiv", "paydiv"):
            if k in kinds and d.get(k):
                events.append({"date": d[k], "kind": k, "sym": s, "name": d["name"], "note": ""})
    if "fomc" in kinds:
        for start, decide, sep in FOMC:
            events.append({"date": decide, "kind": "fomc", "sym": "FOMC", "name": "Federal Reserve",
                           "note": f"\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21 {start.day}\u2013{decide.day} {_TH_M[decide.month - 1]} \u00b7 \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49"
                                   + (" \u00b7 \u0e21\u0e35\u0e41\u0e1c\u0e19\u0e20\u0e39\u0e21\u0e34\u0e08\u0e38\u0e14 (SEP)" if sep else "")
                                   + (" \u00b7 \u0e15\u0e32\u0e23\u0e32\u0e07\u0e1b\u0e35 2027 \u0e40\u0e1b\u0e47\u0e19\u0e41\u0e1a\u0e1a\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e15\u0e49\u0e19" if decide.year >= 2027 else "")})
    out = [e for e in events if 0 <= (e["date"] - today).days <= horizon_days]
    out.sort(key=lambda e: (e["date"], e["kind"], e["sym"]))
    return out


# ---------------------------------------------------------------
# \u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19 (Sector) + \u0e1c\u0e25\u0e07\u0e32\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 + \u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a
# ---------------------------------------------------------------
_YF_SECTOR_ETF = {
    "Technology": "XLK", "Financial Services": "XLF", "Healthcare": "XLV", "Energy": "XLE",
    "Consumer Cyclical": "XLY", "Consumer Defensive": "XLP", "Industrials": "XLI",
    "Communication Services": "XLC", "Basic Materials": "XLB", "Utilities": "XLU", "Real Estate": "XLRE",
}


def _sector_raw(sym: str) -> dict:
    try:
        info = yf.Ticker(sym).info or {}
        return {"sector": info.get("sector") or "", "industry": info.get("industry") or ""}
    except Exception:
        return {"sector": "", "industry": ""}


@st.cache_data(ttl=24 * 3600, show_spinner=False)
def _sector_batch(symbols: tuple) -> dict:
    res = home_ui._pmap(_sector_raw, symbols)
    return {s: (r or {"sector": "", "industry": ""}) for s, r in zip(symbols, res)}


def _sector_perf() -> dict:
    """\u0e1c\u0e25\u0e07\u0e32\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21 (ETF \u0e15\u0e31\u0e27\u0e41\u0e17\u0e19 SPDR) \u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49/5 \u0e27\u0e31\u0e19/1 \u0e40\u0e14\u0e37\u0e2d\u0e19 \u0e04\u0e35\u0e22\u0e4c\u0e14\u0e49\u0e27\u0e22\u0e0a\u0e37\u0e48\u0e2d ETF"""
    try:
        data = home_ui._sectors()
    except Exception:
        return {}
    name2etf = {n: e for n, e in home_ui.SECTORS}
    return {name2etf[n]: dict(v, name=n) for n, v in data.items() if n in name2etf}


def _group_of(sec: dict, perf: dict):
    """\u0e04\u0e37\u0e19 {"name","etf","m1","d5"} \u0e02\u0e2d\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21\u0e17\u0e35\u0e48\u0e2b\u0e38\u0e49\u0e19\u0e2d\u0e22\u0e39\u0e48 \u0e2b\u0e23\u0e37\u0e2d None"""
    etf = _YF_SECTOR_ETF.get((sec or {}).get("sector", ""))
    p = perf.get(etf) if etf else None
    if not p:
        return None
    return {"name": p["name"], "etf": etf, "m1": p["1m"], "d5": p["5d"], "industry": sec.get("industry", "")}


@st.cache_data(ttl=6 * 3600, show_spinner=False)
def _etf_close(etf: str):
    try:
        h = yf.Ticker(etf).history(period="5y", interval="1d", auto_adjust=True)["Close"].dropna()
        h.index = pd.to_datetime(h.index).tz_localize(None).normalize()
        return h
    except Exception:
        return None


@st.cache_data(ttl=3600, show_spinner=False)
def _reactions(sym: str, etf: str) -> list:
    """\u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a\u0e41\u0e04\u0e48\u0e44\u0e2b\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a 8 \u0e04\u0e23\u0e31\u0e49\u0e07\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 (\u0e1b\u0e34\u0e14\u0e01\u0e48\u0e2d\u0e19\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28 -> \u0e1b\u0e34\u0e14\u0e27\u0e31\u0e19\u0e16\u0e31\u0e14\u0e08\u0e32\u0e01\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28 \u0e04\u0e23\u0e2d\u0e1a\u0e04\u0e25\u0e38\u0e21\u0e17\u0e31\u0e49\u0e07\u0e01\u0e48\u0e2d\u0e19/\u0e2b\u0e25\u0e31\u0e07\u0e15\u0e25\u0e32\u0e14)
    \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e1c\u0e25\u0e07\u0e32\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 1 \u0e40\u0e14\u0e37\u0e2d\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e04\u0e23\u0e31\u0e49\u0e07\u0e19\u0e31\u0e49\u0e19"""
    try:
        import chart_pro
        d = chart_pro._load_daily(sym)
        if d is None or len(d) < 60:
            return []
        c = d["Close"].astype(float)
        dates = [x for x in chart_pro._load_earnings(sym) if x < pd.Timestamp(date.today())][-8:]
        ec = _etf_close(etf) if etf else None
        out = []
        for dt in dates:
            pos = int(c.index.searchsorted(dt))
            if pos < 1 or pos + 1 >= len(c):
                continue
            grp = None
            if ec is not None and len(ec) > 30:
                k = int(ec.index.searchsorted(dt)) - 1
                if k >= 22:
                    grp = float((ec.iloc[k] / ec.iloc[k - 21] - 1) * 100)
            out.append({"date": dt.date(), "react": float((c.iloc[pos + 1] / c.iloc[pos - 1] - 1) * 100), "grp": grp})
        return out
    except Exception:
        return []


@st.cache_data(ttl=6 * 3600, show_spinner=False)
def _eps_beats(sym: str) -> dict:
    try:
        import deep
        r = deep.analyze_earnings_surprise(sym)
        return r if r.get("available") else {}
    except Exception:
        return {}


def _pct_color(x):
    return "#19f5a5" if x >= 0 else "#ff5a85"


_GRP_CSS = """<style>
.cal-gs{display:inline-flex;align-items:center;gap:8px;margin-top:8px;padding:4px 12px 4px 6px;
 background:linear-gradient(90deg,rgba(var(--g),.20),rgba(var(--g),.04));border-left:3px solid rgb(var(--g))}
.cal-gi{width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:13px;
 background:rgba(var(--g),.16);border:1px solid rgba(var(--g),.5)}
.cal-gp{font-size:13px;color:rgb(var(--g));font-weight:700;filter:brightness(1.25)}
</style>"""


def _perf_bar(x, cap=6.0):
    """\u0e41\u0e16\u0e1a\u0e1c\u0e25\u0e07\u0e32\u0e19\u0e41\u0e1a\u0e1a\u0e0b\u0e49\u0e32\u0e22-\u0e02\u0e27\u0e32\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e01\u0e25\u0e32\u0e07 (\u0e25\u0e1a = \u0e0b\u0e49\u0e32\u0e22 \u0e41\u0e14\u0e07 / \u0e1a\u0e27\u0e01 = \u0e02\u0e27\u0e32 \u0e40\u0e02\u0e35\u0e22\u0e27)"""
    w = min(abs(x), cap) / cap * 50
    if x >= 0:
        return '<i class="r" style="left:50%;width:' + format(w, ".1f") + '%;background:linear-gradient(90deg,#00a869,#8dffd0)"></i>'
    return '<i class="l" style="left:' + format(50 - w, ".1f") + '%;width:' + format(w, ".1f") + '%;background:linear-gradient(90deg,#ff2457,#ff8aa8)"></i>'


_SEC_ICON = {"\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35": "\U0001f4bb", "\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19": "\U0001f3e6", "\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e": "\U0001f48a", "\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19": "\u26fd", "\u0e04\u0e49\u0e32\u0e1b\u0e25\u0e35\u0e01/\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e1f\u0e38\u0e48\u0e21\u0e40\u0e1f\u0e37\u0e2d\u0e22": "\U0001f6cd\ufe0f",
             "\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19": "\U0001f6d2", "\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21": "\U0001f3ed", "\u0e2a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23/\u0e1a\u0e31\u0e19\u0e40\u0e17\u0e34\u0e07": "\U0001f4e1", "\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a": "\u26cf\ufe0f", "\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04": "\u26a1", "\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e23\u0e34\u0e21\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c": "\U0001f3e0"}


_SEC_COLOR = {"\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35": "#00d4ff", "\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19": "#f5c542", "\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e": "#34d399", "\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19": "#ff9f43",
              "\u0e04\u0e49\u0e32\u0e1b\u0e25\u0e35\u0e01/\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e1f\u0e38\u0e48\u0e21\u0e40\u0e1f\u0e37\u0e2d\u0e22": "#b388ff", "\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19": "#e879f9", "\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21": "#8aa4ff",
              "\u0e2a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23/\u0e1a\u0e31\u0e19\u0e40\u0e17\u0e34\u0e07": "#fb7185", "\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a": "#d2a679", "\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04": "#2dd4bf", "\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e23\u0e34\u0e21\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c": "#bef264"}


def _grp_line(g):
    """\u0e41\u0e16\u0e1a\u0e01\u0e25\u0e38\u0e48\u0e21\u0e43\u0e19\u0e01\u0e32\u0e23\u0e4c\u0e14\u0e07\u0e1a: \u0e44\u0e2d\u0e04\u0e2d\u0e19 + \u0e0a\u0e37\u0e48\u0e2d\u0e01\u0e25\u0e38\u0e48\u0e21 \u0e41\u0e22\u0e01\u0e2a\u0e35\u0e15\u0e32\u0e21\u0e01\u0e25\u0e38\u0e48\u0e21 (\u0e44\u0e21\u0e48\u0e21\u0e35\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02)"""
    if not g:
        return ""
    h = _SEC_COLOR.get(g["name"], "#00d4ff").lstrip("#")
    rgb = ",".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))
    return ('<div class="cal-gs" style="--g:' + rgb + '"><div class="cal-gi">' + _SEC_ICON.get(g["name"], "\U0001f3f7") + '</div>'
            '<span class="cal-gp">\u0e01\u0e25\u0e38\u0e48\u0e21' + _e(g["name"]) + '</span></div>')


def _render_detail(sym: str, g, sec: dict):
    """\u0e41\u0e1c\u0e07\u0e14\u0e39\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14: \u0e01\u0e25\u0e38\u0e48\u0e21 + \u0e18\u0e35\u0e21 + \u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a + \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e04\u0e34\u0e14 '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e36\u0e49\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e07\u0e1a -> \u0e2b\u0e38\u0e49\u0e19\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a'"""
    import chart_pro
    box = "background:rgba(12,14,28,.82);border:1px solid rgba(0,240,255,.2);padding:12px 14px;margin:8px 0 14px"
    lines = []
    # 1) \u0e01\u0e25\u0e38\u0e48\u0e21 vs \u0e2b\u0e38\u0e49\u0e19 \u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49
    m1s = None
    try:
        dd = chart_pro._load_daily(sym)
        if dd is not None and len(dd) > 23:
            cc = dd["Close"].astype(float)
            m1s = float((cc.iloc[-1] / cc.iloc[-22] - 1) * 100)
    except Exception:
        pass
    if g:
        txt = "\u0e01\u0e25\u0e38\u0e48\u0e21 <b>" + _e(g["name"]) + "</b> (" + _e(g["etf"]) + ")"
        if g.get("industry"):
            txt += " \u00b7 \u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21 " + _e(g["industry"])
        lines.append(("\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e2d\u0e22\u0e39\u0e48\u0e01\u0e25\u0e38\u0e48\u0e21", txt))
        lines.append(("\u0e01\u0e25\u0e38\u0e48\u0e21\u0e19\u0e35\u0e49\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32", "5 \u0e27\u0e31\u0e19 <b style=\"color:" + _pct_color(g["d5"]) + "\">" + format(g["d5"], "+.2f") + "%</b> \u00b7 "
                      "1 \u0e40\u0e14\u0e37\u0e2d\u0e19 <b style=\"color:" + _pct_color(g["m1"]) + "\">" + format(g["m1"], "+.2f") + "%</b>"))
    if m1s is not None:
        extra = ""
        if g:
            diff = m1s - g["m1"]
            extra = " \u00b7 " + ("\u0e19\u0e33\u0e01\u0e25\u0e38\u0e48\u0e21 " if diff >= 0 else "\u0e15\u0e32\u0e21\u0e2b\u0e25\u0e31\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21 ") + "<b>" + format(abs(diff), ".1f") + "%</b>" + \
                    (" (\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e32\u0e08\u0e23\u0e31\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e14\u0e35\u0e44\u0e1b\u0e1a\u0e32\u0e07\u0e2a\u0e48\u0e27\u0e19\u0e41\u0e25\u0e49\u0e27)" if diff > 8 else "")
        lines.append((sym + " 1 \u0e40\u0e14\u0e37\u0e2d\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32", "<b style=\"color:" + _pct_color(m1s) + "\">" + format(m1s, "+.1f") + "%</b>" + extra))
    # 2) \u0e18\u0e35\u0e21\u0e17\u0e35\u0e48\u0e2b\u0e38\u0e49\u0e19\u0e2d\u0e22\u0e39\u0e48 (\u0e08\u0e32\u0e01\u0e2b\u0e19\u0e49\u0e32\u0e18\u0e35\u0e21)
    try:
        import themes_ui
        th = themes_ui._load_themes()
        mine = [n for n, t in th.items() if sym in t.get("symbols", [])]
        if mine:
            stats = themes_ui._theme_stats({n: th[n] for n in mine})
            parts = []
            for n in mine:
                s_ = stats.get(n)
                if s_ and s_.get("m1") is not None:
                    parts.append(_e(n) + " <b style=\"color:" + _pct_color(s_["m1"]) + "\">" + format(s_["m1"], "+.1f") + "%</b>")
            if parts:
                lines.append(("\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e18\u0e35\u0e21 (1 \u0e40\u0e14\u0e37\u0e2d\u0e19)", " \u00b7 ".join(parts)))
    except Exception:
        pass
    # 3) EPS \u0e0a\u0e19\u0e30\u0e04\u0e32\u0e14\u0e01\u0e32\u0e23\u0e13\u0e4c
    eb = _eps_beats(sym)
    if eb:
        lines.append(("\u0e0a\u0e19\u0e30\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e01\u0e32\u0e23 EPS", "<b>" + str(eb["beats"]) + "/" + str(eb["total"]) + "</b> \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u00b7 \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 "
                      + format(eb["avg_surprise_pct"], "+.1f") + "%"))
    kv = "".join('<div style="display:grid;grid-template-columns:150px 1fr;gap:10px;padding:4px 0;font-size:13px">'
                 '<span style="color:#9aa4c4">' + k + '</span><span style="color:#f1f5ff">' + v + '</span></div>' for k, v in lines)

    # 4) \u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a + \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e04\u0e34\u0e14
    rs = _reactions(sym, g["etf"] if g else "")
    hist = ""
    if rs:
        mv = [abs(r["react"]) for r in rs]
        ups = sum(1 for r in rs if r["react"] > 0)
        hist += ('<div style="margin-top:10px;color:#e6f1ff;font-weight:700;font-size:13px">\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 ' + str(len(rs)) + ' \u0e04\u0e23\u0e31\u0e49\u0e07\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</div>'
                 '<div style="font-size:13px;color:#c0c9e4;margin:3px 0 8px">\u0e2b\u0e25\u0e31\u0e07\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a \u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 <b style="color:#fff">\u00b1' + format(sum(mv) / len(mv), ".1f") +
                 '%</b> (\u0e41\u0e23\u0e07\u0e2a\u0e38\u0e14 ' + format(max(mv), ".1f") + '%) \u00b7 \u0e02\u0e36\u0e49\u0e19 <b style="color:#19f5a5">' + str(ups) + '</b> \u0e04\u0e23\u0e31\u0e49\u0e07 \u00b7 \u0e25\u0e07 <b style="color:#ff5a85">' + str(len(rs) - ups) + '</b> \u0e04\u0e23\u0e31\u0e49\u0e07</div>')
        head = ('<div style="display:grid;grid-template-columns:110px 1fr 1fr 56px;gap:8px;font-size:12px;color:#9aa4c4;padding:3px 0;border-bottom:1px dashed rgba(125,134,166,.3)">'
                '<span>\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28</span><span>\u0e01\u0e25\u0e38\u0e48\u0e21\u0e01\u0e48\u0e2d\u0e19\u0e07\u0e1a 1 \u0e40\u0e14\u0e37\u0e2d\u0e19</span><span>\u0e2b\u0e38\u0e49\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a (2 \u0e27\u0e31\u0e19)</span><span>\u0e17\u0e34\u0e28\u0e15\u0e23\u0e07\u0e01\u0e31\u0e19</span></div>')
        body = ""
        for r in reversed(rs):
            gtxt = "\u2014" if r["grp"] is None else '<b style="color:' + _pct_color(r["grp"]) + '">' + format(r["grp"], "+.1f") + '%</b>'
            hit = ""
            if r["grp"] is not None:
                hit = "\u2713" if (r["grp"] >= 0) == (r["react"] >= 0) else "\u2717"
            body += ('<div style="display:grid;grid-template-columns:110px 1fr 1fr 56px;gap:8px;font-size:13px;padding:3px 0;color:#c0c9e4">'
                     '<span>' + str(r["date"].day) + ' ' + _TH_M[r["date"].month - 1] + ' ' + str((r["date"].year + 543) % 100) + '</span><span>' + gtxt + '</span>'
                     '<b style="color:' + _pct_color(r["react"]) + '">' + format(r["react"], "+.1f") + '%</b>'
                     '<span style="color:' + ("#19f5a5" if hit == "\u2713" else "#ff5a85") + '">' + hit + '</span></div>')
        hist += head + body
        G = [r for r in rs if r["grp"] is not None and r["grp"] > 0]
        if G:
            h = sum(1 for r in G if r["react"] > 0)
            hist += ('<div style="margin-top:8px;padding:6px 10px;border-left:2px solid #00f0ff;background:rgba(0,240,255,.07);font-size:12.5px;color:#e6f1ff">'
                     '\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e36\u0e49\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e07\u0e1a (' + str(len(G)) + ' \u0e04\u0e23\u0e31\u0e49\u0e07) \u0e2b\u0e38\u0e49\u0e19\u0e19\u0e35\u0e49\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a <b>' + str(h) + '</b> \u0e04\u0e23\u0e31\u0e49\u0e07</div>')
    else:
        hist = '<div style="margin-top:8px;color:#9aa4c4;font-size:12.5px">\u0e14\u0e36\u0e07\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 (Yahoo \u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07)</div>'
    warn = ('<div style="margin-top:10px;font-size:12px;color:#ffb347;background:rgba(255,179,71,.09);border-left:2px solid #ffb347;padding:5px 9px">'
            '\u26a0\ufe0f \u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e36\u0e49\u0e19 \u2260 \u0e07\u0e1a\u0e08\u0e30\u0e14\u0e35 \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a\u0e02\u0e36\u0e49\u0e19\u0e01\u0e31\u0e1a\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e41\u0e25\u0e30\u0e41\u0e19\u0e27\u0e42\u0e19\u0e49\u0e21\u0e1b\u0e35\u0e2b\u0e19\u0e49\u0e32\u0e17\u0e35\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e1a\u0e2d\u0e01 <b>\u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e04\u0e32\u0e14\u0e44\u0e27\u0e49</b> \u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48 \u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21 \u00b7 '
            '\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e21\u0e35\u0e41\u0e04\u0e48\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e04\u0e23\u0e31\u0e49\u0e07 \u0e43\u0e0a\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e20\u0e32\u0e1e\u0e1b\u0e23\u0e30\u0e01\u0e2d\u0e1a \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e15\u0e31\u0e27\u0e17\u0e33\u0e19\u0e32\u0e22</div>')
    st.markdown('<div style="' + box + '"><div style="color:#fcee0a;font-family:monospace;font-weight:700;font-size:16px;margin-bottom:6px">' + _e(sym) + '</div>' +
                kv + hist + warn + '</div>', unsafe_allow_html=True)


def _card(e, today):
    days = (e["date"] - today).days
    label, color = TYPES[e["kind"]]
    when = "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49" if days == 0 else ("\u0e1e\u0e23\u0e38\u0e48\u0e07\u0e19\u0e35\u0e49" if days == 1 else f"\u0e2d\u0e35\u0e01 {days} \u0e27\u0e31\u0e19")
    hot = days <= 7
    alarm = "\u23f0 " if hot else ""          # (\u0e44\u0e21\u0e48\u0e43\u0e2a\u0e48\u0e43\u0e19\u0e19\u0e34\u0e1e\u0e08\u0e19\u0e4c\u0e02\u0e2d\u0e07 f-string \u0e42\u0e14\u0e22\u0e15\u0e23\u0e07: Python \u0e01\u0e48\u0e2d\u0e19 3.12 \u0e44\u0e21\u0e48\u0e22\u0e2d\u0e21\u0e43\u0e2b\u0e49\u0e21\u0e35 backslash/\u0e2d\u0e35\u0e42\u0e21\u0e08\u0e34\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e41\u0e1b\u0e25\u0e07\u0e40\u0e1b\u0e47\u0e19 \u \u0e15\u0e23\u0e07\u0e19\u0e31\u0e49\u0e19)
    note = e["note"] or ("\u0e0a\u0e48\u0e27\u0e07\u0e43\u0e01\u0e25\u0e49\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a\u0e23\u0e32\u0e04\u0e32\u0e21\u0e31\u0e01\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07" if e["kind"] == "earn" else "")
    return (
        f'<div style="display:flex;gap:14px;padding:11px 12px;margin-bottom:8px;background:rgba(12,14,28,.82);'
        f'border:1px solid rgba(0,240,255,.16);border-left:3px solid {color}">'
        f'<div style="min-width:112px"><div style="color:#e6f1ff;font-weight:700;font-size:14px">{_e(th_date(e["date"]))}</div>'
        f'<div style="color:{"#ff2a6d" if hot else "#7d86a6"};font-size:12px;font-weight:{"700" if hot else "400"}">{alarm}{when}</div></div>'
        f'<div style="flex:1;min-width:0"><div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">'
        f'<span style="font-family:monospace;font-weight:700;color:#fcee0a;font-size:15px">{_e(e["sym"])}</span>'
        f'<span style="color:{color};font-size:12px;border:1px solid {color};padding:1px 7px">{_e(label)}</span>'
        f'<span style="color:#7d86a6;font-size:12px">{_e(e["name"] if e["kind"] != "fomc" else "")}</span></div>'
        f'<div style="color:#9aa4c4;font-size:12px;margin-top:3px">{_e(note)}</div>{_grp_line(e.get("grp"))}</div></div>'
    )


def render_calendar():
    st.markdown(_GRP_CSS, unsafe_allow_html=True)
    st.caption("\u0e23\u0e27\u0e21\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a \u00b7 \u0e27\u0e31\u0e19 XD/\u0e08\u0e48\u0e32\u0e22\u0e1b\u0e31\u0e19\u0e1c\u0e25 \u00b7 \u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14 \u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21 \u0e40\u0e23\u0e35\u0e22\u0e07\u0e15\u0e32\u0e21\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e43\u0e01\u0e25\u0e49\u0e2a\u0e38\u0e14\u0e01\u0e48\u0e2d\u0e19")
    src = st.radio("\u0e41\u0e2b\u0e25\u0e48\u0e07\u0e2b\u0e38\u0e49\u0e19", ["\U0001f310 \u0e04\u0e49\u0e19\u0e2b\u0e32\u0e43\u0e2b\u0e49\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34 (\u0e07\u0e1a/\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e01\u0e33\u0e25\u0e31\u0e07\u0e08\u0e30\u0e21\u0e32\u0e16\u0e36\u0e07 \u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14)", "\u2b50 \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e09\u0e31\u0e19\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21"],
                   horizontal=True, key="cal_src")
    auto = src.startswith("\U0001f310")
    if "cal_text" not in st.session_state:
        try:
            st.session_state["cal_text"] = ", ".join(home_ui._watchlist())
        except Exception:
            st.session_state["cal_text"] = "NVDA, AAPL, MSFT, TSLA"
    if auto:
        txt = st.session_state["cal_text"]
        cap_pick = st.radio("\u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17", ["\u0e43\u0e2b\u0e0d\u0e48\u0e21\u0e32\u0e01 (\u2265 $100B)", "\u0e43\u0e2b\u0e0d\u0e48 (\u2265 $10B)", "\u0e01\u0e25\u0e32\u0e07\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b (\u2265 $2B)"],
                            horizontal=True, key="cal_cap", index=1)
        min_cap = {"\u0e43\u0e2b\u0e0d\u0e48\u0e21\u0e32\u0e01 (\u2265 $100B)": 100e9, "\u0e43\u0e2b\u0e0d\u0e48 (\u2265 $10B)": 10e9, "\u0e01\u0e25\u0e32\u0e07\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b (\u2265 $2B)": 2e9}[cap_pick]
    else:
        import watchlist
        _wl = watchlist.get()
        txt = ", ".join(_wl)
        st.markdown(watchlist.chips(_wl[:25]), unsafe_allow_html=True)
        st.caption("\u0e43\u0e0a\u0e49 Watchlist \u0e01\u0e25\u0e32\u0e07 (\u0e41\u0e01\u0e49\u0e44\u0e14\u0e49\u0e17\u0e35\u0e48\u0e2b\u0e19\u0e49\u0e32 \U0001f680 \u0e2a\u0e41\u0e01\u0e19\u0e40\u0e19\u0e2d\u0e23\u0e4c)")
        min_cap = 0
    kind_pick = st.radio("\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c", ["\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", "\U0001f4ca \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a", "\U0001f4b0 \u0e1b\u0e31\u0e19\u0e1c\u0e25", "\U0001f3e6 \u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14"],
                         horizontal=True, key="cal_kind")
    c2, c3 = st.columns([1.4, 1], vertical_alignment="bottom")
    horizon = c2.selectbox("\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32", [14, 30, 60, 90], index=1, format_func=lambda d: f"\u0e43\u0e19 {d} \u0e27\u0e31\u0e19\u0e02\u0e49\u0e32\u0e07\u0e2b\u0e19\u0e49\u0e32")
    if c3.button("\U0001f504 \u0e23\u0e35\u0e40\u0e1f\u0e23\u0e0a\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14", use_container_width=True):
        _fetch.clear()
        _nasdaq_day.clear()
        _nasdaq_div_day.clear()
        _cap_map.clear()
        _sector_batch.clear()

    syms = []
    for t in txt.replace("\n", ",").split(","):
        t = t.strip().upper()
        if t and t not in syms:
            syms.append(t)
    syms = syms[:25]
    kinds = {"\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14": {"earn", "exdiv", "paydiv", "fomc"}, "\U0001f4ca \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a": {"earn"},
             "\U0001f4b0 \u0e1b\u0e31\u0e19\u0e1c\u0e25": {"exdiv", "paydiv"}, "\U0001f3e6 \u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14": {"fomc"}}[kind_pick]

    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e23\u0e27\u0e1a\u0e23\u0e27\u0e21\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c..."):
        if auto:
            # \u0e42\u0e2b\u0e21\u0e14\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34: \u0e07\u0e1a + \u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e08\u0e32\u0e01 Nasdaq (+ \u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14)
            events = build_events((), kinds & {"fomc"}, int(horizon))
            if "earn" in kinds:
                horizon_cap = min(int(horizon), 30)  # \u0e14\u0e36\u0e07\u0e17\u0e35\u0e25\u0e30\u0e27\u0e31\u0e19 \u0e08\u0e33\u0e01\u0e31\u0e14 30 \u0e27\u0e31\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e0a\u0e49\u0e32
                events += auto_earnings(horizon_cap, min_cap)
                events.sort(key=lambda e: (e["date"], -e.get("cap", 0), e["kind"], e["sym"]))
                if int(horizon) > 30:
                    st.caption("\u0e42\u0e2b\u0e21\u0e14\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e14\u0e39\u0e07\u0e1a\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e44\u0e14\u0e49\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 30 \u0e27\u0e31\u0e19 (\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14\u0e22\u0e31\u0e07\u0e41\u0e2a\u0e14\u0e07\u0e15\u0e32\u0e21\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e35\u0e48\u0e40\u0e25\u0e37\u0e2d\u0e01)")
            if kinds & {"exdiv", "paydiv"}:
                divs, have_caps = auto_dividends(min(int(horizon), 30), min_cap, kinds)
                events += divs
                events.sort(key=lambda e: (e["date"], -e.get("cap", 0), e["kind"], e["sym"]))
                if not have_caps:
                    st.caption("\u26a0\ufe0f \u0e14\u0e36\u0e07\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e43\u0e19\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e08\u0e36\u0e07\u0e22\u0e31\u0e07\u0e01\u0e23\u0e2d\u0e07\u0e15\u0e32\u0e21\u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 (\u0e41\u0e2a\u0e14\u0e07\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e2a\u0e39\u0e07\u0e01\u0e48\u0e2d\u0e19) \u0e25\u0e2d\u0e07\u0e01\u0e14 \U0001f504 \u0e23\u0e35\u0e40\u0e1f\u0e23\u0e0a\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07")
                if int(horizon) > 30 and not kinds & {"earn"}:
                    st.caption("\u0e42\u0e2b\u0e21\u0e14\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e14\u0e39\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e44\u0e14\u0e49\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 30 \u0e27\u0e31\u0e19 (\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14\u0e22\u0e31\u0e07\u0e41\u0e2a\u0e14\u0e07\u0e15\u0e32\u0e21\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e35\u0e48\u0e40\u0e25\u0e37\u0e2d\u0e01)")
        else:
            events = build_events(tuple(syms), kinds, int(horizon))
    today = date.today()
    if auto and "earn" in kinds and not any(e["kind"] == "earn" for e in events):
        st.warning("\u0e14\u0e36\u0e07\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e07\u0e1a\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e43\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e19\u0e35\u0e49 \u0e25\u0e2d\u0e07\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e25\u0e47\u0e01\u0e25\u0e07 \u0e01\u0e14 \U0001f504 \u0e23\u0e35\u0e40\u0e1f\u0e23\u0e0a "
                   "\u0e2b\u0e23\u0e37\u0e2d\u0e2a\u0e25\u0e31\u0e1a\u0e44\u0e1b\u0e42\u0e2b\u0e21\u0e14 \u2b50 \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e09\u0e31\u0e19\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21\u0e04\u0e23\u0e31\u0e1a")
    if auto and kinds & {"exdiv", "paydiv"} and not any(e["kind"] in ("exdiv", "paydiv") for e in events):
        st.warning("\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e35\u0e49 (\u0e2b\u0e23\u0e37\u0e2d\u0e14\u0e36\u0e07\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08) \u0e25\u0e2d\u0e07\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e02\u0e19\u0e32\u0e14\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e25\u0e47\u0e01\u0e25\u0e07 \u0e01\u0e14 \U0001f504 \u0e23\u0e35\u0e40\u0e1f\u0e23\u0e0a "
                   "\u0e2b\u0e23\u0e37\u0e2d\u0e2a\u0e25\u0e31\u0e1a\u0e44\u0e1b\u0e42\u0e2b\u0e21\u0e14 \u2b50 \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e09\u0e31\u0e19\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21\u0e04\u0e23\u0e31\u0e1a")
    if not events:
        st.info("\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e35\u0e49 \u0e25\u0e2d\u0e07\u0e02\u0e22\u0e32\u0e22\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32 \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e04\u0e23\u0e31\u0e1a")
        return

    soon = [e for e in events if (e["date"] - today).days <= 7]
    m1, m2, m3 = st.columns(3)
    m1.metric("\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", len(events))
    m2.metric("\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19", len(soon))
    nxt = events[0]
    m3.metric("\u0e43\u0e01\u0e25\u0e49\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14", f'{nxt["sym"]} \u00b7 {nxt["date"].day} {_TH_M[nxt["date"].month - 1]}')

    # \u0e43\u0e2a\u0e48 "\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19 + \u0e1c\u0e25\u0e07\u0e32\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21 1 \u0e40\u0e14\u0e37\u0e2d\u0e19" \u0e43\u0e2b\u0e49\u0e17\u0e38\u0e01\u0e41\u0e16\u0e27\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a
    earn_syms = tuple(sorted({e["sym"] for e in events if e["kind"] == "earn"}))
    secs, perf = {}, {}
    if earn_syms:
        with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e14\u0e39\u0e27\u0e48\u0e32\u0e41\u0e15\u0e48\u0e25\u0e30\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e39\u0e48\u0e01\u0e25\u0e38\u0e48\u0e21\u0e44\u0e2b\u0e19..."):
            secs, perf = _sector_batch(earn_syms), _sector_perf()
            if sum(1 for v in secs.values() if v.get("sector")) < max(1, len(earn_syms) // 3):
                _sector_batch.clear()          # \u0e14\u0e36\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e43\u0e2b\u0e0d\u0e48 \u0e44\u0e21\u0e48\u0e40\u0e01\u0e47\u0e1a\u0e1c\u0e25\u0e40\u0e2a\u0e35\u0e22\u0e44\u0e27\u0e49 \u0e23\u0e2d\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e25\u0e2d\u0e07\u0e43\u0e2b\u0e21\u0e48
        for e in events:
            if e["kind"] == "earn":
                e["grp"] = _group_of(secs.get(e["sym"]), perf)
        pick_opts = []
        for e in events:
            if e["kind"] == "earn" and e["sym"] not in [p[0] for p in pick_opts]:
                pick_opts.append((e["sym"], e))
        sel = st.selectbox("\U0001f50d \u0e14\u0e39\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14: \u0e01\u0e25\u0e38\u0e48\u0e21 + \u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a \u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e08\u0e30\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28",
                           [p[0] for p in pick_opts], index=None, placeholder="\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e27\u0e48\u0e32\u0e2d\u0e22\u0e39\u0e48\u0e01\u0e25\u0e38\u0e48\u0e21\u0e44\u0e2b\u0e19 \u0e01\u0e25\u0e38\u0e48\u0e21\u0e19\u0e31\u0e49\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23 \u0e41\u0e25\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e19\u0e35\u0e49\u0e40\u0e04\u0e22\u0e02\u0e22\u0e31\u0e1a\u0e41\u0e04\u0e48\u0e44\u0e2b\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a",
                           format_func=lambda s_: s_ + " \u00b7 " + next(x[1]["name"] for x in pick_opts if x[0] == s_), key="cal_detail")
        if sel:
            with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e14\u0e36\u0e07\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e2b\u0e25\u0e31\u0e07\u0e07\u0e1a\u0e02\u0e2d\u0e07 " + sel + "..."):
                _render_detail(sel, _group_of(secs.get(sel), perf), secs.get(sel))

    last = None
    for e in events:
        key = (e["date"].year, e["date"].month)
        if key != last:
            st.markdown(f'<div class="section-label">{_TH_M[e["date"].month - 1]} {e["date"].year + 543}</div>', unsafe_allow_html=True)
            last = key
        st.markdown(_card(e, today), unsafe_allow_html=True)

    st.caption("\u26a0\ufe0f \u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a/\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e08\u0e32\u0e01\u0e41\u0e2b\u0e25\u0e48\u0e07\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e30 (Nasdaq/Yahoo Finance) (\u0e1a\u0e32\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e21\u0e48\u0e21\u0e35 \u0e41\u0e25\u0e30\u0e2d\u0e32\u0e08\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19) \u0e04\u0e27\u0e23\u0e40\u0e0a\u0e47\u0e01\u0e01\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17 \u00b7 "
               "\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e43\u0e19\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e32\u0e21\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e2b\u0e23\u0e31\u0e10 \u0e40\u0e27\u0e25\u0e32\u0e44\u0e17\u0e22\u0e17\u0e35\u0e48\u0e41\u0e2a\u0e14\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e42\u0e14\u0e22\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 (\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1a\u0e2d\u0e01\u0e41\u0e04\u0e48\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e1b\u0e34\u0e14/\u0e2b\u0e25\u0e31\u0e07\u0e1b\u0e34\u0e14) \u00b7 "
               "\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e0a\u0e38\u0e21\u0e40\u0e1f\u0e14\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e15\u0e32\u0e23\u0e32\u0e07\u0e17\u0e35\u0e48 Federal Reserve \u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28 (\u0e1b\u0e35 2027 \u0e40\u0e1b\u0e47\u0e19\u0e41\u0e1a\u0e1a\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e15\u0e49\u0e19) \u0e15\u0e23\u0e27\u0e08\u0e44\u0e14\u0e49\u0e17\u0e35\u0e48 federalreserve.gov \u00b7 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e0b\u0e37\u0e49\u0e2d-\u0e02\u0e32\u0e22")