# -*- coding: utf-8 -*-
"""
theme.py
========
ดีไซน์ทั้งเว็บ: ธีมมืด + ทอง สไตล์ terminal การเงิน (กระจกใส เรืองแสง ตัวเลขฟอนต์โมโน)

app.py เรียกใช้:
- ensure_streamlit_theme(โฟลเดอร์แอป)  สร้างไฟล์ .streamlit/config.toml ให้อัตโนมัติ (ทำให้ตาราง/ช่องกรอก/แถบบนเป็นสีเข้มจริง)
- inject()                               ฉีด CSS ทั้งเว็บ
- brand_sidebar()                        โลโก้ + สถานะตลาดสหรัฐ (เวลาไทย) บนแถบซ้าย
- ticker_tape(markets)                   แถบราคาเลื่อนด้านบน
- hero(title, subtitle, pill)            หัวหน้าแบบใหม่
"""

from datetime import datetime
from pathlib import Path

import streamlit as st

CONFIG_TOML = """[theme]
base = "dark"
primaryColor = "#f5c542"
backgroundColor = "#07090f"
secondaryBackgroundColor = "#10131c"
textColor = "#eceff4"
font = "sans serif"

[client]
toolbarMode = "minimal"

[browser]
gatherUsageStats = false
"""

CSS = """
<style>
:root{
  --bg:#07090f; --panel:rgba(255,255,255,.035); --panel2:rgba(255,255,255,.06);
  --line:rgba(255,255,255,.09); --gold:#f5c542; --gold2:#d4a017;
  --up:#2ee59d; --down:#ff5470; --text:#eceff4; --muted:#8b93a7;
}

/* ---------- พื้นหลัง: ไล่สี + ตารางจาง ๆ ---------- */
.stApp{
  background:
    radial-gradient(1100px 520px at 6% -8%, rgba(245,197,66,.10), transparent 60%),
    radial-gradient(900px 500px at 100% 0%, rgba(110,120,255,.10), transparent 55%),
    linear-gradient(rgba(255,255,255,.022) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.022) 1px, transparent 1px),
    #07090f !important;
  background-size:auto, auto, 46px 46px, 46px 46px, auto !important;
  background-attachment:fixed !important;
}
header[data-testid="stHeader"]{background:transparent !important; backdrop-filter:blur(8px);}
.block-container{padding-top:1.4rem !important; max-width:1400px;}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,.14);border-radius:10px}
::-webkit-scrollbar-thumb:hover{background:rgba(245,197,66,.5)}
::selection{background:rgba(245,197,66,.35)}

/* ---------- แถบซ้าย ---------- */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#0c0f17 0%,#080a10 100%) !important;
  border-right:1px solid var(--line) !important;
}
.brand{display:flex;align-items:center;gap:12px;margin:2px 0 12px 0;}
.brand-mark{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;font-size:22px;color:#14151b;
  background:linear-gradient(135deg,#f5c542,#d4a017);box-shadow:0 0 22px rgba(245,197,66,.35);}
.brand-name{font-weight:800;font-size:20px;letter-spacing:3px;color:#fff;line-height:1.1;}
.brand-sub{font-size:10px;letter-spacing:2.4px;color:var(--muted);}
.status{display:flex;align-items:center;gap:9px;padding:8px 12px;border-radius:10px;border:1px solid var(--line);
  background:var(--panel);font-size:12.5px;color:var(--text);margin-bottom:14px;}
.status .dot{width:8px;height:8px;border-radius:50%;background:var(--c);box-shadow:0 0 10px var(--c);animation:pulse 1.8s infinite;flex:none;}
.status-open{--c:#2ee59d}.status-ext{--c:#f5c542}.status-closed{--c:#ff5470}
.status small{display:block;color:var(--muted);font-size:11px;}
@keyframes pulse{0%{opacity:1}50%{opacity:.35}100%{opacity:1}}

/* เมนูโหมด: เปลี่ยนวงกลม radio เป็นปุ่มเมนู (Streamlit รุ่นใหม่) */
section[data-testid="stSidebar"] [data-testid="stRadioGroup"]{gap:4px;}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"]{
  width:100%;margin:0 !important;padding:9px 12px !important;border-radius:10px;border:1px solid transparent;
  background:transparent;transition:.15s;cursor:pointer;
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"]:hover{background:var(--panel2);}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] > div > div:first-child{display:none;}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"][data-selected="true"]{
  background:linear-gradient(90deg,rgba(245,197,66,.20),rgba(245,197,66,.04));
  border:1px solid rgba(245,197,66,.38);box-shadow:inset 3px 0 0 var(--gold);
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] p{font-weight:600;font-size:14.5px;}

/* radio แนวนอนในหน้าหลัก: เป็นปุ่มสลับ (segmented) */
[data-testid="stMain"] [data-testid="stRadioGroup"]{gap:6px;flex-wrap:wrap;}
[data-testid="stMain"] label[data-testid="stRadioOption"]{
  padding:6px 14px !important;margin:0 !important;border-radius:999px;border:1px solid var(--line);
  background:var(--panel);transition:.15s;cursor:pointer;
}
[data-testid="stMain"] label[data-testid="stRadioOption"]:hover{border-color:rgba(245,197,66,.5);}
[data-testid="stMain"] label[data-testid="stRadioOption"] > div > div:first-child{display:none;}
[data-testid="stMain"] label[data-testid="stRadioOption"][data-selected="true"]{
  background:linear-gradient(135deg,#f5c542,#d4a017);border-color:transparent;box-shadow:0 4px 16px rgba(245,197,66,.28);
}
[data-testid="stMain"] label[data-testid="stRadioOption"][data-selected="true"] p{color:#14151b !important;font-weight:700;}

/* ชุดสำรองสำหรับ Streamlit รุ่นเก่า (baseweb) */
section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-baseweb="radio"]{
  width:100%;margin:0 !important;padding:9px 12px !important;border-radius:10px;border:1px solid transparent;transition:.15s;cursor:pointer;
}
section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child{display:none;}
section.main div[role="radiogroup"] > label[data-baseweb="radio"]{
  padding:6px 14px !important;margin:0 6px 0 0 !important;border-radius:999px;border:1px solid var(--line);background:var(--panel);cursor:pointer;
}
section.main div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child{display:none;}

/* ---------- หัวหน้า (hero) + ของเดิม .app-header ---------- */
.app-header, .hero{
  display:flex !important;align-items:center;gap:16px;padding:18px 24px !important;margin-bottom:14px !important;
  border:1px solid var(--line) !important;border-radius:18px;position:relative;overflow:hidden;
  background:linear-gradient(135deg,rgba(245,197,66,.11),rgba(255,255,255,.02) 42%,rgba(110,120,255,.09));
}
.app-header .mark, .hero-mark{width:46px;height:46px;border-radius:13px;display:grid;place-items:center;flex:none;
  font-size:24px !important;color:#14151b !important;background:linear-gradient(135deg,#f5c542,#d4a017);
  box-shadow:0 0 26px rgba(245,197,66,.38);}
.app-header .title-text h1, .hero-title{margin:0 !important;font-size:26px !important;font-weight:800 !important;color:#fff !important;letter-spacing:.3px;}
.app-header .title-text p, .hero-sub{margin:3px 0 0 0 !important;font-size:13px !important;color:var(--muted) !important;}
.hero-pill{margin-left:auto;font-size:11px;letter-spacing:1.4px;padding:5px 12px;border-radius:999px;white-space:nowrap;
  border:1px solid rgba(46,229,157,.4);color:var(--up);background:rgba(46,229,157,.08);}

/* หัวข้อส่วน */
.section-label{display:flex !important;align-items:center;gap:12px;color:var(--gold) !important;font-size:13px !important;
  font-weight:700 !important;letter-spacing:1.4px;margin:6px 0 10px 0 !important;}
.section-label::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,rgba(245,197,66,.45),transparent);}
.stMarkdown h4{border-left:3px solid var(--gold);padding-left:11px;margin-top:1.3rem !important;font-weight:700 !important;}

/* ---------- การ์ด / ตัวเลข ---------- */
div[data-testid="stMetric"]{
  background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02)) !important;
  border:1px solid var(--line) !important;border-radius:14px !important;padding:14px 16px 10px 16px !important;
  backdrop-filter:blur(8px);box-shadow:0 8px 24px rgba(0,0,0,.25);transition:.15s;
}
div[data-testid="stMetric"]:hover{border-color:rgba(245,197,66,.45) !important;transform:translateY(-1px);}
div[data-testid="stMetricValue"]{font-family:'IBM Plex Mono',monospace !important;font-weight:600 !important;font-size:1.9rem !important;}
div[data-testid="stMetricLabel"]{color:var(--muted) !important;letter-spacing:.5px;}

details[data-testid="stExpander"]{
  background:var(--panel) !important;border:1px solid var(--line) !important;border-radius:14px !important;
  backdrop-filter:blur(6px);margin-bottom:10px !important;
}
details[data-testid="stExpander"] summary{font-weight:600;}
details[data-testid="stExpander"] summary:hover{color:var(--gold) !important;}

div[data-testid="stAlert"]{border-radius:14px !important;border:1px solid var(--line) !important;backdrop-filter:blur(6px);}

/* ตาราง */
div[data-testid="stDataFrame"]{border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.25);}
.stMarkdown table{border-collapse:separate;border-spacing:0;width:100%;font-size:14px;border:1px solid var(--line);border-radius:12px;overflow:hidden;}
.stMarkdown th{background:var(--panel2);font-weight:700;text-align:left;}
.stMarkdown td,.stMarkdown th{padding:8px 12px;border-bottom:1px solid var(--line);}
.stMarkdown tr:last-child td{border-bottom:none;}

/* ช่องกรอก */
div[data-baseweb="input"] > div, div[data-baseweb="base-input"], div[data-baseweb="select"] > div,
div[data-baseweb="textarea"], textarea{
  background:#0d111a !important;border:1px solid var(--line) !important;border-radius:11px !important;
}
div[data-baseweb="input"]:focus-within > div, div[data-baseweb="textarea"]:focus-within,
div[data-baseweb="select"]:focus-within > div{
  border-color:rgba(245,197,66,.7) !important;box-shadow:0 0 0 3px rgba(245,197,66,.14) !important;
}
input, textarea{color:var(--text) !important;caret-color:var(--gold);}
input::placeholder, textarea::placeholder{color:#5f6779 !important;}

/* ปุ่ม */
.stButton > button, .stDownloadButton > button{
  background:linear-gradient(135deg,#f5c542,#d4a017) !important;color:#14151b !important;font-weight:700 !important;
  border:none !important;border-radius:11px !important;letter-spacing:.3px;transition:.15s;
  box-shadow:0 4px 14px rgba(245,197,66,.18);
}
.stButton > button:hover, .stDownloadButton > button:hover{
  transform:translateY(-1px);box-shadow:0 8px 22px rgba(245,197,66,.34);filter:brightness(1.06);
}
.stButton > button p{color:#14151b !important;}

/* แท็บ */
button[data-baseweb="tab"]{font-weight:600;color:var(--muted);}
button[data-baseweb="tab"][aria-selected="true"]{color:var(--gold) !important;}
div[data-baseweb="tab-highlight"]{background:var(--gold) !important;height:3px !important;border-radius:3px;}
div[data-baseweb="tab-border"]{background:var(--line) !important;}

hr{border-color:var(--line) !important;}

/* ---------- แถบราคาเลื่อน ---------- */
.tape{overflow:hidden;white-space:nowrap;border:1px solid var(--line);border-radius:12px;background:var(--panel);
  padding:9px 0;margin-bottom:12px;mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);}
.tape-track{display:inline-flex;animation:tape 55s linear infinite;}
.tape:hover .tape-track{animation-play-state:paused;}
@keyframes tape{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.tape-item{display:inline-flex;align-items:baseline;gap:8px;margin:0 22px;font-family:'IBM Plex Mono',monospace;font-size:13px;}
.tape-item b{color:#fff;font-weight:600;font-family:'IBM Plex Sans Thai',sans-serif;}
.tape-item .up{color:var(--up)}.tape-item .down{color:var(--down)}.tape-item .na{color:var(--muted)}
</style>
"""


