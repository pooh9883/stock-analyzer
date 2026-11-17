# -*- coding: utf-8 -*-
"""
screener.py  [screener v1]
==========================
\u0e23\u0e30\u0e1a\u0e1a\u0e04\u0e31\u0e14\u0e01\u0e23\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e41\u0e25\u0e30\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15 (S&P 500 / Nasdaq 100) \u2014 4 \u0e40\u0e2a\u0e32: Quality \u00b7 Growth \u00b7 Value \u00b7 Momentum

1) Quality & Growth  7 \u0e40\u0e01\u0e13\u0e11\u0e4c (\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e44\u0e14\u0e49): \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15 \u226510% \u00b7 \u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e42\u0e15 \u226510% \u00b7 \u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15 \u226515% \u00b7 \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 \u226515%
                     \u00b7 ROIC \u226515% \u00b7 FCF \u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07 \u00b7 \u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 (\u0e15\u0e32\u0e21\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21)
   \u0e43\u0e0a\u0e49\u0e07\u0e1a\u0e23\u0e32\u0e22\u0e1b\u0e35\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e17\u0e48\u0e32\u0e17\u0e35\u0e48 Yahoo \u0e43\u0e2b\u0e49 (\u0e1b\u0e01\u0e15\u0e34 3-4 \u0e1b\u0e35) \u0e27\u0e31\u0e14\u0e40\u0e1b\u0e47\u0e19 CAGR / \u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1b\u0e35\u0e40\u0e14\u0e35\u0e22\u0e27
2) Valuation        P/E \u00b7 Forward P/E \u00b7 PEG \u00b7 \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e41\u0e17\u0e49\u0e08\u0e23\u0e34\u0e07 (DCF \u0e41\u0e1a\u0e1a\u0e07\u0e48\u0e32\u0e22) \u2192 \u0e2a\u0e48\u0e27\u0e19\u0e40\u0e1c\u0e37\u0e48\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22
3) Momentum         Relative Strength \u0e40\u0e17\u0e35\u0e22\u0e1a SPY (\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e44\u0e17\u0e25\u0e4c\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21) \u00b7 \u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e2a\u0e49\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 \u00b7 \u0e41\u0e23\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22 (Volume) \u00b7 \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21 12-1 \u0e40\u0e14\u0e37\u0e2d\u0e19
\u0e40\u0e2a\u0e23\u0e34\u0e21\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e2d\u0e07:       Piotroski F-Score (0-9 \u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e07\u0e1a) \u00b7 Rule of 40 \u00b7 \u0e01\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e21\u0e48 (dilution)

\u26a0\ufe0f \u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c \u2260 \u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19 \u2014 \u0e40\u0e1b\u0e47\u0e19\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e0a\u0e48\u0e27\u0e22\u0e04\u0e31\u0e14\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1b\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e40\u0e0a\u0e34\u0e07\u0e25\u0e36\u0e01\u0e15\u0e48\u0e2d (\u0e1b\u0e38\u0e48\u0e21\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e1b\u0e34\u0e14\u0e21\u0e38\u0e21\u0e21\u0e2d\u0e07\u0e40\u0e0a\u0e34\u0e07\u0e25\u0e36\u0e01\u0e02\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e44\u0e14\u0e49)
   \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo Finance \u0e2d\u0e32\u0e08\u0e02\u0e32\u0e14/\u0e1c\u0e34\u0e14\u0e1a\u0e32\u0e07\u0e15\u0e31\u0e27 \u00b7 \u0e07\u0e1a\u0e40\u0e01\u0e47\u0e1a\u0e43\u0e19\u0e44\u0e1f\u0e25\u0e4c screener_cache.json (\u0e43\u0e0a\u0e49\u0e0b\u0e49\u0e33\u0e44\u0e14\u0e49 7 \u0e27\u0e31\u0e19) \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e14\u0e36\u0e07\u0e43\u0e2b\u0e21\u0e48\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07
"""
import html as _html
import io
import json
import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd
import streamlit as st
import yfinance as yf

CACHE_FILE = Path(__file__).with_name("screener_cache.json")
CACHE_TTL = 7 * 86400          # \u0e07\u0e1a\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e44\u0e21\u0e48\u0e1a\u0e48\u0e2d\u0e22: \u0e43\u0e0a\u0e49\u0e0b\u0e49\u0e33 7 \u0e27\u0e31\u0e19
GREEN, YELLOW, RED, CYAN, MUTED = "#19f5a5", "#fcee0a", "#ff2a6d", "#00f0ff", "#7d86a6"

# ---------------------------------------------------------------
# \u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19 (\u0e14\u0e36\u0e07\u0e08\u0e32\u0e01 Wikipedia \u0e01\u0e48\u0e2d\u0e19 \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e43\u0e0a\u0e49\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e33\u0e23\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07 \u2014 \u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e15\u0e23\u0e07\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 100%)
# ---------------------------------------------------------------
NDX_FALLBACK = (
    "AAPL ABNB ADBE ADI ADP ADSK AEP AMAT AMD AMGN AMZN APP ARM ASML AVGO AXON AZN BKNG BKR CCEP CDNS CDW CEG CHTR CMCSA COST CPRT CRWD CSCO CSGP CSX "
    "CTAS CTSH DASH DDOG DXCM EA EXC FANG FAST FTNT GEHC GFS GILD GOOG GOOGL HON IDXX INTC INTU ISRG KDP KHC KLAC LIN LRCX LULU MAR MCHP MDLZ MELI META "
    "MNST MRVL MSFT MSTR MU NFLX NVDA NXPI ODFL ON ORLY PANW PAYX PCAR PDD PEP PLTR PYPL QCOM REGN ROP ROST SBUX SHOP SNPS TEAM TMUS TRI TSLA TTD TTWO "
    "TXN VRSK VRTX WBD WDAY XEL ZS"
).split()
SP500_FALLBACK = (
    "MMM AOS ABT ABBV ACN ADBE AMD AES AFL A APD ABNB AKAM ALB ARE ALGN ALLE LNT ALL GOOGL GOOG MO AMZN AMCR AEE AEP AXP AIG AMT AWK AMP AME AMGN APH ADI "
    "AON APA APO AAPL AMAT APTV ACGL ADM ANET AJG AIZ T ATO ADSK ADP AZO AVB AVY AXON BKR BALL BAC BAX BDX BRK-B BBY TECH BIIB BLK BX BK BA BKNG BSX BMY "
    "AVGO BR BRO BF-B BLDR BG BXP CHRW CDNS CZR CPT CPB COF CAH KMX CCL CARR CAT CBOE CBRE CDW COR CNC CNP CF CRL SCHW CHTR CVX CMG CB CHD CI CINF CTAS "
    "CSCO C CFG CLX CME CMS KO CTSH COIN CL CMCSA CAG COP ED STZ CEG COO CPRT GLW CPAY CTVA CSGP COST CTRA CRWD CCI CSX CMI CVS DHR DRI DVA DECK DE DELL "
    "DAL DVN DXCM FANG DLR DG DLTR D DPZ DASH DOV DOW DHI DTE DUK DD EMN ETN EBAY ECL EIX EW EA ELV EMR ENPH ETR EOG EPAM EQT EFX EQIX EQR ERIE ESS EL EG "
    "EVRG ES EXC EXE EXPE EXPD EXR XOM FFIV FDS FICO FAST FRT FDX FIS FITB FSLR FE FI F FTNT FTV FOXA FOX BEN FCX GRMN IT GE GEHC GEV GEN GNRC GD GIS GM "
    "GPC GILD GPN GL GDDY GS HAL HIG HAS HCA DOC HSIC HSY HPE HLT HOLX HD HON HRL HST HWM HPQ HUBB HUM HBAN HII IBM IEX IDXX ITW INCY IR PODD INTC ICE "
    "IFF IP INTU ISRG IVZ INVH IQV IRM JBHT JBL JKHY J JNJ JCI JPM K KVUE KDP KEY KEYS KMB KIM KMI KKR KLAC KHC KR LHX LH LRCX LW LVS LDOS LEN LII LLY LIN "
    "LYV LKQ LMT L LOW LULU LYB MTB MPC MKTX MAR MMC MLM MAS MA MTCH MKC MCD MCK MDT MRK META MET MTD MGM MCHP MU MSFT MAA MRNA MHK MOH TAP MDLZ MPWR MNST "
    "MCO MS MOS MSI MSCI NDAQ NTAP NFLX NEM NWSA NWS NEE NKE NI NDSN NSC NTRS NOC NCLH NRG NUE NVDA NVR NXPI ORLY OXY ODFL OMC ON OKE ORCL OTIS PCAR PKG "
    "PLTR PANW PH PAYX PAYC PYPL PNR PEP PFE PCG PM PSX PNW PNC POOL PPG PPL PFG PG PGR PLD PRU PEG PTC PSA PHM PWR QCOM DGX RL RJF RTX O REG REGN RF RSG "
    "RMD RVTY ROK ROL ROP ROST RCL SPGI CRM SBAC SLB STX SRE NOW SHW SPG SWKS SJM SW SNA SOLV SO LUV SWK SBUX STT STLD STE SYK SMCI SYF SNPS SYY TMUS TROW "
    "TTWO TPR TRGP TGT TEL TDY TER TSLA TXN TPL TXT TMO TJX TKO TSCO TT TDG TRV TRMB TFC TYL TSN USB UBER UDR ULTA UNP UAL UNH UPS URI VLO VTR VLTO VRSN "
    "VRSK VZ VRTX VTRS VICI V VST VMC WRB GWW WAB WMT DIS WBD WM WAT WEC WFC WELL WST WDC WY WMB WTW WDAY WYNN XEL XYL YUM ZBRA ZBH ZTS"
).split()


def _wiki_tables(url):
    from urllib.request import Request, urlopen
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=10) as r:
        return pd.read_html(io.StringIO(r.read().decode("utf-8", "ignore")))


@st.cache_data(ttl=86400, show_spinner=False)
def _universe_online():
    out = {}
    try:
        for t in _wiki_tables("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"):
            if "Symbol" in t.columns and len(t) > 400:
                out["sp500"] = [str(s).strip().replace(".", "-") for s in t["Symbol"]]
                break
    except Exception:
        pass
    try:
        for t in _wiki_tables("https://en.wikipedia.org/wiki/Nasdaq-100"):
            col = "Ticker" if "Ticker" in t.columns else ("Symbol" if "Symbol" in t.columns else None)
            if col and 80 <= len(t) <= 120:
                out["ndx"] = [str(s).strip().replace(".", "-") for s in t[col]]
                break
    except Exception:
        pass
    return out


