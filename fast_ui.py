# -*- coding: utf-8 -*-
"""fast_ui.py - \u0e2b\u0e19\u0e49\u0e32 "\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07 / FAST TRADE" \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e2a\u0e32\u0e22\u0e40\u0e17\u0e23\u0e14\u0e40\u0e23\u0e47\u0e27 (\u0e16\u0e37\u0e2d\u0e02\u0e49\u0e32\u0e21\u0e27\u0e31\u0e19\u0e16\u0e36\u0e07\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e2a\u0e31\u0e1b\u0e14\u0e32\u0e2b\u0e4c)

\u0e17\u0e33\u0e2d\u0e30\u0e44\u0e23:
1) \u0e2a\u0e20\u0e32\u0e1e\u0e15\u0e25\u0e32\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (S&P / Nasdaq / VIX / \u0e40\u0e07\u0e34\u0e19\u0e44\u0e2b\u0e25\u0e44\u0e1b\u0e44\u0e2b\u0e19)
2) \u0e2a\u0e41\u0e01\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07: % \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49/5 \u0e27\u0e31\u0e19 \xb7 \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1b\u0e01\u0e15\u0e34 \xb7 \u0e04\u0e27\u0e32\u0e21\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e15\u0e48\u0e2d\u0e27\u0e31\u0e19 (ATR) \xb7 RSI \xb7 \u0e23\u0e30\u0e22\u0e30\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19 \xb7 \u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c
3) \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19 1 \u0e15\u0e31\u0e27 \u2192 \u0e40\u0e15\u0e37\u0e2d\u0e19\u0e07\u0e1a\u0e43\u0e01\u0e25\u0e49\u0e2d\u0e2d\u0e01 \xb7 \u0e15\u0e31\u0e27\u0e04\u0e33\u0e19\u0e27\u0e13\u0e02\u0e19\u0e32\u0e14\u0e44\u0e21\u0e49\u0e08\u0e32\u0e01\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22 \xb7 \u0e23\u0e30\u0e14\u0e31\u0e1a 1R/2R/3R \xb7 \u0e01\u0e23\u0e32\u0e1f 3 \u0e40\u0e14\u0e37\u0e2d\u0e19

\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d-\u0e02\u0e32\u0e22 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22: \u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e25\u0e30\u0e04\u0e13\u0e34\u0e15\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19
\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo \u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c\u0e23\u0e32\u0e27 15 \u0e19\u0e32\u0e17\u0e35 \u0e08\u0e36\u0e07\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e2a\u0e32\u0e22 swing \u0e44\u0e21\u0e48\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e40\u0e01\u0e47\u0e07\u0e01\u0e33\u0e44\u0e23\u0e23\u0e32\u0e22\u0e19\u0e32\u0e17\u0e35
"""
import datetime as _dt
import json
import os
import html as _html
import math

import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

DEFAULT_UNIVERSE = ("NVDA AMD AVGO MU SNDK WDC STX MRVL LRCX AMAT KLAC SMCI DELL ARM TSM INTC QCOM TSLA PLTR COIN MSTR HOOD SOFI "
                    "RKLB IONQ AFRM UPST SHOP NFLX META AMZN GOOGL MSFT AAPL CRWD ANET VRT CEG VST OKLO APP")

RB_NAME = "\U0001f3af \u0e25\u0e07\u0e41\u0e23\u0e07 \xb7 \u0e40\u0e23\u0e34\u0e48\u0e21\u0e21\u0e35\u0e25\u0e38\u0e49\u0e19\u0e14\u0e35\u0e14"

PRESETS = [
    (RB_NAME, "\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e21\u0e32\u0e41\u0e25\u0e49\u0e27 (\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 \u226515% \u0e2b\u0e23\u0e37\u0e2d 5 \u0e27\u0e31\u0e19 \u22658%, RSI \u2264 42) \u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e14\u0e49\u0e27\u0e22\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e41\u0e25\u0e49\u0e27\u0e27\u0e48\u0e32\u0e0a\u0e48\u0e27\u0e22\u0e08\u0e23\u0e34\u0e07 (\u2605) \u2014 \u0e40\u0e1b\u0e47\u0e19\u0e04\u0e27\u0e32\u0e21\u0e19\u0e48\u0e32\u0e08\u0e30\u0e40\u0e1b\u0e47\u0e19 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e27\u0e48\u0e32\u0e08\u0e30\u0e02\u0e36\u0e49\u0e19"),
    ("\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", "\u0e41\u0e2a\u0e14\u0e07\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e2a\u0e41\u0e01\u0e19\u0e44\u0e14\u0e49"),
    ("\u0e02\u0e36\u0e49\u0e19\u0e41\u0e23\u0e07 + \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e21\u0e32", "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e02\u0e36\u0e49\u0e19 \u2265 3% \u0e41\u0e25\u0e30\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22 1.5 \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e1b\u0e01\u0e15\u0e34 \u2014 \u0e21\u0e35\u0e04\u0e19\u0e40\u0e02\u0e49\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e08\u0e23\u0e34\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e40\u0e07\u0e35\u0e22\u0e1a\u0e46"),
    ("\u0e22\u0e48\u0e2d\u0e43\u0e19\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e02\u0e36\u0e49\u0e19", "\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e22\u0e31\u0e07\u0e02\u0e36\u0e49\u0e19 (\u0e23\u0e32\u0e04\u0e32 > EMA20 > EMA50) \u0e41\u0e15\u0e48\u0e1e\u0e31\u0e01\u0e15\u0e31\u0e27\u0e25\u0e07\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 4-15% \u0e41\u0e25\u0e30 RSI 38-55 \u2014 \u0e17\u0e35\u0e48\u0e2b\u0e25\u0e32\u0e22\u0e04\u0e19\u0e21\u0e2d\u0e07\u0e2b\u0e32\u0e08\u0e31\u0e07\u0e2b\u0e27\u0e30\u0e40\u0e02\u0e49\u0e32\u0e15\u0e2d\u0e19\u0e22\u0e48\u0e2d"),
    ("\u0e43\u0e01\u0e25\u0e49\u0e17\u0e30\u0e25\u0e38\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07", "\u0e2b\u0e48\u0e32\u0e07\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19\u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 2% \u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e02\u0e36\u0e49\u0e19 \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e44\u0e21\u0e48\u0e41\u0e2b\u0e49\u0e07 \u2014 \u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e32\u0e08\u0e17\u0e30\u0e25\u0e38\u0e2b\u0e23\u0e37\u0e2d\u0e16\u0e39\u0e01\u0e1b\u0e0f\u0e34\u0e40\u0e2a\u0e18"),
    ("\u0e23\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e31\u0e01", "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e25\u0e07 \u2265 5% \u0e2b\u0e23\u0e37\u0e2d 5 \u0e27\u0e31\u0e19\u0e25\u0e07 \u2265 12% \u2014 \u0e23\u0e30\u0e27\u0e31\u0e07\u0e21\u0e35\u0e14\u0e15\u0e01 \u0e2b\u0e23\u0e37\u0e2d\u0e14\u0e39\u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e40\u0e14\u0e49\u0e07\u0e2a\u0e31\u0e49\u0e19 (\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e2a\u0e39\u0e07)"),
]
SORTS = ["% \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (\u0e21\u0e32\u0e01\u2192\u0e19\u0e49\u0e2d\u0e22)", "% \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (\u0e19\u0e49\u0e2d\u0e22\u2192\u0e21\u0e32\u0e01)", "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1b\u0e01\u0e15\u0e34", "\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19 ATR%", "\u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19", "RSI"]

_CSS = (
    "<style>"
    ".fx-note{margin:6px 0 10px;padding:8px 12px;font-size:13px;line-height:1.6;border-left:3px solid #fcee0a;background:rgba(252,238,10,.06);"
    "color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2}"
    ".fx-rule{margin:10px 0;padding:10px 14px;font-size:13px;line-height:1.7;border:1px solid rgba(255,77,109,.45);border-left:4px solid #ff4d6d;"
    "background:rgba(255,77,109,.06);color:#e6e9f7!important;-webkit-text-fill-color:#e6e9f7}"
    ".fx-rule b{color:#ff8fa3!important;-webkit-text-fill-color:#ff8fa3}"
    ".rb-how{margin:8px 0 12px;padding:10px 14px;font-size:13px;line-height:1.8;border:1px solid rgba(0,240,255,.35);background:rgba(0,240,255,.05);"
    "color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2}"
    ".rb-how b{color:#00f0ff!important;-webkit-text-fill-color:#00f0ff}"
    ".rb-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px;margin:10px 0 14px}"
    ".rb-sub{margin:2px 0 6px;color:#aab3d6!important;-webkit-text-fill-color:#aab3d6;font-size:12.5px}"
    ".rb-sub b{color:#e6e9f7!important;-webkit-text-fill-color:#e6e9f7}"
    ".rb-sec{margin:9px 0 2px;font-size:11px;letter-spacing:.6px;color:#6f7aa8!important;-webkit-text-fill-color:#6f7aa8;border-top:1px dashed rgba(111,122,168,.25);padding-top:5px}"
    ".rb-news{font-size:12.5px;line-height:1.5}.rb-news a{color:#9fe8ff!important;-webkit-text-fill-color:#9fe8ff;text-decoration:none}"
    ".rb-mut{color:#6f7aa8!important;-webkit-text-fill-color:#6f7aa8;font-size:12px}"
    ".rb-obsline{margin-top:8px;font-size:11px;color:#6f7aa8!important;-webkit-text-fill-color:#6f7aa8}"
    ".rb-card{padding:12px 14px;border:1px solid rgba(252,238,10,.28);border-left:4px solid #fcee0a;background:rgba(10,14,28,.78);"
    "color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2;font-size:12.5px;line-height:1.55}"
    ".rb-card.hot{border-left-color:#3dffa0;border-color:rgba(61,255,160,.4)}"
    ".rb-top{display:flex;justify-content:space-between;align-items:baseline}"
    ".rb-sym{font-size:20px;font-weight:800;letter-spacing:.5px;color:#fcee0a!important;-webkit-text-fill-color:#fcee0a}"
    ".rb-px{font-size:13px;color:#aab3d6!important;-webkit-text-fill-color:#aab3d6}"
    ".rb-pips{margin:4px 0 2px;letter-spacing:3px;font-size:13px}"
    ".rb-on{color:#3dffa0!important;-webkit-text-fill-color:#3dffa0}.rb-off{color:#2a3150!important;-webkit-text-fill-color:#2a3150}"
    ".rb-row{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0;color:#aab3d6!important;-webkit-text-fill-color:#aab3d6}"
    ".rb-row b{color:#e6e9f7!important;-webkit-text-fill-color:#e6e9f7}"
    ".rb-neg{color:#ff6b86!important;-webkit-text-fill-color:#ff6b86}.rb-pos{color:#3dffa0!important;-webkit-text-fill-color:#3dffa0}"
    ".rb-chip{display:inline-block;margin:2px 4px 2px 0;padding:1px 7px;font-size:11.5px;border:1px solid rgba(61,255,160,.55);"
    "color:#3dffa0!important;-webkit-text-fill-color:#3dffa0;background:rgba(61,255,160,.09)}"
    ".rb-gold{display:inline-block;margin:2px 4px 2px 0;padding:1px 7px;font-size:11.5px;font-weight:700;border:1px solid #fcee0a;"
    "color:#fcee0a!important;-webkit-text-fill-color:#fcee0a;background:rgba(252,238,10,.12)}"
    ".rb-obs{display:inline-block;margin:2px 4px 2px 0;padding:1px 7px;font-size:11.5px;border:1px solid rgba(170,179,214,.35);"
    "color:#8f98bd!important;-webkit-text-fill-color:#8f98bd;background:rgba(170,179,214,.06)}"
    ".sm-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(350px,1fr));column-gap:18px;row-gap:0;margin:12px 0 16px}"
    ".sm-card{position:relative;display:grid;grid-row:span 7;grid-template-rows:subgrid;row-gap:0;margin-bottom:18px;align-content:start;padding:16px 18px 14px;border:1px solid rgba(252,238,10,.22);border-left:5px solid var(--c,#fcee0a);"
    "background:linear-gradient(160deg,rgba(14,19,38,.96),rgba(8,11,24,.92));box-shadow:0 0 24px rgba(0,240,255,.06);"
    "clip-path:polygon(0 0,calc(100% - 16px) 0,100% 16px,100% 100%,0 100%);color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2;font-size:13.5px;line-height:1.6}"
    ".sm-top{display:flex;justify-content:space-between;align-items:center;gap:8px}"
    ".sm-sym{font-size:28px;font-weight:900;letter-spacing:1px;color:var(--c,#fcee0a)!important;-webkit-text-fill-color:var(--c,#fcee0a);text-shadow:0 0 14px rgba(252,238,10,.35)}"
    ".sm-lv{font-size:12px;font-weight:800;padding:2px 10px;border:1px solid var(--c,#fcee0a);color:var(--c,#fcee0a)!important;-webkit-text-fill-color:var(--c,#fcee0a);"
    "background:rgba(252,238,10,.07)}"
    ".sm-price{display:flex;align-items:baseline;gap:10px;margin:4px 0 8px;flex-wrap:wrap}"
    ".sm-px0{font-size:22px;font-weight:800;color:#e6e9f7!important;-webkit-text-fill-color:#e6e9f7}"
    ".sm-pill{font-size:12px;font-weight:800;padding:1px 9px;border:1px solid}"
    ".sm-pill.neg{color:#ff6b86!important;-webkit-text-fill-color:#ff6b86;border-color:rgba(255,107,134,.55);background:rgba(255,77,109,.08)}"
    ".sm-pill.pos{color:#3dffa0!important;-webkit-text-fill-color:#3dffa0;border-color:rgba(61,255,160,.55);background:rgba(61,255,160,.08)}"
    ".sm-barlab{display:flex;justify-content:space-between;font-size:12px;color:#8f98bd!important;-webkit-text-fill-color:#8f98bd}"
    ".sm-barlab b{color:#ff6b86!important;-webkit-text-fill-color:#ff6b86}"
    ".sm-track{height:6px;margin:3px 0 8px;background:rgba(255,255,255,.08)}"
    ".sm-track i{display:block;height:100%;background:linear-gradient(90deg,#ff4d6d,#ff9a3d);box-shadow:0 0 10px rgba(255,77,109,.6)}"
    ".sm-tags{display:flex;flex-wrap:wrap;gap:5px;margin:2px 0 6px;align-items:flex-start;align-content:flex-start}"
    ".sm-t{font-size:11.5px;font-weight:700;padding:1px 8px;border:1px solid}"
    ".sm-t.sec{color:#7fdcff!important;-webkit-text-fill-color:#7fdcff;border-color:rgba(127,220,255,.5);background:rgba(127,220,255,.07)}"
    ".sm-t.rep{color:#d9a8ff!important;-webkit-text-fill-color:#d9a8ff;border-color:rgba(190,120,255,.55);background:rgba(190,120,255,.08)}"
    ".sm-t.ok{color:#fcee0a!important;-webkit-text-fill-color:#fcee0a;border-color:rgba(252,238,10,.6);background:rgba(252,238,10,.08)}"
    ".sm-h{margin:10px 0 3px;font-weight:800;font-size:12.5px;letter-spacing:.3px}"
    ".sm-h.g{color:#3dffa0!important;-webkit-text-fill-color:#3dffa0}.sm-h.w{color:#ffb454!important;-webkit-text-fill-color:#ffb454}"
    ".sm-h.n{color:#7fdcff!important;-webkit-text-fill-color:#7fdcff}"
    ".sm-card ul{margin:2px 0 0 16px;padding:0}.sm-card li{margin:2px 0}"
    ".sm-news{font-size:13px}.sm-news a{color:#9fe8ff!important;-webkit-text-fill-color:#9fe8ff;text-decoration:none}"
    ".hid-row{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:6px 0;border-bottom:1px dashed rgba(111,122,168,.25)}"
    ".hid-rep{min-width:60px;font-weight:900;color:#d9a8ff!important;-webkit-text-fill-color:#d9a8ff}"
    ".hid-ar{color:#6f7aa8!important;-webkit-text-fill-color:#6f7aa8}"
    ".hid-f{font-size:12px;padding:0 7px;border:1px solid rgba(170,179,214,.35);color:#aab3d6!important;-webkit-text-fill-color:#aab3d6;background:rgba(170,179,214,.06)}"
    ".ck-box{margin:6px 0 10px;border:1px solid rgba(0,240,255,.25);background:rgba(10,14,28,.6)}"
    ".ck-row{display:flex;gap:10px;align-items:baseline;padding:6px 12px;border-bottom:1px dashed rgba(111,122,168,.2);font-size:13px;"
    "color:#d6dcf2!important;-webkit-text-fill-color:#d6dcf2}"
    ".ck-row:last-child{border-bottom:none}.ck-i{width:22px}.ck-t{flex:1}.ck-d{color:#8f98bd!important;-webkit-text-fill-color:#8f98bd;font-size:12px}"
    ".rb-bad{display:inline-block;margin:2px 4px 2px 0;padding:1px 7px;font-size:11.5px;border:1px solid rgba(255,77,109,.5);"
    "color:#ff8fa3!important;-webkit-text-fill-color:#ff8fa3;background:rgba(255,77,109,.07)}"
    "</style>"
)


def _e(x):
    return _html.escape(str(x), quote=True)


# ---------------------------------------------------------------
# \u0e04\u0e13\u0e34\u0e15\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c (\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19\u0e25\u0e49\u0e27\u0e19 \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e44\u0e14\u0e49)
# ---------------------------------------------------------------
def _stats(df):
    """df: \u0e04\u0e2d\u0e25\u0e31\u0e21\u0e19\u0e4c Open High Low Close Volume (\u0e40\u0e23\u0e35\u0e22\u0e07\u0e40\u0e01\u0e48\u0e32\u2192\u0e43\u0e2b\u0e21\u0e48) \u2192 dict \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e2a\u0e41\u0e01\u0e19 \u0e2b\u0e23\u0e37\u0e2d None \u0e16\u0e49\u0e32\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e44\u0e21\u0e48\u0e1e\u0e2d"""
    df = df.dropna(subset=["Close"])
    if len(df) < 60:
        return None
    c, h, l, o, v = df["Close"], df["High"], df["Low"], df["Open"], df["Volume"]
    px = float(c.iloc[-1])
    prev = float(c.iloc[-2])
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1)
    atr = float(tr.rolling(14).mean().iloc[-1])
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
    rsi = float(100 - 100 / (1 + (up / dn.replace(0, np.nan)).iloc[-1])) if float(dn.iloc[-1]) > 0 else 100.0
    ema20 = float(c.ewm(span=20, adjust=False).mean().iloc[-1])
    ema50 = float(c.ewm(span=50, adjust=False).mean().iloc[-1])
    avg_v = float(v.iloc[-21:-1].mean()) if len(v) > 21 else 0.0
    rvol = float(v.iloc[-1]) / avg_v if avg_v > 0 else float("nan")
    hi20 = float(h.iloc[-20:].max())
    hi60 = float(h.iloc[-60:].max())
    lo10 = float(l.iloc[-10:].min())
    trend = "up" if px > ema20 > ema50 else ("down" if px < ema20 < ema50 else "side")
    lo_t, hi_t, op_t = float(l.iloc[-1]), float(h.iloc[-1]), float(o.iloc[-1])
    rng_t = hi_t - lo_t
    clpos = (px - lo_t) / rng_t if rng_t > 0 else 0.5
    wick = (min(px, op_t) - lo_t) / rng_t if rng_t > 0 else 0.0
    higher_low = lo_t >= float(l.iloc[-6:-1].min())
    reds = 0
    for k in range(2, 9):
        if float(c.iloc[-k]) < float(c.iloc[-k - 1]):
            reds += 1
        else:
            break
    rv = v / v.iloc[-21:-1].mean() if avg_v > 0 else v * 0
    spike3 = float(rv.iloc[-3:].max()) if avg_v > 0 else float("nan")
    rets = c.pct_change().tail(60).to_numpy(dtype=float)
    return {"ret": rets, "up_run": (hi20 / float(c.iloc[-60]) - 1) * 100, "clpos": clpos, "wick": wick, "higher_low": higher_low, "reds": reds, "spike3": spike3, "lo_t": lo_t,
            "stretch": (ema20 - px) / atr if atr > 0 else 0.0, "green": px > op_t, "px": px, "chg1": (px / prev - 1) * 100, "chg5": (px / float(c.iloc[-6]) - 1) * 100, "rvol": rvol, "atr": atr, "atr_pct": atr / px * 100,
            "rsi": rsi, "hi20": hi20, "hi60": hi60, "lo10": lo10, "dist_hi": (px / hi20 - 1) * 100, "trend": trend,
            "gap": (float(o.iloc[-1]) / prev - 1) * 100, "ema20": ema20, "ema50": ema50, "dvol": avg_v * px / 1e6}


def _tags(s):
    t = []
    if s["rvol"] == s["rvol"] and s["rvol"] >= 1.5:
        t.append("\U0001f525\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13")
    if s["atr_pct"] >= 5:
        t.append("\u26a0\ufe0f\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19")
    t.append({"up": "\U0001f4c8\u0e02\u0e36\u0e49\u0e19", "down": "\U0001f53b\u0e25\u0e07", "side": "\u2796\u0e41\u0e01\u0e27\u0e48\u0e07"}[s["trend"]])
    return " ".join(t)


def _rebound(s):
    """\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e41\u0e25\u0e49\u0e27\u0e40\u0e23\u0e34\u0e48\u0e21\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e40\u0e14\u0e49\u0e07\u0e01\u0e35\u0e48\u0e02\u0e49\u0e2d -> (\u0e08\u0e33\u0e19\u0e27\u0e19\u0e02\u0e49\u0e2d, [\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25], [\u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e30\u0e27\u0e31\u0e07]) \u0e2b\u0e23\u0e37\u0e2d None \u0e16\u0e49\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e1e\u0e2d
    \u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e19\u0e31\u0e1a\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e17\u0e33\u0e19\u0e32\u0e22: \u0e44\u0e21\u0e48\u0e21\u0e35\u0e43\u0e04\u0e23\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e08\u0e30\u0e40\u0e14\u0e49\u0e07\u0e08\u0e23\u0e34\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48"""
    fell = s["dist_hi"] <= -15 or s["chg5"] <= -8
    if not fell or s["rsi"] > 42:
        return None
    why = []
    if s["rsi"] <= 30:
        why.append("RSI %.0f \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 30 = \u0e02\u0e32\u0e22\u0e40\u0e01\u0e34\u0e19\u0e41\u0e23\u0e07\u0e44\u0e1b\u0e21\u0e32\u0e01" % s["rsi"])
    if s["stretch"] >= 2:
        why.append("\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e22\u0e39\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e40\u0e2a\u0e49\u0e19 EMA20 \u0e16\u0e36\u0e07 %.1f \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e41\u0e01\u0e27\u0e48\u0e07\u0e23\u0e32\u0e22\u0e27\u0e31\u0e19 (\u0e22\u0e37\u0e14\u0e40\u0e01\u0e34\u0e19\u0e1b\u0e01\u0e15\u0e34 \u0e21\u0e31\u0e01\u0e16\u0e39\u0e01\u0e14\u0e36\u0e07\u0e01\u0e25\u0e31\u0e1a)" % s["stretch"])
    if s["spike3"] == s["spike3"] and s["spike3"] >= 2:
        why.append("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e17\u0e38\u0e1a\u0e2b\u0e19\u0e31\u0e01 %.1f \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e1b\u0e01\u0e15\u0e34\u0e43\u0e19 3 \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32 (\u0e21\u0e31\u0e01\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e04\u0e19\u0e17\u0e19\u0e44\u0e21\u0e48\u0e44\u0e2b\u0e27\u0e40\u0e17\u0e02\u0e32\u0e22)" % s["spike3"])
    if s["reds"] >= 4:
        why.append("\u0e1b\u0e34\u0e14\u0e41\u0e14\u0e07\u0e15\u0e34\u0e14\u0e01\u0e31\u0e19 %d \u0e27\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e2b\u0e19\u0e49\u0e32 (\u0e02\u0e32\u0e22\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07\u0e08\u0e19\u0e41\u0e23\u0e07\u0e02\u0e32\u0e22\u0e40\u0e23\u0e34\u0e48\u0e21\u0e2b\u0e21\u0e14)" % s["reds"])
    if s["green"] and s["clpos"] >= 0.6:
        why.append("\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e41\u0e17\u0e48\u0e07\u0e40\u0e02\u0e35\u0e22\u0e27 (\u0e1b\u0e34\u0e14\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e34\u0e14) \u0e41\u0e25\u0e30\u0e1b\u0e34\u0e14\u0e41\u0e16\u0e27\u0e04\u0e23\u0e36\u0e48\u0e07\u0e1a\u0e19\u0e02\u0e2d\u0e07\u0e27\u0e31\u0e19 (\u0e1c\u0e39\u0e49\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e23\u0e31\u0e1a) \u2014 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e02\u0e36\u0e49\u0e19\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e27\u0e32\u0e19")
    if s["wick"] >= 0.4:
        why.append("\u0e41\u0e17\u0e48\u0e07\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e21\u0e35\u0e2b\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e22\u0e32\u0e27 (\u0e23\u0e32\u0e04\u0e32\u0e40\u0e04\u0e22\u0e14\u0e34\u0e48\u0e07\u0e41\u0e15\u0e48\u0e16\u0e39\u0e01\u0e14\u0e31\u0e19\u0e01\u0e25\u0e31\u0e1a\u0e02\u0e36\u0e49\u0e19\u0e21\u0e32)")
    if s["higher_low"]:
        why.append("\u0e44\u0e21\u0e48\u0e17\u0e33\u0e15\u0e48\u0e33\u0e43\u0e2b\u0e21\u0e48\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a 5 \u0e27\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19 (\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21)")
    warn = []
    if not s["green"]:
        warn.append("\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e41\u0e17\u0e48\u0e07\u0e41\u0e14\u0e07 (\u0e1b\u0e34\u0e14\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e34\u0e14) \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e22\u0e37\u0e19\u0e22\u0e31\u0e19\u0e27\u0e48\u0e32\u0e21\u0e35\u0e04\u0e19\u0e23\u0e31\u0e1a")
    if s["trend"] == "down":
        warn.append("\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e22\u0e31\u0e07\u0e25\u0e07 (\u0e23\u0e32\u0e04\u0e32 < EMA20 < EMA50) \u0e01\u0e32\u0e23\u0e40\u0e14\u0e49\u0e07\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e1e\u0e31\u0e01\u0e01\u0e48\u0e2d\u0e19\u0e25\u0e07\u0e15\u0e48\u0e2d")
    if s["atr_pct"] >= 6:
        warn.append("\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e21\u0e32\u0e01 (ATR %.1f%%) \u0e44\u0e21\u0e49\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e25\u0e47\u0e01\u0e25\u0e07" % s["atr_pct"])
    return len(why), why, warn, _chips(s)


