# -*- coding: utf-8 -*-
"""
news_feed.py  [news_feed v1]
============================
เรดาร์ข่าวแบบ "ฟีดข่าวภาษาไทย" (สไตล์แอป Dime):
  • ดึงข่าวล่าสุดของหุ้นใน watchlist (Google News RSS + Yahoo Finance) เรียงใหม่สุดก่อน
  • แปลหัวข้อเป็นภาษาไทยให้ทุกข่าว
      - ไม่มีคีย์ AI  → แปลด้วยบริการแปลฟรี (แปลตรงตัว อ่านรู้เรื่อง)
      - มีคีย์ AI     → Claude แปลให้เป็นภาษาไทยธรรมชาติ + สรุปประเด็น + บอกว่าบวก/ลบต่อหุ้น
                        + สรุปภาพรวมรายหุ้น (1 คำขอต่อหุ้น ใช้โมเดลถูกสุด)
  • จัดกลุ่มตามวัน (พ.ศ.) + บอกเวลา "x ชม.ที่แล้ว" + กรองตามหุ้น/โทนข่าว

ข้อจำกัด (บอกตรงๆ): AI เห็นแค่ "หัวข้อข่าว + แหล่ง + เวลา" ไม่ได้อ่านเนื้อข่าวเต็ม
จึงสรุปได้เท่าที่หัวข้อบอก และถูกสั่งไม่ให้เดาเกินหัวข้อ
"""
import html
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import quote
from urllib.request import Request, urlopen

import streamlit as st

import news_radar

BKK = timezone(timedelta(hours=7))
_TH_MONTHS = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.",
              "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
AI_MODEL = "claude-haiku-4-5-20251001"


# ----------------------------------------------------------------
# เวลา
# ----------------------------------------------------------------
def _parse_ts(s):
    """แปลงข้อความวันที่ (RFC822 / ISO) เป็น datetime มี timezone, ไม่ได้คืน None"""
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)
    except Exception:
        d = None
    if d is None:
        try:
            d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        except Exception:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(BKK)


def th_date(d):
    return f"{d.day} {_TH_MONTHS[d.month - 1]} {d.year + 543}"


def ago(d, now=None):
    now = now or datetime.now(BKK)
    sec = (now - d).total_seconds()
    if sec < 0:
        sec = 0
    if sec < 3600:
        return f"{max(1, int(sec // 60))} นาทีที่แล้ว"
    if sec < 86400:
        return f"{int(sec // 3600)} ชม.ที่แล้ว"
    return f"{d.hour:02d}:{d.minute:02d} น."


# ----------------------------------------------------------------
# ดึงข่าว (ใหม่สุดก่อน, ตัดซ้ำ)
# ----------------------------------------------------------------
def _norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()[:60]


def _clean_title(title, source):
    """ตัดชื่อแหล่งท้ายหัวข้อ (" - Reuters") ออก คืน (หัวข้อ, แหล่ง) ถ้าไม่รู้แหล่งจะเอาจากท้ายหัวข้อ"""
    t = html.unescape(title or "").strip()
    if source and source != "ไม่ทราบแหล่ง" and t.endswith(" - " + source):
        return t[: -len(source) - 3].strip(), source
    if " - " in t:
        head, tail = t.rsplit(" - ", 1)
        if 0 < len(tail) <= 40 and head:
            return head.strip(), tail.strip()
    return t, (source if source != "ไม่ทราบแหล่ง" else "")