def universe(choice):
    on = _universe_online()
    ndx, spx = on.get("ndx") or NDX_FALLBACK, on.get("sp500") or SP500_FALLBACK
    if choice == "ndx":
        lst = ndx
    elif choice == "sp500":
        lst = spx
    else:
        lst = list(ndx) + list(spx)
    return list(dict.fromkeys(lst))


# ---------------------------------------------------------------
# \u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e40\u0e25\u0e47\u0e01\u0e46
# ---------------------------------------------------------------
def _ok(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and not (isinstance(x, float) and (math.isnan(x) or math.isinf(x)))


def _clamp(x, lo=0.0, hi=100.0):
    return max(lo, min(hi, x))


def _e(x):
    return _html.escape(str(x if x is not None else ""), quote=True)


def _row(df, labels, n=5):
    """\u0e2d\u0e48\u0e32\u0e19\u0e41\u0e16\u0e27\u0e08\u0e32\u0e01\u0e07\u0e1a (\u0e04\u0e2d\u0e25\u0e31\u0e21\u0e19\u0e4c = \u0e1b\u0e35 \u0e40\u0e23\u0e35\u0e22\u0e07\u0e43\u0e2b\u0e21\u0e48\u2192\u0e40\u0e01\u0e48\u0e32) \u0e04\u0e37\u0e19 list \u0e22\u0e32\u0e27 n (\u0e44\u0e21\u0e48\u0e21\u0e35 = None)"""
    if df is None or getattr(df, "empty", True):
        return [None] * n
    try:
        df = df.sort_index(axis=1, ascending=False)
    except Exception:
        pass
    for lb in labels:
        if lb in df.index:
            vals = []
            for i in range(n):
                v = df.loc[lb].iloc[i] if i < df.shape[1] else None
                vals.append(float(v) if _ok(v) else None)
            if any(v is not None for v in vals):
                return vals
    return [None] * n


# ---------------------------------------------------------------
# \u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e14\u0e34\u0e1a + \u0e41\u0e04\u0e0a\u0e25\u0e07\u0e44\u0e1f\u0e25\u0e4c
# ---------------------------------------------------------------
INFO_KEYS = ["sector", "shortName", "marketCap", "trailingPE", "forwardPE", "trailingPegRatio", "pegRatio", "forwardEps", "trailingEps",
             "currentPrice", "regularMarketPrice", "debtToEquity", "sharesOutstanding", "earningsGrowth", "revenueGrowth"]


def fetch_raw(sym):
    t = yf.Ticker(sym)
    inc, cf, bs = t.income_stmt, t.cashflow, t.balance_sheet
    try:
        info = t.info or {}
    except Exception:
        info = {}
    raw = {
        "rev": _row(inc, ["Total Revenue", "Operating Revenue"]), "gp": _row(inc, ["Gross Profit"]),
        "ni": _row(inc, ["Net Income", "Net Income Common Stockholders"]),
        "ebit": _row(inc, ["EBIT", "Operating Income"]), "tax": _row(inc, ["Tax Rate For Calcs"]),
        "fcf": _row(cf, ["Free Cash Flow"]), "cfo": _row(cf, ["Operating Cash Flow", "Cash Flow From Continuing Operating Activities"]),
        "ta": _row(bs, ["Total Assets"]), "ic": _row(bs, ["Invested Capital"]),
        "debt": _row(bs, ["Total Debt"]), "eq": _row(bs, ["Stockholders Equity", "Common Stock Equity", "Total Equity Gross Minority Interest"]),
        "cash": _row(bs, ["Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments"]),
        "ca": _row(bs, ["Current Assets"]), "cl": _row(bs, ["Current Liabilities"]), "ltd": _row(bs, ["Long Term Debt"]),
        "shares": _row(bs, ["Ordinary Shares Number", "Share Issued"]),
        "info": {k: info.get(k) for k in INFO_KEYS if isinstance(info.get(k), (int, float, str)) and info.get(k) == info.get(k)},
    }
    if not any(v is not None for v in raw["rev"]):
        raise ValueError("no financials")
    return raw


def _load_cache():
    try:
        d = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        return d.get("data", {}) if d.get("v") == 1 else {}
    except Exception:
        return {}


def _save_cache(data):
    try:
        tmp = CACHE_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps({"v": 1, "data": data}, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, CACHE_FILE)
    except Exception:
        pass


def fetch_many(symbols, workers=6, progress=None):
    """\u0e14\u0e36\u0e07\u0e07\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35/\u0e2b\u0e21\u0e14\u0e2d\u0e32\u0e22\u0e38 \u00b7 \u0e40\u0e0b\u0e1f\u0e25\u0e07\u0e44\u0e1f\u0e25\u0e4c\u0e17\u0e38\u0e01 10 \u0e15\u0e31\u0e27 (\u0e16\u0e49\u0e32\u0e2b\u0e22\u0e38\u0e14\u0e01\u0e25\u0e32\u0e07\u0e17\u0e32\u0e07\u0e01\u0e47\u0e44\u0e21\u0e48\u0e40\u0e2a\u0e35\u0e22\u0e02\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e14\u0e36\u0e07\u0e41\u0e25\u0e49\u0e27)"""
    data = _load_cache()
    now = time.time()
    todo = [s for s in symbols if s not in data or now - data[s].get("t", 0) > CACHE_TTL]
    done, fail = 0, []
    if todo:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(fetch_raw, s): s for s in todo}
            for f in as_completed(futs):
                s = futs[f]
                try:
                    data[s] = {"t": time.time(), "raw": f.result()}
                except Exception:
                    data[s] = {"t": time.time(), "raw": None}      # \u0e08\u0e33\u0e27\u0e48\u0e32\u0e14\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u0e08\u0e30\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e25\u0e2d\u0e07\u0e0b\u0e49\u0e33\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07 (\u0e2b\u0e21\u0e14\u0e2d\u0e32\u0e22\u0e38\u0e41\u0e25\u0e49\u0e27\u0e04\u0e48\u0e2d\u0e22\u0e25\u0e2d\u0e07\u0e43\u0e2b\u0e21\u0e48)
                    fail.append(s)
                done += 1
                if done % 10 == 0:
                    _save_cache(data)
                if progress:
                    progress(done, len(todo), s)
        _save_cache(data)
    return data, len(todo), fail


# ---------------------------------------------------------------
# \u0e15\u0e31\u0e27\u0e0a\u0e35\u0e49\u0e27\u0e31\u0e14 (\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19\u0e25\u0e49\u0e27\u0e19 \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e44\u0e14\u0e49)
# ---------------------------------------------------------------
def cagr(series, max_int=4):
    """\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e15\u0e48\u0e2d\u0e1b\u0e35\u0e41\u0e1a\u0e1a\u0e17\u0e1a\u0e15\u0e49\u0e19 \u0e08\u0e32\u0e01\u0e04\u0e48\u0e32\u0e43\u0e2b\u0e21\u0e48\u0e2a\u0e38\u0e14 (index 0) \u0e16\u0e36\u0e07\u0e40\u0e01\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e17\u0e35\u0e48\u0e21\u0e35 (\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 max_int \u0e1b\u0e35) \u00b7 \u0e04\u0e48\u0e32\u0e15\u0e31\u0e49\u0e07\u0e15\u0e49\u0e19\u0e15\u0e49\u0e2d\u0e07 > 0"""
    pts = [v for v in series[: max_int + 1]]
    if not pts or pts[0] is None:
        return None, 0
    n = 0
    for i in range(len(pts) - 1, 0, -1):
        if pts[i] is not None and pts[i] > 0 and pts[0] > 0:
            n = i
            break
    if n == 0:
        return None, 0
    return ((pts[0] / pts[n]) ** (1.0 / n) - 1) * 100, n


def yoy_hits(series, thr, n=3):
    """\u0e01\u0e35\u0e48\u0e1b\u0e35\u0e08\u0e32\u0e01\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 (\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 n \u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14) \u0e17\u0e35\u0e48\u0e42\u0e15\u0e40\u0e01\u0e34\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c"""
    hit = tot = 0
    for i in range(min(n, len(series) - 1)):
        a, b = series[i], series[i + 1]
        if a is not None and b is not None and b > 0:
            tot += 1
            hit += 1 if (a / b - 1) * 100 >= thr else 0
    return hit, tot


def avg(vals):
    v = [x for x in vals if x is not None]
    return sum(v) / len(v) if v else None


def net_margin(raw, n=3):
    ms = [raw["ni"][i] / raw["rev"][i] * 100 for i in range(min(n, 5)) if raw["ni"][i] is not None and raw["rev"][i]]
    return avg(ms)


def roic_series(raw, n=3):
    out = []
    for i in range(min(n, 5)):
        ebit, tax = raw["ebit"][i], raw["tax"][i]
        ic = raw["ic"][i]
        if ic is None and raw["debt"][i] is not None and raw["eq"][i] is not None:
            ic = raw["debt"][i] + raw["eq"][i] - (raw["cash"][i] or 0)
        if ebit is None or not ic or ic <= 0:
            continue
        t = tax if (tax is not None and 0 <= tax <= 0.40) else 0.21
        out.append(ebit * (1 - t) / ic * 100)
    return out


# \u0e40\u0e1e\u0e14\u0e32\u0e19\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 = \u0e40\u0e1e\u0e14\u0e32\u0e19\u0e10\u0e32\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e15\u0e31\u0e49\u0e07 (th["de"]) x \u0e15\u0e31\u0e27\u0e04\u0e39\u0e13\u0e15\u0e32\u0e21\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21 \u00b7 None = \u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e19\u0e35\u0e49
DE_MULT = {"Financial Services": None, "Utilities": 2.0, "Real Estate": 2.0, "Communication Services": 1.5, "Industrials": 1.5}


def de_ratio(raw):
    d, e = raw["debt"][0], raw["eq"][0]
    if d is not None and e is not None:
        return (d / e if e > 0 else None), (e <= 0)
    de = (raw["info"] or {}).get("debtToEquity")
    return (de / 100.0 if _ok(de) else None), False


