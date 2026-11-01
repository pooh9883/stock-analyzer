# -*- coding: utf-8 -*-
"""
theme.py
========
ดีไซน์ทั้งเว็บ: สไตล์ Cyberpunk (เหลือง-ฟ้า-ชมพูนีออน มุมตัด สแกนไลน์ ตัวเลขฟอนต์โมโน)

app.py เรียกใช้:
- ensure_streamlit_theme(โฟลเดอร์แอป)  สร้างไฟล์ .streamlit/config.toml ให้อัตโนมัติ (ทำให้ตาราง/ช่องกรอก/แถบบันเป็นสีเข้มจริง)
- inject()                               ฉีด CSS ทั้งเว็บ
- brand_sidebar()                        โลโก้ + สถานะตลาดสหรัฐ (เวลาไทย) บนแถบซ้าย
- ticker_tape(markets)                   แถบราคาเลื่อนด้านบน
- hero(title, subtitle, pill)            หัวหน้าแบบใหม่
- hud(markets)                           แถบสถานะล่างจอ + ตัวเลขราคากะพริบ
"""

from datetime import datetime
from pathlib import Path

import streamlit as st

try:
    import logo_asset as _logo   # logo_asset.py — โลโก้ใหม่ (base64)
except Exception:
    _logo = None

