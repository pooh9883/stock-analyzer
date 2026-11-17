# -*- coding: utf-8 -*-
"""market_brief.py - \u0e2a\u0e23\u0e38\u0e1b\u0e15\u0e25\u0e32\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (\u0e2d\u0e48\u0e32\u0e19\u0e08\u0e1a\u0e43\u0e19 1 \u0e19\u0e32\u0e17\u0e35) \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e04\u0e19\u0e44\u0e21\u0e48\u0e16\u0e19\u0e31\u0e14\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02

\u0e42\u0e04\u0e23\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e23\u0e38\u0e1b\u0e15\u0e25\u0e32\u0e14\u0e17\u0e35\u0e48\u0e04\u0e19\u0e17\u0e31\u0e48\u0e27\u0e44\u0e1b\u0e0a\u0e2d\u0e1a\u0e2d\u0e48\u0e32\u0e19 \u0e41\u0e15\u0e48\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e14\u0e36\u0e07\u0e2a\u0e14\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34:
 1) \u0e15\u0e25\u0e32\u0e14\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49: S&P 500 / Nasdaq \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23 \u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e20\u0e32\u0e27\u0e30\u0e2d\u0e30\u0e44\u0e23 + \u0e15\u0e31\u0e27\u0e0a\u0e35\u0e49\u0e27\u0e31\u0e14\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27/\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19/\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22
 2) \u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e1e\u0e25\u0e31\u0e07\u0e02\u0e31\u0e1a\u0e40\u0e04\u0e25\u0e37\u0e48\u0e2d\u0e19: \u0e23\u0e32\u0e04\u0e32 \u0e23\u0e48\u0e27\u0e07\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 P/E \u0e41\u0e25\u0e30 Forward P/E
 3) \u0e17\u0e33\u0e44\u0e21\u0e16\u0e36\u0e07\u0e16\u0e39\u0e01\u0e40\u0e17\u0e02\u0e32\u0e22: \u0e08\u0e31\u0e14\u0e01\u0e25\u0e38\u0e48\u0e21\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27\u0e40\u0e1b\u0e47\u0e19\u0e18\u0e35\u0e21 + \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e15\u0e25\u0e32\u0e14\u0e17\u0e35\u0e48\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19
 4) \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e07

\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e2b\u0e15\u0e38: \u0e40\u0e1b\u0e47\u0e19\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e38\u0e1b\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e25\u0e30\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e02\u0e2d\u0e07\u0e04\u0e19
\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38 = \u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e08\u0e32\u0e01\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27 \u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e08\u0e23\u0e34\u0e07

\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49:
    import market_brief
    market_brief.render_market_brief()
"""
import datetime as _dt
import html as _html
import re as _re

import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

_UP, _DN, _MUT = "#19f5a5", "#ff4d6d", "#8d97b8"
_INDEX = [("^GSPC", "S&P 500"), ("^IXIC", "Nasdaq")]
_GAUGE = [("^VIX", "\u0e14\u0e31\u0e0a\u0e19\u0e35\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27 (VIX)"), ("CL=F", "\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19\u0e14\u0e34\u0e1a WTI"), ("^TNX", "\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23 10 \u0e1b\u0e35")]
_DEFAULT_STOCKS = "NVDA MU TSM AVGO MSFT AMD"
_CYCLICAL = {"MU", "SNDK", "WDC", "STX", "INTC", "TXN", "ON", "NXPI", "MCHP", "XOM", "CVX", "FCX"}

_CSS = (
    "<style>"
    ".mb{margin:10px 0;padding:14px 16px;border:1px solid rgba(125,134,166,.28);border-left:4px solid var(--ac,#00f0ff);"
    "background:linear-gradient(135deg,rgba(8,12,28,.7),rgba(8,12,28,.4))}"
    ".mb-big{font-size:17px;line-height:1.7;font-weight:700;color:#e8ecfa!important;-webkit-text-fill-color:#e8ecfa}"
    ".mb-big b{font-weight:900}"
    ".mb-h{margin:14px 0 6px;font-size:15px;font-weight:800;color:#fcee0a!important;-webkit-text-fill-color:#fcee0a}"
    ".mb-g{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0}"
    ".mb-box{flex:1 1 180px;padding:9px 12px;border:1px solid rgba(125,134,166,.28);background:rgba(0,240,255,.04)}"
    ".mb-box .t{font-size:12px;color:#8d97b8!important;-webkit-text-fill-color:#8d97b8}"
    ".mb-box .v{font-size:22px;font-weight:900;color:#e8ecfa!important;-webkit-text-fill-color:#e8ecfa}"
    ".mb-box .s{font-size:12px;font-weight:700}"
    ".mb-tag{display:inline-block;padding:1px 9px;margin-left:8px;font-size:12px;font-weight:800;border:1px solid}"
    ".mb-tbl{width:100%;border-collapse:collapse;font-size:13px}"
    ".mb-tbl th{text-align:right;color:#8d97b8!important;-webkit-text-fill-color:#8d97b8;font-weight:600;padding:4px 8px;border-bottom:1px solid rgba(125,134,166,.3)}"
    ".mb-tbl td{text-align:right;padding:5px 8px;border-bottom:1px solid rgba(125,134,166,.15);color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2}"
    ".mb-tbl th:first-child,.mb-tbl td:first-child{text-align:left;font-weight:800}"
    ".mb-th{margin:10px 0 2px;font-size:14px;font-weight:800;color:#e8ecfa!important;-webkit-text-fill-color:#e8ecfa}"
    ".mb-ev{margin:2px 0 4px;font-size:12.5px;color:#7fdcff!important;-webkit-text-fill-color:#7fdcff}"
    ".mb-hl{margin:1px 0;font-size:13px;line-height:1.5}"
    ".mb-hl a{color:#7fdcff!important;-webkit-text-fill-color:#7fdcff;text-decoration:none}"
    ".mb-hl small{color:#8d97b8}"
    ".mb-me{margin:4px 0;font-size:13.5px;line-height:1.65;color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2}"
    ".mb-note{margin:8px 0 0;font-size:12px;line-height:1.6;color:#8d97b8!important;-webkit-text-fill-color:#8d97b8}"
    "div[data-testid=\"stCode\"] pre,div[data-testid=\"stCode\"] code{font-family:inherit!important;font-size:14px!important;line-height:1.8!important;white-space:pre-wrap!important}"
    "div[data-testid=\"stVerticalBlockBorderWrapper\"]{border-color:rgba(0,240,255,.4)!important;background:rgba(8,12,28,.55);padding:6px 4px}"
    "</style>"
)

