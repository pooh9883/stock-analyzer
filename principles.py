# -*- coding: utf-8 -*-
"""
principles.py  [principles v1]
==============================
\u0e40\u0e2d\u0e32\u0e41\u0e19\u0e27\u0e04\u0e34\u0e14\u0e08\u0e32\u0e01\u0e1a\u0e17\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c "23 \u0e2b\u0e25\u0e31\u0e01\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e2b\u0e38\u0e49\u0e19 + \u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04 + Action Plan" \u0e21\u0e32\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e44\u0e14\u0e49

\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21\u0e15\u0e49\u0e19\u0e41\u0e1a\u0e1a 3 \u0e02\u0e49\u0e2d:
  1) \u0e04\u0e30\u0e41\u0e19\u0e19\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d "\u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01\u0e07\u0e1a\u0e08\u0e23\u0e34\u0e07" \u0e14\u0e49\u0e27\u0e22\u0e01\u0e15\u0e34\u0e01\u0e32\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e14\u0e39\u0e44\u0e14\u0e49 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e43\u0e2b\u0e49 AI \u0e15\u0e31\u0e49\u0e07\u0e04\u0e30\u0e41\u0e19\u0e19\u0e15\u0e32\u0e21\u0e43\u0e08)
  2) \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49\u0e27\u0e34\u0e08\u0e32\u0e23\u0e13\u0e0d\u0e32\u0e13 (\u0e27\u0e34\u0e2a\u0e31\u0e22\u0e17\u0e31\u0e28\u0e19\u0e4c\u0e1c\u0e39\u0e49\u0e1a\u0e23\u0e34\u0e2b\u0e32\u0e23 \u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07\u0e15\u0e25\u0e32\u0e14 \u0e2f\u0e25\u0e2f) \u0e44\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19\u0e41\u0e17\u0e19 \u0e41\u0e15\u0e48\u0e43\u0e2a\u0e48\u0e04\u0e33\u0e16\u0e32\u0e21\u0e43\u0e2b\u0e49\u0e15\u0e23\u0e27\u0e08\u0e40\u0e2d\u0e07 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e19\u0e31\u0e1a\u0e43\u0e19\u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22
  3) \u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e47\u0e19 "\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e08\u0e32\u0e01\u0e01\u0e23\u0e32\u0e1f" (\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a/\u0e41\u0e19\u0e27\u0e15\u0e49\u0e32\u0e19/\u0e23\u0e30\u0e22\u0e30 ATR) \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22 3-5 \u0e1b\u0e35 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22

\u26a0\ufe0f \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo Finance \u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a/\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c \u00b7 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e08\u0e30\u0e41\u0e2a\u0e14\u0e07\u0e27\u0e48\u0e32 "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d" \u0e44\u0e21\u0e48\u0e40\u0e14\u0e32\u0e41\u0e17\u0e19
"""
import html as _html
import math

import pandas as pd
import streamlit as st
import yfinance as yf

GREEN, YELLOW, RED, CYAN, MUTED = "#19f5a5", "#fcee0a", "#ff4d6d", "#00f0ff", "#7d86a6"


def _e(x):
    return _html.escape(str(x if x is not None else ""), quote=True)


def _ok(x):
    return isinstance(x, (int, float)) and not (isinstance(x, float) and (math.isnan(x) or math.isinf(x)))


def _lin(x, lo, hi):
    """x=lo \u2192 0 \u0e04\u0e30\u0e41\u0e19\u0e19, x=hi \u2192 100 \u0e04\u0e30\u0e41\u0e19\u0e19 (hi \u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32 lo \u0e44\u0e14\u0e49 = \u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e14\u0e35)"""
    if not _ok(x):
        return None
    t = (x - lo) / (hi - lo)
    return max(0.0, min(100.0, 100.0 * t))


def _avg(vals):
    v = [x for x in vals if x is not None]
    return sum(v) / len(v) if v else None


def _pc(x, d=1, sign=False):
    return "\u2014" if not _ok(x) else (("%+." + str(d) + "f%%") if sign else ("%." + str(d) + "f%%")) % x


def _usd(x):
    if not _ok(x):
        return "\u2014"
    a = abs(x)
    s = "-" if x < 0 else ""
    if a >= 1e9:
        return "%s%.1f \u0e1e\u0e31\u0e19\u0e25\u0e49\u0e32\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c" % (s, a / 1e9)
    if a >= 1e6:
        return "%s%.0f \u0e25\u0e49\u0e32\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c" % (s, a / 1e6)
    return "%s%s \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c" % (s, format(a, ",.0f"))


# ---------------------------------------------------------------
# \u0e42\u0e2b\u0e25\u0e14\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25
# ---------------------------------------------------------------
@st.cache_data(ttl=3600, show_spinner=False)
def _fetch(sym):
    t = yf.Ticker(sym)
    out = {}
    for name, fn in (("info", lambda: t.info), ("inc", lambda: t.income_stmt), ("bs", lambda: t.balance_sheet),
                     ("cf", lambda: t.cashflow), ("div", lambda: t.dividends)):
        try:
            out[name] = fn()
        except Exception:
            out[name] = None
    try:
        d = yf.download(sym, period="2y", interval="1d", auto_adjust=True, progress=False)
        if hasattr(d.columns, "nlevels") and d.columns.nlevels > 1:
            try:
                d = d[sym]
            except Exception:
                d.columns = d.columns.get_level_values(0)
        out["hist"] = d.dropna(subset=["Close"])
    except Exception:
        out["hist"] = None
    return out


def _series(df, labels, n=5):
    """\u0e41\u0e16\u0e27\u0e07\u0e1a (\u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u2192 \u0e40\u0e01\u0e48\u0e32\u0e2a\u0e38\u0e14) \u00b7 \u0e04\u0e37\u0e19 list \u0e02\u0e2d\u0e07 float (None = \u0e44\u0e21\u0e48\u0e21\u0e35)"""
    if df is None or getattr(df, "empty", True):
        return []
    try:
        d = df.sort_index(axis=1, ascending=False)
    except Exception:
        d = df
    for lb in labels:
        if lb in d.index:
            vals = []
            for v in list(d.loc[lb].iloc[:n]):
                try:
                    f = float(v)
                    vals.append(None if math.isnan(f) else f)
                except Exception:
                    vals.append(None)
            if any(v is not None for v in vals):
                return vals
    return []


def _first(s):
    return s[0] if s and s[0] is not None else None


def _cagr(s):
    """\u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e08\u0e32\u0e01\u0e1b\u0e35\u0e40\u0e01\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u2192 \u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u00b7 \u0e10\u0e32\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01"""
    v = [x for x in s if x is not None]
    if len(v) < 2 or v[-1] <= 0 or v[0] <= 0:
        return None, 0
    yrs = len(v) - 1
    return ((v[0] / v[-1]) ** (1.0 / yrs) - 1) * 100, yrs


