# -*- coding: utf-8 -*-
"""morning_ui.py - \u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e0a\u0e49\u0e32\u0e19\u0e35\u0e49 (\u0e2d\u0e48\u0e32\u0e19\u0e08\u0e1a\u0e43\u0e19 1 \u0e19\u0e32\u0e17\u0e35) \u0e27\u0e32\u0e07\u0e44\u0e27\u0e49\u0e1a\u0e19\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e41\u0e23\u0e01

\u0e23\u0e27\u0e21 3 \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e40\u0e0a\u0e47\u0e01\u0e17\u0e38\u0e01\u0e40\u0e0a\u0e49\u0e32\u0e44\u0e27\u0e49\u0e17\u0e35\u0e48\u0e40\u0e14\u0e35\u0e22\u0e27:
 1) \u0e15\u0e25\u0e32\u0e14\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49: S&P 500 / Nasdaq / VIX + \u0e1b\u0e23\u0e30\u0e40\u0e14\u0e47\u0e19\u0e40\u0e14\u0e48\u0e19\u0e02\u0e2d\u0e07\u0e02\u0e48\u0e32\u0e27 (\u0e43\u0e0a\u0e49\u0e15\u0e31\u0e27\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e41\u0e17\u0e47\u0e1a "\u0e2a\u0e23\u0e38\u0e1b\u0e15\u0e25\u0e32\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49")
 2) \u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e19 Watchlist \u0e17\u0e35\u0e48\u0e08\u0e30\u0e2d\u0e2d\u0e01\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19
 3) \u0e2b\u0e38\u0e49\u0e19\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e17\u0e35\u0e48\u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32 3 \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01 (\u0e43\u0e0a\u0e49\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32 \u26a1 \u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07) \u0e01\u0e14\u0e1b\u0e38\u0e48\u0e21\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2d\u0e22\u0e32\u0e01\u0e14\u0e39 \u0e40\u0e1e\u0e23\u0e32\u0e30\u0e2a\u0e41\u0e01\u0e19\u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e43\u0e0a\u0e49\u0e40\u0e27\u0e25\u0e32

\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22 \u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e23\u0e38\u0e1b\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e08\u0e32\u0e01\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e41\u0e25\u0e30\u0e1e\u0e32\u0e14\u0e2b\u0e31\u0e27\u0e02\u0e48\u0e32\u0e27

\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49:
    import morning_ui
    morning_ui.render_morning()
"""
import datetime as _dt
import html as _html

import numpy as np
import streamlit as st

import fast_ui
import market_brief as mb

_UP, _DN = "#19f5a5", "#ff4d6d"

_CYB_CSS = """<style>
.cy-box{border:1px solid rgba(25,211,245,.35);border-left:4px solid var(--c,#19d3f5);background:rgba(10,12,22,.78);padding:9px 13px;margin:8px 0;clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px));}
.cy-top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.cy-lab{font-size:11px;letter-spacing:2px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6}
.cy-st{font-weight:800;letter-spacing:1.5px;font-size:15px;color:var(--c)!important;-webkit-text-fill-color:var(--c);text-shadow:0 0 8px var(--c)}
.cy-track{height:7px;background:rgba(255,255,255,.08);margin:7px 0 5px;position:relative;overflow:hidden}
.cy-track i{display:block;height:100%;background:var(--c);box-shadow:0 0 10px var(--c)}
.cy-note{font-size:12.5px;color:#aab3d1!important;-webkit-text-fill-color:#aab3d1}
.cy-lg{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.cy-lg span{font-size:12px;padding:2px 9px;border:1px solid rgba(255,255,255,.12);color:#8d96b5!important;-webkit-text-fill-color:#8d96b5}
.cy-lg span.on{border-color:var(--c2);color:var(--c2)!important;-webkit-text-fill-color:var(--c2);font-weight:800;background:rgba(255,255,255,.05)}
.cy-pulse{animation:cyp 2.4s ease-in-out infinite}
@keyframes cyp{0%,100%{opacity:1}50%{opacity:.55}}
@media (prefers-reduced-motion:reduce){.cy-pulse{animation:none}}
</style>"""



def _e(x):
    return _html.escape(str(x), quote=True)


