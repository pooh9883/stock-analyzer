# -*- coding: utf-8 -*-
"""journal_ui.py - TRADE LOG \xb7 \u0e2a\u0e21\u0e38\u0e14\u0e40\u0e17\u0e23\u0e14 (\u0e41\u0e19\u0e27 Cyberpunk Edgerunners)

\u0e08\u0e14\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e40\u0e02\u0e49\u0e32 (\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 \xb7 \u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 \xb7 \u0e40\u0e1b\u0e49\u0e32) \u0e41\u0e25\u0e49\u0e27\u0e14\u0e39\u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e2a\u0e14\u0e17\u0e38\u0e01\u0e44\u0e21\u0e49\u0e43\u0e19\u0e17\u0e35\u0e48\u0e40\u0e14\u0e35\u0e22\u0e27
 - \u0e23\u0e32\u0e04\u0e32\u0e16\u0e36\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 = \u0e1b\u0e49\u0e32\u0e22 FLATLINE (\u0e40\u0e15\u0e37\u0e2d\u0e19\u0e43\u0e2b\u0e49\u0e2d\u0e2d\u0e01)
 - R = \u0e01\u0e33\u0e44\u0e23/\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e40\u0e17\u0e35\u0e22\u0e1a\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e15\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32 (1R = \u0e40\u0e2a\u0e35\u0e22\u0e40\u0e17\u0e48\u0e32\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e43\u0e08\u0e44\u0e27\u0e49)
 - \u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e23\u0e27\u0e21 = \u0e16\u0e49\u0e32\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e38\u0e01\u0e44\u0e21\u0e49\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19\u0e08\u0e30\u0e40\u0e2a\u0e35\u0e22\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23
 - \u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e43\u0e01\u0e25\u0e49\u0e27\u0e31\u0e19\u0e07\u0e1a\u0e21\u0e35\u0e1b\u0e49\u0e32\u0e22\u0e40\u0e15\u0e37\u0e2d\u0e19
 - \u0e1b\u0e34\u0e14\u0e44\u0e21\u0e49\u0e41\u0e25\u0e49\u0e27\u0e40\u0e01\u0e47\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34 + \u0e2a\u0e16\u0e34\u0e15\u0e34\u0e0a\u0e19\u0e30/\u0e41\u0e1e\u0e49

\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e01\u0e47\u0e1a\u0e43\u0e19\u0e44\u0e1f\u0e25\u0e4c trade_journal.json \u0e02\u0e49\u0e32\u0e07\u0e44\u0e1f\u0e25\u0e4c\u0e19\u0e35\u0e49 (\u0e2d\u0e22\u0e39\u0e48\u0e43\u0e19\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e2a\u0e48\u0e07\u0e2d\u0e2d\u0e01\u0e44\u0e1b\u0e44\u0e2b\u0e19)
\u26a0\ufe0f \u0e23\u0e30\u0e1a\u0e1a\u0e19\u0e35\u0e49 "\u0e40\u0e15\u0e37\u0e2d\u0e19" \u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e2a\u0e48\u0e07\u0e04\u0e33\u0e2a\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e02\u0e32\u0e22\u0e08\u0e23\u0e34\u0e07 \u0e23\u0e32\u0e04\u0e32\u0e08\u0e32\u0e01 Yahoo \u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c\u0e23\u0e32\u0e27 15 \u0e19\u0e32\u0e17\u0e35 \u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e16\u0e37\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e27\u0e31\u0e19\u0e46
   (\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1d\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d/\u0e16\u0e37\u0e2d\u0e22\u0e32\u0e27 \u0e44\u0e21\u0e48\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a short)

\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49:
    import journal_ui
    journal_ui.render_journal()
"""
import datetime as _dt
import html as _html
import json
import os
import uuid

import streamlit as st

_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trade_journal.json")
_UP, _DN, _GOLD, _CY, _MUT = "#19f5a5", "#ff4d6d", "#fcee0a", "#19d3f5", "#7d86a6"

_CSS = """<style>
.tj-note{border-left:3px solid #fcee0a;background:rgba(252,238,10,.06);padding:8px 12px;margin:4px 0 10px;font-size:13px;color:#cfd6ee!important;-webkit-text-fill-color:#cfd6ee}
.tj-sum{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin:8px 0 12px}
.tj-sb{border:1px solid rgba(25,211,245,.3);background:rgba(10,12,22,.75);padding:9px 12px;clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px))}
.tj-sb .t{font-size:11.5px;letter-spacing:1px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6}
.tj-sb .v{font-size:22px;font-weight:800;margin-top:2px}
.tj-sb .s{font-size:12px;color:#aab3d1!important;-webkit-text-fill-color:#aab3d1}
.tj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.tj-card{border:1px solid rgba(255,255,255,.1);border-top:3px solid var(--c);background:rgba(10,12,22,.8);padding:11px 13px;clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}
.tj-card.flat{box-shadow:0 0 14px rgba(255,77,109,.35) inset}
.tj-top{display:flex;justify-content:space-between;align-items:center;gap:8px}
.tj-sym{font-size:20px;font-weight:900;letter-spacing:1px}
.tj-st{font-size:11.5px;font-weight:800;letter-spacing:1.5px;color:var(--c)!important;-webkit-text-fill-color:var(--c);border:1px solid var(--c);padding:1px 8px}
.tj-st.pulse{animation:tjp 1.8s ease-in-out infinite}
@keyframes tjp{0%,100%{opacity:1}50%{opacity:.5}}
@media (prefers-reduced-motion:reduce){.tj-st.pulse{animation:none}}
.tj-pl{font-size:21px;font-weight:800;margin:6px 0 2px}
.tj-sub{font-size:12.5px;color:#aab3d1!important;-webkit-text-fill-color:#aab3d1}
.tj-track{position:relative;height:8px;background:rgba(255,255,255,.08);margin:10px 0 3px}
.tj-track i{position:absolute;top:-3px;width:3px;height:14px;background:#fff}
.tj-track b{position:absolute;top:0;left:0;height:100%;background:var(--c);opacity:.55}
.tj-lab{display:flex;justify-content:space-between;font-size:11.5px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6}
.tj-tag{display:inline-block;margin:5px 5px 0 0;padding:1px 8px;border:1px solid rgba(255,159,67,.7);color:#ff9f43!important;-webkit-text-fill-color:#ff9f43;font-size:12px}
.tj-card ul{margin:5px 0 0 16px;padding:0;font-size:12.5px}
.tj-log{font-family:ui-monospace,Consolas,monospace;font-size:10.5px;letter-spacing:1.5px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6;margin-bottom:3px}
.tj-ecg{font-family:ui-monospace,Consolas,monospace;font-size:15px;line-height:1;white-space:nowrap;overflow:hidden;color:var(--c)!important;-webkit-text-fill-color:var(--c);opacity:.85;margin:7px 0 2px;text-shadow:0 0 6px var(--c)}
.tj-card.flat .tj-ecg{animation:tjp 1.8s ease-in-out infinite}
.tj-card:before{content:"";position:absolute;left:0;top:0;width:14px;height:14px;border-left:2px solid var(--c);border-top:2px solid var(--c);opacity:.8}
.tj-card{position:relative}
</style>"""


def _e(x):
    return _html.escape(str(x), quote=True)


# ---------------------------------------------------------------
# \u0e40\u0e01\u0e47\u0e1a\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25
# ---------------------------------------------------------------
def _load():
    try:
        with open(_FILE, "r", encoding="utf-8") as f:
            d = json.load(f)
        if isinstance(d, dict) and isinstance(d.get("trades"), list):
            return d
    except Exception:
        pass
    return {"account": 0.0, "trades": []}