# \u0e18\u0e35\u0e21\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38: (\u0e23\u0e2b\u0e31\u0e2a, \u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e17\u0e22, regex \u0e02\u0e2d\u0e07\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e20\u0e32\u0e29\u0e32\u0e2d\u0e31\u0e07\u0e01\u0e24\u0e29, \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 "\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e07")
_THEMES = [
    ("rates", "\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22 \xb7 \u0e40\u0e07\u0e34\u0e19\u0e40\u0e1f\u0e49\u0e2d \xb7 \u0e40\u0e1f\u0e14",
     r"\b(fed|fomc|powell|rate (hike|cut)s?|interest rates?|inflation|cpi|pce|treasury yields?|bond yields?|10-year)\b",
     "\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e2a\u0e39\u0e07\u0e19\u0e32\u0e19\u0e02\u0e36\u0e49\u0e19 = \u0e04\u0e48\u0e32\u0e1c\u0e48\u0e2d\u0e19\u0e1a\u0e49\u0e32\u0e19 \u0e1c\u0e48\u0e2d\u0e19\u0e23\u0e16 \u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e1a\u0e31\u0e15\u0e23\u0e40\u0e04\u0e23\u0e14\u0e34\u0e15 \u0e41\u0e25\u0e30\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e01\u0e39\u0e49\u0e02\u0e2d\u0e07\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e2a\u0e39\u0e07\u0e02\u0e36\u0e49\u0e19\u0e15\u0e32\u0e21"),
    ("oil", "\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19 \xb7 \u0e04\u0e27\u0e32\u0e21\u0e02\u0e31\u0e14\u0e41\u0e22\u0e49\u0e07\u0e42\u0e25\u0e01",
     r"\b(oil|crude|brent|wti|opec|iran|israel|hormuz|middle east|war|ukraine|russia|geopolitic\w*|energy prices?|gasoline)\b",
     "\u0e23\u0e32\u0e04\u0e32\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e04\u0e48\u0e32\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19 \u0e04\u0e48\u0e32\u0e44\u0e1f \u0e04\u0e48\u0e32\u0e02\u0e19\u0e2a\u0e48\u0e07 \u0e41\u0e25\u0e30\u0e23\u0e32\u0e04\u0e32\u0e02\u0e2d\u0e07\u0e43\u0e0a\u0e49\u0e17\u0e38\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07 = \u0e04\u0e48\u0e32\u0e04\u0e23\u0e2d\u0e07\u0e0a\u0e35\u0e1e\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13"),
    ("policy", "\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e2d\u0e07 \xb7 \u0e19\u0e42\u0e22\u0e1a\u0e32\u0e22 \xb7 \u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a",
     r"\b(election|midterms?|congress|senate|regulat\w*|tariffs?|trade war|white house|trump|export (controls?|curbs?|ban)|sanctions?|antitrust|shutdown)\b",
     "\u0e19\u0e42\u0e22\u0e1a\u0e32\u0e22\u0e41\u0e25\u0e30\u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a (\u0e40\u0e0a\u0e48\u0e19 \u0e20\u0e32\u0e29\u0e35 \u0e01\u0e32\u0e23\u0e04\u0e49\u0e32 AI) \u0e01\u0e33\u0e2b\u0e19\u0e14\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08 \u0e01\u0e32\u0e23\u0e08\u0e49\u0e32\u0e07\u0e07\u0e32\u0e19 \u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15\u0e02\u0e2d\u0e07\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27"),
    ("ai", "AI \xb7 \u0e0a\u0e34\u0e1b \xb7 \u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35",
     r"\b(ai|a\.i\.|artificial intelligence|nvidia|chip(s|makers?)?|semiconductors?|data ?centers?|tsmc|micron|bubble|openai|hyperscalers?)\b",
     "\u0e2b\u0e38\u0e49\u0e19 AI \u0e41\u0e25\u0e30\u0e0a\u0e34\u0e1b\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e23\u0e07\u0e02\u0e31\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e02\u0e2d\u0e07\u0e15\u0e25\u0e32\u0e14 \u0e16\u0e49\u0e32\u0e01\u0e25\u0e38\u0e48\u0e21\u0e19\u0e35\u0e49\u0e23\u0e48\u0e27\u0e07 \u0e14\u0e31\u0e0a\u0e19\u0e35\u0e41\u0e25\u0e30\u0e01\u0e2d\u0e07\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e01\u0e47\u0e23\u0e48\u0e27\u0e07\u0e15\u0e32\u0e21\u0e41\u0e21\u0e49\u0e04\u0e38\u0e13\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e0b\u0e37\u0e49\u0e2d\u0e15\u0e23\u0e07\u0e46"),
    ("earn", "\u0e1c\u0e25\u0e1b\u0e23\u0e30\u0e01\u0e2d\u0e1a\u0e01\u0e32\u0e23\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17",
     r"\b(earnings|guidance|profit warning|revenue miss|misses? estimates|beats? estimates|quarterly results)\b",
     "\u0e07\u0e1a\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e43\u0e2b\u0e0d\u0e48\u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01\u0e21\u0e32\u0e44\u0e21\u0e48\u0e14\u0e35\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e25\u0e14\u0e04\u0e27\u0e32\u0e21\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e31\u0e48\u0e19\u0e15\u0e48\u0e2d\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21"),
    ("econ", "\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08 \xb7 \u0e01\u0e32\u0e23\u0e08\u0e49\u0e32\u0e07\u0e07\u0e32\u0e19",
     r"\b(jobs report|payrolls?|unemployment|recession|gdp|layoffs?|consumer (spending|confidence)|slowdown|jobless)\b",
     "\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e0a\u0e30\u0e25\u0e2d\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u0e01\u0e32\u0e23\u0e08\u0e49\u0e32\u0e07\u0e07\u0e32\u0e19 \u0e41\u0e25\u0e30\u0e01\u0e33\u0e25\u0e31\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e2d\u0e07\u0e04\u0e23\u0e31\u0e27\u0e40\u0e23\u0e37\u0e2d\u0e19"),
    ("fx", "ค่าเงิน · ดอลลาร์",
     r"\b(dollar|dxy|yen|euro|currency|currencies|forex|devaluation)\b",
     "ดอลลาร์แข็ง = บาทมักอ่อนลง ของนำเข้าและค่าใช้จ่ายเป็นดอลลาร์แพงขึ้น แต่ผู้ส่งออกได้ประโยชน์ ส่วนดอลลาร์อ่อนก็กลับกัน"),
    ("china", "จีน · ไต้หวัน · การค้าโลก",
     r"\b(china|chinese|beijing|taiwan|hong kong|yuan|xi jinping)\b",
     "ความตึงเครียดหรือเศรษฐกิจจีนชะลอ กระทบห่วงโซ่อุปทาน ราคาสินค้า (ของใช้ อิเล็กทรอนิกส์) และหุ้นชิปที่พึ่งโรงงานในเอเชีย"),
    ("bank", "ธนาคาร · สินเชื่อ",
     r"\b(regional banks?|bank failures?|banking (sector|stocks|crisis)|private credit|credit (crunch|stress|spreads?)|loan losses|defaults?)\b",
     "ถ้าธนาคารและสินเชื่อตึงตัว การกู้บ้าน กู้ธุรกิจจะยากและแพงขึ้น และเศรษฐกิจอาจชะลอ"),
    ("crypto", "คริปโต",
     r"\b(bitcoin|crypto(currenc(y|ies))?|ethereum|stablecoins?)\b",
     "ถ้าถือคริปโตหรือกองทุนที่เกี่ยวข้อง มูลค่าจะแกว่งแรงตามอารมณ์ตลาด (มักแรงกว่าหุ้น)"),
    ("housing", "บ้าน · อสังหา",
     r"\b(housing|mortgage rates?|home sales|real estate|homebuilders?)\b",
     "อัตราจำนองสูง = ค่าผ่อนบ้านแพง คนซื้อบ้านลดลง กระทบทั้งผู้ซื้อและธุรกิจที่เกี่ยวข้อง"),
]
_THEME_RX = {k: _re.compile(rx, _re.I) for k, _n, rx, _m in _THEMES}
_THEME_NAME = {k: n for k, n, _rx, _m in _THEMES}
_THEME_ME = {k: m for k, _n, _rx, m in _THEMES}
# \u0e04\u0e33\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22 "\u0e40\u0e1e\u0e23\u0e32\u0e30\u0e2d\u0e30\u0e44\u0e23" \u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e18\u0e35\u0e21 \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e15\u0e32\u0e21\u0e04\u0e33\u0e17\u0e35\u0e48\u0e40\u0e08\u0e2d\u0e08\u0e23\u0e34\u0e07\u0e43\u0e19\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27 (\u0e44\u0e21\u0e48\u0e40\u0e08\u0e2d\u0e04\u0e33\u0e44\u0e2b\u0e19\u0e01\u0e47\u0e44\u0e21\u0e48\u0e40\u0e02\u0e35\u0e22\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e31\u0e49\u0e19)
_CLAUSES = {
    "policy": [
        (r"\b(election|midterms?)\b", "\u0e1c\u0e25\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e15\u0e31\u0e49\u0e07\u0e01\u0e25\u0e32\u0e07\u0e40\u0e17\u0e2d\u0e21 (Midterm) \u0e02\u0e2d\u0e07\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e2f \u0e17\u0e33\u0e43\u0e2b\u0e49\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07\u0e19\u0e42\u0e22\u0e1a\u0e32\u0e22\u0e43\u0e19\u0e2d\u0e19\u0e32\u0e04\u0e15\u0e44\u0e21\u0e48\u0e41\u0e19\u0e48\u0e19\u0e2d\u0e19 \u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e08\u0e36\u0e07\u0e25\u0e14\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19 \u0e08\u0e19\u0e01\u0e27\u0e48\u0e32\u0e08\u0e30\u0e40\u0e2b\u0e47\u0e19\u0e27\u0e48\u0e32\u0e23\u0e31\u0e10\u0e1a\u0e32\u0e25\u0e41\u0e25\u0e30\u0e2a\u0e20\u0e32\u0e08\u0e30\u0e40\u0e14\u0e34\u0e19\u0e44\u0e1b\u0e17\u0e32\u0e07\u0e44\u0e2b\u0e19"),
        (r"\b(regulat\w*|antitrust)\b", "\u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e40\u0e02\u0e49\u0e21\u0e07\u0e27\u0e14\u0e02\u0e36\u0e49\u0e19 \u0e42\u0e14\u0e22\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e01\u0e31\u0e1a AI \u0e41\u0e25\u0e30\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e43\u0e2b\u0e0d\u0e48 \u0e2d\u0e32\u0e08\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e42\u0e15\u0e0a\u0e49\u0e32\u0e25\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e21\u0e35\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e40\u0e1e\u0e34\u0e48\u0e21"),
        (r"\b(tariffs?|trade war)\b", "\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e20\u0e32\u0e29\u0e35\u0e19\u0e33\u0e40\u0e02\u0e49\u0e32\u0e41\u0e25\u0e30\u0e2a\u0e07\u0e04\u0e23\u0e32\u0e21\u0e01\u0e32\u0e23\u0e04\u0e49\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e19\u0e34\u0e48\u0e07 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e41\u0e25\u0e30\u0e23\u0e32\u0e04\u0e32\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e2d\u0e32\u0e08\u0e2a\u0e39\u0e07\u0e02\u0e36\u0e49\u0e19 \u0e01\u0e33\u0e44\u0e23\u0e08\u0e36\u0e07\u0e2d\u0e32\u0e08\u0e25\u0e14\u0e25\u0e07"),
        (r"\b(export (controls?|curbs?|ban)|sanctions?)\b", "\u0e21\u0e32\u0e15\u0e23\u0e01\u0e32\u0e23\u0e08\u0e33\u0e01\u0e31\u0e14\u0e01\u0e32\u0e23\u0e2a\u0e48\u0e07\u0e2d\u0e2d\u0e01\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e04\u0e27\u0e48\u0e33\u0e1a\u0e32\u0e15\u0e23\u0e2d\u0e32\u0e08\u0e15\u0e31\u0e14\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e0a\u0e34\u0e1b\u0e41\u0e25\u0e30\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e02\u0e49\u0e32\u0e21\u0e0a\u0e32\u0e15\u0e34\u0e1a\u0e32\u0e07\u0e2a\u0e48\u0e27\u0e19"),
        (r"\b(shutdown|congress|senate)\b", "\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e2d\u0e07\u0e43\u0e19\u0e2a\u0e20\u0e32\u0e17\u0e35\u0e48\u0e22\u0e31\u0e07\u0e15\u0e01\u0e25\u0e07\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 \u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e07\u0e1a\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19\u0e02\u0e2d\u0e07\u0e23\u0e31\u0e10\u0e1a\u0e32\u0e25\u0e2a\u0e30\u0e14\u0e38\u0e14"),
        (r"\b(trump|white house)\b", "\u0e17\u0e48\u0e32\u0e17\u0e35\u0e08\u0e32\u0e01\u0e17\u0e33\u0e40\u0e19\u0e35\u0e22\u0e1a\u0e02\u0e32\u0e27\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e44\u0e14\u0e49\u0e40\u0e23\u0e47\u0e27 \u0e17\u0e33\u0e43\u0e2b\u0e49\u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e27\u0e32\u0e07\u0e41\u0e1c\u0e19\u0e23\u0e30\u0e22\u0e30\u0e22\u0e32\u0e27\u0e22\u0e32\u0e01"),
    ],
    "ai": [
        (r"\bbubble\b", "\u0e21\u0e35\u0e04\u0e27\u0e32\u0e21\u0e01\u0e31\u0e07\u0e27\u0e25\u0e27\u0e48\u0e32\u0e2b\u0e38\u0e49\u0e19 AI \u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e40\u0e23\u0e47\u0e27\u0e40\u0e01\u0e34\u0e19\u0e01\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e08\u0e23\u0e34\u0e07 (\u0e1f\u0e2d\u0e07\u0e2a\u0e1a\u0e39\u0e48) \u0e1e\u0e2d\u0e21\u0e35\u0e02\u0e48\u0e32\u0e27\u0e23\u0e49\u0e32\u0e22 \u0e04\u0e19\u0e17\u0e35\u0e48\u0e01\u0e33\u0e44\u0e23\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e36\u0e07\u0e23\u0e35\u0e1a\u0e02\u0e32\u0e22\u0e17\u0e33\u0e01\u0e33\u0e44\u0e23"),
        (r"\b(slowdown|slows?|slowing)\b", "\u0e02\u0e48\u0e32\u0e27\u0e27\u0e48\u0e32\u0e01\u0e32\u0e23\u0e25\u0e07\u0e17\u0e38\u0e19\u0e14\u0e49\u0e32\u0e19 AI \u0e2d\u0e32\u0e08\u0e0a\u0e30\u0e25\u0e2d\u0e15\u0e31\u0e27 \u0e01\u0e23\u0e30\u0e17\u0e1a\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e0a\u0e34\u0e1b\u0e41\u0e25\u0e30 Data Center \u0e42\u0e14\u0e22\u0e15\u0e23\u0e07 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e02\u0e2d\u0e07\u0e1e\u0e27\u0e01\u0e40\u0e02\u0e32\u0e21\u0e32\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e17\u0e35\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e43\u0e2b\u0e0d\u0e48\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e2d\u0e07\u0e44\u0e1b\u0e2a\u0e23\u0e49\u0e32\u0e07 AI"),
        (r"\b(data ?centers?)\b", "\u0e04\u0e27\u0e32\u0e21\u0e44\u0e21\u0e48\u0e41\u0e19\u0e48\u0e19\u0e2d\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07 Data Center (\u0e40\u0e0a\u0e48\u0e19 \u0e01\u0e0e\u0e23\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e1a \u0e44\u0e1f\u0e1f\u0e49\u0e32 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19) \u0e17\u0e33\u0e43\u0e2b\u0e49\u0e22\u0e2d\u0e14\u0e2a\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e0a\u0e34\u0e1b\u0e41\u0e25\u0e30\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c\u0e2d\u0e32\u0e08\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e04\u0e32\u0e14"),
        (r"\b(spending|capex|hyperscalers?)\b", "\u0e15\u0e25\u0e32\u0e14\u0e08\u0e31\u0e1a\u0e15\u0e32\u0e27\u0e48\u0e32\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e22\u0e31\u0e01\u0e29\u0e4c\u0e43\u0e2b\u0e0d\u0e48\u0e08\u0e30\u0e17\u0e38\u0e48\u0e21\u0e40\u0e07\u0e34\u0e19\u0e25\u0e07\u0e17\u0e38\u0e19 AI \u0e15\u0e48\u0e2d\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e40\u0e07\u0e34\u0e19\u0e01\u0e49\u0e2d\u0e19\u0e19\u0e31\u0e49\u0e19\u0e04\u0e37\u0e2d\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e0a\u0e34\u0e1b"),
        (r"\b(nvidia|chip(s|makers?)?|semiconductors?|tsmc|micron)\b", "\u0e2b\u0e38\u0e49\u0e19\u0e0a\u0e34\u0e1b\u0e41\u0e25\u0e30 AI \u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e21\u0e32\u0e01\u0e41\u0e25\u0e30\u0e21\u0e35\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e2a\u0e39\u0e07\u0e43\u0e19\u0e14\u0e31\u0e0a\u0e19\u0e35 \u0e1e\u0e2d\u0e16\u0e39\u0e01\u0e40\u0e17\u0e02\u0e32\u0e22 Nasdaq \u0e08\u0e36\u0e07\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e01\u0e27\u0e48\u0e32\u0e15\u0e25\u0e32\u0e14\u0e42\u0e14\u0e22\u0e23\u0e27\u0e21"),
        (r"\b(ai|a\.i\.|artificial intelligence|openai)\b", "\u0e02\u0e48\u0e32\u0e27\u0e14\u0e49\u0e32\u0e19 AI \u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01\u0e21\u0e32\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e17\u0e1a\u0e17\u0e27\u0e19\u0e04\u0e27\u0e32\u0e21\u0e04\u0e32\u0e14\u0e2b\u0e27\u0e31\u0e07\u0e15\u0e48\u0e2d\u0e01\u0e25\u0e38\u0e48\u0e21\u0e19\u0e35\u0e49"),
    ],
    "rates": [
        (r"\b(rate hikes?|hike)\b", "\u0e22\u0e31\u0e07\u0e21\u0e35\u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e17\u0e35\u0e48\u0e40\u0e1f\u0e14\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e2d\u0e35\u0e01 \u0e0b\u0e36\u0e48\u0e07\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e40\u0e07\u0e34\u0e19\u0e01\u0e39\u0e49\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e2a\u0e39\u0e07\u0e02\u0e36\u0e49\u0e19\u0e41\u0e25\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15\u0e14\u0e39\u0e41\u0e1e\u0e07\u0e25\u0e07"),
        (r"\b(inflation|cpi|pce)\b", "\u0e40\u0e07\u0e34\u0e19\u0e40\u0e1f\u0e49\u0e2d\u0e22\u0e31\u0e07\u0e2a\u0e39\u0e07 \u0e40\u0e1f\u0e14\u0e08\u0e36\u0e07\u0e2d\u0e32\u0e08\u0e15\u0e49\u0e2d\u0e07\u0e04\u0e07\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e2a\u0e39\u0e07\u0e44\u0e27\u0e49\u0e19\u0e32\u0e19\u0e02\u0e36\u0e49\u0e19 \u0e0b\u0e36\u0e48\u0e07\u0e01\u0e14\u0e14\u0e31\u0e19\u0e2b\u0e38\u0e49\u0e19 \u0e42\u0e14\u0e22\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e17\u0e35\u0e48\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e02\u0e36\u0e49\u0e19\u0e01\u0e31\u0e1a\u0e01\u0e33\u0e44\u0e23\u0e43\u0e19\u0e2d\u0e19\u0e32\u0e04\u0e15"),
        (r"\b(rate cuts?)\b", "\u0e15\u0e25\u0e32\u0e14\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e41\u0e19\u0e48\u0e43\u0e08\u0e27\u0e48\u0e32\u0e40\u0e1f\u0e14\u0e08\u0e30\u0e25\u0e14\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e44\u0e23 \u0e16\u0e49\u0e32\u0e0a\u0e49\u0e32\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e2b\u0e27\u0e31\u0e07 \u0e2b\u0e38\u0e49\u0e19\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15\u0e08\u0e30\u0e16\u0e39\u0e01\u0e01\u0e14\u0e14\u0e31\u0e19"),
        (r"\b(fed|fomc|powell)\b", "\u0e17\u0e48\u0e32\u0e17\u0e35\u0e02\u0e2d\u0e07\u0e40\u0e1f\u0e14\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e0a\u0e31\u0e14 \u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e01\u0e25\u0e49\u0e32\u0e16\u0e37\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e2a\u0e39\u0e07"),
        (r"\b(treasury yields?|bond yields?|10-year)\b", "\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23\u0e17\u0e35\u0e48\u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e36\u0e49\u0e19\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23\u0e19\u0e48\u0e32\u0e16\u0e37\u0e2d\u0e02\u0e36\u0e49\u0e19 \u0e40\u0e07\u0e34\u0e19\u0e1a\u0e32\u0e07\u0e2a\u0e48\u0e27\u0e19\u0e08\u0e36\u0e07\u0e22\u0e49\u0e32\u0e22\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e2b\u0e38\u0e49\u0e19"),
    ],
    "oil": [
        (r"\b(iran|israel|hormuz|middle east)\b", "\u0e04\u0e27\u0e32\u0e21\u0e02\u0e31\u0e14\u0e41\u0e22\u0e49\u0e07\u0e43\u0e19\u0e15\u0e30\u0e27\u0e31\u0e19\u0e2d\u0e2d\u0e01\u0e01\u0e25\u0e32\u0e07 (\u0e40\u0e0a\u0e48\u0e19 \u0e01\u0e23\u0e13\u0e35\u0e2d\u0e34\u0e2b\u0e23\u0e48\u0e32\u0e19) \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e08\u0e1a \u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e01\u0e32\u0e23\u0e02\u0e19\u0e2a\u0e48\u0e07\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19\u0e41\u0e25\u0e30\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e42\u0e25\u0e01\u0e44\u0e21\u0e48\u0e21\u0e31\u0e48\u0e19\u0e04\u0e07"),
        (r"\b(ukraine|russia)\b", "\u0e2a\u0e07\u0e04\u0e23\u0e32\u0e21\u0e22\u0e39\u0e40\u0e04\u0e23\u0e19-\u0e23\u0e31\u0e2a\u0e40\u0e0b\u0e35\u0e22\u0e22\u0e31\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e15\u0e48\u0e2d\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19\u0e41\u0e25\u0e30\u0e2b\u0e48\u0e27\u0e07\u0e42\u0e0b\u0e48\u0e2d\u0e38\u0e1b\u0e17\u0e32\u0e19"),
        (r"\b(oil|crude|brent|wti|opec|energy prices?|gasoline)\b", "\u0e23\u0e32\u0e04\u0e32\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19 \u0e16\u0e49\u0e32\u0e41\u0e1e\u0e07\u0e02\u0e36\u0e49\u0e19 \u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e41\u0e25\u0e30\u0e04\u0e48\u0e32\u0e04\u0e23\u0e2d\u0e07\u0e0a\u0e35\u0e1e\u0e40\u0e1e\u0e34\u0e48\u0e21 \u0e40\u0e07\u0e34\u0e19\u0e40\u0e1f\u0e49\u0e2d\u0e2d\u0e32\u0e08\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32 \u0e41\u0e15\u0e48\u0e16\u0e49\u0e32\u0e16\u0e39\u0e01\u0e25\u0e07\u0e40\u0e23\u0e47\u0e27\u0e40\u0e1e\u0e23\u0e32\u0e30\u0e01\u0e25\u0e31\u0e27\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e0a\u0e30\u0e25\u0e2d \u0e01\u0e47\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e44\u0e21\u0e48\u0e14\u0e35\u0e40\u0e0a\u0e48\u0e19\u0e01\u0e31\u0e19"),
        (r"\b(war|geopolitic\w*)\b", "\u0e04\u0e27\u0e32\u0e21\u0e15\u0e36\u0e07\u0e40\u0e04\u0e23\u0e35\u0e22\u0e14\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e16\u0e37\u0e2d\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e21\u0e32\u0e01\u0e02\u0e36\u0e49\u0e19\u0e41\u0e25\u0e30\u0e02\u0e32\u0e22\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e25\u0e07"),
    ],
    "earn": [
        (r"\b(guidance|profit warning|revenue miss|misses? estimates)\b", "\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e1a\u0e32\u0e07\u0e41\u0e2b\u0e48\u0e07\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e1c\u0e25\u0e2b\u0e23\u0e37\u0e2d\u0e04\u0e32\u0e14\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e27\u0e31\u0e07 \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e08\u0e36\u0e07\u0e16\u0e39\u0e01\u0e1b\u0e23\u0e31\u0e1a\u0e25\u0e07\u0e15\u0e32\u0e21\u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e08\u0e30\u0e19\u0e49\u0e2d\u0e22\u0e25\u0e07"),
        (r"\b(earnings|quarterly results|beats? estimates)\b", "\u0e0a\u0e48\u0e27\u0e07\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e21\u0e31\u0e01\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e15\u0e25\u0e32\u0e14\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e08\u0e23\u0e34\u0e07\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e04\u0e32\u0e14\u0e44\u0e27\u0e49"),
    ],
    "econ": [
        (r"\brecession\b", "\u0e02\u0e48\u0e32\u0e27\u0e0a\u0e35\u0e49\u0e27\u0e48\u0e32\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e2d\u0e32\u0e08\u0e16\u0e14\u0e16\u0e2d\u0e22 \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e41\u0e25\u0e30\u0e01\u0e33\u0e44\u0e23\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e08\u0e36\u0e07\u0e21\u0e35\u0e41\u0e19\u0e27\u0e42\u0e19\u0e49\u0e21\u0e25\u0e14\u0e25\u0e07"),
        (r"\b(jobs report|payrolls?|unemployment|jobless)\b", "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e01\u0e32\u0e23\u0e08\u0e49\u0e32\u0e07\u0e07\u0e32\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01\u0e21\u0e32\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e15\u0e25\u0e32\u0e14\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e41\u0e25\u0e30\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e43\u0e2b\u0e21\u0e48"),
        (r"\blayoffs?\b", "\u0e01\u0e32\u0e23\u0e1b\u0e25\u0e14\u0e1e\u0e19\u0e31\u0e01\u0e07\u0e32\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e27\u0e48\u0e32\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e23\u0e34\u0e48\u0e21\u0e23\u0e30\u0e27\u0e31\u0e07\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e41\u0e25\u0e30\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22"),
        (r"\b(consumer (spending|confidence))\b", "\u0e1c\u0e39\u0e49\u0e1a\u0e23\u0e34\u0e42\u0e20\u0e04\u0e43\u0e0a\u0e49\u0e08\u0e48\u0e32\u0e22\u0e19\u0e49\u0e2d\u0e22\u0e25\u0e07 \u0e01\u0e23\u0e30\u0e17\u0e1a\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07"),
        (r"\b(gdp|slowdown)\b", "\u0e40\u0e28\u0e23\u0e29\u0e10\u0e01\u0e34\u0e08\u0e0a\u0e30\u0e25\u0e2d \u0e17\u0e33\u0e43\u0e2b\u0e49\u0e19\u0e31\u0e01\u0e25\u0e07\u0e17\u0e38\u0e19\u0e25\u0e14\u0e04\u0e27\u0e32\u0e21\u0e04\u0e32\u0e14\u0e2b\u0e27\u0e31\u0e07\u0e15\u0e48\u0e2d\u0e01\u0e33\u0e44\u0e23"),
    ],
    "fx": [
        (r"\b(yen)\b", "เงินเยนผันผวนแรง ทำให้นักลงทุนที่กู้เงินเยนมาลงทุนอาจต้องรีบปิดสถานะ จึงมีแรงขายในหลายตลาดพร้อมกันได้"),
        (r"\b(dollar|dxy)\b", "ดอลลาร์เปลี่ยนทิศแรง ทำให้เงินไหลเข้าออกสินทรัพย์ในสหรัฐ และกระทบรายได้ของบริษัทที่ขายต่างประเทศเมื่อแปลงกลับเป็นดอลลาร์"),
        (r"\b(euro|currency|currencies|forex|devaluation)\b", "ค่าเงินที่ผันผวนทำให้นักลงทุนระวังตัวและย้ายเงินไปสินทรัพย์ที่ปลอดภัยกว่า"),
    ],
    "china": [
        (r"\b(taiwan)\b", "ความกังวลเรื่องไต้หวัน ซึ่งเป็นแหล่งผลิตชิปสำคัญของโลก ทำให้หุ้นชิปถูกมองว่าเสี่ยงขึ้น"),
        (r"\b(china|chinese|beijing|xi jinping|yuan|hong kong)\b", "ข่าวจีน (เศรษฐกิจชะลอ หรือความสัมพันธ์กับสหรัฐ) กระทบยอดขายของบริษัทสหรัฐที่ขายในจีน และห่วงโซ่อุปทานของสินค้าหลายประเภท"),
    ],
    "bank": [
        (r"\b(regional banks?|bank failures?|banking (sector|stocks|crisis))\b", "ความกังวลเรื่องธนาคารและหนี้เสีย ทำให้นักลงทุนกลัวว่าสินเชื่อจะตึงตัวและเศรษฐกิจชะลอ"),
        (r"\b(private credit|credit (crunch|stress|spreads?)|loan losses|defaults?)\b", "ข่าวผิดนัดชำระหนี้หรือสินเชื่อตึงตัว ทำให้ตลาดกลัวว่าปัญหาหนี้จะลามไปที่อื่น"),
    ],
    "crypto": [
        (r"\b(bitcoin|crypto(currenc(y|ies))?|ethereum|stablecoins?)\b", "คริปโตมักแกว่งตามอารมณ์ตลาดเสี่ยง เมื่อนักลงทุนลดความเสี่ยงจะถูกขายก่อน"),
    ],
    "housing": [
        (r"\b(mortgage rates?)\b", "อัตราจำนองที่สูงทำให้ยอดซื้อบ้านลดลง กระทบหุ้นอสังหาและธุรกิจที่เกี่ยวข้อง"),
        (r"\b(housing|home sales|real estate|homebuilders?)\b", "ตลาดบ้านที่ชะลอเป็นสัญญาณว่าผู้บริโภครัดเข็มขัด และกระทบหุ้นที่เกี่ยวข้อง"),
    ],
}
_CLAUSE_RX = {k: [(_re.compile(rx, _re.I), t) for rx, t in v] for k, v in _CLAUSES.items()}
# \u0e43\u0e0a\u0e49\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e21\u0e35\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e15\u0e23\u0e07\u0e46 \u0e41\u0e15\u0e48\u0e21\u0e35\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e15\u0e25\u0e32\u0e14\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19
_WHY = {
    "rates": "\u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e41\u0e25\u0e30\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e2a\u0e39\u0e07 \u0e17\u0e33\u0e43\u0e2b\u0e49\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15\u0e16\u0e39\u0e01\u0e01\u0e14\u0e14\u0e31\u0e19 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e40\u0e07\u0e34\u0e19\u0e01\u0e39\u0e49\u0e41\u0e1e\u0e07\u0e02\u0e36\u0e49\u0e19\u0e41\u0e25\u0e30\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23\u0e19\u0e48\u0e32\u0e16\u0e37\u0e2d\u0e02\u0e36\u0e49\u0e19",
    "oil": "\u0e23\u0e32\u0e04\u0e32\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19\u0e17\u0e35\u0e48\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e15\u0e25\u0e32\u0e14\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e41\u0e25\u0e30\u0e40\u0e07\u0e34\u0e19\u0e40\u0e1f\u0e49\u0e2d\u0e44\u0e14\u0e49\u0e22\u0e32\u0e01 \u0e08\u0e36\u0e07\u0e23\u0e30\u0e27\u0e31\u0e07\u0e15\u0e31\u0e27\u0e21\u0e32\u0e01\u0e02\u0e36\u0e49\u0e19",
}