def _cyber_meter(vix):
    """\u0e21\u0e32\u0e15\u0e23\u0e27\u0e31\u0e14\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27\u0e02\u0e2d\u0e07\u0e15\u0e25\u0e32\u0e14 (\u0e1c\u0e39\u0e01\u0e01\u0e31\u0e1a VIX) \u0e41\u0e1a\u0e1a Cyberpsychosis \u0e43\u0e19 Edgerunners"""
    if vix is None:
        return
    if vix >= 30:
        lv, col, th, pulse = "CYBERPSYCHO ALERT", "#ff4d6d", "\u0e15\u0e25\u0e32\u0e14\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27\u0e2a\u0e39\u0e07\u0e21\u0e32\u0e01 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 \u0e25\u0e14\u0e44\u0e21\u0e49 \u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07", True
    elif vix >= 22:
        lv, col, th, pulse = "CYBERPSYCHO WARNING", "#ff9f43", "\u0e15\u0e25\u0e32\u0e14\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07\u0e02\u0e36\u0e49\u0e19 \u0e23\u0e30\u0e27\u0e31\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e42\u0e14\u0e19\u0e07\u0e48\u0e32\u0e22", True
    elif vix >= 16:
        lv, col, th, pulse = "EDGY", "#fcee0a", "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e23\u0e30\u0e41\u0e27\u0e07 \u0e22\u0e31\u0e07\u0e1e\u0e2d\u0e1b\u0e01\u0e15\u0e34 \u0e41\u0e15\u0e48\u0e04\u0e27\u0e23\u0e40\u0e1d\u0e49\u0e32\u0e14\u0e39", False
    else:
        lv, col, th, pulse = "STABLE", "#19d3f5", "\u0e15\u0e25\u0e32\u0e14\u0e19\u0e34\u0e48\u0e07 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e01\u0e27\u0e48\u0e07\u0e19\u0e49\u0e2d\u0e22", False
    w = max(4.0, min(vix / 45.0, 1.0) * 100.0)
    lv_i = 3 if vix >= 30 else (2 if vix >= 22 else (1 if vix >= 16 else 0))
    legs = [("\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 16", "\u0e19\u0e34\u0e48\u0e07", "#19d3f5"), ("16-22", "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e23\u0e30\u0e41\u0e27\u0e07", "#fcee0a"), ("22-30", "\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27", "#ff9f43"), ("30 \u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b", "\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27\u0e2a\u0e39\u0e07\u0e21\u0e32\u0e01", "#ff4d6d")]
    leg = "".join('<span class="%s" style="--c2:%s">%s = %s%s</span>' % ("on" if i == lv_i else "", c, r, n, " \u2190 \u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49" if i == lv_i else "") for i, (r, n, c) in enumerate(legs))
    st.markdown(_CYB_CSS + '<div class="cy-box" style="--c:%s"><div class="cy-top"><span class="cy-lab">CYBERPSYCHOSIS METER \xb7 \u0e23\u0e30\u0e14\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27\u0e02\u0e2d\u0e07\u0e15\u0e25\u0e32\u0e14</span>'
                '<span class="cy-st%s">%s \xb7 VIX %.1f</span></div><div class="cy-track"><i style="width:%.0f%%"></i></div>'
                '<div class="cy-note">%s</div><div class="cy-lg">%s</div>'
                '<div class="cy-note" style="margin-top:6px;font-size:12px">VIX \u0e04\u0e37\u0e2d "\u0e14\u0e31\u0e0a\u0e19\u0e35\u0e04\u0e27\u0e32\u0e21\u0e01\u0e25\u0e31\u0e27" \u0e02\u0e2d\u0e07\u0e15\u0e25\u0e32\u0e14\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e2f \u0e22\u0e34\u0e48\u0e07\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e2a\u0e39\u0e07 \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e22\u0e34\u0e48\u0e07\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07\u0e17\u0e31\u0e49\u0e07\u0e02\u0e36\u0e49\u0e19\u0e41\u0e25\u0e30\u0e25\u0e07 \u0e1b\u0e01\u0e15\u0e34\u0e2d\u0e22\u0e39\u0e48\u0e23\u0e32\u0e27 15-20</div></div>' % (col, " cy-pulse" if pulse else "", lv, vix, w, th, leg), unsafe_allow_html=True)


