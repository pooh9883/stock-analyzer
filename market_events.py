# -*- coding: utf-8 -*-
"""market_events.py - \u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e15\u0e25\u0e32\u0e14\u0e17\u0e35\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e02\u0e48\u0e32\u0e27\u0e2b\u0e38\u0e49\u0e19\u0e23\u0e32\u0e22\u0e15\u0e31\u0e27)
\u0e40\u0e0a\u0e48\u0e19 \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e15\u0e31\u0e49\u0e07\u0e01\u0e25\u0e32\u0e07\u0e40\u0e17\u0e2d\u0e21, \u0e1c\u0e25\u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e43\u0e2b\u0e0d\u0e48\u0e17\u0e35\u0e48\u0e25\u0e32\u0e01\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21, \u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a\u0e43\u0e2b\u0e21\u0e48, \u0e15\u0e37\u0e48\u0e19\u0e15\u0e23\u0e30\u0e2b\u0e19\u0e01\u0e02\u0e32\u0e22\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14

\u0e2b\u0e25\u0e31\u0e01\u0e01\u0e32\u0e23 (\u0e1f\u0e23\u0e35 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e04\u0e35\u0e22\u0e4c AI):
1) \u0e2b\u0e32 "\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e23\u0e37\u0e2d\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e22\u0e31\u0e1a\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34" \u0e08\u0e32\u0e01 SPY / QQQ / ETF \u0e01\u0e25\u0e38\u0e48\u0e21 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e1b\u0e01\u0e15\u0e34\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e40\u0e2d\u0e07
2) \u0e2d\u0e48\u0e32\u0e19\u0e1e\u0e24\u0e15\u0e34\u0e01\u0e23\u0e23\u0e21\u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e08\u0e32\u0e01 VIX / \u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23 / \u0e17\u0e2d\u0e07 / \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c (\u0e02\u0e32\u0e22\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e1b\u0e16\u0e37\u0e2d\u0e18\u0e19\u0e1a\u0e31\u0e15\u0e23\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e1b\u0e25\u0e48\u0e32)
3) \u0e14\u0e36\u0e07\u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d\u0e02\u0e48\u0e32\u0e27\u0e23\u0e2d\u0e1a\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e1e\u0e39\u0e14\u0e16\u0e36\u0e07 "\u0e18\u0e35\u0e21\u0e02\u0e48\u0e32\u0e27" \u0e15\u0e48\u0e2d\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e21\u0e35\u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d\u0e02\u0e48\u0e32\u0e27\u0e2a\u0e19\u0e31\u0e1a\u0e2a\u0e19\u0e38\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22 2 \u0e0a\u0e34\u0e49\u0e19
   \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e16\u0e36\u0e07 \u0e08\u0e30\u0e1a\u0e2d\u0e01\u0e15\u0e23\u0e07\u0e46 \u0e27\u0e48\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48\u0e0a\u0e35\u0e49\u0e0a\u0e31\u0e14 \u0e44\u0e21\u0e48\u0e40\u0e14\u0e32\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38

\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49:
    import market_events
    market_events.render_market_events()                     # \u0e2b\u0e19\u0e49\u0e32\u0e40\u0e15\u0e47\u0e21 (\u0e43\u0e2a\u0e48\u0e43\u0e19\u0e40\u0e23\u0e14\u0e32\u0e23\u0e4c\u0e02\u0e48\u0e32\u0e27 / \u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e15\u0e25\u0e32\u0e14)
    market_events.render_market_events(compact=True, focus_etf="SOXX")   # \u0e41\u0e16\u0e1a\u0e22\u0e48\u0e2d\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e21\u0e38\u0e21\u0e21\u0e2d\u0e07\u0e40\u0e0a\u0e34\u0e07\u0e25\u0e36\u0e01
"""
import datetime as _dt
import html as _html

import pandas as pd
import streamlit as st
import yfinance as yf