def fscore(raw):
    """Piotroski F-Score (0-9) \u0e08\u0e32\u0e01\u0e07\u0e1a\u0e23\u0e32\u0e22\u0e1b\u0e35 2 \u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u00b7 \u0e04\u0e37\u0e19 (\u0e04\u0e30\u0e41\u0e19\u0e19, \u0e08\u0e33\u0e19\u0e27\u0e19\u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e14\u0e49)"""
    g = lambda k, i: raw[k][i] if raw.get(k) and len(raw[k]) > i else None
    pts, n = 0, 0

    def chk(cond):
        nonlocal pts, n
        if cond is None:
            return
        n += 1
        pts += 1 if cond else 0

    ni0, ni1, ta0, ta1, cfo0 = g("ni", 0), g("ni", 1), g("ta", 0), g("ta", 1), g("cfo", 0)
    roa0 = ni0 / ta0 if ni0 is not None and ta0 else None
    roa1 = ni1 / ta1 if ni1 is not None and ta1 else None
    chk(None if roa0 is None else roa0 > 0)
    chk(None if cfo0 is None else cfo0 > 0)
    chk(None if roa0 is None or roa1 is None else roa0 > roa1)
    chk(None if cfo0 is None or ni0 is None else cfo0 > ni0)
    l0 = (g("ltd", 0) if g("ltd", 0) is not None else g("debt", 0))
    l1 = (g("ltd", 1) if g("ltd", 1) is not None else g("debt", 1))
    chk(None if l0 is None or l1 is None or not ta0 or not ta1 else l0 / ta0 < l1 / ta1)
    ca0, cl0, ca1, cl1 = g("ca", 0), g("cl", 0), g("ca", 1), g("cl", 1)
    chk(None if None in (ca0, cl0, ca1, cl1) or not cl0 or not cl1 else ca0 / cl0 > ca1 / cl1)
    s0, s1 = g("shares", 0), g("shares", 1)
    chk(None if s0 is None or s1 is None else s0 <= s1 * 1.005)
    gp0, gp1, r0, r1 = g("gp", 0), g("gp", 1), g("rev", 0), g("rev", 1)
    chk(None if None in (gp0, gp1, r0, r1) or not r0 or not r1 else gp0 / r0 > gp1 / r1)
    chk(None if None in (r0, r1, ta0, ta1) or not ta0 or not ta1 else r0 / ta0 > r1 / ta1)
    return pts, n


def dcf_value(raw, discount=0.10, terminal=0.03, years=5, cap=0.15):
    """\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e41\u0e17\u0e49\u0e08\u0e23\u0e34\u0e07\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e41\u0e1a\u0e1a DCF \u0e07\u0e48\u0e32\u0e22\u0e46: FCF \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 3 \u0e1b\u0e35 \u0e42\u0e15\u0e15\u0e32\u0e21\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e17\u0e35\u0e48\u0e23\u0e30\u0e21\u0e31\u0e14\u0e23\u0e30\u0e27\u0e31\u0e07 (\u226415%) \u0e41\u0e25\u0e49\u0e27\u0e04\u0e48\u0e2d\u0e22\u0e25\u0e14\u0e25\u0e07\u0e2a\u0e39\u0e48\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27"""
    info = raw.get("info") or {}
    sh = info.get("sharesOutstanding")
    f0 = avg(raw["fcf"][:3])
    if not _ok(sh) or sh <= 0 or f0 is None or f0 <= 0:
        return None
    gr = []
    c, _ = cagr(raw["rev"])
    fc, _ = cagr(raw["fcf"])
    for v in (c, fc):
        if v is not None:
            gr.append(v / 100.0)
    g0 = max(0.0, min(min(gr) if gr else 0.05, cap))                   # \u0e43\u0e0a\u0e49\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e42\u0e15\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49/\u0e42\u0e15 FCF \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19\u0e40\u0e1e\u0e14\u0e32\u0e19
    pv, f = 0.0, f0
    for y in range(1, years + 1):
        g = g0 + (terminal - g0) * (y - 1) / max(1, years - 1)         # \u0e04\u0e48\u0e2d\u0e22\u0e46 \u0e25\u0e14\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e25\u0e07\u0e2a\u0e39\u0e48\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27
        f *= 1 + g
        pv += f / (1 + discount) ** y
    tv = f * (1 + terminal) / (discount - terminal) / (1 + discount) ** years
    return (pv + tv) / sh


def evaluate(raw, th, mom=None, discount=0.10):
    """\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e2b\u0e38\u0e49\u0e19 1 \u0e15\u0e31\u0e27 \u2192 dict \u0e1c\u0e25\u0e17\u0e38\u0e01\u0e40\u0e2a\u0e32 \u00b7 th = \u0e40\u0e01\u0e13\u0e11\u0e4c\u0e17\u0e35\u0e48\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e15\u0e31\u0e49\u0e07"""
    info = raw.get("info") or {}
    r = {"sym": None, "name": info.get("shortName"), "sector": info.get("sector") or "\u2014"}
    crit = []                                                         # 7 \u0e40\u0e01\u0e13\u0e11\u0e4c: (\u0e0a\u0e37\u0e48\u0e2d, \u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e41\u0e2a\u0e14\u0e07, \u0e1c\u0e48\u0e32\u0e19 True/False/None)

    rc, rn = cagr(raw["rev"])
    gc, gn = cagr(raw["gp"])
    nc, nn = cagr(raw["ni"])
    nm = net_margin(raw)
    rs = roic_series(raw)
    ro = avg(rs)

    def add(name, val, passed):
        crit.append((name, val, passed))

    add("\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15 (CAGR)", "\u2014" if rc is None else "%.1f%% (%d \u0e1b\u0e35)" % (rc, rn), None if rc is None else rc >= th["rev"])
    add("\u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e42\u0e15 (CAGR)", "\u2014" if gc is None else "%.1f%% (%d \u0e1b\u0e35)" % (gc, gn), None if gc is None else gc >= th["gp"])
    add("\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15 (CAGR)", "\u2014" if nc is None else "%.1f%% (%d \u0e1b\u0e35)" % (nc, nn), None if nc is None else nc >= th["ni"])
    add("\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 (\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 3 \u0e1b\u0e35)", "\u2014" if nm is None else "%.1f%%" % nm, None if nm is None else nm >= th["nm"])
    add("ROIC (\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 3 \u0e1b\u0e35)", "\u2014" if ro is None else "%.1f%%" % ro, None if ro is None else ro >= th["roic"])
    fv = [v for v in raw["fcf"][:4] if v is not None]
    add("FCF \u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07", "\u2014" if not fv else "%d/%d \u0e1b\u0e35\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01" % (sum(1 for v in fv if v > 0), len(fv)), None if not fv else all(v > 0 for v in fv))
    de, neg_eq = de_ratio(raw)
    exempt = r["sector"] in DE_MULT and DE_MULT[r["sector"]] is None
    lim = th.get("de", 1.0) * (DE_MULT.get(r["sector"]) or 1.0)
    if exempt:
        add("\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 (D/E)", "\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19 \u2014 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e19\u0e35\u0e49", True)
    elif neg_eq:
        add("\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 (D/E)", "\u0e2a\u0e48\u0e27\u0e19\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e34\u0e14\u0e25\u0e1a", False)
    else:
        add("\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 (D/E)", "\u2014" if de is None else "%.2f \u0e40\u0e17\u0e48\u0e32 (\u0e40\u0e01\u0e13\u0e11\u0e4c \u2264 %.1f)" % (de, lim), None if de is None else de <= lim)
    r["crit"] = crit
    ok_n = sum(1 for c in crit if c[2] is True)
    r["passed"], r["known"] = ok_n, sum(1 for c in crit if c[2] is not None)

    # --- \u0e40\u0e2a\u0e23\u0e34\u0e21 ---
    fs, fn = fscore(raw)
    r["fscore"] = fs if fn >= 7 else None
    fcf0, rev0 = raw["fcf"][0], raw["rev"][0]
    rg_last = (raw["rev"][0] / raw["rev"][1] - 1) * 100 if raw["rev"][0] and raw["rev"][1] else None
    r["rule40"] = (rg_last + fcf0 / rev0 * 100) if rg_last is not None and fcf0 is not None and rev0 else None
    sc, _ = cagr(raw["shares"], 3)
    r["dilution"] = sc

    # --- \u0e40\u0e2a\u0e32 Quality / Growth (0-100) ---
    def part(v, thr):                                                  # \u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07: \u0e16\u0e36\u0e07\u0e40\u0e01\u0e13\u0e11\u0e4c = 100
        return None if v is None else _clamp(v / thr * 100 if thr > 0 else 0)

    if exempt:
        de_part = 100.0                                                # \u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19: \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19
    elif neg_eq:
        de_part = 0.0
    elif de is None:
        de_part = None
    else:
        de_part = _clamp((1 - max(0.0, de - lim) / lim) * 100)         # \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c = 100 \u00b7 \u0e40\u0e01\u0e34\u0e19\u0e41\u0e25\u0e49\u0e27\u0e04\u0e48\u0e2d\u0e22\u0e46 \u0e25\u0e14\u0e04\u0e30\u0e41\u0e19\u0e19
    q_parts = [part(nm, th["nm"]), part(ro, th["roic"]),
               100.0 if (fv and all(v > 0 for v in fv)) else (0.0 if fv else None),
               de_part, None if r["fscore"] is None else r["fscore"] / 9 * 100]
    g_parts = [part(rc, th["rev"]), part(gc, th["gp"]), part(nc, th["ni"]), None if r["rule40"] is None else _clamp(r["rule40"] / 40 * 100)]
    r["q_score"], r["g_score"] = avg(q_parts), avg(g_parts)

    # --- \u0e40\u0e2a\u0e32 Value ---
    price = info.get("currentPrice", info.get("regularMarketPrice"))
    pe, fpe = info.get("trailingPE"), info.get("forwardPE")
    peg = info.get("trailingPegRatio") if _ok(info.get("trailingPegRatio")) else info.get("pegRatio")
    if not _ok(peg) and _ok(fpe) and fpe > 0 and nc is not None and nc > 0:
        peg = fpe / nc                                                 # \u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e40\u0e2d\u0e07: Forward P/E \u00f7 \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e01\u0e33\u0e44\u0e23 (%)
    iv = dcf_value(raw, discount)
    mos = (iv - price) / iv * 100 if iv and _ok(price) and price > 0 else None
    r.update({"price": price, "pe": pe if _ok(pe) and pe > 0 else None, "fpe": fpe if _ok(fpe) and fpe > 0 else None,
              "peg": peg if _ok(peg) and peg > 0 else None, "iv": iv, "mos": mos})
    v_parts = [None if r["pe"] is None else _clamp(100 - max(0, r["pe"] - th["pe"]) / th["pe"] * 100),
               None if r["fpe"] is None else _clamp(100 - max(0, r["fpe"] - th["fpe"]) / th["fpe"] * 100),
               None if r["peg"] is None else _clamp(100 - max(0, r["peg"] - th["peg"]) / th["peg"] * 100),
               None if mos is None else _clamp(50 + mos * 1.25)]
    r["v_score"] = avg(v_parts)

    # --- \u0e40\u0e2a\u0e32 Momentum (\u0e04\u0e48\u0e32\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32) ---
    r["m_score"], r["mom"] = None, mom
    if mom:
        r["m_score"] = mom.get("score")

    ps = [r["q_score"], r["g_score"], r["v_score"], r["m_score"]]
    r["pillars_ok"] = sum(1 for p in ps if p is not None and p >= 60)
    r["total"] = avg(ps)
    return r