# ---------------------------------------------------------------
# 23 \u0e2b\u0e25\u0e31\u0e01\u0e01\u0e32\u0e23
# ---------------------------------------------------------------
SELF = {
    1: ("\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e07\u0e48\u0e32\u0e22", "\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22\u0e44\u0e14\u0e49\u0e43\u0e19 1 \u0e1b\u0e23\u0e30\u0e42\u0e22\u0e04\u0e44\u0e2b\u0e21\u0e27\u0e48\u0e32\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e2b\u0e32\u0e40\u0e07\u0e34\u0e19\u0e08\u0e32\u0e01\u0e2d\u0e30\u0e44\u0e23 \u0e41\u0e25\u0e30\u0e43\u0e04\u0e23\u0e04\u0e37\u0e2d\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32?"),
    14: ("\u0e27\u0e34\u0e2a\u0e31\u0e22\u0e17\u0e31\u0e28\u0e19\u0e4c\u0e1c\u0e39\u0e49\u0e1a\u0e23\u0e34\u0e2b\u0e32\u0e23", "\u0e1c\u0e39\u0e49\u0e1a\u0e23\u0e34\u0e2b\u0e32\u0e23\u0e17\u0e33\u0e15\u0e32\u0e21\u0e17\u0e35\u0e48\u0e40\u0e04\u0e22\u0e1e\u0e39\u0e14\u0e44\u0e2b\u0e21? \u0e21\u0e35\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e1b\u0e23\u0e31\u0e1a\u0e01\u0e25\u0e22\u0e38\u0e17\u0e18\u0e4c\u0e16\u0e39\u0e01\u0e08\u0e31\u0e07\u0e2b\u0e27\u0e30\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e1b\u0e25\u0e48\u0e32?"),
    15: ("\u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07\u0e01\u0e32\u0e23\u0e15\u0e25\u0e32\u0e14", "\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e1b\u0e47\u0e19\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23\u0e43\u0e19\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21 \u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07\u0e01\u0e33\u0e25\u0e31\u0e07\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e2b\u0e23\u0e37\u0e2d\u0e25\u0e14?"),
    16: ("\u0e01\u0e32\u0e23\u0e1e\u0e36\u0e48\u0e07\u0e1e\u0e32\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e23\u0e32\u0e22\u0e43\u0e2b\u0e0d\u0e48", "\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32 1-2 \u0e23\u0e32\u0e22\u0e04\u0e34\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e01\u0e35\u0e48 % \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49? (\u0e14\u0e39\u0e43\u0e19 10-K \u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d customers)"),
    20: ("\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e2b\u0e48\u0e27\u0e07\u0e42\u0e0b\u0e48\u0e2d\u0e38\u0e1b\u0e17\u0e32\u0e19", "\u0e1e\u0e36\u0e48\u0e07\u0e42\u0e23\u0e07\u0e07\u0e32\u0e19/\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a/\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e43\u0e14\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e21\u0e32\u0e01\u0e44\u0e2b\u0e21?"),
    21: ("\u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a\u0e41\u0e25\u0e30\u0e20\u0e39\u0e21\u0e34\u0e23\u0e31\u0e10\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c", "\u0e21\u0e35\u0e02\u0e48\u0e32\u0e27\u0e20\u0e32\u0e29\u0e35 \u0e02\u0e49\u0e2d\u0e08\u0e33\u0e01\u0e31\u0e14\u0e2a\u0e48\u0e07\u0e2d\u0e2d\u0e01 \u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e14\u0e35\u0e17\u0e35\u0e48\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07\u0e44\u0e2b\u0e21?"),
    22: ("\u0e1e\u0e31\u0e19\u0e18\u0e21\u0e34\u0e15\u0e23\u0e17\u0e32\u0e07\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08", "\u0e1e\u0e36\u0e48\u0e07\u0e1e\u0e31\u0e19\u0e18\u0e21\u0e34\u0e15\u0e23\u0e23\u0e32\u0e22\u0e43\u0e14\u0e23\u0e32\u0e22\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e21\u0e32\u0e01\u0e44\u0e2b\u0e21 \u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27\u0e41\u0e04\u0e48\u0e44\u0e2b\u0e19?"),
}


def _p(n, title, score, reason):
    return {"n": n, "title": title, "score": score, "reason": reason, "kind": "calc"}