_TH_MON = ["\u0e21.\u0e04.", "\u0e01.\u0e1e.", "\u0e21\u0e35.\u0e04.", "\u0e40\u0e21.\u0e22.", "\u0e1e.\u0e04.", "\u0e21\u0e34.\u0e22.", "\u0e01.\u0e04.", "\u0e2a.\u0e04.", "\u0e01.\u0e22.", "\u0e15.\u0e04.", "\u0e1e.\u0e22.", "\u0e18.\u0e04."]
_WD = ["\u0e08\u0e31\u0e19\u0e17\u0e23\u0e4c", "\u0e2d\u0e31\u0e07\u0e04\u0e32\u0e23", "\u0e1e\u0e38\u0e18", "\u0e1e\u0e24\u0e2b\u0e31\u0e2a\u0e1a\u0e14\u0e35", "\u0e28\u0e38\u0e01\u0e23\u0e4c", "\u0e40\u0e2a\u0e32\u0e23\u0e4c", "\u0e2d\u0e32\u0e17\u0e34\u0e15\u0e22\u0e4c"]
_GROUPS = [("SPY", "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21 S&P 500"), ("QQQ", "\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e43\u0e2b\u0e0d\u0e48 Nasdaq"), ("SOXX", "AI \u0e41\u0e25\u0e30\u0e0a\u0e34\u0e1b"), ("XLK", "\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35"),
           ("XLC", "\u0e2a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23/\u0e2d\u0e34\u0e19\u0e40\u0e17\u0e2d\u0e23\u0e4c\u0e40\u0e19\u0e47\u0e15"), ("XLF", "\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19"), ("XLV", "\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e"), ("XLE", "\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19"), ("XLY", "\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e1f\u0e38\u0e48\u0e21\u0e40\u0e1f\u0e37\u0e2d\u0e22"),
           ("XLP", "\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19"), ("XLI", "\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21"), ("XLB", "\u0e27\u0e31\u0e2a\u0e14\u0e38"), ("XLU", "\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04"), ("XLRE", "\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e2f")]
_FLOWS = ["^VIX", "TLT", "GLD", "UUP"]
_UPC, _DNC, _MUTED = "#19f5a5", "#ff4d6d", "#8d97b8"

_CSS = (
    "<style>"
    ".me{margin:10px 0;padding:14px 16px;border:1px solid rgba(125,134,166,.28);border-left:4px solid var(--ac);"
    "background:linear-gradient(135deg,rgba(8,12,28,.7),rgba(8,12,28,.4))}"
    ".me-top{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}"
    ".me-d{font-size:16px;font-weight:800;color:#e8ecfa!important;-webkit-text-fill-color:#e8ecfa}"
    ".me-pct{font-size:20px;font-weight:900}"
    ".me-chip{font-size:12px;padding:1px 8px;border:1px solid;font-weight:700}"
    ".me-s{margin:8px 0 6px;font-size:14px;line-height:1.6;color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2}"
    ".me-fl{margin:6px 0;padding:8px 10px;font-size:13px;line-height:1.55;background:rgba(0,240,255,.06);border-left:3px solid #00f0ff;"
    "color:#cfd7f2!important;-webkit-text-fill-color:#cfd7f2}"
    ".me-g{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}"
    ".me-p{padding:3px 9px;font-size:12px;border:1px solid;font-weight:700}"
    ".me-th{margin:8px 0 2px;font-size:13px;font-weight:700;color:#fcee0a!important;-webkit-text-fill-color:#fcee0a}"
    ".me-h{margin:2px 0;font-size:13px;line-height:1.5}"
    ".me-h a{color:#7fdcff!important;-webkit-text-fill-color:#7fdcff;text-decoration:none}"
    ".me-h small{color:#8d97b8}"
    ".me-note{margin:6px 0 0;font-size:12px;color:#8d97b8!important;-webkit-text-fill-color:#8d97b8}"
    "</style>"
)


def _e(x):
    return _html.escape(str(x), quote=True)


def _pct(x, d=1, sign=True):
    if x is None:
        return "-"
    return ("%+." + str(d) + "f%%") % x if sign else ("%." + str(d) + "f%%") % x


@st.cache_data(ttl=900, show_spinner=False)
def _find_events(last_days=30):
    """\u0e04\u0e37\u0e19\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23 event: date, moves{etf:chg}, flows{k:{chg,lvl}}, score"""
    syms = [s for s, _ in _GROUPS] + _FLOWS
    try:
        d = yf.download(" ".join(syms), period="8mo", interval="1d", group_by="ticker", progress=False, auto_adjust=True)
    except Exception:
        return []
    closes = {}
    for s in syms:
        try:
            c = d[s]["Close"].dropna()
            if len(c) > 80:
                closes[s] = c
        except Exception:
            pass
    if "SPY" not in closes:
        return []
    rets = {s: c.pct_change().dropna() * 100 for s, c in closes.items()}
    zs = {s: r / r.rolling(60).std().shift(1) for s, r in rets.items()}
    last = closes["SPY"].index[-1]
    cut = last - pd.Timedelta(days=last_days)
    out = []
    for dt in rets["SPY"].index:
        if dt < cut:
            continue
        mv, best = {}, 0.0
        for s, _n in _GROUPS:
            r = rets.get(s)
            if r is None or dt not in r.index:
                continue
            z = zs[s].get(dt)
            z = float(z) if z is not None and z == z else 0.0
            mv[s] = {"chg": float(r.loc[dt]), "z": z}
            best = max(best, abs(z) * (1.3 if s in ("SPY", "QQQ") else 1.0))
        spy = mv.get("SPY", {}).get("chg", 0)
        # \u0e16\u0e37\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e40\u0e21\u0e37\u0e48\u0e2d: \u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21/Nasdaq \u0e02\u0e22\u0e31\u0e1a\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34 \u0e2b\u0e23\u0e37\u0e2d\u0e01\u0e25\u0e38\u0e48\u0e21\u0e43\u0e14\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e02\u0e22\u0e31\u0e1a\u0e41\u0e23\u0e07\u0e21\u0e32\u0e01 (>=2.4 \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e1b\u0e01\u0e15\u0e34 \u0e41\u0e25\u0e30 >=3%)
        big_group = any(abs(v["chg"]) >= 3 and abs(v["z"]) >= 2.4 for v in mv.values())
        big_mkt = abs(spy) >= 1.5 or abs(mv.get("QQQ", {}).get("chg", 0)) >= 2.0 or abs(mv.get("SPY", {}).get("z", 0)) >= 2.2
        if not (big_group or big_mkt):
            continue
        fl = {}
        for k in _FLOWS:
            r = rets.get(k)
            if r is not None and dt in r.index:
                fl[k] = {"chg": float(r.loc[dt]), "lvl": float(closes[k].loc[dt]) if k == "^VIX" else None}
        out.append({"date": dt.date(), "moves": mv, "flows": fl, "score": best})
    out.sort(key=lambda e: -e["score"])
    return sorted(out[:5], key=lambda e: e["date"], reverse=True)