# ---------------------------------------------------------------
# \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32 (\u0e14\u0e36\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e38\u0e14)
# ---------------------------------------------------------------
def momentum_from_prices(close, volume, spy_close=None):
    """close/volume = pandas Series \u0e23\u0e32\u0e22\u0e27\u0e31\u0e19\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19 1 \u0e15\u0e31\u0e27 \u00b7 \u0e04\u0e37\u0e19 dict \u0e15\u0e31\u0e27\u0e0a\u0e35\u0e49\u0e27\u0e31\u0e14 (RS \u0e40\u0e1b\u0e47\u0e19\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e44\u0e17\u0e25\u0e4c\u0e04\u0e33\u0e19\u0e27\u0e13\u0e17\u0e35\u0e2b\u0e25\u0e31\u0e07\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21)"""
    c = close.dropna()
    if len(c) < 130:
        return None
    px = float(c.iloc[-1])
    ret = lambda d: (px / float(c.iloc[-1 - d]) - 1) * 100 if len(c) > d else None
    r3, r6, r9, r12 = ret(63), ret(126), ret(189), ret(252)
    r12_1 = (float(c.iloc[-22]) / float(c.iloc[-1 - 252]) - 1) * 100 if len(c) > 252 else None      # \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21 12-1 \u0e40\u0e14\u0e37\u0e2d\u0e19 (\u0e15\u0e31\u0e14\u0e40\u0e14\u0e37\u0e2d\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e17\u0e34\u0e49\u0e07)
    sma50, sma200 = float(c.tail(50).mean()), float(c.tail(200).mean()) if len(c) >= 200 else None
    trend = px > sma50 and (sma200 is None or sma50 > sma200)
    v = volume.reindex(c.index).fillna(0) if volume is not None else None
    vr = ud = None
    if v is not None and len(v) >= 90 and float(v.tail(90).mean()) > 0:
        vr = float(v.tail(20).mean()) / float(v.tail(90).mean())
        d = c.diff().tail(50)
        vv = v.tail(50)
        up, dn = float(vv[d > 0].sum()), float(vv[d < 0].sum())
        ud = up / dn if dn > 0 else None
    # RS \u0e41\u0e1a\u0e1a IBD: \u0e16\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e0a\u0e48\u0e27\u0e07\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32
    parts = [(0.4, r3), (0.2, r6), (0.2, r9), (0.2, r12)]
    have = [(w, x) for w, x in parts if x is not None]
    rs_raw = sum(w * x for w, x in have) / sum(w for w, _ in have) if have else None
    spy_rel = None
    if spy_close is not None and len(spy_close.dropna()) > 126 and r6 is not None:
        s = spy_close.dropna()
        spy_rel = r6 - (float(s.iloc[-1]) / float(s.iloc[-127]) - 1) * 100
    return {"px": px, "r3": r3, "r6": r6, "r12": r12, "r12_1": r12_1, "trend": trend, "vol_ratio": vr, "ud": ud, "rs_raw": rs_raw, "rel6": spy_rel,
            "sma50": sma50, "sma200": sma200}


def finish_momentum(moms):
    """\u0e40\u0e15\u0e34\u0e21 RS \u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e44\u0e17\u0e25\u0e4c (1-99) \u0e41\u0e25\u0e30\u0e04\u0e30\u0e41\u0e19\u0e19\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21 0-100 \u0e43\u0e2b\u0e49\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21"""
    vals = sorted(m["rs_raw"] for m in moms.values() if m and m.get("rs_raw") is not None)
    n = len(vals)
    for s, m in moms.items():
        if not m:
            continue
        if m.get("rs_raw") is not None and n > 1:
            rank = sum(1 for v in vals if v <= m["rs_raw"])
            m["rs"] = max(1, min(99, round(rank / n * 99)))
        else:
            m["rs"] = None
        parts = [m["rs"], 100.0 if m["trend"] else 0.0,
                 None if m["r12_1"] is None else _clamp(50 + m["r12_1"]),
                 None if m["vol_ratio"] is None else _clamp(vol_pts(m["vol_ratio"], m["ud"]))]
        m["score"] = avg(parts)
    return moms


def vol_pts(ratio, ud):
    p = _clamp(50 + (ratio - 1.0) * 60)                              # \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e0a\u0e48\u0e27\u0e07 20 \u0e27\u0e31\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a 90 \u0e27\u0e31\u0e19
    if ud is not None:
        p = (p + _clamp(50 + (ud - 1.0) * 50)) / 2.0               # \u0e41\u0e23\u0e07\u0e0b\u0e37\u0e49\u0e2d vs \u0e41\u0e23\u0e07\u0e02\u0e32\u0e22 (\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e27\u0e31\u0e19\u0e02\u0e36\u0e49\u0e19 \u00f7 \u0e27\u0e31\u0e19\u0e25\u0e07)
    return p


@st.cache_data(ttl=3600, show_spinner=False)
def momentum_batch(symbols):
    symbols = list(symbols)
    out = {}
    try:
        spy = yf.download("SPY", period="14mo", interval="1d", progress=False, auto_adjust=True)["Close"]
        spy = spy.iloc[:, 0] if hasattr(spy, "columns") else spy
    except Exception:
        spy = None
    for i in range(0, len(symbols), 80):
        chunk = symbols[i:i + 80]
        try:
            d = yf.download(" ".join(chunk), period="14mo", interval="1d", group_by="ticker", progress=False, threads=True, auto_adjust=True)
        except Exception:
            continue
        for s in chunk:
            try:
                sub = d[s] if len(chunk) > 1 else d
                out[s] = momentum_from_prices(sub["Close"], sub["Volume"], spy)
            except Exception:
                out[s] = None
    return finish_momentum(out)


# ---------------------------------------------------------------
# \u0e2b\u0e19\u0e49\u0e32\u0e08\u0e2d
# ---------------------------------------------------------------
# \u0e0a\u0e38\u0e14\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08\u0e23\u0e39\u0e1b (\u0e14\u0e49\u0e32\u0e19\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32 P/E \u00b7 Fwd P/E \u00b7 PEG \u0e43\u0e0a\u0e49\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e0a\u0e38\u0e14)
PRESETS = {
    "\u0e40\u0e02\u0e49\u0e21 (\u0e15\u0e32\u0e21\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e41\u0e0a\u0e23\u0e4c)": {"rev": 10.0, "gp": 20.0, "ni": 20.0, "nm": 20.0, "roic": 15.0, "de": 1.0, "minpass": 7,
                      "note": "\u0e40\u0e02\u0e49\u0e21\u0e21\u0e32\u0e01 \u2014 \u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e2a\u0e34\u0e1a\u0e15\u0e31\u0e27\u0e08\u0e32\u0e01\u0e23\u0e32\u0e27 500 (\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e01\u0e32\u0e23 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e19\u0e01\u0e31\u0e1a\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e14) \u0e2a\u0e48\u0e27\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35/\u0e0a\u0e33\u0e23\u0e30\u0e40\u0e07\u0e34\u0e19/\u0e22\u0e32"},
    "\u0e21\u0e32\u0e15\u0e23\u0e10\u0e32\u0e19 (\u0e15\u0e32\u0e21\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21\u0e41\u0e23\u0e01)": {"rev": 10.0, "gp": 10.0, "ni": 15.0, "nm": 15.0, "roic": 15.0, "de": 1.0, "minpass": 5,
                          "note": "\u0e2a\u0e21\u0e14\u0e38\u0e25 \u2014 \u0e44\u0e14\u0e49\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e01\u0e27\u0e49\u0e32\u0e07\u0e1e\u0e2d\u0e40\u0e25\u0e37\u0e2d\u0e01 \u0e41\u0e25\u0e30\u0e22\u0e31\u0e07\u0e04\u0e07\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e2a\u0e39\u0e07"},
    "\u0e1c\u0e48\u0e2d\u0e19": {"rev": 8.0, "gp": 8.0, "ni": 10.0, "nm": 10.0, "roic": 12.0, "de": 1.5, "minpass": 4,
                "note": "\u0e1c\u0e48\u0e2d\u0e19\u0e41\u0e25\u0e30\u0e01\u0e27\u0e49\u0e32\u0e07 \u2014 \u0e40\u0e2b\u0e21\u0e32\u0e30\u0e43\u0e0a\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e15\u0e49\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e04\u0e48\u0e2d\u0e22\u0e01\u0e23\u0e2d\u0e07\u0e15\u0e48\u0e2d\u0e14\u0e49\u0e27\u0e22\u0e40\u0e2a\u0e32\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32/\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21"},
}
DEFAULT_PRESET = "\u0e40\u0e02\u0e49\u0e21 (\u0e15\u0e32\u0e21\u0e20\u0e32\u0e1e\u0e17\u0e35\u0e48\u0e41\u0e0a\u0e23\u0e4c)"
DEFAULT_TH = {"rev": 10.0, "gp": 20.0, "ni": 20.0, "nm": 20.0, "roic": 15.0, "de": 1.0, "pe": 35.0, "fpe": 30.0, "peg": 1.5}
_TH_KEYS = {"rev": "th_rev", "gp": "th_gp", "ni": "th_ni", "nm": "th_nm", "roic": "th_roic", "de": "th_de"}