CONFIG_TOML = """[theme]
base = "dark"
primaryColor = "#fcee0a"
backgroundColor = "#05060d"
secondaryBackgroundColor = "#0b0d1a"
textColor = "#e6f1ff"
font = "sans serif"

[client]
toolbarMode = "minimal"

[browser]
gatherUsageStats = false

[server]
enableStaticServing = true
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');
:root{
  --bg:#05060d; --panel:rgba(12,14,28,.78); --panel2:rgba(252,238,10,.07);
  --line:rgba(0,240,255,.17); --gold:#fcee0a; --gold2:#c9bc00;
  --cyan:#00f0ff; --pink:#ff2a6d; --violet:#8b5cf6;
  --up:#19f5a5; --down:#ff2a6d; --text:#e6f1ff; --muted:#7d86a6;
  --cut:12px;
  --cp:polygon(0 0, calc(100% - var(--cut)) 0, 100% var(--cut), 100% 100%, var(--cut) 100%, 0 calc(100% - var(--cut)));
  --mono:'Share Tech Mono','IBM Plex Mono',ui-monospace,monospace;
}

/* ---------- ฟอนต์: Chakra Petch (มีภาษาไทย) ---------- */
.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4,
label, summary, button, input, textarea, [data-testid="stMetricLabel"], [data-testid="stCaptionContainer"],
.hero, .brand, .status, .tape-item b, .section-label, button[data-baseweb="tab"]{
  font-family:'Chakra Petch','IBM Plex Sans Thai',system-ui,sans-serif;
}

/* ---------- พื้นหลัง: ตารางนีออน + แสงม่วง/เหลือง + สแกนไลน์ ---------- */
.stApp{
  background:
    radial-gradient(1000px 520px at 4% -10%, rgba(252,238,10,.09), transparent 60%),
    radial-gradient(900px 560px at 102% 2%, rgba(255,42,109,.11), transparent 58%),
    radial-gradient(800px 500px at 50% 115%, rgba(0,240,255,.07), transparent 60%),
    linear-gradient(rgba(0,240,255,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,240,255,.03) 1px, transparent 1px),
    #05060d !important;
  background-size:auto, auto, auto, 44px 44px, 44px 44px, auto !important;
  background-attachment:fixed !important;
}
.stApp::after{
  content:"";position:fixed;inset:0;pointer-events:none;z-index:9999;
  background:none;   /* เอาเส้นสแกนไลน์พาดจอออก */
}
header[data-testid="stHeader"]{background:transparent !important; backdrop-filter:blur(8px);}
.block-container{padding-top:1.4rem !important; max-width:1400px;}
::-webkit-scrollbar{width:9px;height:9px}
::-webkit-scrollbar-track{background:#05060d}
::-webkit-scrollbar-thumb{background:rgba(0,240,255,.28);border-radius:0}
::-webkit-scrollbar-thumb:hover{background:var(--gold)}
::selection{background:var(--gold);color:#05060d}

/* ---------- แถบซ้าย ---------- */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#090b17 0%,#05060d 100%) !important;
  border-right:1px solid var(--line) !important;
  box-shadow:6px 0 30px rgba(0,240,255,.04);
}
.brand{display:flex;align-items:center;gap:10px;margin:2px 0 12px 0;}
.brand-mark{width:42px;height:42px;display:grid;place-items:center;font-size:22px;color:#05060d;font-weight:700;
  background:var(--gold);clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px));}
.qs-fs-btn{display:flex;align-items:center;justify-content:center;margin:0 0 12px 0;padding:7px 10px;cursor:pointer;user-select:none;
  font-size:12.5px;font-weight:600;letter-spacing:1.2px;color:var(--cyan);border:1px solid rgba(0,240,255,.35);background:rgba(0,240,255,.06);
  clip-path:polygon(0 0,calc(100% - 8px) 0,100% 8px,100% 100%,8px 100%,0 calc(100% - 8px));transition:.15s;}
.qs-fs-btn:hover{background:var(--cyan);color:#05060d;}
.qs-fs-btn .on-exit{display:none;}
html.qs-isfs .qs-fs-btn .on-enter{display:none;}
html.qs-isfs .qs-fs-btn .on-exit{display:inline;}
.brand-logo{width:100px;height:auto;flex:none;display:block;filter:drop-shadow(0 0 7px rgba(252,238,10,.28));}
.brand-name{font-weight:700;font-size:21px;letter-spacing:5px;color:#fff;line-height:1.1;
  text-shadow:1.5px 0 rgba(255,42,109,.85),-1.5px 0 rgba(0,240,255,.85);}
.brand-sub{font-size:10px;letter-spacing:3px;color:var(--cyan);opacity:.85;}
.status{display:flex;align-items:center;gap:9px;padding:8px 12px;border:1px solid var(--line);border-left:3px solid var(--c);
  background:var(--panel);font-size:12.5px;color:var(--text);margin-bottom:14px;}
.status .dot{width:8px;height:8px;background:var(--c);box-shadow:0 0 10px var(--c);animation:pulse 1.6s infinite;flex:none;}
.status-open{--c:#19f5a5}.status-ext{--c:#fcee0a}.status-closed{--c:#ff2a6d}
.status small{display:block;color:var(--muted);font-size:11px;}
@keyframes pulse{0%{opacity:1}50%{opacity:.3}100%{opacity:1}}

/* ซ่อนแถบเลื่อนของแถบซ้าย (ยังเลื่อนด้วยล้อเมาส์/นิ้วได้ตามปกติ) */
section[data-testid="stSidebar"], section[data-testid="stSidebar"] *{scrollbar-width:none !important;-ms-overflow-style:none !important;}
section[data-testid="stSidebar"]::-webkit-scrollbar, section[data-testid="stSidebar"] *::-webkit-scrollbar{display:none !important;width:0 !important;height:0 !important;}

/* เมนูโหมด */
section[data-testid="stSidebar"] [data-testid="stRadioGroup"]{gap:4px;}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"]{
  width:100%;margin:0 !important;padding:9px 12px !important;border-radius:0;border:1px solid transparent;
  background:transparent;transition:.15s;cursor:pointer;
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"]:hover{background:var(--panel2);border-color:rgba(252,238,10,.25);}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] > div > div:first-child{display:none;}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"][data-selected="true"]{
  background:linear-gradient(90deg,rgba(252,238,10,.20),rgba(252,238,10,.02));
  border:1px solid rgba(252,238,10,.45);box-shadow:inset 3px 0 0 var(--gold),0 0 18px rgba(252,238,10,.10);
}
section[data-testid="stSidebar"] label[data-testid="stRadioOption"] p{font-weight:600;font-size:14.5px;letter-spacing:.3px;}

/* radio แนวนอนในหน้าหลัก: ปุ่มสลับทรงตัดมุม */
[data-testid="stMain"] [data-testid="stRadioGroup"]{gap:6px;flex-wrap:wrap;}
[data-testid="stMain"] label[data-testid="stRadioOption"]{
  padding:6px 14px !important;margin:0 !important;border-radius:0;border:1px solid var(--line);
  background:var(--panel);transition:.15s;cursor:pointer;clip-path:polygon(0 0,calc(100% - 8px) 0,100% 8px,100% 100%,8px 100%,0 calc(100% - 8px));
}
[data-testid="stMain"] label[data-testid="stRadioOption"]:hover{border-color:var(--cyan);background:rgba(0,240,255,.07);}
[data-testid="stMain"] label[data-testid="stRadioOption"] > div > div:first-child{display:none;}
[data-testid="stMain"] label[data-testid="stRadioOption"][data-selected="true"]{
  background:var(--gold);border-color:var(--gold);
}
[data-testid="stMain"] label[data-testid="stRadioOption"][data-selected="true"] p{color:#05060d !important;font-weight:700;}

/* ชุดสำรองสำหรับ Streamlit รุ่นเก่า (baseweb) */
section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-baseweb="radio"]{
  width:100%;margin:0 !important;padding:9px 12px !important;border-radius:0;border:1px solid transparent;transition:.15s;cursor:pointer;
}
section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child{display:none;}
section.main div[role="radiogroup"] > label[data-baseweb="radio"]{
  padding:6px 14px !important;margin:0 6px 0 0 !important;border-radius:0;border:1px solid var(--line);background:var(--panel);cursor:pointer;
}
section.main div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child{display:none;}

/* ---------- หัวหน้า (hero) ---------- */
.app-header, .hero{
  display:flex !important;align-items:center;gap:16px;padding:18px 26px !important;margin-bottom:14px !important;
  border:1px solid var(--line) !important;border-left:4px solid var(--gold) !important;border-radius:0 !important;position:relative;overflow:hidden;
  background:
    linear-gradient(135deg,rgba(252,238,10,.10),rgba(5,6,13,.4) 38%,rgba(255,42,109,.10)),
    repeating-linear-gradient(135deg,transparent 0 10px,rgba(0,240,255,.025) 10px 11px);
  clip-path:polygon(0 0,calc(100% - 22px) 0,100% 22px,100% 100%,22px 100%,0 calc(100% - 22px));
}
.app-header::after, .hero::after{
  content:"";position:absolute;left:0;right:0;top:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--cyan),var(--gold),var(--pink),transparent);
  background-size:200% 100%;animation:sweep 5s linear infinite;
}
@keyframes sweep{0%{background-position:0 0}100%{background-position:200% 0}}
.hero-logo{width:112px;height:auto;flex:none;display:block;filter:drop-shadow(0 0 9px rgba(252,238,10,.30));}
.app-header .mark, .hero-mark{width:46px;height:46px;display:grid;place-items:center;flex:none;
  font-size:24px !important;color:#05060d !important;background:var(--gold);font-weight:700;
  clip-path:polygon(0 0,calc(100% - 11px) 0,100% 11px,100% 100%,11px 100%,0 calc(100% - 11px));}
.app-header .title-text h1, .hero-title{margin:0 !important;font-size:27px !important;font-weight:700 !important;color:#fff !important;
  letter-spacing:1.2px;text-shadow:2px 0 rgba(255,42,109,.75),-2px 0 rgba(0,240,255,.75);}
.app-header .title-text p, .hero-sub{margin:3px 0 0 0 !important;font-size:13px !important;color:var(--muted) !important;letter-spacing:.4px;}
.hero-pill{margin-left:auto;font-family:var(--mono);font-size:11px;letter-spacing:2px;padding:5px 12px;white-space:nowrap;
  border:1px solid var(--cyan);color:var(--cyan);background:rgba(0,240,255,.08);
  clip-path:polygon(0 0,calc(100% - 7px) 0,100% 7px,100% 100%,7px 100%,0 calc(100% - 7px));}

/* หัวข้อส่วน */
.section-label{display:flex !important;align-items:center;gap:12px;color:#5ee7ff !important;font-size:13px !important;
  font-weight:700 !important;letter-spacing:2px;margin:6px 0 10px 0 !important;}
.section-label::before{content:"//";color:var(--cyan);font-family:var(--mono);}
.section-label::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,rgba(0,240,255,.45),transparent);}
.stMarkdown h4{border-left:3px solid var(--cyan);padding-left:11px;margin-top:1.3rem !important;font-weight:700 !important;letter-spacing:.5px;}

/* ---------- การ์ด / ตัวเลข ---------- */
div[data-testid="stMetric"]{
  background:linear-gradient(160deg,rgba(0,240,255,.07),rgba(12,14,28,.7) 55%) !important;
  border:1px solid var(--line) !important;border-top:2px solid var(--cyan) !important;border-radius:0 !important;padding:14px 16px 10px 16px !important;
  backdrop-filter:blur(6px);transition:.15s;
  clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px));
}
div[data-testid="stMetric"]:hover{border-color:var(--gold) !important;border-top-color:var(--gold) !important;background:linear-gradient(160deg,rgba(252,238,10,.08),rgba(12,14,28,.7) 55%) !important;}
div[data-testid="stMetricValue"]{font-family:var(--mono) !important;font-weight:400 !important;font-size:1.95rem !important;letter-spacing:.5px;}
div[data-testid="stMetricLabel"]{color:var(--muted) !important;letter-spacing:1px;}

details[data-testid="stExpander"]{
  background:var(--panel) !important;border:1px solid var(--line) !important;border-left:3px solid var(--cyan) !important;border-radius:0 !important;
  backdrop-filter:blur(6px);margin-bottom:10px !important;
}
details[data-testid="stExpander"] summary{font-weight:600;letter-spacing:.3px;}
details[data-testid="stExpander"] summary:hover{color:var(--gold) !important;}
details[data-testid="stExpander"][open]{border-left-color:var(--gold) !important;}

div[data-testid="stAlert"]{border-radius:0 !important;border:1px solid var(--line) !important;border-left:3px solid var(--cyan) !important;backdrop-filter:blur(6px);}

/* ตาราง */
div[data-testid="stDataFrame"]{border:1px solid var(--line);border-radius:0;overflow:hidden;}
.stMarkdown table{border-collapse:separate;border-spacing:0;width:100%;font-size:14px;border:1px solid var(--line);border-radius:0;overflow:hidden;}
.stMarkdown th{background:rgba(0,240,255,.08);font-weight:700;text-align:left;color:var(--cyan);letter-spacing:.6px;}
.stMarkdown td,.stMarkdown th{padding:8px 12px;border-bottom:1px solid var(--line);}
.stMarkdown tr:last-child td{border-bottom:none;}

/* ช่องกรอก */
div[data-baseweb="input"] > div, div[data-baseweb="base-input"], div[data-baseweb="select"] > div,
div[data-baseweb="textarea"], textarea{
  background:#080a15 !important;border:1px solid var(--line) !important;border-bottom:2px solid rgba(0,240,255,.45) !important;border-radius:0 !important;
}
div[data-baseweb="input"]:focus-within > div, div[data-baseweb="textarea"]:focus-within,
div[data-baseweb="select"]:focus-within > div{
  border-color:var(--gold) !important;box-shadow:0 0 0 3px rgba(252,238,10,.13),0 0 18px rgba(252,238,10,.12) !important;
}
input, textarea{color:var(--text) !important;caret-color:var(--gold);}
input[type="number"], div[data-baseweb="input"] input{font-family:var(--mono);}
input::placeholder, textarea::placeholder{color:#4f5878 !important;}

/* ปุ่ม: ทรงตัดมุม เหลืองนีออน (glow ทำที่ตัวห่อ เพราะ clip-path ตัดเงาของปุ่มเอง) */
.stButton, .stDownloadButton, [data-testid="stFormSubmitButton"]{filter:drop-shadow(0 0 6px rgba(252,238,10,.28));transition:.15s;}
.stButton:hover, .stDownloadButton:hover, [data-testid="stFormSubmitButton"]:hover{filter:drop-shadow(0 0 11px rgba(0,240,255,.65));}
.stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button{
  background:var(--gold) !important;color:#05060d !important;font-weight:700 !important;
  border:none !important;border-radius:0 !important;letter-spacing:.8px;transition:.15s;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px));
}
.stButton > button:hover, .stDownloadButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover{background:var(--cyan) !important;color:#05060d !important;}
.stButton > button:active, [data-testid="stFormSubmitButton"] > button:active{background:var(--pink) !important;}
.stButton > button p, [data-testid="stFormSubmitButton"] > button p{color:#05060d !important;}

/* แท็บ */
/* ---------- ป้ายตัวเลือกที่เลือกแล้ว (multiselect): พื้นเหลือง ตัวอักษรดำ ---------- */
span[data-baseweb="tag"]{background:#fcee0a !important;color:#05060d !important;border-radius:0 !important;}
span[data-baseweb="tag"] *{color:#05060d !important;-webkit-text-fill-color:#05060d !important;font-weight:700 !important;}
span[data-baseweb="tag"] svg{fill:#05060d !important;color:#05060d !important;}

/* ช่องเลือกหลายตัว: ตัวอักษรในป้ายเป็นดำ (ไม่พึ่ง data-baseweb เพราะบาง Streamlit เวอร์ชันไม่มี) */
[data-testid="stMultiSelect"] span,[data-testid="stMultiSelect"] span *{color:#05060d !important;-webkit-text-fill-color:#05060d !important;font-weight:700 !important;}
[data-testid="stMultiSelect"] span svg,[data-testid="stMultiSelect"] span svg *{fill:#05060d !important;stroke:#05060d !important;}
/* แท็บ: ผูกกับ data-testid + role (ใช้ได้หลายเวอร์ชัน) */
[data-testid="stTabs"] [role="tab"]{background:rgba(12,14,28,.75) !important;border:1px solid rgba(0,240,255,.17) !important;border-radius:0 !important;
  padding:9px 18px !important;margin-right:8px !important;clip-path:polygon(0 0,calc(100% - 9px) 0,100% 9px,100% 100%,9px 100%,0 calc(100% - 9px));}
[data-testid="stTabs"] [role="tab"] *{color:#9aa4c4 !important;font-weight:600 !important;}
[data-testid="stTabs"] [role="tab"][aria-selected="true"]{background:#fcee0a !important;border-color:#fcee0a !important;}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] *{color:#05060d !important;-webkit-text-fill-color:#05060d !important;font-weight:800 !important;}
[data-testid="stTabs"] [role="tablist"]{border-bottom:none !important;box-shadow:none !important;}

/* ---------- แท็บ: ปุ่มตัดมุม แท็บที่เลือก = เหลืองทึบ ตัวอักษรดำ (รองรับ Streamlit หลายเวอร์ชัน) ---------- */
div[data-baseweb="tab-list"],div[role="tablist"]{gap:8px !important;padding:4px 2px 10px 2px !important;overflow-x:auto;scrollbar-width:thin;background:transparent !important;}
button[data-baseweb="tab"],button[role="tab"]{
  background:rgba(12,14,28,.75) !important;border:1px solid var(--line) !important;border-radius:0 !important;
  padding:9px 18px !important;height:auto !important;margin:0 !important;white-space:nowrap;
  clip-path:polygon(0 0,calc(100% - 9px) 0,100% 9px,100% 100%,9px 100%,0 calc(100% - 9px));
  transition:.15s;
}
button[data-baseweb="tab"] p,button[role="tab"] p,button[role="tab"] div{color:#9aa4c4 !important;font-weight:600 !important;letter-spacing:.4px;font-size:.92rem !important;margin:0 !important;}
button[data-baseweb="tab"]:hover,button[role="tab"]:hover{background:rgba(0,240,255,.09) !important;border-color:var(--cyan) !important;}
button[data-baseweb="tab"]:hover p,button[role="tab"]:hover p,button[role="tab"]:hover div{color:#e6f1ff !important;}
button[data-baseweb="tab"][aria-selected="true"],button[role="tab"][aria-selected="true"]{background:#fcee0a !important;border-color:#fcee0a !important;filter:drop-shadow(0 0 8px rgba(252,238,10,.45));}
button[data-baseweb="tab"][aria-selected="true"] p,button[role="tab"][aria-selected="true"] p,button[role="tab"][aria-selected="true"] div{color:#05060d !important;-webkit-text-fill-color:#05060d !important;font-weight:800 !important;}
div[data-baseweb="tab-highlight"],div[data-baseweb="tab-border"]{display:none !important;}
div[data-testid="stTabs"] > div[role="tabpanel"], div[data-baseweb="tab-panel"],div[role="tabpanel"]{padding-top:.6rem !important;}

hr{border-color:var(--line) !important;}

/* กันข้อความในปุ่ม/ตัวเลือกถูกตัดเป็น "..." */
[data-testid="stMain"] label[data-testid="stRadioOption"] p,
.stButton > button p, .stDownloadButton > button p, [data-testid="stFormSubmitButton"] > button p{
  white-space:normal !important;overflow:visible !important;text-overflow:clip !important;line-height:1.25;
}
.stButton > button *, .stDownloadButton > button *, [data-testid="stFormSubmitButton"] > button *,
[data-testid="stMain"] label[data-testid="stRadioOption"] *{
  white-space:normal !important;overflow:visible !important;text-overflow:clip !important;
}
.stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button{height:auto !important;min-height:38px;padding:6px 10px !important;}
[data-testid="stMain"] label[data-testid="stRadioOption"]{height:auto !important;max-width:100%;}

/* ---------- แถบราคาเลื่อน ---------- */
.tape{overflow:hidden;white-space:nowrap;border-top:1px solid var(--cyan);border-bottom:1px solid var(--line);background:rgba(0,240,255,.04);
  padding:9px 0;margin-bottom:12px;mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);}
.tape-track{display:inline-flex;animation:tape 55s linear infinite;}
.tape:hover .tape-track{animation-play-state:paused;}
@keyframes tape{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.tape-item{display:inline-flex;align-items:baseline;gap:8px;margin:0 22px;font-family:var(--mono);font-size:13.5px;}
.tape-item b{color:#fff;font-weight:600;letter-spacing:.5px;}
.tape-item .up{color:var(--up);text-shadow:0 0 8px rgba(25,245,165,.45)}
.tape-item .down{color:var(--down);text-shadow:0 0 8px rgba(255,42,109,.45)}
.tape-item .na{color:var(--muted)}

@media (prefers-reduced-motion:reduce){
  .tape-track, .app-header::after, .hero::after, .status .dot{animation:none !important;}
}

/* ---------- Boot (ขึ้นครั้งเดียวต่อเซสชัน) ---------- */
.boot{position:fixed;inset:0;z-index:2147483647;background:#05060d;display:grid;place-items:center;
  animation:bootOut .55s ease 45s forwards;  /* กันค้างกรณีระบบขัดข้อง: จางหายเองหลัง 45 วินาที (ปกติต้องกดปุ่มหรือ Enter) */
  background-image:repeating-linear-gradient(0deg,transparent 0 2px,rgba(0,240,255,.04) 3px);}
.boot-in{font-family:var(--mono);font-size:clamp(10.5px,1.75vw,26px);letter-spacing:1.2px;width:min(940px,88vw);}
.boot .boot-top,.boot .boot-bot{position:absolute;left:5vw;right:5vw;font-family:var(--mono);font-size:clamp(10px,1vw,14px);letter-spacing:3px;color:var(--cyan);opacity:.8;display:flex;justify-content:space-between;}
.boot .boot-logo{position:absolute;top:6vh;left:50%;width:clamp(130px,21vh,260px);height:auto;transform:translateX(-50%);
  opacity:0;filter:drop-shadow(0 0 18px rgba(252,238,10,.35)) drop-shadow(0 0 40px rgba(255,42,109,.20));animation:bootOn 0s .05s forwards;}
@media (max-height:720px){.boot .boot-logo{display:none;}}
.boot .boot-top{top:4.5vh;}.boot .boot-bot{bottom:4.5vh;color:var(--muted);}
.boot .boot-c{position:absolute;width:clamp(28px,4vw,64px);height:clamp(28px,4vw,64px);border:2px solid var(--gold);opacity:.85;}
.boot .boot-c.c-tl{top:2.5vh;left:2.5vw;border-right:0;border-bottom:0}.boot .boot-c.c-tr{top:2.5vh;right:2.5vw;border-left:0;border-bottom:0}
.boot .boot-c.c-bl{bottom:2.5vh;left:2.5vw;border-right:0;border-top:0}.boot .boot-c.c-br{bottom:2.5vh;right:2.5vw;border-left:0;border-top:0}
.boot .bl{white-space:nowrap;overflow:hidden;width:0;opacity:0;color:var(--cyan);margin:5px 0;
  animation:bootOn 0s var(--d) forwards, bootType .5s steps(46,end) var(--d) forwards;}
.boot .bl.ok{color:var(--gold);text-shadow:2px 0 rgba(255,42,109,.8),-2px 0 rgba(0,240,255,.8);font-size:1.3em;font-weight:700;margin-top:.7em;}
.boot::after{content:"";position:absolute;left:0;right:0;top:50%;height:3px;margin-top:-1px;background:#fff;
  box-shadow:0 0 22px 4px var(--cyan),0 0 50px 10px rgba(0,240,255,.5);opacity:0;}
.boot.boot-out{animation:bootExit .85s cubic-bezier(.7,0,.3,1) forwards;pointer-events:none;}
.boot.boot-out::after{animation:bootLine .85s ease forwards;}
.boot.boot-out .boot-go{animation:goFlash .3s ease forwards;opacity:1;}
@keyframes goFlash{0%{background:var(--gold);color:#05060d;box-shadow:0 0 0 rgba(252,238,10,0)}50%{background:#fff;color:#05060d;box-shadow:0 0 40px 10px rgba(252,238,10,.9);transform:scale(1.07)}100%{background:var(--gold);color:#05060d;transform:scale(1)}}
@keyframes bootExit{
  0%{transform:none;filter:none;opacity:1}
  14%{transform:translateX(-10px) skewX(4deg);filter:hue-rotate(60deg) saturate(2)}
  28%{transform:translateX(12px) skewX(-3deg);filter:hue-rotate(-50deg)}
  40%{transform:none;filter:none;opacity:1}
  72%{transform:scaleY(.006);filter:brightness(2.2);opacity:1}
  90%{transform:scaleY(.006) scaleX(.04);opacity:1}
  100%{transform:scaleY(.006) scaleX(0);opacity:0;visibility:hidden}
}
@keyframes bootLine{0%,40%{opacity:0}72%{opacity:1}100%{opacity:0}}
.boot .boot-go{opacity:0;margin-top:24px;text-align:center;color:var(--gold);border:2px solid var(--gold);padding:10px 18px;
  font-weight:700;letter-spacing:.3em;font-size:1.05em;padding:.8em 1em;animation:bootOn 0s 2.5s forwards, goPulse 1.3s ease-in-out 2.5s infinite;}
.boot .boot-go{cursor:pointer;}
.boot .boot-go:hover{background:var(--gold);color:#05060d;}
.boot .boot-hint{opacity:0;margin-top:.9em;text-align:center;color:var(--muted);font-size:.72em;letter-spacing:1px;animation:bootOn 0s 2.7s forwards;}
@keyframes goPulse{0%,100%{box-shadow:0 0 4px rgba(252,238,10,.35)}50%{box-shadow:0 0 18px rgba(0,240,255,.85)}}
@keyframes bootOn{to{opacity:1}}
@keyframes bootType{to{width:100%}}
@keyframes bootOut{to{opacity:0;visibility:hidden}}

div[data-testid="stElementContainer"]:has(.boot), div[data-testid="element-container"]:has(.boot),
div[data-testid="stElementContainer"]:has(iframe[height="0"]), div[data-testid="element-container"]:has(iframe[height="0"]){
  position:absolute !important;height:0 !important;margin:0 !important;overflow:visible !important;
}

/* ---------- ตัวเลขราคากะพริบเมื่อเปลี่ยน ---------- */
.qs-up{animation:qsUp 1.1s ease-out;}
.qs-down{animation:qsDown 1.1s ease-out;}
@keyframes qsUp{0%{color:#fff;text-shadow:0 0 20px #19f5a5,0 0 6px #19f5a5;background:rgba(25,245,165,.22);}100%{background:transparent;text-shadow:none;}}
@keyframes qsDown{0%{color:#fff;text-shadow:0 0 20px #ff2a6d,0 0 6px #ff2a6d;background:rgba(255,42,109,.22);}100%{background:transparent;text-shadow:none;}}

/* ---------- แถบสถานะล่างจอ (HUD) ---------- */
.hud{position:fixed;left:0;right:0;bottom:0;height:28px;z-index:9990;display:flex;align-items:center;gap:22px;padding:0 16px;
  background:rgba(5,6,13,.94);border-top:1px solid var(--cyan);box-shadow:0 -6px 24px rgba(0,240,255,.08);
  font-family:var(--mono);font-size:11.5px;letter-spacing:1px;color:var(--muted);white-space:nowrap;overflow:hidden;}
.hud b{color:#fff;font-weight:400;}
.hud .st{display:inline-flex;align-items:center;gap:7px;color:var(--c,#fcee0a);}
.hud .st i{width:7px;height:7px;background:var(--c,#fcee0a);box-shadow:0 0 9px var(--c,#fcee0a);animation:pulse 1.6s infinite;}
.hud .sp{flex:1;}
.hud .u{color:var(--up);}.hud .d{color:var(--down);}
.hud .tag{color:var(--cyan);}
.hud .fs,.hud .sfx{cursor:pointer;color:var(--cyan);border:1px solid rgba(0,240,255,.35);padding:0 9px;margin-left:4px;letter-spacing:1.5px;font-size:10.5px;line-height:18px;user-select:none;}
.hud .fs:hover,.hud .sfx:hover{background:var(--cyan);color:#05060d;}
.hud .sfx.off{color:var(--muted);border-color:rgba(125,134,166,.35);}
.block-container{padding-bottom:3.2rem !important;}
section[data-testid="stSidebar"] > div{padding-bottom:34px;}
@media (max-width:760px){.hud .hide-sm{display:none;}}
@media (prefers-reduced-motion:reduce){.boot{display:none;} .qs-up,.qs-down{animation:none !important;}}
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
    boot_once()


def _mark(kind: str = "brand") -> str:
    """โลโก้ใหม่ (รูป) — ถ้าไม่มีไฟล์ logo_asset.py จะกลับไปใช้สัญลักษณ์ ◆ เดิม"""
    try:
        if _logo is not None:
            cls = "hero-logo" if kind == "hero" else "brand-logo"
            return f'<img class="{cls}" alt="Quant Stock Analyzer" src="data:image/png;base64,{_logo.LOGO_SM}">'
    except Exception:
        pass
    return '<div class="hero-mark">◆</div>' if kind == "hero" else '<div class="brand-mark">◆</div>'


def hero(title: str, subtitle: str = "", pill: str = "LIVE"):
    pill_html = f'<div class="hero-pill">● {pill}</div>' if pill else ""
    st.markdown(_html(f"""
        <div class="hero">
        {_mark('hero')}
        <div><div class="hero-title">{title}</div><div class="hero-sub">{subtitle}</div></div>
        {pill_html}
        </div>
    """), unsafe_allow_html=True)


BOOT_HTML = """
<div class="boot">__BOOTLOGO__<i class="boot-c c-tl"></i><i class="boot-c c-tr"></i><i class="boot-c c-bl"></i><i class="boot-c c-br"></i>
<div class="boot-top"><span>QUANT STOCK ANALYZER // SYSTEM BOOT</span><span>v2077</span></div>
<div class="boot-bot"><span>SECURE LINK ESTABLISHED</span><span>NIGHT CITY MARKET FEED</span></div>
<div class="boot-in">
<div class="bl" style="--d:.15s">&gt; BOOT SEQUENCE ................ OK</div>
<div class="bl" style="--d:.65s">&gt; LINKING NIGHT CITY MARKET FEED ... OK</div>
<div class="bl" style="--d:1.15s">&gt; LOADING QUANT CORE v2077 ........ OK</div>
<div class="bl" style="--d:1.65s">&gt; SYNCING NEURAL SCANNER .......... OK</div>
<div class="bl ok" style="--d:2.05s">&gt; ACCESS GRANTED</div>
<div class="boot-go">[ ▶ ENTER NIGHT CITY ]</div>
<div class="boot-hint">กดปุ่มด้านบน หรือกดแป้น Enter เพื่อเข้าสู่ระบบ (เข้าโหมดเต็มจอให้อัตโนมัติ)</div>
</div></div>
"""


def boot_once():
    """หน้าบูตแบบเทอร์มินัล: แสดงครั้งเดียวต่อเซสชัน แล้วจางหายเอง"""
    try:
        if not st.session_state.get("_qs_booted"):
            st.session_state["_qs_booted"] = True
            _b = BOOT_HTML
            try:
                _b = _b.replace("__BOOTLOGO__", f'<img class="boot-logo" alt="" src="data:image/png;base64,{_logo.LOGO_LG}">' if _logo else "")
            except Exception:
                _b = _b.replace("__BOOTLOGO__", "")
            st.markdown(_b, unsafe_allow_html=True)
    except Exception:
        pass


# ---------- เสียงเอฟเฟกต์ (สังเคราะห์ด้วย WebAudio ไม่ต้องมีไฟล์เสียง) ----------
# รันที่หน้าต่างหลัก (P.eval) เพื่อให้อยู่ต่อเนื่องแม้ Streamlit รีโหลดหน้า
SFX_CODE = r"""(function(){
  if(window.__qsSfx && window.__qsSfx.v===19) return;
  var A=window.__qsSfx={v:19,c:null,m:null,on:true,unlocked:false,lt:{},hov:null,trim:{hover:10,click:3.3,nav:.8,boot:4.5,on:2.6,off:.78}};
  try{ A.on = window.localStorage.getItem('qs_sfx')!=='0'; }catch(e){}
  function ctx(){
    if(!A.c){ var C=window.AudioContext||window.webkitAudioContext; if(!C) return null;
      try{ A.c=new C(); A.m=A.c.createGain(); A.m.gain.value=1;
        var lim=A.c.createDynamicsCompressor(); lim.threshold.value=-14; lim.knee.value=6; lim.ratio.value=12; lim.attack.value=.002; lim.release.value=.15;   // กันเสียงแตก/ดังเกิน
        A.m.connect(lim); lim.connect(A.c.destination); }catch(e){ A.c=null; return null; } }
    if(A.c.state==='suspended'){ try{ A.c.resume(); }catch(e){} }
    return A.c;
  }
  // บัสเสียง "ดิจิทัลหยาบ" (ลดระดับสัญญาณเป็นขั้นๆ ให้ได้กลิ่นไซเบอร์แวร์/เสียงจอ HUD)
  function dirty(){
    if(A.d) return A.d; var c=A.c; if(!c) return A.m;
    try{ var w=c.createWaveShaper(), n=1024, cu=new Float32Array(n), q=14;
      for(var i=0;i<n;i++){ var x=i/(n-1)*2-1; cu[i]=Math.round(x*q)/q; }
      var gi=c.createGain(), go=c.createGain(); gi.gain.value=10; go.gain.value=.1;   // ขยายก่อนแล้วลดหลังตัดเป็นขั้น (ไม่งั้นเสียงเบาจะถูกปัดเป็นศูนย์)
      w.curve=cu; gi.connect(w); w.connect(go); go.connect(A.m); A.d=gi; }catch(e){ A.d=A.m; }
    return A.d;
  }
  // เสียงก้องในห้องใหญ่ (รีเวิร์บสังเคราะห์จากนอยส์ที่ค่อยๆ จาง) ให้ได้ความรู้สึกหนังไซไฟ
  function rev(){
    if(A.r) return A.r; var c=A.c; if(!c) return A.m;
    try{ var n=Math.floor(c.sampleRate*1.5), buf=c.createBuffer(2,n,c.sampleRate);
      for(var ch=0;ch<2;ch++){ var d=buf.getChannelData(ch); for(var i=0;i<n;i++) d[i]=(Math.random()*2-1)*Math.pow(1-i/n,2.6); }
      var cv=c.createConvolver(); cv.buffer=buf; var og=c.createGain(); og.gain.value=.8; cv.connect(og); og.connect(A.m); A.r=cv; }catch(e){ A.r=A.m; }
    return A.r;
  }
  function out(g,grit,wet){
    g.connect(grit?dirty():A.m);
    if(wet){ var w=A.c.createGain(); w.gain.value=wet; g.connect(w); w.connect(rev()); }
  }
  // โทน: cut = ตัดความถี่สูงออก (ให้ทุ้มหนัก ไม่แหลมแบบการ์ตูน), wet = ปริมาณเสียงก้อง
  function tone(f1,f2,d,type,vol,delay,grit,cut,wet){
    var c=ctx(); if(!c) return; var t=c.currentTime+(delay||0);
    vol*=(A.t||1); var o=c.createOscillator(), g=c.createGain(), nd=o; o.type=type||'square';
    o.frequency.setValueAtTime(f1,t); if(f2&&f2!==f1) o.frequency.exponentialRampToValueAtTime(f2,t+d);
    g.gain.setValueAtTime(0.0001,t); g.gain.linearRampToValueAtTime(vol,t+.006); g.gain.exponentialRampToValueAtTime(.0001,t+d);
    if(cut){ var lp=c.createBiquadFilter(); lp.type='lowpass'; lp.frequency.value=cut; o.connect(lp); nd=lp; }
    nd.connect(g); out(g,grit,wet); o.start(t); o.stop(t+d+.03);
  }
  // นอยส์ผ่านฟิลเตอร์ที่กวาดความถี่ — type: bandpass/lowpass/highpass, rise = ค่อยๆ ดังขึ้น (เหมือนหายใจเข้าก่อนระเบิด)
  function noise(d,f1,f2,vol,delay,type,rise,wet){
    var c=ctx(); if(!c) return; vol*=(A.t||1); var t=c.currentTime+(delay||0), n=Math.floor(c.sampleRate*d);
    var buf=c.createBuffer(1,n,c.sampleRate), da=buf.getChannelData(0); for(var i=0;i<n;i++) da[i]=Math.random()*2-1;
    var s=c.createBufferSource(); s.buffer=buf; var f=c.createBiquadFilter(); f.type=type||'bandpass'; f.Q.value=(f.type==='bandpass')?2.5:.8;
    f.frequency.setValueAtTime(f1,t); f.frequency.exponentialRampToValueAtTime(f2,t+d);
    var g=c.createGain();
    if(rise){ g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(vol,t+d*.95); g.gain.linearRampToValueAtTime(0,t+d); }
    else{ g.gain.setValueAtTime(vol,t); g.gain.exponentialRampToValueAtTime(.0001,t+d); }
    s.connect(f); f.connect(g); out(g,false,wet); s.start(t);
  }
  // ธีม Cyberpunk: Edgerunners — โทนมืด หนัก ทุ้ม เหมือนฉากหนังไซไฟ (ไม่มีโน้ตดนตรี/เสียงกระดิ่ง) สังเคราะห์เองทั้งหมด ไม่ได้ใช้เสียงจากเรื่อง
  // ซินธ์เบสกระแทก (ซอว์ 2 ตัวเพี้ยนเล็กน้อย + ฟิลเตอร์ที่ปิดลง) สไตล์ซินธ์เวฟ
  function stab(f,d,vol,delay,c1,c2,wet){
    var c=ctx(); if(!c) return; var t=c.currentTime+(delay||0); vol*=(A.t||1);
    var lp=c.createBiquadFilter(); lp.type='lowpass'; lp.Q.value=4; lp.frequency.setValueAtTime(c1,t); lp.frequency.exponentialRampToValueAtTime(c2,t+d);
    var g=c.createGain(); g.gain.setValueAtTime(0.0001,t); g.gain.linearRampToValueAtTime(vol,t+.01); g.gain.exponentialRampToValueAtTime(.0001,t+d);
    [f*0.994,f*1.006].forEach(function(ff){ var o=c.createOscillator(); o.type='sawtooth'; o.frequency.value=ff; o.connect(lp); o.start(t); o.stop(t+d+.03); });
    lp.connect(g); out(g,true,wet);
  }
  // ซอว์ไต่ความถี่ขึ้นพร้อมฟิลเตอร์เปิด (ไรเซอร์ซินธ์)
  function riser(f1,f2,c1,c2,d,vol,delay,wet){
    var c=ctx(); if(!c) return; var t=c.currentTime+(delay||0); vol*=(A.t||1);
    var o=c.createOscillator(), lp=c.createBiquadFilter(), g=c.createGain(); o.type='sawtooth';
    o.frequency.setValueAtTime(f1,t); o.frequency.exponentialRampToValueAtTime(f2,t+d);
    lp.type='lowpass'; lp.Q.value=3; lp.frequency.setValueAtTime(c1,t); lp.frequency.exponentialRampToValueAtTime(c2,t+d);
    g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(vol,t+d*.9); g.gain.linearRampToValueAtTime(0,t+d);
    o.connect(lp); lp.connect(g); out(g,false,wet); o.start(t); o.stop(t+d+.03);
  }
  // นอยส์กลิตช์สั้นๆ: ตัดเป็นช่วง สุ่มเปิด/ปิด (เสียงสัญญาณฉีก)
  function gnoise(d,vol,delay,seg,lp,wet,hmax){
    var c=ctx(); if(!c) return; vol*=(A.t||1); var t=c.currentTime+(delay||0), sr=c.sampleRate, n=Math.floor(sr*d);
    var buf=c.createBuffer(1,n,sr), da=buf.getChannelData(0), i=0;
    while(i<n){ var L=Math.max(40,Math.floor(sr*seg*(.4+Math.random()*1.2))), on=Math.random()>.3, hold=1+Math.floor(Math.random()*(hmax||6)), v=0;
      for(var k=0;k<L&&i<n;k++,i++){ if(k%hold===0) v=Math.random()*2-1; da[i]=on?v:0; } }
    var s=c.createBufferSource(); s.buffer=buf; var f=c.createBiquadFilter(); f.type='lowpass'; f.frequency.value=lp||3200;
    var g=c.createGain(); g.gain.setValueAtTime(vol,t); g.gain.setValueAtTime(vol,t+d*.8); g.gain.linearRampToValueAtTime(0,t+d);
    s.connect(f); f.connect(g); out(g,false,wet); s.start(t);
  }
  var SND={
    // ชี้เมนู: คลิกจางๆ ของสวิตช์
    hover:function(){ noise(.018,3800,3000,.02,0,'bandpass'); },
    // คลิก: สวิตช์โลหะ "กด-ปล่อย" โทนทึบ — คลิกแห้งต่ำกว่าตอนชี้ + ตุบทุ้มสั้น + ติ๊กดิจิทัลทึบๆ + คลิกปล่อยเบาๆ (ไม่แหลม ไม่ใส)
    click:function(){
      noise(.03,1900,1000,.07,0,'bandpass');
      tone(110,42,.14,'sine',.11,.006);
      tone(420,260,.06,'square',.010,.02,true,900);
      noise(.014,1500,900,.03,.09,'bandpass');
    },
    // เปลี่ยนหน้า: ซานเดวิสตัน — สูดลมเข้า แล้วระเบิดเบสลึก + ลมกระชาก + ก้องลอยหาย
    nav:function(){
      noise(.15,260,2800,.06,0,'bandpass',true);
      tone(125,32,.55,'sine',.12,.15,false,0,.25);
      noise(.5,2400,90,.07,.15,'lowpass',false,.35);
      tone(58,50,.5,'sawtooth',.025,.15,true,240);
      tone(4600,4300,.45,'sine',.004,.17,false,0,.4);
    },
    // เข้าระบบ: เสียงบูตแบบเดิมจากไฟล์ theme_.py ที่ผู้ใช้เลือก (เบสไต่ขึ้น + ลม + โน้ตสามตัวไต่ขึ้น)
    boot:function(){ tone(70,420,.7,'sawtooth',.05); noise(.55,200,4200,.06); tone(440,440,.18,'square',.03,.45); tone(660,660,.18,'square',.03,.58); tone(880,880,.32,'square',.035,.71); },
    // เปิด: รีเลย์ปิดวงจร + พลังไต่ขึ้น
    on:function(){ tone(170,85,.06,'square',.05,0,true,700); tone(110,520,.24,'sawtooth',.03,.06,false,1500); noise(.2,500,3200,.03,.06,'bandpass',true); },
    // ปิด: พลังตกลง + ตุบ
    off:function(){ tone(520,95,.32,'sawtooth',.035,0,false,1300); tone(110,45,.22,'sine',.09,.18); }
  };
  // ไฟล์เสียงบูตของผู้ใช้: ถ้ามี static/boot_sfx.mp3 (หรือ .wav/.ogg) จะเล่นไฟล์นั้นแทนเสียงสังเคราะห์ ถ้าไม่มี/เล่นไม่ได้ จะใช้เสียงสังเคราะห์เดิม
  A.bootGain=2.5;   // ความดังเสียงบูตจากไฟล์ของคุณ (1 = เท่าต้นฉบับ, 2.5 = ดังขึ้นราว 8 dB)
  A.bootSkip=.4;   // ข้ามช่วงต้นไฟล์กี่วินาที (ยิ่งมาก เสียงกระแทกยิ่งมาเร็วเมื่อเทียบกับภาพ) — ปรับเลขนี้ได้
  var BF=['boot_sfx.mp3','boot_sfx.wav','boot_sfx.ogg'], BP=['app/static/','/app/static/','/~/+/app/static/'], BL=[];
  BF.forEach(function(f){ BP.forEach(function(p){ var h; try{ h=new URL(p+f,document.baseURI).href; }catch(e){ h=p+f; } if(BL.indexOf(h)<0) BL.push(h); }); });
  function loadBoot(i){
    if(i>=BL.length){ A.bau=null; return; }
    var a=new Audio(); a.preload='auto'; a.volume=.9;
    a.oncanplaythrough=function(){ a.oncanplaythrough=null; a.onerror=null; A.bau=a; };
    a.onerror=function(){ a.oncanplaythrough=null; a.onerror=null; loadBoot(i+1); };
    try{ a.src=BL[i]; }catch(e){ loadBoot(i+1); }
  }
  loadBoot(0);
  // ถอดรหัสไฟล์ไว้ในหน่วยความจำล่วงหน้า → กด ENTER แล้วเสียงออกทันที (แม่นกว่าและไวกว่าเล่นผ่าน <audio>) เริ่มจากจุด A.bootSkip
  function loadBuf(i){
    if(i>=BL.length) return;
    try{
      fetch(BL[i]).then(function(r){ if(!r.ok) throw 0; return r.arrayBuffer(); })
        .then(function(ab){ var c=ctx(); if(!c) throw 0; return new Promise(function(res,rej){ c.decodeAudioData(ab,res,rej); }); })
        .then(function(b){ A.bbuf=b; })
        .catch(function(){ loadBuf(i+1); });
    }catch(e){ loadBuf(i+1); }
  }
  loadBuf(0);
  A.play=function(k,force){
    if(!A.on && !force) return;
    if(k==='boot' && A.bbuf && A.c){
      try{ var c0=ctx(), sb=c0.createBufferSource(), gb=c0.createGain(); sb.buffer=A.bbuf; gb.gain.value=(A.bootGain||2.5);   // ขยายเสียงไฟล์บูต (ปรับ A.bootGain: 1 = เท่าต้นฉบับ) + ลิมิตเตอร์กันแตก
           var lm=c0.createDynamicsCompressor(); lm.threshold.value=-3; lm.knee.value=0; lm.ratio.value=20; lm.attack.value=.001; lm.release.value=.12;
           sb.connect(gb); gb.connect(lm); lm.connect(c0.destination);
           sb.start(0,Math.max(0,Math.min(A.bootSkip||0,A.bbuf.duration-.3))); return; }catch(e){}
    }
    if(k==='boot' && A.bau){
      try{ A.bau.currentTime=Math.max(0,Math.min(A.bootSkip||0,(A.bau.duration||1)-.3)); var pp=A.bau.play(); if(pp&&pp.catch) pp.catch(function(){ try{ A.t=(A.trim&&A.trim.boot)||1; SND.boot(); }catch(e){} }); return; }catch(e){}
    }
    var now=Date.now(), key=(k==='hover')?'h':'a', gap=(k==='hover')?110:(k==='boot'?0:45);
    if(now-(A.lt[key]||0)<gap) return; A.lt[key]=now;
    A.t=(A.trim&&A.trim[k])||1; try{ SND[k](); }catch(e){ A.err=e; try{console.error("sfx",e);}catch(x){} }
  };
  function paint(){
    try{ var q=document.querySelectorAll('.hud .sfx'); for(var i=0;i<q.length;i++){ q[i].className='sfx'+(A.on?'':' off'); q[i].textContent='♪ SFX '+(A.on?'ON':'OFF'); } }catch(e){}
  }
  A.set=function(x){ A.on=!!x; try{ window.localStorage.setItem('qs_sfx',A.on?'1':'0'); }catch(e){} paint(); if(A.on) A.play('on',true); else { A.on=true; A.play('off',true); A.on=false; } };
  // พร้อมเล่นเสียงบูตเมื่อ: ปุ่ม ENTER ขึ้นมาแล้ว และยังไม่เคยเล่นรอบนี้ (ไม่ดูคลาส boot-out เพราะตัวจัดการเข้าระบบอาจใส่คลาสนั้นไปก่อนแล้ว)
  function bootReady(){
    if(document.querySelector('.boot:not(.boot-out)')) A.bootDone=false;
    if(A.bootDone) return false;
    var g=document.querySelector('.boot .boot-go'); if(!g) return false;
    var o=1; try{ o=parseFloat(getComputedStyle(g).opacity); }catch(e){}
    return o>=.5;
  }
  function unlock(){ if(!A.unlocked){ A.unlocked=true; ctx(); } }
  var NAV='[data-testid="stSidebar"] [role="radiogroup"] label, [data-testid="stSidebar"] [data-baseweb="radio"]';
  var BTN='button, [role="tab"], [role="radio"], [data-baseweb="select"], summary, .qs-fs-btn, .hud .fs, a[href]';
  try{ ['click','pointerdown','keydown','mouseover'].forEach(function(e){ document.removeEventListener(e,window.__qsSfxH,true); }); }catch(e){}
  window.__qsSfxH=function(e){
    try{
      var t=e.target; if(!t||!t.closest) return;
      if(e.type==='pointerdown'){ unlock(); return; }
      if(e.type==='keydown'){ unlock(); if(e.key==='Enter' && bootReady()){ A.bootDone=true; A.play('boot'); } return; }
      if(e.type==='mouseover'){
        if(!A.unlocked) return;
        var h=t.closest(NAV+', '+BTN);   // เสียงตอนชี้: ดังทั้งแถบซ้ายและหน้าหลัก (คลิกไม่มีเสียง)
        if(h && h!==A.hov){ A.hov=h; if(!t.closest('.boot')) A.play('hover'); } else if(!h){ A.hov=null; }
        return;
      }
      // click
      var s=t.closest('.hud .sfx'); if(s){ unlock(); A.set(!A.on); return; }
      if(t.closest('.boot-go')){ unlock(); if(bootReady()){ A.bootDone=true; A.play('boot'); } return; }
      // คลิกทั่วไป/คลิกเมนู: ไม่มีเสียง (ยังเหลือเฉพาะเสียงบูตกับเสียงเปิด-ปิด SFX ด้านบน)
    }catch(x){}
  };
  ['click','pointerdown','keydown','mouseover'].forEach(function(e){ document.addEventListener(e,window.__qsSfxH,true); });
})();"""


HUD_JS = r"""<!doctype html><html><body><script>
(function(){
  var P, D;
  try{ P=window.parent; D=P.document; }catch(e){ return; }
  try{ if(!P.__qsSfx || P.__qsSfx.v!==19) P.eval(__SFX__); }catch(e){}
  var DATA=__DATA__;
  function esc(x){return String(x).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  // ---- HUD ล่างจอ ----
  var h=D.getElementById('qs-hud');
  if(!h){ h=D.createElement('div'); h.id='qs-hud'; h.className='hud'; D.body.appendChild(h); }
  function tm(tz){ try{return new Intl.DateTimeFormat('en-GB',{timeZone:tz,hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}).format(new Date());}catch(e){return '--:--:--';} }
  function mkt(){
    try{
      var p=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'short',hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date());
      var g={}; p.forEach(function(x){g[x.type]=x.value;});
      var m=(parseInt(g.hour,10)%24)*60+parseInt(g.minute,10), wd=g.weekday;
      if(wd==='Sat'||wd==='Sun') return ['#ff2a6d','US MARKET CLOSED // WEEKEND'];
      if(m>=570&&m<960) return ['#19f5a5','US MARKET OPEN'];
      if(m>=240&&m<570) return ['#fcee0a','PRE-MARKET'];
      if(m>=960&&m<1200) return ['#fcee0a','AFTER-HOURS'];
      return ['#ff2a6d','US MARKET CLOSED'];
    }catch(e){return ['#7d86a6','MARKET'];}
  }
  function render(){
    var s=mkt(), t='', sfxOn=!(P.__qsSfx && P.__qsSfx.on===false);
    DATA.slice(0,4).forEach(function(x){
      if(x[1]==null) return;
      var up=x[2]>=0;
      t+='<span class="hide-sm"><b>'+esc(x[0])+'</b> '+Number(x[1]).toLocaleString('en-US',{maximumFractionDigits:2})+' <span class="'+(up?'u':'d')+'">'+(up?'▲':'▼')+Math.abs(x[2]).toFixed(2)+'%</span></span>';
    });
    h.innerHTML='<span class="st" style="--c:'+s[0]+'"><i></i>'+s[1]+'</span>'
      +'<span class="hide-sm"><span class="tag">BKK</span> <b>'+tm('Asia/Bangkok')+'</b> &nbsp;<span class="tag">NYC</span> <b>'+tm('America/New_York')+'</b></span>'
      +'<span class="sp"></span>'+t+'<span class="sfx'+(sfxOn?'':' off')+'" title="เปิด/ปิดเสียงเอฟเฟกต์ (คลิกเมนู เปลี่ยนหน้า)">♪ SFX '+(sfxOn?'ON':'OFF')+'</span><span class="fs" title="เข้า/ออกโหมดเต็มจอ (เหมือนกด F11)">⛶ FULLSCREEN</span>';
  }
  if(!h.__fs){ h.__fs=1; h.addEventListener('click',function(e){
    if(!(e.target.closest&&e.target.closest('.fs'))) return;
    try{ var de=D.documentElement;
      if(D.fullscreenElement||D.webkitFullscreenElement){ (D.exitFullscreen||D.webkitExitFullscreen).call(D); }
      else{ var rf=de.requestFullscreen||de.webkitRequestFullscreen; if(rf){ var pr=rf.call(de); if(pr&&pr.catch) pr.catch(function(){}); } }
    }catch(x){}
  }); }
  try{ if(P.__qsHud) P.clearInterval(P.__qsHud); }catch(e){}
  render(); P.__qsHud=P.setInterval(function(){ try{render();}catch(e){} },1000);

  // ---- ตัวเลขราคากะพริบเมื่อเปลี่ยน ----
  function num(el){ return parseFloat((el.textContent||'').replace(/[^0-9.\-]/g,'')); }
  function seed(){ D.querySelectorAll('[data-testid="stMetricValue"]').forEach(function(el){ if(el.__qv==null) el.__qv=num(el); }); }
  seed();
  try{ if(P.__qsObs) P.__qsObs.disconnect(); }catch(e){}
  var obs=new P.MutationObserver(function(ms){
    ms.forEach(function(m){
      var el=m.target.nodeType===3?m.target.parentElement:m.target;
      if(!el||!el.closest) return;
      var mv=el.closest('[data-testid="stMetricValue"]'); if(!mv) return;
      var n=num(mv), old=mv.__qv; mv.__qv=n;
      if(old!=null && !isNaN(n) && !isNaN(old) && n!==old){
        mv.classList.remove('qs-up','qs-down'); void mv.offsetWidth; mv.classList.add(n>old?'qs-up':'qs-down');
        P.setTimeout(function(){ mv.classList.remove('qs-up','qs-down'); },1200);
      }
    });
    seed();
  });
  obs.observe(D.body,{subtree:true,childList:true,characterData:true});
  P.__qsObs=obs;
})();
</script></body></html>"""


def hud(markets: dict = None):
    """แถบสถานะล่างจอ (นาฬิกาไทย/นิวยอร์ก, สถานะตลาด, ดัชนีหลัก) + ตัวเลขราคากะพริบเมื่อเปลี่ยน"""
    try:
        import json
        import streamlit.components.v1 as components
        data = []
        for name, v in (markets or {}).items():
            data.append([name, (float(v[0]) if v else None), (float(v[1]) if v else 0.0)])
        components.html(HUD_JS.replace("__SFX__", json.dumps(SFX_CODE)).replace("__DATA__", json.dumps(data, ensure_ascii=False)), height=0)
    except Exception:
        pass



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


MUSIC_HTML = r"""<!doctype html><html><head><meta charset="utf-8">
<style>
  html,body{margin:0;background:transparent;font-family:'Chakra Petch','IBM Plex Sans Thai',system-ui,sans-serif;color:#e6f1ff;}
  .box{position:relative;overflow:hidden;border:1px solid rgba(0,240,255,.2);border-left:3px solid #fcee0a;background:rgba(12,14,28,.78);padding:9px 11px 10px;transition:border-color .4s,box-shadow .4s;}
  .box.play{animation:glow 2.6s ease-in-out infinite alternate;border-color:rgba(0,240,255,.34);border-left-color:#fcee0a;}
  .box.play::after{content:"";position:absolute;top:0;bottom:0;width:46px;left:-70px;background:linear-gradient(90deg,transparent,rgba(0,240,255,.09),transparent);animation:sweep 16s linear infinite;pointer-events:none;}
  @keyframes glow{from{box-shadow:inset 0 0 8px rgba(0,240,255,.05),0 0 3px rgba(252,238,10,.04);}to{box-shadow:inset 0 0 18px rgba(0,240,255,.15),0 0 11px rgba(252,238,10,.16);}}
  @keyframes sweep{0%{left:-70px;}25%{left:112%;}100%{left:112%;}}
  .t{font-size:10px;letter-spacing:2.2px;color:#00f0ff;display:flex;justify-content:space-between;align-items:center;}
  .t .live{display:flex;align-items:center;gap:5px;color:#7d86a6;letter-spacing:1.6px;font-size:9px;}
  .t .live i{display:block;width:6px;height:6px;border-radius:50%;background:#3a3f55;transition:background .3s;}
  .box.play .t .live{color:#ff2a6d;} .box.play .t .live i{background:#ff2a6d;animation:dot 1.3s ease-in-out infinite;}
  @keyframes dot{0%,100%{opacity:1;box-shadow:0 0 6px #ff2a6d;}50%{opacity:.35;box-shadow:none;}}
  .n{font-size:12.5px;font-weight:600;margin:4px 0 6px;letter-spacing:.3px;white-space:nowrap;overflow:hidden;}
  .n span{display:inline-block;will-change:transform;}
  .n span.mq{animation:mq var(--dur,9s) ease-in-out infinite alternate;}
  @keyframes mq{0%,12%{transform:translateX(0)}88%,100%{transform:translateX(var(--sh,0))}}
  .n.err{color:#ff2a6d;white-space:normal;font-size:11.5px;line-height:1.3;}
  canvas{display:block;width:100%;height:18px;margin:0 0 5px;opacity:.8;}
  .meta{display:flex;justify-content:space-between;font-size:9.5px;letter-spacing:1.4px;color:#7d86a6;font-variant-numeric:tabular-nums;}
  .pg{position:relative;height:4px;margin:4px 0 9px;background:#232638;cursor:pointer;}
  .pg::before{content:"";position:absolute;left:0;right:0;top:-6px;bottom:-6px;}
  .pg i{display:block;height:100%;width:0;background:linear-gradient(90deg,#00f0ff,#fcee0a);box-shadow:0 0 6px rgba(0,240,255,.5);transition:width .25s linear;}
  .row{display:flex;align-items:center;gap:7px;}
  button{background:#fcee0a;color:#05060d;border:0;font:700 12px 'Chakra Petch',sans-serif;letter-spacing:1px;padding:6px 12px;cursor:pointer;
    clip-path:polygon(0 0,calc(100% - 7px) 0,100% 7px,100% 100%,7px 100%,0 calc(100% - 7px));min-width:72px;transition:background .2s,transform .2s;}
  button.sm{min-width:30px;padding:6px 7px;}
  button:hover{background:#00f0ff;animation:sh .42s ease-in-out 1;} button.on{background:#ff2a6d;color:#fff;} button.on:hover{background:#ff5c8f;}
  @keyframes sh{0%{transform:translate(0,0)}18%{transform:translate(-2px,0)}38%{transform:translate(1.6px,0)}58%{transform:translate(-1px,0)}78%{transform:translate(.6px,0)}100%{transform:translate(0,0)}}
  input[type=range]{flex:1;min-width:44px;height:16px;margin:0;background:transparent;cursor:pointer;-webkit-appearance:none;appearance:none;}
  input[type=range]::-webkit-slider-runnable-track{height:4px;background:linear-gradient(90deg,#fcee0a var(--f,35%),#2a2d40 var(--f,35%));}
  input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:9px;height:15px;margin-top:-5.5px;background:#fcee0a;border:0;border-radius:0;box-shadow:0 0 7px rgba(252,238,10,.7);transition:transform .15s;}
  input[type=range]:hover::-webkit-slider-thumb{transform:scaleY(1.12);}
  input[type=range]::-moz-range-track{height:4px;background:#2a2d40;} input[type=range]::-moz-range-progress{height:4px;background:#fcee0a;}
  input[type=range]::-moz-range-thumb{width:9px;height:15px;background:#fcee0a;border:0;border-radius:0;}
</style></head><body>
<div class="box" id="bx">
  <div class="t"><span>NIGHT CITY FM</span><span class="live"><i></i><span id="lv">OFF AIR</span></span></div>
  <div class="n" id="nm"><span id="ni">—</span></div>
  <canvas id="cv"></canvas>
  <div class="meta"><span id="tk">TRACK 01/03</span><span id="tm">0:00 / 0:00</span></div>
  <div class="pg" id="pg" title="กดเพื่อเลื่อนตำแหน่งเพลง"><i id="pf"></i></div>
  <div class="row"><button id="pv" class="sm" title="เพลงก่อนหน้า">⏮</button><button id="b">▶ PLAY</button><button id="nx" class="sm" title="เพลงถัดไป">⏭</button><input id="v" type="range" min="0" max="100" value="35" title="ระดับเสียง"></div>
</div>
<script>
(function(){
  var P=null; try{ P=window.parent; void P.document; }catch(e){ P=null; }
  var b=document.getElementById('b'), v=document.getElementById('v'), nm=document.getElementById('nm'), ni=document.getElementById('ni'), nx=document.getElementById('nx'), pv=document.getElementById('pv'),
      box=document.getElementById('bx'), cv=document.getElementById('cv'), tk=document.getElementById('tk'), tm=document.getElementById('tm'), pg=document.getElementById('pg'), pf=document.getElementById('pf'), lv=document.getElementById('lv');

  // ตัวเล่นเพลงอยู่ที่หน้าต่างหลัก (ไม่ใช่ใน iframe) เพื่อให้เพลงเล่นต่อเนื่อง ไม่เริ่มใหม่เวลา Streamlit รีโหลดหน้า
  var CODE = "(" + function(){
    if(window.__qs && window.__qs.v===10) return;
    var T=[
      {n:'Let You Down', f:'bgm_2.mp3'},
      {n:'wiv — i love u (slowed + reverb)', f:'bgm_1.mp3'},
      {n:'I Really Want to Stay at Your House (Epic Cover)', f:'bgm_3.mp3'}
    ];
    // ลองหลายตำแหน่ง: ในเครื่อง (/app/static) และบน Streamlit Cloud ที่แอปอยู่ใต้ /~/+/
    function urls(f){ var out=[]; ['app/static/'+f,'/app/static/'+f,'/~/+/app/static/'+f].forEach(function(u){ var h; try{ h=new URL(u,document.baseURI).href; }catch(e){ h=u; } if(out.indexOf(h)<0) out.push(h); }); return out; }
    var S=window.__qs={v:10,ti:0,au:null,playing:false,err:false,vol:0.35,subs:[],tracks:T,armed:false};
    var ls=null; try{ ls=window.localStorage; }catch(e){}
    function get(k){ try{return ls&&ls.getItem(k);}catch(e){return null;} }
    function set(k,x){ try{ ls&&ls.setItem(k,x); }catch(e){} }
    var sv=get('bgm_vol'); if(sv!==null && !isNaN(parseFloat(sv))) S.vol=parseFloat(sv)/100;
    S.off = get('bgm_off')==='1';
    function vol(){ return Math.pow(S.vol,1.6); }
    S.emit=function(){ S.subs.forEach(function(f){ try{f();}catch(e){} }); };
    function drop(x){ try{ x.onended=null; x.onerror=null; x.pause(); x.removeAttribute('src'); x.load(); }catch(e){} }
    function kill(){ if(S.au){ drop(S.au); S.au=null; } }
    S.start=function(ci){
      ci=ci||0; var L=urls(T[S.ti].f); kill(); var a=new Audio(L[ci]); S.au=a; S.url=L[ci]; a.volume=vol(); a.preload='auto';
      a.onended=function(){ S.ti=(S.ti+1)%T.length; S.start(); };
      a.onerror=function(){ if(S.au!==a) return; drop(a); S.au=null; if(ci+1<L.length){ S.start(ci+1); return; } S.playing=false; S.err=true; S.tried=L.join(' | '); S.emit(); };
      var p=a.play();
      if(p && p.then){
        p.then(function(){ if(S.au===a){ S.playing=true; S.err=false; S.emit(); } })
         .catch(function(e){ if(S.au===a){ drop(a); S.au=null; S.playing=false; S.emit(); if(e && e.name==='NotAllowedError') S.arm(); } });
      }
      S.emit();
    };
    S.play=function(){ S.off=false; set('bgm_off','0'); S.err=false; S.start(); };
    S.stop=function(){ S.off=true; set('bgm_off','1'); kill(); S.playing=false; S.emit(); };
    S.next=function(){ var was=S.playing; kill(); S.playing=false; S.ti=(S.ti+1)%T.length; if(was) S.start(); else S.emit(); };
    S.setVol=function(x){ S.vol=x; set('bgm_vol',String(Math.round(x*100))); if(S.au) S.au.volume=vol(); };
    // เบราว์เซอร์บล็อกเสียงอัตโนมัติ: ถ้าเล่นเองไม่ได้ จะเริ่มเล่นตอนผู้ใช้คลิก/กดแป้นครั้งแรกที่ไหนก็ได้ในหน้า
    S.arm=function(){
      if(S.armed) return; S.armed=true;
      var evs=['pointerdown','keydown','touchstart'];
      function h(){ if(document.querySelector('.boot:not(.boot-out)')) return; evs.forEach(function(e){ document.removeEventListener(e,h,true); }); S.armed=false; if(!S.off && !S.playing && !S.au) S.play(); }
      evs.forEach(function(e){ document.addEventListener(e,h,true); });
    };
    S.auto=function(){ if(document.querySelector('.boot:not(.boot-out)')) return; if(!S.off && !S.playing && !S.au) S.start(); };
    // หน้าบูต: กดเข้าระบบ (คลิก / Enter) = ปิดหน้าบูต + เริ่มเพลงพร้อมกัน (การคลิกนี้คือสิ่งที่เบราว์เซอร์ต้องการเพื่อเปิดเสียง)
    // ปุ่ม ENTER จะค่อยๆ ขึ้นหลังบรรทัดบูตจบ (~2.5 วิ) — ก่อนหน้านั้นกดคลิก/Enter แล้วไม่เข้าเว็บ
    function bootReady(){ var g=document.querySelector('.boot:not(.boot-out) .boot-go'); if(!g) return false; try{ return parseFloat(getComputedStyle(g).opacity)>=.5; }catch(e){ return true; } }
    function enter(b){
      b.classList.add('boot-out');
      // เต็มจอแบบ F11 (เบราว์เซอร์อนุญาตเฉพาะตอนผู้ใช้กดเอง จึงทำพร้อมการกดเข้าระบบ)
      try{ var de=document.documentElement; if(!document.fullscreenElement && !document.webkitFullscreenElement){
        var rf=de.requestFullscreen||de.webkitRequestFullscreen||de.msRequestFullscreen;
        if(rf){ var pr=rf.call(de); if(pr&&pr.catch) pr.catch(function(){}); } } }catch(e){}
      S.off=false; set('bgm_off','0');            // กดเข้าระบบ = ตั้งใจเปิดเพลง (แม้เคยกด STOP ไว้)
      if(!S.playing && !S.au) S.play();
    }
    try{ document.removeEventListener('click',window.__qsClickH,true); document.removeEventListener('keydown',window.__qsKeyH,true); }catch(e){}
    window.__qsClickH=function(e){ var g=e.target&&e.target.closest&&e.target.closest('.boot-go'); var b=g&&g.closest('.boot'); if(b && !b.classList.contains('boot-out') && bootReady()) enter(b); };
    window.__qsKeyH=function(e){
      if(e.key==='Enter'){ var b=document.querySelector('.boot:not(.boot-out)'); if(b){ e.preventDefault(); if(bootReady()) enter(b); } }
    };
    // ปุ่มเข้า/ออกเต็มจอ (.qs-fs-btn ในแถบซ้าย) — สลับข้อความตามสถานะด้วยคลาส qs-isfs
    function fsOn(){ return !!(document.fullscreenElement||document.webkitFullscreenElement); }
    function fsToggle(){
      var D=document, de=D.documentElement;
      try{
        if(fsOn()){ (D.exitFullscreen||D.webkitExitFullscreen).call(D); }
        else{ var rf=de.requestFullscreen||de.webkitRequestFullscreen; if(rf){ var pr=rf.call(de); if(pr&&pr.catch) pr.catch(function(){}); } }
      }catch(e){}
    }
    try{ document.removeEventListener('click',window.__qsFsClick,true); document.removeEventListener('fullscreenchange',window.__qsFsChg); document.removeEventListener('webkitfullscreenchange',window.__qsFsChg); }catch(e){}
    window.__qsFsClick=function(e){ var t=e.target&&e.target.closest&&e.target.closest('.qs-fs-btn'); if(t){ e.preventDefault(); fsToggle(); } };
    window.__qsFsChg=function(){ document.documentElement.classList.toggle('qs-isfs', fsOn()); };
    document.addEventListener('click',window.__qsFsClick,true);
    document.addEventListener('fullscreenchange',window.__qsFsChg);
    document.addEventListener('webkitfullscreenchange',window.__qsFsChg);
    window.__qsFsChg();
    document.addEventListener('click',window.__qsClickH,true);
    document.addEventListener('keydown',window.__qsKeyH,true);
  }.toString() + ")();";
  try{
    if(P){ if(!P.__qs || P.__qs.v!==10){ P.eval(CODE); } }
  }catch(e){
    try{ var sc=P.document.createElement('script'); sc.textContent=CODE; P.document.head.appendChild(sc); }catch(e2){}
  }
  var S=P&&P.__qs;
  if(!S){ nm.className='n err'; ni.textContent='เครื่องเล่นใช้ไม่ได้ในเบราว์เซอร์นี้'; return; }
  v.value=Math.round(S.vol*100);
  function fill(){ v.style.setProperty('--f', v.value+'%'); } fill();
  function fmt(s){ if(!isFinite(s)||s<0) s=0; s=Math.floor(s); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
  function pad(n){ return (n<10?'0':'')+n; }

  // ชื่อเพลงยาวเกินช่อง → เลื่อนไปมาเบาๆ · เปลี่ยนเพลง → ตัวอักษรถอดรหัสเป็นชื่อเพลง
  var scr=null, lastName='';
  function fitMarquee(){
    ni.classList.remove('mq'); ni.style.removeProperty('--sh');
    var over=ni.scrollWidth-nm.clientWidth;
    if(over>4){ ni.style.setProperty('--sh','-'+(over+6)+'px'); ni.style.setProperty('--dur',Math.max(6,over/16+4)+'s'); ni.classList.add('mq'); }
  }
  function decode(txt){
    clearInterval(scr); ni.classList.remove('mq');
    var chars='█▓▒░#$%&@/<>01', n=0, steps=14;
    scr=setInterval(function(){
      n++; var o='';
      for(var i=0;i<txt.length;i++){ o+=(txt[i]===' '||i<txt.length*n/steps)?txt[i]:chars[Math.floor(Math.random()*chars.length)]; }
      ni.textContent=o;
      if(n>=steps){ clearInterval(scr); ni.textContent=txt; fitMarquee(); }
    },34);
  }

  function render(){
    var on=S.playing;
    b.textContent=on?'■ STOP':'▶ PLAY'; b.className=on?'on':''; box.className=on?'box play':'box'; lv.textContent=on?'ON AIR':'OFF AIR';
    tk.textContent='TRACK '+pad(S.ti+1)+'/'+pad(S.tracks.length);
    if(S.err){ clearInterval(scr); nm.className='n err'; ni.classList.remove('mq'); ni.textContent='ไม่พบไฟล์เพลง (ลองแล้ว: '+(S.tried||'-')+') ตรวจโฟลเดอร์ static/ และ enableStaticServing'; lastName=''; return; }
    nm.className='n';
    var t=S.tracks[S.ti].n;
    if(t!==lastName){ var first=(lastName===''); lastName=t; pf.style.width='0'; tm.textContent='0:00 / 0:00'; if(first){ ni.textContent=t; fitMarquee(); } else decode(t); }
  }
  S.subs=[render]; render();
  b.onclick=function(){ S.playing?S.stop():S.play(); };
  nx.onclick=function(){ S.next(); };
  pv.onclick=function(){ var was=S.playing; if(S.au && S.au.currentTime>3){ S.au.currentTime=0; return; }
    S.ti=(S.ti+S.tracks.length-1)%S.tracks.length; if(was) S.start(); else S.emit(); };
  v.oninput=function(){ fill(); S.setVol(v.value/100); };
  pg.onclick=function(e){ var a=S.au; if(a && isFinite(a.duration) && a.duration>0){ var r=pg.getBoundingClientRect(); a.currentTime=Math.max(0,Math.min(1,(e.clientX-r.left)/r.width))*a.duration; } };

  // แถบเวลาเพลง (อ่านอย่างเดียวจากตัวเล่นหลัก)
  setInterval(function(){
    var a=S.au; if(!a || !isFinite(a.duration) || a.duration<=0) return;
    pf.style.width=(a.currentTime/a.duration*100)+'%'; tm.textContent=fmt(a.currentTime)+' / '+fmt(a.duration);
  },250);

  // สเปกตรัมตกแต่ง: แท่งเต้นตามจังหวะเมื่อเพลงเล่น, ค่อยๆ ลดลงเมื่อหยุด (ไม่ได้วิเคราะห์เสียงจริง)
  var N=22, hs=[], cp=[], ph=[], fr=[], ctx=cv.getContext('2d'), dpr=Math.min(2,window.devicePixelRatio||1), gw=0, grad=null;
  for(var i=0;i<N;i++){ hs.push(0); cp.push(0); ph.push(Math.random()*6.28); fr.push(1.3+Math.random()*2.7); }
  function draw(ts){
    requestAnimationFrame(draw);
    var w=cv.clientWidth, h=cv.clientHeight; if(!w||!h) return;
    if(cv.width!==Math.round(w*dpr)||cv.height!==Math.round(h*dpr)){ cv.width=Math.round(w*dpr); cv.height=Math.round(h*dpr); }
    ctx.setTransform(dpr,0,0,dpr,0,0); ctx.clearRect(0,0,w,h);
    if(gw!==w){ gw=w; grad=ctx.createLinearGradient(0,h,0,0); grad.addColorStop(0,'rgba(0,240,255,.85)'); grad.addColorStop(1,'rgba(0,240,255,.25)'); }
    var t=ts/1000, on=S.playing, gap=3, bw=(w-gap*(N-1))/N, beat=.5+.5*Math.pow(Math.sin(t*2.6),2);
    for(var i=0;i<N;i++){
      var env=1-i/N*.5, wob=.5+.5*Math.sin(t*fr[i]+ph[i]), tgt=on?(.12+.62*wob*(.6+.4*beat))*env:.05;
      hs[i]+=(tgt-hs[i])*(on?.12:.08);
      var bh=Math.max(2,hs[i]*h), x=i*(bw+gap);
      ctx.fillStyle=grad; ctx.fillRect(x,h-bh,bw,bh);
    }
  }
  requestAnimationFrame(draw);
  S.auto();   // พยายามเล่นเองทุกครั้งที่เข้าเว็บ (ถ้าถูกบล็อก จะเล่นตอนคลิกครั้งแรก)
})();
</script></body></html>"""


def music_player():
    """เครื่องเล่นเพลงพื้นหลัง: เล่นเองทุกครั้งที่เข้าเว็บ (ถ้าเบราว์เซอร์บล็อก จะเล่นตอนคลิกครั้งแรก) — เพลงอยู่ใน static/bgm_2.mp3, bgm_1.mp3 ต้องเปิด enableStaticServing"""
    try:
        import streamlit.components.v1 as components
        components.html(MUSIC_HTML, height=146)
    except Exception:
        pass


def brand_sidebar():
    st.markdown(_html(f"""
        <div class="brand">{_mark('brand')}
        <div><div class="brand-name">QUANT</div><div class="brand-sub">STOCK ANALYZER</div></div></div>
    """), unsafe_allow_html=True)
    st.markdown('<div class="qs-fs-btn" role="button" tabindex="0" title="สลับโหมดเต็มจอ (เหมือนกด F11)">'
                '<span class="on-enter">⛶ เข้าโหมดเต็มจอ</span><span class="on-exit">⮌ ออกจากเต็มจอ</span></div>',
                unsafe_allow_html=True)
    s = market_status()
    if s:
        st.markdown(_html(f"""
            <div class="status status-{s['cls']}"><span class="dot"></span>
            <div>{s['label']}<small>เวลาไทย {s['thai']} น. · ไม่รวมวันหยุดพิเศษ</small></div></div>
        """), unsafe_allow_html=True)
    music_player()


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