def _read_flows(fl, spy):
    vix, tlt, gld, uup = [(fl.get(k) or {}).get("chg") for k in _FLOWS]
    safe_up = sum(1 for v in (tlt, gld, uup) if v is not None and v >= 0.4)
    safe_dn = sum(1 for v in (tlt, gld, uup) if v is not None and v <= -0.4)
    vix_up = vix is not None and vix >= 10
    if spy <= -1.0 and safe_up >= 2:
        return "\u0e40\u0e07\u0e34\u0e19\u0e2b\u0e19\u0e35\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07: \u0e02\u0e32\u0e22\u0e2b\u0e38\u0e49\u0e19\u0e41\u0e25\u0e49\u0e27\u0e44\u0e2b\u0e25\u0e40\u0e02\u0e49\u0e32\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23/\u0e17\u0e2d\u0e07/\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 (\u0e04\u0e37\u0e2d\u0e02\u0e32\u0e22\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e1b\u0e16\u0e37\u0e2d\u0e02\u0e2d\u0e07\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22)"
    if spy <= -1.0 and vix_up and safe_up == 1:
        return "\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27\u0e1e\u0e38\u0e48\u0e07 \u0e41\u0e15\u0e48\u0e40\u0e07\u0e34\u0e19\u0e44\u0e2b\u0e25\u0e40\u0e02\u0e49\u0e32\u0e02\u0e2d\u0e07\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22\u0e41\u0e04\u0e48\u0e1a\u0e32\u0e07\u0e15\u0e31\u0e27: \u0e20\u0e32\u0e1e\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e0a\u0e31\u0e14\u0e27\u0e48\u0e32\u0e2b\u0e19\u0e35\u0e44\u0e1b\u0e16\u0e37\u0e2d\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23/\u0e17\u0e2d\u0e07/\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 \u0e2b\u0e23\u0e37\u0e2d\u0e41\u0e04\u0e48\u0e25\u0e14\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e1a\u0e32\u0e07\u0e2a\u0e48\u0e27\u0e19"
    if spy <= -1.0 and (vix_up or safe_dn >= 2) and safe_up == 0:
        return "\u0e02\u0e32\u0e22\u0e15\u0e32\u0e21\u0e01\u0e31\u0e19\u0e41\u0e25\u0e30\u0e25\u0e49\u0e32\u0e07\u0e01\u0e33\u0e44\u0e23: \u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27\u0e1e\u0e38\u0e48\u0e07\u0e41\u0e15\u0e48\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23/\u0e17\u0e2d\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e1a\u0e40\u0e07\u0e34\u0e19\u0e44\u0e2b\u0e25\u0e40\u0e02\u0e49\u0e32 (\u0e16\u0e2d\u0e19\u0e2d\u0e2d\u0e01\u0e21\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2b\u0e25\u0e1a\u0e44\u0e1b\u0e17\u0e35\u0e48\u0e44\u0e2b\u0e19)"
    if spy <= -1.0:
        return "\u0e2b\u0e38\u0e49\u0e19\u0e25\u0e07\u0e41\u0e15\u0e48\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27\u0e44\u0e21\u0e48\u0e1e\u0e38\u0e48\u0e07\u0e21\u0e32\u0e01: \u0e19\u0e48\u0e32\u0e08\u0e30\u0e40\u0e1b\u0e47\u0e19\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e31\u0e1a\u0e1e\u0e2d\u0e23\u0e4c\u0e15\u0e2b\u0e23\u0e37\u0e2d\u0e2b\u0e21\u0e38\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e01\u0e32\u0e23\u0e15\u0e37\u0e48\u0e19\u0e15\u0e23\u0e30\u0e2b\u0e19\u0e01"
    if spy >= 1.0:
        return "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e1a\u0e27\u0e01\u0e41\u0e23\u0e07: \u0e40\u0e07\u0e34\u0e19\u0e01\u0e33\u0e25\u0e31\u0e07\u0e44\u0e2b\u0e25\u0e40\u0e02\u0e49\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e41\u0e25\u0e30\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07"
    return "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e02\u0e22\u0e31\u0e1a\u0e41\u0e23\u0e07: \u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e02\u0e2d\u0e07\u0e1a\u0e32\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14"