def _market_block():
    px = mb._prices(("^GSPC", "^IXIC", "^VIX", "CL=F", "^TNX"))
    ix = {s: mb._stats(px[s]) for s in ("^GSPC", "^IXIC") if s in px}
    g = {s: mb._stats(px[s]) for s in ("^VIX", "CL=F", "^TNX") if s in px}
    if not ix:
        st.caption("\U0001f4e1 \u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e02\u0e32\u0e14 // \u0e14\u0e36\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e15\u0e25\u0e32\u0e14\u0e08\u0e32\u0e01 Yahoo \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49")
        return
    sp, nq = ix.get("^GSPC"), ix.get("^IXIC")
    parts = []
    if sp:
        parts.append("S&amp;P 500 \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14 <b style=\"color:%s\">%.1f%%</b> (\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %+.1f%%)" % (mb._c(sp["dd"]), abs(sp["dd"]), sp["d1"]))
    if nq:
        lab, col = mb._regime(nq["dd"])
        parts.append("Nasdaq \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32 <b style=\"color:%s\">%.1f%%</b> (\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 %+.1f%%) <span class=\"mb-tag\" style=\"color:%s;border-color:%s\">%s</span>" % (
            mb._c(nq["dd"]), abs(nq["dd"]), nq["d1"], col, col, _e(lab)))
    vx = g.get("^VIX")
    vnote = ""
    if vx:
        vnote = "VIX %.1f = %s" % (vx["px"], "\u0e15\u0e37\u0e48\u0e19\u0e01\u0e25\u0e31\u0e27\u0e2a\u0e39\u0e07 \u0e23\u0e32\u0e04\u0e32\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07" if vx["px"] >= 30 else ("\u0e40\u0e23\u0e34\u0e48\u0e21\u0e01\u0e31\u0e07\u0e27\u0e25" if vx["px"] >= 20 else "\u0e22\u0e31\u0e07\u0e19\u0e34\u0e48\u0e07"))
    themes = ""
    try:
        rows = mb._headlines()
        down = bool((sp and sp["d5"] <= -1) or (nq and nq["d5"] <= -1))
        th = mb._themes(rows, g, down) if (rows or g) else []
        if th:
            themes = "\u0e1b\u0e23\u0e30\u0e40\u0e14\u0e47\u0e19\u0e40\u0e14\u0e48\u0e19: " + " \xb7 ".join(_e(mb._THEME_NAME[k]) for k, _s, _r, _ev in th[:3])
    except Exception:
        themes = ""
    st.markdown('<div class="mb"><div class="mb-h">\u2600\ufe0f \u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e0a\u0e49\u0e32\u0e19\u0e35\u0e49 (\u0e2d\u0e48\u0e32\u0e19\u0e08\u0e1a\u0e43\u0e19 1 \u0e19\u0e32\u0e17\u0e35)</div>'
                '<div class="mb-me">\U0001F4C8 %s</div><div class="mb-me">\U0001F321\ufe0f %s</div>%s'
                '<div class="mb-note">\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e40\u0e15\u0e47\u0e21\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48 \u0e40\u0e23\u0e14\u0e32\u0e23\u0e4c\u0e02\u0e48\u0e32\u0e27 \u2192 \U0001F4DD \u0e2a\u0e23\u0e38\u0e1b\u0e15\u0e25\u0e32\u0e14\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 \xb7 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1f\u0e23\u0e35\u0e08\u0e32\u0e01 Yahoo \u0e2d\u0e32\u0e08\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c</div></div>' % (
                    " \xb7 ".join(parts), _e(vnote), ('<div class="mb-me">\U0001F4F0 %s</div>' % themes) if themes else ""), unsafe_allow_html=True)
    _cyber_meter(vx["px"] if vx else None)