def _story(k, rs):
    """\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22\u0e1b\u0e23\u0e30\u0e40\u0e14\u0e47\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e20\u0e32\u0e29\u0e32\u0e04\u0e19\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25 '\u0e40\u0e1e\u0e23\u0e32\u0e30\u0e2d\u0e30\u0e44\u0e23' \u0e08\u0e32\u0e01\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e43\u0e19\u0e18\u0e35\u0e21\u0e19\u0e31\u0e49\u0e19 (\u0e44\u0e21\u0e48\u0e01\u0e4a\u0e2d\u0e1b\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e2d\u0e31\u0e07\u0e01\u0e24\u0e29) -> \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 \u0e2b\u0e23\u0e37\u0e2d '' \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25"""
    if not rs:
        return _WHY.get(k, "")
    txt = " | ".join(h["title"] for h in rs)
    found = []
    for rx, t in _CLAUSE_RX.get(k, []):
        n = len(rx.findall(txt))
        if n:
            found.append((n, t))
    found.sort(key=lambda x: -x[0])
    cl = [t for _n, t in found[:3]]
    srcs = []
    for h in rs:
        if h.get("source") and h["source"] not in srcs:
            srcs.append(h["source"])
    sr = (" (\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e08\u0e32\u0e01 %s)" % ", ".join(srcs[:3])) if srcs else ""
    if not cl:
        return "\u0e21\u0e35\u0e02\u0e48\u0e32\u0e27\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49\u0e08\u0e32\u0e01\u0e2b\u0e25\u0e32\u0e22\u0e2a\u0e33\u0e19\u0e31\u0e01%s %s" % (sr, _WHY.get(k, ""))
    out = "\u0e08\u0e32\u0e01\u0e02\u0e48\u0e32\u0e27\u0e0a\u0e48\u0e27\u0e07\u0e2a\u0e31\u0e1b\u0e14\u0e32\u0e2b\u0e4c\u0e19\u0e35\u0e49%s \u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e04\u0e37\u0e2d %s" % (sr, cl[0])
    if len(cl) > 1:
        out += " \u0e19\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e19\u0e35\u0e49 " + cl[1]
    if len(cl) > 2:
        out += " \u0e41\u0e25\u0e30" + cl[2]
    return out.strip()