@st.cache_data(ttl=1800, show_spinner=False)
def _news_for_day(date_iso, groups):
    """\u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d\u0e02\u0e48\u0e32\u0e27\u0e23\u0e2d\u0e1a\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19: \u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21 + \u0e01\u0e25\u0e38\u0e48\u0e21\u0e17\u0e35\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e41\u0e23\u0e07 (\u0e44\u0e21\u0e48\u0e1c\u0e39\u0e01\u0e01\u0e31\u0e1a\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e43\u0e14\u0e15\u0e31\u0e27\u0e2b\u0e19\u0e36\u0e48\u0e07) \u0e41\u0e1b\u0e25\u0e44\u0e17\u0e22\u0e1f\u0e23\u0e35"""
    try:
        import news_radar
        import news_feed
    except Exception:
        return []
    d0 = _dt.date.fromisoformat(date_iso)
    rng = "after:%s before:%s" % (d0.isoformat(), (d0 + _dt.timedelta(days=2)).isoformat())
    qmap = {"SOXX": "semiconductor stocks", "QQQ": "tech stocks Nasdaq", "XLK": "technology stocks", "XLF": "bank stocks",
            "XLE": "energy stocks oil", "XLV": "healthcare stocks", "XLY": "consumer stocks retail", "XLC": "internet media stocks"}
    qs = ["stock market selloff OR rally %s" % rng, "Wall Street stocks %s" % rng]
    for g in groups:
        if g in qmap:
            qs.append("%s %s" % (qmap[g], rng))
    rows, seen = [], set()
    for q in qs[:4]:
        try:
            got = news_radar.fetch_google_news(q, max_items=8) or []
        except Exception:
            got = []
        for n in got:
            t, src = news_feed._clean_title(n.get("title"), n.get("source"))
            k = news_feed._norm(t)
            if not k or k in seen:
                continue
            seen.add(k)
            rows.append({"title_en": t, "link": n.get("link", ""), "source": src})
    rows = rows[:12]
    try:
        th = news_feed.translate_free([r["title_en"] for r in rows])
    except Exception:
        th = []
    th = list(th) + [""] * len(rows)
    for r, t in zip(rows, th):
        r["th"] = t or r["title_en"]
    return rows


def _gnews(q):
    import urllib.parse as up
    return "https://news.google.com/search?q=%s&hl=en-US&gl=US&ceid=US:en" % up.quote(q)


_BASKET = {
    "AI \u0e41\u0e25\u0e30\u0e0a\u0e34\u0e1b": ["NVDA", "AMD", "AVGO", "TSM", "MU", "SNDK", "WDC", "STX", "INTC", "QCOM", "ARM", "MRVL", "LRCX", "AMAT", "KLAC", "ASML", "SMCI", "DELL"],
    "\u0e0b\u0e2d\u0e1f\u0e15\u0e4c\u0e41\u0e27\u0e23\u0e4c/\u0e04\u0e25\u0e32\u0e27\u0e14\u0e4c/\u0e28\u0e39\u0e19\u0e22\u0e4c\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25": ["MSFT", "GOOGL", "META", "AMZN", "ORCL", "PLTR", "ANET", "VRT", "CRWD", "NOW"],
    "\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e2d\u0e37\u0e48\u0e19\u0e46": ["AAPL", "TSLA", "NFLX", "JPM", "XOM", "LLY", "WMT", "COST"],
}
_SYM_GRP = {t: g for g, ts in _BASKET.items() for t in ts}