def _earn_block():
    try:
        import home_ui
        syms = tuple(home_ui._watchlist())
    except Exception:
        syms = ()
    if not syms:
        return
    try:
        em = fast_ui._earn_map(syms)
    except Exception:
        em = {}
    today = _dt.date.today()
    soon = sorted(((d - today).days, s) for s, d in em.items() if d and 0 <= (d - today).days <= 7)
    if soon:
        body = " \xb7 ".join("<b>%s</b> \u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19" % (_e(s), n) for n, s in soon)
        st.markdown('<div class="mb"><div class="mb-h">\U0001F4C5 \u0e07\u0e1a\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e19 Watchlist \u0e17\u0e35\u0e48\u0e08\u0e30\u0e2d\u0e2d\u0e01\u0e43\u0e19 7 \u0e27\u0e31\u0e19</div><div class="mb-me">%s</div>'
                    '<div class="mb-note">\u0e43\u0e01\u0e25\u0e49\u0e27\u0e31\u0e19\u0e07\u0e1a \u0e23\u0e32\u0e04\u0e32\u0e21\u0e31\u0e01\u0e01\u0e23\u0e30\u0e42\u0e14\u0e14\u0e02\u0e49\u0e32\u0e21\u0e04\u0e37\u0e19 \u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e2d\u0e32\u0e08\u0e44\u0e21\u0e48\u0e17\u0e33\u0e07\u0e32\u0e19 \u0e25\u0e14\u0e44\u0e21\u0e49\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e25\u0e35\u0e48\u0e22\u0e07\u0e16\u0e37\u0e2d\u0e02\u0e49\u0e32\u0e21\u0e07\u0e1a</div></div>' % body, unsafe_allow_html=True)
    else:
        st.caption("\U0001F4C5 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e2b\u0e38\u0e49\u0e19\u0e43\u0e19 Watchlist \u0e17\u0e35\u0e48\u0e07\u0e1a\u0e08\u0e30\u0e2d\u0e2d\u0e01\u0e20\u0e32\u0e22\u0e43\u0e19 7 \u0e27\u0e31\u0e19")


def _picks():
    """3 \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07 (\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07 + \u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07 + \u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 + \u0e44\u0e21\u0e48\u0e0b\u0e49\u0e33\u0e01\u0e25\u0e38\u0e48\u0e21 + \u0e07\u0e1a\u0e44\u0e21\u0e48\u0e43\u0e01\u0e25\u0e49) -> ([dict], \u0e08\u0e33\u0e19\u0e27\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19, \u0e21\u0e35\u0e1c\u0e25\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07\u0e44\u0e2b\u0e21)"""
    import screener
    syms = tuple(screener.universe("both"))[:600]
    rows = [x for x in fast_ui._scan(syms) if x.get("dvol", 0) >= 20]
    vinfo = fast_ui._load_valid()
    vset = set((vinfo or {}).get("valid", [])) - fast_ui.REGIME
    spy5 = (fast_ui._market().get("SPY") or {}).get("chg5")
    cand = []
    for r in rows:
        if not fast_ui._rebound(r) or r["atr_pct"] < 3:
            continue
        fl = fast_ui._live_feats(r, spy5)
        k = sum(1 for f in vset if fl.get(f))
        if vset and k < 1:
            continue
        rv = r["rvol"] if r["rvol"] == r["rvol"] else 0.0
        cand.append((k, rv, r, [fast_ui.PLAIN.get(f, f) for f in fast_ui.FEAT_LABEL if f in vset and fl.get(f)]))
    cand.sort(key=lambda x: (-x[0], -x[1]))
    kept = []
    for k, rv, r, lab in cand:
        a = r.get("ret")
        dup = False
        if a is not None and len(a) == 60 and np.isfinite(a[1:]).all():
            for _k, _rv, r2, _l in kept:
                b = r2.get("ret")
                if b is not None and len(b) == 60 and np.isfinite(b[1:]).all() and float(np.corrcoef(a[1:], b[1:])[0, 1]) >= 0.6:
                    dup = True
                    break
        if not dup:
            kept.append((k, rv, r, lab))
        if len(kept) >= 12:
            break
    try:
        em = fast_ui._earn_map(tuple(x[2]["sym"] for x in kept))
    except Exception:
        em = {}
    today = _dt.date.today()
    out = []
    for k, rv, r, lab in kept:
        d = em.get(r["sym"])
        if d and 0 <= (d - today).days <= 7:
            continue
        out.append({"sym": r["sym"], "px": r["px"], "chg5": r["chg5"], "dist": r["dist_hi"], "lab": lab})
    return out[:3], len(cand), bool(vset)