def _fetch_one(ticker, days):
    items = []
    # Google News: ขอข่าวย้อนหลังไม่เกิน N วัน (ถ้าไม่เจอเลยค่อยลองแบบไม่จำกัด)
    g = news_radar.fetch_google_news(f"{ticker} stock when:{days}d", max_items=15)
    if not g:
        g = news_radar.fetch_google_news(f"{ticker} stock", max_items=15)
    for n in g:
        _t, _src = _clean_title(n["title"], n["source"])
        items.append({
            "ticker": ticker,
            "title_en": _t,
            "link": n["link"],
            "source": _src,
            "ts": _parse_ts(n.get("pub_date")),
        })
    # Yahoo Finance (มีเวลาในข้อมูลดิบ)
    try:
        import yfinance as yf
        for n in (yf.Ticker(ticker).news or [])[:8]:
            c = n.get("content", {}) or {}
            title = c.get("title") or n.get("title", "")
            if not title:
                continue
            link = (c.get("canonicalUrl", {}) or {}).get("url") or n.get("link", "")
            prov = (c.get("provider", {}) or {}).get("displayName") or "Yahoo Finance"
            items.append({
                "ticker": ticker,
                "title_en": title.strip(),
                "link": link,
                "source": prov,
                "ts": _parse_ts(c.get("pubDate") or c.get("displayTime")),
            })
    except Exception:
        pass

    # ตัดซ้ำ + ตัดข่าวเก่าเกินกำหนด + เรียงใหม่สุดก่อน
    cutoff = datetime.now(BKK) - timedelta(days=days)
    seen, out = set(), []
    for it in items:
        k = _norm(it["title_en"])
        if not k or k in seen:
            continue
        if it["ts"] is not None and it["ts"] < cutoff:
            continue
        seen.add(k)
        out.append(it)
    out.sort(key=lambda x: x["ts"] or datetime(1970, 1, 1, tzinfo=BKK), reverse=True)
    return out[:10]


# ----------------------------------------------------------------
# แปลฟรี (ไม่ต้องมีคีย์)
# ----------------------------------------------------------------
def _gt(text):
    try:
        url = ("https://translate.googleapis.com/translate_a/single"
               "?client=gtx&sl=en&tl=th&dt=t&q=" + quote(text))
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode("utf-8"))
        return "".join(seg[0] for seg in data[0] if seg and seg[0]).strip()
    except Exception:
        return ""


def translate_free(titles):
    if not titles:
        return []
    with ThreadPoolExecutor(max_workers=8) as ex:
        return list(ex.map(_gt, titles))


# ----------------------------------------------------------------
# สรุป + แปลด้วย AI (1 คำขอต่อหุ้น)
# ----------------------------------------------------------------
def _extract_json(text):
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b <= a:
        return None
    try:
        return json.loads(text[a:b + 1])
    except Exception:
        return None