def principles(D):
    info = D.get("info") or {}
    inc, bs, cf = D.get("inc"), D.get("bs"), D.get("cf")
    rev = _series(inc, ["Total Revenue", "Operating Revenue"])
    ni = _series(inc, ["Net Income", "Net Income Common Stockholders"])
    gp = _series(inc, ["Gross Profit"])
    ebit = _series(inc, ["EBIT", "Operating Income"])
    intx = _series(inc, ["Interest Expense", "Interest Expense Non Operating"])
    rd = _series(inc, ["Research And Development"])
    assets = _series(bs, ["Total Assets"])
    eq = _series(bs, ["Stockholders Equity", "Common Stock Equity", "Total Equity Gross Minority Interest"])
    debt = _series(bs, ["Total Debt"])
    cash = _series(bs, ["Cash Cash Equivalents And Short Term Investments", "Cash And Cash Equivalents"])
    shares = _series(bs, ["Ordinary Shares Number", "Share Issued"])
    fcf = _series(cf, ["Free Cash Flow"])
    if not fcf:
        ocf, cap = _series(cf, ["Operating Cash Flow", "Cash Flow From Continuing Operating Activities"]), _series(cf, ["Capital Expenditure"])
        fcf = [(o + c) if (o is not None and c is not None) else None for o, c in zip(ocf, cap)] if ocf and cap else []
    out = []
    r0, ni0 = _first(rev), _first(ni)

    # 2 \u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e41\u0e02\u0e48\u0e07\u0e02\u0e31\u0e19 (\u0e23\u0e48\u0e2d\u0e07\u0e23\u0e2d\u0e22\u0e43\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02)
    gm = [(g / r) * 100 for g, r in zip(gp, rev) if g is not None and r]
    if gm:
        rng = max(gm) - min(gm)
        sc = 0.7 * _lin(sum(gm) / len(gm), 20, 60) + 0.3 * (_lin(rng, 15, 2) or 0)
        out.append(_p(2, "\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e41\u0e02\u0e48\u0e07\u0e02\u0e31\u0e19 (\u0e14\u0e39\u0e08\u0e32\u0e01\u0e23\u0e48\u0e2d\u0e07\u0e23\u0e2d\u0e22\u0e43\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02)", sc, "\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 %s (\u0e41\u0e01\u0e27\u0e48\u0e07\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07 %.0f \u0e08\u0e38\u0e14) \u2014 \u0e21\u0e32\u0e23\u0e4c\u0e08\u0e34\u0e49\u0e19\u0e2a\u0e39\u0e07\u0e41\u0e25\u0e30\u0e19\u0e34\u0e48\u0e07\u0e21\u0e31\u0e01\u0e2a\u0e30\u0e17\u0e49\u0e2d\u0e19\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e23\u0e32\u0e04\u0e32" % (_pc(sum(gm) / len(gm)), rng)))
    else:
        out.append(_p(2, "\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e41\u0e02\u0e48\u0e07\u0e02\u0e31\u0e19 (\u0e14\u0e39\u0e08\u0e32\u0e01\u0e23\u0e48\u0e2d\u0e07\u0e23\u0e2d\u0e22\u0e43\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02)", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 3 \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15
    cg, yrs = _cagr(rev)
    out.append(_p(3, "\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15\u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49", _lin(cg, 0, 25), "\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e1b\u0e35\u0e25\u0e30 %s (\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 %d \u0e1b\u0e35)" % (_pc(cg), yrs) if cg is not None else "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e1e\u0e2d (\u0e2b\u0e23\u0e37\u0e2d\u0e10\u0e32\u0e19\u0e1b\u0e35\u0e41\u0e23\u0e01\u0e15\u0e34\u0e14\u0e25\u0e1a/\u0e28\u0e39\u0e19\u0e22\u0e4c)"))
    # 4 \u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07
    nv = [x for x in ni if x is not None]
    if len(nv) >= 2:
        posfrac = sum(1 for x in nv if x > 0) / len(nv)
        rising = sum(1 for a, b in zip(nv[:-1], nv[1:]) if a > b) / (len(nv) - 1)
        cgn, _y = _cagr(ni)
        sc = (0.5 * (_lin(cgn, 0, 25) or 0) + 0.5 * 100 * rising) * posfrac if cgn is not None else 50 * posfrac * rising
        out.append(_p(4, "\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07", sc, "\u0e01\u0e33\u0e44\u0e23\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01 %d \u0e08\u0e32\u0e01 %d \u0e1b\u0e35 \u00b7 \u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e36\u0e49\u0e19\u0e08\u0e32\u0e01\u0e1b\u0e35\u0e01\u0e48\u0e2d\u0e19 %d \u0e08\u0e32\u0e01 %d \u0e04\u0e23\u0e31\u0e49\u0e07%s" % (
            sum(1 for x in nv if x > 0), len(nv), round(rising * (len(nv) - 1)), len(nv) - 1, (" \u00b7 \u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e1b\u0e35\u0e25\u0e30 " + _pc(cgn)) if cgn is not None else "")))
    else:
        out.append(_p(4, "\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 5 net margin / 6 ROE / 7 ROA
    nm = ni0 / r0 * 100 if _ok(ni0) and r0 else None
    out.append(_p(5, "\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34", _lin(nm, 0, 25), "\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 %s \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 (\u0e1b\u0e35\u0e07\u0e1a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14)" % _pc(nm) if nm is not None else "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    roe = ni0 / _first(eq) * 100 if _ok(ni0) and _first(eq) and _first(eq) > 0 else None
    out.append(_p(6, "ROE (\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e17\u0e38\u0e19)", _lin(roe, 5, 30), "ROE %s \u2014 \u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19" % _pc(roe) if roe is not None else "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    roa = ni0 / _first(assets) * 100 if _ok(ni0) and _first(assets) else None
    out.append(_p(7, "ROA (\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c)", _lin(roa, 2, 15), "ROA %s \u2014 \u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e15\u0e48\u0e2d\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14" % _pc(roa) if roa is not None else "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 8 FCF
    fv = [x for x in fcf if x is not None]
    if fv and r0:
        fm = fv[0] / r0 * 100
        posf = sum(1 for x in fv if x > 0) / len(fv)
        out.append(_p(8, "\u0e01\u0e23\u0e30\u0e41\u0e2a\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e2d\u0e34\u0e2a\u0e23\u0e30 (FCF)", 0.6 * (_lin(fm, 0, 20) or 0) + 0.4 * 100 * posf, "FCF %s = %s \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u00b7 \u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01 %d \u0e08\u0e32\u0e01 %d \u0e1b\u0e35" % (_usd(fv[0]), _pc(fm), sum(1 for x in fv if x > 0), len(fv))))
    else:
        out.append(_p(8, "\u0e01\u0e23\u0e30\u0e41\u0e2a\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e2d\u0e34\u0e2a\u0e23\u0e30 (FCF)", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e23\u0e30\u0e41\u0e2a\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 9 \u0e2b\u0e19\u0e35\u0e49
    d0, a0 = _first(debt), _first(assets)
    if d0 is not None and a0:
        out.append(_p(9, "\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e20\u0e32\u0e23\u0e30\u0e2b\u0e19\u0e35\u0e49\u0e2a\u0e34\u0e19", _lin(d0 / a0, 0.6, 0.1), "\u0e2b\u0e19\u0e35\u0e49\u0e23\u0e27\u0e21 %s = %.2f \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e2a\u0e34\u0e19\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c (\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22)" % (_usd(d0), d0 / a0)))
    else:
        out.append(_p(9, "\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e20\u0e32\u0e23\u0e30\u0e2b\u0e19\u0e35\u0e49\u0e2a\u0e34\u0e19", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2b\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 10 \u0e04\u0e27\u0e32\u0e21\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e08\u0e48\u0e32\u0e22\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22
    e0, i0 = _first(ebit), _first(intx)
    if e0 is not None and i0 not in (None, 0):
        cov = e0 / abs(i0)
        out.append(_p(10, "\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e08\u0e48\u0e32\u0e22\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22", _lin(cov, 1.5, 12), "\u0e01\u0e33\u0e44\u0e23\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e14\u0e33\u0e40\u0e19\u0e34\u0e19\u0e07\u0e32\u0e19\u0e04\u0e23\u0e2d\u0e1a\u0e04\u0e25\u0e38\u0e21\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22 %.1f \u0e40\u0e17\u0e48\u0e32" % cov))
    elif d0 is not None and a0 and d0 / a0 < 0.1:
        out.append(_p(10, "\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e08\u0e48\u0e32\u0e22\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22", 95, "\u0e41\u0e17\u0e1a\u0e44\u0e21\u0e48\u0e21\u0e35\u0e20\u0e32\u0e23\u0e30\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22 (\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e33\u0e21\u0e32\u0e01)"))
    else:
        out.append(_p(10, "\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e08\u0e48\u0e32\u0e22\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22", None, "\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e08\u0e48\u0e32\u0e22"))
    # 11 BVPS
    bv = [(e / s) for e, s in zip(eq, shares) if e is not None and s]
    if len(bv) >= 2 and bv[-1] > 0 and bv[0] > 0:
        g = ((bv[0] / bv[-1]) ** (1.0 / (len(bv) - 1)) - 1) * 100
        out.append(_p(11, "\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e32\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19 (BVPS)", _lin(g, 0, 12), "BVPS %s \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c \u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e1b\u0e35\u0e25\u0e30 %s" % (format(bv[0], ",.2f"), _pc(g))))
    elif bv:
        out.append(_p(11, "\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e32\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19 (BVPS)", None, "BVPS %s \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c \u0e41\u0e15\u0e48\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e21\u0e48\u0e1e\u0e2d\u0e27\u0e31\u0e14\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15" % format(bv[0], ",.2f")))
    else:
        out.append(_p(11, "\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e32\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19 (BVPS)", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 12 \u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14
    c0 = _first(cash)
    if c0 is not None and d0 is not None:
        sc = 95 if d0 <= 0 else _lin(c0 / d0, 0.2, 1.5)
        out.append(_p(12, "\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e43\u0e19\u0e21\u0e37\u0e2d", sc, "\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e41\u0e25\u0e30\u0e40\u0e07\u0e34\u0e19\u0e25\u0e07\u0e17\u0e38\u0e19\u0e23\u0e30\u0e22\u0e30\u0e2a\u0e31\u0e49\u0e19 %s \u00b7 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e2b\u0e19\u0e35\u0e49\u0e23\u0e27\u0e21 %s" % (_usd(c0), _usd(d0))))
    else:
        out.append(_p(12, "\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e43\u0e19\u0e21\u0e37\u0e2d", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14/\u0e2b\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 13 \u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19 (\u0e1b\u0e31\u0e19\u0e1c\u0e25 + \u0e0b\u0e37\u0e49\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e04\u0e37\u0e19)
    dv = D.get("div")
    hist = D.get("hist")
    px = float(hist["Close"].iloc[-1]) if hist is not None and len(hist) else None
    dy, dyrs = None, 0
    try:
        if dv is not None and len(dv):
            dv = dv.copy()
            dv.index = pd.to_datetime(dv.index).tz_localize(None) if getattr(dv.index, "tz", None) is not None else pd.to_datetime(dv.index)
            last12 = float(dv[dv.index >= dv.index.max() - pd.Timedelta(days=365)].sum())
            dy = last12 / px * 100 if px else None
            dyrs = len(set(dv.index.year[dv.index >= dv.index.max() - pd.Timedelta(days=365 * 5)]))
    except Exception:
        pass
    sh = [x for x in shares if x is not None]
    bb = (sh[-1] / sh[0] - 1) * 100 if len(sh) >= 2 and sh[0] else None       # +\u0e04\u0e48\u0e32 = \u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e25\u0e14\u0e25\u0e07 (\u0e0b\u0e37\u0e49\u0e2d\u0e04\u0e37\u0e19)
    base = 35 + (min(dyrs, 5) / 5 * 25 if dyrs else 0) + (_lin(dy, 0, 4) or 0) * 0.2 + ((_lin(bb, 0, 5) or 0) * 0.2 if bb is not None else 0)
    if bb is not None and bb < -3:
        base -= 15
    txt = []
    txt.append("\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 12 \u0e40\u0e14\u0e37\u0e2d\u0e19 %s (\u0e08\u0e48\u0e32\u0e22\u0e43\u0e19 %d \u0e08\u0e32\u0e01 5 \u0e1b\u0e35)" % (_pc(dy), dyrs) if dyrs else "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e1b\u0e31\u0e19\u0e1c\u0e25\u0e43\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49")
    if bb is not None:
        txt.append("\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19%s %s \u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e07\u0e1a\u0e17\u0e35\u0e48\u0e21\u0e35" % ("\u0e25\u0e14\u0e25\u0e07 (\u0e0b\u0e37\u0e49\u0e2d\u0e04\u0e37\u0e19\u0e2a\u0e38\u0e17\u0e18\u0e34)" if bb > 0 else "\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e36\u0e49\u0e19 (\u0e16\u0e39\u0e01\u0e25\u0e14\u0e2a\u0e31\u0e14\u0e2a\u0e48\u0e27\u0e19)", _pc(abs(bb))))
    out.append(_p(13, "\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19 (\u0e1b\u0e31\u0e19\u0e1c\u0e25/\u0e0b\u0e37\u0e49\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e04\u0e37\u0e19)", max(0, min(100, base)), " \u00b7 ".join(txt)))
    # 17 R&D
    r_0 = _first(rd)
    if r_0 is not None and r0:
        rr = r_0 / r0 * 100
        out.append(_p(17, "\u0e01\u0e32\u0e23\u0e27\u0e34\u0e08\u0e31\u0e22\u0e41\u0e25\u0e30\u0e1e\u0e31\u0e12\u0e19\u0e32 (R&D)", _lin(rr, 0, 12), "\u0e43\u0e0a\u0e49\u0e40\u0e07\u0e34\u0e19\u0e27\u0e34\u0e08\u0e31\u0e22\u0e41\u0e25\u0e30\u0e1e\u0e31\u0e12\u0e19\u0e32 %s \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 (%s)" % (_pc(rr), _usd(r_0))))
    else:
        out.append(_p(17, "\u0e01\u0e32\u0e23\u0e27\u0e34\u0e08\u0e31\u0e22\u0e41\u0e25\u0e30\u0e1e\u0e31\u0e12\u0e19\u0e32 (R&D)", None, "\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e04\u0e48\u0e32\u0e43\u0e0a\u0e49\u0e08\u0e48\u0e32\u0e22 R&D \u0e41\u0e22\u0e01\u0e43\u0e19\u0e07\u0e1a"))
    # 18 \u0e04\u0e27\u0e32\u0e21\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e15\u0e32\u0e21\u0e27\u0e31\u0e0f\u0e08\u0e31\u0e01\u0e23 (\u0e22\u0e34\u0e48\u0e07\u0e19\u0e34\u0e48\u0e07\u0e22\u0e34\u0e48\u0e07\u0e44\u0e14\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19\u0e2a\u0e39\u0e07)
    gs = [(a / b - 1) * 100 for a, b in zip(rev[:-1], rev[1:]) if a is not None and b]
    nmg = [(n_ / r_) * 100 for n_, r_ in zip(ni, rev) if n_ is not None and r_]
    parts, txt = [], []
    if len(gs) >= 3:
        sd = pd.Series(gs).std()
        parts.append(_lin(sd, 60, 5))
        txt.append("\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e41\u0e01\u0e27\u0e48\u0e07 \u00b1%.0f \u0e08\u0e38\u0e14" % sd)
    if len(nmg) >= 3:
        mr = max(nmg) - min(nmg)
        parts.append(_lin(mr, 40, 5))
        txt.append("\u0e21\u0e32\u0e23\u0e4c\u0e08\u0e34\u0e49\u0e19\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e41\u0e01\u0e27\u0e48\u0e07\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07 %.0f \u0e08\u0e38\u0e14" % mr)
    beta = info.get("beta")
    if _ok(beta):
        parts.append(_lin(beta, 2.2, 0.8))
        txt.append("\u0e40\u0e1a\u0e15\u0e49\u0e32 %.2f" % beta)
    out.append(_p(18, "\u0e04\u0e27\u0e32\u0e21\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e15\u0e32\u0e21\u0e27\u0e31\u0e0f\u0e08\u0e31\u0e01\u0e23 (\u0e04\u0e30\u0e41\u0e19\u0e19\u0e2a\u0e39\u0e07 = \u0e19\u0e34\u0e48\u0e07\u0e01\u0e27\u0e48\u0e32)", _avg(parts), " \u00b7 ".join(txt) if txt else "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 19 \u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07
    if hist is not None and len(hist) > 30 and "Volume" in hist.columns:
        dvol = float((hist["Close"] * hist["Volume"]).tail(63).mean())
        mc = info.get("marketCap")
        out.append(_p(19, "\u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22", _lin(math.log10(dvol), 6.5, 9) if dvol > 0 else None,
                      "\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e27\u0e31\u0e19\u0e25\u0e30 %s%s" % (_usd(dvol), (" \u00b7 \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14 " + _usd(mc)) if _ok(mc) else "")))
    else:
        out.append(_p(19, "\u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22", None, "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e23\u0e32\u0e04\u0e32\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    # 23 \u0e23\u0e32\u0e04\u0e32\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15
    pe = info.get("trailingPE")
    pe = pe if _ok(pe) and pe > 0 else (info.get("forwardPE") if _ok(info.get("forwardPE")) and info.get("forwardPE") > 0 else None)
    gro = cg
    if pe is not None and gro is not None and gro > 0:
        peg = pe / max(gro, 1.0)
        out.append(_p(23, "\u0e04\u0e27\u0e32\u0e21\u0e04\u0e38\u0e49\u0e21\u0e04\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e15\u0e48\u0e2d\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15", _lin(peg, 3, 0.5), "P/E %.1f \u0e40\u0e17\u0e48\u0e32 \u00f7 \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15\u0e1b\u0e35\u0e25\u0e30 %.0f%% = %.2f (\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 1 \u0e21\u0e31\u0e01\u0e16\u0e37\u0e2d\u0e27\u0e48\u0e32\u0e44\u0e21\u0e48\u0e41\u0e1e\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e32\u0e23\u0e42\u0e15) \u2014 \u0e43\u0e0a\u0e49 P/E \u0e08\u0e32\u0e01\u0e01\u0e33\u0e44\u0e23\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 \u0e0b\u0e36\u0e48\u0e07\u0e2d\u0e32\u0e08\u0e15\u0e48\u0e33\u0e40\u0e01\u0e34\u0e19\u0e08\u0e23\u0e34\u0e07\u0e43\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e01\u0e33\u0e44\u0e23\u0e1e\u0e38\u0e48\u0e07" % (pe, gro, peg)))
    elif pe is not None:
        out.append(_p(23, "\u0e04\u0e27\u0e32\u0e21\u0e04\u0e38\u0e49\u0e21\u0e04\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e15\u0e48\u0e2d\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15", _lin(pe, 40, 10), "P/E %.1f \u0e40\u0e17\u0e48\u0e32 \u0e41\u0e15\u0e48\u0e27\u0e31\u0e14\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u0e08\u0e36\u0e07\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19\u0e08\u0e32\u0e01 P/E \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27" % pe))
    else:
        out.append(_p(23, "\u0e04\u0e27\u0e32\u0e21\u0e04\u0e38\u0e49\u0e21\u0e04\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e15\u0e48\u0e2d\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15", None, "\u0e44\u0e21\u0e48\u0e21\u0e35 P/E (\u0e2d\u0e32\u0e08\u0e22\u0e31\u0e07\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19) \u0e2b\u0e23\u0e37\u0e2d\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"))
    for n, (t, q) in SELF.items():
        out.append({"n": n, "title": t, "score": None, "reason": q, "kind": "self"})
    out.sort(key=lambda x: x["n"])
    return out


def _stars(v):
    k = 0 if v is None else max(1, min(5, int(round(v / 20.0))))
    return "\u2605" * k + "\u2606" * (5 - k)


def ratings(ps):
    sc = {p["n"]: p["score"] for p in ps if p["score"] is not None}
    calc = list(sc.values())
    if not calc:
        return None
    q = sum(calc) / len(calc)
    growth = _avg([sc.get(3), sc.get(4)])
    safety = _avg([sc.get(9), sc.get(10), sc.get(12), sc.get(18), sc.get(19)])
    long_ = _avg([q, sc.get(23), sc.get(8)])
    risk_lv = None if safety is None else 100 - safety
    return {"quality": q, "growth": growth, "safety": safety, "risk": risk_lv, "long": long_, "n": len(calc), "total": len([p for p in ps if p["kind"] == "calc"])}


def _band(v):
    if v is None:
        return "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d", MUTED
    if v >= 75:
        return "\u0e41\u0e02\u0e47\u0e07\u0e41\u0e23\u0e07\u0e21\u0e32\u0e01", GREEN
    if v >= 60:
        return "\u0e14\u0e35", GREEN
    if v >= 45:
        return "\u0e01\u0e25\u0e32\u0e07\u0e46", YELLOW
    return "\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e30\u0e27\u0e31\u0e07", RED


def trend_summary(ps, rt):
    calc = sorted([p for p in ps if p["score"] is not None], key=lambda x: -x["score"])
    if not calc or not rt:
        return "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e07\u0e1a\u0e44\u0e21\u0e48\u0e1e\u0e2d\u0e17\u0e35\u0e48\u0e08\u0e30\u0e2a\u0e23\u0e38\u0e1b"
    strong = " \u0e41\u0e25\u0e30 ".join(p["title"].split(" (")[0] for p in calc[:2])
    weak = [p for p in calc[::-1] if p["score"] < 60][:2]
    s = "\u0e04\u0e30\u0e41\u0e19\u0e19\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 %.0f/100 (\u0e08\u0e32\u0e01 %d \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e14\u0e49) \u2014 \u0e08\u0e38\u0e14\u0e40\u0e14\u0e48\u0e19\u0e04\u0e37\u0e2d %s" % (rt["quality"], rt["n"], strong)
    if weak:
        s += " \u00b7 \u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e04\u0e27\u0e23\u0e40\u0e0a\u0e47\u0e01\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e04\u0e37\u0e2d %s" % " \u0e41\u0e25\u0e30 ".join(p["title"].split(" (")[0] for p in weak)
    else:
        s += " \u00b7 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e04\u0e30\u0e41\u0e19\u0e19\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 60"
    return s


# ---------------------------------------------------------------
# \u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e40\u0e0a\u0e34\u0e07\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04 + Action Plan (\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e08\u0e32\u0e01\u0e01\u0e23\u0e32\u0e1f \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33)
# ---------------------------------------------------------------
def technicals(hist):
    if hist is None or len(hist) < 120:
        return None
    c, h, lo = hist["Close"].astype(float), hist["High"].astype(float), hist["Low"].astype(float)
    px = float(c.iloc[-1])
    ema200 = float(c.ewm(span=200, adjust=False).mean().iloc[-1])
    sma50 = float(c.tail(50).mean())
    dl = c.diff()
    up, dn = dl.clip(lower=0), (-dl).clip(lower=0)
    rs = up.ewm(alpha=1 / 14, adjust=False).mean() / dn.ewm(alpha=1 / 14, adjust=False).mean().replace(0, float("nan"))
    rsi_s = 100 - 100 / (1 + rs)
    rsi, rsi3 = float(rsi_s.iloc[-1]), float(rsi_s.iloc[-4])
    tr = pd.concat([h - lo, (h - c.shift()).abs(), (lo - c.shift()).abs()], axis=1).max(axis=1)
    atr = float(tr.ewm(alpha=1 / 14, adjust=False).mean().iloc[-1])
    w = 5
    n = len(c)
    sl = [float(lo.iloc[i]) for i in range(max(w, n - 250), n - w) if lo.iloc[i] == lo.iloc[i - w:i + w + 1].min()]
    sh = [float(h.iloc[i]) for i in range(max(w, n - 250), n - w) if h.iloc[i] == h.iloc[i - w:i + w + 1].max()]
    hi52, lo52 = float(h.tail(252).max()), float(lo.tail(252).min())

    def cluster(levels, rev):
        zs = []
        for v in sorted(levels, reverse=rev):
            if zs and abs(v / zs[-1]["hi" if rev else "lo"] - 1) <= 0.03:
                zs[-1]["lo"], zs[-1]["hi"] = min(zs[-1]["lo"], v), max(zs[-1]["hi"], v)
                zs[-1]["k"] += 1
            else:
                zs.append({"lo": v, "hi": v, "k": 1})
        return zs
    below = [v for v in sl if v < px * 0.99]
    labels = []
    if ema200 < px * 0.99:
        below.append(ema200)
    if sma50 < px * 0.99:
        below.append(sma50)
    sup = cluster(below, True)[:3]
    for z in sup:
        z["mid"] = (z["lo"] + z["hi"]) / 2
    above = [v for v in sh if v > px * 1.01] + ([hi52] if hi52 > px * 1.01 else [])
    res = cluster(above, False)[:2]
    for z in res:
        z["mid"] = (z["lo"] + z["hi"]) / 2
    near_high = px >= hi52 * 0.98
    stop = (sup[0]["lo"] - 1.5 * atr) if sup else (px - 3 * atr)
    rr = ((res[0]["mid"] - px) / (px - stop)) if res and px > stop else None
    last_up = float(c.iloc[-1]) > float(c.iloc[-2])
    return {"px": px, "ema200": ema200, "sma50": sma50, "rsi": rsi, "rsi3": rsi3, "atr": atr, "sup": sup, "res": res, "stop": stop, "rr": rr,
            "hi52": hi52, "lo52": lo52, "near_high": near_high, "last_up": last_up}


def _rg(z, px):
    return format(z["lo"], ",.2f") if abs(z["hi"] - z["lo"]) < 0.005 * px else "%s\u2013%s" % (format(z["lo"], ",.2f"), format(z["hi"], ",.2f"))


def action_plan(t):
    """5 \u0e02\u0e49\u0e2d\u0e2a\u0e31\u0e07\u0e40\u0e01\u0e15: \u0e41\u0e15\u0e48\u0e25\u0e30\u0e02\u0e49\u0e2d\u0e04\u0e37\u0e19 (\u0e2a\u0e16\u0e32\u0e19\u0e30 good/mid/bad/na, \u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d, \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21)"""
    if not t:
        return []
    px = t["px"]
    out = []
    if px >= t["ema200"]:
        out.append(("good", "\u0e40\u0e0a\u0e47\u0e01\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c", "\u0e23\u0e32\u0e04\u0e32 %s \u0e2d\u0e22\u0e39\u0e48\u0e40\u0e2b\u0e19\u0e37\u0e2d\u0e40\u0e2a\u0e49\u0e19 EMA200 (%s) = \u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27\u0e22\u0e31\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e32\u0e02\u0e36\u0e49\u0e19" % (format(px, ",.2f"), format(t["ema200"], ",.2f"))))
    else:
        out.append(("bad", "\u0e40\u0e0a\u0e47\u0e01\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c", "\u0e23\u0e32\u0e04\u0e32 %s \u0e2d\u0e22\u0e39\u0e48\u0e43\u0e15\u0e49\u0e40\u0e2a\u0e49\u0e19 EMA200 (%s) \u0e2d\u0e22\u0e39\u0e48 %s = \u0e02\u0e32\u0e25\u0e07\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27 \u0e04\u0e27\u0e23\u0e23\u0e2d\u0e43\u0e2b\u0e49\u0e15\u0e31\u0e49\u0e07\u0e10\u0e32\u0e19\u0e01\u0e48\u0e2d\u0e19" % (format(px, ",.2f"), format(t["ema200"], ",.2f"), _pc(abs(px / t["ema200"] - 1) * 100))))
    r = t["rsi"]
    if r >= 70:
        out.append(("bad", "\u0e40\u0e0a\u0e47\u0e01\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21", "RSI %.0f \u0e23\u0e49\u0e2d\u0e19\u0e41\u0e23\u0e07 (\u0e40\u0e01\u0e34\u0e19 70) \u2014 \u0e23\u0e32\u0e04\u0e32\u0e27\u0e34\u0e48\u0e07\u0e40\u0e23\u0e47\u0e27\u0e40\u0e01\u0e34\u0e19 \u0e23\u0e30\u0e27\u0e31\u0e07\u0e01\u0e32\u0e23\u0e44\u0e25\u0e48\u0e23\u0e32\u0e04\u0e32" % r))
    elif r <= 30:
        out.append(("mid", "\u0e40\u0e0a\u0e47\u0e01\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21", "RSI %.0f \u0e02\u0e32\u0e22\u0e21\u0e32\u0e01\u0e40\u0e01\u0e34\u0e19 (\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 30) \u2014 \u0e2d\u0e32\u0e08\u0e40\u0e14\u0e49\u0e07\u0e44\u0e14\u0e49 \u0e41\u0e15\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19" % r))
    else:
        out.append(("good", "\u0e40\u0e0a\u0e47\u0e01\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21", "RSI %.0f \u0e2d\u0e22\u0e39\u0e48\u0e42\u0e0b\u0e19\u0e01\u0e25\u0e32\u0e07 (30-70) \u2014 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e23\u0e49\u0e2d\u0e19\u0e41\u0e23\u0e07\u0e40\u0e01\u0e34\u0e19\u0e44\u0e1b" % r))
    if t["sup"]:
        s1 = t["sup"][0]
        dist = (1 - s1["hi"] / px) * 100            # \u0e23\u0e32\u0e04\u0e32\u0e15\u0e49\u0e2d\u0e07\u0e25\u0e07\u0e2d\u0e35\u0e01\u0e01\u0e35\u0e48 % \u0e16\u0e36\u0e07\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a
        if dist <= 3:
            out.append(("good", "\u0e23\u0e2d\u0e22\u0e48\u0e2d", "\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e01\u0e25\u0e49\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a %s (\u0e2b\u0e48\u0e32\u0e07 %s)" % (_rg(s1, px), _pc(dist))))
        else:
            out.append(("mid", "\u0e23\u0e2d\u0e22\u0e48\u0e2d", "\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a\u0e43\u0e01\u0e25\u0e49\u0e2a\u0e38\u0e14\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48 %s \u0e2b\u0e48\u0e32\u0e07\u0e25\u0e07\u0e44\u0e1b %s \u2014 \u0e16\u0e49\u0e32\u0e2d\u0e22\u0e32\u0e01\u0e44\u0e14\u0e49\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e14\u0e35\u0e02\u0e36\u0e49\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e2d\u0e23\u0e32\u0e04\u0e32\u0e22\u0e48\u0e2d (\u0e44\u0e21\u0e48\u0e01\u0e32\u0e23\u0e31\u0e19\u0e15\u0e35\u0e27\u0e48\u0e32\u0e08\u0e30\u0e22\u0e48\u0e2d)" % (_rg(s1, px), _pc(dist))))
    else:
        out.append(("na", "\u0e23\u0e2d\u0e22\u0e48\u0e2d", "\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a\u0e0a\u0e31\u0e14\u0e40\u0e08\u0e19\u0e43\u0e15\u0e49\u0e23\u0e32\u0e04\u0e32\u0e08\u0e32\u0e01\u0e01\u0e23\u0e32\u0e1f 1 \u0e1b\u0e35"))
    if t["rsi"] > t["rsi3"] and t["last_up"]:
        out.append(("good", "\u0e23\u0e2d\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", "RSI \u0e40\u0e23\u0e34\u0e48\u0e21\u0e2b\u0e31\u0e19\u0e02\u0e36\u0e49\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a 3 \u0e27\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19 (%.0f \u2192 %.0f) \u0e41\u0e25\u0e30\u0e1b\u0e34\u0e14\u0e1a\u0e27\u0e01\u0e27\u0e31\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u2014 \u0e40\u0e23\u0e34\u0e48\u0e21\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e14\u0e35\u0e14\u0e01\u0e25\u0e31\u0e1a" % (t["rsi3"], t["rsi"])))
    else:
        out.append(("mid", "\u0e23\u0e2d\u0e01\u0e32\u0e23\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e01\u0e25\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e0a\u0e31\u0e14 (RSI %.0f \u0e40\u0e17\u0e35\u0e22\u0e1a 3 \u0e27\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19 %.0f) \u2014 \u0e23\u0e2d\u0e14\u0e39\u0e41\u0e17\u0e48\u0e07\u0e40\u0e17\u0e35\u0e22\u0e19\u0e01\u0e25\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e2b\u0e23\u0e37\u0e2d RSI \u0e2b\u0e31\u0e19\u0e02\u0e36\u0e49\u0e19\u0e01\u0e48\u0e2d\u0e19" % (t["rsi"], t["rsi3"])))
    out.append(("na", "\u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e20\u0e32\u0e1e\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19", "\u0e16\u0e49\u0e32\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e34\u0e14\u0e2b\u0e25\u0e38\u0e14 %s (\u0e2b\u0e48\u0e32\u0e07\u0e25\u0e07\u0e44\u0e1b %s \u00b7 \u0e43\u0e15\u0e49\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a 1.5 \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07 ATR) \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e20\u0e32\u0e1e\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a\u0e40\u0e14\u0e34\u0e21\u0e44\u0e21\u0e48\u0e22\u0e37\u0e19 \u2014 \u0e04\u0e27\u0e23\u0e27\u0e32\u0e07\u0e41\u0e1c\u0e19\u0e08\u0e33\u0e01\u0e31\u0e14\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e2d\u0e07" % (format(t["stop"], ",.2f"), _pc((1 - t["stop"] / px) * 100))))
    return out


# ---------------------------------------------------------------
# \u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25
# ---------------------------------------------------------------
_CSS = (
    "<style>"
    ".pr-top{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin:8px 0}"
    ".pr-r{padding:10px 14px;border:1px solid rgba(125,134,166,.28);border-top:3px solid var(--ac);background:rgba(8,12,28,.6)}"
    ".pr-rk{font-size:12.5px;color:#9aa4c4}"
    ".pr-rs{font-size:26px;letter-spacing:3px;line-height:1.25;color:var(--ac)!important}"
    ".pr-rb{font-size:13px;color:#cfd7f2}"
    ".pr-sum{margin:10px 0;padding:12px 16px;border-left:4px solid #fcee0a;background:rgba(252,238,10,.06);font-size:15px;line-height:1.7;color:#e6f1ff}"
    ".pr-tb{margin:6px 0}"
    ".pr-row{display:grid;grid-template-columns:34px minmax(150px,230px) 140px 1fr;gap:10px;align-items:center;padding:7px 4px;border-bottom:1px solid rgba(125,134,166,.16)}"
    ".pr-n{font-family:var(--mono,monospace);color:#7d86a6;font-size:13px}"
    ".pr-t{font-size:14px;font-weight:700;color:#e6f1ff}"
    ".pr-bar{display:flex;align-items:center;gap:8px}"
    ".pr-bg{flex:1;height:8px;background:rgba(125,134,166,.2)}"
    ".pr-fg{height:8px}"
    ".pr-sc{width:30px;text-align:right;font-family:var(--mono,monospace);font-weight:800;font-size:14px}"
    ".pr-why{font-size:12.8px;line-height:1.55;color:#b9c4e4}"
    ".pr-self .pr-t{color:#9aa4c4}"
    ".pr-self .pr-why{color:#9aa4c4;font-style:italic}"
    ".pr-tag{display:inline-block;padding:1px 8px;border:1px dashed rgba(125,134,166,.6);font-size:12px;color:#9aa4c4}"
    ".pr-lad{margin:8px 0}"
    ".pr-l{display:flex;justify-content:space-between;gap:12px;padding:7px 12px;margin:3px 0;border-left:4px solid var(--ac);background:rgba(125,134,166,.08);font-size:14px;color:#e6f1ff}"
    ".pr-l small{color:#9aa4c4;font-size:12.5px}"
    ".pr-now{background:rgba(0,240,255,.14);font-weight:800}"
    ".pr-ap{display:flex;gap:12px;padding:9px 12px;margin:6px 0;border:1px solid rgba(125,134,166,.25);border-left:4px solid var(--ac);background:rgba(8,12,28,.55)}"
    ".pr-ai{flex:0 0 26px;height:26px;line-height:26px;text-align:center;font-weight:900;color:#05060d;background:var(--ac)}"
    ".pr-ah{font-size:14px;font-weight:800;color:#e6f1ff}"
    ".pr-at{font-size:13.5px;line-height:1.6;color:#cfd7f2}"
    "@media(max-width:700px){.pr-row{grid-template-columns:28px 1fr}.pr-bar,.pr-why{grid-column:1/-1}}"
    "</style>"
)

_ST = {"good": GREEN, "mid": YELLOW, "bad": RED, "na": CYAN}


def _score_col(v):
    return MUTED if v is None else (GREEN if v >= 70 else (YELLOW if v >= 50 else RED))


def _rating_card(name, v, sub, col=None, stars=None):
    band, c = _band(v)
    c = col or c
    return ('<div class="pr-r" style="--ac:%s"><div class="pr-rk">%s</div><div class="pr-rs" style="color:%s!important">%s</div>'
            '<div class="pr-rb">%s</div></div>') % (c, _e(name), c, _stars(v if stars is None else stars), _e(sub))


def _ratings_html(rt):
    if not rt:
        return ""
    qb = _band(rt["quality"])
    gb = _band(rt["growth"])
    rk = rt["risk"]
    rlab, rcol = ("\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d", MUTED) if rk is None else (("\u0e15\u0e48\u0e33", GREEN) if rk < 35 else (("\u0e1b\u0e32\u0e19\u0e01\u0e25\u0e32\u0e07", YELLOW) if rk < 55 else ("\u0e2a\u0e39\u0e07", RED)))
    lb = _band(rt["long"])
    cards = (_rating_card("\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08", rt["quality"], "%s \u00b7 \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 %.0f/100" % (qb[0], rt["quality"]))
             + _rating_card("\u0e28\u0e31\u0e01\u0e22\u0e20\u0e32\u0e1e\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15", rt["growth"], "%s%s" % (gb[0], (" \u00b7 %.0f/100" % rt["growth"]) if rt["growth"] is not None else ""))
             + _rating_card("\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07", None if rk is None else rk, "\u0e23\u0e30\u0e14\u0e31\u0e1a%s (\u0e22\u0e34\u0e48\u0e07\u0e14\u0e32\u0e27\u0e21\u0e32\u0e01 \u0e22\u0e34\u0e48\u0e07\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07)" % rlab, col=rcol)
             + _rating_card("\u0e04\u0e27\u0e32\u0e21\u0e19\u0e48\u0e32\u0e16\u0e37\u0e2d\u0e22\u0e32\u0e27", rt["long"], "%s%s" % (lb[0], (" \u00b7 %.0f/100" % rt["long"]) if rt["long"] is not None else "")))
    return '<div class="pr-top">%s</div>' % cards


def _table_html(ps):
    rows = ""
    for p in ps:
        if p["kind"] == "self":
            rows += ('<div class="pr-row pr-self"><div class="pr-n">%d</div><div class="pr-t">%s</div><div class="pr-bar"><span class="pr-tag">\u0e15\u0e23\u0e27\u0e08\u0e40\u0e2d\u0e07</span></div>'
                     '<div class="pr-why">%s</div></div>') % (p["n"], _e(p["title"]), _e(p["reason"]))
        elif p["score"] is None:
            rows += ('<div class="pr-row"><div class="pr-n">%d</div><div class="pr-t">%s</div><div class="pr-bar"><span class="pr-tag">\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d</span></div>'
                     '<div class="pr-why">%s</div></div>') % (p["n"], _e(p["title"]), _e(p["reason"]))
        else:
            c = _score_col(p["score"])
            rows += ('<div class="pr-row"><div class="pr-n">%d</div><div class="pr-t">%s</div><div class="pr-bar"><div class="pr-bg"><div class="pr-fg" style="width:%.0f%%;background:%s"></div></div>'
                     '<div class="pr-sc" style="color:%s!important">%.0f</div></div><div class="pr-why">%s</div></div>') % (p["n"], _e(p["title"]), p["score"], c, c, p["score"], _e(p["reason"]))
    return '<div class="pr-tb">%s</div>' % rows


def _ladder_html(t):
    px = t["px"]
    pct = lambda v: _pc((v / px - 1) * 100, 1, True)
    rows = ""
    for z in reversed(t["res"]):
        rg = "%s" % format(z["lo"], ",.2f") if abs(z["hi"] - z["lo"]) < 0.005 * px else "%s\u2013%s" % (format(z["lo"], ",.2f"), format(z["hi"], ",.2f"))
        rows += '<div class="pr-l" style="--ac:%s"><div>\u0e41\u0e19\u0e27\u0e15\u0e49\u0e32\u0e19\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07 %s</div><small>%s \u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19</small></div>' % (YELLOW, rg, pct(z["mid"]))
    if not t["res"]:
        rows += '<div class="pr-l" style="--ac:%s"><div>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e41\u0e19\u0e27\u0e15\u0e49\u0e32\u0e19\u0e40\u0e01\u0e48\u0e32\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19</div><small>\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 52 \u0e2a\u0e31\u0e1b\u0e14\u0e32\u0e2b\u0e4c (%s)</small></div>' % (MUTED, format(t["hi52"], ",.2f"))
    rows += '<div class="pr-l pr-now" style="--ac:%s"><div>\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 %s</div><small>EMA200 %s \u00b7 SMA50 %s \u00b7 ATR %s</small></div>' % (
        CYAN, format(px, ",.2f"), format(t["ema200"], ",.2f"), format(t["sma50"], ",.2f"), format(t["atr"], ",.2f"))
    for i, z in enumerate(t["sup"]):
        rg = "%s" % format(z["lo"], ",.2f") if abs(z["hi"] - z["lo"]) < 0.005 * px else "%s\u2013%s" % (format(z["lo"], ",.2f"), format(z["hi"], ",.2f"))
        rows += '<div class="pr-l" style="--ac:%s"><div>\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e17\u0e35\u0e48 %d: %s</div><small>%s \u00b7 \u0e41\u0e15\u0e30\u0e21\u0e32 %d \u0e04\u0e23\u0e31\u0e49\u0e07</small></div>' % (GREEN, i + 1, rg, pct(z["mid"]), z["k"])
    if not t["sup"]:
        rows += '<div class="pr-l" style="--ac:%s"><div>\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a\u0e0a\u0e31\u0e14\u0e40\u0e08\u0e19\u0e43\u0e15\u0e49\u0e23\u0e32\u0e04\u0e32</div><small>\u0e43\u0e0a\u0e49 ATR \u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e41\u0e17\u0e19</small></div>' % MUTED
    rows += '<div class="pr-l" style="--ac:%s"><div>\u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e20\u0e32\u0e1e\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19 %s</div><small>%s \u00b7 \u0e43\u0e15\u0e49\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a 1.5\u00d7ATR</small></div>' % (RED, format(t["stop"], ",.2f"), pct(t["stop"]))
    extra = ""
    if t["rr"] is not None:
        extra = '<div class="in-foot" style="margin-top:6px">\u0e16\u0e49\u0e32\u0e44\u0e1b\u0e16\u0e36\u0e07\u0e41\u0e19\u0e27\u0e15\u0e49\u0e32\u0e19\u0e41\u0e23\u0e01 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e20\u0e32\u0e1e\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19 \u0e44\u0e14\u0e49\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e15\u0e48\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e23\u0e32\u0e27 <b>%.1f \u0e40\u0e17\u0e48\u0e32</b> (\u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01\u0e01\u0e23\u0e32\u0e1f \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19)</div>' % t["rr"]
    return '<div class="pr-lad">%s</div>%s' % (rows, extra)


def _plan_html(plan):
    h = ""
    for i, (st_, ttl, txt) in enumerate(plan, 1):
        h += '<div class="pr-ap" style="--ac:%s"><div class="pr-ai">%d</div><div><div class="pr-ah">%s</div><div class="pr-at">%s</div></div></div>' % (_ST[st_], i, _e(ttl), _e(txt))
    return h


def data_confidence(D, ps):
    """\u0e04\u0e27\u0e32\u0e21\u0e19\u0e48\u0e32\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e16\u0e37\u0e2d\u0e02\u0e2d\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19: \u0e07\u0e1a\u0e01\u0e35\u0e48\u0e1b\u0e35 \u00b7 \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u00b7 \u0e10\u0e32\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34 (\u0e40\u0e0a\u0e48\u0e19\u0e40\u0e1e\u0e34\u0e48\u0e07\u0e41\u0e22\u0e01\u0e15\u0e31\u0e27/\u0e40\u0e1e\u0e34\u0e48\u0e07\u0e1e\u0e25\u0e34\u0e01\u0e01\u0e33\u0e44\u0e23) \u00b7 \u0e23\u0e32\u0e04\u0e32\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e2a\u0e31\u0e49\u0e19"""
    inc = D.get("inc")
    rev = _series(inc, ["Total Revenue", "Operating Revenue"])
    ni = [x for x in _series(inc, ["Net Income", "Net Income Common Stockholders"]) if x is not None]
    yrs = len([x for x in rev if x is not None])
    calc = [x for x in ps if x["kind"] == "calc"]
    na = [x for x in calc if x["score"] is None]
    pts, why = 3, []
    if yrs < 3:
        pts -= 2 if yrs < 2 else 1
        why.append("\u0e21\u0e35\u0e07\u0e1a\u0e23\u0e32\u0e22\u0e1b\u0e35\u0e41\u0e04\u0e48 %d \u0e1b\u0e35" % yrs)
    if calc and len(na) >= len(calc) * 0.25:
        pts -= 1
        why.append("%d \u0e08\u0e32\u0e01 %d \u0e02\u0e49\u0e2d\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e1e\u0e23\u0e32\u0e30\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d" % (len(na), len(calc)))
    cg, _y = _cagr(rev)
    if cg is not None and cg >= 100:
        pts -= 1
        why.append("\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15\u0e2a\u0e39\u0e07\u0e21\u0e32\u0e01 (\u0e1b\u0e35\u0e25\u0e30 %.0f%%) \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e22\u0e31\u0e48\u0e07\u0e22\u0e37\u0e19\u0e15\u0e25\u0e2d\u0e14\u0e44\u0e1b \u0e41\u0e25\u0e30\u0e10\u0e32\u0e19\u0e1b\u0e35\u0e41\u0e23\u0e01\u0e2d\u0e32\u0e08\u0e15\u0e48\u0e33 \u0e08\u0e36\u0e07\u0e2d\u0e22\u0e48\u0e32\u0e40\u0e2d\u0e32\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e1b\u0e04\u0e39\u0e13\u0e15\u0e48\u0e2d" % cg)
    if len(ni) >= 3 and sum(1 for x in ni if x > 0) <= len(ni) / 2:
        pts -= 1
        why.append("\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e40\u0e1e\u0e34\u0e48\u0e07\u0e1e\u0e25\u0e34\u0e01\u0e08\u0e32\u0e01\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 \u0e04\u0e30\u0e41\u0e19\u0e19\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15\u0e41\u0e25\u0e30\u0e04\u0e27\u0e32\u0e21\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e2d\u0e32\u0e08\u0e40\u0e1e\u0e35\u0e49\u0e22\u0e19")
    h = D.get("hist")
    if h is None or len(h) < 252:
        pts -= 1
        why.append("\u0e23\u0e32\u0e04\u0e32\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e21\u0e48\u0e16\u0e36\u0e07 1 \u0e1b\u0e35")
    level = "good" if pts >= 3 else ("mid" if pts == 2 else "bad")
    return {"level": level, "why": why or ["\u0e07\u0e1a\u0e04\u0e23\u0e1a\u0e2b\u0e25\u0e32\u0e22\u0e1b\u0e35 \u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34\u0e02\u0e2d\u0e07\u0e10\u0e32\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02"], "yrs": yrs}


def compute(sym):
    """\u0e04\u0e37\u0e19 (\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23 23 \u0e02\u0e49\u0e2d, \u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21, \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04) \u00b7 \u0e43\u0e0a\u0e49\u0e41\u0e04\u0e0a\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25"""
    D = _fetch((sym or "").strip().upper())
    ps = principles(D)
    return ps, ratings(ps), technicals(D.get("hist")), data_confidence(D, ps)


def render_principles(sym):
    sym = (sym or "").strip().upper()
    if not sym:
        return
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown('<div class="section-label">\u25c6 \u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e 23 \u0e2b\u0e25\u0e31\u0e01\u0e01\u0e32\u0e23 + \u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07 \u2014 %s</div>' % _e(sym), unsafe_allow_html=True)
    st.caption("\u0e04\u0e30\u0e41\u0e19\u0e19\u0e17\u0e38\u0e01\u0e02\u0e49\u0e2d\u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01\u0e07\u0e1a\u0e08\u0e23\u0e34\u0e07\u0e14\u0e49\u0e27\u0e22\u0e01\u0e15\u0e34\u0e01\u0e32\u0e15\u0e32\u0e22\u0e15\u0e31\u0e27 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 AI \u0e15\u0e31\u0e49\u0e07\u0e04\u0e30\u0e41\u0e19\u0e19")
    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e23\u0e27\u0e1a\u0e23\u0e27\u0e21\u0e07\u0e1a 4-5 \u0e1b\u0e35\u0e41\u0e25\u0e30\u0e01\u0e23\u0e32\u0e1f\u0e23\u0e32\u0e04\u0e32 ..."):
        D = _fetch(sym)
    ps = principles(D)
    rt = ratings(ps)
    if not rt:
        st.info("\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e1e\u0e2d\u0e17\u0e35\u0e48\u0e08\u0e30\u0e04\u0e33\u0e19\u0e27\u0e13 (\u0e2b\u0e38\u0e49\u0e19\u0e19\u0e2d\u0e01\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e21\u0e31\u0e01\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a)")
    else:
        st.markdown(_ratings_html(rt), unsafe_allow_html=True)
        st.markdown('<div class="pr-sum">%s</div>' % _e(trend_summary(ps, rt)), unsafe_allow_html=True)
    calc = [p for p in ps if p["kind"] == "calc"]
    cf = data_confidence(D, ps)
    cl, cc = {"good": ("\u0e2a\u0e39\u0e07", GREEN), "mid": ("\u0e1b\u0e32\u0e19\u0e01\u0e25\u0e32\u0e07", YELLOW), "bad": ("\u0e15\u0e48\u0e33", RED)}[cf["level"]]
    st.markdown('<div class="pr-sum" style="border-left-color:%s">\u0e04\u0e27\u0e32\u0e21\u0e19\u0e48\u0e32\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e16\u0e37\u0e2d\u0e02\u0e2d\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e0a\u0e38\u0e14\u0e19\u0e35\u0e49: <b style="color:%s!important">%s</b> \u2014 %s</div>' % (cc, cc, cl, _e(" \u00b7 ".join(cf["why"]))), unsafe_allow_html=True)
    with st.expander("\U0001f4cb \u0e14\u0e39\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e32\u0e22\u0e02\u0e49\u0e2d (%d \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e04\u0e33\u0e19\u0e27\u0e13\u0e08\u0e32\u0e01\u0e07\u0e1a\u0e44\u0e14\u0e49)" % len(calc), expanded=False):
        st.caption("\u0e40\u0e02\u0e35\u0e22\u0e27 \u226570 \u00b7 \u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e07 50-69 \u00b7 \u0e41\u0e14\u0e07 <50")
        st.markdown(_table_html(calc), unsafe_allow_html=True)
    with st.expander("\U0001f9d0 \u0e2d\u0e35\u0e01 %d \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e1a\u0e2d\u0e01\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 (\u0e15\u0e23\u0e27\u0e08\u0e40\u0e2d\u0e07)" % (len(ps) - len(calc)), expanded=False):
        st.caption("\u0e02\u0e49\u0e2d\u0e40\u0e2b\u0e25\u0e48\u0e32\u0e19\u0e35\u0e49\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49\u0e27\u0e34\u0e08\u0e32\u0e23\u0e13\u0e0d\u0e32\u0e13\u0e08\u0e32\u0e01\u0e02\u0e48\u0e32\u0e27\u0e41\u0e25\u0e30\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19\u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e19\u0e31\u0e1a\u0e43\u0e19\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22")
        st.markdown(_table_html([p for p in ps if p["kind"] == "self"]), unsafe_allow_html=True)
    t = technicals(D.get("hist"))
    if t:
        st.markdown('<div class="in-sec">\u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e08\u0e32\u0e01\u0e01\u0e23\u0e32\u0e1f 1 \u0e1b\u0e35</div>', unsafe_allow_html=True)
        st.markdown(_ladder_html(t), unsafe_allow_html=True)
        with st.expander("\U0001f9ed \u0e02\u0e49\u0e2d\u0e2a\u0e31\u0e07\u0e40\u0e01\u0e15 5 \u0e02\u0e31\u0e49\u0e19: \u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c \u2192 \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21 \u2192 \u0e23\u0e2d\u0e22\u0e48\u0e2d \u2192 \u0e23\u0e2d\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19 \u2192 \u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e20\u0e32\u0e1e\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19", expanded=False):
            st.markdown(_plan_html(action_plan(t)), unsafe_allow_html=True)
    else:
        st.caption("\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e23\u0e32\u0e04\u0e32\u0e44\u0e21\u0e48\u0e1e\u0e2d\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32 (\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e23\u0e32\u0e27 6 \u0e40\u0e14\u0e37\u0e2d\u0e19)")
    st.caption("\u26a0\ufe0f \u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e04\u0e37\u0e2d\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e01\u0e25\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e40\u0e01\u0e48\u0e32\u0e41\u0e25\u0e30\u0e40\u0e2a\u0e49\u0e19\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22\u0e2b\u0e23\u0e37\u0e2d\u0e08\u0e38\u0e14\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e17\u0e35\u0e48\u0e41\u0e19\u0e30\u0e19\u0e33 \u00b7 \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e38\u0e14\u0e2b\u0e23\u0e37\u0e2d\u0e17\u0e30\u0e25\u0e38\u0e41\u0e19\u0e27\u0e40\u0e2b\u0e25\u0e48\u0e32\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49\u0e40\u0e2a\u0e21\u0e2d \u00b7 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo \u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a \u00b7 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e25\u0e07\u0e17\u0e38\u0e19")