_REBOUND = _re.compile(r"\b(rebound\w*|bounce\w*|rall(y|ies|ied)|recover\w*|snap\w* (back|\w+ losing streak)|stocks (rise|gain|climb|jump|advance|edge up))\b", _re.I)
_NAMES = {"NVDA": "Nvidia", "MU": "Micron", "TSM": "TSMC", "AVGO": "Broadcom", "MSFT": "Microsoft", "AMD": "AMD", "AAPL": "Apple", "GOOGL": "Alphabet (Google)",
          "GOOG": "Alphabet (Google)", "AMZN": "Amazon", "META": "Meta", "TSLA": "Tesla", "INTC": "Intel", "ORCL": "Oracle", "ASML": "ASML", "QCOM": "Qualcomm",
          "SNDK": "Sandisk", "NFLX": "Netflix", "CRM": "Salesforce", "PLTR": "Palantir"}
_ORD = ["\u0e41\u0e23\u0e01", "\u0e2a\u0e2d\u0e07", "\u0e2a\u0e32\u0e21", "\u0e2a\u0e35\u0e48"]
_QUERIES = ["stock market sell-off why when:7d", "Wall Street stocks fall when:7d", "Nasdaq S&P 500 stocks drop investors when:7d", "stock market today when:2d"]


def _e(x):
    return _html.escape(str(x), quote=True)