def _chips(s):
    """\u0e1b\u0e49\u0e32\u0e22\u0e2a\u0e31\u0e49\u0e19\u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19 (\u0e43\u0e0a\u0e49\u0e1a\u0e19\u0e01\u0e32\u0e23\u0e4c\u0e14)"""
    c = []
    if s["rsi"] <= 30:
        c.append("RSI %.0f \u0e02\u0e32\u0e22\u0e40\u0e01\u0e34\u0e19" % s["rsi"])
    if s["stretch"] >= 2:
        c.append("\u0e22\u0e37\u0e14\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 EMA20")
    if s["spike3"] == s["spike3"] and s["spike3"] >= 2:
        c.append("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e17\u0e38\u0e1a %.1fx" % s["spike3"])
    if s["reds"] >= 4:
        c.append("\u0e41\u0e14\u0e07 %d \u0e27\u0e31\u0e19\u0e15\u0e34\u0e14" % s["reds"])
    if s["green"] and s["clpos"] >= 0.6:
        c.append("\u0e41\u0e17\u0e48\u0e07\u0e40\u0e02\u0e35\u0e22\u0e27\u0e1b\u0e34\u0e14\u0e04\u0e23\u0e36\u0e48\u0e07\u0e1a\u0e19")
    if s["wick"] >= 0.4:
        c.append("\u0e2b\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e22\u0e32\u0e27")
    if s["higher_low"]:
        c.append("\u0e44\u0e21\u0e48\u0e17\u0e33\u0e15\u0e48\u0e33\u0e43\u0e2b\u0e21\u0e48")
    return c


def _preset_mask(df, name):
    if name == "\u0e02\u0e36\u0e49\u0e19\u0e41\u0e23\u0e07 + \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e21\u0e32":
        return (df["\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %"] >= 3) & (df["\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x"] >= 1.5)
    if name == "\u0e22\u0e48\u0e2d\u0e43\u0e19\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e02\u0e36\u0e49\u0e19":
        return (df["_trend"] == "up") & df["RSI"].between(38, 55) & df["\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20\u0e27 %"].between(-15, -4)
    if name == "\u0e43\u0e01\u0e25\u0e49\u0e17\u0e30\u0e25\u0e38\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07":
        return (df["\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20\u0e27 %"] >= -2) & (df["_trend"] == "up") & (df["\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x"] >= 1.0)
    if name == RB_NAME:
        return df["_elig"]
    if name == "\u0e23\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e31\u0e01":
        return (df["\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %"] <= -5) | (df["5 \u0e27\u0e31\u0e19 %"] <= -12)
    return pd.Series(True, index=df.index)


def size_position(capital, risk_pct, entry, stop):
    """\u0e04\u0e33\u0e19\u0e27\u0e13\u0e02\u0e19\u0e32\u0e14\u0e44\u0e21\u0e49\u0e1d\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d (long) \u0e08\u0e32\u0e01\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22 \u2192 dict \u0e2b\u0e23\u0e37\u0e2d None \u0e16\u0e49\u0e32\u0e2d\u0e34\u0e19\u0e1e\u0e38\u0e15\u0e1c\u0e34\u0e14"""
    if capital <= 0 or risk_pct <= 0 or entry <= 0 or stop <= 0 or stop >= entry:
        return None
    risk_cash = capital * risk_pct / 100.0
    per_share = entry - stop
    want = int(math.floor(risk_cash / per_share))
    afford = int(math.floor(capital / entry))
    shares = max(0, min(want, afford))
    return {"risk_cash": risk_cash, "per_share": per_share, "want": want, "afford": afford, "shares": shares,
            "value": shares * entry, "value_pct": shares * entry / capital * 100,
            "real_risk": shares * per_share, "real_risk_pct": shares * per_share / capital * 100,
            "capped": want > afford, "stop_pct": per_share / entry * 100}


# ---------------------------------------------------------------
# \u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25
# ---------------------------------------------------------------
@st.cache_data(ttl=300, show_spinner=False)
def _scan(symbols):
    """\u0e14\u0e36\u0e07\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e38\u0e14\u0e25\u0e30 100 \u0e15\u0e31\u0e27 (\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e43\u0e2b\u0e0d\u0e48\u0e46 \u0e2d\u0e22\u0e48\u0e32\u0e07 S&P 500 \u0e08\u0e30\u0e44\u0e21\u0e48\u0e25\u0e49\u0e21\u0e17\u0e31\u0e49\u0e07\u0e01\u0e49\u0e2d\u0e19\u0e16\u0e49\u0e32\u0e1a\u0e32\u0e07\u0e0a\u0e38\u0e14\u0e1e\u0e25\u0e32\u0e14)"""
    rows = []
    syms = list(symbols)
    for i in range(0, len(syms), 100):
        chunk = syms[i:i + 100]
        try:
            d = yf.download(" ".join(chunk), period="6mo", interval="1d", group_by="ticker", progress=False, auto_adjust=True, threads=True)
        except Exception:
            continue
        for t in chunk:
            try:
                s_ = _stats(d[t][["Open", "High", "Low", "Close", "Volume"]]) if len(chunk) > 1 else _stats(d[["Open", "High", "Low", "Close", "Volume"]])
            except Exception:
                s_ = None
            if s_:
                rows.append(dict(s_, sym=t))
    return rows


@st.cache_data(ttl=300, show_spinner=False)
def _market():
    syms = ["SPY", "QQQ", "^VIX", "TLT", "GLD", "UUP"]
    try:
        d = yf.download(" ".join(syms), period="1mo", interval="1d", group_by="ticker", progress=False, auto_adjust=True)
    except Exception:
        return {}
    out = {}
    for t in syms:
        try:
            c = d[t]["Close"].dropna()
            out[t] = {"chg": float(c.iloc[-1] / c.iloc[-2] - 1) * 100, "lvl": float(c.iloc[-1]),
                      "chg5": float(c.iloc[-1] / c.iloc[-6] - 1) * 100 if len(c) >= 6 else 0.0}
        except Exception:
            pass
    return out


@st.cache_data(ttl=3600, show_spinner=False)
def _next_earn(sym):
    try:
        cal = yf.Ticker(sym).calendar
        eds = cal.get("Earnings Date") if isinstance(cal, dict) else None
        today = _dt.date.today()
        for x in (eds or []):
            dx = x.date() if hasattr(x, "date") else x
            if dx >= today:
                return dx
    except Exception:
        pass
    return None


@st.cache_data(ttl=300, show_spinner=False)
def _hist(sym):
    try:
        d = yf.download(sym, period="6mo", interval="1d", progress=False, auto_adjust=True)
        if isinstance(d.columns, pd.MultiIndex):
            d.columns = d.columns.get_level_values(0)
        return d
    except Exception:
        return None


def _fmt(x, d=2):
    return "-" if x is None or x != x else format(x, ",.%df" % d)


# ---------------------------------------------------------------
# \u0e2b\u0e19\u0e49\u0e32\u0e08\u0e2d
# ---------------------------------------------------------------
# \u0e1f\u0e35\u0e40\u0e08\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 (\u0e04\u0e35\u0e22\u0e4c\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e17\u0e31\u0e49\u0e07\u0e15\u0e2d\u0e19\u0e2a\u0e41\u0e01\u0e19\u0e2a\u0e14\u0e41\u0e25\u0e30\u0e15\u0e2d\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a) \u2014 7 \u0e02\u0e49\u0e2d\u0e41\u0e23\u0e01\u0e04\u0e37\u0e2d\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e40\u0e14\u0e34\u0e21 \u0e2a\u0e48\u0e27\u0e19\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e23\u0e34\u0e1a\u0e17\u0e17\u0e35\u0e48\u0e1c\u0e21\u0e2a\u0e07\u0e2a\u0e31\u0e22\u0e27\u0e48\u0e32\u0e2d\u0e32\u0e08\u0e0a\u0e48\u0e27\u0e22
FEATS = [("s1", "RSI \u2264 30"), ("s2", "\u0e23\u0e32\u0e04\u0e32\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 EMA20 \u2265 2 ATR"), ("s3", "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e17\u0e38\u0e1a \u2265 2 \u0e40\u0e17\u0e48\u0e32\u0e43\u0e19 3 \u0e27\u0e31\u0e19"), ("s4", "\u0e41\u0e14\u0e07\u0e15\u0e34\u0e14 \u2265 4 \u0e27\u0e31\u0e19"),
         ("s5", "\u0e41\u0e17\u0e48\u0e07\u0e40\u0e02\u0e35\u0e22\u0e27\u0e1b\u0e34\u0e14\u0e04\u0e23\u0e36\u0e48\u0e07\u0e1a\u0e19"), ("s6", "\u0e2b\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e22\u0e32\u0e27"), ("s7", "\u0e44\u0e21\u0e48\u0e17\u0e33\u0e15\u0e48\u0e33\u0e43\u0e2b\u0e21\u0e48 5 \u0e27\u0e31\u0e19"),
         ("up10", "\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e01\u0e40\u0e04\u0e22\u0e27\u0e34\u0e48\u0e07\u0e02\u0e36\u0e49\u0e19 \u2265 10%"), ("deep30", "\u0e23\u0e48\u0e27\u0e07\u0e25\u0e36\u0e01 \u2265 30% \u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07"), ("hiatr", "\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 ATR \u2265 5%"),
         ("dry", "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e1b\u0e01\u0e15\u0e34"), ("up1d", "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e23\u0e32\u0e04\u0e32\u0e1a\u0e27\u0e01\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e27\u0e32\u0e19"), ("mktdn", "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e23\u0e48\u0e27\u0e07\u0e43\u0e19 5 \u0e27\u0e31\u0e19 (S&P \u2264 -2%)")]
FEAT_LABEL = dict(FEATS)
PLAIN = {"s1": "\u0e02\u0e32\u0e22\u0e2b\u0e19\u0e31\u0e01\u0e08\u0e19\u0e16\u0e39\u0e01\u0e40\u0e01\u0e34\u0e19\u0e44\u0e1b", "s2": "\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e21\u0e32\u0e01", "s3": "\u0e21\u0e35\u0e04\u0e19\u0e40\u0e17\u0e02\u0e32\u0e22\u0e2b\u0e19\u0e31\u0e01 (\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e2a\u0e39\u0e07)", "s4": "\u0e25\u0e07\u0e15\u0e34\u0e14\u0e01\u0e31\u0e19\u0e2b\u0e25\u0e32\u0e22\u0e27\u0e31\u0e19", "s5": "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e40\u0e23\u0e34\u0e48\u0e21\u0e21\u0e35\u0e04\u0e19\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e25\u0e31\u0e1a",
         "s6": "\u0e16\u0e39\u0e01\u0e14\u0e31\u0e19\u0e01\u0e25\u0e31\u0e1a\u0e02\u0e36\u0e49\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e14\u0e34\u0e48\u0e07", "s7": "\u0e44\u0e21\u0e48\u0e17\u0e33\u0e15\u0e48\u0e33\u0e43\u0e2b\u0e21\u0e48", "up10": "\u0e40\u0e1e\u0e34\u0e48\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e32\u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e01\u0e48\u0e2d\u0e19", "deep30": "\u0e25\u0e07\u0e25\u0e36\u0e01\u0e01\u0e27\u0e48\u0e32 30% \u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07", "hiatr": "\u0e2b\u0e38\u0e49\u0e19\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07",
         "dry": "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e40\u0e1a\u0e32", "up1d": "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e23\u0e32\u0e04\u0e32\u0e1a\u0e27\u0e01", "mktdn": "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e01\u0e33\u0e25\u0e31\u0e07\u0e23\u0e48\u0e27\u0e07"}
REGIME = {"mktdn"}  # \u0e2a\u0e20\u0e32\u0e27\u0e30\u0e15\u0e25\u0e32\u0e14: \u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e43\u0e19\u0e27\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e2b\u0e38\u0e49\u0e19 \u0e41\u0e2a\u0e14\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e23\u0e34\u0e1a\u0e17\u0e04\u0e23\u0e31\u0e49\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19
_VALID_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fast_valid.json")


def _live_feats(r, spy5=None):
    """\u0e1f\u0e35\u0e40\u0e08\u0e2d\u0e23\u0e4c\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e2b\u0e19\u0e36\u0e48\u0e07\u0e15\u0e31\u0e27\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 (\u0e19\u0e34\u0e22\u0e32\u0e21\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a _bt_one)"""
    f = {"s1": r["rsi"] <= 30, "s2": r["stretch"] >= 2, "s3": bool(r["spike3"] == r["spike3"] and r["spike3"] >= 2), "s4": r["reds"] >= 4,
         "s5": bool(r["green"] and r["clpos"] >= 0.6), "s6": r["wick"] >= 0.4, "s7": bool(r["higher_low"]),
         "up10": r["up_run"] >= 10, "deep30": r["dist_hi"] <= -30, "hiatr": r["atr_pct"] >= 5,
         "dry": bool(r["rvol"] == r["rvol"] and r["rvol"] < 1), "up1d": r["chg1"] > 0,
         "mktdn": bool(spy5 is not None and spy5 <= -2)}
    return {k: bool(v) for k, v in f.items()}


def _load_valid():
    try:
        sv = st.session_state.get("fast_valid")
        if isinstance(sv, dict) and isinstance(sv.get("valid"), list):
            return sv
    except Exception:
        pass
    try:
        with open(_VALID_PATH, "r", encoding="utf-8") as fh:
            d = json.load(fh)
        if isinstance(d, dict) and isinstance(d.get("valid"), list):
            return d
    except Exception:
        pass
    return None


def _save_valid(valid, bad, n_tickers):
    try:
        with open(_VALID_PATH, "w", encoding="utf-8") as fh:
            json.dump({"date": str(_dt.date.today()), "valid": valid, "bad": bad, "tickers": n_tickers}, fh, ensure_ascii=True)
    except Exception:
        pass


def _group_read(rows):
    """\u0e2b\u0e32 "\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e19\u0e1a\u0e49\u0e32\u0e19" \u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e15\u0e31\u0e27 = 8 \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a\u0e15\u0e32\u0e21\u0e01\u0e31\u0e19\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19 60 \u0e27\u0e31\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e14\u0e39\u0e27\u0e48\u0e32\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e19\u0e1a\u0e49\u0e32\u0e19\u0e25\u0e07\u0e14\u0e49\u0e27\u0e22\u0e44\u0e2b\u0e21 (\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e01\u0e32\u0e23 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21\u0e17\u0e32\u0e07\u0e01\u0e32\u0e23)"""
    ok = [r for r in rows if r.get("ret") is not None and len(r["ret"]) == 60 and np.isfinite(r["ret"][1:]).all()]
    if len(ok) < 20:
        return {}
    M = np.vstack([r["ret"] for r in ok])[:, 1:]
    C = np.corrcoef(M)
    ch5 = np.array([r["chg5"] for r in ok])
    out = {}
    for i, r in enumerate(ok):
        cc = C[i].copy()
        cc[i] = -9
        idx = np.argsort(cc)[-8:]
        out[r["sym"]] = {"peer5": float(np.median(ch5[idx])), "peers": [ok[j]["sym"] for j in idx[::-1][:3]]}
    return out


def _earn_raw(sym):
    try:
        cal = yf.Ticker(sym).calendar
        eds = cal.get("Earnings Date") if isinstance(cal, dict) else None
        today = _dt.date.today()
        for x in (eds or []):
            dx = x.date() if hasattr(x, "date") else x
            if dx >= today:
                return dx
    except Exception:
        pass
    return None


@st.cache_data(ttl=3600 * 6, show_spinner=False)
def _earn_map(symbols):
    """\u0e27\u0e31\u0e19\u0e07\u0e1a\u0e16\u0e31\u0e14\u0e44\u0e1b\u0e02\u0e2d\u0e07\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 (\u0e14\u0e36\u0e07\u0e02\u0e19\u0e32\u0e19 8 \u0e40\u0e18\u0e23\u0e14)"""
    from concurrent.futures import ThreadPoolExecutor
    syms = list(symbols)
    try:
        with ThreadPoolExecutor(max_workers=8) as ex:
            res = list(ex.map(_earn_raw, syms))
    except Exception:
        res = [None] * len(syms)
    return dict(zip(syms, res))


def _ctx(r, grp, earn):
    """\u0e1b\u0e49\u0e32\u0e22\u0e1a\u0e23\u0e34\u0e1a\u0e17 (\u0e44\u0e21\u0e48\u0e19\u0e31\u0e1a\u0e43\u0e19\u0e04\u0e30\u0e41\u0e19\u0e19 x/7): \u0e15\u0e01\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21/\u0e15\u0e01\u0e40\u0e14\u0e35\u0e48\u0e22\u0e27 \xb7 \u0e15\u0e01\u0e08\u0e32\u0e01\u0e02\u0e32\u0e02\u0e36\u0e49\u0e19/\u0e02\u0e32\u0e25\u0e07 \xb7 \u0e07\u0e1a\u0e43\u0e01\u0e25\u0e49\u0e2d\u0e2d\u0e01 -> (\u0e14\u0e35, \u0e23\u0e30\u0e27\u0e31\u0e07)"""
    good, bad = [], []
    g = (grp or {}).get(r["sym"])
    if g:
        if g["peer5"] <= -5:
            good.append("\u0e15\u0e01\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21 (\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e19\u0e1a\u0e49\u0e32\u0e19 %+.0f%%)" % g["peer5"])
        elif g["peer5"] >= -2:
            bad.append("\u0e15\u0e01\u0e40\u0e14\u0e35\u0e48\u0e22\u0e27 (\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e19\u0e1a\u0e49\u0e32\u0e19 %+.0f%%)" % g["peer5"])
    if r.get("up_run") is not None:
        if r["up_run"] >= 10:
            good.append("\u0e15\u0e01\u0e08\u0e32\u0e01\u0e02\u0e32\u0e02\u0e36\u0e49\u0e19 (\u0e01\u0e48\u0e2d\u0e19\u0e2b\u0e19\u0e49\u0e32 %+.0f%%)" % r["up_run"])
        elif r["up_run"] < 0:
            bad.append("\u0e15\u0e01\u0e15\u0e48\u0e2d\u0e08\u0e32\u0e01\u0e02\u0e32\u0e25\u0e07\u0e40\u0e14\u0e34\u0e21")
    ed = (earn or {}).get(r["sym"])
    if ed:
        dd = (ed - _dt.date.today()).days
        if 0 <= dd <= 7:
            bad.append("\u26A0\uFE0F \u0e07\u0e1a\u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19" % dd)
    return good, bad


# ---------------------------------------------------------------
# \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07: \u0e43\u0e0a\u0e49\u0e01\u0e0e 7 \u0e02\u0e49\u0e2d\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 \u0e27\u0e31\u0e14\u0e27\u0e48\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13 \u0e23\u0e32\u0e04\u0e32\u0e44\u0e1b\u0e17\u0e32\u0e07\u0e44\u0e2b\u0e19\u0e08\u0e23\u0e34\u0e07
# ---------------------------------------------------------------
_SIG_NAMES = ["RSI \u2264 30", "\u0e22\u0e37\u0e14\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 EMA20 \u2265 2 ATR", "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e17\u0e38\u0e1a \u2265 2 \u0e40\u0e17\u0e48\u0e32\u0e43\u0e19 3 \u0e27\u0e31\u0e19", "\u0e41\u0e14\u0e07\u0e15\u0e34\u0e14 \u2265 4 \u0e27\u0e31\u0e19",
              "\u0e41\u0e17\u0e48\u0e07\u0e40\u0e02\u0e35\u0e22\u0e27\u0e1b\u0e34\u0e14\u0e04\u0e23\u0e36\u0e48\u0e07\u0e1a\u0e19", "\u0e2b\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e22\u0e32\u0e27", "\u0e44\u0e21\u0e48\u0e17\u0e33\u0e15\u0e48\u0e33\u0e43\u0e2b\u0e21\u0e48 (5 \u0e27\u0e31\u0e19)"]