@st.cache_data(ttl=900, show_spinner=False)
def _movers(dates):
    """\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e43\u0e19\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e40\u0e1d\u0e49\u0e32\u0e14\u0e39: % \u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e43\u0e19\u0e41\u0e15\u0e48\u0e25\u0e30\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c \u2192 {date_iso: [(sym, chg), ...]}"""
    syms = list(_SYM_GRP)
    try:
        d = yf.download(" ".join(syms), period="4mo", interval="1d", group_by="ticker", progress=False, auto_adjust=True)
    except Exception:
        return {}
    out = {x: [] for x in dates}
    for t in syms:
        try:
            c = d[t]["Close"].dropna()
            r = c.pct_change().dropna() * 100
        except Exception:
            continue
        for x in dates:
            ts = pd.Timestamp(x)
            if ts in r.index:
                out[x].append((t, float(r.loc[ts])))
    return out


def _translate(titles):
    """\u0e41\u0e1b\u0e25\u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d\u0e02\u0e48\u0e32\u0e27\u0e1f\u0e23\u0e35\u0e14\u0e49\u0e27\u0e22\u0e15\u0e31\u0e27\u0e41\u0e1b\u0e25\u0e01\u0e25\u0e32\u0e07\u0e43\u0e19 insight.py (\u0e25\u0e2d\u0e07\u0e0b\u0e49\u0e33 + \u0e1b\u0e25\u0e32\u0e22\u0e17\u0e32\u0e07\u0e2a\u0e33\u0e23\u0e2d\u0e07) \u00b7 \u0e41\u0e1b\u0e25\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e08\u0e23\u0e34\u0e07\u0e46 \u0e04\u0e48\u0e2d\u0e22\u0e41\u0e2a\u0e14\u0e07\u0e2d\u0e31\u0e07\u0e01\u0e24\u0e29\u0e40\u0e14\u0e34\u0e21"""
    titles = list(titles)
    try:
        import insight as _in
        th = _in.tr_list(titles)
    except Exception:
        th = [""] * len(titles)
    return [t or en for en, t in zip(titles, th)]