def _save(d):
    """\u0e40\u0e02\u0e35\u0e22\u0e19\u0e41\u0e1a\u0e1a\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22 (\u0e40\u0e02\u0e35\u0e22\u0e19\u0e44\u0e1f\u0e25\u0e4c\u0e0a\u0e31\u0e48\u0e27\u0e04\u0e23\u0e32\u0e27\u0e01\u0e48\u0e2d\u0e19\u0e41\u0e25\u0e49\u0e27\u0e04\u0e48\u0e2d\u0e22\u0e41\u0e17\u0e19) -> True/False"""
    try:
        tmp = _FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        os.replace(tmp, _FILE)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------
# \u0e04\u0e33\u0e19\u0e27\u0e13 (\u0e41\u0e22\u0e01\u0e40\u0e1b\u0e47\u0e19\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19\u0e25\u0e49\u0e27\u0e19\u0e46 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e17\u0e14\u0e2a\u0e2d\u0e1a\u0e44\u0e14\u0e49)
# ---------------------------------------------------------------
def analyze(t, price):
    """t = \u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e34\u0e14\u0e2d\u0e22\u0e39\u0e48 (dict), price = \u0e23\u0e32\u0e04\u0e32\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14 \u0e2b\u0e23\u0e37\u0e2d None -> dict \u0e1c\u0e25\u0e04\u0e33\u0e19\u0e27\u0e13
    status: FLATLINE (\u0e23\u0e32\u0e04\u0e32<=\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19) | DANGER (\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2b\u0e48\u0e32\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14 <=1.5%) | PROFIT | HOLD | NOPRICE"""
    entry, stop, qty = float(t["entry"]), float(t["stop"]), float(t["qty"])
    risk_ps = entry - stop
    out = {"risk_ps": risk_ps, "risk_total": risk_ps * qty, "cost": entry * qty, "price": price}
    tgt = t.get("target")
    tgt = float(tgt) if tgt else None
    out["target"] = tgt
    if price is None or price != price:
        out.update(status="NOPRICE", pl=None, plp=None, r=None, to_stop=None, pos=None)
        return out
    pl = (price - entry) * qty
    out["pl"] = pl
    out["plp"] = (price / entry - 1.0) * 100.0
    out["r"] = (price - entry) / risk_ps if risk_ps > 0 else None
    out["to_stop"] = (price / stop - 1.0) * 100.0 if stop > 0 else None
    hi = tgt if (tgt and tgt > entry) else entry + 2.0 * risk_ps
    span = hi - stop
    out["pos"] = max(0.0, min(1.0, (price - stop) / span)) if span > 0 else 0.0
    out["entry_pos"] = max(0.0, min(1.0, (entry - stop) / span)) if span > 0 else 0.0
    if price <= stop:
        st_ = "FLATLINE"
    elif out["to_stop"] is not None and out["to_stop"] <= 1.5:
        st_ = "DANGER"
    elif price > entry:
        st_ = "PROFIT"
    else:
        st_ = "HOLD"
    out["status"] = st_
    return out


def resolve(entry, stop, stop_pct, qty, money, risk_d, frac=False):
    """\u0e41\u0e1b\u0e25\u0e07\u0e2a\u0e34\u0e48\u0e07\u0e17\u0e35\u0e48\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e01\u0e23\u0e2d\u0e01\u0e43\u0e2b\u0e49\u0e40\u0e1b\u0e47\u0e19 (\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e23\u0e32\u0e04\u0e32, \u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19)
    \u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19: \u0e43\u0e2a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e21\u0e32\u0e01\u0e48\u0e2d\u0e19 \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e43\u0e2a\u0e48\u0e43\u0e0a\u0e49 % \u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e43\u0e2b\u0e49\u0e25\u0e07
    \u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19: \u0e43\u0e2a\u0e48\u0e08\u0e33\u0e19\u0e27\u0e19\u0e21\u0e32\u0e01\u0e48\u0e2d\u0e19 \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e43\u0e2a\u0e48\u0e43\u0e0a\u0e49 '\u0e25\u0e07\u0e40\u0e07\u0e34\u0e19\u0e01\u0e35\u0e48 $' \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e43\u0e2a\u0e48\u0e43\u0e0a\u0e49 '\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e44\u0e14\u0e49\u0e01\u0e35\u0e48 $' (\u0e2b\u0e32\u0e23\u0e14\u0e49\u0e27\u0e22\u0e23\u0e30\u0e22\u0e30\u0e2b\u0e48\u0e32\u0e07\u0e16\u0e36\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14)
    \u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e1b\u0e31\u0e14\u0e25\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e08\u0e33\u0e19\u0e27\u0e19\u0e40\u0e15\u0e47\u0e21 (\u0e02\u0e31\u0e49\u0e19\u0e15\u0e48\u0e33 1 \u0e16\u0e49\u0e32\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e14\u0e49 >0) \u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e04\u0e37\u0e19 0"""
    entry = float(entry or 0)
    st_ = float(stop or 0)
    if st_ <= 0 and stop_pct and entry > 0:
        st_ = round(entry * (1.0 - float(stop_pct) / 100.0), 4)
    q = float(qty or 0)
    if q <= 0 and money and entry > 0:
        q = float(money) / entry
    if q <= 0 and risk_d and entry > 0 and 0 < st_ < entry:
        q = float(risk_d) / (entry - st_)
    if q > 0 and not float(qty or 0) > 0:
        if frac:
            q = round(q, 4)
        else:
            q = float(int(q)) if q >= 1 else 0.0
    return st_, q


def validate(sym, qty, entry, stop, target):
    """\u0e15\u0e23\u0e27\u0e08\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e17\u0e35\u0e48\u0e01\u0e23\u0e2d\u0e01 -> \u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e1c\u0e34\u0e14\u0e1e\u0e25\u0e32\u0e14 \u0e2b\u0e23\u0e37\u0e2d '' \u0e16\u0e49\u0e32\u0e43\u0e0a\u0e49\u0e44\u0e14\u0e49"""
    if not sym or not sym.strip():
        return "\u0e43\u0e2a\u0e48\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19\u0e01\u0e48\u0e2d\u0e19"
    if not qty or qty <= 0:
        return "\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32 0"
    if not entry or entry <= 0:
        return "\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32 0"
    if not stop or stop <= 0:
        return "\u0e43\u0e2a\u0e48\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e14\u0e49\u0e27\u0e22 (\u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e2b\u0e31\u0e27\u0e43\u0e08\u0e02\u0e2d\u0e07\u0e2a\u0e21\u0e38\u0e14\u0e19\u0e35\u0e49 \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e15\u0e31\u0e49\u0e07 \u0e08\u0e30\u0e44\u0e21\u0e48\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23)"
    if stop >= entry:
        return "\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 (\u0e2a\u0e21\u0e38\u0e14\u0e19\u0e35\u0e49\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1d\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d)"
    if target and target <= entry:
        return "\u0e40\u0e1b\u0e49\u0e32\u0e01\u0e33\u0e44\u0e23\u0e15\u0e49\u0e2d\u0e07\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e40\u0e02\u0e49\u0e32 (\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e27\u0e49\u0e19\u0e27\u0e48\u0e32\u0e07\u0e44\u0e27\u0e49)"
    return ""