def _bt_one(df, liq=0.0, spy5=None):
    """df OHLCV 1 \u0e15\u0e31\u0e27 -> DataFrame \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 "\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07" \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13 s1..s7 \u0e41\u0e25\u0e30\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32 (\u0e43\u0e0a\u0e49\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e34\u0e14\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14)"""
    df = df.dropna(subset=["Close"])
    if len(df) < 80:
        return None
    c, h, l, o, v = df["Close"], df["High"], df["Low"], df["Open"], df["Volume"]
    prev = c.shift(1)
    tr = pd.concat([h - l, (h - prev).abs(), (l - prev).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14).mean()
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
    rsi = 100 - 100 / (1 + up / dn.replace(0, np.nan))
    rsi = rsi.where(dn > 0, 100.0)
    ema20 = c.ewm(span=20, adjust=False).mean()
    dist_hi = (c / h.rolling(20).max() - 1) * 100
    chg5 = (c / c.shift(5) - 1) * 100
    avg_v = v.rolling(20).mean().shift(1)
    spike3 = (v / avg_v).rolling(3).max()
    rng = (h - l).replace(0, np.nan)
    clpos = ((c - l) / rng).fillna(0.5)
    wick = ((np.minimum(c, o) - l) / rng).fillna(0.0)
    s = pd.DataFrame(index=df.index)
    s["s1"] = rsi <= 30
    s["s2"] = ((ema20 - c) / atr) >= 2
    s["s3"] = spike3 >= 2
    s["s4"] = (d < 0).shift(1).rolling(4).sum() == 4
    s["s5"] = (c > o) & (clpos >= 0.6)
    s["s6"] = wick >= 0.4
    s["s7"] = l >= l.shift(1).rolling(5).min()
    s["up10"] = (h.rolling(20).max() / c.shift(59) - 1) * 100 >= 10
    s["deep30"] = dist_hi <= -30
    s["hiatr"] = atr / c * 100 >= 5
    s["dry"] = (v / avg_v) < 1
    s["up1d"] = c > prev
    if spy5 is not None:
        s["mktdn"] = spy5.reindex(df.index).ffill() <= -2
    else:
        s["mktdn"] = False
    elig = ((dist_hi <= -15) | (chg5 <= -8)) & (rsi <= 42) & (avg_v * c / 1e6 >= liq)
    fw = pd.concat([c.shift(-k) for k in range(1, 11)], axis=1)
    out = pd.DataFrame({"n": s[["s1", "s2", "s3", "s4", "s5", "s6", "s7"]].sum(axis=1).astype(int), "max5": fw.iloc[:, :5].max(axis=1) / c - 1, "max10": fw.max(axis=1) / c - 1,
                        "min10": fw.min(axis=1) / c - 1, "min5": fw.iloc[:, :5].min(axis=1) / c - 1, "r5": c.shift(-5) / c - 1, "r10": c.shift(-10) / c - 1}, index=df.index)
    out = pd.concat([out, s.astype(int)], axis=1)
    out["all_r5"] = out["r5"]
    ok = elig & c.shift(-10).notna() & atr.notna() & rsi.notna()
    base = out.loc[c.shift(-10).notna() & atr.notna(), "r5"]
    res = out[ok].copy()
    res.attrs["base_n"] = int(base.notna().sum())
    res.attrs["base_med"] = float(base.median()) if len(base) else float("nan")
    res.attrs["base_up"] = float((base >= 0.05).mean()) if len(base) else float("nan")
    return res


@st.cache_data(ttl=86400, show_spinner=False)
def _backtest(symbols, liq):
    frames, bn, bm, bu, k = [], [], [], [], 0
    syms = list(symbols)
    spy5 = None
    try:
        sp = yf.download("SPY", period="3y", interval="1d", progress=False, auto_adjust=True)
        if isinstance(sp.columns, pd.MultiIndex):
            sp.columns = sp.columns.get_level_values(0)
        spy5 = (sp["Close"] / sp["Close"].shift(5) - 1) * 100
    except Exception:
        spy5 = None
    for i in range(0, len(syms), 100):
        chunk = syms[i:i + 100]
        try:
            d = yf.download(" ".join(chunk), period="3y", interval="1d", group_by="ticker", progress=False, auto_adjust=True, threads=True)
        except Exception:
            continue
        for t in chunk:
            try:
                x = _bt_one(d[t][["Open", "High", "Low", "Close", "Volume"]] if len(chunk) > 1 else d[["Open", "High", "Low", "Close", "Volume"]], liq, spy5)
            except Exception:
                x = None
            if x is None:
                continue
            k += 1
            x = x.assign(sym=t)
            frames.append(x)
            bn.append(x.attrs.get("base_n", 0)); bm.append(x.attrs.get("base_med", float("nan"))); bu.append(x.attrs.get("base_up", float("nan")))
    if not frames:
        return None
    allr = pd.concat(frames)
    w = np.array(bn, dtype=float)
    ok = ~np.isnan(np.array(bu))
    base_up = float(np.average(np.array(bu)[ok], weights=w[ok])) if ok.any() and w[ok].sum() > 0 else float("nan")
    base_med = float(np.nanmedian(np.array(bm)))
    return {"rows": allr.reset_index().rename(columns={"index": "date", "Date": "date"}), "tickers": k, "base_up": base_up, "base_med": base_med}


def _bt_summary(res):
    """\u0e2a\u0e23\u0e38\u0e1b\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e32\u0e23\u0e32\u0e07\u0e15\u0e32\u0e21\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13 + \u0e15\u0e32\u0e23\u0e32\u0e07\u0e23\u0e32\u0e22\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13 + \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e2d\u0e48\u0e32\u0e19\u0e1c\u0e25 (\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19\u0e25\u0e49\u0e27\u0e19 \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e44\u0e14\u0e49)"""
    r = res["rows"]
    groups = [("0-2 \u0e02\u0e49\u0e2d (\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a)", r["n"] <= 2), ("3 \u0e02\u0e49\u0e2d", r["n"] == 3), ("4 \u0e02\u0e49\u0e2d", r["n"] == 4), ("5 \u0e02\u0e49\u0e2d", r["n"] == 5), ("6-7 \u0e02\u0e49\u0e2d", r["n"] >= 6)]

    def stat(m):
        x = r[m]
        if len(x) == 0:
            return None
        return {"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07": len(x), "\u0e08\u0e33\u0e19\u0e27\u0e19\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19": x["date"].nunique(), "\u0e02\u0e36\u0e49\u0e19 \u2265 5% \u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19": (x["max5"] >= 0.05).mean() * 100,
                "\u0e02\u0e36\u0e49\u0e19 \u2265 10% \u0e20\u0e32\u0e22\u0e43\u0e19 10 \u0e27\u0e31\u0e19": (x["max10"] >= 0.10).mean() * 100, "\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e01\u0e25\u0e32\u0e07 5 \u0e27\u0e31\u0e19": x["r5"].median() * 100,
                "\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e01\u0e25\u0e32\u0e07 10 \u0e27\u0e31\u0e19": x["r10"].median() * 100, "\u0e25\u0e07\u0e15\u0e48\u0e2d \u2265 5% \u0e20\u0e32\u0e22\u0e43\u0e19 10 \u0e27\u0e31\u0e19": (x["min10"] <= -0.05).mean() * 100}
    rows = []
    for name, m in groups:
        st_ = stat(m)
        if st_:
            rows.append(dict({"\u0e01\u0e25\u0e38\u0e48\u0e21": name}, **st_))
    tb = pd.DataFrame(rows)
    sig = []
    for i, nm in enumerate(_SIG_NAMES):
        col = "s%d" % (i + 1)
        a, b = r[r[col] == 1], r[r[col] == 0]
        if len(a) >= 30 and len(b) >= 30:
            sig.append({"\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13": nm, "\u0e08\u0e33\u0e19\u0e27\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e40\u0e08\u0e2d": len(a), "\u0e02\u0e36\u0e49\u0e19 \u2265 5% \u0e43\u0e19 5 \u0e27\u0e31\u0e19 (\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e21\u0e35)": (a["max5"] >= 0.05).mean() * 100,
                        "(\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e21\u0e35)": (b["max5"] >= 0.05).mean() * 100, "\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07 (\u0e08\u0e38\u0e14 %)": (a["max5"] >= 0.05).mean() * 100 - (b["max5"] >= 0.05).mean() * 100})
    sg = pd.DataFrame(sig)
    note = ""
    ctrl = tb[tb["\u0e01\u0e25\u0e38\u0e48\u0e21"].str.startswith("0-2")]
    hi = r[r["n"] >= 4]
    if len(ctrl) and len(hi) >= 30:
        c5 = float(ctrl["\u0e02\u0e36\u0e49\u0e19 \u2265 5% \u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19"].iloc[0])
        h5 = (hi["max5"] >= 0.05).mean() * 100
        diff = h5 - c5
        if diff >= 5:
            note = "\u0e01\u0e25\u0e38\u0e48\u0e21 4 \u0e02\u0e49\u0e2d\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e02\u0e36\u0e49\u0e19 \u2265 5%% \u0e43\u0e19 5 \u0e27\u0e31\u0e19\u0e44\u0e14\u0e49 %.0f%% \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a %.0f%% (\u0e14\u0e35\u0e01\u0e27\u0e48\u0e32 %.0f \u0e08\u0e38\u0e14) \u2014 \u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e21\u0e35\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e08\u0e23\u0e34\u0e07\u0e43\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e0a\u0e38\u0e14\u0e19\u0e35\u0e49 \u0e41\u0e15\u0e48\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e23\u0e32\u0e22\u0e15\u0e31\u0e27" % (h5, c5, diff)
        elif diff >= 2:
            note = "\u0e01\u0e25\u0e38\u0e48\u0e21 4 \u0e02\u0e49\u0e2d\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e25\u0e47\u0e01\u0e19\u0e49\u0e2d\u0e22 (%.0f%% \u0e40\u0e17\u0e35\u0e22\u0e1a %.0f%%) \u2014 \u0e0a\u0e48\u0e27\u0e22\u0e44\u0e14\u0e49\u0e19\u0e34\u0e14\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e2d\u0e22\u0e48\u0e32\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e31\u0e48\u0e19\u0e40\u0e01\u0e34\u0e19\u0e08\u0e23\u0e34\u0e07" % (h5, c5)
        else:
            note = "\u0e01\u0e25\u0e38\u0e48\u0e21 4 \u0e02\u0e49\u0e2d\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e41\u0e17\u0e1a\u0e44\u0e21\u0e48\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a (%.0f%% \u0e40\u0e17\u0e35\u0e22\u0e1a %.0f%%) \u2014 \u0e43\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e0a\u0e38\u0e14\u0e19\u0e35\u0e49 \u0e01\u0e32\u0e23\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e2b\u0e25\u0e32\u0e22\u0e02\u0e49\u0e2d\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e14\u0e35\u0e14\u0e1a\u0e48\u0e2d\u0e22\u0e02\u0e36\u0e49\u0e19 \u0e04\u0e27\u0e23\u0e25\u0e14\u0e04\u0e27\u0e32\u0e21\u0e21\u0e31\u0e48\u0e19\u0e43\u0e08\u0e15\u0e48\u0e2d\u0e04\u0e30\u0e41\u0e19\u0e19 x/7" % (h5, c5)
    return tb, sg, note


def _boot_lo(d, col, B=300, seed=7):
    """\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07 90% \u0e02\u0e2d\u0e07 "\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a" (\u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02 \u2212 \u0e44\u0e21\u0e48\u0e21\u0e35) \u0e42\u0e14\u0e22\u0e2a\u0e38\u0e48\u0e21\u0e0b\u0e49\u0e33 "\u0e17\u0e35\u0e25\u0e30\u0e27\u0e31\u0e19" (block bootstrap) \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e43\u0e19\u0e27\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e44\u0e21\u0e48\u0e2d\u0e34\u0e2a\u0e23\u0e30\u0e15\u0e48\u0e2d\u0e01\u0e31\u0e19
    \u0e43\u0e0a\u0e49\u0e15\u0e31\u0e14\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e42\u0e0a\u0e04/\u0e21\u0e32\u0e08\u0e32\u0e01\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19"""
    g = d.groupby("date")
    e = d["edge"].values
    f = d[col].values
    keys = d["date"].values
    uniq, inv = np.unique(keys, return_inverse=True)
    D = len(uniq)
    n1 = np.bincount(inv, weights=(f == 1).astype(float), minlength=D)
    s1 = np.bincount(inv, weights=e * (f == 1), minlength=D)
    n0 = np.bincount(inv, weights=(f == 0).astype(float), minlength=D)
    s0 = np.bincount(inv, weights=e * (f == 0), minlength=D)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, D, size=(B, D))
    N1, S1, N0, S0 = n1[idx].sum(1), s1[idx].sum(1), n0[idx].sum(1), s0[idx].sum(1)
    ok = (N1 > 0) & (N0 > 0)
    if ok.sum() < B * 0.8:
        return float("nan")
    lift = (S1[ok] / N1[ok] - S0[ok] / N0[ok]) * 100
    return float(np.percentile(lift, 5))


def _bt_validate(res, thr=3.0, min_n=150):
    """\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e17\u0e35\u0e25\u0e30\u0e1f\u0e35\u0e40\u0e08\u0e2d\u0e23\u0e4c 2 \u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32: \u0e0a\u0e48\u0e27\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49 (\u0e40\u0e01\u0e48\u0e32\u0e01\u0e27\u0e48\u0e32 1 \u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14) \u0e41\u0e25\u0e30\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a (1 \u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14)
    \u0e27\u0e31\u0e14\u0e14\u0e49\u0e27\u0e22 "\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a" = \u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e02\u0e36\u0e49\u0e19 \u2265 5% \u0e43\u0e19 5 \u0e27\u0e31\u0e19 \u2212 \u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e25\u0e07 \u2265 5% \u0e43\u0e19 5 \u0e27\u0e31\u0e19 (\u0e01\u0e31\u0e19\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e41\u0e04\u0e48\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e41\u0e23\u0e07)
    \u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c = \u0e40\u0e1e\u0e34\u0e48\u0e21\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a \u2265 thr \u0e08\u0e38\u0e14\u0e43\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07 \u0e40\u0e08\u0e2d\u0e21\u0e32\u0e01\u0e1e\u0e2d \u0e41\u0e25\u0e30\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07 90% (\u0e2a\u0e38\u0e48\u0e21\u0e0b\u0e49\u0e33\u0e23\u0e32\u0e22\u0e27\u0e31\u0e19) \u0e02\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32 0
    \u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21 = \u0e25\u0e14 \u2265 thr \u0e08\u0e38\u0e14\u0e43\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07 \u0e41\u0e25\u0e30\u0e02\u0e2d\u0e1a\u0e1a\u0e19\u0e02\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32 0"""
    r = res["rows"].copy()
    r["date"] = pd.to_datetime(r["date"])
    cut = r["date"].max() - pd.Timedelta(days=365)
    if len(r) < 600 or "min5" not in r.columns:
        return pd.DataFrame(), [], []
    r["edge"] = (r["max5"] >= 0.05).astype(float) - (r["min5"] <= -0.05).astype(float)
    tr, te = r[r["date"] < cut], r[r["date"] >= cut]
    if len(tr) < 300 or len(te) < 300:
        return pd.DataFrame(), [], []

    def lift(d, col):
        a, b = d[d[col] == 1], d[d[col] == 0]
        if len(a) < 30 or len(b) < 30:
            return None, len(a)
        return (a["edge"].mean() - b["edge"].mean()) * 100, len(a)
    out, valid, bad = [], [], []
    for k, lab in FEATS:
        if k not in r.columns:
            continue
        l1, n1 = lift(tr, k)
        l2, n2 = lift(te, k)
        if l1 is None or l2 is None:
            continue
        cand_v = l1 >= thr and l2 >= thr and min(n1, n2) >= min_n
        cand_b = l1 <= -thr and l2 <= -thr and min(n1, n2) >= min_n
        lo1 = lo2 = float("nan")
        st_ = "\u0e44\u0e21\u0e48\u0e0a\u0e31\u0e14"
        if cand_v:
            lo1, lo2 = _boot_lo(tr, k), _boot_lo(te, k)
            if lo1 > 0 and lo2 > 0:
                st_ = "\u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c"
                valid.append(k)
            else:
                st_ = "\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e42\u0e0a\u0e04"
        elif cand_b:
            lo1, lo2 = _boot_lo(tr, k), _boot_lo(te, k)
            hi1, hi2 = -_boot_lo(tr.assign(**{k: 1 - tr[k]}), k), -_boot_lo(te.assign(**{k: 1 - te[k]}), k)
            if hi1 < 0 and hi2 < 0:
                st_ = "\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21"
                bad.append(k)
            else:
                st_ = "\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e42\u0e0a\u0e04"
        out.append({"\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02": lab, "\u0e1c\u0e25\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49 (\u0e08\u0e38\u0e14)": l1, "\u0e1c\u0e25\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a (\u0e08\u0e38\u0e14)": l2, "\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49": lo1, "\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a": lo2,
                    "\u0e40\u0e08\u0e2d (\u0e04\u0e23\u0e31\u0e49\u0e07)": n1 + n2, "\u0e2a\u0e16\u0e32\u0e19\u0e30": st_})
    return pd.DataFrame(out), valid, bad


def _bt_verdict(res):
    """\u0e2a\u0e23\u0e38\u0e1b\u0e2a\u0e31\u0e49\u0e19\u0e2d\u0e48\u0e32\u0e19\u0e17\u0e31\u0e19\u0e17\u0e35 -> (\u0e23\u0e30\u0e14\u0e31\u0e1a, [\u0e1a\u0e23\u0e23\u0e17\u0e31\u0e14], \u0e1a\u0e17\u0e2a\u0e23\u0e38\u0e1b, \u0e15\u0e32\u0e23\u0e32\u0e07\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c, valid, bad)"""
    r = res["rows"]
    up = (r["max5"] >= 0.05).mean() * 100
    dn = (r["min10"] <= -0.05).mean() * 100
    base = res.get("base_up", float("nan")) * 100
    lines = ["\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07: \u0e02\u0e36\u0e49\u0e19 \u2265 5%% \u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19\u0e44\u0e14\u0e49 %.0f%% (\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e31\u0e48\u0e27\u0e44\u0e1b\u0e17\u0e38\u0e01\u0e27\u0e31\u0e19\u0e44\u0e14\u0e49 %.0f%%) \u0e41\u0e15\u0e48\u0e01\u0e47\u0e25\u0e07\u0e15\u0e48\u0e2d\u0e2d\u0e35\u0e01 \u2265 5%% \u0e20\u0e32\u0e22\u0e43\u0e19 10 \u0e27\u0e31\u0e19\u0e16\u0e36\u0e07 %.0f%% "
             "\u2014 \u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e41\u0e25\u0e49\u0e27\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e17\u0e32\u0e07 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e02\u0e36\u0e49\u0e19\u0e07\u0e48\u0e32\u0e22\u0e46" % (up, base, dn)]
    ctrl, hi = r[r["n"] <= 2], r[r["n"] >= 4]
    if len(ctrl) >= 30 and len(hi) >= 30:
        c5, h5 = (ctrl["max5"] >= 0.05).mean() * 100, (hi["max5"] >= 0.05).mean() * 100
        if h5 - c5 <= -3:
            lines.append("\u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e14\u0e34\u0e21 x/7: \u0e44\u0e14\u0e49 4 \u0e02\u0e49\u0e2d\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b \"\u0e14\u0e35\u0e14\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\" (%.0f%% \u0e40\u0e17\u0e35\u0e22\u0e1a %.0f%%) \u2014 \u0e08\u0e36\u0e07\u0e40\u0e25\u0e34\u0e01\u0e43\u0e0a\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a" % (h5, c5))
        elif h5 - c5 < 4:
            lines.append("\u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e14\u0e34\u0e21 x/7: \u0e44\u0e21\u0e48\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a (%.0f%% \u0e40\u0e17\u0e35\u0e22\u0e1a %.0f%%) \u2014 \u0e08\u0e36\u0e07\u0e40\u0e25\u0e34\u0e01\u0e43\u0e0a\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a" % (h5, c5))
    tb, valid, bad = _bt_validate(res)
    level = "mid"
    if len(tb):
        if valid:
            level = "good"
            lines.append("\u2605 \u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c (\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e25\u0e07\u0e08\u0e23\u0e34\u0e07\u0e17\u0e31\u0e49\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49\u0e41\u0e25\u0e30\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a): " + " \u00b7 ".join(FEAT_LABEL[k] for k in valid))
        else:
            lines.append("\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e44\u0e2b\u0e19\u0e0a\u0e48\u0e27\u0e22\u0e44\u0e14\u0e49\u0e0a\u0e31\u0e14\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32")
        if bad:
            level = "good" if valid else "bad"
            lines.append("\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07 (\u0e23\u0e30\u0e27\u0e31\u0e07): " + " \u00b7 ".join(FEAT_LABEL[k] for k in bad))
    end = {"good": "\u0e2a\u0e23\u0e38\u0e1b: \u0e2b\u0e19\u0e49\u0e32\u0e2a\u0e41\u0e01\u0e19\u0e08\u0e30\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e15\u0e32\u0e21\u0e08\u0e33\u0e19\u0e27\u0e19\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48 \"\u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\" \u0e41\u0e25\u0e30\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21 \u0e22\u0e31\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e04\u0e27\u0e32\u0e21\u0e19\u0e48\u0e32\u0e08\u0e30\u0e40\u0e1b\u0e47\u0e19 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19 \u0e27\u0e32\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07",
           "mid": "\u0e2a\u0e23\u0e38\u0e1b: \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e44\u0e14\u0e49 \u0e43\u0e0a\u0e49\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e41\u0e04\u0e48\u0e04\u0e31\u0e14\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d \"\u0e25\u0e07\u0e41\u0e23\u0e07\u0e21\u0e32\u0e41\u0e25\u0e49\u0e27\" \u0e44\u0e1b\u0e14\u0e39\u0e15\u0e48\u0e2d \u0e41\u0e25\u0e49\u0e27\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08\u0e08\u0e32\u0e01\u0e02\u0e48\u0e32\u0e27 \u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21 \u0e41\u0e25\u0e30\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19",
           "bad": "\u0e2a\u0e23\u0e38\u0e1b: \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e44\u0e14\u0e49 \u0e41\u0e25\u0e30\u0e1a\u0e32\u0e07\u0e02\u0e49\u0e2d\u0e01\u0e25\u0e31\u0e1a\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21 \u0e43\u0e0a\u0e49\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e41\u0e04\u0e48\u0e04\u0e31\u0e14\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e44\u0e1b\u0e14\u0e39\u0e15\u0e48\u0e2d \u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08\u0e08\u0e32\u0e01\u0e02\u0e48\u0e32\u0e27 \u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21 \u0e41\u0e25\u0e30\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19"}[level]
    return level, lines, end, tb, valid, bad


def _render_backtest(syms, liq, expanded=False):
    with st.expander("\U0001F9EA \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07: \u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e44\u0e2b\u0e19\u0e0a\u0e48\u0e27\u0e22\u0e08\u0e23\u0e34\u0e07? (\u0e23\u0e30\u0e1a\u0e1a\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e41\u0e25\u0e49\u0e27\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e43\u0e2b\u0e49\u0e40\u0e2d\u0e07)", expanded=expanded):
        st.markdown("\u0e23\u0e31\u0e19\u0e01\u0e31\u0e1a\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e17\u0e35\u0e48\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2d\u0e22\u0e39\u0e48 \u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 3 \u0e1b\u0e35 \u0e17\u0e14\u0e2a\u0e2d\u0e1a 13 \u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02 (7 \u0e02\u0e49\u0e2d\u0e40\u0e14\u0e34\u0e21 + 6 \u0e1a\u0e23\u0e34\u0e1a\u0e17\u0e43\u0e2b\u0e21\u0e48) \u0e41\u0e1a\u0e48\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49\u0e41\u0e25\u0e30\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a 1 \u0e1b\u0e35\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u0e41\u0e25\u0e49\u0e27\u0e40\u0e01\u0e47\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e17\u0e35\u0e48\u0e0a\u0e48\u0e27\u0e22\u0e08\u0e23\u0e34\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07 \u0e41\u0e25\u0e49\u0e27\u0e19\u0e31\u0e1a\u0e27\u0e48\u0e32\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e08\u0e2d\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13 \u0e23\u0e32\u0e04\u0e32 **\u0e02\u0e36\u0e49\u0e19 \u2265 5% \u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19** \u0e01\u0e35\u0e48\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c "
                    "\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a \"\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a\" = \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e41\u0e15\u0e48\u0e44\u0e14\u0e49\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e41\u0e04\u0e48 0-2 \u0e02\u0e49\u0e2d (\u0e16\u0e49\u0e32\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e40\u0e22\u0e2d\u0e30\u0e44\u0e21\u0e48\u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e17\u0e35\u0e22\u0e1a \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e04\u0e30\u0e41\u0e19\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e0a\u0e48\u0e27\u0e22)")
        st.caption("\u0e02\u0e49\u0e2d\u0e08\u0e33\u0e01\u0e31\u0e14\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e39\u0e49: \u0e43\u0e0a\u0e49\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 (\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e15\u0e01\u0e2b\u0e19\u0e31\u0e01\u0e41\u0e25\u0e49\u0e27\u0e44\u0e21\u0e48\u0e1f\u0e37\u0e49\u0e19\u0e08\u0e19\u0e2b\u0e25\u0e38\u0e14\u0e14\u0e31\u0e0a\u0e19\u0e35\u0e44\u0e21\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e19\u0e35\u0e49 \u0e08\u0e36\u0e07\u0e40\u0e02\u0e49\u0e32\u0e02\u0e49\u0e32\u0e07\u0e1d\u0e31\u0e48\u0e07\u0e40\u0e14\u0e49\u0e07 \u0e41\u0e25\u0e30\u0e02\u0e49\u0e2d \"\u0e23\u0e48\u0e27\u0e07\u0e25\u0e36\u0e01\" \u0e42\u0e14\u0e19\u0e1c\u0e25\u0e19\u0e35\u0e49\u0e21\u0e32\u0e01\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14) \xb7 "
                   "\u0e19\u0e31\u0e1a\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e34\u0e14\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e40\u0e01\u0e34\u0e14\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13 \xb7 \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e25\u0e32\u0e14\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14\u0e23\u0e48\u0e27\u0e07\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19\u0e08\u0e30\u0e19\u0e31\u0e1a\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27\u0e0b\u0e49\u0e33\u0e43\u0e19\u0e27\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27 (\u0e14\u0e39\u0e04\u0e2d\u0e25\u0e31\u0e21\u0e19\u0e4c \"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\") \xb7 \u0e44\u0e21\u0e48\u0e2b\u0e31\u0e01\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21 \xb7 \u0e2d\u0e14\u0e35\u0e15\u0e44\u0e21\u0e48\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e30\u0e01\u0e31\u0e19\u0e2d\u0e19\u0e32\u0e04\u0e15")
        if st.button("\u25B6 \u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 (\u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e23\u0e32\u0e27 1-3 \u0e19\u0e32\u0e17\u0e35 \u0e41\u0e25\u0e49\u0e27\u0e40\u0e01\u0e47\u0e1a\u0e41\u0e04\u0e0a 1 \u0e27\u0e31\u0e19)", key="fast_bt_run"):
            with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 3 \u0e1b\u0e35\u0e41\u0e25\u0e30\u0e17\u0e14\u0e2a\u0e2d\u0e1a %d \u0e15\u0e31\u0e27 ..." % len(syms)):
                res = _backtest(tuple(syms), float(liq))
            st.session_state["fast_bt"] = res if res else "fail"
            if res and "min5" in res["rows"].columns:
                _t, _v, _b = _bt_validate(res)
                if len(_t):
                    st.session_state["fast_valid"] = {"date": str(_dt.date.today()), "valid": _v, "bad": _b, "tickers": res["tickers"]}
                    _save_valid(_v, _b, res["tickers"])
                st.rerun()
        res = st.session_state.get("fast_bt")
        if isinstance(res, dict) and "min5" not in res["rows"].columns:
            st.info("\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e40\u0e01\u0e48\u0e32\u0e08\u0e32\u0e01\u0e40\u0e27\u0e2d\u0e23\u0e4c\u0e0a\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19 (\u0e27\u0e31\u0e14\u0e44\u0e21\u0e48\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e1e\u0e2d) \u0e01\u0e14\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e43\u0e2b\u0e21\u0e48\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e1c\u0e25\u0e16\u0e39\u0e01\u0e15\u0e49\u0e2d\u0e07")
            res = None
        if res == "fail":
            st.info("\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08 (\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49) \u0e25\u0e2d\u0e07\u0e43\u0e2b\u0e21\u0e48\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07")
        elif res:
            tb, sg, note = _bt_summary(res)
            lvl, vl, end, vt, vvalid, vbad = _bt_verdict(res)
            if len(vt):
                _save_valid(vvalid, vbad, res["tickers"])
            col = {"bad": "#ff4d6d", "mid": "#fcee0a", "good": "#3dffa0"}[lvl]
            ico = {"bad": "\U0001F534", "mid": "\U0001F7E1", "good": "\U0001F7E2"}[lvl]
            items = "".join("<li>%s</li>" % _e(x) for x in vl)
            st.markdown('<div class="fx-note" style="border-left-color:%s;background:rgba(255,255,255,.04)"><b style="font-size:15px">%s \u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 %d \u0e15\u0e31\u0e27 \xb7 %s \u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c</b>'
                        '<ul style="margin:8px 0 8px 18px">%s</ul><b>%s</b></div>' % (col, ico, res["tickers"], format(len(res["rows"]), ","), items, _e(end)), unsafe_allow_html=True)
            if not st.checkbox("\u0e41\u0e2a\u0e14\u0e07\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14 (\u0e15\u0e32\u0e23\u0e32\u0e07\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c + \u0e15\u0e32\u0e23\u0e32\u0e07\u0e15\u0e32\u0e21\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13)", value=False, key="fast_bt_detail"):
                return
            if len(vt):
                st.markdown("**\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e17\u0e35\u0e25\u0e30\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02** (\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a = \u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e02\u0e36\u0e49\u0e19 \u2265 5% \u2212 \u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e25\u0e07 \u2265 5% \u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19 \u0e40\u0e21\u0e37\u0e48\u0e2d\u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e19\u0e31\u0e49\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e44\u0e21\u0e48\u0e21\u0e35 \xb7 \u0e15\u0e49\u0e2d\u0e07\u0e40\u0e1e\u0e34\u0e48\u0e21 \u2265 3 \u0e08\u0e38\u0e14\u0e43\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07 \u0e41\u0e25\u0e30\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07 90% (\u0e2a\u0e38\u0e48\u0e21\u0e0b\u0e49\u0e33\u0e23\u0e32\u0e22\u0e27\u0e31\u0e19) \u0e15\u0e49\u0e2d\u0e07\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32 0 \u0e16\u0e36\u0e07\u0e1c\u0e48\u0e32\u0e19 \xb7 \u0e2a\u0e16\u0e32\u0e19\u0e30\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e42\u0e0a\u0e04 = \u0e14\u0e39\u0e14\u0e35\u0e41\u0e15\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e41\u0e19\u0e48\u0e19\u0e1e\u0e2d")
                try:
                    st.dataframe(vt, hide_index=True, use_container_width=True, column_config={
                        c: st.column_config.NumberColumn(c, format="%+.1f") for c in ("\u0e1c\u0e25\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49 (\u0e08\u0e38\u0e14)", "\u0e1c\u0e25\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a (\u0e08\u0e38\u0e14)", "\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49", "\u0e02\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e07\u0e17\u0e14\u0e2a\u0e2d\u0e1a")})
                except Exception:
                    st.dataframe(vt)
            st.markdown("**\u0e1c\u0e25\u0e08\u0e32\u0e01 %d \u0e15\u0e31\u0e27 \xb7 \u0e1e\u0e1a\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c \"\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\" %s \u0e04\u0e23\u0e31\u0e49\u0e07**" % (res["tickers"], format(len(res["rows"]), ",")))
            if len(tb):
                try:
                    st.dataframe(tb, hide_index=True, use_container_width=True, column_config={
                        c: st.column_config.NumberColumn(c, format="%.1f") for c in tb.columns if c not in ("\u0e01\u0e25\u0e38\u0e48\u0e21", "\u0e08\u0e33\u0e19\u0e27\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07", "\u0e08\u0e33\u0e19\u0e27\u0e19\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19")})
                except Exception:
                    st.dataframe(tb)
            if len(sg):
                st.markdown("**\u0e23\u0e32\u0e22\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13: \u0e40\u0e21\u0e37\u0e48\u0e2d\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e19\u0e35\u0e49 \u0e14\u0e35\u0e14\u0e1a\u0e48\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e15\u0e2d\u0e19\u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e35\u0e48\u0e08\u0e38\u0e14**")
                try:
                    st.dataframe(sg, hide_index=True, use_container_width=True, column_config={
                        c: st.column_config.NumberColumn(c, format="%.1f") for c in sg.columns if c not in ("\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13", "\u0e08\u0e33\u0e19\u0e27\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e40\u0e08\u0e2d")})
                except Exception:
                    st.dataframe(sg)
                st.caption("\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e15\u0e34\u0e14\u0e25\u0e1a\u0e2b\u0e23\u0e37\u0e2d\u0e43\u0e01\u0e25\u0e49 0 = \u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e19\u0e31\u0e49\u0e19\u0e44\u0e21\u0e48\u0e0a\u0e48\u0e27\u0e22\u0e43\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e0a\u0e38\u0e14\u0e19\u0e35\u0e49")
            st.caption("\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e17\u0e38\u0e01\u0e27\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27 (\u0e44\u0e21\u0e48\u0e01\u0e23\u0e2d\u0e07\u0e2d\u0e30\u0e44\u0e23): \u0e02\u0e36\u0e49\u0e19 \u2265 5%% \u0e20\u0e32\u0e22\u0e43\u0e19 5 \u0e27\u0e31\u0e19 (\u0e1b\u0e34\u0e14\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 5) = %.0f%% \xb7 \u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19\u0e01\u0e25\u0e32\u0e07 5 \u0e27\u0e31\u0e19 = %.1f%%" % (res["base_up"] * 100, res["base_med"] * 100))