def ai_digest(api_key, ticker, name, items):
    """คืน (overview, [ {th, sum, tone} ต่อข่าว ], headline) ถ้าพลาดคืน ("", [None]*n, "")"""
    empty = ("", [None] * len(items), "")
    if not api_key or not items:
        return empty
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        now = datetime.now(BKK)
        lines = []
        for i, it in enumerate(items, 1):
            when = ago(it["ts"], now) if it["ts"] else "ไม่ทราบเวลา"
            lines.append(f'{i}. [{it["source"]} · {when}] {it["title_en"]}')
        prompt = f"""คุณเป็นบรรณาธิการข่าวหุ้นภาษาไทย (สไตล์แอป Dime / Settrade) นี่คือหัวข้อข่าวล่าสุดของหุ้น {ticker} ({name}):

{chr(10).join(lines)}

งานของคุณ: ตอบเป็น JSON อย่างเดียว (ห้ามมีข้อความอื่น) รูปแบบ:
{{"headline":"ขึ้นต้นด้วย emoji 1 ตัวที่เข้ากับเรื่อง แล้วสรุปเรื่องเด่นที่สุดของหุ้นนี้เป็น 1 ประโยคไทยสั้นกระชับ (ไม่เกิน 90 ตัวอักษร) แบบพาดหัวแอป Dime เช่น '💊 LLY กำไร Q3 เกินคาดและปรับเป้าปีขึ้น'",
 "overview":"สรุปภาพรวมข่าวของหุ้นนี้ 2-3 ประโยคภาษาไทย บอกว่าตอนนี้มีเรื่องอะไรเด่น และโทนรวมเป็นอย่างไร",
 "items":[{{"i":1,"th":"หัวข้อข่าวแปลเป็นไทยกระชับ ธรรมชาติ แบบข่าวหุ้นไทย","sum":"สรุปประเด็น 1 ประโยค ว่าข่าวนี้สำคัญกับหุ้นยังไง","tone":"บวก|ลบ|กลาง"}}]}}

กฎ: 1) items ต้องครบ {len(items)} ข่าวตามลำดับเลข 2) ใช้เฉพาะข้อมูลที่อยู่ในหัวข้อ ห้ามเดาหรือเติมตัวเลข/เหตุการณ์ที่หัวข้อไม่ได้บอก ถ้าหัวข้อไม่พอให้สรุปสั้นๆ ตามที่มี 3) คงชื่อบริษัท/ตัวย่อ/ตัวเลข/ $ ตามต้นฉบับ 4) tone คือผลต่อราคาหุ้น {ticker} โดยตรง ถ้าไม่ชัดให้ "กลาง" """
        resp = client.messages.create(
            model=AI_MODEL,
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        data = _extract_json(resp.content[0].text)
        if not data:
            return empty
        res = [None] * len(items)
        for o in data.get("items", []):
            try:
                idx = int(o.get("i")) - 1
            except Exception:
                continue
            if 0 <= idx < len(items):
                res[idx] = {
                    "th": str(o.get("th", "")).strip(),
                    "sum": str(o.get("sum", "")).strip(),
                    "tone": str(o.get("tone", "กลาง")).strip(),
                }
        return str(data.get("overview", "")).strip(), res, str(data.get("headline", "")).strip()
    except Exception:
        return empty


# ----------------------------------------------------------------
# รวมทุกอย่าง (cache 5 นาที เพื่อไม่ยิงซ้ำ แต่ยังสดอยู่)
# ----------------------------------------------------------------
def _price(t):
    """คืน (ราคาล่าสุด, % เปลี่ยนแปลงเทียบวันก่อนหน้า) ถ้าไม่ได้คืน (None, None)"""
    try:
        import yfinance as yf
        fi = yf.Ticker(t).fast_info
        p, pc = fi.get("lastPrice"), fi.get("previousClose")
        if p and pc:
            return float(p), (float(p) / float(pc) - 1) * 100
    except Exception:
        pass
    return None, None


def _info(t):
    name, sector = t, ""
    try:
        import yfinance as yf
        i = yf.Ticker(t).info or {}
        name = i.get("shortName") or t
        sector = i.get("sector") or ""
    except Exception:
        pass
    return name, sector


@st.cache_data(ttl=300, show_spinner=False)
def build_feed(tickers: tuple, api_key: str, days: int = 3):
    tickers = list(tickers)
    with ThreadPoolExecutor(max_workers=6) as ex:
        news_lists = list(ex.map(lambda t: _fetch_one(t, days), tickers))
        infos = list(ex.map(_info, tickers))
        earnings = list(ex.map(news_radar.get_next_earnings_date, tickers))
        prices = list(ex.map(_price, tickers))

    def work(args):
        t, items, (name, _s) = args
        if api_key:
            return ai_digest(api_key, t, name, items)
        return "", [None] * len(items), ""

    with ThreadPoolExecutor(max_workers=5) as ex:
        digests = list(ex.map(work, zip(tickers, news_lists, infos)))

    feed, per = [], {}
    for t, items, (name, sector), (overview, dg, headline), ed, (px, pct) in zip(
            tickers, news_lists, infos, digests, earnings, prices):
        # แปลฟรีให้ข่าวที่ AI ไม่ได้แปลให้ (ไม่มีคีย์ / AI พลาดบางข่าว)
        need = [i for i, d in enumerate(dg) if not (d and d.get("th"))]
        if need:
            tr = translate_free([items[i]["title_en"] for i in need])
            for i, th in zip(need, tr):
                dg[i] = {"th": th, "sum": "", "tone": None} if not dg[i] else {**dg[i], "th": th}
        tones = []
        for it, d in zip(items, dg):
            it["th"] = (d.get("th") or "").strip() or it["title_en"]
            it["sum"] = d.get("sum", "")
            tone = d.get("tone")
            if tone not in ("บวก", "ลบ", "กลาง"):  # ไม่มี AI → ใช้ keyword คร่าวๆ
                s = news_radar._score_headline(it["title_en"])
                tone = "บวก" if s > 0 else ("ลบ" if s < 0 else "กลาง")
            it["tone"] = tone
            it["pct"] = pct
            tones.append(tone)
            feed.append(it)
        pos, neg = tones.count("บวก"), tones.count("ลบ")
        overall = "เอียงบวก" if pos > neg else ("เอียงลบ" if neg > pos else "เป็นกลาง")
        if not headline and items:       # ไม่มี AI → ใช้หัวข้อไทยของข่าวล่าสุดแทน
            headline = items[0]["th"]
        per[t] = {"price": px, "pct": pct, "headline": headline,
                  "hl_src": (items[0]["source"] if items else ""),
                  "hl_link": (items[0]["link"] if items else ""),
                  "name": name, "sector": sector, "overview": overview,
                  "earnings": ed, "n": len(items), "pos": pos, "neg": neg, "overall": overall}
    feed.sort(key=lambda x: x["ts"] or datetime(1970, 1, 1, tzinfo=BKK), reverse=True)
    return {"feed": feed, "per": per, "ai": bool(api_key),
            "fetched": datetime.now(BKK)}


# ----------------------------------------------------------------
# แสดงผล
# ----------------------------------------------------------------
_CSS = """
<style>
.nf-sum{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin:6px 0 18px}
.nf-box{background:var(--panel);border:1px solid var(--line);padding:12px 14px;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px))}
.nf-box .h{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.nf-box .tk{font-family:var(--mono);font-weight:700;color:var(--gold);font-size:1.05rem;letter-spacing:.06em}
.nf-box .nm{color:var(--muted);font-size:.78rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nf-box .ov{color:var(--text);font-size:.9rem;line-height:1.55}
.nf-box .ft{margin-top:8px;color:var(--muted);font-size:.74rem;display:flex;gap:10px;flex-wrap:wrap}
.nf-day{font-family:var(--mono);color:var(--cyan);letter-spacing:.12em;font-size:.82rem;
  margin:22px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--line)}
.nf-card{display:flex;gap:12px;padding:12px 4px;border-bottom:1px solid rgba(125,134,166,.16)}
.nf-bar{width:3px;flex:0 0 3px;border-radius:2px;background:var(--muted)}
.nf-card.pos .nf-bar{background:var(--up)} .nf-card.neg .nf-bar{background:var(--down)}
.nf-body{flex:1;min-width:0}
.nf-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px;font-size:.74rem;color:var(--muted)}
.nf-chip{font-family:var(--mono);font-weight:700;color:#05060d!important;-webkit-text-fill-color:#05060d;background:var(--gold);padding:1px 7px;font-size:.72rem;letter-spacing:.05em}
.nf-tone{padding:1px 7px;font-size:.7rem;border:1px solid currentColor}
.nf-tone.pos{color:#19f5a5!important;-webkit-text-fill-color:#19f5a5}.nf-tone.neg{color:#ff2a6d!important;-webkit-text-fill-color:#ff2a6d}.nf-tone.mid{color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4}
.nf-th{display:block;color:var(--text)!important;font-weight:700;font-size:1.02rem;line-height:1.45;text-decoration:none!important}
.nf-th:hover{color:var(--cyan)!important}
.nf-s{color:#b9c4e4;font-size:.88rem;line-height:1.55;margin-top:3px}
.nf-en{color:var(--muted);font-size:.72rem;margin-top:4px;font-style:italic;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nf-car{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px 2px 12px;margin:6px 0 10px}
.nf-hl{flex:0 0 min(300px,82%);scroll-snap-align:start;background:var(--panel);border:1px solid var(--line);
  padding:14px 16px;display:flex;flex-direction:column;gap:10px;min-height:190px;
  clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}
.nf-hl .a{display:flex;align-items:center;gap:8px}
.nf-hl .t{font-family:var(--mono);font-weight:700;color:var(--gold);font-size:1.1rem;letter-spacing:.06em}
.nf-hl .x{color:var(--text)!important;font-size:1.08rem;line-height:1.5;font-weight:600;flex:1;text-decoration:none!important}
.nf-hl .x:hover{color:var(--cyan)!important}
.nf-hl .b{display:flex;justify-content:space-between;align-items:center;font-size:.8rem;color:var(--muted)}
.nf-pct{font-family:var(--mono);font-weight:700}
.nf-pct.up{color:#19f5a5!important;-webkit-text-fill-color:#19f5a5}.nf-pct.dn{color:#ff2a6d!important;-webkit-text-fill-color:#ff2a6d}
</style>
"""


def _pct(p):
    if p is None:
        return ""
    cls = "up" if p >= 0 else "dn"
    arrow = "↗" if p >= 0 else "↘"
    return f'<span class="nf-pct {cls}">{arrow} {abs(p):.2f}%</span>'


def _e(x):
    return html.escape(str(x or ""), quote=True)


def _card(it, now):
    cls = {"บวก": "pos", "ลบ": "neg"}.get(it["tone"], "mid")
    when = ago(it["ts"], now) if it["ts"] else ""
    th = _e(it["th"])
    title = (f'<a class="nf-th" href="{_e(it["link"])}" target="_blank" rel="noopener">{th}</a>'
             if it.get("link") else f'<span class="nf-th">{th}</span>')
    s = f'<div class="nf-s">{_e(it["sum"])}</div>' if it.get("sum") else ""
    en = ""
    if it["th"] != it["title_en"]:
        en = f'<div class="nf-en" title="{_e(it["title_en"])}">{_e(it["title_en"])}</div>'
    return (f'<div class="nf-card {cls}"><div class="nf-bar"></div><div class="nf-body">'
            f'<div class="nf-top"><span class="nf-chip">{_e(it["ticker"])}</span>'
            f'<span class="nf-tone {cls}">{_e(it["tone"])}</span>'
            f'<span>{_e(it["source"])}</span><span>{"· " if it["source"] else ""}{_e(when)}</span></div>'
            f'{title}{s}{en}</div></div>')


def render(ai_key: str):
    st.markdown(_CSS, unsafe_allow_html=True)
    st.caption("ใส่รายชื่อหุ้นที่อยากเฝ้าดู (สูงสุด 15 ตัว) ระบบดึงข่าวล่าสุดจาก Google News + Yahoo Finance "
               "แล้วแปล/สรุปเป็นภาษาไทยให้ทุกข่าว")
    if "nf_wl" not in st.session_state:
        st.session_state["nf_wl"] = "NVDA, SNDK, TSLA, AMD, MU, META, GOOGL, AMZN, AVGO"
    wl = st.text_area("รายชื่อหุ้นที่อยากเฝ้าดู (คั่นด้วยจุลภาค หรือขึ้นบรรทัดใหม่)", key="nf_wl", height=80)
    c1, c2, _ = st.columns([1, 1.2, 3], vertical_alignment="bottom")
    with c1:
        go = st.button("📡 สแกนข่าวล่าสุด")
    with c2:
        days = st.selectbox("ย้อนหลัง", [1, 2, 3, 7], index=2,
                            format_func=lambda d: "24 ชม." if d == 1 else f"{d} วัน",
                            label_visibility="collapsed")
    if not ai_key:
        st.caption("💡 ตอนนี้แปลหัวข้อฟรี (แปลตรงตัว) — ใส่คีย์ AI ที่แถบข้าง จะได้ภาษาไทยธรรมชาติขึ้น "
                   "+ สรุปประเด็นรายข่าว + สรุปภาพรวมรายหุ้น + บอกว่าบวก/ลบต่อหุ้น")

    if go:
        tickers = []
        for t in wl.replace("\n", ",").split(","):
            t = t.strip().upper()
            if t and t not in tickers:
                tickers.append(t)
        tickers = tickers[:15]
        if not tickers:
            st.error("กรุณาใส่ชื่อหุ้นอย่างน้อย 1 ตัวครับ")
        else:
            with st.spinner(f"กำลังดึงข่าวล่าสุดและแปลเป็นไทย ({len(tickers)} หุ้น)..."):
                st.session_state.feed_result = build_feed(tuple(tickers), ai_key or "", int(days))

    res = st.session_state.get("feed_result")
    if not res:
        st.info("ใส่รายชื่อหุ้นแล้วกด 📡 สแกนข่าวล่าสุด ได้เลยครับ")
        return

    feed, per = res["feed"], res["per"]
    now = datetime.now(BKK)
    st.caption(f"อัปเดตเมื่อ {res['fetched'].strftime('%H:%M')} น. · ข่าวเก็บผลไว้ 5 นาที กดสแกนใหม่เพื่อรีเฟรช")

    if not feed:
        st.warning("ไม่พบข่าวในช่วงเวลานี้ ลองขยายช่วง 'ย้อนหลัง' หรือตรวจชื่อหุ้นอีกครั้งครับ")
        return

    # ---- สรุปเด่นวันนี้ (การ์ดเลื่อนซ้าย-ขวา แบบ Dime! Daily) ----
    cards = []
    for t, p in per.items():
        if not p["headline"]:
            continue
        link = p["hl_link"]
        txt = _e(p["headline"])
        body = (f'<a class="x" href="{_e(link)}" target="_blank" rel="noopener">{txt}</a>' if link
                else f'<span class="x">{txt}</span>')
        cards.append(f'<div class="nf-hl"><div class="a"><span class="nf-chip">{_e(t)}</span>'
                     f'<span style="margin-left:auto">{_pct(p["pct"])}</span></div>{body}'
                     f'<div class="b"><span>{_e(p["hl_src"])}</span>'
                     f'<span>{"ราคา $" + format(p["price"], ",.2f") if p["price"] else ""}</span></div></div>')
    if cards:
        st.markdown('<div class="section-label">สรุปเด่นวันนี้</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="nf-car">{"".join(cards)}</div>', unsafe_allow_html=True)

    # ---- สรุปภาพรวมรายหุ้น ----
    boxes = []
    for t, p in per.items():
        col = {"เอียงบวก": "var(--up)", "เอียงลบ": "var(--down)"}.get(p["overall"], "var(--muted)")
        ov = p["overview"] or (f"พบข่าวล่าสุด {p['n']} ข่าว — บวก {p['pos']} · ลบ {p['neg']}"
                               if p["n"] else "ไม่พบข่าวในช่วงนี้")
        ed = p["earnings"].strftime("%d/%m/%Y") if p["earnings"] else "ไม่ทราบ"
        boxes.append(
            f'<div class="nf-box"><div class="h"><span class="tk">{_e(t)}</span>'
            f'<span class="nm">{_e(p["name"])}</span>'
            f'<span style="margin-left:auto;color:{col};font-size:.78rem;font-weight:700">{_e(p["overall"])}</span></div>'
            f'<div class="ov">{_e(ov)}</div>'
            f'<div class="ft"><span>ข่าว {p["n"]}</span><span>🟢 {p["pos"]}</span><span>🔴 {p["neg"]}</span>'
            f'<span>Earnings ถัดไป: {_e(ed)}</span></div></div>')
    st.markdown('<div class="section-label">ภาพรวมรายหุ้น</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="nf-sum">{"".join(boxes)}</div>', unsafe_allow_html=True)

    groups = {}
    for p_t, p in per.items():
        if p["sector"]:
            groups.setdefault(p["sector"], []).append(p_t)
    groups = {k: v for k, v in groups.items() if len(v) > 1}
    if groups:
        st.caption("กลุ่มเดียวกันในลิสต์ของคุณ (อาจขยับตามกัน): " +
                   " · ".join(f"{k}: {', '.join(v)}" for k, v in groups.items()))

    # ---- ฟิลเตอร์ ----
    f1, f2 = st.columns([3, 2])
    with f1:
        pick = st.radio("หุ้น", ["ทั้งหมด"] + list(per.keys()), horizontal=True,
                        label_visibility="collapsed", key="nf_pick")
    with f2:
        tone = st.radio("โทน", ["ทั้งหมด", "บวก", "ลบ"], horizontal=True,
                        label_visibility="collapsed", key="nf_tone")
    rows = [x for x in feed
            if (pick == "ทั้งหมด" or x["ticker"] == pick) and (tone == "ทั้งหมด" or x["tone"] == tone)]
    if not rows:
        st.info("ไม่มีข่าวตรงกับตัวกรองนี้")
        return

    # ---- ฟีดตามวัน ----
    out, last = [], None
    for it in rows:
        key = th_date(it["ts"]) if it["ts"] else "ไม่ทราบวันที่"
        if key != last:
            label = key
            if it["ts"] and it["ts"].date() == now.date():
                label = "วันนี้ · " + key
            elif it["ts"] and it["ts"].date() == (now - timedelta(days=1)).date():
                label = "เมื่อวาน · " + key
            out.append(f'<div class="nf-day">{_e(label)}</div>')
            last = key
        out.append(_card(it, now))
    st.markdown("".join(out), unsafe_allow_html=True)

    st.caption(
        ("แปลและสรุปโดย AI จากหัวข้อข่าว (ไม่ได้อ่านเนื้อข่าวเต็ม) — กดหัวข้อเพื่ออ่านต้นฉบับ. "
         if res["ai"] else
         "หัวข้อแปลด้วยเครื่องแปลฟรี และโทนข่าวเป็น keyword คร่าวๆ — ใส่คีย์ AI เพื่อสรุปและแยกโทนแม่นขึ้น. ")
        + "ไม่ใช่คำแนะนำซื้อ-ขาย")