def _c(v):
    return _UP if v >= 0 else _DN


def _fmtp(v, d=1):
    return "%+.*f%%" % (d, v)


# ---------------------------------------------------------------
# \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25
# ---------------------------------------------------------------
@st.cache_data(ttl=600, show_spinner=False)
def _prices(symbols):
    """\u0e1b\u0e34\u0e14\u0e23\u0e32\u0e22\u0e27\u0e31\u0e19 1 \u0e1b\u0e35 \u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2a\u0e31\u0e0d\u0e25\u0e31\u0e01\u0e29\u0e13\u0e4c -> {sym: [close,...]} (\u0e40\u0e01\u0e47\u0e1a\u0e40\u0e1b\u0e47\u0e19 list \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e41\u0e04\u0e0a\u0e07\u0e48\u0e32\u0e22)"""
    syms = list(symbols)
    try:
        d = yf.download(" ".join(syms), period="1y", interval="1d", group_by="ticker", progress=False, auto_adjust=True, threads=True)
    except Exception:
        return {}
    out = {}
    for s in syms:
        try:
            c = (d[s]["Close"] if len(syms) > 1 else d["Close"]).dropna()
            if len(c) >= 10:
                out[s] = [float(x) for x in c.values]
        except Exception:
            continue
    return out


def _stats(c):
    """\u0e23\u0e32\u0e04\u0e32\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \xb7 \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49% \xb7 5 \u0e27\u0e31\u0e19% \xb7 \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 1 \u0e1b\u0e35 %"""
    a = np.array(c, dtype=float)
    px = float(a[-1])
    return {
        "px": px,
        "d1": (px / a[-2] - 1) * 100 if len(a) >= 2 else 0.0,
        "d5": (px / a[-6] - 1) * 100 if len(a) >= 6 else 0.0,
        "dd": (px / float(a.max()) - 1) * 100,
        "d5abs": px - float(a[-6]) if len(a) >= 6 else 0.0,
    }


def _regime(dd):
    if dd <= -20:
        return "\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e21\u0e35 (\u0e23\u0e48\u0e27\u0e07\u0e40\u0e01\u0e34\u0e19 20%)", _DN
    if dd <= -10:
        return "\u0e20\u0e32\u0e27\u0e30\u0e1b\u0e23\u0e31\u0e1a\u0e10\u0e32\u0e19 \u0e2b\u0e23\u0e37\u0e2d Correction (\u0e23\u0e48\u0e27\u0e07\u0e40\u0e01\u0e34\u0e19 10%)", _DN
    if dd <= -5:
        return "\u0e22\u0e48\u0e2d\u0e15\u0e31\u0e27\u0e1e\u0e2d\u0e2a\u0e21\u0e04\u0e27\u0e23 (\u0e23\u0e48\u0e27\u0e07 5-10%)", "#fcee0a"
    if dd <= -2:
        return "\u0e22\u0e48\u0e2d\u0e15\u0e31\u0e27\u0e40\u0e1a\u0e32\u0e46", "#fcee0a"
    return "\u0e22\u0e31\u0e07\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14", _UP


@st.cache_data(ttl=3600, show_spinner=False)
def _valuation(symbols):
    """P/E \u0e41\u0e25\u0e30 Forward P/E \u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2b\u0e38\u0e49\u0e19 (\u0e14\u0e36\u0e07\u0e02\u0e19\u0e32\u0e19 4 \u0e40\u0e18\u0e23\u0e14) -> {sym: (pe, fpe)} \u0e17\u0e35\u0e48\u0e14\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e47\u0e19 None"""
    from concurrent.futures import ThreadPoolExecutor
    syms = list(symbols)

    def one(s):
        try:
            info = yf.Ticker(s).info or {}
        except Exception:
            return (None, None)
        pe, fpe = info.get("trailingPE"), info.get("forwardPE")
        pe = float(pe) if isinstance(pe, (int, float)) and pe > 0 else None
        fpe = float(fpe) if isinstance(fpe, (int, float)) and fpe > 0 else None
        return (pe, fpe)
    try:
        with ThreadPoolExecutor(max_workers=4) as ex:
            res = list(ex.map(one, syms))
    except Exception:
        res = [(None, None)] * len(syms)
    return dict(zip(syms, res))


def _rss(q, n=10):
    """\u0e15\u0e31\u0e27\u0e2a\u0e33\u0e23\u0e2d\u0e07: \u0e14\u0e36\u0e07 Google News RSS \u0e40\u0e2d\u0e07 \u0e16\u0e49\u0e32 news_radar \u0e43\u0e0a\u0e49\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49"""
    import urllib.parse as up
    import urllib.request as ur
    import xml.etree.ElementTree as ET
    url = "https://news.google.com/rss/search?q=%s&hl=en-US&gl=US&ceid=US:en" % up.quote(q)
    try:
        raw = ur.urlopen(ur.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=8).read()
        root = ET.fromstring(raw)
    except Exception:
        return []
    out = []
    for it in root.iter("item"):
        t = (it.findtext("title") or "").strip()
        src = (it.findtext("source") or "").strip()
        if t:
            out.append({"title": t, "source": src, "link": it.findtext("link") or ""})
        if len(out) >= n:
            break
    return out


@st.cache_data(ttl=900, show_spinner=False)
def _headlines():
    """\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21 7 \u0e27\u0e31\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 (\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e2a\u0e16\u0e32\u0e19\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e35\u0e49) (\u0e44\u0e21\u0e48\u0e0b\u0e49\u0e33) -> [{title, source, link}]"""
    got = []
    for q in _QUERIES:
        rows = []
        try:
            import news_radar
            rows = news_radar.fetch_google_news(q, max_items=12) or []
        except Exception:
            rows = []
        if not rows:
            rows = _rss(q, 12)
        got.extend(rows)
    out, seen = [], set()
    for n in got:
        t = (n.get("title") or "").strip()
        src = n.get("source") or ""
        if " - " in t and src and t.endswith(src):
            t = t[:-(len(src) + 3)].strip()
        k = _re.sub(r"[^a-z0-9]", "", t.lower())[:50]
        if not t or k in seen:
            continue
        seen.add(k)
        out.append({"title": t, "source": "" if src == "\u0e44\u0e21\u0e48\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e2b\u0e25\u0e48\u0e07" else src, "link": n.get("link", "")})
    return out


def _themes(rows, g, down=False):
    """\u0e08\u0e31\u0e14\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e40\u0e1b\u0e47\u0e19\u0e18\u0e35\u0e21 \u0e41\u0e25\u0e49\u0e27\u0e43\u0e2b\u0e49\u0e04\u0e30\u0e41\u0e19\u0e19\u0e23\u0e27\u0e21\u0e01\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e15\u0e25\u0e32\u0e14\u0e17\u0e35\u0e48\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19 -> [(code, score, [rows], evidence_text)] \u0e40\u0e23\u0e35\u0e22\u0e07\u0e21\u0e32\u0e01\u0e44\u0e1b\u0e19\u0e49\u0e2d\u0e22"""
    hits = {k: [] for k in _THEME_RX}
    for r in rows:
        if down and _REBOUND.search(r["title"]):
            continue  # \u0e02\u0e48\u0e32\u0e27\u0e40\u0e14\u0e49\u0e07/\u0e1f\u0e37\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e02\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e40\u0e17\u0e02\u0e32\u0e22
        for k, rx in _THEME_RX.items():
            if rx.search(r["title"]):
                hits[k].append(r)
    ev, boost = {}, {}
    oil = g.get("CL=F")
    if oil and abs(oil["d5"]) >= 4:
        ev["oil"] = "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19: \u0e23\u0e32\u0e04\u0e32\u0e19\u0e49\u0e33\u0e21\u0e31\u0e19\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e41\u0e23\u0e07 %s %.1f%% \u0e43\u0e19 5 \u0e27\u0e31\u0e19 (\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 %.1f \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c)" % ("\u0e02\u0e36\u0e49\u0e19" if oil["d5"] > 0 else "\u0e25\u0e07", abs(oil["d5"]), oil["px"])
        boost["oil"] = 2
    tnx = g.get("^TNX")
    if tnx:
        val = tnx["px"] if tnx["px"] < 20 else tnx["px"] / 10
        bp = tnx["d5abs"] * (100 if tnx["px"] < 20 else 10)
        mv = ("%s %.0f \u0e08\u0e38\u0e14\u0e10\u0e32\u0e19 (bp) \u0e43\u0e19 5 \u0e27\u0e31\u0e19" % ("\u0e02\u0e36\u0e49\u0e19" if bp > 0 else "\u0e25\u0e07", abs(bp))) if abs(bp) >= 3 else "\u0e17\u0e23\u0e07\u0e15\u0e31\u0e27\u0e43\u0e19 5 \u0e27\u0e31\u0e19"
        if val >= 4.5:
            ev["rates"] = "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19: \u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23 10 \u0e1b\u0e35 \u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48 %.2f%% (\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e2a\u0e39\u0e07 = \u0e14\u0e2d\u0e01\u0e40\u0e1a\u0e35\u0e49\u0e22\u0e41\u0e1e\u0e07\u0e19\u0e32\u0e19) %s" % (val, mv)
            boost["rates"] = 2
        elif abs(bp) >= 8:
            ev["rates"] = "\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19: \u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e1e\u0e31\u0e19\u0e18\u0e1a\u0e31\u0e15\u0e23 10 \u0e1b\u0e35 %s \u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 %.2f%%" % (mv, val)
            boost["rates"] = 2 if bp > 0 else 0
    res = []
    for k, rs in hits.items():
        sc = len(rs) + boost.get(k, 0)
        if sc >= 2 and (rs or k in boost):
            res.append((k, sc, rs, ev.get(k, "")))
    res.sort(key=lambda x: -x[1])
    shown, out = set(), []
    for k, sc, rs, evt in res[:4]:
        uniq = []
        for h in rs:
            key = _re.sub(r"[^a-z0-9]", "", h["title"].lower())[:50]
            if key in shown:
                continue  # \u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e02\u0e36\u0e49\u0e19\u0e41\u0e04\u0e48\u0e18\u0e35\u0e21\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e44\u0e21\u0e48\u0e0b\u0e49\u0e33\u0e2b\u0e25\u0e32\u0e22\u0e18\u0e35\u0e21
            shown.add(key)
            uniq.append(h)
            if len(uniq) >= 6:
                break
        out.append((k, sc, uniq, evt))
    return out