def _event_html(ev, focus_etf=None, movers=None):
    mv = ev["moves"]
    spy = mv.get("SPY", {}).get("chg", 0)
    name = dict(_GROUPS)
    ranked = sorted([(s, v) for s, v in mv.items() if s not in ("SPY",)], key=lambda x: -abs(x[1]["chg"]))
    top3 = ranked[:3]
    lead = ranked[0] if ranked else ("SPY", mv.get("SPY", {"chg": 0}))
    d = ev["date"]
    if abs(spy) >= 1.0:
        drive = spy                                   # \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e02\u0e22\u0e31\u0e1a\u0e41\u0e23\u0e07: \u0e17\u0e34\u0e28\u0e02\u0e2d\u0e07\u0e27\u0e31\u0e19 = \u0e17\u0e34\u0e28\u0e02\u0e2d\u0e07 S&P 500
    else:
        drive = lead[1]["chg"] if abs(lead[1]["chg"]) > abs(spy) else spy
    down = drive < 0
    col = _DNC if down else _UPC
    # --- \u0e02\u0e48\u0e32\u0e27 + \u0e18\u0e35\u0e21 ---
    try:
        import insight as _in
        rows = _news_for_day(d.isoformat(), tuple(s for s, _v in top3))
        rows = _in._rank_by_direction(rows, -1 if down else 1)
        th = [t for t in _in._themes_from([r.get("title_en") or "" for r in rows]) if t["key"] not in ("chip_sector", "corp", "analyst") and len(t["idx"]) >= 2]
    except Exception:
        rows, th = [], []
    # --- \u0e1b\u0e23\u0e30\u0e42\u0e22\u0e04\u0e40\u0e25\u0e48\u0e32\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07 (\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e08\u0e23\u0e34\u0e07 + "\u0e2a\u0e37\u0e48\u0e2d\u0e42\u0e22\u0e07\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49\u0e01\u0e31\u0e1a..." \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e18\u0e35\u0e21\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e48\u0e32\u0e27\u0e2a\u0e19\u0e31\u0e1a\u0e2a\u0e19\u0e38\u0e19 >= 2 \u0e0a\u0e34\u0e49\u0e19) ---
    s1 = "\u0e27\u0e31\u0e19%s\u0e17\u0e35\u0e48 %d %s \u0e15\u0e32\u0e21\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e2b\u0e23\u0e31\u0e10 \u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21 S&P 500 %s" % (_WD[d.weekday()], d.day, _TH_MON[d.month - 1], _pct(spy, 2))
    if lead and abs(lead[1]["chg"]) >= 2 and abs(lead[1]["chg"]) > abs(spy) * 1.5:
        ln = name.get(lead[0], lead[0])
        if (lead[1]["chg"] < 0) == down:
            s1 += " \u0e42\u0e14\u0e22\u0e01\u0e25\u0e38\u0e48\u0e21 %s %s \u0e2b\u0e19\u0e31\u0e01\u0e2a\u0e38\u0e14 %s \u0e17\u0e48\u0e32\u0e21\u0e01\u0e25\u0e32\u0e07%s %s" % (ln, "\u0e25\u0e07" if down else "\u0e02\u0e36\u0e49\u0e19", _pct(abs(lead[1]["chg"]), 1, False), "\u0e01\u0e32\u0e23\u0e40\u0e17\u0e02\u0e32\u0e22\u0e2b\u0e38\u0e49\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21" if down else "\u0e41\u0e23\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21", ln)
        else:
            s1 += " \u0e41\u0e15\u0e48\u0e01\u0e25\u0e38\u0e48\u0e21 %s %s %s \u0e2a\u0e27\u0e19\u0e17\u0e32\u0e07\u0e15\u0e25\u0e32\u0e14" % (ln, "\u0e25\u0e07" if lead[1]["chg"] < 0 else "\u0e02\u0e36\u0e49\u0e19", _pct(abs(lead[1]["chg"]), 1, False))
    mlist = sorted(movers or [], key=lambda x: x[1])
    if not down:
        mlist = mlist[::-1]
    shown = [x for x in mlist if (x[1] < 0) == down][:6]
    if th:
        ph = [t["phrase"] for t in th[:2]]
        s1 += " \u0e2a\u0e37\u0e48\u0e2d\u0e42\u0e22\u0e07\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49\u0e01\u0e31\u0e1a" + " \u0e41\u0e25\u0e30".join(ph)
    if shown and len([x for x in (movers or []) if abs(x[1]) >= 3 and (x[1] < 0) == down]) >= 3:
        s1 += " \u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27%s\u0e41\u0e23\u0e07\u0e43\u0e19\u0e27\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 (\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07)" % ("\u0e25\u0e07" if down else "\u0e02\u0e36\u0e49\u0e19")
    pl = []
    for s_, v in [("SPY", mv.get("SPY", {"chg": spy}))] + top3:
        c_ = _UPC if v["chg"] >= 0 else _DNC
        bg_ = "rgba(25,245,165,.10)" if v["chg"] >= 0 else "rgba(255,77,109,.12)"
        pl.append('<div class="me-p" style="color:%s!important;-webkit-text-fill-color:%s;border-color:%s;background:%s">%s %s</div>' % (
            c_, c_, c_, bg_, _e(name.get(s_, s_)), _pct(v["chg"], 1)))
    pills = "".join(pl)
    mv_html = ""

    def _mrow(lst, is_down, title):
        mp = []
        for t_, ch in lst:
            c_ = _UPC if ch >= 0 else _DNC
            bg_ = "rgba(25,245,165,.10)" if ch >= 0 else "rgba(255,77,109,.12)"
            mp.append('<div class="me-p" style="color:%s!important;-webkit-text-fill-color:%s;border-color:%s;background:%s">%s %s</div>' % (c_, c_, c_, bg_, _e(t_), _pct(ch, 1)))
        return '<div class="me-th" style="color:#e8ecfa!important;-webkit-text-fill-color:#e8ecfa">%s</div><div class="me-g">%s</div>' % (_e(title), "".join(mp))

    if movers:
        losers = sorted([x for x in movers if x[1] < 0], key=lambda x: x[1])
        gainers = sorted([x for x in movers if x[1] > 0], key=lambda x: -x[1])
        nl = len([x for x in losers if x[1] <= -3])
        ng = len([x for x in gainers if x[1] >= 3])
        pri = (losers, True, nl) if down else (gainers, False, ng)
        sec = (gainers, False, ng) if down else (losers, True, nl)
        if pri[0]:
            mv_html += _mrow(pri[0][:6], pri[1], "\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e17\u0e35\u0e48%s\u0e2b\u0e19\u0e31\u0e01\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19 (\u0e08\u0e32\u0e01 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e40\u0e1d\u0e49\u0e32\u0e14\u0e39 \u0e21\u0e35 %d \u0e15\u0e31\u0e27%s\u0e40\u0e01\u0e34\u0e19 3%%)" % ("\u0e25\u0e07" if pri[1] else "\u0e02\u0e36\u0e49\u0e19", len(movers), pri[2], "\u0e25\u0e07" if pri[1] else "\u0e02\u0e36\u0e49\u0e19"))
        if sec[0] and abs(sec[0][0][1]) >= 3:
            mv_html += _mrow(sec[0][:4], sec[1], "\u0e2a\u0e27\u0e19\u0e17\u0e32\u0e07\u0e15\u0e25\u0e32\u0e14: \u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e17\u0e35\u0e48%s\u0e41\u0e23\u0e07\u0e2a\u0e38\u0e14" % ("\u0e25\u0e07" if sec[1] else "\u0e02\u0e36\u0e49\u0e19"))
    fl = _read_flows(ev["flows"], spy)
    fp = ""
    if ev["flows"]:
        parts = []
        for k, lab in (("^VIX", "\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27 VIX"), ("TLT", "\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23"), ("GLD", "\u0e17\u0e2d\u0e07"), ("UUP", "\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c")):
            v = (ev["flows"].get(k) or {}).get("chg")
            if v is not None:
                parts.append("%s %s" % (lab, _pct(v, 1)))
        fp = " \u00b7 ".join(parts)
    body = ""
    if th:
        t0 = th[0]
        idxs = []
        for t in th[:2]:
            for i_ in t["idx"]:
                if i_ not in idxs:
                    idxs.append(i_)
        sel = idxs[:4]
        thai = _translate([rows[i_]["title_en"] for i_ in sel])
        body += '<div class="me-th">\u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e37\u0e48\u0e2d\u0e42\u0e22\u0e07\u0e01\u0e31\u0e1a\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e19\u0e35\u0e49 (\u0e18\u0e35\u0e21: %s)</div>' % _e(" \u00b7 ".join("%s %d \u0e0a\u0e34\u0e49\u0e19" % (t["label"], len(t["idx"])) for t in th[:2]))
        for i_, tt in zip(sel, thai):
            r = rows[i_]
            body += '<div class="me-h"><a href="%s" target="_blank" rel="noopener">%s</a> <small>%s</small></div>' % (_e(r["link"]), _e(tt), _e(r.get("source", "")))
        body += '<div class="me-note">\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e2b\u0e15\u0e38: \u0e02\u0e48\u0e32\u0e27\u0e2b\u0e25\u0e32\u0e22\u0e0a\u0e34\u0e49\u0e19\u0e1e\u0e39\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e43\u0e19\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e40\u0e14\u0e35\u0e22\u0e27\u0e17\u0e35\u0e48\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a</div>'
    else:
        body += '<div class="me-note">\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48\u0e0a\u0e35\u0e49\u0e0a\u0e31\u0e14\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38 (\u0e44\u0e21\u0e48\u0e41\u0e2a\u0e14\u0e07\u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d\u0e02\u0e48\u0e32\u0e27\u0e04\u0e31\u0e14\u0e21\u0e31\u0e48\u0e27\u0e46 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e40\u0e14\u0e32\u0e1c\u0e34\u0e14) \u2014 \u0e01\u0e14\u0e04\u0e49\u0e19\u0e02\u0e48\u0e32\u0e27\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19\u0e40\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e44\u0e14\u0e49</div>'
    links = '<div class="me-h"><a href="%s" target="_blank" rel="noopener">\u0e02\u0e48\u0e32\u0e27\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19 \u2197</a>' % _e(_gnews("stock market after:%s before:%s" % (d.isoformat(), (d + _dt.timedelta(days=2)).isoformat())))
    if top3:
        links += ' \u00b7 <a href="%s" target="_blank" rel="noopener">\u0e02\u0e48\u0e32\u0e27\u0e01\u0e25\u0e38\u0e48\u0e21 %s \u2197</a>' % (_e(_gnews("%s stocks after:%s before:%s" % (top3[0][0], d.isoformat(), (d + _dt.timedelta(days=2)).isoformat()))), _e(name.get(top3[0][0], top3[0][0])))
    links += "</div>"
    focus = ""
    if focus_etf and focus_etf in mv:
        focus = '<div class="me-fl">\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e14\u0e39\u0e2d\u0e22\u0e39\u0e48 (%s): %s \u0e43\u0e19\u0e27\u0e31\u0e19\u0e19\u0e31\u0e49\u0e19</div>' % (_e(name.get(focus_etf, focus_etf)), _pct(mv[focus_etf]["chg"], 1))
    return ('<div class="me" style="--ac:%s"><div class="me-top"><div class="me-pct" style="color:%s!important;-webkit-text-fill-color:%s">%s</div>'
            '<div class="me-d">%d %s</div><div class="me-chip" style="color:%s!important;-webkit-text-fill-color:%s;border-color:%s">%s</div></div>'
            '<div class="me-s">%s</div><div class="me-g">%s</div>%s%s<div class="me-fl">\u0e40\u0e07\u0e34\u0e19\u0e44\u0e2b\u0e25\u0e44\u0e1b\u0e17\u0e32\u0e07\u0e44\u0e2b\u0e19: %s<br><small style="color:#8d97b8">%s</small></div>%s%s</div>') % (
        col, col, col, _pct(spy, 2), d.day, _TH_MON[d.month - 1], _MUTED, _MUTED, _MUTED,
        "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21" if abs(spy) >= 1.0 else "\u0e1a\u0e32\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21", _e(s1), pills, mv_html, focus, _e(fl), _e(fp), body, links)