_CRIT_CAVEAT = """
**\u0e41\u0e25\u0e49\u0e27\u0e0a\u0e38\u0e14\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e19\u0e35\u0e49 "\u0e04\u0e31\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e42\u0e15\u0e08\u0e23\u0e34\u0e07\u0e17\u0e35\u0e48\u0e14\u0e35\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14" \u0e44\u0e2b\u0e21?** \u0e0a\u0e38\u0e14 "\u0e40\u0e02\u0e49\u0e21" \u0e04\u0e31\u0e14\u0e44\u0e14\u0e49\u0e14\u0e35\u0e43\u0e19\u0e41\u0e07\u0e48 *\u0e42\u0e15\u0e08\u0e23\u0e34\u0e07 + \u0e01\u0e33\u0e44\u0e23\u0e41\u0e1b\u0e25\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e08\u0e23\u0e34\u0e07 + \u0e44\u0e21\u0e48\u0e2b\u0e19\u0e35\u0e49\u0e17\u0e48\u0e27\u0e21 + \u0e23\u0e32\u0e04\u0e32\u0e44\u0e21\u0e48\u0e41\u0e1e\u0e07\u0e40\u0e01\u0e34\u0e19\u0e44\u0e1b* \u0e41\u0e15\u0e48\u0e04\u0e27\u0e23\u0e23\u0e39\u0e49\u0e02\u0e49\u0e2d\u0e08\u0e33\u0e01\u0e31\u0e14:
- **\u0e21\u0e2d\u0e07\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07** \u2014 \u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e08\u0e30\u0e42\u0e15\u0e15\u0e48\u0e2d (\u0e42\u0e14\u0e22\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e27\u0e31\u0e0f\u0e08\u0e31\u0e01\u0e23 \u0e40\u0e0a\u0e48\u0e19 \u0e0a\u0e34\u0e1b/\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e04\u0e27\u0e32\u0e21\u0e08\u0e33 \u0e17\u0e35\u0e48\u0e01\u0e33\u0e44\u0e23\u0e1e\u0e38\u0e48\u0e07\u0e15\u0e32\u0e21\u0e23\u0e2d\u0e1a \u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e23\u0e2d\u0e1a)
- **\u0e10\u0e32\u0e19\u0e15\u0e48\u0e33\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e42\u0e15\u0e2a\u0e39\u0e07\u0e40\u0e01\u0e34\u0e19\u0e08\u0e23\u0e34\u0e07** \u0e40\u0e0a\u0e48\u0e19 \u0e40\u0e1e\u0e34\u0e48\u0e07\u0e1e\u0e25\u0e34\u0e01\u0e08\u0e32\u0e01\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e21\u0e32\u0e01\u0e33\u0e44\u0e23
- **\u0e40\u0e02\u0e49\u0e21\u0e21\u0e32\u0e01\u0e2d\u0e32\u0e08\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e19\u0e49\u0e2d\u0e22** \u0e41\u0e25\u0e30\u0e15\u0e31\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e22\u0e35\u0e48\u0e22\u0e21\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e41\u0e1e\u0e07\u0e0a\u0e31\u0e48\u0e27\u0e04\u0e23\u0e32\u0e27\u0e17\u0e34\u0e49\u0e07 \u2014 \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e40\u0e08\u0e2d\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e32\u0e01\u0e44\u0e14\u0e49 \u0e25\u0e2d\u0e07\u0e1c\u0e48\u0e2d\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e17\u0e35\u0e25\u0e30\u0e02\u0e49\u0e2d
- **\u0e43\u0e0a\u0e49\u0e40\u0e1b\u0e47\u0e19 "\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e15\u0e49\u0e19"** \u0e41\u0e25\u0e49\u0e27\u0e01\u0e14\u0e14\u0e39\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e23\u0e32\u0e22\u0e15\u0e31\u0e27 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d
"""


def _crit_row(make, text):
    """\u0e0a\u0e48\u0e2d\u0e07\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e01\u0e13\u0e11\u0e4c 1 \u0e0a\u0e48\u0e2d\u0e07 \u0e17\u0e32\u0e07\u0e0b\u0e49\u0e32\u0e22 + \u0e04\u0e33\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22\u0e02\u0e2d\u0e07\u0e0a\u0e48\u0e2d\u0e07\u0e19\u0e31\u0e49\u0e19\u0e42\u0e14\u0e22\u0e40\u0e09\u0e1e\u0e32\u0e30 \u0e17\u0e32\u0e07\u0e02\u0e27\u0e32 (\u0e23\u0e39\u0e1b\u0e41\u0e1a\u0e1a: \u0e0a\u0e37\u0e48\u0e2d \u2265 X = \u0e04\u0e27\u0e32\u0e21\u0e2b\u0e21\u0e32\u0e22 \u00b7 \u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21)"""
    l, r = st.columns([1, 3], vertical_alignment="center")
    val = make(l)
    r.markdown(text)
    return val


def _apply_preset():
    p = PRESETS.get(st.session_state.get("sc_preset"), PRESETS[DEFAULT_PRESET])
    for k, key in _TH_KEYS.items():
        st.session_state[key] = p[k]
    st.session_state["sc_minpass"] = p["minpass"]


def _init_state():
    """\u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e17\u0e35\u0e48\u0e40\u0e02\u0e49\u0e32\u0e2b\u0e19\u0e49\u0e32: \u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e38\u0e14\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19 (\u0e2b\u0e25\u0e31\u0e07\u0e08\u0e32\u0e01\u0e19\u0e31\u0e49\u0e19\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e2d\u0e07\u0e44\u0e14\u0e49)"""
    if "sc_preset" not in st.session_state:
        st.session_state["sc_preset"] = DEFAULT_PRESET
    if "th_rev" not in st.session_state:
        _apply_preset()

_CSS = (
    "<style>"
    ".sc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;margin-top:8px}"
    ".sc-c{background:rgba(12,14,28,.86);border:1px solid rgba(0,240,255,.18);border-top:2px solid var(--ac,#00f0ff);padding:12px 14px}"
    ".sc-c h5{margin:0 0 8px;font-size:14px;color:var(--ac,#e6f1ff)}"
    ".sc-r{display:flex;justify-content:space-between;gap:12px;padding:4px 0;border-bottom:1px dashed rgba(125,134,166,.2);font-size:13px}"
    ".sc-r i{font-style:normal;color:#9aa4c4}.sc-r b{font-weight:600;color:#f1f5ff;text-align:right}"
    ".stApp .stDownloadButton > button, .stApp .stDownloadButton > button p, .stApp .stDownloadButton > button span, .stApp .stDownloadButton > button div{color:#05060d !important}"
    "</style>"
)


def _show_df(df, **kw):
    try:
        st.dataframe(df, width="stretch", **kw)
    except Exception:
        st.dataframe(df, use_container_width=True, **kw)


def _mark(p):
    return ("\u2705", GREEN) if p is True else (("\u274c", RED) if p is False else ("\u2796", MUTED))


def _detail(sym, r):
    ev = r
    crit = "".join('<div class="sc-r"><i>%s %s</i><b>%s</b></div>' % (_mark(p)[0], _e(n), _e(v)) for n, v, p in ev["crit"])
    fmt = lambda v, f="%.1f", s="": "\u2014" if v is None else (f % v) + s
    val = "".join('<div class="sc-r"><i>%s</i><b>%s</b></div>' % (_e(k), _e(v)) for k, v in [
        ("\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19", fmt(ev.get("price"), "%.2f", " \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c")), ("P/E \u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07", fmt(ev["pe"])), ("Forward P/E", fmt(ev["fpe"])),
        ("PEG", fmt(ev["peg"], "%.2f")), ("\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e41\u0e17\u0e49\u0e08\u0e23\u0e34\u0e07 (DCF \u0e07\u0e48\u0e32\u0e22)", fmt(ev["iv"], "%.2f", " \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c")),
        ("\u0e2a\u0e48\u0e27\u0e19\u0e40\u0e1c\u0e37\u0e48\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22 (+ = \u0e16\u0e39\u0e01\u0e01\u0e27\u0e48\u0e32 DCF)", fmt(ev["mos"], "%+.0f", "%"))])
    m = ev.get("mom") or {}
    mom = "".join('<div class="sc-r"><i>%s</i><b>%s</b></div>' % (_e(k), _e(v)) for k, v in [
        ("Relative Strength (1-99)", "\u2014" if m.get("rs") is None else str(m["rs"])), ("\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19 6 \u0e40\u0e14\u0e37\u0e2d\u0e19 \u0e40\u0e17\u0e35\u0e22\u0e1a SPY", fmt(m.get("rel6"), "%+.1f", " \u0e08\u0e38\u0e14")),
        ("\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21 12-1 \u0e40\u0e14\u0e37\u0e2d\u0e19", fmt(m.get("r12_1"), "%+.1f", "%")), ("\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c (\u0e23\u0e32\u0e04\u0e32 > SMA50 > SMA200)", "\u0e43\u0e0a\u0e48" if m.get("trend") else "\u0e44\u0e21\u0e48"),
        ("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 20 \u0e27\u0e31\u0e19 \u00f7 90 \u0e27\u0e31\u0e19", fmt(m.get("vol_ratio"), "%.2f", "\u00d7")), ("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e27\u0e31\u0e19\u0e02\u0e36\u0e49\u0e19 \u00f7 \u0e27\u0e31\u0e19\u0e25\u0e07 (50 \u0e27\u0e31\u0e19)", fmt(m.get("ud"), "%.2f", "\u00d7"))])
    ext = "".join('<div class="sc-r"><i>%s</i><b>%s</b></div>' % (_e(k), _e(v)) for k, v in [
        ("Piotroski F-Score (0-9)", "\u2014" if ev["fscore"] is None else "%d / 9" % ev["fscore"]), ("Rule of 40 (\u0e42\u0e15\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 + FCF margin)", fmt(ev["rule40"], "%.0f")),
        ("\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e15\u0e48\u0e2d\u0e1b\u0e35 (\u2212 = \u0e0b\u0e37\u0e49\u0e2d\u0e04\u0e37\u0e19)", fmt(ev["dilution"], "%+.1f", "%"))])
    st.markdown(_CSS + '<div class="sc-grid">'
                '<div class="sc-c" style="--ac:%s"><h5>\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e & \u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15 (7 \u0e40\u0e01\u0e13\u0e11\u0e4c \u0e1c\u0e48\u0e32\u0e19 %d/%d)</h5>%s</div>'
                '<div class="sc-c" style="--ac:%s"><h5>\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32 (Valuation)</h5>%s</div>'
                '<div class="sc-c" style="--ac:%s"><h5>\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21</h5>%s</div>'
                '<div class="sc-c" style="--ac:%s"><h5>\u0e21\u0e38\u0e21\u0e40\u0e2a\u0e23\u0e34\u0e21 (\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e2d\u0e07)</h5>%s</div></div>' % (GREEN, ev["passed"], 7, crit, YELLOW, val, CYAN, mom, "#ff7ad9", ext),
                unsafe_allow_html=True)