# ---------------------------------------------------------------
# \u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25
# ---------------------------------------------------------------
def _article(sp, nq, stock_rows, low_ct, cyc, th, tr, down, today):
    """\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e25\u0e49\u0e27\u0e19 (\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e44\u0e1b\u0e42\u0e1e\u0e2a\u0e15\u0e4c/\u0e2a\u0e48\u0e07\u0e15\u0e48\u0e2d\u0e44\u0e14\u0e49) \u0e25\u0e33\u0e14\u0e31\u0e1a\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e1a\u0e17\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e23\u0e38\u0e1b\u0e15\u0e25\u0e32\u0e14"""
    L = []
    s1 = []
    if sp:
        s1.append("\u0e14\u0e31\u0e0a\u0e19\u0e35 S&P 500 \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e43\u0e19 1 \u0e1b\u0e35\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 %.1f%% (\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %+.1f%%)" % (abs(sp["dd"]), sp["d1"]))
    if nq:
        tail = ""
        if -20 < nq["dd"] <= -10:
            tail = " \u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e48\u0e20\u0e32\u0e27\u0e30\u0e1b\u0e23\u0e31\u0e1a\u0e10\u0e32\u0e19 (Correction)"
        elif nq["dd"] <= -20:
            tail = " \u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e48\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e21\u0e35"
        s1.append("\u0e02\u0e13\u0e30\u0e17\u0e35\u0e48 Nasdaq \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 %.1f%% (\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %+.1f%%)%s" % (abs(nq["dd"]), nq["d1"], tail))
    L.append(" ".join(s1))
    if stock_rows:
        L.append("")
        L.append("\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e17\u0e35\u0e48\u0e19\u0e48\u0e32\u0e08\u0e31\u0e1a\u0e15\u0e32 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e42\u0e14\u0e22\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 \u0e13 \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 %s (P/E = \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e48\u0e2d\u0e01\u0e33\u0e44\u0e23):" % today)
        for s, d, pe, fpe in stock_rows:
            L.append("\u2022 %s: \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 %.1f%% \u00b7 P/E %s \u00b7 Forward P/E %s" % (
                _NAMES.get(s, s), abs(d["dd"]), ("%.1f \u0e40\u0e17\u0e48\u0e32" % pe) if pe else "-", ("%.1f \u0e40\u0e17\u0e48\u0e32" % fpe) if fpe else "-"))
        L.append("")
        if low_ct:
            L.append("Forward P/E \u0e17\u0e35\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 P/E \u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 \u0e2a\u0e30\u0e17\u0e49\u0e2d\u0e19\u0e27\u0e48\u0e32\u0e19\u0e31\u0e01\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e08\u0e30\u0e40\u0e15\u0e34\u0e1a\u0e42\u0e15 \u0e41\u0e15\u0e48\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e14\u0e39\u0e23\u0e32\u0e04\u0e32\u0e16\u0e39\u0e01\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2b\u0e21\u0e32\u0e22\u0e04\u0e27\u0e32\u0e21\u0e27\u0e48\u0e32\u0e08\u0e30\u0e43\u0e2b\u0e49\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e17\u0e35\u0e48\u0e14\u0e35\u0e40\u0e2a\u0e21\u0e2d\u0e44\u0e1b")
        if cyc:
            L.append("%s \u0e40\u0e1b\u0e47\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e27\u0e31\u0e0f\u0e08\u0e31\u0e01\u0e23 P/E \u0e15\u0e48\u0e33\u0e21\u0e31\u0e01\u0e40\u0e01\u0e34\u0e14\u0e15\u0e2d\u0e19\u0e01\u0e33\u0e44\u0e23\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e23\u0e2d\u0e1a \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e16\u0e39\u0e01\u0e40\u0e2a\u0e21\u0e2d" % ", ".join(_NAMES.get(x, x) for x in cyc))
    if th:
        L.append("")
        L.append("\u0e41\u0e25\u0e49\u0e27\u0e17\u0e33\u0e44\u0e21\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e16\u0e36\u0e07\u0e01\u0e33\u0e25\u0e31\u0e07\u0e16\u0e39\u0e01\u0e40\u0e17\u0e02\u0e32\u0e22\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e2b\u0e19\u0e31\u0e01? (\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e35\u0e49)" if down else "\u0e41\u0e25\u0e49\u0e27\u0e15\u0e25\u0e32\u0e14\u0e01\u0e33\u0e25\u0e31\u0e07\u0e2a\u0e19\u0e43\u0e08\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e2d\u0e30\u0e44\u0e23\u0e2d\u0e22\u0e39\u0e48? (\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e35\u0e49)")
        for i, (k, _sc, rs, evt) in enumerate(th):
            L.append("")
            L.append("\u0e1b\u0e23\u0e30\u0e40\u0e14\u0e47\u0e19%s: %s" % (_ORD[i] if i < len(_ORD) else str(i + 1), _THEME_NAME[k]))
            stx = _story(k, rs)
            if stx:
                L.append(stx)
            if evt:
                L.append(evt)
        L.append("")
        L.append("(\u0e1b\u0e23\u0e30\u0e40\u0e14\u0e47\u0e19\u0e40\u0e2b\u0e25\u0e48\u0e32\u0e19\u0e35\u0e49\u0e08\u0e31\u0e14\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e08\u0e32\u0e01\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27 \u0e40\u0e1b\u0e47\u0e19\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e17\u0e35\u0e48\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e41\u0e25\u0e49\u0e27)")
        L.append("")
        L.append("\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e19\u0e35\u0e49\u0e2a\u0e48\u0e07\u0e1c\u0e25\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e15\u0e48\u0e2d\u0e0a\u0e35\u0e27\u0e34\u0e15\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13 \u0e44\u0e21\u0e48\u0e27\u0e48\u0e32\u0e04\u0e38\u0e13\u0e08\u0e30\u0e25\u0e07\u0e17\u0e38\u0e19\u0e43\u0e19\u0e15\u0e25\u0e32\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48\u0e01\u0e47\u0e15\u0e32\u0e21")
        for k, _sc, _rs, _ev in th:
            L.append("\u2022 %s: %s" % (_THEME_NAME[k], _THEME_ME[k]))
    L.append("")
    L.append("\u0e17\u0e35\u0e48\u0e21\u0e32: Yahoo Finance, Google News \u00b7 \u0e2a\u0e23\u0e38\u0e1b\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22 \u00b7 %s" % today)
    return "\n".join(L)


_STOP = set("""about above after again against amid among around because before being below between both could does doing down during each
from further have having here into itself just more most much only other over same should since some such than that their them then there these they this
those through under until very want were what when where which while will with would your market markets stock stocks share shares wall street investors investor
today week weeks year years says said say new news latest first last next less also back ahead rises rise falls fall drop drops gain gains dow nasdaq index indexes
futures trading traders session close closes open opens record high highs low lows sell selloff sell-off rally rallies slide slides surge surges plunge plunges
tumble tumbles jump jumps climb climbs sink sinks lose loses losing biggest worst best big small points point percent here's how why what's live updates update
analysis explained watch things know need take takes top bull bear company companies business money tech sector report reports amid fears worries concerns
investor's stocks' u.s. us americans american economy economic economists analysts expected expect expects set sets still make makes making like look looks""".split())
_AI_MODEL = "claude-sonnet-5-5"   # รุ่น AI ที่ใช้ตอนมีคีย์ (เปลี่ยนได้)


def _emerging(rows, top=5):
    """หาคำที่โผล่ซ้ำในหลายพาดหัว แต่ไม่ตรงกับธีมที่เว็บรู้จัก/คำทั่วไป -> [(คำ, จำนวนพาดหัว, [ตัวอย่างพาดหัว])]
    เป็นแค่การนับคำ ไม่ได้เข้าใจเนื้อหา — ไว้ชี้ให้เห็นว่ามีเรื่องใหม่ที่เว็บยังไม่มีคำอธิบาย"""
    known = {n.lower() for n in _NAMES.values()} | {s.lower() for s in _NAMES}
    df, ex = {}, {}
    for r in rows:
        toks = set()
        for w in _re.findall(r"[a-z][a-z\-']{3,}", r["title"].lower()):
            w = w[:-2] if w.endswith("'s") else w
            if len(w) < 4 or w in _STOP or w in known:
                continue
            if any(rx.search(w) for rx in _THEME_RX.values()):
                continue
            toks.add(w)
        for w in toks:
            df[w] = df.get(w, 0) + 1
            ex.setdefault(w, []).append(r)
    out = [(w, n, ex[w][:2]) for w, n in df.items() if n >= 3]
    out.sort(key=lambda x: (-x[1], x[0]))
    return out[:top]


def _find_ai_key(passed=""):
    """หาคีย์ AI จากค่าที่ส่งมา / st.secrets / ตัวแปรสภาพแวดล้อม ANTHROPIC_API_KEY — ไม่มีคีย์ = ไม่แสดงปุ่ม AI"""
    k = (passed or "").strip()
    if not k:
        try:
            k = str(st.secrets.get("ANTHROPIC_API_KEY", "") or "").strip()
        except Exception:
            k = ""
    if not k:
        import os
        k = (os.environ.get("ANTHROPIC_API_KEY") or "").strip()
    return k