def prefetch():
    """\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e15\u0e25\u0e32\u0e14\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32 (\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e02\u0e22\u0e31\u0e1a \u00b7 \u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48 \u00b7 \u0e02\u0e48\u0e32\u0e27\u0e23\u0e2d\u0e1a\u0e27\u0e31\u0e19) \u0e41\u0e1a\u0e1a\u0e02\u0e19\u0e32\u0e19 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e15\u0e2d\u0e19\u0e27\u0e32\u0e14\u0e2b\u0e19\u0e49\u0e32\u0e2d\u0e48\u0e32\u0e19\u0e08\u0e32\u0e01\u0e41\u0e04\u0e0a"""
    evs = _find_events()
    if not evs:
        return
    try:
        import insight as _in
        dates = tuple(e["date"].isoformat() for e in evs)
        jobs = [lambda: _movers(dates)]
        for e in evs:
            ranked = sorted([(s, v) for s, v in e["moves"].items() if s != "SPY"], key=lambda x: -abs(x[1]["chg"]))
            groups = tuple(s for s, _v in ranked[:3])
            jobs.append(lambda e=e, groups=groups: _news_for_day(e["date"].isoformat(), groups))
        _in._par(jobs, 4)
    except Exception:
        pass


def render_market_events(ai_key="", compact=False, focus_etf=None):
    st.markdown(_CSS, unsafe_allow_html=True)
    if not compact:
        st.markdown('<div class="section-label">\u25c6 \u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e15\u0e25\u0e32\u0e14\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u2014 \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14/\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e22\u0e31\u0e1a\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19</div>', unsafe_allow_html=True)
        st.caption("\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e02\u0e48\u0e32\u0e27\u0e2b\u0e38\u0e49\u0e19\u0e23\u0e32\u0e22\u0e15\u0e31\u0e27 \u0e41\u0e15\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e23\u0e37\u0e2d\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e22\u0e31\u0e1a\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34 (\u0e40\u0e0a\u0e48\u0e19 \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e15\u0e31\u0e49\u0e07 \u0e1c\u0e25\u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e43\u0e2b\u0e0d\u0e48 \u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a\u0e43\u0e2b\u0e21\u0e48 \u0e15\u0e37\u0e48\u0e19\u0e15\u0e23\u0e30\u0e2b\u0e19\u0e01\u0e02\u0e32\u0e22) \u00b7 "
                   "\u0e23\u0e30\u0e1a\u0e1a\u0e2b\u0e32\u0e27\u0e31\u0e19\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e08\u0e23\u0e34\u0e07 \u0e41\u0e25\u0e49\u0e27\u0e14\u0e36\u0e07\u0e02\u0e48\u0e32\u0e27\u0e21\u0e32\u0e1b\u0e23\u0e30\u0e01\u0e2d\u0e1a \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e48\u0e32\u0e27\u0e2b\u0e25\u0e32\u0e22\u0e0a\u0e34\u0e49\u0e19\u0e0a\u0e35\u0e49\u0e44\u0e1b\u0e17\u0e32\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e08\u0e30\u0e1a\u0e2d\u0e01\u0e15\u0e23\u0e07\u0e46 \u0e27\u0e48\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e0a\u0e31\u0e14 \u0e44\u0e21\u0e48\u0e40\u0e14\u0e32\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38")
    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e2b\u0e32\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e02\u0e22\u0e31\u0e1a\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34 ..."):
        evs = _find_events()
    if not evs:
        st.info("1 \u0e40\u0e14\u0e37\u0e2d\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e23\u0e37\u0e2d\u0e01\u0e25\u0e38\u0e48\u0e21\u0e02\u0e22\u0e31\u0e1a\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34 (\u0e2b\u0e23\u0e37\u0e2d\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e08\u0e32\u0e01 Yahoo \u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08)")
        return
    if compact and focus_etf:
        rel = [e for e in evs if focus_etf in e["moves"] and abs(e["moves"][focus_etf]["chg"]) >= 2.5]
        evs = (rel or evs)[:2]
    elif compact:
        evs = evs[:2]
    try:
        mvs = _movers(tuple(e["date"].isoformat() for e in evs))
    except Exception:
        mvs = {}
    for e in evs:
        try:
            st.markdown(_event_html(e, focus_etf, mvs.get(e["date"].isoformat())), unsafe_allow_html=True)
        except Exception as ex:
            st.caption("\u0e41\u0e2a\u0e14\u0e07\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 %s \u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08: %s" % (e.get("date"), str(ex)[:80]))
    st.caption("\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo Finance + Google News \u0e2d\u0e32\u0e08\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c/\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a \u00b7 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e17\u0e33\u0e19\u0e32\u0e22\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e0b\u0e37\u0e49\u0e2d-\u0e02\u0e32\u0e22")