def _table(show):
    try:
        st.dataframe(show, hide_index=True, use_container_width=True, column_config={
            "\u0e23\u0e32\u0e04\u0e32": st.column_config.NumberColumn("\u0e23\u0e32\u0e04\u0e32", format="%.2f"), "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %": st.column_config.NumberColumn("\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %", format="%+.2f"),
            "5 \u0e27\u0e31\u0e19 %": st.column_config.NumberColumn("5 \u0e27\u0e31\u0e19 %", format="%+.1f"), "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x": st.column_config.NumberColumn("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x \u0e1b\u0e01\u0e15\u0e34", format="%.1f"),
            "ATR %": st.column_config.NumberColumn("ATR % \u0e15\u0e48\u0e2d\u0e27\u0e31\u0e19", format="%.1f"), "RSI": st.column_config.NumberColumn("RSI", format="%.0f"),
            "\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20\u0e27 %": st.column_config.NumberColumn("\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19 %", format="%+.1f"), "Gap %": st.column_config.NumberColumn("Gap \u0e40\u0e1b\u0e34\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %", format="%+.1f"),
            "\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22/\u0e27\u0e31\u0e19 (\u0e25\u0e49\u0e32\u0e19$)": st.column_config.NumberColumn("\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22/\u0e27\u0e31\u0e19 (\u0e25\u0e49\u0e32\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c)", format="%.0f")})
    except Exception:
        st.dataframe(show)


import re as _re

_BADNEWS = _re.compile(r"(downgrad|cuts? (its |the |full-year )?(forecast|outlook|guidance|target)|\bmiss(es|ed)?\b|lawsuit|\bsued?\b|\bsues\b|(sec|doj|ftc) (probe|investigation)|investigat|\brecall|resigns?\b|steps? down|fraud|short[- ](seller|report)|layoffs?|(plunge|slump|tumble|sink)s? after (earnings|results)|guidance cut|profit warning|margins? (squeez|compress|shrink|narrow|tighten)|squeez(e|ed|es) margins?|(profit|revenue|sales|earnings) (miss|fall|falls|fell|drop|drops|decline|declines|slump|slumps))", _re.I)
_GROUPNEWS = _re.compile(r"(\boil\b|crude|tariff|\bfed\b|interest rates?|inflation|\bsector\b|sell-?off|chip ?(stocks|makers)|ai stocks|semiconductor stocks|wall street|nasdaq|s&p 500|treasury yields?)", _re.I)
_DROPW = _re.compile(r"(fall|fell|drop|slid|slide|slump|sink|sank|tumbl|plunge|sell-?off|down |lower|declin|slash|crash|rout)", _re.I)
_QUOTEPAGE = _re.compile(r"(stock price,? company overview|company overview (&|and) news|stock quote|stock price (today|history|chart)|stock chart|share price today|price,? (chart|history|quote))", _re.I)
_CLICKBAIT = _re.compile(r"(price prediction|forecast 20|should you|is it a buy|worth buying|stock analysis|\bhold\b|prediction|buy or sell|stock quote|stock forecast|shares? (sold|acquired|purchased|bought|trimmed|cut|raised|lifted|boosted|sells|buys)|(sells|buys|acquires|purchases|trims|lifts|boosts|cuts|raises|has) [0-9,]+ shares|stake (in|lowered|raised|trimmed|boosted)|position (in|lowered|raised|trimmed|boosted)|insider (sells|selling|buying|buys)|\\$[A-Z]{1,5} (stock|shares)|price target|stock price|analyst rating|undervalued|overvalued)", _re.I)


def _news_ts(v):
    """\u0e41\u0e1b\u0e25\u0e07\u0e40\u0e27\u0e25\u0e32\u0e02\u0e48\u0e32\u0e27\u0e40\u0e1b\u0e47\u0e19 datetime UTC (\u0e23\u0e31\u0e1a\u0e44\u0e14\u0e49\u0e17\u0e31\u0e49\u0e07\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 RFC822/ISO \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e27\u0e34\u0e19\u0e32\u0e17\u0e35 \u0e2b\u0e23\u0e37\u0e2d datetime) \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e04\u0e37\u0e19 None"""
    import datetime as _d
    if not v:
        return None
    try:
        if isinstance(v, _d.datetime):
            d = v
        elif isinstance(v, (int, float)):
            d = _d.datetime.fromtimestamp(float(v), _d.timezone.utc)
        else:
            from email.utils import parsedate_to_datetime
            try:
                d = parsedate_to_datetime(str(v))
            except Exception:
                d = _d.datetime.fromisoformat(str(v).replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=_d.timezone.utc)
        return d.astimezone(_d.timezone.utc)
    except Exception:
        return None