@st.cache_data(ttl=3600, show_spinner=False)
def _ai_explain(_key, terms, heads):
    """ให้ AI อธิบายหัวข้อใหม่เป็นภาษาไทยง่ายๆ จากพาดหัวที่ให้เท่านั้น (ต้องมีคีย์ · ยังไม่ได้ทดสอบกับ API จริง)"""
    import json as _json
    import urllib.request as ur
    prompt = (
        "คุณช่วยสรุปข่าวตลาดหุ้นเป็นภาษาไทยง่ายๆ ให้คนที่ไม่ถนัดตัวเลข ใช้เฉพาะข้อมูลจากพาดหัวด้านล่างเท่านั้น "
        "ห้ามเดาตัวเลข ห้ามแนะนำซื้อขาย และต้องบอกว่าเป็นการประมาณ\n"
        "สำหรับแต่ละหัวข้อ เขียน 2 บรรทัด: (1) น่าจะเกี่ยวกับอะไรและกระทบตลาดยังไง (2) กระทบชีวิตคนทั่วไปยังไง\n\n"
        "หัวข้อ: " + ", ".join(terms) + "\n\nพาดหัวข่าว:\n" + "\n".join("- " + h for h in heads))
    body = _json.dumps({"model": _AI_MODEL, "max_tokens": 800, "messages": [{"role": "user", "content": prompt}]}).encode("utf-8")
    req = ur.Request("https://api.anthropic.com/v1/messages", data=body, method="POST",
                     headers={"x-api-key": _key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with ur.urlopen(req, timeout=40) as r:
        data = _json.loads(r.read().decode("utf-8"))
    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text").strip()


def _emerging_box(rows, ai_key=""):
    em = _emerging(rows)
    if not em:
        st.caption("🆕 ตรวจหัวข้อใหม่แล้ว: ยังไม่พบเรื่องที่ข่าวพูดถึงเยอะแต่เว็บไม่รู้จัก")
        return
    body = ""
    for w, n, exs in em:
        body += '<div class="mb-th">🆕 %s <small>· อยู่ใน %d พาดหัว</small></div>' % (_e(w), n)
        for h in exs:
            body += '<div class="mb-hl">• <a href="%s" target="_blank">%s</a>%s</div>' % (
                _e(h.get("link", "")), _e(h["title"]), (" <small>· %s</small>" % _e(h["source"])) if h.get("source") else "")
    st.markdown('<div class="mb"><div class="mb-h">🆕 หัวข้อที่ข่าวพูดถึงเยอะ แต่เว็บยังไม่มีคำอธิบาย</div>%s'
                '<div class="mb-note">เว็บนับคำที่โผล่ซ้ำในพาดหัวเท่านั้น <b>ยังไม่เข้าใจเนื้อหา</b> และ <b>ยังไม่มีคำอธิบายสาเหตุ</b> '
                'ถ้าอยากให้เว็บอธิบายเรื่องนี้ถาวร คัดลอกข้อความด้านล่างไปถาม Claude แล้วขอให้เพิ่มเป็นกลุ่มประเด็นใหม่</div></div>' % body,
                unsafe_allow_html=True)
    terms = tuple(w for w, _n, _e2 in em)
    heads = tuple(h["title"] for _w, _n, exs in em for h in exs)
    prompt = ("ช่วยเพิ่มกลุ่มประเด็นใหม่ในหน้า 'ภาพรวมตลาด' ของเว็บ QUANT (ไฟล์ market_brief.py) "
              "โดยเขียนประโยคอธิบายภาษาไทยง่ายๆ ว่า 'ทำไมเรื่องนี้กระทบตลาด' และ 'กระทบชีวิตเรายังไง'\n"
              "หัวข้อที่พบ: " + ", ".join(terms) + "\nพาดหัวข่าวที่เกี่ยวข้อง:\n" + "\n".join("- " + h for h in heads))
    with st.expander("📋 คัดลอกข้อความนี้ไปถาม Claude", expanded=False):
        st.code(prompt, language=None)
    key = _find_ai_key(ai_key)
    if key:
        if st.button("🤖 ให้ AI อธิบายหัวข้อใหม่ (ต้องมีคีย์ · มีค่าใช้จ่ายตามการใช้งาน)", key="mb_ai_btn"):
            try:
                with st.spinner("กำลังให้ AI สรุป ..."):
                    txt = _ai_explain(key, terms, heads)
                st.markdown('<div class="mb"><div class="mb-h">🤖 AI อธิบาย (เป็นการประมาณจากพาดหัว ไม่ใช่สาเหตุที่ยืนยันแล้ว)</div><div class="mb-me" style="white-space:pre-wrap">%s</div></div>' % _e(txt), unsafe_allow_html=True)
            except Exception as ex:
                st.warning("เรียก AI ไม่สำเร็จ: " + str(ex)[:120])


def _box(title, val, sub, col):
    return '<div class="mb-box"><div class="t">%s</div><div class="v">%s</div><div class="s" style="color:%s">%s</div></div>' % (_e(title), val, col, sub)


def render_market_brief(ai_key=""):
    st.markdown(_CSS, unsafe_allow_html=True)
    text = st.text_input("\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e32\u0e01\u0e14\u0e39\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32 (\u0e04\u0e31\u0e48\u0e19\u0e14\u0e49\u0e27\u0e22\u0e0a\u0e48\u0e2d\u0e07\u0e27\u0e48\u0e32\u0e07)", value=_DEFAULT_STOCKS, key="mb_syms")
    stocks = []
    for s in _re.split(r"[\s,]+", (text or "").upper()):
        if _re.fullmatch(r"[A-Z.\-]{1,6}", s) and s not in stocks:
            stocks.append(s)
    stocks = stocks[:10] or _DEFAULT_STOCKS.split()
    top = st.container()  # \u0e01\u0e25\u0e48\u0e2d\u0e07 "\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21" \u0e40\u0e15\u0e34\u0e21\u0e17\u0e35\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e23\u0e1a \u0e41\u0e15\u0e48\u0e41\u0e2a\u0e14\u0e07\u0e44\u0e27\u0e49\u0e1a\u0e19\u0e2a\u0e38\u0e14
    allsyms = tuple([x for x, _ in _INDEX] + [x for x, _ in _GAUGE] + stocks)
    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e41\u0e08\u0e47\u0e04\u0e2d\u0e34\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e15\u0e25\u0e32\u0e14 ..."):
        px = _prices(allsyms)
    ix = {s: _stats(px[s]) for s, _ in _INDEX if s in px}
    g = {s: _stats(px[s]) for s, _ in _GAUGE if s in px}
    if not ix:
        st.warning("\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e14\u0e31\u0e0a\u0e19\u0e35\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e25\u0e2d\u0e07\u0e43\u0e2b\u0e21\u0e48\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e19\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e19\u0e32\u0e17\u0e35")
        return

    # ---- 1) \u0e15\u0e25\u0e32\u0e14\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 ----
    sp, nq = ix.get("^GSPC"), ix.get("^IXIC")
    parts = []
    if sp:
        parts.append("\u0e14\u0e31\u0e0a\u0e19\u0e35 <b>S&amp;P 500</b> \u0e2d\u0e22\u0e39\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e43\u0e19 1 \u0e1b\u0e35 \u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 <b style=\"color:%s\">%s</b>" % (_c(sp["dd"]), "%.1f%%" % abs(sp["dd"])))
    if nq:
        lab, col = _regime(nq["dd"])
        parts.append("\u0e02\u0e13\u0e30\u0e17\u0e35\u0e48 <b>Nasdaq</b> \u0e2d\u0e22\u0e39\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 <b style=\"color:%s\">%s</b> <span class=\"mb-tag\" style=\"color:%s;border-color:%s\">%s</span>" % (_c(nq["dd"]), "%.1f%%" % abs(nq["dd"]), col, col, _e(lab)))
    big = " ".join(parts)
    boxes = ""
    for s, name in _INDEX:
        if s in ix:
            d = ix[s]
            boxes += _box(name, "{:,.0f}".format(d["px"]), "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %s \xb7 5 \u0e27\u0e31\u0e19 %s" % (_fmtp(d["d1"]), _fmtp(d["d5"])), _c(d["d5"]))
    for s, name in _GAUGE:
        if s in g:
            d = g[s]
            v = d["px"] if not (s == "^TNX" and d["px"] >= 20) else d["px"] / 10
            vs = "%.2f%%" % v if s == "^TNX" else "%.1f" % v
            boxes += _box(name, vs, "5 \u0e27\u0e31\u0e19 %s" % _fmtp(d["d5"]), _c(d["d5"]) if s != "^VIX" else (_DN if d["d5"] >= 0 else _UP))
    vx = g.get("^VIX")
    vnote = ""
    if vx:
        vnote = "\u0e14\u0e31\u0e0a\u0e19\u0e35\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27 (VIX) %.1f = %s" % (vx["px"], "\u0e15\u0e25\u0e32\u0e14\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27\u0e2a\u0e39\u0e07 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07" if vx["px"] >= 30 else ("\u0e40\u0e23\u0e34\u0e48\u0e21\u0e01\u0e31\u0e07\u0e27\u0e25" if vx["px"] >= 20 else "\u0e15\u0e25\u0e32\u0e14\u0e22\u0e31\u0e07\u0e04\u0e48\u0e2d\u0e19\u0e02\u0e49\u0e32\u0e07\u0e19\u0e34\u0e48\u0e07"))
    st.markdown('<div class="mb"><div class="mb-big">%s</div><div class="mb-g">%s</div><div class="mb-note">%s \xb7 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo \u0e2d\u0e32\u0e08\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c\u0e23\u0e32\u0e27 15 \u0e19\u0e32\u0e17\u0e35</div></div>' % (big, boxes, _e(vnote)), unsafe_allow_html=True)

    # ---- 2) \u0e2b\u0e38\u0e49\u0e19\u0e1e\u0e25\u0e31\u0e07\u0e02\u0e31\u0e1a\u0e40\u0e04\u0e25\u0e37\u0e48\u0e2d\u0e19 + \u0e21\u0e39\u0e25\u0e04\u0e48\u0e32 ----
    val = _valuation(tuple(stocks))
    trs = ""
    note_cyc = []
    srows = []
    for s in stocks:
        if s not in px:
            continue
        d = _stats(px[s])
        pe, fpe = val.get(s, (None, None))
        srows.append((s, d, pe, fpe))
        trs += "<tr><td>%s</td><td>%.2f</td><td style=\"color:%s!important;-webkit-text-fill-color:%s\">%s</td><td style=\"color:%s!important;-webkit-text-fill-color:%s\">%s</td><td>%s</td><td>%s</td></tr>" % (
            _e(s), d["px"], _c(d["d5"]), _c(d["d5"]), _fmtp(d["d5"]), _c(d["dd"]), _c(d["dd"]), _fmtp(d["dd"]),
            ("%.1f \u0e40\u0e17\u0e48\u0e32" % pe) if pe else "-", ("%.1f \u0e40\u0e17\u0e48\u0e32" % fpe) if fpe else "-")
        if s in _CYCLICAL and pe and pe < 15:
            note_cyc.append(s)
    both = [(s, val.get(s)) for s in stocks if s in px and val.get(s) and val[s][0] and val[s][1]]
    low = [s for s, (pe_, fpe_) in both if fpe_ < pe_]
    vsum = ""
    if both:
        vsum = "<br><b>\u0e2d\u0e48\u0e32\u0e19\u0e41\u0e1a\u0e1a\u0e07\u0e48\u0e32\u0e22:</b> %d \u0e43\u0e19 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 \u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e1b\u0e35\u0e2b\u0e19\u0e49\u0e32\u0e42\u0e15\u0e02\u0e36\u0e49\u0e19 (Forward P/E \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 P/E \u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19)%s \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e2d\u0e32\u0e08\u0e2a\u0e30\u0e17\u0e49\u0e2d\u0e19\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e25\u0e07\u0e21\u0e32\u0e41\u0e23\u0e07\u0e01\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e04\u0e32\u0e14 \u0e41\u0e15\u0e48\u0e01\u0e47\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e01\u0e32\u0e23\u0e04\u0e32\u0e14\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e02\u0e2d\u0e07\u0e19\u0e31\u0e01\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c \u0e0b\u0e36\u0e48\u0e07\u0e1c\u0e34\u0e14\u0e44\u0e14\u0e49" % (
            len(low), len(both), (": " + ", ".join(_e(x) for x in low)) if low else "")
    cyc = ""
    if note_cyc:
        cyc = "<br>\u26a0\ufe0f %s \u0e40\u0e1b\u0e47\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e27\u0e31\u0e0f\u0e08\u0e31\u0e01\u0e23 P/E \u0e15\u0e48\u0e33\u0e21\u0e31\u0e01\u0e40\u0e01\u0e34\u0e14\u0e15\u0e2d\u0e19\u0e01\u0e33\u0e44\u0e23\u0e2d\u0e22\u0e39\u0e48\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e23\u0e2d\u0e1a \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e16\u0e39\u0e01\u0e40\u0e2a\u0e21\u0e2d" % _e(", ".join(note_cyc))
    st.markdown(
        '<div class="mb"><div class="mb-h">\U0001F4C8 \u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e23\u0e32\u0e04\u0e32\u0e01\u0e31\u0e1a\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32</div>'
        '<table class="mb-tbl"><tr><th>\u0e2b\u0e38\u0e49\u0e19</th><th>\u0e23\u0e32\u0e04\u0e32</th><th>5 \u0e27\u0e31\u0e19</th><th>\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 1 \u0e1b\u0e35</th><th>P/E \u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19</th><th>P/E \u0e17\u0e35\u0e48\u0e04\u0e32\u0e14 (Forward)</th></tr>%s</table>'
        '<div class="mb-note">P/E = \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19 \xf7 \u0e01\u0e33\u0e44\u0e23\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19 (\u0e22\u0e34\u0e48\u0e07\u0e15\u0e48\u0e33\u0e22\u0e34\u0e48\u0e07\u0e08\u0e48\u0e32\u0e22\u0e41\u0e1e\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e15\u0e48\u0e2d\u0e01\u0e33\u0e44\u0e23 1 \u0e1a\u0e32\u0e17) \xb7 Forward P/E \u0e43\u0e0a\u0e49\u0e01\u0e33\u0e44\u0e23\u0e17\u0e35\u0e48\u0e19\u0e31\u0e01\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e04\u0e32\u0e14\u0e1b\u0e35\u0e2b\u0e19\u0e49\u0e32 \u0e16\u0e49\u0e32\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 P/E \u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 = \u0e04\u0e32\u0e14\u0e27\u0e48\u0e32\u0e01\u0e33\u0e44\u0e23\u0e08\u0e30\u0e42\u0e15 '
        '\xb7 <b>\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e14\u0e39\u0e23\u0e32\u0e04\u0e32\u0e16\u0e39\u0e01\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e08\u0e30\u0e43\u0e2b\u0e49\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e14\u0e35\u0e40\u0e2a\u0e21\u0e2d\u0e44\u0e1b</b>%s%s</div></div>' % (trs or "<tr><td colspan=6>\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49</td></tr>", vsum, cyc), unsafe_allow_html=True)

    # ---- 3) \u0e17\u0e33\u0e44\u0e21\u0e16\u0e36\u0e07\u0e16\u0e39\u0e01\u0e40\u0e17\u0e02\u0e32\u0e22 ----
    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e41\u0e08\u0e47\u0e04\u0e2d\u0e34\u0e19\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27\u0e08\u0e32\u0e01 Net ..."):
        rows = _headlines()
        down = bool((sp and sp["d5"] <= -1) or (nq and nq["d5"] <= -1))
        th = _themes(rows, g, down) if rows or g else []
    tr = {}
    head = "\U0001F50D \u0e17\u0e33\u0e44\u0e21\u0e15\u0e25\u0e32\u0e14\u0e16\u0e36\u0e07\u0e16\u0e39\u0e01\u0e40\u0e17\u0e02\u0e32\u0e22" if down else "\U0001F50D \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e01\u0e33\u0e25\u0e31\u0e07\u0e2a\u0e19\u0e43\u0e08"
    if th:
        pick = [h for _k, _s, rs, _e2 in th for h in rs[:2]]
        tr = {}
        try:
            import insight
            outs = insight.tr_list([h["title"] for h in pick])
            tr = {h["title"]: (o or h["title"]) for h, o in zip(pick, outs)}
        except Exception:
            tr = {}
        body = ""
        for i, (k, sc, rs, evt) in enumerate(th, 1):
            body += '<div class="mb-th">\u0e1b\u0e23\u0e30\u0e40\u0e14\u0e47\u0e19\u0e17\u0e35\u0e48 %d: %s</div>' % (i, _e(_THEME_NAME[k]))
            if evt:
                body += '<div class="mb-ev">%s</div>' % _e(evt)
            for h in rs[:2]:
                body += '<div class="mb-hl">\u2022 <a href="%s" target="_blank">%s</a>%s</div>' % (
                    _e(h["link"]), _e(tr.get(h["title"], h["title"])), (" <small>\xb7 %s</small>" % _e(h["source"])) if h["source"] else "")
            if not rs:
                body += '<div class="mb-hl"><small>\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e40\u0e08\u0e2d\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27\u0e15\u0e23\u0e07\u0e46 \u0e43\u0e19\u0e18\u0e35\u0e21\u0e19\u0e35\u0e49 (\u0e14\u0e39\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e15\u0e25\u0e32\u0e14\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19)</small></div>'
        st.markdown('<div class="mb"><div class="mb-h">%s</div>%s'
                    '<div class="mb-note">\u0e08\u0e31\u0e14\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e08\u0e32\u0e01\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 7 \u0e27\u0e31\u0e19\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 (\u0e40\u0e1b\u0e47\u0e19\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e2a\u0e16\u0e32\u0e19\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e35\u0e49 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49) + \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e15\u0e25\u0e32\u0e14 \u0e40\u0e1b\u0e47\u0e19\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 <b>\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e17\u0e35\u0e48\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e41\u0e25\u0e49\u0e27</b> \u0e01\u0e14\u0e2d\u0e48\u0e32\u0e19\u0e02\u0e48\u0e32\u0e27\u0e15\u0e49\u0e19\u0e09\u0e1a\u0e31\u0e1a\u0e01\u0e48\u0e2d\u0e19\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e2d\u0e07</div></div>' % (head, body), unsafe_allow_html=True)

        # ---- 4) \u0e01\u0e23\u0e30\u0e17\u0e1a\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e07 ----
        me = "".join('<div class="mb-me">\u2022 <b>%s</b> \u2014 %s</div>' % (_e(_THEME_NAME[k]), _e(_THEME_ME[k])) for k, _s, _r, _ev in th)
        st.markdown('<div class="mb"><div class="mb-h">\U0001F3E0 \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e19\u0e35\u0e49\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e04\u0e38\u0e13\u0e22\u0e31\u0e07\u0e44\u0e07 (\u0e44\u0e21\u0e48\u0e27\u0e48\u0e32\u0e08\u0e30\u0e25\u0e07\u0e17\u0e38\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48)</div>%s</div>' % me, unsafe_allow_html=True)
    else:
        st.markdown('<div class="mb"><div class="mb-h">%s</div><div class="mb-me">\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48\u0e0a\u0e35\u0e49\u0e0a\u0e31\u0e14\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e2d\u0e30\u0e44\u0e23 (\u0e2b\u0e23\u0e37\u0e2d\u0e14\u0e36\u0e07\u0e02\u0e48\u0e32\u0e27\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49) \u0e23\u0e30\u0e1a\u0e1a\u0e44\u0e21\u0e48\u0e40\u0e14\u0e32\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38</div></div>' % head, unsafe_allow_html=True)

    try:
        _emerging_box(rows, ai_key)
    except Exception:
        pass

    try:
        txt = _article(sp, nq, srows, len(low), note_cyc, th, tr, down, _dt.date.today().strftime("%d/%m/%Y"))
        with top:
            try:
                box = st.container(border=True)
            except TypeError:
                box = st.container()
            with box:
                st.markdown('<div class="mb-h" style="margin-top:2px">\U0001F4CB \u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 (\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e44\u0e1b\u0e43\u0e0a\u0e49\u0e15\u0e48\u0e2d\u0e44\u0e14\u0e49)</div>'
                            '<div class="mb-note" style="margin:0 0 6px">\u0e01\u0e14\u0e44\u0e2d\u0e04\u0e2d\u0e19\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e17\u0e35\u0e48\u0e21\u0e38\u0e21\u0e02\u0e27\u0e32\u0e1a\u0e19\u0e02\u0e2d\u0e07\u0e01\u0e25\u0e48\u0e2d\u0e07 \xb7 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e25\u0e30\u0e01\u0e23\u0e32\u0e1f\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e2d\u0e22\u0e39\u0e48\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e41\u0e17\u0e47\u0e1a\u0e19\u0e35\u0e49</div>', unsafe_allow_html=True)
                try:
                    st.code(txt, language=None, wrap_lines=True)
                except TypeError:
                    st.text_area("\u0e2a\u0e23\u0e38\u0e1b", value=txt, height=420, label_visibility="collapsed")
    except Exception:
        pass
    st.caption("\u0e2a\u0e23\u0e38\u0e1b\u0e19\u0e35\u0e49\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e25\u0e30\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e02\u0e2d\u0e07\u0e04\u0e19 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e04\u0e33\u0e41\u0e19\u0e30\u0e19\u0e33\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22 \xb7 %s" % _dt.date.today().strftime("%d/%m/%Y"))