def _picks_block():
    if st.session_state.get("mo_picks") is None:
        if st.button("\U0001F50E \u0e14\u0e39\u0e2b\u0e38\u0e49\u0e19\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e17\u0e35\u0e48\u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32 3 \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01 (\u0e2a\u0e41\u0e01\u0e19\u0e17\u0e31\u0e49\u0e07\u0e15\u0e25\u0e32\u0e14 \u0e04\u0e23\u0e31\u0e49\u0e07\u0e41\u0e23\u0e01\u0e2d\u0e32\u0e08\u0e43\u0e0a\u0e49 30-60 \u0e27\u0e34\u0e19\u0e32\u0e17\u0e35)", key="mo_go"):
            with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e41\u0e08\u0e47\u0e04\u0e2d\u0e34\u0e19\u0e2a\u0e41\u0e01\u0e19 Nasdaq 100 + S&P 500 ..."):
                try:
                    st.session_state["mo_picks"] = _picks()
                except Exception as ex:
                    st.warning("\U0001f4e1 \u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e02\u0e32\u0e14 // \u0e2a\u0e41\u0e01\u0e19\u0e44\u0e21\u0e48\u0e2a\u0e33\u0e40\u0e23\u0e47\u0e08: %s" % str(ex)[:80])
        else:
            return
    res = st.session_state.get("mo_picks")
    if not res:
        return
    picks, n_all, has_valid = res
    if not picks:
        st.info("\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c\u0e0a\u0e31\u0e14\u0e40\u0e08\u0e19 \u0e44\u0e21\u0e48\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e47\u0e44\u0e21\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e23")
        return
    boxes = ""
    for p in picks:
        chips = "".join('<span class="sm-t ok" style="display:inline-block;margin:2px 4px 0 0;padding:1px 7px;border:1px solid rgba(252,238,10,.6);color:#fcee0a;font-size:11.5px">\u2713 %s</span>' % _e(x) for x in p["lab"])
        boxes += ('<div class="mb-box"><div class="t">\u0e23\u0e48\u0e27\u0e07\u0e08\u0e32\u0e01\u0e08\u0e38\u0e14\u0e2a\u0e39\u0e07 20 \u0e27\u0e31\u0e19 <b style="color:%s">%+.0f%%</b></div><div class="v">%s</div>'
                  '<div class="s" style="color:%s">%s \xb7 5 \u0e27\u0e31\u0e19 %+.1f%%</div><div>%s</div></div>') % (
            _DN, p["dist"], _e(p["sym"]), _DN if p["chg5"] < 0 else _UP, "%.2f" % p["px"], p["chg5"], chips)
    note = "" if has_valid else " \xb7 <b>\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e23\u0e31\u0e19\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e22\u0e49\u0e2d\u0e19\u0e2b\u0e25\u0e31\u0e07</b> \u0e17\u0e35\u0e48\u0e2b\u0e19\u0e49\u0e32 \u26a1 \u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07 \u0e15\u0e31\u0e27\u0e01\u0e23\u0e2d\u0e07\u0e08\u0e36\u0e07\u0e2b\u0e25\u0e27\u0e21\u0e01\u0e27\u0e48\u0e32"
    st.markdown('<div class="mb"><div class="mb-h">\U0001F3AF \u0e2b\u0e38\u0e49\u0e19\u0e23\u0e48\u0e27\u0e07\u0e41\u0e23\u0e07\u0e17\u0e35\u0e48\u0e19\u0e48\u0e32\u0e28\u0e36\u0e01\u0e29\u0e32 3 \u0e15\u0e31\u0e27\u0e41\u0e23\u0e01 (\u0e08\u0e32\u0e01 %d \u0e15\u0e31\u0e27\u0e17\u0e35\u0e48\u0e1c\u0e48\u0e32\u0e19\u0e40\u0e01\u0e13\u0e11\u0e4c)</div><div class="mb-g">%s</div>'
                '<div class="mb-note">\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e2a\u0e31\u0e0d\u0e0d\u0e32\u0e13\u0e0b\u0e37\u0e49\u0e2d \xb7 \u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25 \u0e02\u0e48\u0e32\u0e27 \u0e41\u0e25\u0e30\u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32\u0e2d\u0e22\u0e39\u0e48\u0e17\u0e35\u0e48\u0e2b\u0e19\u0e49\u0e32 \u26a1 \u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07 \xb7 \u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07%s</div></div>' % (n_all, boxes, note), unsafe_allow_html=True)
    if st.button("\U0001F504 \u0e2a\u0e41\u0e01\u0e19\u0e43\u0e2b\u0e21\u0e48", key="mo_re"):
        st.session_state["mo_picks"] = None
        st.rerun()


def render_morning():
    st.markdown(mb._CSS, unsafe_allow_html=True)
    with st.spinner("\u0e01\u0e33\u0e25\u0e31\u0e07\u0e41\u0e08\u0e47\u0e04\u0e2d\u0e34\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e15\u0e25\u0e32\u0e14\u0e40\u0e0a\u0e49\u0e32\u0e19\u0e35\u0e49 ..."):
        _market_block()
    _earn_block()
    _picks_block()