def closed_stats(closed):
    """\u0e2a\u0e16\u0e34\u0e15\u0e34\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e1b\u0e34\u0e14\u0e41\u0e25\u0e49\u0e27 -> dict"""
    n = len(closed)
    if not n:
        return {"n": 0}
    pls = [(c["exit"] - c["entry"]) * c["qty"] for c in closed]
    rs = [((c["exit"] - c["entry"]) / (c["entry"] - c["stop"])) if c["entry"] > c["stop"] else 0.0 for c in closed]
    wins = [p for p in pls if p > 0]
    loss = [p for p in pls if p <= 0]
    return {"n": n, "wins": len(wins), "loss": len(loss), "total": sum(pls),
            "avg_win": (sum(wins) / len(wins)) if wins else 0.0,
            "avg_loss": (sum(loss) / len(loss)) if loss else 0.0,
            "avg_r": sum(rs) / n,
            "worst_r": min(rs)}


# ---------------------------------------------------------------
# \u0e23\u0e32\u0e04\u0e32 / \u0e07\u0e1a
# ---------------------------------------------------------------
@st.cache_data(ttl=60, show_spinner=False)
def _prices(symbols):
    import yfinance as yf
    out = {}
    syms = list(symbols)
    if not syms:
        return out
    try:
        d = yf.download(" ".join(syms), period="5d", interval="1d", group_by="ticker", progress=False, auto_adjust=True)
    except Exception:
        return out
    for s in syms:
        try:
            c = (d["Close"] if len(syms) == 1 and "Close" in d else d[s]["Close"]).dropna()
            if len(c):
                out[s] = float(c.iloc[-1])
        except Exception:
            pass
    return out


def _earn_days(symbols):
    """{sym: \u0e08\u0e33\u0e19\u0e27\u0e19\u0e27\u0e31\u0e19\u0e16\u0e36\u0e07\u0e27\u0e31\u0e19\u0e07\u0e1a} \u0e40\u0e09\u0e1e\u0e32\u0e30\u0e17\u0e35\u0e48 <= 7 \u0e27\u0e31\u0e19 (\u0e43\u0e0a\u0e49\u0e15\u0e31\u0e27\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07 \u0e16\u0e49\u0e32\u0e14\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e01\u0e47\u0e02\u0e49\u0e32\u0e21)"""
    try:
        import fast_ui
        em = fast_ui._earn_map(tuple(symbols))
    except Exception:
        return {}
    today = _dt.date.today()
    out = {}
    for s, d in (em or {}).items():
        try:
            n = (d - today).days
            if 0 <= n <= 7:
                out[s] = n
        except Exception:
            pass
    return out


def _fmt(v, d=2):
    return ("{:,.%df}" % d).format(v)


_FX = {"v": None}


@st.cache_data(ttl=600, show_spinner=False)
def _fx_rate():
    """\u0e2d\u0e31\u0e15\u0e23\u0e32 USD/THB (\u0e1a\u0e32\u0e17\u0e15\u0e48\u0e2d 1 \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c) \u0e08\u0e32\u0e01 Yahoo \u0e14\u0e36\u0e07\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e04\u0e37\u0e19 None"""
    try:
        import yfinance as yf
        d = yf.download("THB=X", period="5d", interval="1d", progress=False, auto_adjust=True)
        c = d["Close"].dropna()
        v = float(c.iloc[-1].iloc[0]) if hasattr(c.iloc[-1], "iloc") else float(c.iloc[-1])
        return v if 20 < v < 60 else None
    except Exception:
        return None


def _bt(v_usd):
    """\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e1a\u0e32\u0e17\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e15\u0e48\u0e2d\u0e17\u0e49\u0e32\u0e22\u0e08\u0e33\u0e19\u0e27\u0e19\u0e40\u0e07\u0e34\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c \u0e40\u0e0a\u0e48\u0e19 ' (\u2248 \u0e3f7,200)' \u0e16\u0e49\u0e32\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e04\u0e37\u0e19\u0e27\u0e48\u0e32\u0e07"""
    fx = _FX["v"]
    if not fx:
        return ""
    return " (\u2248 %s\u0e3f%s)" % ("-" if v_usd < 0 else "", "{:,.0f}".format(abs(v_usd) * fx))


def _bts(v_usd):
    """\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19 _bt \u0e41\u0e15\u0e48\u0e2b\u0e48\u0e2d\u0e14\u0e49\u0e27\u0e22\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e40\u0e25\u0e47\u0e01 (\u0e43\u0e0a\u0e49\u0e43\u0e19\u0e01\u0e25\u0e48\u0e2d\u0e07\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e43\u0e2b\u0e0d\u0e48)"""
    t = _bt(v_usd)
    return ('<span style="font-size:13px;font-weight:600">%s</span>' % t) if t else ""


def _money(v):
    return ("+" if v >= 0 else "-") + "$" + _fmt(abs(v))


# ---------------------------------------------------------------
# \u0e41\u0e2a\u0e14\u0e07\u0e1c\u0e25
# ---------------------------------------------------------------
_ST = {
    "FLATLINE": (_DN, "FLATLINE", True),
    "DANGER": ("#ff9f43", "\u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14", True),
    "PROFIT": (_UP, "\u0e01\u0e33\u0e44\u0e23", False),
    "HOLD": (_CY, "\u0e16\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48", False),
    "NOPRICE": (_MUT, "\u0e44\u0e21\u0e48\u0e21\u0e35\u0e23\u0e32\u0e04\u0e32", False),
}


_ECG = {
    "FLATLINE": "\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581\u2581",
    "DANGER": "\u2581\u2582\u2586\u2583\u2581\u2583\u2587\u2582\u2581\u2582\u2586\u2583\u2581\u2583\u2587\u2582\u2581\u2582\u2586\u2583\u2581\u2583\u2587\u2582\u2581\u2582\u2586\u2583\u2581\u2583",
    "PROFIT": "\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583",
    "HOLD": "\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583\u2581\u2581\u2581\u2582\u2587\u2583",
    "NOPRICE": "\u2581" * 30,
}