def _age_tag(ts):
    """'3 \u0e0a\u0e21.\u0e01\u0e48\u0e2d\u0e19' / '2 \u0e27\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19' (+ \u0e2a\u0e35\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e16\u0e49\u0e32\u0e40\u0e01\u0e48\u0e32\u0e40\u0e01\u0e34\u0e19 3 \u0e27\u0e31\u0e19) -> HTML \u0e40\u0e25\u0e47\u0e01\u0e46 \u0e2b\u0e23\u0e37\u0e2d\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e27\u0e48\u0e32\u0e07\u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e23\u0e39\u0e49\u0e40\u0e27\u0e25\u0e32"""
    import datetime as _d
    if ts is None:
        return ""
    sec = (_d.datetime.now(_d.timezone.utc) - ts).total_seconds()
    if sec < 0:
        sec = 0
    if sec < 3600:
        t, old = "%d \u0e19\u0e32\u0e17\u0e35\u0e01\u0e48\u0e2d\u0e19" % max(1, int(sec // 60)), False
    elif sec < 86400:
        t, old = "%d \u0e0a\u0e21.\u0e01\u0e48\u0e2d\u0e19" % int(sec // 3600), False
    else:
        n = int(sec // 86400)
        t, old = "%d \u0e27\u0e31\u0e19\u0e01\u0e48\u0e2d\u0e19" % n, n >= 3
    col = "#ff9f43" if old else "#7ee0b0"
    return ' <span style="font-size:11px;color:%s!important;-webkit-text-fill-color:%s">\u00b7 %s%s</span>' % (col, col, t, " (\u0e02\u0e48\u0e32\u0e27\u0e40\u0e01\u0e48\u0e32)" if old else "")


def _news_raw(sym):
    """\u0e02\u0e48\u0e32\u0e27\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49: \u0e43\u0e0a\u0e49\u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48 Yahoo \u0e1c\u0e39\u0e01\u0e01\u0e31\u0e1a\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19\u0e01\u0e48\u0e2d\u0e19 (\u0e15\u0e23\u0e07\u0e15\u0e31\u0e27\u0e01\u0e27\u0e48\u0e32) \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e48\u0e2d\u0e22\u0e04\u0e49\u0e19 Google News
    (\u0e23\u0e2b\u0e31\u0e2a\u0e2a\u0e31\u0e49\u0e19\u0e46 \u0e40\u0e0a\u0e48\u0e19 P \u0e2b\u0e23\u0e37\u0e2d IT \u0e04\u0e49\u0e19 Google \u0e41\u0e25\u0e49\u0e27\u0e44\u0e14\u0e49\u0e02\u0e48\u0e32\u0e27\u0e1c\u0e34\u0e14\u0e15\u0e31\u0e27 \u0e08\u0e36\u0e07\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e49 Google \u0e01\u0e31\u0e1a\u0e23\u0e2b\u0e31\u0e2a\u0e22\u0e32\u0e27 \u2264 2 \u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23)"""
    got = []
    from_g = False
    try:
        import news_radar
        got = news_radar.fetch_yfinance_news(sym, max_items=6) or []
        if not got and len(sym) >= 3:
            got = news_radar.fetch_google_news('"%s" stock when:3d' % sym, max_items=6) or []
            from_g = True
    except Exception:
        got = []
    if from_g:
        # \u0e02\u0e48\u0e32\u0e27\u0e08\u0e32\u0e01 Google \u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e08\u0e23\u0e34\u0e07\u0e46 \u0e44\u0e21\u0e48\u0e07\u0e31\u0e49\u0e19\u0e21\u0e31\u0e01\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e48\u0e32\u0e27\u0e15\u0e25\u0e32\u0e14\u0e01\u0e27\u0e49\u0e32\u0e07\u0e46 \u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49
        _pat = _re.compile(r"(?<![A-Za-z])%s(?![A-Za-z])" % _re.escape(sym))
        got = [n for n in got if _pat.search(n.get("title") or "")]
    rows, seen = [], set()
    for n in got:
        t = (n.get("title") or "").strip()
        src = n.get("source") or ""
        if " - " in t and src and t.endswith(src):
            t = t[:-(len(src) + 3)].strip()
        k = t.lower()[:60]
        if not t or k in seen or _QUOTEPAGE.search(t):
            continue  # \u0e02\u0e49\u0e32\u0e21\u0e2b\u0e19\u0e49\u0e32\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e31\u0e48\u0e27\u0e44\u0e1b (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e02\u0e48\u0e32\u0e27)
        seen.add(k)
        if src == "\u0e44\u0e21\u0e48\u0e17\u0e23\u0e32\u0e1a\u0e41\u0e2b\u0e25\u0e48\u0e07":
            src = ""
        rows.append({"title": t, "source": src, "link": n.get("link", ""),
                     "ts": _news_ts(n.get("pub_date") or n.get("published") or n.get("pubDate") or n.get("ts") or n.get("time"))})
    # \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e17\u0e35\u0e48\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22\u0e01\u0e32\u0e23\u0e15\u0e01\u0e01\u0e48\u0e2d\u0e19 (\u0e21\u0e35\u0e04\u0e33\u0e27\u0e48\u0e32\u0e23\u0e48\u0e27\u0e07/\u0e14\u0e34\u0e48\u0e07) \u0e41\u0e25\u0e30\u0e40\u0e2d\u0e32\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e40\u0e0a\u0e34\u0e07\u0e42\u0e06\u0e29\u0e13\u0e32/\u0e04\u0e32\u0e14\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e23\u0e32\u0e04\u0e32\u0e44\u0e27\u0e49\u0e17\u0e49\u0e32\u0e22
    rows.sort(key=lambda x: -((2 if _DROPW.search(x["title"]) else 0) - (3 if _CLICKBAIT.search(x["title"]) else 0)))
    return rows


@st.cache_data(ttl=1800, show_spinner=False)
def _news_map(symbols):
    """\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27 (\u0e14\u0e36\u0e07\u0e02\u0e19\u0e32\u0e19 6 \u0e40\u0e18\u0e23\u0e14 \u0e40\u0e01\u0e47\u0e1a\u0e41\u0e04\u0e0a 30 \u0e19\u0e32\u0e17\u0e35)"""
    from concurrent.futures import ThreadPoolExecutor
    syms = list(symbols)
    try:
        with ThreadPoolExecutor(max_workers=6) as ex:
            res = list(ex.map(_news_raw, syms))
    except Exception:
        res = [[] for _ in syms]
    return dict(zip(syms, res))


def _clean_titles(rows):
    out = []
    for r in rows[:3]:
        t = _re.sub(r"\((NYSE|NYSEARCA|NasdaqGS|NasdaqGM|NasdaqCM|NASDAQ|Nasdaq)[^)]*\)", " ", r["title"])
        out.append(_re.sub(r"\b(NYSE|NASDAQ|Nasdaq(GS|GM|CM)?):", " ", t))
    return out


def _cause_tag(rows, sym=None):
    """\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e08\u0e32\u0e01\u0e04\u0e33\u0e43\u0e19\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c) -> ('bad'|'group'|'', \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21)
    \u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e17\u0e35\u0e48\u0e40\u0e2d\u0e48\u0e22\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49\u0e15\u0e23\u0e07\u0e46 \u0e16\u0e37\u0e2d\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e2d\u0e07 \u0e44\u0e21\u0e48\u0e19\u0e31\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e48\u0e32\u0e27\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21"""
    txt = " | ".join(_clean_titles(rows))
    if _BADNEWS.search(txt):
        return "bad", "\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e07\u0e1a/\u0e1b\u0e23\u0e31\u0e1a\u0e25\u0e14/\u0e2a\u0e2d\u0e1a\u0e2a\u0e27\u0e19 \u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17"
    gt = []
    for raw, cl in zip(rows[:3], _clean_titles(rows)):
        if sym and _re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % _re.escape(sym), raw["title"]):
            continue
        gt.append(cl)
    if gt and _GROUPNEWS.search(" | ".join(gt)):
        return "group", "\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e1e\u0e39\u0e14\u0e16\u0e36\u0e07\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21/\u0e15\u0e25\u0e32\u0e14 \u0e19\u0e48\u0e32\u0e08\u0e30\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e2d\u0e07"
    return "", ""


_SEC_TH = {"Information Technology": "\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35", "Health Care": "\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e", "Financials": "\u0e01\u0e32\u0e23\u0e40\u0e07\u0e34\u0e19", "Consumer Discretionary": "\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e1f\u0e38\u0e48\u0e21\u0e40\u0e1f\u0e37\u0e2d\u0e22",
           "Consumer Staples": "\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19", "Industrials": "\u0e2d\u0e38\u0e15\u0e2a\u0e32\u0e2b\u0e01\u0e23\u0e23\u0e21", "Energy": "\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19", "Utilities": "\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e39\u0e1b\u0e42\u0e20\u0e04", "Materials": "\u0e27\u0e31\u0e2a\u0e14\u0e38",
           "Real Estate": "\u0e2d\u0e2a\u0e31\u0e07\u0e2b\u0e32\u0e23\u0e34\u0e21\u0e17\u0e23\u0e31\u0e1e\u0e22\u0e4c", "Communication Services": "\u0e2a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23/\u0e2d\u0e34\u0e19\u0e40\u0e17\u0e2d\u0e23\u0e4c\u0e40\u0e19\u0e47\u0e15"}


@st.cache_data(ttl=86400, show_spinner=False)
def _sector_map():
    """\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19 -> (\u0e01\u0e25\u0e38\u0e48\u0e21\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e44\u0e17\u0e22, \u0e01\u0e25\u0e38\u0e48\u0e21\u0e22\u0e48\u0e2d\u0e22\u0e2d\u0e31\u0e07\u0e01\u0e24\u0e29) \u0e08\u0e32\u0e01\u0e15\u0e32\u0e23\u0e32\u0e07 S&P 500 \u0e43\u0e19 Wikipedia \u0e17\u0e35\u0e48\u0e14\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e01\u0e47\u0e04\u0e37\u0e19 {} (\u0e1b\u0e49\u0e32\u0e22\u0e08\u0e30\u0e44\u0e21\u0e48\u0e02\u0e36\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e2a\u0e48\u0e27\u0e19\u0e2d\u0e37\u0e48\u0e19)"""
    out = {}
    try:
        import screener
        for t in screener._wiki_tables("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"):
            if "Symbol" in t.columns and "GICS Sector" in t.columns and len(t) > 400:
                sub = "GICS Sub-Industry" if "GICS Sub-Industry" in t.columns else None
                for _, r in t.iterrows():
                    sym = str(r["Symbol"]).strip().replace(".", "-")
                    sec = str(r["GICS Sector"]).strip()
                    out[sym] = (_SEC_TH.get(sec, sec), str(r[sub]).strip() if sub else "")
                break
    except Exception:
        return {}
    return out


def _th_titles(titles):
    try:
        import insight
        out = insight.tr_list(list(titles))
        return [o or t for o, t in zip(out, titles)]
    except Exception:
        return list(titles)


_HELP_MD = """
**\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e17\u0e33\u0e2d\u0e30\u0e44\u0e23**
\u0e2a\u0e41\u0e01\u0e19\u0e2b\u0e38\u0e49\u0e19 Nasdaq 100 + S&P 500 \u0e2b\u0e32\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48 *\u0e40\u0e1e\u0e34\u0e48\u0e07\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07* \u0e41\u0e25\u0e30 *\u0e2d\u0e32\u0e08\u0e40\u0e14\u0e49\u0e07\u0e01\u0e25\u0e31\u0e1a\u0e2a\u0e31\u0e49\u0e19\u0e46* \u0e20\u0e32\u0e22\u0e43\u0e19\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e27\u0e31\u0e19 \u0e41\u0e25\u0e49\u0e27\u0e04\u0e31\u0e14\u0e43\u0e2b\u0e49\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e31\u0e49\u0e19\u0e46 \u0e43\u0e2b\u0e49\u0e04\u0e38\u0e13\u0e44\u0e1b\u0e28\u0e36\u0e01\u0e29\u0e32\u0e15\u0e48\u0e2d

**\u0e23\u0e30\u0e1a\u0e1a\u0e04\u0e31\u0e14\u0e22\u0e31\u0e07\u0e44\u0e07 (3 \u0e02\u0e31\u0e49\u0e19)**
1. **\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e08\u0e23\u0e34\u0e07\u0e44\u0e2b\u0e21** \u2014 \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e21\u0e32\u0e01 \u0e2b\u0e23\u0e37\u0e2d\u0e15\u0e01 5 \u0e27\u0e31\u0e19\u0e15\u0e34\u0e14\u0e41\u0e23\u0e07 \u0e41\u0e25\u0e30\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e23\u0e49\u0e2d\u0e19\u0e41\u0e23\u0e07
2. **\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e04\u0e22\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e44\u0e2b\u0e21** \u2014 \u0e23\u0e30\u0e1a\u0e1a\u0e40\u0e2d\u0e32\u0e2b\u0e38\u0e49\u0e19 3 \u0e1b\u0e35\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e21\u0e32\u0e17\u0e14\u0e2a\u0e2d\u0e1a \u0e40\u0e01\u0e47\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e02\u0e36\u0e49\u0e19\u0e1a\u0e48\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e25\u0e07\u0e08\u0e23\u0e34\u0e07 (\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e41\u0e04\u0e48\u0e19\u0e34\u0e14\u0e2b\u0e19\u0e48\u0e2d\u0e22 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e40\u0e22\u0e2d\u0e30)
3. **\u0e21\u0e35\u0e40\u0e2b\u0e15\u0e38\u0e43\u0e2b\u0e49\u0e02\u0e49\u0e32\u0e21\u0e44\u0e2b\u0e21** \u2014 \u0e40\u0e0a\u0e48\u0e19 \u0e07\u0e1a\u0e08\u0e30\u0e2d\u0e2d\u0e01\u0e43\u0e19 7 \u0e27\u0e31\u0e19 \u0e2b\u0e23\u0e37\u0e2d\u0e02\u0e48\u0e32\u0e27\u0e14\u0e39\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e2d\u0e07 \u0e15\u0e31\u0e27\u0e1e\u0e27\u0e01\u0e19\u0e35\u0e49\u0e08\u0e30\u0e16\u0e39\u0e01\u0e41\u0e22\u0e01\u0e44\u0e27\u0e49\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07 "\u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19"

**\u0e2d\u0e48\u0e32\u0e19\u0e01\u0e32\u0e23\u0e4c\u0e14**
- \U0001F7E1 **\u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32\u0e15\u0e48\u0e2d** = \u0e1c\u0e48\u0e32\u0e19\u0e14\u0e48\u0e32\u0e19\u0e41\u0e23\u0e01 *\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e43\u0e2b\u0e49\u0e0b\u0e37\u0e49\u0e2d*
- \u2705 **\u0e17\u0e33\u0e44\u0e21\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08** = \u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49\u0e40\u0e02\u0e49\u0e32\u0e40\u0e01\u0e13\u0e11\u0e4c
- \u26A0\uFE0F **\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e30\u0e27\u0e31\u0e07** = \u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e1e\u0e25\u0e32\u0e14
- \U0001F4F0 **\u0e02\u0e48\u0e32\u0e27** = \u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e17\u0e35\u0e48\u0e04\u0e49\u0e19\u0e40\u0e08\u0e2d \u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e15\u0e01 \u0e15\u0e49\u0e2d\u0e07\u0e01\u0e14\u0e2d\u0e48\u0e32\u0e19\u0e40\u0e2d\u0e07
- **\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27** = \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e21\u0e35\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19 \u0e16\u0e39\u0e01\u0e23\u0e27\u0e21\u0e44\u0e27\u0e49\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e1a\u0e19\u0e2a\u0e38\u0e14 \u0e08\u0e30\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e2d\u0e48\u0e32\u0e19\u0e0b\u0e49\u0e33

**\u0e04\u0e33\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e07\u0e07**
- **\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07** = \u0e23\u0e32\u0e04\u0e32\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14\u0e0a\u0e48\u0e27\u0e07\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32 "\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 -40%" \u0e04\u0e37\u0e2d\u0e23\u0e32\u0e04\u0e32\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 40%
- **\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19** = \u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e44\u0e27\u0e49\u0e25\u0e48\u0e27\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e27\u0e48\u0e32\u0e16\u0e49\u0e32\u0e25\u0e07\u0e16\u0e36\u0e07\u0e15\u0e23\u0e07\u0e19\u0e35\u0e49\u0e08\u0e30\u0e02\u0e32\u0e22\u0e17\u0e31\u0e19\u0e17\u0e35 \u0e01\u0e31\u0e19\u0e40\u0e2a\u0e35\u0e22\u0e2b\u0e19\u0e31\u0e01
- **\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07** = \u0e23\u0e32\u0e04\u0e32\u0e02\u0e36\u0e49\u0e19\u0e25\u0e07\u0e27\u0e31\u0e19\u0e25\u0e30\u0e21\u0e32\u0e01\u0e46 \u0e16\u0e49\u0e32\u0e40\u0e25\u0e48\u0e19\u0e43\u0e2b\u0e49\u0e25\u0e07\u0e40\u0e07\u0e34\u0e19\u0e19\u0e49\u0e2d\u0e22\u0e25\u0e07
- **\u0e07\u0e1a** = \u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e1c\u0e25\u0e1b\u0e23\u0e30\u0e01\u0e2d\u0e1a\u0e01\u0e32\u0e23 \u0e23\u0e32\u0e04\u0e32\u0e21\u0e31\u0e01\u0e01\u0e23\u0e30\u0e42\u0e14\u0e14\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19

**\u0e04\u0e27\u0e32\u0e21\u0e08\u0e23\u0e34\u0e07\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e39\u0e49**
- \u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e17\u0e35\u0e48\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e40\u0e08\u0e2d\u0e40\u0e25\u0e47\u0e01\u0e21\u0e32\u0e01 (\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 3 \u0e08\u0e38\u0e14\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c) \u0e1c\u0e34\u0e14\u0e44\u0e14\u0e49\u0e1a\u0e48\u0e2d\u0e22
- \u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e14\u0e39\u0e14\u0e35\u0e01\u0e27\u0e48\u0e32\u0e04\u0e27\u0e32\u0e21\u0e08\u0e23\u0e34\u0e07\u0e40\u0e25\u0e47\u0e01\u0e19\u0e49\u0e2d\u0e22
- \u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49 *\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d* \u0e40\u0e1b\u0e47\u0e19\u0e41\u0e04\u0e48\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e43\u0e2b\u0e49\u0e44\u0e1b\u0e28\u0e36\u0e01\u0e29\u0e32\u0e15\u0e48\u0e2d

**\u0e27\u0e34\u0e18\u0e35\u0e43\u0e0a\u0e49\u0e17\u0e35\u0e48\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22**
1. \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e41\u0e04\u0e48 1-2 \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08
2. \u0e01\u0e14\u0e2d\u0e48\u0e32\u0e19\u0e02\u0e48\u0e32\u0e27\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e2a\u0e21\u0e2d
3. \u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e25\u0e07\u0e44\u0e1b\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e15\u0e31\u0e27\u0e19\u0e31\u0e49\u0e19\u0e43\u0e19\u0e0a\u0e48\u0e2d\u0e07 "\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19" \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e41\u0e25\u0e30\u0e04\u0e33\u0e19\u0e27\u0e13\u0e02\u0e19\u0e32\u0e14\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e04\u0e27\u0e23\u0e25\u0e07
4. \u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e0b\u0e37\u0e49\u0e2d\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07 \u0e41\u0e25\u0e30\u0e25\u0e07\u0e40\u0e07\u0e34\u0e19\u0e19\u0e49\u0e2d\u0e22\u0e46
"""


def _simple_verdict(r, grp, earn, nr, vinfo, spy5):
    """\u0e2a\u0e23\u0e38\u0e1b\u0e41\u0e1a\u0e1a\u0e04\u0e19\u0e44\u0e21\u0e48\u0e40\u0e01\u0e48\u0e07\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02 -> (\u0e23\u0e30\u0e14\u0e31\u0e1a 'skip'|'look'|'meh', [\u0e17\u0e33\u0e44\u0e21\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08], [\u0e23\u0e30\u0e27\u0e31\u0e07], \u0e04\u0e30\u0e41\u0e19\u0e19\u0e40\u0e23\u0e35\u0e22\u0e07)
    \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d: look = \u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32\u0e15\u0e48\u0e2d, skip = \u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19"""
    valid = set((vinfo or {}).get("valid", [])) - REGIME
    badk = set((vinfo or {}).get("bad", []))
    fl = _live_feats(r, spy5)
    pv = [k for k in valid if fl.get(k)]
    pb = [k for k in badk if fl.get(k)]
    cg, cb = _ctx(r, grp, earn)
    tag, tt = _cause_tag(nr, r["sym"]) if nr else ("", "")
    why, care, hard = [], [], []
    if pv:
        why.append("\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 3 \u0e1b\u0e35 \u0e2b\u0e38\u0e49\u0e19\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49 (%s) \u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e02\u0e36\u0e49\u0e19\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32\u0e25\u0e07\u0e40\u0e25\u0e47\u0e01\u0e19\u0e49\u0e2d\u0e22" % " + ".join(PLAIN.get(k, FEAT_LABEL[k]) for k in pv))
    for x in cg:
        if x.startswith("\u0e15\u0e01\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21"):
            why.append("\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a\u0e04\u0e25\u0e49\u0e32\u0e22\u0e01\u0e31\u0e19\u0e01\u0e47\u0e25\u0e07\u0e14\u0e49\u0e27\u0e22 \u0e19\u0e48\u0e32\u0e08\u0e30\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e02\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e41\u0e04\u0e48\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e19\u0e35\u0e49")
        elif x.startswith("\u0e15\u0e01\u0e08\u0e32\u0e01\u0e02\u0e32\u0e02\u0e36\u0e49\u0e19"):
            if r["dist_hi"] <= -20:
                why.append("\u0e01\u0e48\u0e2d\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e04\u0e22\u0e02\u0e36\u0e49\u0e19\u0e41\u0e23\u0e07 \u0e41\u0e15\u0e48\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e23\u0e48\u0e27\u0e07\u0e25\u0e07\u0e21\u0e32\u0e25\u0e36\u0e01\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e41\u0e04\u0e48\u0e22\u0e48\u0e2d\u0e40\u0e1a\u0e32\u0e46)")
            else:
                why.append("\u0e01\u0e48\u0e2d\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e32\u0e02\u0e36\u0e49\u0e19 \u0e40\u0e1e\u0e34\u0e48\u0e07\u0e22\u0e48\u0e2d\u0e25\u0e07\u0e21\u0e32")
    if tag == "group":
        why.append("\u0e02\u0e48\u0e32\u0e27\u0e19\u0e48\u0e32\u0e08\u0e30\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21/\u0e15\u0e25\u0e32\u0e14")
    ed = (earn or {}).get(r["sym"])
    if ed and 0 <= (ed - _dt.date.today()).days <= 7:
        hard.append("\u0e07\u0e1a\u0e08\u0e30\u0e2d\u0e2d\u0e01\u0e43\u0e19\u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19 \u0e23\u0e32\u0e04\u0e32\u0e2d\u0e32\u0e08\u0e01\u0e23\u0e30\u0e42\u0e14\u0e14\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19" % (ed - _dt.date.today()).days)
    if tag == "bad":
        hard.append("\u0e02\u0e48\u0e32\u0e27\u0e19\u0e48\u0e32\u0e08\u0e30\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e2d\u0e07 (\u0e25\u0e14\u0e40\u0e1b\u0e49\u0e32/\u0e16\u0e39\u0e01\u0e25\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a/\u0e16\u0e39\u0e01\u0e2a\u0e2d\u0e1a)")
    if pb:
        care.append("\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 \u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e21\u0e35\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30 \"%s\" \u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e1b\u0e01\u0e15\u0e34\u0e40\u0e25\u0e47\u0e01\u0e19\u0e49\u0e2d\u0e22" % " + ".join(PLAIN.get(k, FEAT_LABEL[k]) for k in pb))
    for x in cb:
        if x.startswith("\u0e15\u0e01\u0e40\u0e14\u0e35\u0e48\u0e22\u0e27"):
            care.append("\u0e15\u0e01\u0e15\u0e31\u0e27\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e19\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e44\u0e21\u0e48\u0e15\u0e01 \u0e2d\u0e32\u0e08\u0e21\u0e35\u0e02\u0e48\u0e32\u0e27\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17")
    if r["chg5"] <= -20:
        care.append("\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e21\u0e32\u0e01\u0e43\u0e19\u0e2a\u0e31\u0e1b\u0e14\u0e32\u0e2b\u0e4c\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e15\u0e23\u0e27\u0e08\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e40\u0e2d\u0e07\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32 (\u0e2d\u0e32\u0e08\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17)")
    if r["trend"] == "down":
        care.append("\u0e41\u0e19\u0e27\u0e42\u0e19\u0e49\u0e21\u0e22\u0e31\u0e07\u0e25\u0e07\u0e2d\u0e22\u0e39\u0e48 \u0e2d\u0e32\u0e08\u0e23\u0e48\u0e27\u0e07\u0e15\u0e48\u0e2d")
    if not r["green"]:
        care.append("\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e41\u0e23\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e25\u0e31\u0e1a")
    if r["atr_pct"] >= 6:
        care.append("\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07\u0e21\u0e32\u0e01 \u0e16\u0e49\u0e32\u0e40\u0e25\u0e48\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49\u0e40\u0e07\u0e34\u0e19\u0e19\u0e49\u0e2d\u0e22\u0e46")
    if hard:
        return "skip", why, hard + care, -1
    if pv or any(x.startswith("\u0e15\u0e01\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21") for x in cg):  # \u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35\u0e2b\u0e25\u0e31\u0e01\u0e10\u0e32\u0e19\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02 \u0e02\u0e48\u0e32\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e44\u0e21\u0e48\u0e1e\u0e2d
        return "look", why, care, len(pv) * 2 + (1 if tag == "group" else 0) + (1 if any(x.startswith("\u0e15\u0e01\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21") for x in cg) else 0) - 2 * len(pb)
    return "meh", why, care, 0


def _num(x):
    """\u0e41\u0e1b\u0e25\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e40\u0e09\u0e1e\u0e32\u0e30 int/float \u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 NaN \u0e19\u0e2d\u0e01\u0e19\u0e31\u0e49\u0e19\u0e04\u0e37\u0e19 None"""
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    return float(x) if x == x else None


def _health_one(sym):
    """\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e15\u0e49\u0e19\u0e08\u0e32\u0e01\u0e07\u0e1a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e43\u0e19 Yahoo -> [(warn:bool, \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21)] \u0e2d\u0e48\u0e32\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e04\u0e37\u0e19 []"""
    try:
        info = yf.Ticker(sym).info or {}
    except Exception:
        return []
    out = []
    try:
        rg, pm, de = _num(info.get("revenueGrowth")), _num(info.get("profitMargins")), _num(info.get("debtToEquity"))
        if rg is not None:
            if rg <= -0.02:
                out.append((True, "\u26A0\uFE0F \u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e2b\u0e14 %.0f%% (\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14)" % abs(rg * 100)))
            elif rg >= 0.02:
                out.append((False, "\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e42\u0e15 +%.0f%%" % (rg * 100)))
            else:
                out.append((False, "\u0e22\u0e2d\u0e14\u0e02\u0e32\u0e22\u0e19\u0e34\u0e48\u0e07"))
        if pm is not None:
            out.append((True, "\u26A0\uFE0F \u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e22\u0e31\u0e07\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19") if pm < 0 else (False, "\u0e21\u0e35\u0e01\u0e33\u0e44\u0e23"))
        if de is not None and de > 300 and info.get("sector") != "Financial Services":
            out.append((True, "\u26A0\uFE0F \u0e2b\u0e19\u0e35\u0e49\u0e2a\u0e39\u0e07 (D/E %.1f \u0e40\u0e17\u0e48\u0e32)" % (de / 100.0)))
    except Exception:
        return []
    out.sort(key=lambda x: 0 if x[0] else 1)
    return out[:3]


@st.cache_data(ttl=21600, show_spinner=False)
def _health_map(symbols):
    """\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e\u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27 (\u0e14\u0e36\u0e07\u0e02\u0e19\u0e32\u0e19 4 \u0e40\u0e18\u0e23\u0e14 \u0e40\u0e01\u0e47\u0e1a\u0e41\u0e04\u0e0a 6 \u0e0a\u0e31\u0e48\u0e27\u0e42\u0e21\u0e07)"""
    from concurrent.futures import ThreadPoolExecutor
    syms = list(symbols)
    try:
        with ThreadPoolExecutor(max_workers=4) as ex:
            res = list(ex.map(_health_one, syms))
    except Exception:
        res = [[] for _ in syms]
    return dict(zip(syms, res))


def _health_chips(items):
    """HTML \u0e02\u0e2d\u0e07\u0e1b\u0e49\u0e32\u0e22\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17: \u0e40\u0e15\u0e37\u0e2d\u0e19=\u0e2a\u0e49\u0e21 \u0e1b\u0e01\u0e15\u0e34=\u0e40\u0e17\u0e32"""
    out = ""
    for warn, txt in items or []:
        col = "#ff9f43" if warn else "#9aa4c7"
        out += ('<span title="\u0e07\u0e1a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e08\u0e32\u0e01 Yahoo (\u0e2d\u0e32\u0e08\u0e0a\u0e49\u0e32\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48\u0e04\u0e23\u0e1a) \u0e1a\u0e2d\u0e01\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07\u0e23\u0e32\u0e04\u0e32" '
                'style="display:inline-block;margin:2px 4px 0 0;padding:1px 8px;border:1px solid %s;color:%s!important;-webkit-text-fill-color:%s;font-size:11.5px;font-weight:700">%s</span>') % (col, col, col, _e(txt))
    return out


def _simple_view(view, rows, grp, earn, vinfo, spy5, hid=None):
    """\u0e42\u0e2b\u0e21\u0e14\u0e07\u0e48\u0e32\u0e22: \u0e41\u0e2a\u0e14\u0e07\u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19 5 \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48 \"\u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32\u0e15\u0e48\u0e2d\" \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e20\u0e32\u0e29\u0e32\u0e04\u0e19 \u0e41\u0e25\u0e30\u0e0b\u0e48\u0e2d\u0e19\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e04\u0e27\u0e23\u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e1e\u0e31\u0e1a"""
    by = {r["sym"]: r for r in rows}
    syms = [x for x in list(view["\u0e2b\u0e38\u0e49\u0e19"])[:24] if by.get(x) is not None and _rebound(by[x])]
    news = {}
    if syms:
        try:
            with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e41\u0e08\u0e47\u0e04\u0e2d\u0e34\u0e19\u0e02\u0e48\u0e32\u0e27\u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e15\u0e31\u0e27 ..."):
                news = _news_map(tuple(syms))
        except Exception:
            news = {}
    try:
        hmap = _health_map(tuple(syms)) if syms else {}
    except Exception:
        hmap = {}
    res = []
    for sy in syms:
        lv, why, care, sc = _simple_verdict(by[sy], grp, earn, news.get(sy) or [], vinfo, spy5)
        res.append((sy, lv, why, care, sc))
    all_looks = sorted([x for x in res if x[1] == "look"], key=lambda x: (-x[4], 0 if by[x[0]]["green"] else 1))
    looks = all_looks[:5]
    if len(all_looks) > 5 and st.checkbox("\u0e14\u0e39\u0e04\u0e23\u0e1a\u0e17\u0e31\u0e49\u0e07 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e14\u0e48\u0e32\u0e19\u0e41\u0e23\u0e01 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e41\u0e04\u0e48 5 \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01)" % len(all_looks), value=False, key="fast_more_look"):
        looks = all_looks[:12]
    skips = [x for x in res if x[1] == "skip"]
    n_all_look = len([x for x in res if x[1] == "look"])
    n_meh = len([x for x in res if x[1] == "meh"])
    n_left = len(view) - len(syms)
    st.markdown('<div class="rb-how"><b>%d \u0e15\u0e31\u0e27\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07</b> \u2192 \u0e1c\u0e48\u0e32\u0e19\u0e14\u0e48\u0e32\u0e19\u0e41\u0e23\u0e01 <b>%d \u0e15\u0e31\u0e27</b>%s \u00b7 \u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19 <b>%d \u0e15\u0e31\u0e27</b> (\u0e14\u0e39\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e1e\u0e31\u0e1a\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07) \u00b7 \u0e44\u0e21\u0e48\u0e40\u0e14\u0e48\u0e19 <b>%d \u0e15\u0e31\u0e27</b> (\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e2a\u0e14\u0e07)%s</div>' % (
        len(view), n_all_look, (" (\u0e40\u0e23\u0e35\u0e22\u0e07\u0e41\u0e25\u0e49\u0e27 \u0e42\u0e0a\u0e27\u0e4c %d \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01\u0e17\u0e35\u0e48\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14 \u0e15\u0e34\u0e4a\u0e01\u0e0a\u0e48\u0e2d\u0e07\u0e02\u0e49\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e40\u0e1e\u0e34\u0e48\u0e21)" % len(looks)) if n_all_look > len(looks) else " (\u0e41\u0e2a\u0e14\u0e07\u0e02\u0e49\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14)", len(skips), n_meh,
        (" \u00b7 \u0e2d\u0e35\u0e01 %d \u0e15\u0e31\u0e27\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19 (\u0e40\u0e01\u0e34\u0e19 24 \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01)" % n_left) if n_left > 0 else ""), unsafe_allow_html=True)
    heads = [(news.get(x[0]) or [{}])[0].get("title", "") for x in looks]
    heads2 = [((news.get(x[0]) or [{}, {}])[1:2] or [{}])[0].get("title", "") for x in looks]
    allth = _th_titles(heads + heads2) if any(heads + heads2) else heads + heads2
    ths = allth[:len(heads)]
    ths2 = allth[len(heads):]

    valid_set = set((vinfo or {}).get("valid", [])) - REGIME
    try:
        secs = _sector_map()
    except Exception:
        secs = {}
    com_w, com_c = [], []
    if len(looks) >= 3:
        com_w = [x for x in looks[0][2] if all(x in y[2] for y in looks)]
        com_c = [x for x in looks[0][3] if all(x in y[3] for y in looks)]
    if com_w or com_c:
        _cw = "".join("<li>%s</li>" % _e(x) for x in com_w)
        _cc = "".join("<li>%s</li>" % _e(x) for x in com_c)
        st.markdown('<div class="rb-how"><b>\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e02\u0e49\u0e32\u0e07\u0e25\u0e48\u0e32\u0e07</b> (\u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e2d\u0e48\u0e32\u0e19\u0e0b\u0e49\u0e33\u0e43\u0e19\u0e41\u0e15\u0e48\u0e25\u0e30\u0e43\u0e1a)'
                    + ('<br>\u2705 \u0e02\u0e49\u0e2d\u0e14\u0e35<ul>%s</ul>' % _cw if _cw else '')
                    + ('\u26A0\uFE0F \u0e02\u0e49\u0e2d\u0e23\u0e30\u0e27\u0e31\u0e07<ul>%s</ul>' % _cc if _cc else '') + '</div>', unsafe_allow_html=True)

    def card(sy, lv, why, care, th, nr, th2=""):
        r = by[sy]
        why = [x for x in why if x not in com_w]
        care = [x for x in care if x not in com_c]
        _fl = _live_feats(r, spy5)
        sc_ = secs.get(sy)
        tg = ""
        if sc_:
            _lab = sc_[0] + ((" \u00b7 " + sc_[1]) if sc_[1] else "")
            tg += '<span class="sm-t sec" title="\u0e01\u0e25\u0e38\u0e48\u0e21\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08: %s">%s</span>' % (_e(_lab), _e(_lab))
        fol = [x for x in (hid or {}).get(sy, [])]
        if fol:
            tg += '<span class="sm-t rep" title="\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e02\u0e2d\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21 \u0e0b\u0e48\u0e2d\u0e19\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e15\u0e32\u0e21\u0e01\u0e31\u0e19: %s">\U0001F465 \u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21 \u00b7 \u0e0b\u0e48\u0e2d\u0e19 %d \u0e15\u0e31\u0e27: %s%s</span>' % (
                _e(", ".join(fol)), len(fol), _e(", ".join(fol[:3])), " ..." if len(fol) > 3 else "")
        tg += "".join('<span class="sm-t ok">\u2713 %s</span>' % _e(PLAIN.get(k, FEAT_LABEL[k])) for k in FEAT_LABEL if k in valid_set and _fl.get(k))
        tg += _health_chips(hmap.get(sy))
        col = {"look": "#fcee0a", "skip": "#ff4d6d"}[lv]
        ico = {"look": "\U0001F7E1 \u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32\u0e15\u0e48\u0e2d", "skip": "\U0001F534 \u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19"}[lv]
        w = "".join("<li>%s</li>" % _e(x) for x in why[:3]) or ("<li>\u0e14\u0e39\u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19</li>" if com_w else "<li>\u2014</li>")
        c = "".join("<li>%s</li>" % _e(x) for x in care[:3]) or ("<li>\u0e14\u0e39\u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19\u0e17\u0e38\u0e01\u0e15\u0e31\u0e27\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19</li>" if com_c else "<li>\u2014</li>")
        if nr:
            nl = '<a href="%s" target="_blank">%s</a>%s' % (_e(nr[0]["link"]), _e(th or nr[0]["title"]), _age_tag(nr[0].get("ts")))
            if len(nr) > 1 and th2:
                nl += '<br><a href="%s" target="_blank">%s</a>%s' % (_e(nr[1]["link"]), _e(th2), _age_tag(nr[1].get("ts")))
        else:
            nl = '\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49 \xb7 <a href="https://www.google.com/search?q=%s+stock+news&tbm=nws" target="_blank">\u0e25\u0e2d\u0e07\u0e04\u0e49\u0e19\u0e40\u0e2d\u0e07</a>' % _e(sy)
        bw = min(abs(r["dist_hi"]) / 60.0 * 100.0, 100.0)
        return ('<div class="sm-card" style="--c:%s"><div class="sm-top"><span class="sm-sym">%s</span><span class="sm-lv">%s</span></div>'
                '<div class="sm-price"><span class="sm-px0">%s</span><span class="sm-pill %s">5 \u0e27\u0e31\u0e19 %+.1f%%</span></div>'
                '<div class="sm-bar"><div class="sm-barlab"><span>\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19</span><b>%+.0f%%</b></div><div class="sm-track"><i style="width:%.0f%%"></i></div></div>'
                '<div class="sm-tags">%s</div>'
                '<div class="sm-sec"><div class="sm-h g">\u2705 \u0e17\u0e33\u0e44\u0e21\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08</div><ul>%s</ul></div><div class="sm-sec"><div class="sm-h w">\u26A0\uFE0F \u0e15\u0e49\u0e2d\u0e07\u0e23\u0e30\u0e27\u0e31\u0e07</div><ul>%s</ul></div>'
                '<div class="sm-sec"><div class="sm-h n">\U0001F4F0 \u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48\u0e04\u0e49\u0e19\u0e40\u0e08\u0e2d <span style="font-weight:400;opacity:.75">(\u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e02\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e15\u0e01 \u0e2d\u0e48\u0e32\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08)</span></div><div class="sm-news">%s</div></div></div>' % (
                    col, _e(sy), ico, _fmt(r["px"]), "pos" if r["chg5"] >= 0 else "neg", r["chg5"], r["dist_hi"], bw, tg, w, c, nl))
    if looks:
        st.markdown('<div class="sm-grid">' + "".join(card(sy, lv, w, c, t, news.get(sy) or [], t2) for (sy, lv, w, c, _s), t, t2 in zip(looks, ths, ths2)) + "</div>", unsafe_allow_html=True)
        st.caption("\U0001F7E1 = \u0e1c\u0e48\u0e32\u0e19\u0e14\u0e48\u0e32\u0e19\u0e41\u0e23\u0e01 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d \u0e15\u0e49\u0e2d\u0e07\u0e2d\u0e48\u0e32\u0e19\u0e02\u0e48\u0e32\u0e27\u0e01\u0e48\u0e2d\u0e19\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07 \xb7 \u0e1b\u0e49\u0e32\u0e22\u0e17\u0e2d\u0e07 \u2713 = \u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 \xb7 \u0e1f\u0e49\u0e32 = \u0e01\u0e25\u0e38\u0e48\u0e21\u0e18\u0e38\u0e23\u0e01\u0e34\u0e08 \xb7 \u0e21\u0e48\u0e27\u0e07 = \u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21 (\u0e0b\u0e48\u0e2d\u0e19\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e15\u0e32\u0e21\u0e01\u0e31\u0e19) \xb7 \u0e16\u0e49\u0e32\u0e2a\u0e19\u0e43\u0e08\u0e15\u0e31\u0e27\u0e44\u0e2b\u0e19 \u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e25\u0e07\u0e44\u0e1b\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e15\u0e31\u0e27\u0e19\u0e31\u0e49\u0e19\u0e43\u0e19\u0e0a\u0e48\u0e2d\u0e07 \"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\" \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e41\u0e25\u0e30\u0e04\u0e33\u0e19\u0e27\u0e13\u0e02\u0e19\u0e32\u0e14\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e04\u0e27\u0e23\u0e25\u0e07")
    else:
        st.info("\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e14\u0e48\u0e32\u0e19\u0e41\u0e23\u0e01\u0e0a\u0e31\u0e14\u0e40\u0e08\u0e19 \u0e44\u0e21\u0e48\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e47\u0e44\u0e21\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e23 \u0e15\u0e25\u0e32\u0e14\u0e21\u0e35\u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e43\u0e2b\u0e21\u0e48\u0e17\u0e38\u0e01\u0e27\u0e31\u0e19" + ("" if vinfo else " (\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 \u0e01\u0e14\u0e23\u0e31\u0e19\u0e17\u0e35\u0e48\u0e01\u0e25\u0e48\u0e2d\u0e07 \U0001F9EA \u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07 \u0e23\u0e30\u0e1a\u0e1a\u0e08\u0e30\u0e04\u0e31\u0e14\u0e44\u0e14\u0e49\u0e15\u0e23\u0e07\u0e02\u0e36\u0e49\u0e19)"))
    if skips:
        with st.expander("\U0001F534 \u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19 (%d \u0e15\u0e31\u0e27): %s \u2014 \u0e01\u0e14\u0e14\u0e39\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25" % (len(skips), ", ".join(x[0] for x in skips[:8])), expanded=False):
            for sy, lv, w, c, _s in skips[:15]:
                st.markdown("**%s** \u2014 %s" % (sy, " \xb7 ".join(c[:2])))


def _cards(view, rows, grp=None, earn=None, vinfo=None, spy5=None):
    """\u0e01\u0e32\u0e23\u0e4c\u0e14\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07\u0e41\u0e23\u0e07: \u0e2b\u0e31\u0e27\u0e01\u0e32\u0e23\u0e4c\u0e14 -> \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e2a\u0e33\u0e04\u0e31\u0e0d -> \u2605 \u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c -> \u0e17\u0e33\u0e44\u0e21\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08 -> \u0e23\u0e30\u0e27\u0e31\u0e07 -> \u0e02\u0e48\u0e32\u0e27\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 -> \u0e02\u0e49\u0e2d\u0e2a\u0e31\u0e07\u0e40\u0e01\u0e15\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04 (\u0e40\u0e17\u0e32)"""
    by = {r["sym"]: r for r in rows}
    valid = set((vinfo or {}).get("valid", [])) - REGIME
    badk = set((vinfo or {}).get("bad", []))
    syms = [x for x in list(view["\u0e2b\u0e38\u0e49\u0e19"])[:24] if by.get(x) is not None and _rebound(by[x])]
    news = {}
    if syms:
        try:
            with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e41\u0e08\u0e47\u0e04\u0e2d\u0e34\u0e19\u0e02\u0e48\u0e32\u0e27\u0e02\u0e2d\u0e07\u0e41\u0e15\u0e48\u0e25\u0e30\u0e15\u0e31\u0e27 ..."):
                news = _news_map(tuple(syms[:24]))
        except Exception:
            news = {}
    heads = [(news.get(x) or [{}])[0].get("title", "") for x in syms]
    ths = dict(zip(syms, _th_titles(heads))) if any(heads) else {}
    out = []
    for sym in syms:
        r = by[sym]
        n, _w, warn, chips = _rebound(r)
        fl = _live_feats(r, spy5)
        pv = [k for k in valid if fl.get(k)]
        pb = [k for k in badk if fl.get(k)]
        cc = "rb-pos" if r["chg1"] >= 0 else "rb-neg"
        c5 = "rb-pos" if r["chg5"] >= 0 else "rb-neg"
        gold = "".join('<span class="rb-gold">\u2605 %s</span>' % _e(FEAT_LABEL[k]) for k in pv) or '<span class="rb-mut">\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c</span>'
        ws = []
        if not r["green"]:
            ws.append("\u0e41\u0e17\u0e48\u0e07\u0e41\u0e14\u0e07\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49")
        if r["trend"] == "down":
            ws.append("\u0e40\u0e17\u0e23\u0e19\u0e14\u0e4c\u0e22\u0e31\u0e07\u0e25\u0e07")
        if r["atr_pct"] >= 6:
            ws.append("\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e2a\u0e39\u0e07")
        cg, cb = _ctx(r, grp, earn)
        nr = news.get(sym) or []
        tag, tagtxt = _cause_tag(nr, sym) if nr else ("", "")
        good = "".join('<span class="rb-chip">%s</span>' % _e(x) for x in cg)
        if tag == "group":
            good += '<span class="rb-chip">%s</span>' % _e("\U0001F4F0 " + tagtxt)
        bad = "".join('<span class="rb-bad">%s</span>' % _e(x) for x in ws + cb)
        bad += "".join('<span class="rb-bad">\u26A0 \u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21: %s</span>' % _e(FEAT_LABEL[k]) for k in pb)
        if tag == "bad":
            bad += '<span class="rb-bad">\U0001F4F0 %s</span>' % _e(tagtxt)
        if nr:
            nl = '<a href="%s" target="_blank">%s</a> <span class="rb-mut">%s</span>' % (_e(nr[0]["link"]), _e(ths.get(sym) or nr[0]["title"]), ("\u00b7 " + _e(nr[0]["source"])) if nr[0]["source"] else "")
        else:
            nl = '<span class="rb-mut">\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u0e2b\u0e23\u0e37\u0e2d\u0e14\u0e36\u0e07\u0e02\u0e48\u0e32\u0e27\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \xb7 </span><a href="https://www.google.com/search?q=%s+stock+news&tbm=nws" target="_blank">\u0e04\u0e49\u0e19\u0e02\u0e48\u0e32\u0e27</a>' % _e(sym)
        head = ('\u2605 \u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c %d/%d \u0e02\u0e49\u0e2d' % (len(pv), len(valid))) if valid else "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c (\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19)"
        obs = " \u00b7 ".join(chips)
        out.append(
            '<div class="rb-card%s">'
            '<div class="rb-top"><span class="rb-sym">%s</span><span class="rb-px">%s <b class="%s">%+.1f%%</b></span></div>'
            '<div class="rb-sub">5 \u0e27\u0e31\u0e19 <b class="%s">%+.1f%%</b> \u00b7 \u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 <b class="rb-neg">%+.0f%%</b> \u00b7 RSI <b>%.0f</b> \u00b7 \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 <b>%.1fx</b></div>'
            '<div class="rb-sec">%s</div><div>%s</div>'
            '<div class="rb-sec">\u0e17\u0e33\u0e44\u0e21\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08</div><div>%s</div>'
            '<div class="rb-sec">\u0e23\u0e30\u0e27\u0e31\u0e07</div><div>%s</div>'
            '<div class="rb-sec">\u0e02\u0e48\u0e32\u0e27\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14</div><div class="rb-news">%s</div>'
            '<div class="rb-obsline">\u0e02\u0e49\u0e2d\u0e2a\u0e31\u0e07\u0e40\u0e01\u0e15\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04 (\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e0a\u0e48\u0e27\u0e22\u0e17\u0e33\u0e19\u0e32\u0e22): %s</div></div>' % (
                " hot" if len(pv) >= 2 else "", _e(sym), _fmt(r["px"]), cc, r["chg1"], c5, r["chg5"], r["dist_hi"], r["rsi"],
                r["rvol"] if r["rvol"] == r["rvol"] else 0, _e(head), gold,
                good or '<span class="rb-mut">\u2014</span>', bad or '<span class="rb-mut">\u2014</span>', nl, _e(obs) or "\u2014"))
    if out:
        st.markdown('<div class="rb-grid">' + "".join(out) + "</div>", unsafe_allow_html=True)
        st.caption("\u2605 \u0e17\u0e2d\u0e07 = \u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e0a\u0e48\u0e27\u0e22\u0e08\u0e23\u0e34\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e0a\u0e48\u0e27\u0e07\u0e40\u0e27\u0e25\u0e32 (\u0e40\u0e23\u0e35\u0e22\u0e07\u0e01\u0e32\u0e23\u0e4c\u0e14\u0e15\u0e32\u0e21\u0e08\u0e33\u0e19\u0e27\u0e19\u0e19\u0e35\u0e49) \xb7 \u0e40\u0e02\u0e35\u0e22\u0e27 = \u0e1a\u0e23\u0e34\u0e1a\u0e17\u0e17\u0e35\u0e48\u0e19\u0e48\u0e32\u0e08\u0e30\u0e14\u0e35 \xb7 \u0e41\u0e14\u0e07 = \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e23\u0e23\u0e30\u0e27\u0e31\u0e07 (\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e19\u0e2d\u0e01\u0e08\u0e32\u0e01 \u2605 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c) \xb7 "
                   "\u0e02\u0e48\u0e32\u0e27\u0e08\u0e31\u0e1a\u0e04\u0e33\u0e08\u0e32\u0e01\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e32\u0e23\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c \u0e2d\u0e48\u0e32\u0e19\u0e02\u0e48\u0e32\u0e27\u0e08\u0e23\u0e34\u0e07\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32\u0e40\u0e2a\u0e21\u0e2d \xb7 \u0e41\u0e2a\u0e14\u0e07\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 24 \u0e15\u0e31\u0e27 \u0e14\u0e39\u0e04\u0e23\u0e1a\u0e43\u0e19\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e15\u0e47\u0e21")
    else:
        st.info("\u0e44\u0e21\u0e48\u0e21\u0e35\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e25\u0e2d\u0e07\u0e1b\u0e34\u0e14\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07 ATR \u0e2b\u0e23\u0e37\u0e2d\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07\u0e07\u0e1a")


_JR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fast_journal.csv")
_JR_COLS = ["id", "open_date", "sym", "entry", "stop", "shares", "note", "exit", "close_date"]


def _jr_load():
    try:
        d = pd.read_csv(_JR_PATH, encoding="utf-8")
        for c in _JR_COLS:
            if c not in d.columns:
                d[c] = np.nan
        return d[_JR_COLS]
    except Exception:
        return pd.DataFrame(columns=_JR_COLS)


def _jr_save(d):
    try:
        d.to_csv(_JR_PATH, index=False, encoding="utf-8")
        return True
    except Exception:
        return False


def _jr_stats(d):
    """\u0e2a\u0e16\u0e34\u0e15\u0e34\u0e02\u0e2d\u0e07\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e1b\u0e34\u0e14\u0e41\u0e25\u0e49\u0e27: \u0e08\u0e33\u0e19\u0e27\u0e19 \xb7 \u0e0a\u0e19\u0e30 % \xb7 R \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 \xb7 R \u0e23\u0e27\u0e21 (R = \u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 \u00f7 \u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19)"""
    c = d[d["exit"].notna()].copy()
    if not len(c):
        return None
    risk = (c["entry"] - c["stop"]).replace(0, np.nan)
    c["R"] = (c["exit"] - c["entry"]) / risk
    c["pnl"] = (c["exit"] - c["entry"]) * c["shares"]
    return {"n": len(c), "win": float((c["R"] > 0).mean() * 100), "avgR": float(c["R"].mean()), "sumR": float(c["R"].sum()), "pnl": float(c["pnl"].sum()), "tbl": c}


def _render_checklist(sel, r, ed, news_rows, vinfo, spy5, vix, rr20, key):
    """\u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32: \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e23\u0e30\u0e1a\u0e1a\u0e40\u0e0a\u0e47\u0e01\u0e40\u0e2d\u0e07\u0e44\u0e14\u0e49\u0e1c\u0e48\u0e32\u0e19/\u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e0a\u0e31\u0e14 + \u0e02\u0e49\u0e2d\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e34\u0e4a\u0e01\u0e40\u0e2d\u0e07 \u0e44\u0e21\u0e48\u0e41\u0e19\u0e30\u0e19\u0e33\u0e43\u0e2b\u0e49\u0e0b\u0e37\u0e49\u0e2d\u0e2b\u0e23\u0e37\u0e2d\u0e02\u0e32\u0e22"""
    items = []
    if ed:
        dd = (ed - _dt.date.today()).days
        items.append(("ok" if dd > 7 else "no", "\u0e07\u0e1a\u0e44\u0e21\u0e48\u0e2d\u0e2d\u0e01\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19", "\u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19" % dd))
    else:
        items.append(("warn", "\u0e07\u0e1a\u0e44\u0e21\u0e48\u0e2d\u0e2d\u0e01\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19", "\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a \u0e40\u0e0a\u0e47\u0e01\u0e40\u0e2d\u0e07"))
    tag, tt = _cause_tag(news_rows, sel) if news_rows else ("", "")
    if tag == "bad":
        items.append(("no", "\u0e02\u0e48\u0e32\u0e27\u0e44\u0e21\u0e48\u0e0a\u0e35\u0e49\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17", tt))
    elif tag == "group":
        items.append(("ok", "\u0e02\u0e48\u0e32\u0e27\u0e44\u0e21\u0e48\u0e0a\u0e35\u0e49\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17", tt))
    else:
        items.append(("warn", "\u0e02\u0e48\u0e32\u0e27\u0e44\u0e21\u0e48\u0e0a\u0e35\u0e49\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17", "\u0e23\u0e30\u0e1a\u0e1a\u0e44\u0e21\u0e48\u0e41\u0e19\u0e48\u0e43\u0e08 \u0e15\u0e49\u0e2d\u0e07\u0e2d\u0e48\u0e32\u0e19\u0e02\u0e48\u0e32\u0e27\u0e40\u0e2d\u0e07"))
    valid = set((vinfo or {}).get("valid", [])) - REGIME
    badk = set((vinfo or {}).get("bad", []))
    fl = _live_feats(r, spy5)
    if vinfo:
        pb = [FEAT_LABEL[k] for k in badk if fl.get(k)]
        items.append(("no" if pb else "ok", "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21", ", ".join(pb) if pb else "\u0e44\u0e21\u0e48\u0e1e\u0e1a"))
        pv = [FEAT_LABEL[k] for k in valid if fl.get(k)]
        items.append(("ok" if pv else "no", "\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e04\u0e22\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a", ", ".join(pv) if pv else "\u0e44\u0e21\u0e48\u0e21\u0e35"))
    else:
        items.append(("warn", "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e17\u0e35\u0e48\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21", "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07"))
        items.append(("warn", "\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e04\u0e22\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a", "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07"))
    if rr20 is not None:
        items.append(("ok" if rr20 >= 2 else "no", "\u0e23\u0e32\u0e04\u0e32\u0e44\u0e1b\u0e16\u0e36\u0e07\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19\u0e44\u0e14\u0e49\u0e1c\u0e25\u0e15\u0e2d\u0e1a\u0e41\u0e17\u0e19 \u2265 2 \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22", "R/R \u2248 %.1f : 1" % rr20))
    if vix is not None:
        items.append(("ok" if vix < 25 else "warn", "\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e44\u0e21\u0e48\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27 (VIX < 25)", "VIX %.1f%s" % (vix, "" if vix < 25 else " \u2014 \u0e25\u0e14\u0e02\u0e19\u0e32\u0e14\u0e44\u0e21\u0e49")))
    ico = {"ok": "\u2705", "no": "\u274C", "warn": "\u26A0\uFE0F"}
    rows = "".join('<div class="ck-row"><span class="ck-i">%s</span><span class="ck-t">%s</span><span class="ck-d">%s</span></div>' % (ico[k], _e(a), _e(b)) for k, a, b in items)
    n_ok = sum(1 for k, _a, _b in items if k == "ok")
    n_no = sum(1 for k, _a, _b in items if k == "no")
    st.markdown('<div class="fx-note"><b>\u2611 \u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32 %s</b> \u2014 \u0e23\u0e30\u0e1a\u0e1a\u0e40\u0e0a\u0e47\u0e01\u0e43\u0e2b\u0e49 %d \u0e02\u0e49\u0e2d: \u0e1c\u0e48\u0e32\u0e19 %d \xb7 \u0e44\u0e21\u0e48\u0e1c\u0e48\u0e32\u0e19 %d \xb7 \u0e44\u0e21\u0e48\u0e41\u0e19\u0e48\u0e43\u0e08 %d%s</div><div class="ck-box">%s</div>' % (
        _e(sel), len(items), n_ok, n_no, len(items) - n_ok - n_no,
        (" \u2014 <b>\u0e21\u0e35 \u274C \u0e43\u0e2b\u0e49\u0e02\u0e49\u0e32\u0e21\u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19</b>" if n_no else ""), rows), unsafe_allow_html=True)
    m1 = st.checkbox("\u0e1c\u0e21\u0e2d\u0e48\u0e32\u0e19\u0e02\u0e48\u0e32\u0e27\u0e15\u0e49\u0e19\u0e09\u0e1a\u0e31\u0e1a\u0e41\u0e25\u0e49\u0e27 \u0e41\u0e25\u0e30\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e17\u0e33\u0e44\u0e21\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e19\u0e35\u0e49\u0e15\u0e01", key="ck1_" + key)
    m2 = st.checkbox("\u0e1c\u0e21\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e16\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e31\u0e27\u0e2d\u0e37\u0e48\u0e19\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19\u0e2d\u0e22\u0e39\u0e48 (\u0e44\u0e21\u0e48\u0e27\u0e32\u0e07\u0e40\u0e14\u0e34\u0e21\u0e1e\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e0b\u0e49\u0e33)", key="ck2_" + key)
    m3 = st.checkbox("\u0e1c\u0e21\u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e41\u0e25\u0e30\u0e40\u0e27\u0e25\u0e32\u0e2d\u0e2d\u0e01 (\u0e20\u0e32\u0e22\u0e43\u0e19 5-10 \u0e27\u0e31\u0e19) \u0e44\u0e27\u0e49\u0e01\u0e48\u0e2d\u0e19\u0e0b\u0e37\u0e49\u0e2d\u0e41\u0e25\u0e49\u0e27", key="ck3_" + key)
    if n_no == 0 and m1 and m2 and m3:
        st.caption("\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e04\u0e23\u0e1a \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e04\u0e27\u0e23\u0e0b\u0e37\u0e49\u0e2d \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e2b\u0e49\u0e32\u0e21\u0e17\u0e35\u0e48\u0e23\u0e30\u0e1a\u0e1a\u0e21\u0e2d\u0e07\u0e40\u0e2b\u0e47\u0e19 \u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e43\u0e08\u0e14\u0e49\u0e27\u0e22\u0e15\u0e31\u0e27\u0e04\u0e38\u0e13\u0e40\u0e2d\u0e07 \u0e41\u0e25\u0e30\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e44\u0e14\u0e49\u0e44\u0e21\u0e48\u0e40\u0e01\u0e34\u0e19\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e44\u0e27\u0e49")


def _render_journal(sel, plan):
    """\u0e2a\u0e21\u0e38\u0e14\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e21\u0e49: \u0e40\u0e01\u0e47\u0e1a\u0e25\u0e07\u0e44\u0e1f\u0e25\u0e4c fast_journal.csv \u0e02\u0e49\u0e32\u0e07\u0e41\u0e2d\u0e1b \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1c\u0e25\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e01\u0e31\u0e1a\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07"""
    d = _jr_load()
    with st.expander("\U0001F4D2 \u0e2a\u0e21\u0e38\u0e14\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e21\u0e49\u0e02\u0e2d\u0e07\u0e09\u0e31\u0e19 (\u0e40\u0e01\u0e47\u0e1a\u0e1c\u0e25\u0e08\u0e23\u0e34\u0e07 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e27\u0e48\u0e32\u0e23\u0e30\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49\u0e01\u0e31\u0e1a\u0e40\u0e07\u0e34\u0e19\u0e04\u0e38\u0e13\u0e44\u0e2b\u0e21)", expanded=False):
        with st.form("fast_jr_form", clear_on_submit=False):
            a, b, c_, e_ = st.columns(4)
            sy = a.text_input("\u0e2b\u0e38\u0e49\u0e19", value=sel).strip().upper()
            en = b.number_input("\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32", min_value=0.0, value=float(plan["entry"]) if plan else 0.0, step=0.1)
            sp = c_.number_input("\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19", min_value=0.0, value=float(plan["stop"]) if plan else 0.0, step=0.1)
            sh = e_.number_input("\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19", min_value=0, value=int(plan["shares"]) if plan else 0, step=1)
            nt = st.text_input("\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e40\u0e02\u0e49\u0e32 (\u0e2a\u0e31\u0e49\u0e19\u0e46)", value="")
            if st.form_submit_button("\u2795 \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e40\u0e02\u0e49\u0e32"):
                if sy and en > 0 and sp > 0 and sp < en and sh > 0:
                    nid = int(d["id"].max()) + 1 if len(d) and d["id"].notna().any() else 1
                    d = pd.concat([d, pd.DataFrame([{"id": nid, "open_date": str(_dt.date.today()), "sym": sy, "entry": en, "stop": sp, "shares": sh,
                                                      "note": nt, "exit": np.nan, "close_date": ""}])], ignore_index=True)
                    st.success("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e41\u0e25\u0e49\u0e27" if _jr_save(d) else "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08 (\u0e40\u0e02\u0e35\u0e22\u0e19\u0e44\u0e1f\u0e25\u0e4c\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49)")
                else:
                    st.error("\u0e01\u0e23\u0e2d\u0e01\u0e43\u0e2b\u0e49\u0e04\u0e23\u0e1a \u0e41\u0e25\u0e30\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32")
        op = d[d["exit"].isna()]
        if len(op):
            with st.form("fast_jr_close"):
                lab = {int(r_["id"]): "#%d %s \u0e40\u0e02\u0e49\u0e32 %s (%s)" % (int(r_["id"]), r_["sym"], _fmt(r_["entry"]), r_["open_date"]) for _i, r_ in op.iterrows()}
                pick = st.selectbox("\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e2d\u0e22\u0e39\u0e48", list(lab.keys()), format_func=lambda i: lab[i])
                ex = st.number_input("\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01", min_value=0.0, value=0.0, step=0.1)
                if st.form_submit_button("\u2714 \u0e1b\u0e34\u0e14\u0e44\u0e21\u0e49"):
                    if ex > 0:
                        d.loc[d["id"] == pick, "exit"] = ex
                        d.loc[d["id"] == pick, "close_date"] = str(_dt.date.today())
                        st.success("\u0e1b\u0e34\u0e14\u0e44\u0e21\u0e49\u0e41\u0e25\u0e49\u0e27" if _jr_save(d) else "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08")
                    else:
                        st.error("\u0e43\u0e2a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01")
        stt = _jr_stats(d)
        if stt:
            st.markdown("**\u0e1c\u0e25\u0e08\u0e23\u0e34\u0e07\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13: %d \u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e1b\u0e34\u0e14\u0e41\u0e25\u0e49\u0e27 \xb7 \u0e0a\u0e19\u0e30 %.0f%% \xb7 R \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 %+.2f \xb7 R \u0e23\u0e27\u0e21 %+.1f \xb7 \u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21 %s**" % (stt["n"], stt["win"], stt["avgR"], stt["sumR"], format(stt["pnl"], ",.0f")))
            if stt["n"] < 30:
                st.caption("\u0e22\u0e31\u0e07\u0e21\u0e35\u0e44\u0e21\u0e48\u0e16\u0e36\u0e07 30 \u0e44\u0e21\u0e49 \u0e1c\u0e25\u0e23\u0e30\u0e22\u0e30\u0e2a\u0e31\u0e49\u0e19\u0e2a\u0e38\u0e48\u0e21\u0e21\u0e32\u0e01 \u0e2d\u0e22\u0e48\u0e32\u0e40\u0e1e\u0e34\u0e48\u0e07\u0e2a\u0e23\u0e38\u0e1b \u0e40\u0e01\u0e47\u0e1a\u0e43\u0e2b\u0e49\u0e16\u0e36\u0e07 30 \u0e44\u0e21\u0e49\u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07")
            else:
                st.caption("\u0e04\u0e23\u0e1a 30 \u0e44\u0e21\u0e49\u0e41\u0e25\u0e49\u0e27: \u0e16\u0e49\u0e32 R \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e22\u0e31\u0e07\u0e15\u0e34\u0e14\u0e25\u0e1a \u0e2b\u0e23\u0e37\u0e2d\u0e0a\u0e19\u0e30\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e0a\u0e31\u0e14\u0e40\u0e08\u0e19 \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e23\u0e30\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e40\u0e17\u0e23\u0e14\u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13 \u0e43\u0e2b\u0e49\u0e2b\u0e22\u0e38\u0e14\u0e41\u0e25\u0e30\u0e17\u0e1a\u0e17\u0e27\u0e19")
            show = stt["tbl"][["id", "open_date", "sym", "entry", "stop", "exit", "R", "pnl", "note"]]
            try:
                st.dataframe(show, hide_index=True, use_container_width=True, column_config={"R": st.column_config.NumberColumn("R", format="%+.2f"), "pnl": st.column_config.NumberColumn("\u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19", format="%+.0f")})
            except Exception:
                st.dataframe(show)
        elif len(op):
            st.caption("\u0e21\u0e35\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e2d\u0e22\u0e39\u0e48 %d \u0e44\u0e21\u0e49 \u0e1b\u0e34\u0e14\u0e44\u0e21\u0e49\u0e41\u0e25\u0e49\u0e27\u0e08\u0e30\u0e41\u0e2a\u0e14\u0e07\u0e2a\u0e16\u0e34\u0e15\u0e34" % len(op))
        else:
            st.caption("\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01 \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e17\u0e38\u0e01\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e40\u0e02\u0e49\u0e32\u0e08\u0e23\u0e34\u0e07 \u0e23\u0e27\u0e21\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e41\u0e1e\u0e49\u0e14\u0e49\u0e27\u0e22 \u0e16\u0e36\u0e07\u0e08\u0e30\u0e40\u0e2b\u0e47\u0e19\u0e20\u0e32\u0e1e\u0e08\u0e23\u0e34\u0e07")


def _sande_badge(vix):
    """\u0e1b\u0e49\u0e32\u0e22\u0e2a\u0e16\u0e32\u0e19\u0e30 SANDEVISTAN: \u0e15\u0e25\u0e32\u0e14\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 (VIX >= 20) = \u0e08\u0e31\u0e07\u0e2b\u0e27\u0e30\u0e40\u0e23\u0e47\u0e27 \u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07 \u0e41\u0e15\u0e48\u0e1e\u0e25\u0e32\u0e14\u0e01\u0e47\u0e40\u0e08\u0e47\u0e1a\u0e40\u0e23\u0e47\u0e27"""
    if vix is None:
        return
    on = vix >= 20
    col = "#fcee0a" if on else "#7d86a6"
    if on:
        txt = "\u0e15\u0e25\u0e32\u0e14\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 (VIX %.1f) \u0e08\u0e31\u0e07\u0e2b\u0e27\u0e30\u0e40\u0e23\u0e47\u0e27\u0e21\u0e32\u0e01 \u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e14\u0e35\u0e41\u0e25\u0e30\u0e40\u0e08\u0e47\u0e1a\u0e40\u0e23\u0e47\u0e27\u0e1e\u0e2d\u0e01\u0e31\u0e19 \u0e25\u0e14\u0e44\u0e21\u0e49\u0e41\u0e25\u0e30\u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19" % vix
    else:
        txt = "\u0e15\u0e25\u0e32\u0e14\u0e19\u0e34\u0e48\u0e07 (VIX %.1f) \u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07\u0e08\u0e30\u0e02\u0e22\u0e31\u0e1a\u0e0a\u0e49\u0e32\u0e01\u0e27\u0e48\u0e32\u0e1b\u0e01\u0e15\u0e34 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e35\u0e1a" % vix
    st.markdown('<style>.sd-b{display:inline-block;border:1px solid var(--c);color:var(--c)!important;-webkit-text-fill-color:var(--c);padding:3px 12px;font-size:12.5px;font-weight:800;letter-spacing:2px;margin:2px 0 8px;'
                'clip-path:polygon(0 0,calc(100% - 9px) 0,100% 9px,100% 100%,9px 100%,0 calc(100% - 9px));background:rgba(10,12,22,.7)}'
                '.sd-b.on{text-shadow:0 0 8px var(--c);animation:sdp 2.6s ease-in-out infinite}.sd-s{font-size:12.5px;color:#aab3d1!important;-webkit-text-fill-color:#aab3d1;margin-left:10px}'
                '@keyframes sdp{0%,100%{opacity:1}50%{opacity:.6}}@media (prefers-reduced-motion:reduce){.sd-b.on{animation:none}}</style>'
                + '<div><span class="sd-b%s" style="--c:%s">SANDEVISTAN // %s</span><span class="sd-s">%s</span></div>' % (
                    " on" if on else "", col, "ON" if on else "STANDBY", txt), unsafe_allow_html=True)


def render_fast():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown('<div class="fx-note">\u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e25\u0e30\u0e04\u0e13\u0e34\u0e15\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 <b>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d-\u0e02\u0e32\u0e22 \u0e41\u0e25\u0e30\u0e44\u0e21\u0e48\u0e21\u0e35\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22</b> \xb7 '
                '\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo \u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c\u0e23\u0e32\u0e27 15 \u0e19\u0e32\u0e17\u0e35 \u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e16\u0e37\u0e2d\u0e02\u0e49\u0e32\u0e21\u0e27\u0e31\u0e19\u0e16\u0e36\u0e07\u0e44\u0e21\u0e48\u0e01\u0e35\u0e48\u0e2a\u0e31\u0e1b\u0e14\u0e32\u0e2b\u0e4c \u0e44\u0e21\u0e48\u0e40\u0e2b\u0e21\u0e32\u0e30\u0e01\u0e31\u0e1a\u0e40\u0e01\u0e47\u0e07\u0e01\u0e33\u0e44\u0e23\u0e23\u0e32\u0e22\u0e19\u0e32\u0e17\u0e35</div>', unsafe_allow_html=True)

    # ---- 1) \u0e2a\u0e20\u0e32\u0e1e\u0e15\u0e25\u0e32\u0e14 ----
    st.markdown('<div class="section-label">\u25c6 1 \xb7 \u0e2a\u0e20\u0e32\u0e1e\u0e15\u0e25\u0e32\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49</div>', unsafe_allow_html=True)
    mk = _market()
    if mk:
        c1, c2, c3 = st.columns(3)
        if "SPY" in mk:
            c1.metric("S&P 500 (SPY)", _fmt(mk["SPY"]["lvl"]), "%+.2f%%" % mk["SPY"]["chg"])
        if "QQQ" in mk:
            c2.metric("Nasdaq-100 (QQQ)", _fmt(mk["QQQ"]["lvl"]), "%+.2f%%" % mk["QQQ"]["chg"])
        if "^VIX" in mk:
            c3.metric("\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27 VIX", _fmt(mk["^VIX"]["lvl"], 1), "%+.1f%%" % mk["^VIX"]["chg"], delta_color="inverse")
        try:
            import market_events
            st.caption("\u0e40\u0e07\u0e34\u0e19\u0e44\u0e2b\u0e25\u0e44\u0e1b\u0e17\u0e32\u0e07\u0e44\u0e2b\u0e19: " + market_events._read_flows({k: mk[k] for k in ("^VIX", "TLT", "GLD", "UUP") if k in mk}, mk.get("SPY", {}).get("chg", 0)))
        except Exception:
            pass
        vix = (mk.get("^VIX") or {}).get("lvl")
        _sande_badge(vix)
        if vix and vix >= 25:
            st.warning("VIX \u0e2a\u0e39\u0e07 (%.1f): \u0e15\u0e25\u0e32\u0e14\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e21\u0e32\u0e01 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 \u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e21\u0e35\u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e42\u0e14\u0e19\u0e07\u0e48\u0e32\u0e22\u0e02\u0e36\u0e49\u0e19 \u2014 \u0e1e\u0e34\u0e08\u0e32\u0e23\u0e13\u0e32\u0e25\u0e14\u0e02\u0e19\u0e32\u0e14\u0e44\u0e21\u0e49" % vix)
    else:
        st.info("\U0001f4e1 \u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e02\u0e32\u0e14 // \u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e15\u0e25\u0e32\u0e14\u0e08\u0e32\u0e01 Yahoo \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e25\u0e2d\u0e07\u0e23\u0e35\u0e40\u0e1f\u0e23\u0e0a\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07")

    # ---- 2) \u0e2a\u0e41\u0e01\u0e19 ----
    st.markdown('<div class="section-label">\u25c6 2 \xb7 \u0e2a\u0e41\u0e01\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07</div>', unsafe_allow_html=True)
    src = st.radio("\u0e2a\u0e41\u0e01\u0e19\u0e08\u0e32\u0e01", ["\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e02\u0e2d\u0e07\u0e09\u0e31\u0e19 (\u0e41\u0e01\u0e49\u0e44\u0e14\u0e49)", "Nasdaq 100", "S&P 500", "\u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07 (Nasdaq 100 + S&P 500)"], horizontal=True, key="fast_src", index=3)
    if src.startswith("\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d"):
        with st.expander("\u2699\ufe0f \u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e2a\u0e41\u0e01\u0e19 (\u0e41\u0e01\u0e49\u0e44\u0e14\u0e49 \xb7 \u0e04\u0e31\u0e48\u0e19\u0e14\u0e49\u0e27\u0e22\u0e0a\u0e48\u0e2d\u0e07\u0e27\u0e48\u0e32\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e08\u0e38\u0e25\u0e20\u0e32\u0e04)", expanded=False):
            raw = st.text_area("\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19", DEFAULT_UNIVERSE, height=90, key="fast_universe", label_visibility="collapsed")
        syms = tuple(dict.fromkeys(x.strip().upper() for x in raw.replace(",", " ").split() if x.strip()))[:150]
    else:
        try:
            import screener
            syms = tuple(screener.universe({"Nasdaq 100": "ndx", "S&P 500": "sp500"}.get(src, "both")))[:600]
        except Exception as ex:
            syms = ()
            st.warning("\u0e42\u0e2b\u0e25\u0e14\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e14\u0e31\u0e0a\u0e19\u0e35\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08 (%s) \u2014 \u0e43\u0e0a\u0e49 \"\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e02\u0e2d\u0e07\u0e09\u0e31\u0e19\" \u0e44\u0e1b\u0e01\u0e48\u0e2d\u0e19" % str(ex)[:80])
    liq = st.number_input("\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e27\u0e31\u0e19\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e19\u0e49\u0e2d\u0e22 (\u0e25\u0e49\u0e32\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c)", min_value=0.0, value=20.0, step=10.0, key="fast_liq",
                          help="\u0e15\u0e31\u0e14\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e1a\u0e32\u0e07\u0e2d\u0e2d\u0e01 \u2014 \u0e2a\u0e32\u0e22\u0e0b\u0e34\u0e48\u0e07\u0e40\u0e02\u0e49\u0e32\u0e2d\u0e2d\u0e01\u0e22\u0e32\u0e01\u0e16\u0e49\u0e32\u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07\u0e15\u0e48\u0e33 \xb7 \u0e43\u0e2a\u0e48 0 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e01\u0e23\u0e2d\u0e07")
    if not syms:
        st.info("\u0e44\u0e21\u0e48\u0e21\u0e35\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e2b\u0e49\u0e2a\u0e41\u0e01\u0e19")
        return
    with st.spinner("เน็ตรันเนอร์กำลังสแกนหุ้น %d ตัว ... ครั้งแรกอาจใช้ 30–60 วินาที · รอบถัดไปไวกว่านี้ (จำผลไว้ 5 นาที)" % len(syms)):
        rows = _scan(syms)
    rows = [x for x in rows if x.get("dvol", 0) >= liq]
    st.caption("\u0e2a\u0e41\u0e01\u0e19\u0e44\u0e14\u0e49 %d \u0e08\u0e32\u0e01 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e02\u0e2d (\u0e17\u0e35\u0e48\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1e\u0e2d \u0e2b\u0e23\u0e37\u0e2d\u0e2a\u0e20\u0e32\u0e1e\u0e04\u0e25\u0e48\u0e2d\u0e07\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07)" % (len(rows), len(syms)))
    if not rows:
        st.info("\u0e2a\u0e41\u0e01\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 (\u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e08\u0e32\u0e01 Yahoo \u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08 \u0e2b\u0e23\u0e37\u0e2d\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e15\u0e49\u0e2d\u0e07) \u0e25\u0e2d\u0e07\u0e23\u0e35\u0e40\u0e1f\u0e23\u0e0a\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07")
        return
    df = pd.DataFrame([{"\u0e2b\u0e38\u0e49\u0e19": r["sym"], "\u0e23\u0e32\u0e04\u0e32": r["px"], "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %": r["chg1"], "5 \u0e27\u0e31\u0e19 %": r["chg5"], "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x": r["rvol"], "ATR %": r["atr_pct"],
                        "RSI": r["rsi"], "\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20\u0e27 %": r["dist_hi"], "Gap %": r["gap"], "\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22/\u0e27\u0e31\u0e19 (\u0e25\u0e49\u0e32\u0e19$)": r["dvol"], "\u0e2a\u0e16\u0e32\u0e19\u0e30": _tags(r), "_trend": r["trend"], "_rb": (_rebound(r) or (0,))[0], "_elig": _rebound(r) is not None, "_green": bool(r["green"]),
                        "\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e40\u0e14\u0e49\u0e07": " \xb7 ".join(x.split(" (")[0] for x in (_rebound(r) or (0, []))[1])} for r in rows])
    f1, f2 = st.columns([2, 1])
    preset = f1.radio("\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07", [p[0] for p in PRESETS], horizontal=True, key="fast_preset")
    sort_by = f2.selectbox("\u0e40\u0e23\u0e35\u0e22\u0e07\u0e15\u0e32\u0e21", SORTS, key="fast_sort")
    st.caption(dict(PRESETS)[preset])
    view = df[_preset_mask(df, preset)].copy()
    vinfo, spy5 = None, None
    skey = {"% \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (\u0e21\u0e32\u0e01\u2192\u0e19\u0e49\u0e2d\u0e22)": ("\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %", False), "% \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (\u0e19\u0e49\u0e2d\u0e22\u2192\u0e21\u0e32\u0e01)": ("\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %", True), "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1b\u0e01\u0e15\u0e34": ("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x", False),
            "\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19 ATR%": ("ATR %", False), "\u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19": ("\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20\u0e27 %", False), "RSI": ("RSI", False)}[sort_by]
    grp, earn, hid = {}, {}, {}
    if preset == RB_NAME:
        vinfo = _load_valid()
        with st.expander("\U0001F4D6 \u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e04\u0e37\u0e2d\u0e2d\u0e30\u0e44\u0e23 \u0e2d\u0e48\u0e32\u0e19\u0e22\u0e31\u0e07\u0e44\u0e07 (\u0e2d\u0e48\u0e32\u0e19 1 \u0e19\u0e32\u0e17\u0e35)", expanded=False):
            st.markdown(_HELP_MD)
        spy5 = (mk.get("SPY") or {}).get("chg5")
        _vset = set((vinfo or {}).get("valid", [])) - REGIME
        df["_k"] = [(sum(1 for k, v in _live_feats(r, spy5).items() if v and k in _vset) if _rebound(r) else 0) for r in rows]
        view["_k"] = df.loc[view.index, "_k"]
        if vinfo:
            try:
                _age = (_dt.date.today() - _dt.date.fromisoformat(str(vinfo.get("date", "")))).days
            except Exception:
                _age = 0
            if _age > 30:
                st.warning("\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e01\u0e48\u0e32 %d \u0e27\u0e31\u0e19 (\u0e40\u0e01\u0e34\u0e19 30 \u0e27\u0e31\u0e19) \u2605 \u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a\u0e15\u0e25\u0e32\u0e14\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e01\u0e14\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e43\u0e2b\u0e21\u0e48\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07" % _age)
            _vn = len(_vset)
            st.markdown('<div class="rb-how"><b>\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e23\u0e35\u0e22\u0e07\u0e08\u0e32\u0e01\u0e19\u0e48\u0e32\u0e2a\u0e19\u0e43\u0e08\u0e21\u0e32\u0e01\u0e44\u0e1b\u0e19\u0e49\u0e2d\u0e22</b> \u0e42\u0e14\u0e22\u0e14\u0e39\u0e27\u0e48\u0e32\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e41\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 3 \u0e1b\u0e35\u0e40\u0e04\u0e22\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e44\u0e2b\u0e21 (\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e21\u0e35 %d \u0e02\u0e49\u0e2d \xb7 \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 %s) '
                        '\u00b7 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d \u00b7 <b>\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e41\u0e04\u0e48 2-3 \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e14\u0e35\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14 \u0e41\u0e25\u0e30\u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07</b></div>' % (_vn, _e(vinfo.get("date", "-"))), unsafe_allow_html=True)
        else:
            st.markdown('<div class="rb-how"><b>\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e27\u0e48\u0e32\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e44\u0e2b\u0e19\u0e0a\u0e48\u0e27\u0e22\u0e08\u0e23\u0e34\u0e07</b> \u2014 \u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\u0e19\u0e35\u0e49\u0e04\u0e37\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48 "\u0e25\u0e07\u0e41\u0e23\u0e07\u0e21\u0e32\u0e41\u0e25\u0e49\u0e27" \u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1a\u0e2d\u0e01\u0e27\u0e48\u0e32\u0e15\u0e31\u0e27\u0e44\u0e2b\u0e19\u0e19\u0e48\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e27\u0e48\u0e32 '
                        '\u0e44\u0e1b\u0e17\u0e35\u0e48\u0e01\u0e25\u0e48\u0e2d\u0e07 \U0001F9EA \u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e17\u0e49\u0e32\u0e22\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e25\u0e49\u0e27\u0e01\u0e14\u0e23\u0e31\u0e19 \u0e23\u0e30\u0e1a\u0e1a\u0e08\u0e30\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e41\u0e25\u0e49\u0e27\u0e08\u0e31\u0e14\u0e2d\u0e31\u0e19\u0e14\u0e31\u0e1a\u0e43\u0e2b\u0e49\u0e40\u0e2d\u0e07</div>', unsafe_allow_html=True)
        try:
            _vx, _sp = mk.get("^VIX"), mk.get("SPY")
            if _vx and _sp:
                if _vx["chg"] < 0 and _sp["chg"] > 0:
                    st.caption("\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e40\u0e2d\u0e37\u0e49\u0e2d\u0e15\u0e48\u0e2d\u0e01\u0e32\u0e23\u0e40\u0e14\u0e49\u0e07: S&P %+.2f%% \u0e41\u0e25\u0e30 VIX \u0e25\u0e07 %.1f%% (\u0e04\u0e19\u0e01\u0e25\u0e31\u0e27\u0e19\u0e49\u0e2d\u0e22\u0e25\u0e07)" % (_sp["chg"], abs(_vx["chg"])))
                elif _vx["lvl"] >= 25:
                    st.caption("\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e22\u0e31\u0e07\u0e01\u0e25\u0e31\u0e27 (VIX %.1f): \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e40\u0e14\u0e49\u0e07\u0e2d\u0e32\u0e08\u0e42\u0e14\u0e19\u0e17\u0e38\u0e1a\u0e0b\u0e49\u0e33\u0e07\u0e48\u0e32\u0e22 \u0e25\u0e14\u0e02\u0e19\u0e32\u0e14\u0e44\u0e21\u0e49" % _vx["lvl"])
                else:
                    st.caption("\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49: S&P %+.2f%% \xb7 VIX %.1f (%+.1f%%)" % (_sp["chg"], _vx["lvl"], _vx["chg"]))
        except Exception:
            pass
        if vinfo and "mktdn" in vinfo.get("valid", []) and spy5 is not None and spy5 <= -2:
            st.caption("\u0e15\u0e25\u0e32\u0e14\u0e23\u0e27\u0e21\u0e23\u0e48\u0e27\u0e07\u0e2d\u0e22\u0e39\u0e48 %.1f%% \u0e43\u0e19 5 \u0e27\u0e31\u0e19 \u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07\u0e40\u0e1e\u0e23\u0e32\u0e30\u0e15\u0e25\u0e32\u0e14\u0e25\u0e07\u0e2d\u0e32\u0e08\u0e40\u0e14\u0e49\u0e07\u0e44\u0e14\u0e49 \u0e41\u0e15\u0e48\u0e01\u0e47\u0e2d\u0e32\u0e08\u0e23\u0e48\u0e27\u0e07\u0e15\u0e48\u0e2d \u0e2d\u0e22\u0e48\u0e32\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e32\u0e01\u0e40\u0e01\u0e34\u0e19\u0e44\u0e1b" % abs(spy5))
        _render_backtest(syms, liq, expanded=not vinfo)
        q1, q2, q3, q4, q5 = st.columns([2, 1, 1, 1, 1])
        only_valid = q1.checkbox("\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e40\u0e04\u0e22\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a", value=bool(_vset), key="fast_rb_valid", disabled=not _vset,
                                 help="\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e36\u0e07\u0e08\u0e30\u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49")
        need_atr = q2.checkbox("\u0e15\u0e31\u0e27\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 (ATR \u2265 3%)", value=True, key="fast_rb_atr", help="\u0e0b\u0e34\u0e48\u0e07\u0e44\u0e14\u0e49\u0e15\u0e49\u0e2d\u0e07\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07\u0e1e\u0e2d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48 ATR \u0e15\u0e48\u0e33\u0e40\u0e14\u0e49\u0e07\u0e41\u0e25\u0e49\u0e27\u0e02\u0e22\u0e31\u0e1a\u0e19\u0e49\u0e2d\u0e22")
        need_green = q3.checkbox("\u0e41\u0e17\u0e48\u0e07\u0e40\u0e02\u0e35\u0e22\u0e27\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 (\u0e1b\u0e34\u0e14\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e34\u0e14)", value=False, key="fast_rb_green", help="\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e41\u0e17\u0e48\u0e07\u0e41\u0e14\u0e07\u0e04\u0e37\u0e2d\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e04\u0e19\u0e23\u0e31\u0e1a")
        hide_earn = q4.checkbox("\u0e0b\u0e48\u0e2d\u0e19\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e07\u0e1a\u0e2d\u0e2d\u0e01 \u2264 7 \u0e27\u0e31\u0e19", value=True, key="fast_rb_earn", help="\u0e07\u0e1a\u0e43\u0e01\u0e25\u0e49\u0e2d\u0e2d\u0e01\u0e21\u0e31\u0e01\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e23\u0e32\u0e04\u0e32\u0e01\u0e23\u0e30\u0e42\u0e14\u0e14\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04\u0e43\u0e0a\u0e49\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49")
        one_per = q5.checkbox("\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e25\u0e30 1 \u0e15\u0e31\u0e27", value=True, key="fast_rb_dedupe", help="\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e01\u0e31\u0e19 (\u0e40\u0e0a\u0e48\u0e19 \u0e01\u0e25\u0e38\u0e48\u0e21\u0e0a\u0e34\u0e1b) \u0e19\u0e31\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e19 \u0e0b\u0e37\u0e49\u0e2d\u0e2b\u0e25\u0e32\u0e22\u0e15\u0e31\u0e27 = \u0e27\u0e32\u0e07\u0e40\u0e14\u0e34\u0e21\u0e1e\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27\u0e0b\u0e49\u0e33")
        if only_valid and _vset:
            view = view[view["_k"] >= 1]
        if need_atr:
            view = view[view["ATR %"] >= 3]
        if need_green:
            view = view[view["_green"]]
        view = view.sort_values(["_k", "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x"], ascending=[False, False], na_position="last").reset_index(drop=True).head(60)
        grp = _group_read(rows)
        try:
            earn = _earn_map(tuple(view["\u0e2b\u0e38\u0e49\u0e19"]))
        except Exception:
            earn = {}
        if one_per and len(view):
            _rt = {r["sym"]: r["ret"][1:] for r in rows if r.get("ret") is not None and len(r["ret"]) == 60 and np.isfinite(r["ret"][1:]).all()}
            _kept, _skip = [], []
            for _sy in view["\u0e2b\u0e38\u0e49\u0e19"]:
                _a = _rt.get(_sy)
                _dup = False
                if _a is not None:
                    for k in _kept:
                        _b = _rt.get(k)
                        if _b is not None and float(np.corrcoef(_a, _b)[0, 1]) >= 0.6:
                            _dup = True
                            hid.setdefault(k, []).append(_sy)
                            break
                (_skip if _dup else _kept).append(_sy)
            if _skip:
                with st.expander("\U0001F9E9 \u0e0b\u0e48\u0e2d\u0e19 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e15\u0e32\u0e21\u0e15\u0e31\u0e27\u0e2d\u0e37\u0e48\u0e19 \xb7 \u0e01\u0e14\u0e14\u0e39\u0e27\u0e48\u0e32\u0e43\u0e04\u0e23\u0e2d\u0e22\u0e39\u0e48\u0e2b\u0e25\u0e31\u0e07\u0e15\u0e31\u0e27\u0e44\u0e2b\u0e19" % len(_skip), expanded=False):
                    _rows = "".join('<div class="hid-row"><span class="hid-rep">%s</span><span class="hid-ar">\u2190</span>%s</div>' % (
                        _e(k), "".join('<span class="hid-f">%s</span>' % _e(x) for x in v[:14]) + ('<span class="hid-ar">+%d</span>' % (len(v) - 14) if len(v) > 14 else ""))
                        for k, v in hid.items())
                    st.markdown(_rows + '<div class="rb-note" style="margin-top:8px;font-size:12px;color:#8d97b8">\u0e15\u0e31\u0e27\u0e14\u0e49\u0e32\u0e19\u0e0b\u0e49\u0e32\u0e22\u0e04\u0e37\u0e2d\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e17\u0e35\u0e48\u0e41\u0e2a\u0e14\u0e07 \u0e15\u0e31\u0e27\u0e14\u0e49\u0e32\u0e19\u0e02\u0e27\u0e32\u0e04\u0e37\u0e2d\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e02\u0e22\u0e31\u0e1a\u0e15\u0e32\u0e21\u0e01\u0e31\u0e19\u0e21\u0e32\u0e01 (\u0e2a\u0e2b\u0e2a\u0e31\u0e21\u0e1e\u0e31\u0e19\u0e18\u0e4c \u2265 0.6 \u0e43\u0e19 60 \u0e27\u0e31\u0e19) \u0e16\u0e39\u0e01\u0e0b\u0e48\u0e2d\u0e19\u0e44\u0e27\u0e49 \xb7 \u0e1b\u0e34\u0e14\u0e0a\u0e48\u0e2d\u0e07 "\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21\u0e25\u0e30 1 \u0e15\u0e31\u0e27" \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14</div>', unsafe_allow_html=True)
                view = view[~view["\u0e2b\u0e38\u0e49\u0e19"].isin(_skip)].reset_index(drop=True)
        if hide_earn and len(view):
            _td = _dt.date.today()
            soon = [x for x in view["\u0e2b\u0e38\u0e49\u0e19"] if earn.get(x) and 0 <= (earn[x] - _td).days <= 7]
            if soon:
                st.caption("\u0e0b\u0e48\u0e2d\u0e19 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e07\u0e1a\u0e2d\u0e2d\u0e01\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19: %s" % (len(soon), ", ".join(soon[:12])))
                view = view[~view["\u0e2b\u0e38\u0e49\u0e19"].isin(soon)].reset_index(drop=True)
    else:
        view = view.sort_values(skey[0], ascending=skey[1], na_position="last").reset_index(drop=True)
    st.markdown("**\u0e15\u0e23\u0e07\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02 %d \u0e08\u0e32\u0e01 %d \u0e15\u0e31\u0e27**" % (len(view), len(df)))
    show = view.drop(columns=["_trend", "_green", "_elig"])
    if preset == RB_NAME:
        show = show.assign(**{"\u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c (\u0e02\u0e49\u0e2d)": show["_k"]}).drop(columns=["_rb", "_k"])
        show = show[["\u0e2b\u0e38\u0e49\u0e19", "\u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c (\u0e02\u0e49\u0e2d)", "\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e40\u0e14\u0e49\u0e07", "\u0e23\u0e32\u0e04\u0e32", "\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %", "5 \u0e27\u0e31\u0e19 %", "\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20\u0e27 %", "RSI", "\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x", "ATR %", "\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22/\u0e27\u0e31\u0e19 (\u0e25\u0e49\u0e32\u0e19$)", "\u0e2a\u0e16\u0e32\u0e19\u0e30"]]
    else:
        show = show.drop(columns=["_rb", "\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25\u0e17\u0e35\u0e48\u0e2d\u0e32\u0e08\u0e40\u0e14\u0e49\u0e07", "_k"], errors="ignore")
    if preset == RB_NAME:
        _shown = set(view["\u0e2b\u0e38\u0e49\u0e19"])
        _simple_view(view, rows, grp, earn, vinfo, spy5, {k: v for k, v in hid.items() if k in _shown})
        if st.checkbox("\u0e14\u0e39\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07 (\u0e23\u0e27\u0e21\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e40\u0e14\u0e48\u0e19) \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14", value=False, key="fast_detail"):
            _cards(view, rows, grp, earn, vinfo, spy5)
        with st.expander("\U0001f4cb \u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e15\u0e47\u0e21 (\u0e40\u0e23\u0e35\u0e22\u0e07\u0e44\u0e14\u0e49 \u0e04\u0e49\u0e19\u0e2b\u0e32\u0e44\u0e14\u0e49)", expanded=False):
            _table(show)
    else:
        _table(show)
    st.caption("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 x = \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 \xf7 \u0e04\u0e48\u0e32\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 20 \u0e27\u0e31\u0e19 \xb7 ATR % = \u0e0a\u0e48\u0e27\u0e07\u0e41\u0e01\u0e27\u0e48\u0e07\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e27\u0e31\u0e19\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e23\u0e32\u0e04\u0e32 (\u0e22\u0e34\u0e48\u0e07\u0e2a\u0e39\u0e07 \u0e44\u0e21\u0e49\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e25\u0e47\u0e01\u0e25\u0e07) \xb7 RSI > 70 \u0e23\u0e49\u0e2d\u0e19\u0e41\u0e23\u0e07 < 30 \u0e0b\u0e1a\u0e40\u0e0b\u0e32 \xb7 "
               "Gap = \u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e34\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e1b\u0e34\u0e14\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e27\u0e32\u0e19\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23 \xb7 \U0001f525 \u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13 \u2265 1.5 \u0e40\u0e17\u0e48\u0e32 \xb7 \u26a0\ufe0f ATR \u2265 5% \xb7 \U0001f4c8 \u0e23\u0e32\u0e04\u0e32 > EMA20 > EMA50 \xb7 \U0001f53b \u0e23\u0e32\u0e04\u0e32 < EMA20 < EMA50")

    pool = list(view["\u0e2b\u0e38\u0e49\u0e19"]) or list(df["\u0e2b\u0e38\u0e49\u0e19"])
    sel = st.selectbox("\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e27\u0e32\u0e07\u0e41\u0e1c\u0e19\u0e44\u0e21\u0e49", pool, key="fast_pick")
    r = next((x for x in rows if x["sym"] == sel), None)
    if not r:
        return

    rb = _rebound(r)
    if preset == RB_NAME and rb:
        cg, cb = _ctx(r, grp, earn)
        _fl = _live_feats(r, spy5)
        _pv = ["\u2605 \u0e1c\u0e48\u0e32\u0e19\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c: " + FEAT_LABEL[k] for k in (vinfo or {}).get("valid", []) if _fl.get(k)]
        _pb = ["\u26A0 \u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32\u0e41\u0e22\u0e48\u0e01\u0e27\u0e48\u0e32\u0e40\u0e14\u0e34\u0e21: " + FEAT_LABEL[k] for k in (vinfo or {}).get("bad", []) if _fl.get(k)]
        lis = "".join("<li>%s</li>" % _e(x) for x in _pv + rb[1] + cg)
        wl = "".join("<li>%s</li>" % _e(x) for x in _pb + rb[2] + cb) or "<li>\u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e23\u0e23\u0e30\u0e27\u0e31\u0e07\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e0a\u0e38\u0e14\u0e19\u0e35\u0e49 \u0e41\u0e15\u0e48\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e17\u0e23\u0e32\u0e1a\u0e02\u0e48\u0e32\u0e27\u0e17\u0e35\u0e48\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e23\u0e32\u0e04\u0e32\u0e15\u0e01</li>"
        with st.expander("\U0001F52C \u0e14\u0e39\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e17\u0e32\u0e07\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04\u0e02\u0e2d\u0e07 %s (\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e04\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e32\u0e01\u0e14\u0e39\u0e25\u0e36\u0e01)" % sel, expanded=False):
            st.markdown('<div class="fx-note"><b>%s \u2014 \u0e02\u0e49\u0e2d\u0e2a\u0e31\u0e07\u0e40\u0e01\u0e15\u0e17\u0e32\u0e07\u0e40\u0e17\u0e04\u0e19\u0e34\u0e04 %d \u0e02\u0e49\u0e2d (\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e27\u0e48\u0e32\u0e0a\u0e48\u0e27\u0e22\u0e17\u0e33\u0e19\u0e32\u0e22)</b><ul style="margin:6px 0 6px 18px">%s</ul>'
                        '<b>\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e30\u0e27\u0e31\u0e07</b><ul style="margin:6px 0 6px 18px">%s</ul>'
                        '<b>\u0e04\u0e27\u0e32\u0e21\u0e04\u0e34\u0e14\u0e02\u0e2d\u0e07\u0e1d\u0e31\u0e48\u0e07\u0e40\u0e14\u0e49\u0e07\u0e1c\u0e34\u0e14\u0e40\u0e21\u0e37\u0e48\u0e2d:</b> \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e25\u0e38\u0e14\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %s (\u0e17\u0e33\u0e15\u0e48\u0e33\u0e43\u0e2b\u0e21\u0e48 = \u0e41\u0e23\u0e07\u0e02\u0e32\u0e22\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e08\u0e1a) \xb7 '
                        '<b>\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e1a\u0e2d\u0e01\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49:</b> \u0e2a\u0e32\u0e40\u0e2b\u0e15\u0e38\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e15\u0e01 \u2014 \u0e16\u0e49\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e02\u0e48\u0e32\u0e27\u0e1b\u0e31\u0e08\u0e08\u0e31\u0e22\u0e1e\u0e37\u0e49\u0e19\u0e10\u0e32\u0e19\u0e40\u0e2a\u0e35\u0e22\u0e2b\u0e32\u0e22 (\u0e07\u0e1a\u0e41\u0e22\u0e48 \u0e25\u0e14\u0e04\u0e32\u0e14\u0e01\u0e32\u0e23\u0e13\u0e4c) \u0e01\u0e32\u0e23\u0e40\u0e14\u0e49\u0e07\u0e21\u0e31\u0e01\u0e2d\u0e48\u0e2d\u0e19\u0e41\u0e25\u0e30\u0e2d\u0e32\u0e22\u0e38\u0e2a\u0e31\u0e49\u0e19 \u0e40\u0e0a\u0e47\u0e01\u0e02\u0e48\u0e32\u0e27\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e2a\u0e21\u0e2d '
                        '<a href="https://www.google.com/search?q=%s+stock+why+down+today&tbm=nws" target="_blank">\u0e04\u0e49\u0e19\u0e02\u0e48\u0e32\u0e27 %s</a></div>' % (
                            _e(sel), rb[0], lis, wl, _fmt(r["lo_t"]), _e(sel), _e(sel)), unsafe_allow_html=True)
    elif preset == RB_NAME:
        st.caption("%s \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e40\u0e02\u0e49\u0e32\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07 (\u0e15\u0e49\u0e2d\u0e07\u0e23\u0e48\u0e27\u0e07 \u226515%% \u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 \u0e2b\u0e23\u0e37\u0e2d 5 \u0e27\u0e31\u0e19 \u22658%% \u0e41\u0e25\u0e30 RSI \u2264 42)" % sel)

    # ---- 3) \u0e41\u0e1c\u0e19\u0e44\u0e21\u0e49 ----
    st.markdown('<div class="section-label">\u25c6 3 \xb7 \u0e41\u0e1c\u0e19\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e02\u0e2d\u0e07 %s</div>' % _e(sel), unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("\u0e23\u0e32\u0e04\u0e32\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14", _fmt(r["px"]), "%+.2f%% \u0e27\u0e31\u0e19\u0e19\u0e35\u0e49" % r["chg1"])
    m2.metric("\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e15\u0e48\u0e2d\u0e27\u0e31\u0e19 (ATR)", "%s (%.1f%%)" % (_fmt(r["atr"]), r["atr_pct"]))
    m3.metric("\u0e1b\u0e23\u0e34\u0e21\u0e32\u0e13\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e1b\u0e01\u0e15\u0e34", "%s \u0e40\u0e17\u0e48\u0e32" % _fmt(r["rvol"], 1))
    m4.metric("RSI 14 \u0e27\u0e31\u0e19", _fmt(r["rsi"], 0))
    plan = None
    ed = _next_earn(sel)
    if ed:
        days = (ed - _dt.date.today()).days
        if days <= 7:
            st.warning("\u26a0\ufe0f \u0e07\u0e1a\u0e2d\u0e2d\u0e01\u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19 (%s) \u2014 \u0e23\u0e32\u0e04\u0e32\u0e21\u0e31\u0e01\u0e01\u0e23\u0e30\u0e42\u0e14\u0e14\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19 (gap) \u0e08\u0e19\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e44\u0e21\u0e48\u0e17\u0e33\u0e07\u0e32\u0e19 \u0e25\u0e14\u0e44\u0e21\u0e49\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e25\u0e35\u0e48\u0e22\u0e07\u0e16\u0e37\u0e2d\u0e02\u0e49\u0e32\u0e21\u0e07\u0e1a" % (days, ed.strftime("%d/%m/%Y")))
        else:
            st.caption("\u0e07\u0e1a\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e16\u0e31\u0e14\u0e44\u0e1b\u0e23\u0e32\u0e27\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48 %s (\u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19)" % (ed.strftime("%d/%m/%Y"), days))
    else:
        st.caption("\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e27\u0e31\u0e19\u0e1b\u0e23\u0e30\u0e01\u0e32\u0e28\u0e07\u0e1a\u0e08\u0e32\u0e01 Yahoo \u2014 \u0e40\u0e0a\u0e47\u0e01\u0e1b\u0e0f\u0e34\u0e17\u0e34\u0e19\u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e37\u0e2d\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19")

    st.markdown("**\u0e15\u0e31\u0e27\u0e04\u0e33\u0e19\u0e27\u0e13\u0e02\u0e19\u0e32\u0e14\u0e44\u0e21\u0e49 (\u0e1d\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d)** \u2014 \u0e04\u0e34\u0e14\u0e08\u0e32\u0e01 \"\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e16\u0e49\u0e32\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\" \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e08\u0e32\u0e01\u0e04\u0e27\u0e32\u0e21\u0e21\u0e31\u0e48\u0e19\u0e43\u0e08")
    a, b, c_ = st.columns(3)
    capital = a.number_input("\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21 (\u0e2a\u0e01\u0e38\u0e25\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19)", min_value=0.0, value=100000.0, step=1000.0, key="fast_cap")
    risk_pct = b.number_input("\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e15\u0e48\u0e2d\u0e44\u0e21\u0e49 (% \u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19)", min_value=0.1, max_value=10.0, value=1.0, step=0.25, key="fast_risk",
                              help="\u0e21\u0e37\u0e2d\u0e2d\u0e32\u0e0a\u0e35\u0e1e\u0e2a\u0e48\u0e27\u0e19\u0e43\u0e2b\u0e0d\u0e48\u0e43\u0e0a\u0e49 0.5-2% \u0e15\u0e48\u0e2d\u0e44\u0e21\u0e49 \xb7 \u0e40\u0e2a\u0e35\u0e22\u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07 10 \u0e44\u0e21\u0e49\u0e17\u0e35\u0e48 1% = \u0e40\u0e07\u0e34\u0e19\u0e2b\u0e32\u0e22\u0e23\u0e32\u0e27 10% \u0e22\u0e31\u0e07\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e44\u0e14\u0e49")
    entry = c_.number_input("\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32", min_value=0.01, value=float(round(r["px"], 2)), step=0.1, key="fast_entry_%s" % sel)
    d1, d2 = st.columns([2, 1])
    mult_lab = d1.radio("\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19", ["\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 1.5 \xd7 ATR (\u0e41\u0e19\u0e30\u0e19\u0e33)", "1.0 \xd7 ATR (\u0e41\u0e04\u0e1a \u0e42\u0e14\u0e19\u0e07\u0e48\u0e32\u0e22)", "2.0 \xd7 ATR (\u0e01\u0e27\u0e49\u0e32\u0e07 \u0e44\u0e21\u0e49\u0e40\u0e25\u0e47\u0e01\u0e25\u0e07)", "\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14 10 \u0e27\u0e31\u0e19", "\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e40\u0e2d\u0e07"],
                        horizontal=True, key="fast_stopmode")
    if mult_lab.startswith("\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32"):
        stop = entry - 1.5 * r["atr"]
    elif mult_lab.startswith("1.0"):
        stop = entry - 1.0 * r["atr"]
    elif mult_lab.startswith("2.0"):
        stop = entry - 2.0 * r["atr"]
    elif mult_lab.startswith("\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14"):
        stop = r["lo10"] * 0.995
    else:
        stop = d2.number_input("\u0e23\u0e32\u0e04\u0e32\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19", min_value=0.01, value=float(round(max(entry - 1.5 * r["atr"], 0.01), 2)), step=0.1, key="fast_stop_custom_%s" % sel)
    res = size_position(capital, risk_pct, entry, stop)
    if not res:
        st.error("\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 (\u0e41\u0e25\u0e30\u0e17\u0e38\u0e01\u0e0a\u0e48\u0e2d\u0e07\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32 0)")
    else:
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19", _fmt(stop), "-%.1f%% \u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32" % res["stop_pct"], delta_color="off")
        k2.metric("\u0e0b\u0e37\u0e49\u0e2d\u0e44\u0e14\u0e49", "%s \u0e2b\u0e38\u0e49\u0e19" % format(res["shares"], ","), "\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32 %s (%.0f%% \u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19)" % (format(res["value"], ",.0f"), res["value_pct"]), delta_color="off")
        k3.metric("\u0e16\u0e49\u0e32\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 \u0e40\u0e2a\u0e35\u0e22\u0e23\u0e32\u0e27", format(res["real_risk"], ",.0f"), "%.2f%% \u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19" % res["real_risk_pct"], delta_color="off")
        k4.metric("\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19", _fmt(res["per_share"]))
        if res["capped"]:
            st.info("\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19\u0e0b\u0e37\u0e49\u0e2d\u0e44\u0e14\u0e49\u0e41\u0e04\u0e48 %s \u0e2b\u0e38\u0e49\u0e19 (\u0e44\u0e21\u0e48\u0e1e\u0e2d\u0e0b\u0e37\u0e49\u0e2d\u0e15\u0e32\u0e21\u0e17\u0e35\u0e48\u0e04\u0e33\u0e19\u0e27\u0e13 %s \u0e2b\u0e38\u0e49\u0e19) \u0e08\u0e36\u0e07\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e08\u0e23\u0e34\u0e07\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e44\u0e27\u0e49 \u2014 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e43\u0e0a\u0e49\u0e21\u0e32\u0e23\u0e4c\u0e08\u0e34\u0e49\u0e19" % (format(res["afford"], ","), format(res["want"], ",")))
        if res["stop_pct"] < r["atr_pct"] * 0.8:
            st.warning("\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e41\u0e04\u0e1a\u0e01\u0e27\u0e48\u0e32\u0e04\u0e27\u0e32\u0e21\u0e1c\u0e31\u0e19\u0e1c\u0e27\u0e19\u0e1b\u0e01\u0e15\u0e34\u0e23\u0e32\u0e22\u0e27\u0e31\u0e19 (ATR %.1f%%) \u2014 \u0e21\u0e35\u0e42\u0e2d\u0e01\u0e32\u0e2a\u0e42\u0e14\u0e19\u0e2a\u0e30\u0e1a\u0e31\u0e14\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e41\u0e01\u0e27\u0e48\u0e07\u0e18\u0e23\u0e23\u0e21\u0e14\u0e32" % r["atr_pct"])
        if res["shares"] == 0:
            st.warning("\u0e44\u0e21\u0e49\u0e40\u0e25\u0e47\u0e01\u0e40\u0e01\u0e34\u0e19\u0e01\u0e27\u0e48\u0e32 1 \u0e2b\u0e38\u0e49\u0e19\u0e15\u0e32\u0e21\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22 \u2014 \u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19/ % \u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22 \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32")
        plan = {"entry": entry, "stop": stop, "shares": res["shares"]}
        _vi = _load_valid()
        try:
            _nr = _news_map((sel,)).get(sel) or []
        except Exception:
            _nr = []
        _vix = (mk.get("^VIX") or {}).get("lvl")
        _rr20 = ((r["hi20"] - entry) / res["per_share"]) if (r["hi20"] > entry and res["per_share"] > 0) else 0.0
        _render_checklist(sel, r, ed, _nr, _vi, (mk.get("SPY") or {}).get("chg5"), _vix, _rr20, sel)
        rr = [("1R", entry + 1 * res["per_share"]), ("2R", entry + 2 * res["per_share"]), ("3R", entry + 3 * res["per_share"])]
        lv = [("\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19", r["hi20"]), ("\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 60 \u0e27\u0e31\u0e19", r["hi60"])]
        with st.expander("\U0001F3AF \u0e14\u0e39\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e23\u0e32\u0e04\u0e32\u0e2d\u0e49\u0e32\u0e07\u0e2d\u0e34\u0e07 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22 \u0e41\u0e04\u0e48\u0e15\u0e31\u0e27\u0e0a\u0e48\u0e27\u0e22\u0e04\u0e34\u0e14)", expanded=False):
            tb = [{"\u0e23\u0e30\u0e14\u0e31\u0e1a": ("\u0e01\u0e33\u0e44\u0e23\u0e40\u0e17\u0e48\u0e32\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22 (%s)" if n == "1R" else "\u0e01\u0e33\u0e44\u0e23 %s \u0e40\u0e17\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22 (%s)") % ((n,) if n == "1R" else (n[0], n)), "\u0e23\u0e32\u0e04\u0e32": p, "\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 %": (p / entry - 1) * 100} for n, p in rr]
            for n, p in lv:
                ext = "R/R \u2248 %.1f : 1" % ((p - entry) / res["per_share"]) if p > entry else "\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32\u0e41\u0e25\u0e49\u0e27"
                tb.append({"\u0e23\u0e30\u0e14\u0e31\u0e1a": "%s (%s)" % (n, ext), "\u0e23\u0e32\u0e04\u0e32": p, "\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 %": (p / entry - 1) * 100})
            tdf = pd.DataFrame(tb)
            try:
                st.dataframe(tdf, hide_index=True, use_container_width=True, column_config={
                    "\u0e23\u0e32\u0e04\u0e32": st.column_config.NumberColumn("\u0e23\u0e32\u0e04\u0e32", format="%.2f"), "\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 %": st.column_config.NumberColumn("\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 %", format="%+.1f")})
            except Exception:
                st.dataframe(tdf)
            st.caption("R = \u0e23\u0e30\u0e22\u0e30\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e15\u0e48\u0e2d\u0e2b\u0e38\u0e49\u0e19 (\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 \u2212 \u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19) \xb7 \u0e16\u0e49\u0e32\u0e21\u0e35\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e40\u0e01\u0e48\u0e32\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e01\u0e25\u0e49 \u0e23\u0e32\u0e04\u0e32\u0e21\u0e31\u0e01\u0e15\u0e34\u0e14\u0e41\u0e19\u0e27\u0e15\u0e49\u0e32\u0e19 \u0e25\u0e2d\u0e07\u0e40\u0e0a\u0e47\u0e01\u0e27\u0e48\u0e32\u0e01\u0e48\u0e2d\u0e19\u0e16\u0e36\u0e07 2R \u0e21\u0e35\u0e41\u0e19\u0e27\u0e15\u0e49\u0e32\u0e19\u0e02\u0e27\u0e32\u0e07\u0e44\u0e2b\u0e21")

    # ---- \u0e01\u0e23\u0e32\u0e1f ----
    with st.expander("\U0001F4C8 \u0e14\u0e39\u0e01\u0e23\u0e32\u0e1f\u0e23\u0e32\u0e04\u0e32 3 \u0e40\u0e14\u0e37\u0e2d\u0e19", expanded=False):
        h = _hist(sel)
        if h is not None and len(h) > 30:
            try:
                cc = h["Close"].dropna()
                ch = pd.DataFrame({"\u0e23\u0e32\u0e04\u0e32\u0e1b\u0e34\u0e14": cc}).tail(90)
                st.line_chart(ch)
            except Exception:
                pass

    _render_journal(sel, plan)
    st.markdown('<div class="fx-rule"><b>\u0e01\u0e0e\u0e40\u0e2b\u0e25\u0e47\u0e01\u0e2a\u0e32\u0e22\u0e0b\u0e34\u0e48\u0e07:</b> \u2460 \u0e27\u0e32\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 "\u0e01\u0e48\u0e2d\u0e19" \u0e01\u0e14\u0e0b\u0e37\u0e49\u0e2d \u0e41\u0e25\u0e49\u0e27\u0e17\u0e33\u0e15\u0e32\u0e21\u0e08\u0e23\u0e34\u0e07 \u0e44\u0e21\u0e48\u0e02\u0e22\u0e31\u0e1a\u0e2b\u0e19\u0e35 \xb7 \u2461 \u0e44\u0e21\u0e48\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e01\u0e34\u0e19 1-2% \u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e17\u0e38\u0e19\u0e15\u0e48\u0e2d\u0e44\u0e21\u0e49 \xb7 '
                '\u2462 \u0e44\u0e21\u0e48\u0e44\u0e25\u0e48\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e27\u0e34\u0e48\u0e07\u0e44\u0e1b\u0e41\u0e25\u0e49\u0e27\u0e2b\u0e25\u0e32\u0e22\u0e2a\u0e34\u0e1a\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c\u0e43\u0e19\u0e27\u0e31\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e15\u0e48\u0e2d\u0e01\u0e33\u0e44\u0e23\u0e44\u0e21\u0e48\u0e04\u0e38\u0e49\u0e21 \xb7 \u2463 \u0e23\u0e30\u0e27\u0e31\u0e07\u0e07\u0e1a \u0e02\u0e48\u0e32\u0e27\u0e43\u0e2b\u0e0d\u0e48 \u0e41\u0e25\u0e30 gap \u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19 \u2014 \u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e44\u0e21\u0e48\u0e01\u0e32\u0e23\u0e31\u0e19\u0e15\u0e35\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01 \xb7 '
                '\u2464 \u0e2b\u0e19\u0e49\u0e32\u0e19\u0e35\u0e49\u0e0a\u0e48\u0e27\u0e22\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e0a\u0e48\u0e27\u0e22\u0e17\u0e33\u0e19\u0e32\u0e22\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07</div>', unsafe_allow_html=True)
    st.caption("\u0e2d\u0e22\u0e32\u0e01\u0e14\u0e39\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e07\u0e48\u0e32\u0e22 \u0e40\u0e2b\u0e15\u0e38\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e21\u0e32 \u0e41\u0e25\u0e30\u0e1e\u0e37\u0e49\u0e19\u0e10\u0e32\u0e19\u0e02\u0e2d\u0e07 %s? \u0e44\u0e1b\u0e17\u0e35\u0e48\u0e40\u0e21\u0e19\u0e39 DEEP INSIGHT \u0e41\u0e25\u0e49\u0e27\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e23\u0e2b\u0e31\u0e2a\u0e19\u0e35\u0e49" % sel)