def render_screener(ai_key=""):
    st.markdown(_CSS, unsafe_allow_html=True)
    with st.expander("\U0001f4d6 \u0e2b\u0e25\u0e31\u0e01\u0e01\u0e32\u0e23\u0e02\u0e2d\u0e07\u0e23\u0e30\u0e1a\u0e1a\u0e19\u0e35\u0e49 (\u0e2d\u0e48\u0e32\u0e19\u0e01\u0e48\u0e2d\u0e19 1 \u0e19\u0e32\u0e17\u0e35)", expanded=False):
        st.markdown(
            """
**\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22:** \u0e2b\u0e32\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e21\u0e35 4 \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 \u2014 **Quality** (\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e) \u00b7 **Growth** (\u0e42\u0e15\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07) \u00b7 **Value** (\u0e23\u0e32\u0e04\u0e32\u0e2a\u0e21\u0e40\u0e2b\u0e15\u0e38\u0e2a\u0e21\u0e1c\u0e25) \u00b7 **Momentum** (\u0e23\u0e32\u0e04\u0e32\u0e41\u0e02\u0e47\u0e07\u0e41\u0e23\u0e07)

**\u0e02\u0e31\u0e49\u0e19 1 \u2014 7 \u0e40\u0e01\u0e13\u0e11\u0e4c\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e/\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15 (\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e0a\u0e38\u0e14\u0e40\u0e02\u0e49\u0e21/\u0e21\u0e32\u0e15\u0e23\u0e10\u0e32\u0e19/\u0e1c\u0e48\u0e2d\u0e19 \u0e2b\u0e23\u0e37\u0e2d\u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e2d\u0e07\u0e44\u0e14\u0e49):** \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15 \u00b7 \u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e42\u0e15 \u00b7 \u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15 \u00b7 \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 \u00b7 ROIC \u00b7 FCF \u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01\u0e17\u0e38\u0e01\u0e1b\u0e35 \u00b7 \u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 D/E
(\u0e0a\u0e38\u0e14 "\u0e40\u0e02\u0e49\u0e21" = \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u226510%, \u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19 \u226520%, \u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 \u226520%, margin \u226520%, ROIC \u226515%, D/E <1 \u00b7 \u0e18\u0e19\u0e32\u0e04\u0e32\u0e23/\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e40\u0e01\u0e13\u0e11\u0e4c D/E \u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04\u0e41\u0e25\u0e30\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e2f \u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32)

**\u0e02\u0e31\u0e49\u0e19 2 \u2014 \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32:** P/E \u00b7 Forward P/E \u00b7 PEG \u00b7 \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e41\u0e17\u0e49\u0e08\u0e23\u0e34\u0e07 (DCF \u0e41\u0e1a\u0e1a\u0e07\u0e48\u0e32\u0e22) \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e23\u0e32\u0e04\u0e32

**\u0e02\u0e31\u0e49\u0e19 3 \u2014 \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21:** Relative Strength (\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a 1-99 \u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e17\u0e35\u0e48\u0e2a\u0e41\u0e01\u0e19) \u00b7 \u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e2a\u0e49\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 \u00b7 \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22 \u00b7 \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21 12-1 \u0e40\u0e14\u0e37\u0e2d\u0e19

**\u0e43\u0e0a\u0e49\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2b\u0e25\u0e32\u0e22\u0e1b\u0e35 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1b\u0e35\u0e40\u0e14\u0e35\u0e22\u0e27:** \u0e27\u0e31\u0e14\u0e40\u0e1b\u0e47\u0e19 CAGR/\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e08\u0e32\u0e01\u0e07\u0e1a\u0e23\u0e32\u0e22\u0e1b\u0e35\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e17\u0e48\u0e32\u0e17\u0e35\u0e48 Yahoo \u0e43\u0e2b\u0e49 (\u0e1b\u0e01\u0e15\u0e34 3-4 \u0e1b\u0e35)

**\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e2d\u0e07 3 \u0e21\u0e38\u0e21:** Piotroski F-Score (\u0e15\u0e23\u0e27\u0e08 9 \u0e02\u0e49\u0e2d\u0e27\u0e48\u0e32\u0e07\u0e1a\u0e41\u0e02\u0e47\u0e07\u0e41\u0e23\u0e07\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e2d\u0e48\u0e2d\u0e19\u0e25\u0e07) \u00b7 Rule of 40 \u00b7 \u0e01\u0e32\u0e23\u0e2d\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e21\u0e48 (dilution)

**\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c \u2260 \u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19** \u2014 \u0e43\u0e0a\u0e49\u0e04\u0e31\u0e14\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1b\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e40\u0e0a\u0e34\u0e07\u0e25\u0e36\u0e01\u0e15\u0e48\u0e2d (\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e08\u0e32\u0e01\u0e15\u0e32\u0e23\u0e32\u0e07\u0e41\u0e25\u0e49\u0e27\u0e40\u0e1b\u0e34\u0e14 "\u0e21\u0e38\u0e21\u0e21\u0e2d\u0e07\u0e40\u0e0a\u0e34\u0e07\u0e25\u0e36\u0e01" \u0e44\u0e14\u0e49\u0e17\u0e31\u0e19\u0e17\u0e35)
"""
        )

    c1, c2, c3 = st.columns([2, 1, 1])
    uni_label = c1.selectbox("\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e08\u0e30\u0e2a\u0e41\u0e01\u0e19", ["Nasdaq 100", "S&P 500", "\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e14\u0e31\u0e0a\u0e19\u0e35", "Watchlist \u0e02\u0e2d\u0e07\u0e09\u0e31\u0e19"], index=2, key="sc_uni")
    limit = c2.number_input("\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e15\u0e48\u0e2d\u0e23\u0e2d\u0e1a", min_value=10, max_value=600, value=600, step=10, key="sc_lim",
                            help="\u0e14\u0e36\u0e07\u0e07\u0e1a\u0e2b\u0e38\u0e49\u0e19\u0e25\u0e30\u0e2b\u0e25\u0e32\u0e22\u0e04\u0e33\u0e02\u0e2d \u0e16\u0e49\u0e32\u0e40\u0e22\u0e2d\u0e30\u0e08\u0e30\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32\u0e19\u0e32\u0e19 \u0e14\u0e36\u0e07\u0e17\u0e35\u0e25\u0e30\u0e0a\u0e38\u0e14\u0e44\u0e14\u0e49 \u0e07\u0e1a\u0e40\u0e01\u0e47\u0e1a\u0e41\u0e04\u0e0a\u0e43\u0e19\u0e44\u0e1f\u0e25\u0e4c \u0e04\u0e23\u0e31\u0e49\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e14\u0e36\u0e07\u0e0b\u0e49\u0e33")
    discount = c3.slider("\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e04\u0e34\u0e14\u0e25\u0e14 DCF (%)", 7, 14, 10, key="sc_disc") / 100.0

    if uni_label == "Watchlist \u0e02\u0e2d\u0e07\u0e09\u0e31\u0e19":
        try:
            import watchlist as _w
            syms = _w.get()
        except Exception:
            syms = []
    else:
        syms = universe({"Nasdaq 100": "ndx", "S&P 500": "sp500"}.get(uni_label, "both"))
    syms = list(dict.fromkeys(syms))[: int(limit)]
    cache = _load_cache()
    now = time.time()
    fresh = [s for s in syms if s in cache and now - cache[s].get("t", 0) <= CACHE_TTL]
    need = [s for s in syms if s not in fresh]
    st.caption("\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d %d \u0e15\u0e31\u0e27 \u00b7 \u0e21\u0e35\u0e07\u0e1a\u0e43\u0e19\u0e41\u0e04\u0e0a\u0e41\u0e25\u0e49\u0e27 %d \u0e15\u0e31\u0e27 \u00b7 \u0e15\u0e49\u0e2d\u0e07\u0e14\u0e36\u0e07\u0e40\u0e1e\u0e34\u0e48\u0e21 %d \u0e15\u0e31\u0e27" % (len(syms), len(fresh), len(need)))
    if len(need) > 150:
        st.caption("\u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e17\u0e35\u0e48\u0e14\u0e36\u0e07\u0e2b\u0e25\u0e32\u0e22\u0e23\u0e49\u0e2d\u0e22\u0e15\u0e31\u0e27\u0e2d\u0e32\u0e08\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32\u0e2b\u0e25\u0e32\u0e22\u0e19\u0e32\u0e17\u0e35 \u2014 \u0e2b\u0e22\u0e38\u0e14\u0e01\u0e25\u0e32\u0e07\u0e17\u0e32\u0e07\u0e44\u0e14\u0e49 \u0e02\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e14\u0e36\u0e07\u0e41\u0e25\u0e49\u0e27\u0e40\u0e01\u0e47\u0e1a\u0e44\u0e27\u0e49\u0e43\u0e0a\u0e49\u0e15\u0e48\u0e2d (\u0e2b\u0e23\u0e37\u0e2d\u0e25\u0e14\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e15\u0e48\u0e2d\u0e23\u0e2d\u0e1a\u0e25\u0e07\u0e01\u0e48\u0e2d\u0e19\u0e01\u0e47\u0e44\u0e14\u0e49)")

    if st.button("\u2b07\ufe0f \u0e14\u0e36\u0e07\u0e07\u0e1a%s (\u0e40\u0e01\u0e47\u0e1a\u0e41\u0e04\u0e0a\u0e44\u0e27\u0e49\u0e43\u0e0a\u0e49\u0e0b\u0e49\u0e33)" % (" %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35" % len(need) if need else " (\u0e04\u0e23\u0e1a\u0e41\u0e25\u0e49\u0e27 \u2014 \u0e01\u0e14\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e2d\u0e31\u0e1b\u0e40\u0e14\u0e15\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e17\u0e35\u0e48\u0e2b\u0e21\u0e14\u0e2d\u0e32\u0e22\u0e38)"),
                 key="sc_fetch", disabled=not syms):
        bar = st.progress(0.0, text="\u0e01\u0e33\u0e25\u0e31\u0e07\u0e40\u0e23\u0e34\u0e48\u0e21 ...")
        t0 = time.time()

        def prog(d, n, s):
            bar.progress(d / n, text="\u0e14\u0e36\u0e07\u0e07\u0e1a %d/%d \u00b7 %s \u00b7 \u0e1c\u0e48\u0e32\u0e19\u0e44\u0e1b %.0f \u0e27\u0e34\u0e19\u0e32\u0e17\u0e35" % (d, n, s, time.time() - t0))
        _, n_do, fail = fetch_many(syms, progress=prog)
        bar.empty()
        st.success("\u0e40\u0e2a\u0e23\u0e47\u0e08 \u2014 \u0e14\u0e36\u0e07\u0e43\u0e2b\u0e21\u0e48 %d \u0e15\u0e31\u0e27%s" % (n_do, (" \u00b7 \u0e14\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 %d \u0e15\u0e31\u0e27 (\u0e40\u0e0a\u0e48\u0e19 %s)" % (len(fail), ", ".join(fail[:6]))) if fail else ""))
        cache = _load_cache()

    have = [s for s in syms if s in cache and cache[s].get("raw")]
    if not have:
        st.info("\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21\u0e19\u0e35\u0e49 \u2014 \u0e01\u0e14\u0e1b\u0e38\u0e48\u0e21\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e14\u0e36\u0e07 (\u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e2d\u0e32\u0e08\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32\u0e2a\u0e31\u0e01\u0e1e\u0e31\u0e01)")
        return

    _init_state()
    st.radio("\u0e0a\u0e38\u0e14\u0e40\u0e01\u0e13\u0e11\u0e4c", list(PRESETS.keys()), key="sc_preset", horizontal=True, on_change=_apply_preset,
             help="\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e0a\u0e38\u0e14\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08\u0e23\u0e39\u0e1b \u0e41\u0e25\u0e49\u0e27\u0e1b\u0e23\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e15\u0e48\u0e2d\u0e44\u0e14\u0e49\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07")
    st.caption(PRESETS.get(st.session_state.get("sc_preset"), PRESETS[DEFAULT_PRESET])["note"])
    with st.expander("\u2699\ufe0f \u0e1b\u0e23\u0e31\u0e1a\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e40\u0e2d\u0e07", expanded=False):
        st.caption("\u0e1b\u0e23\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e17\u0e32\u0e07\u0e0b\u0e49\u0e32\u0e22 \u00b7 \u0e04\u0e33\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22\u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e32\u0e07\u0e02\u0e27\u0e32\u0e02\u0e2d\u0e07\u0e0a\u0e48\u0e2d\u0e07\u0e19\u0e31\u0e49\u0e19")
        st.markdown("##### \u0e02\u0e31\u0e49\u0e19 1 \u2014 \u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e + \u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15: \u0e15\u0e49\u0e2d\u0e07\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e35\u0e48\u0e02\u0e49\u0e2d\u0e08\u0e32\u0e01 7 (\u0e1c\u0e48\u0e32\u0e19/\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e0a\u0e31\u0e14\u0e40\u0e08\u0e19)")
        th = {}
        th["rev"] = _crit_row(lambda c: c.number_input("\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15 \u2265 (%)", 0.0, 100.0, step=1.0, key="th_rev"),
                              "**\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e42\u0e15 \u2265 X%** = \u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e1b\u0e35 (\u0e41\u0e1a\u0e1a\u0e17\u0e1a\u0e15\u0e49\u0e19 \u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e15\u0e32\u0e21\u0e07\u0e1a\u0e23\u0e32\u0e22\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e21\u0e35 3-4 \u0e1b\u0e35) \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e16\u0e49\u0e32\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e44\u0e21\u0e48\u0e42\u0e15 \u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e42\u0e15\u0e21\u0e31\u0e01\u0e21\u0e32\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e25\u0e14\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19 \u0e0b\u0e36\u0e48\u0e07\u0e17\u0e33\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e19\u0e32\u0e19")
        th["gp"] = _crit_row(lambda c: c.number_input("\u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e42\u0e15 \u2265 (%)", 0.0, 100.0, step=1.0, key="th_gp"),
                             "**\u0e01\u0e33\u0e44\u0e23\u0e02\u0e31\u0e49\u0e19\u0e15\u0e49\u0e19\u0e42\u0e15 \u2265 X%** = \u0e01\u0e33\u0e44\u0e23\u0e2b\u0e25\u0e31\u0e07\u0e2b\u0e31\u0e01\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e1b\u0e35 \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e16\u0e49\u0e32\u0e42\u0e15\u0e15\u0e32\u0e21\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22 \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e02\u0e32\u0e22\u0e44\u0e14\u0e49\u0e23\u0e32\u0e04\u0e32\u0e14\u0e35 \u0e21\u0e35\u0e2d\u0e33\u0e19\u0e32\u0e08\u0e15\u0e31\u0e49\u0e07\u0e23\u0e32\u0e04\u0e32 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e25\u0e14\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e31\u0e19\u0e22\u0e2d\u0e14")
        th["ni"] = _crit_row(lambda c: c.number_input("\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15 \u2265 (%)", 0.0, 100.0, step=1.0, key="th_ni"),
                             "**\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34\u0e42\u0e15 \u2265 X%** = \u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e16\u0e36\u0e07\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e42\u0e15\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e1b\u0e35 \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e14\u0e39\u0e27\u0e48\u0e32\u0e01\u0e32\u0e23\u0e42\u0e15\u0e41\u0e1b\u0e25\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e01\u0e33\u0e44\u0e23\u0e08\u0e23\u0e34\u0e07\u0e44\u0e2b\u0e21 (\u0e15\u0e31\u0e49\u0e07\u0e44\u0e27\u0e49\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e2d\u0e22\u0e32\u0e01\u0e44\u0e14\u0e49\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e17\u0e35\u0e48\u0e01\u0e33\u0e44\u0e23\u0e42\u0e15\u0e40\u0e23\u0e47\u0e27\u0e01\u0e27\u0e48\u0e32\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22)")
        th["nm"] = _crit_row(lambda c: c.number_input("\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 \u2265 (%)", 0.0, 100.0, step=1.0, key="th_nm"),
                             "**\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e01\u0e33\u0e44\u0e23\u0e2a\u0e38\u0e17\u0e18\u0e34 \u2265 X%** = \u0e02\u0e32\u0e22\u0e02\u0e2d\u0e07 100 \u0e1a\u0e32\u0e17 \u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e01\u0e33\u0e44\u0e23\u0e01\u0e35\u0e48\u0e1a\u0e32\u0e17 (\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 3 \u0e1b\u0e35) \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e17\u0e35\u0e48\u0e40\u0e01\u0e48\u0e07\u0e08\u0e23\u0e34\u0e07\u0e21\u0e31\u0e01\u0e40\u0e01\u0e47\u0e1a\u0e01\u0e33\u0e44\u0e23\u0e44\u0e14\u0e49\u0e2a\u0e39\u0e07 \u0e41\u0e15\u0e48\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e04\u0e49\u0e32\u0e1b\u0e25\u0e35\u0e01/\u0e02\u0e19\u0e2a\u0e48\u0e07\u0e1b\u0e01\u0e15\u0e34\u0e21\u0e35\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e19\u0e35\u0e49 \u0e16\u0e49\u0e32\u0e2d\u0e22\u0e32\u0e01\u0e43\u0e2b\u0e49\u0e15\u0e34\u0e14\u0e21\u0e32\u0e01\u0e02\u0e36\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e0a\u0e38\u0e14 \"\u0e1c\u0e48\u0e2d\u0e19\"")
        th["roic"] = _crit_row(lambda c: c.number_input("ROIC \u2265 (%)", 0.0, 100.0, step=1.0, key="th_roic"),
                               "**ROIC \u2265 X%** = \u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e15\u0e48\u0e2d\u0e40\u0e07\u0e34\u0e19\u0e25\u0e07\u0e17\u0e38\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17 (\u0e17\u0e31\u0e49\u0e07\u0e40\u0e07\u0e34\u0e19\u0e01\u0e39\u0e49\u0e41\u0e25\u0e30\u0e40\u0e07\u0e34\u0e19\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19) \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 3 \u0e1b\u0e35 \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e1a\u0e2d\u0e01\u0e27\u0e48\u0e32\u0e40\u0e2d\u0e32\u0e40\u0e07\u0e34\u0e19\u0e44\u0e1b\u0e25\u0e07\u0e17\u0e38\u0e19\u0e41\u0e25\u0e49\u0e27\u0e04\u0e38\u0e49\u0e21\u0e04\u0e48\u0e32\u0e44\u0e2b\u0e21 15% \u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e16\u0e37\u0e2d\u0e27\u0e48\u0e32\u0e40\u0e01\u0e48\u0e07")
        th["de"] = _crit_row(lambda c: c.number_input("\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 D/E \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 (\u0e40\u0e17\u0e48\u0e32)", 0.1, 5.0, step=0.1, key="th_de",
                                                      help="\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e1e\u0e14\u0e32\u0e19\u0e10\u0e32\u0e19: \u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04/\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e2f \u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a 2 \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e04\u0e48\u0e32\u0e19\u0e35\u0e49 \u00b7 \u0e2a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23/\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21 1.5 \u0e40\u0e17\u0e48\u0e32 \u00b7 \u0e18\u0e19\u0e32\u0e04\u0e32\u0e23/\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e19\u0e35\u0e49"),
                             "**\u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e2d\u0e17\u0e38\u0e19 D/E \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 X \u0e40\u0e17\u0e48\u0e32** = \u0e2b\u0e19\u0e35\u0e49\u0e2a\u0e34\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e2a\u0e48\u0e27\u0e19\u0e02\u0e2d\u0e07\u0e1c\u0e39\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19 \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e2b\u0e19\u0e35\u0e49\u0e15\u0e48\u0e33 = \u0e23\u0e31\u0e1a\u0e21\u0e37\u0e2d\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e41\u0e22\u0e48\u0e44\u0e14\u0e49 (\u0e18\u0e19\u0e32\u0e04\u0e32\u0e23/\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e02\u0e49\u0e2d\u0e19\u0e35\u0e49 \u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04/\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e2f \u0e1c\u0e48\u0e2d\u0e19\u0e43\u0e2b\u0e49 2 \u0e40\u0e17\u0e48\u0e32 \u2014 \u0e14\u0e39\u0e44\u0e2d\u0e04\u0e2d\u0e19 ? \u0e17\u0e35\u0e48\u0e0a\u0e48\u0e2d\u0e07)")
        l, r = st.columns([1, 3], vertical_alignment="center")
        l.markdown("*(\u0e44\u0e21\u0e48\u0e21\u0e35\u0e0a\u0e48\u0e2d\u0e07\u0e1b\u0e23\u0e31\u0e1a)*")
        r.markdown("**FCF \u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07** = \u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e2d\u0e34\u0e2a\u0e23\u0e30\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01\u0e17\u0e38\u0e01\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u00b7 *\u0e21\u0e35\u0e44\u0e27\u0e49\u0e17\u0e33\u0e44\u0e21:* \u0e01\u0e33\u0e44\u0e23\u0e1a\u0e19\u0e01\u0e23\u0e30\u0e14\u0e32\u0e29\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e08\u0e23\u0e34\u0e07\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a")
        st.markdown("##### \u0e02\u0e31\u0e49\u0e19 2 \u2014 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e1e\u0e07\u0e44\u0e1b\u0e44\u0e2b\u0e21: \u0e40\u0e1e\u0e14\u0e32\u0e19\u0e02\u0e2d\u0e07\u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e2a\u0e32 V (\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e31\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e34\u0e49\u0e07 \u0e22\u0e34\u0e48\u0e07\u0e41\u0e1e\u0e07\u0e01\u0e27\u0e48\u0e32\u0e40\u0e1e\u0e14\u0e32\u0e19 \u0e04\u0e30\u0e41\u0e19\u0e19\u0e22\u0e34\u0e48\u0e07\u0e25\u0e14)")
        th["pe"] = _crit_row(lambda c: c.number_input("P/E \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 (\u0e40\u0e17\u0e48\u0e32)", 5.0, 100.0, DEFAULT_TH["pe"], 1.0, key="th_pe"),
                             "**P/E \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 X** = \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19 \u00f7 \u0e01\u0e33\u0e44\u0e23\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 (\u0e01\u0e35\u0e48\u0e1b\u0e35\u0e17\u0e35\u0e48\u0e01\u0e33\u0e44\u0e23\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19\u0e08\u0e30\u0e04\u0e37\u0e19\u0e17\u0e38\u0e19) \u00b7 35 = \u0e22\u0e2d\u0e21\u0e08\u0e48\u0e32\u0e22\u0e41\u0e1e\u0e07\u0e43\u0e2b\u0e49\u0e2b\u0e38\u0e49\u0e19\u0e42\u0e15\u0e40\u0e23\u0e47\u0e27")
        th["fpe"] = _crit_row(lambda c: c.number_input("Forward P/E \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 (\u0e40\u0e17\u0e48\u0e32)", 5.0, 100.0, DEFAULT_TH["fpe"], 1.0, key="th_fpe"),
                              "**Forward P/E \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 X** = \u0e23\u0e32\u0e04\u0e32 \u00f7 \u0e01\u0e33\u0e44\u0e23\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e19\u0e31\u0e01\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e04\u0e32\u0e14\u0e1b\u0e35\u0e2b\u0e19\u0e49\u0e32 \u00b7 \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 P/E \u0e1b\u0e01\u0e15\u0e34 = \u0e15\u0e25\u0e32\u0e14\u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e08\u0e30\u0e42\u0e15")
        th["peg"] = _crit_row(lambda c: c.number_input("PEG \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19", 0.3, 5.0, DEFAULT_TH["peg"], 0.1, key="th_peg"),
                              "**PEG \u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 X** = P/E \u00f7 \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e42\u0e15\u0e02\u0e2d\u0e07\u0e01\u0e33\u0e44\u0e23 (\u0e1b\u0e23\u0e31\u0e1a P/E \u0e15\u0e32\u0e21\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15) \u00b7 \u0e23\u0e32\u0e27 1 = \u0e2a\u0e21\u0e40\u0e2b\u0e15\u0e38\u0e2a\u0e21\u0e1c\u0e25\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e42\u0e15, \u0e40\u0e01\u0e34\u0e19 2 = \u0e41\u0e1e\u0e07")
        st.markdown("---")
        st.markdown(_CRIT_CAVEAT)

    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e04\u0e33\u0e19\u0e27\u0e13\u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32 (\u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e2d\u0e32\u0e08\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32)..."):
        moms = momentum_batch(tuple(have))
    rows, full = [], {}
    for s in have:
        try:
            ev = evaluate(cache[s]["raw"], th, moms.get(s), discount)
        except Exception:
            continue
        ev["sym"] = s
        full[s] = ev
        rows.append({"\u0e2b\u0e38\u0e49\u0e19": s, "\u0e0a\u0e37\u0e48\u0e2d": (ev["name"] or "")[:26], "\u0e01\u0e25\u0e38\u0e48\u0e21": ev["sector"], "\u0e1c\u0e48\u0e32\u0e19 7 \u0e40\u0e01\u0e13\u0e11\u0e4c": ev["passed"], "\u0e40\u0e2a\u0e32 Q": ev["q_score"], "\u0e40\u0e2a\u0e32 G": ev["g_score"],
                     "\u0e40\u0e2a\u0e32 V": ev["v_score"], "\u0e40\u0e2a\u0e32 M": ev["m_score"], "\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e35\u0e48\u0e40\u0e2a\u0e32": ev["pillars_ok"], "\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21": ev["total"], "F-Score": ev["fscore"],
                     "RS": (ev["mom"] or {}).get("rs"), "Fwd P/E": ev["fpe"], "PEG": ev["peg"], "MoS %": ev["mos"]})
    if not rows:
        st.warning("\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08\u0e2a\u0e31\u0e01\u0e15\u0e31\u0e27")
        return
    df = pd.DataFrame(rows)

    f1, f2, f3 = st.columns(3)
    min_pass = f1.slider("\u0e1c\u0e48\u0e32\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e35\u0e48\u0e40\u0e01\u0e13\u0e11\u0e4c (\u0e08\u0e32\u0e01 7)", 0, 7, key="sc_minpass")
    min_pill = f2.slider("\u0e1c\u0e48\u0e32\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e35\u0e48\u0e40\u0e2a\u0e32 (\u0e08\u0e32\u0e01 4)", 0, 4, 2, key="sc_minpill")
    sort_by = f3.selectbox("\u0e40\u0e23\u0e35\u0e22\u0e07\u0e15\u0e32\u0e21", ["\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21", "\u0e1c\u0e48\u0e32\u0e19 7 \u0e40\u0e01\u0e13\u0e11\u0e4c", "\u0e40\u0e2a\u0e32 Q", "\u0e40\u0e2a\u0e32 G", "\u0e40\u0e2a\u0e32 V", "\u0e40\u0e2a\u0e32 M", "RS"], key="sc_sort")
    view = df[(df["\u0e1c\u0e48\u0e32\u0e19 7 \u0e40\u0e01\u0e13\u0e11\u0e4c"] >= min_pass) & (df["\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e35\u0e48\u0e40\u0e2a\u0e32"] >= min_pill)].sort_values(sort_by, ascending=False, na_position="last").reset_index(drop=True)
    st.markdown("**\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07 %d \u0e08\u0e32\u0e01 %d \u0e15\u0e31\u0e27**" % (len(view), len(df)))
    pb = lambda label: st.column_config.ProgressColumn(label, min_value=0, max_value=100, format="%d")
    _show_df(view, hide_index=True, column_config={
        "\u0e1c\u0e48\u0e32\u0e19 7 \u0e40\u0e01\u0e13\u0e11\u0e4c": st.column_config.NumberColumn("\u0e1c\u0e48\u0e32\u0e19 7 \u0e40\u0e01\u0e13\u0e11\u0e4c", format="%d / 7"), "\u0e40\u0e2a\u0e32 Q": pb("\u0e40\u0e2a\u0e32 Q \u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e"), "\u0e40\u0e2a\u0e32 G": pb("\u0e40\u0e2a\u0e32 G \u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15"), "\u0e40\u0e2a\u0e32 V": pb("\u0e40\u0e2a\u0e32 V \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32"),
        "\u0e40\u0e2a\u0e32 M": pb("\u0e40\u0e2a\u0e32 M \u0e42\u0e21\u0e40\u0e21\u0e19\u0e15\u0e31\u0e21"), "\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21": pb("\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21"), "F-Score": st.column_config.NumberColumn("F-Score", format="%d / 9"),
        "Fwd P/E": st.column_config.NumberColumn("Fwd P/E", format="%.1f"), "PEG": st.column_config.NumberColumn("PEG", format="%.2f"),
        "MoS %": st.column_config.NumberColumn("MoS %", format="%+.0f")})
    st.caption("\u0e40\u0e2a\u0e32\u0e25\u0e30 0-100 \u00b7 \u0e16\u0e37\u0e2d\u0e27\u0e48\u0e32 \"\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e2a\u0e32\" \u0e40\u0e21\u0e37\u0e48\u0e2d \u2265 60 \u00b7 MoS % = \u0e2a\u0e48\u0e27\u0e19\u0e40\u0e1c\u0e37\u0e48\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22\u0e40\u0e17\u0e35\u0e22\u0e1a DCF \u0e41\u0e1a\u0e1a\u0e07\u0e48\u0e32\u0e22 (\u0e1a\u0e27\u0e01 = \u0e23\u0e32\u0e04\u0e32\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19) \u00b7 \u0e04\u0e48\u0e32\u0e27\u0e48\u0e32\u0e07 = \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d")
    st.download_button("\u2b07\ufe0f \u0e14\u0e32\u0e27\u0e19\u0e4c\u0e42\u0e2b\u0e25\u0e14\u0e1c\u0e25 (CSV)", view.to_csv(index=False).encode("utf-8-sig"), file_name="screener_result.csv", mime="text/csv")

    pick_pool = list(view["\u0e2b\u0e38\u0e49\u0e19"]) or list(df["\u0e2b\u0e38\u0e49\u0e19"])
    sel = st.selectbox("\u0e14\u0e39\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19", pick_pool, key="sc_pick")
    if sel in full:
        ev = full[sel]
        st.markdown('<div class="section-label">\u25c6 %s \u2014 %s</div>' % (_e(sel), _e(ev["name"] or "")), unsafe_allow_html=True)
        _detail(sel, ev)
        try:                                         # \u0e43\u0e2b\u0e49\u0e2b\u0e19\u0e49\u0e32 DEEP INSIGHT \u0e40\u0e1b\u0e34\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49\u0e23\u0e2d\u0e44\u0e27\u0e49\u0e40\u0e25\u0e22 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e43\u0e2b\u0e21\u0e48
            for k_ in ("ins_ticker", "ins_sym", "_sb_ticker"):
                st.session_state[k_] = sel
        except Exception:
            pass
        st.info("\u0e2d\u0e22\u0e32\u0e01\u0e14\u0e39\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e07\u0e48\u0e32\u0e22 \u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32 23 \u0e2b\u0e25\u0e31\u0e01\u0e01\u0e32\u0e23 \u0e41\u0e25\u0e30\u0e42\u0e0b\u0e19\u0e23\u0e32\u0e04\u0e32\u0e02\u0e2d\u0e07 %s? \u0e44\u0e1b\u0e17\u0e35\u0e48\u0e40\u0e21\u0e19\u0e39 **DEEP INSIGHT \u00b7 \u0e21\u0e38\u0e21\u0e21\u0e2d\u0e07\u0e40\u0e0a\u0e34\u0e07\u0e25\u0e36\u0e01** \u0e17\u0e32\u0e07\u0e0b\u0e49\u0e32\u0e22 (\u0e43\u0e2a\u0e48\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19\u0e19\u0e35\u0e49\u0e23\u0e2d\u0e44\u0e27\u0e49\u0e43\u0e2b\u0e49\u0e41\u0e25\u0e49\u0e27)" % sel)
    st.caption("\u26a0\ufe0f \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo Finance \u0e2d\u0e32\u0e08\u0e02\u0e32\u0e14/\u0e1c\u0e34\u0e14/\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c \u00b7 DCF \u0e41\u0e25\u0e30\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e15\u0e48\u0e32\u0e07\u0e46 \u0e40\u0e1b\u0e47\u0e19\u0e01\u0e0e\u0e2b\u0e31\u0e27\u0e41\u0e21\u0e48\u0e21\u0e37\u0e2d \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e08\u0e23\u0e34\u0e07 \u00b7 \u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e44\u0e21\u0e48\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19 \u00b7 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e0b\u0e37\u0e49\u0e2d-\u0e02\u0e32\u0e22")