def _html(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


def ensure_streamlit_theme(app_dir) -> bool:
    """สร้าง .streamlit/config.toml ถ้ายังไม่มี คืน True ถ้าเพิ่งสร้าง (ต้องรีสตาร์ทแอป 1 ครั้งให้ตารางเป็นสีเข้ม)"""
    try:
        folder = Path(app_dir) / ".streamlit"
        cfg = folder / "config.toml"
        if cfg.exists():
            return False
        folder.mkdir(exist_ok=True)
        cfg.write_text(CONFIG_TOML, encoding="utf-8")
        return True
    except Exception:
        return False


def inject():
    st.markdown(CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str = "", pill: str = "LIVE"):
    pill_html = f'<div class="hero-pill">● {pill}</div>' if pill else ""
    st.markdown(_html(f"""
        <div class="hero">
        <div class="hero-mark">◆</div>
        <div><div class="hero-title">{title}</div><div class="hero-sub">{subtitle}</div></div>
        {pill_html}
        </div>
    """), unsafe_allow_html=True)


def market_status():
    """สถานะตลาดสหรัฐ (ไม่รวมวันหยุดพิเศษ) พร้อมเวลาไทย"""
    try:
        from zoneinfo import ZoneInfo
        ny = datetime.now(ZoneInfo("America/New_York"))
        th = datetime.now(ZoneInfo("Asia/Bangkok"))
    except Exception:
        return None
    mins = ny.hour * 60 + ny.minute
    if ny.weekday() >= 5:
        cls, label = "closed", "ตลาดสหรัฐปิด (สุดสัปดาห์)"
    elif 570 <= mins < 960:
        cls, label = "open", "ตลาดสหรัฐเปิดซื้อขาย"
    elif 240 <= mins < 570:
        cls, label = "ext", "พรีมาร์เก็ต (ก่อนเปิด)"
    elif 960 <= mins < 1200:
        cls, label = "ext", "หลังปิดตลาด (After-hours)"
    else:
        cls, label = "closed", "ตลาดสหรัฐปิด"
    return {"cls": cls, "label": label, "thai": th.strftime("%H:%M")}


def brand_sidebar():
    st.markdown(_html("""
        <div class="brand"><div class="brand-mark">◆</div>
        <div><div class="brand-name">QUANT</div><div class="brand-sub">STOCK ANALYZER</div></div></div>
    """), unsafe_allow_html=True)
    s = market_status()
    if s:
        st.markdown(_html(f"""
            <div class="status status-{s['cls']}"><span class="dot"></span>
            <div>{s['label']}<small>เวลาไทย {s['thai']} น. · ไม่รวมวันหยุดพิเศษ</small></div></div>
        """), unsafe_allow_html=True)


def ticker_tape(markets: dict):
    """markets: {ชื่อ: (ราคา, %เปลี่ยน) หรือ None}"""
    items = ""
    for name, v in markets.items():
        if v:
            cls, arrow = ("up", "▲") if v[1] >= 0 else ("down", "▼")
            items += f'<span class="tape-item"><b>{name}</b>{v[0]:,.2f}<span class="{cls}">{arrow} {abs(v[1]):.2f}%</span></span>'
        else:
            items += f'<span class="tape-item"><b>{name}</b><span class="na">—</span></span>'
    if not items:
        return
    st.markdown(f'<div class="tape"><div class="tape-track">{items}{items}</div></div>', unsafe_allow_html=True)