def _card(t, a, earn_n, no=0):
    col, lab, pulse = _ST[a["status"]]
    sym = t["sym"]
    if a["status"] == "NOPRICE":
        body = '<div class="tj-sub" style="margin-top:8px">\u0e14\u0e36\u0e07\u0e23\u0e32\u0e04\u0e32\u0e25\u0e48\u0e32\u0e2a\u0e38\u0e14\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 (Yahoo \u0e2d\u0e32\u0e08\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c) \u0e25\u0e2d\u0e07\u0e43\u0e2b\u0e21\u0e48\u0e43\u0e19\u0e2d\u0e35\u0e01\u0e2a\u0e31\u0e01\u0e04\u0e23\u0e39\u0e48</div>'
    else:
        plc = _UP if a["pl"] >= 0 else _DN
        rtxt = ""
        if a["r"] is not None:
            rtxt = " \xb7 %+.1fR" % a["r"]
        pos = a["pos"] * 100.0
        ep = a.get("entry_pos", 0) * 100.0
        hi_lab = ("\u0e40\u0e1b\u0e49\u0e32 %s" % _fmt(a["target"])) if a["target"] else ("+2R %s" % _fmt(t["entry"] + 2 * a["risk_ps"]))
        body = ('<div class="tj-pl" style="color:%s!important;-webkit-text-fill-color:%s">%s <span style="font-size:14px">(%+.1f%%%s)</span></div>'
                '<div class="tj-sub">\u0e23\u0e32\u0e04\u0e32\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 %s \xb7 \u0e40\u0e02\u0e49\u0e32 %s \xb7 %s \u0e2b\u0e38\u0e49\u0e19%s</div>'
                '<div class="tj-track"><b style="width:%.0f%%"></b><i style="left:%.0f%%;background:#7d86a6;opacity:.8"></i><i style="left:calc(%.0f%% - 1px)"></i></div>'
                '<div class="tj-lab"><span>\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 %s</span><span>%s</span></div>') % (
            plc, plc, _money(a["pl"]), a["plp"], rtxt, _fmt(a["price"]), _fmt(t["entry"]), _fmt(t["qty"], 0) if float(t["qty"]).is_integer() else _fmt(t["qty"], 2),
            (" \xb7 \u0e01\u0e33\u0e44\u0e23/\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19" + _bt(a["pl"]).replace(" (", " ").replace(")", "")) if _FX["v"] else "",
            pos, ep, pos, _fmt(t["stop"]), hi_lab)
    notes = []
    if a["status"] == "FLATLINE":
        notes.append("\u0e23\u0e32\u0e04\u0e32\u0e25\u0e07\u0e21\u0e32\u0e16\u0e36\u0e07\u0e2b\u0e23\u0e37\u0e2d\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e44\u0e27\u0e49 \u0e16\u0e36\u0e07\u0e40\u0e27\u0e25\u0e32\u0e17\u0e33\u0e15\u0e32\u0e21\u0e41\u0e1c\u0e19 (\u0e23\u0e30\u0e1a\u0e1a\u0e19\u0e35\u0e49\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e02\u0e32\u0e22\u0e43\u0e2b\u0e49 \u0e04\u0e38\u0e13\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e14\u0e02\u0e32\u0e22\u0e40\u0e2d\u0e07)")
    elif a["status"] == "DANGER":
        notes.append("\u0e23\u0e32\u0e04\u0e32\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2b\u0e48\u0e32\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e41\u0e04\u0e48 %.1f%% \u0e40\u0e15\u0e23\u0e35\u0e22\u0e21\u0e15\u0e31\u0e27\u0e44\u0e27\u0e49" % a["to_stop"])
    notes.append("\u0e16\u0e49\u0e32\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 \u0e08\u0e30\u0e40\u0e2a\u0e35\u0e22 %s%s (%.1f%% \u0e02\u0e2d\u0e07\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07)" % ("$" + _fmt(a["risk_total"]), _bt(a["risk_total"]), a["risk_ps"] / t["entry"] * 100.0))
    tags = ""
    if earn_n is not None:
        tags += '<span class="tj-tag">\U0001F4C5 \u0e07\u0e1a\u0e2d\u0e2d\u0e01\u0e2d\u0e35\u0e01 %d \u0e27\u0e31\u0e19 \u0e23\u0e32\u0e04\u0e32\u0e2d\u0e32\u0e08\u0e01\u0e23\u0e30\u0e42\u0e14\u0e14\u0e02\u0e49\u0e32\u0e21\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19</span>' % earn_n
    if t.get("note"):
        notes.append("\u0e42\u0e19\u0e49\u0e15: " + t["note"])
    ul = "<ul>" + "".join("<li>%s</li>" % _e(x) for x in notes) + "</ul>"
    cls = "tj-card flat" if a["status"] == "FLATLINE" else "tj-card"
    logh = '<div class="tj-log">LOG #%03d \u00b7 %s</div>' % (no, _e(t.get("opened", "")))
    ecg = '<div class="tj-ecg">%s</div>' % _ECG.get(a["status"], "")
    return ('<div class="%s" style="--c:%s">%s<div class="tj-top"><span class="tj-sym">%s</span><span class="tj-st%s">%s</span></div>%s%s%s%s</div>') % (
        cls, col, logh, _e(sym), " pulse" if pulse else "", lab, ecg, body, tags, ul)


def _summary(trades, ans, account):
    live = [(t, a) for t, a in zip(trades, ans) if a["status"] != "NOPRICE"]
    pl = sum(a["pl"] for _t, a in live)
    risk = sum(a["risk_total"] for a in ans)
    cost = sum(a["cost"] for a in ans)
    flat = sum(1 for a in ans if a["status"] == "FLATLINE")
    danger = sum(1 for a in ans if a["status"] == "DANGER")
    plc = _UP if pl >= 0 else _DN
    riskp = ("%.1f%% \u0e02\u0e2d\u0e07\u0e1e\u0e2d\u0e23\u0e4c\u0e15" % (risk / account * 100.0)) if account and account > 0 else "\u0e43\u0e2a\u0e48\u0e02\u0e19\u0e32\u0e14\u0e1e\u0e2d\u0e23\u0e4c\u0e15\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e14\u0e39 %"
    rcol = _CY
    if account and account > 0:
        rp = risk / account * 100.0
        rcol = _UP if rp <= 3 else ("#ff9f43" if rp <= 6 else _DN)
    alert = ""
    if flat:
        alert = ('<div class="tj-sb" style="border-color:%s"><div class="t">\u0e40\u0e15\u0e37\u0e2d\u0e19</div><div class="v" style="color:%s!important;-webkit-text-fill-color:%s">%d FLATLINE</div>'
                 '<div class="s">\u0e16\u0e36\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e41\u0e25\u0e49\u0e27</div></div>') % (_DN, _DN, _DN, flat)
    elif danger:
        alert = ('<div class="tj-sb" style="border-color:#ff9f43"><div class="t">\u0e40\u0e15\u0e37\u0e2d\u0e19</div><div class="v" style="color:#ff9f43!important;-webkit-text-fill-color:#ff9f43">%d \u0e43\u0e01\u0e25\u0e49\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14</div>'
                 '<div class="s">\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e2b\u0e48\u0e32\u0e07\u0e44\u0e21\u0e48\u0e16\u0e36\u0e07 1.5%%</div></div>') % danger
    return ('<div class="tj-sum">'
            '<div class="tj-sb"><div class="t">\u0e01\u0e33\u0e44\u0e23/\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 (\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e16\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48)</div><div class="v" style="color:%s!important;-webkit-text-fill-color:%s">%s</div><div class="s">\u0e40\u0e07\u0e34\u0e19\u0e25\u0e07\u0e23\u0e27\u0e21 $%s%s \xb7 %d \u0e44\u0e21\u0e49</div></div>'
            '<div class="tj-sb"><div class="t">\u0e40\u0e2a\u0e35\u0e22\u0e21\u0e32\u0e01\u0e2a\u0e38\u0e14\u0e16\u0e49\u0e32\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e17\u0e38\u0e01\u0e44\u0e21\u0e49</div><div class="v" style="color:%s!important;-webkit-text-fill-color:%s">%s</div><div class="s">%s</div></div>'
            '%s</div>') % (plc, plc, _money(pl) + _bts(pl), _fmt(cost, 0), _bt(cost), len(trades), rcol, rcol, "$" + _fmt(risk) + _bts(risk), riskp, alert)


def render_journal():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown('<div class="tj-note">\u0e2a\u0e21\u0e38\u0e14\u0e19\u0e35\u0e49 <b>\u0e40\u0e15\u0e37\u0e2d\u0e19</b> \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e02\u0e32\u0e22\u0e43\u0e2b\u0e49 \xb7 \u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e01\u0e47\u0e1a\u0e43\u0e19\u0e44\u0e1f\u0e25\u0e4c trade_journal.json \u0e43\u0e19\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \xb7 \u0e23\u0e32\u0e04\u0e32\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c\u0e23\u0e32\u0e27 15 \u0e19\u0e32\u0e17\u0e35 \xb7 '
                '\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e1d\u0e31\u0e48\u0e07\u0e0b\u0e37\u0e49\u0e2d \xb7 \u0e15\u0e31\u0e49\u0e07\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 <b>\u0e01\u0e48\u0e2d\u0e19</b>\u0e01\u0e14\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e2a\u0e21\u0e2d</div>', unsafe_allow_html=True)

    _FX["v"] = _fx_rate()
    data = _load()
    trades_all = data["trades"]
    openl = [t for t in trades_all if t.get("status", "open") == "open"]
    closed = [t for t in trades_all if t.get("status") == "closed"]

    # ---- \u0e40\u0e1e\u0e34\u0e48\u0e21\u0e44\u0e21\u0e49 ----
    with st.expander("\u2795 \u0e08\u0e14\u0e44\u0e21\u0e49\u0e43\u0e2b\u0e21\u0e48", expanded=not openl):
        sym = st.text_input("1) \u0e2b\u0e38\u0e49\u0e19\u0e2d\u0e30\u0e44\u0e23", placeholder="\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e23\u0e2b\u0e31\u0e2a \u0e40\u0e0a\u0e48\u0e19 NVDA \u0e41\u0e25\u0e49\u0e27\u0e01\u0e14 Enter", key="tj_sym").strip().upper()
        cur = None
        if sym:
            cur = _prices((sym,)).get(sym)
            if cur:
                st.caption("\u0e23\u0e32\u0e04\u0e32\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \\$%s (\u0e14\u0e35\u0e40\u0e25\u0e22\u0e4c\u0e23\u0e32\u0e27 15 \u0e19\u0e32\u0e17\u0e35)" % _fmt(cur))
            else:
                st.caption("\u0e2b\u0e32\u0e23\u0e32\u0e04\u0e32 %s \u0e44\u0e21\u0e48\u0e40\u0e08\u0e2d \u0e25\u0e2d\u0e07\u0e40\u0e0a\u0e47\u0e01\u0e23\u0e2b\u0e31\u0e2a\u0e2b\u0e38\u0e49\u0e19 \u0e2b\u0e23\u0e37\u0e2d\u0e43\u0e2a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07" % sym)
        entry = st.number_input("\u0e0b\u0e37\u0e49\u0e2d\u0e2b\u0e38\u0e49\u0e19\u0e25\u0e30\u0e01\u0e35\u0e48\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c ($ \u0e15\u0e48\u0e2d 1 \u0e2b\u0e38\u0e49\u0e19)", min_value=0.0, value=float(cur) if cur else 0.0, step=0.01, format="%.2f", key="tj_entry_%s" % (sym or "x"), help="\u0e04\u0e37\u0e2d\u0e23\u0e32\u0e04\u0e32\u0e02\u0e2d\u0e07\u0e2b\u0e38\u0e49\u0e19 1 \u0e2b\u0e38\u0e49\u0e19\u0e15\u0e2d\u0e19\u0e17\u0e35\u0e48\u0e04\u0e38\u0e13\u0e01\u0e14\u0e0b\u0e37\u0e49\u0e2d (\u0e14\u0e39\u0e08\u0e32\u0e01\u0e41\u0e2d\u0e1b\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e17\u0e35\u0e48\u0e0a\u0e48\u0e2d\u0e07 Avg cost \u0e2b\u0e23\u0e37\u0e2d\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49) \u0e16\u0e49\u0e32\u0e01\u0e33\u0e25\u0e31\u0e07\u0e08\u0e30\u0e0b\u0e37\u0e49\u0e2d\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e1b\u0e25\u0e48\u0e2d\u0e22\u0e15\u0e32\u0e21\u0e23\u0e32\u0e04\u0e32\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e44\u0e14\u0e49\u0e40\u0e25\u0e22 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e41\u0e01\u0e49")
        fx = _FX["v"]
        mode2 = st.radio("2) \u0e2d\u0e22\u0e32\u0e01\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e2d\u0e30\u0e44\u0e23", ["\U0001F4B0 \u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e08\u0e30\u0e25\u0e07\u0e0b\u0e37\u0e49\u0e2d", "\u26A0\uFE0F \u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e16\u0e49\u0e32\u0e1e\u0e25\u0e32\u0e14"], horizontal=True, key="tj_mode",
                         help="\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e41\u0e23\u0e01 = \u0e1a\u0e2d\u0e01\u0e27\u0e48\u0e32\u0e08\u0e30\u0e25\u0e07\u0e40\u0e07\u0e34\u0e19\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23 \u0e23\u0e30\u0e1a\u0e1a\u0e04\u0e33\u0e19\u0e27\u0e13\u0e43\u0e2b\u0e49\u0e27\u0e48\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e35\u0e48\u0e2b\u0e38\u0e49\u0e19 \xb7 \u0e40\u0e25\u0e37\u0e2d\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e2b\u0e25\u0e31\u0e07 = \u0e1a\u0e2d\u0e01\u0e27\u0e48\u0e32\u0e40\u0e2a\u0e35\u0e22\u0e44\u0e14\u0e49\u0e40\u0e17\u0e48\u0e32\u0e44\u0e23 \u0e23\u0e30\u0e1a\u0e1a\u0e04\u0e33\u0e19\u0e27\u0e13\u0e27\u0e48\u0e32\u0e04\u0e27\u0e23\u0e0b\u0e37\u0e49\u0e2d\u0e01\u0e35\u0e48\u0e2b\u0e38\u0e49\u0e19")
        by_money = mode2.startswith("\U0001F4B0")
        ccy = st.radio("\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e40\u0e07\u0e34\u0e19", ["\u0e1a\u0e32\u0e17 (\u0e3f)", "\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c ($)"], horizontal=True, key="tj_ccy2") if fx else "\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c ($)"
        in_baht = ccy.startswith("\u0e1a\u0e32\u0e17")
        lab_ = ("\u0e08\u0e30\u0e25\u0e07\u0e40\u0e07\u0e34\u0e19\u0e01\u0e35\u0e48" if by_money else "\u0e22\u0e2d\u0e21\u0e40\u0e2a\u0e35\u0e22\u0e44\u0e14\u0e49\u0e01\u0e35\u0e48") + ("\u0e1a\u0e32\u0e17" if in_baht else "\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c")
        dflt = (50000.0 if in_baht else 1500.0) if by_money else (3000.0 if in_baht else 100.0)
        stp = (1000.0 if in_baht else 100.0) if by_money else (100.0 if in_baht else 10.0)
        amt_in = st.number_input(lab_, min_value=0.0, value=dflt, step=stp, key="tj_amt_%s_%s" % ("m" if by_money else "r", "b" if in_baht else "d"))
        amt_usd = (amt_in / fx) if (in_baht and fx) else amt_in
        money_u, risk_d = (amt_usd, 0.0) if by_money else (0.0, amt_usd)
        frac = st.checkbox("\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e14\u0e49 (\u0e40\u0e0a\u0e48\u0e19 Dime, Webull)", value=False, key="tj_frac") if by_money else False
        if fx:
            st.caption("\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e41\u0e25\u0e01\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 1 \u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c \u2248 %.2f \u0e1a\u0e32\u0e17 (\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e15\u0e25\u0e32\u0e14\u0e08\u0e32\u0e01 Yahoo \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e40\u0e23\u0e17\u0e18\u0e19\u0e32\u0e04\u0e32\u0e23 \u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19\u0e22\u0e31\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c)" % fx)
        else:
            st.caption("\u0e14\u0e36\u0e07\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e41\u0e25\u0e01\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e08\u0e36\u0e07\u0e43\u0e2a\u0e48\u0e40\u0e1b\u0e47\u0e19\u0e14\u0e2d\u0e25\u0e25\u0e32\u0e23\u0e4c\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19")
        stop_pct = st.radio("3) \u0e16\u0e49\u0e32\u0e23\u0e32\u0e04\u0e32\u0e25\u0e07\u0e01\u0e35\u0e48 % \u0e43\u0e2b\u0e49\u0e02\u0e32\u0e22\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19", [3.0, 5.0, 8.0, 10.0], index=1, horizontal=True, format_func=lambda v: "%g%%" % v, key="tj_pct",
                            help="\u0e2b\u0e38\u0e49\u0e19\u0e0b\u0e34\u0e48\u0e07\u0e41\u0e01\u0e27\u0e48\u0e07\u0e41\u0e23\u0e07 \u0e21\u0e31\u0e01\u0e43\u0e0a\u0e49 5-8% \u0e16\u0e49\u0e32\u0e15\u0e31\u0e49\u0e07\u0e41\u0e04\u0e1a\u0e40\u0e01\u0e34\u0e19\u0e44\u0e1b\u0e08\u0e30\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e07\u0e48\u0e32\u0e22\u0e42\u0e14\u0e22\u0e44\u0e21\u0e48\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19")
        with st.expander("\u0e15\u0e31\u0e49\u0e07\u0e40\u0e2d\u0e07 (\u0e44\u0e21\u0e48\u0e08\u0e33\u0e40\u0e1b\u0e47\u0e19)"):
            stop_m = st.number_input("\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e40\u0e1b\u0e47\u0e19\u0e23\u0e32\u0e04\u0e32 ($) \u0e16\u0e49\u0e32\u0e43\u0e2a\u0e48 \u0e08\u0e30\u0e43\u0e0a\u0e49\u0e04\u0e48\u0e32\u0e19\u0e35\u0e49\u0e41\u0e17\u0e19\u0e02\u0e49\u0e2d 3", min_value=0.0, value=0.0, step=0.01, format="%.2f", key="tj_stopm")
            qty_m = st.number_input("\u0e08\u0e33\u0e19\u0e27\u0e19\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e2d\u0e07 \u0e16\u0e49\u0e32\u0e43\u0e2a\u0e48 \u0e08\u0e30\u0e43\u0e0a\u0e49\u0e04\u0e48\u0e32\u0e19\u0e35\u0e49\u0e41\u0e17\u0e19\u0e02\u0e49\u0e2d 2", min_value=0.0, value=0.0, step=1.0, key="tj_qtym")
            target = st.number_input("\u0e40\u0e1b\u0e49\u0e32\u0e01\u0e33\u0e44\u0e23 ($) \u0e44\u0e21\u0e48\u0e43\u0e2a\u0e48\u0e01\u0e47\u0e44\u0e14\u0e49", min_value=0.0, value=0.0, step=0.01, format="%.2f", key="tj_tgt")
            note = st.text_input("\u0e42\u0e19\u0e49\u0e15 \u0e44\u0e21\u0e48\u0e43\u0e2a\u0e48\u0e01\u0e47\u0e44\u0e14\u0e49", placeholder="\u0e40\u0e0a\u0e48\u0e19 \u0e40\u0e14\u0e49\u0e07\u0e08\u0e32\u0e01\u0e41\u0e19\u0e27\u0e23\u0e31\u0e1a", key="tj_note")
        stop_f, qty_f = resolve(entry, stop_m, stop_pct, qty_m, money_u, risk_d, frac)
        if sym and entry > 0 and stop_f > 0 and qty_f > 0:
            qtxt = _fmt(qty_f, 0) if float(qty_f).is_integer() else _fmt(qty_f, 2)
            cost_u, loss_u = qty_f * entry, (entry - stop_f) * qty_f
            fx_ = _FX["v"]

            def _two(u):
                return ("\u0e3f" + "{:,.0f}".format(u * fx_), "$" + _fmt(u, 0 if u >= 100 else 2)) if fx_ else ("$" + _fmt(u, 0 if u >= 100 else 2), "")
            c1_, c1s = _two(cost_u)
            c2_, c2s = _two(loss_u)
            drop = (1.0 - stop_f / entry) * 100.0
            st.markdown('<div class="tj-sum">'
                        '<div class="tj-sb"><div class="t">\U0001F4B0 \u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 (\u0e0b\u0e37\u0e49\u0e2d %s \u0e2b\u0e38\u0e49\u0e19)</div><div class="v">%s</div><div class="s">%s</div></div>'
                        '<div class="tj-sb"><div class="t">\u26A0\uFE0F \u0e16\u0e49\u0e32\u0e1e\u0e25\u0e32\u0e14\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 \u0e40\u0e2a\u0e35\u0e22</div><div class="v" style="color:%s!important;-webkit-text-fill-color:%s">%s</div><div class="s">%s</div></div>'
                        '<div class="tj-sb"><div class="t">\U0001F6D1 \u0e15\u0e31\u0e49\u0e07\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32</div><div class="v">$%s</div><div class="s">\u0e25\u0e07 %.1f%% \u0e08\u0e32\u0e01\u0e23\u0e32\u0e04\u0e32\u0e0b\u0e37\u0e49\u0e2d</div></div></div>' % (
                            qtxt, c1_, ("= " + c1s) if c1s else "", _DN, _DN, c2_, ("= " + c2s) if c2s else "", _fmt(stop_f), drop), unsafe_allow_html=True)
            if by_money and not frac and money_u > 0 and cost_u < money_u * 0.95:
                left = money_u - cost_u
                st.caption("\u0e2b\u0e38\u0e49\u0e19\u0e25\u0e30 \\$%s \u0e0b\u0e37\u0e49\u0e2d\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e47\u0e19\u0e08\u0e33\u0e19\u0e27\u0e19\u0e40\u0e15\u0e47\u0e21\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19 \u0e40\u0e25\u0e22\u0e43\u0e0a\u0e49\u0e40\u0e07\u0e34\u0e19\u0e08\u0e23\u0e34\u0e07 \\$%s \u0e40\u0e2b\u0e25\u0e37\u0e2d \\$%s%s \u0e0b\u0e37\u0e49\u0e2d\u0e2d\u0e35\u0e01\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 (\u0e16\u0e49\u0e32\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e14\u0e49 \u0e15\u0e34\u0e4a\u0e01\u0e0a\u0e48\u0e2d\u0e07 '\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e14\u0e49')" % (
                    _fmt(entry), _fmt(cost_u, 0), _fmt(left, 0), _bt(left)))
        elif sym and entry > 0:
            if by_money and money_u > 0 and money_u < entry:
                st.warning("\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07 (\\$%s) \u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19 1 \u0e2b\u0e38\u0e49\u0e19 (\\$%s%s) \u0e16\u0e49\u0e32\u0e42\u0e1a\u0e23\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e14\u0e49 \u0e15\u0e34\u0e4a\u0e01 '\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e14\u0e49' \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e07\u0e34\u0e19" % (_fmt(money_u), _fmt(entry), _bt(entry)))
            else:
                st.caption("\u0e22\u0e31\u0e07\u0e04\u0e33\u0e19\u0e27\u0e13\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49: \u0e25\u0e2d\u0e07\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e07\u0e34\u0e19 \u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e0a\u0e47\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19")
        # ---- \u0e2a\u0e16\u0e32\u0e19\u0e01\u0e32\u0e23\u0e13\u0e4c\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 \u0e16\u0e49\u0e32\u0e0b\u0e37\u0e49\u0e2d\u0e44\u0e1b\u0e41\u0e25\u0e49\u0e27\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e19\u0e36\u0e48\u0e07 \u0e41\u0e25\u0e30\u0e23\u0e32\u0e04\u0e32\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e15\u0e48\u0e32\u0e07\u0e44\u0e1b ----
        invest_u = money_u if (by_money and money_u > 0) else (qty_f * entry if qty_f > 0 else 0.0)
        if sym and cur and entry > 0 and invest_u > 0 and abs(cur / entry - 1.0) >= 0.005:
            chg = (cur / entry - 1.0) * 100.0
            now_u = invest_u * (cur / entry)
            pl_u = now_u - invest_u
            up = pl_u >= 0
            col_ = _UP if up else _DN
            fx_ = _FX["v"]

            def _m(u):
                return ("\u0e3f" + "{:,.0f}".format(abs(u) * fx_)) if fx_ else ("$" + _fmt(abs(u), 0))

            def _sub(u):
                return ("= $" + _fmt(abs(u), 0)) if fx_ else ""
            word = "\u0e01\u0e33\u0e44\u0e23" if up else "\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19"
            st.markdown('<div class="tj-sum">'
                        '<div class="tj-sb"><div class="t">\U0001F4B0 \u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07\u0e44\u0e1b (\u0e0b\u0e37\u0e49\u0e2d\u0e17\u0e35\u0e48 $%s)</div><div class="v">%s</div><div class="s">%s</div></div>'
                        '<div class="tj-sb"><div class="t">\U0001F4C9 \u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49\u0e2b\u0e38\u0e49\u0e19\u0e40\u0e2b\u0e25\u0e37\u0e2d (\u0e23\u0e32\u0e04\u0e32 $%s)</div><div class="v">%s</div><div class="s">%s</div></div>'
                        '<div class="tj-sb" style="border-color:%s"><div class="t">%s \u0e16\u0e49\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e02\u0e32\u0e22%s</div><div class="v" style="color:%s!important;-webkit-text-fill-color:%s">%s%s</div><div class="s">\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19 %s %.1f%% \u0e08\u0e32\u0e01\u0e17\u0e35\u0e48\u0e0b\u0e37\u0e49\u0e2d</div></div></div>' % (
                            _fmt(entry), _m(invest_u), _sub(invest_u), _fmt(cur), _m(now_u), _sub(now_u), col_, "\U0001F7E2" if up else "\U0001F534", " \u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49%s" % word,
                            col_, col_, "+" if up else "-", _m(pl_u), "\u0e02\u0e36\u0e49\u0e19" if up else "\u0e25\u0e07", abs(chg)), unsafe_allow_html=True)
            msg = "\u0e16\u0e49\u0e32\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e02\u0e32\u0e22 %s\u0e1a\u0e19\u0e01\u0e23\u0e30\u0e14\u0e32\u0e29 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e01\u0e33\u0e44\u0e23\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e08\u0e23\u0e34\u0e07\u0e08\u0e19\u0e01\u0e27\u0e48\u0e32\u0e08\u0e30\u0e01\u0e14\u0e02\u0e32\u0e22" % ("\u0e01\u0e33\u0e44\u0e23" if up else "\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19")
            st.caption(msg + (" \xb7 \u0e40\u0e07\u0e34\u0e19\u0e1a\u0e32\u0e17\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13\u0e08\u0e32\u0e01\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e41\u0e25\u0e01\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e27\u0e31\u0e19\u0e19\u0e35\u0e49 \u0e44\u0e21\u0e48\u0e19\u0e31\u0e1a\u0e04\u0e48\u0e32\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e44\u0e1b\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e0b\u0e37\u0e49\u0e2d" if fx_ else "") + " \xb7 \u0e16\u0e49\u0e32\u0e23\u0e32\u0e04\u0e32 \\$%s \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e0b\u0e37\u0e49\u0e2d\u0e08\u0e23\u0e34\u0e07 \u0e41\u0e01\u0e49\u0e0a\u0e48\u0e2d\u0e07\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19" % _fmt(entry))
            if stop_f > 0 and cur <= stop_f:
                st.error("\u0e23\u0e32\u0e04\u0e32\u0e15\u0e2d\u0e19\u0e19\u0e35\u0e49 (\\$%s) \u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32\u0e08\u0e38\u0e14\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e44\u0e27\u0e49 (\\$%s) \u0e41\u0e25\u0e49\u0e27 \u0e16\u0e49\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e44\u0e21\u0e49\u0e08\u0e23\u0e34\u0e07 \u0e19\u0e35\u0e48\u0e04\u0e37\u0e2d\u0e08\u0e38\u0e14\u0e17\u0e35\u0e48\u0e41\u0e1c\u0e19\u0e1a\u0e2d\u0e01\u0e43\u0e2b\u0e49\u0e2d\u0e2d\u0e01" % (_fmt(cur), _fmt(stop_f)))
            if by_money and money_u < entry and not frac:
                st.caption("\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e2b\u0e15\u0e38: \u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e25\u0e07\u0e19\u0e49\u0e2d\u0e22\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e04\u0e32\u0e2b\u0e38\u0e49\u0e19 1 \u0e2b\u0e38\u0e49\u0e19 \u0e15\u0e49\u0e2d\u0e07\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19 \u0e15\u0e34\u0e4a\u0e01 '\u0e0b\u0e37\u0e49\u0e2d\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e28\u0e29\u0e2b\u0e38\u0e49\u0e19\u0e44\u0e14\u0e49' \u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19 \u0e16\u0e49\u0e32\u0e08\u0e30\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01")
        if st.button("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e21\u0e49\u0e19\u0e35\u0e49 (\u0e0b\u0e37\u0e49\u0e2d\u0e41\u0e25\u0e49\u0e27)", key="tj_save"):
            err = validate(sym, qty_f, entry, stop_f, target)
            if err:
                st.warning(err)
            else:
                trades_all.append({"id": uuid.uuid4().hex[:10], "sym": sym, "qty": qty_f, "entry": entry, "stop": stop_f,
                                   "target": target or None, "note": (note or "").strip(), "status": "open",
                                   "opened": _dt.date.today().isoformat()})
                if _save(data):
                    st.success("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e41\u0e25\u0e49\u0e27: %s" % sym)
                    st.rerun()
                else:
                    st.error("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e1f\u0e25\u0e4c\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 (\u0e40\u0e0a\u0e47\u0e01\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e4c\u0e40\u0e02\u0e35\u0e22\u0e19\u0e44\u0e1f\u0e25\u0e4c\u0e43\u0e19\u0e42\u0e1f\u0e25\u0e40\u0e14\u0e2d\u0e23\u0e4c\u0e42\u0e1b\u0e23\u0e40\u0e08\u0e01\u0e15\u0e4c)")

    # ---- \u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e16\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48 ----
    if openl:
        syms = tuple(sorted({t["sym"] for t in openl}))
        px = _prices(syms)
        earn = _earn_days(syms)
        ans = [analyze(t, px.get(t["sym"])) for t in openl]
        order = {"FLATLINE": 0, "DANGER": 1, "NOPRICE": 4, "HOLD": 3, "PROFIT": 2}
        idx = sorted(range(len(openl)), key=lambda i: (order[ans[i]["status"]], openl[i]["sym"]))
        st.markdown(_summary([openl[i] for i in idx], [ans[i] for i in idx], float(data.get("account") or 0)), unsafe_allow_html=True)
        cards = "".join(_card(openl[i], ans[i], earn.get(openl[i]["sym"]), no=1 + trades_all.index(openl[i])) for i in idx)
        st.markdown('<div class="tj-grid">%s</div>' % cards, unsafe_allow_html=True)

        with st.expander("\u2705 \u0e1b\u0e34\u0e14\u0e44\u0e21\u0e49 / \u0e25\u0e1a"):
            labs = ["%s \xb7 \u0e40\u0e02\u0e49\u0e32 %s \xb7 %s \u0e2b\u0e38\u0e49\u0e19 (%s)" % (t["sym"], _fmt(t["entry"]), _fmt(t["qty"], 0), t.get("opened", "")) for t in openl]
            pick = st.selectbox("\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e44\u0e21\u0e49", range(len(openl)), format_func=lambda i: labs[i], key="tj_pick")
            t = openl[pick]
            cur = px.get(t["sym"])
            xp = st.number_input("\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e22\u0e2d\u0e2d\u0e01 ($)", min_value=0.0, value=float(cur) if cur else 0.0, step=0.01, format="%.2f", key="tj_exit_%s" % t["id"])
            b1, b2 = st.columns(2)
            if b1.button("\u0e1b\u0e34\u0e14\u0e44\u0e21\u0e49\u0e19\u0e35\u0e49 (\u0e02\u0e32\u0e22\u0e41\u0e25\u0e49\u0e27)", key="tj_close"):
                if xp <= 0:
                    st.warning("\u0e43\u0e2a\u0e48\u0e23\u0e32\u0e04\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e22\u0e2d\u0e2d\u0e01\u0e14\u0e49\u0e27\u0e22")
                else:
                    t["status"], t["exit"], t["closed"] = "closed", float(xp), _dt.date.today().isoformat()
                    if _save(data):
                        st.rerun()
                    else:
                        st.error("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e1f\u0e25\u0e4c\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49")
            if b2.button("\u0e25\u0e1a (\u0e08\u0e14\u0e1c\u0e34\u0e14)", key="tj_del"):
                data["trades"] = [x for x in trades_all if x.get("id") != t["id"]]
                if _save(data):
                    st.rerun()
                else:
                    st.error("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e1f\u0e25\u0e4c\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49")
    else:
        st.info("\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e21\u0e35\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e16\u0e37\u0e2d\u0e2d\u0e22\u0e39\u0e48 \u0e01\u0e14 \u2795 \u0e08\u0e14\u0e44\u0e21\u0e49\u0e43\u0e2b\u0e21\u0e48 \u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19")

    # ---- \u0e02\u0e19\u0e32\u0e14\u0e1e\u0e2d\u0e23\u0e4c\u0e15 (\u0e43\u0e0a\u0e49\u0e04\u0e33\u0e19\u0e27\u0e13 % \u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07) ----
    with st.expander("\u2699\ufe0f \u0e02\u0e19\u0e32\u0e14\u0e1e\u0e2d\u0e23\u0e4c\u0e15 (\u0e43\u0e0a\u0e49\u0e04\u0e33\u0e19\u0e27\u0e13 % \u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07\u0e23\u0e27\u0e21)"):
        acc = st.number_input("\u0e40\u0e07\u0e34\u0e19\u0e43\u0e19\u0e1e\u0e2d\u0e23\u0e4c\u0e15\u0e23\u0e27\u0e21\u0e42\u0e14\u0e22\u0e1b\u0e23\u0e30\u0e21\u0e32\u0e13 ($)", min_value=0.0, value=float(data.get("account") or 0.0), step=100.0, key="tj_acc")
        if st.button("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e19\u0e32\u0e14\u0e1e\u0e2d\u0e23\u0e4c\u0e15", key="tj_acc_save"):
            data["account"] = float(acc)
            if _save(data):
                st.rerun()
            else:
                st.error("\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e44\u0e1f\u0e25\u0e4c\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49")
        st.caption("\u0e41\u0e19\u0e27\u0e17\u0e32\u0e07\u0e17\u0e31\u0e48\u0e27\u0e44\u0e1b: \u0e16\u0e49\u0e32\u0e42\u0e14\u0e19\u0e15\u0e31\u0e14\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e17\u0e38\u0e01\u0e44\u0e21\u0e49\u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 \u0e44\u0e21\u0e48\u0e04\u0e27\u0e23\u0e40\u0e2a\u0e35\u0e22\u0e40\u0e01\u0e34\u0e19 3-6% \u0e02\u0e2d\u0e07\u0e1e\u0e2d\u0e23\u0e4c\u0e15 \xb7 \u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e19\u0e35\u0e49\u0e40\u0e01\u0e47\u0e1a\u0e43\u0e19\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19")

    # ---- \u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34 ----
    if closed:
        s = closed_stats(closed)
        st.markdown('<div class="section-label">\u25c6 \u0e1b\u0e23\u0e30\u0e27\u0e31\u0e15\u0e34\u0e44\u0e21\u0e49\u0e17\u0e35\u0e48\u0e1b\u0e34\u0e14\u0e41\u0e25\u0e49\u0e27</div>', unsafe_allow_html=True)
        wr = s["wins"] / s["n"] * 100.0
        tc = _UP if s["total"] >= 0 else _DN
        st.markdown('<div class="tj-sum">'
                    '<div class="tj-sb"><div class="t">\u0e01\u0e33\u0e44\u0e23/\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19\u0e23\u0e27\u0e21</div><div class="v" style="color:%s!important;-webkit-text-fill-color:%s">%s</div><div class="s">%d \u0e44\u0e21\u0e49 \xb7 \u0e0a\u0e19\u0e30 %d \u0e41\u0e1e\u0e49 %d (%.0f%%)</div></div>'
                    '<div class="tj-sb"><div class="t">\u0e0a\u0e19\u0e30\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22 / \u0e41\u0e1e\u0e49\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22</div><div class="v" style="font-size:18px">%s / %s</div><div class="s">\u0e0a\u0e19\u0e30\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22\u0e04\u0e27\u0e23\u0e43\u0e2b\u0e0d\u0e48\u0e01\u0e27\u0e48\u0e32\u0e41\u0e1e\u0e49\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22</div></div>'
                    '<div class="tj-sb"><div class="t">\u0e40\u0e2a\u0e35\u0e22\u0e2b\u0e19\u0e31\u0e01\u0e2a\u0e38\u0e14\u0e17\u0e35\u0e48\u0e40\u0e04\u0e22\u0e21\u0e35</div><div class="v" style="font-size:%s">%s</div><div class="s">-1R = \u0e40\u0e2a\u0e35\u0e22\u0e15\u0e32\u0e21\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e43\u0e08\u0e44\u0e27\u0e49 \u0e16\u0e49\u0e32\u0e40\u0e01\u0e34\u0e19 -1R \u0e21\u0e32\u0e01 \u0e41\u0e1b\u0e25\u0e27\u0e48\u0e32\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e15\u0e31\u0e14\u0e15\u0e32\u0e21\u0e41\u0e1c\u0e19</div></div></div>'
                    % (tc, tc, _money(s["total"]), s["n"], s["wins"], s["loss"], wr, _money(s["avg_win"]), _money(s["avg_loss"]), "22px" if s["worst_r"] < 0 else "16px", ("%+.1fR" % s["worst_r"]) if s["worst_r"] < 0 else "\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e40\u0e04\u0e22\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19"), unsafe_allow_html=True)
        rows = []
        for c in sorted(closed, key=lambda x: x.get("closed", ""), reverse=True)[:30]:
            pl = (c["exit"] - c["entry"]) * c["qty"]
            r = (c["exit"] - c["entry"]) / (c["entry"] - c["stop"]) if c["entry"] > c["stop"] else 0.0
            rows.append({"\u0e2b\u0e38\u0e49\u0e19": c["sym"], "\u0e40\u0e02\u0e49\u0e32": c["entry"], "\u0e2d\u0e2d\u0e01": c["exit"], "\u0e08\u0e33\u0e19\u0e27\u0e19": c["qty"], "\u0e01\u0e33\u0e44\u0e23/\u0e02\u0e32\u0e14\u0e17\u0e38\u0e19 ($)": round(pl, 2), "R": round(r, 2),
                         "\u0e1b\u0e34\u0e14\u0e40\u0e21\u0e37\u0e48\u0e2d": c.get("closed", "")})
        try:
            import pandas as pd
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        except Exception:
            for r in rows:
                st.write(r)