# -*- coding: utf-8 -*-
"""
theme.py
========
ดีไซน์ทั้งเว็บ: สไตล์ Cyberpunk (เหลือง-ฟ้า-ชมพูนีออน มุมตัด สแกนไลน์ ตัวเลขฟอนต์โมโน)

app.py เรียกใช้:
- ensure_streamlit_theme(โฟลเดอร์แอป)  สร้างไฟล์ .streamlit/config.toml ให้อัตโนมัติ (ทำให้ตาราง/ช่องกรอก/แถบบนเป็นสีเข้มจริง)
- inject()                               ฉีด CSS ทั้งเว็บ
- brand_sidebar()                        โลโก้ + สถานะตลาดสหรัฐ (เวลาไทย) บนแถบซ้าย
- ticker_tape(markets)                   แถบราคาเลื่อนด้านบน
- hero(title, subtitle, pill)            หัวหน้าแบบใหม่
- hud(markets)                           แถบสถานะล่างจอ + ตัวเลขราคากะพริบ
"""

from datetime import datetime
from pathlib import Path

import streamlit as st

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
  background:repeating-linear-gradient(0deg, transparent 0, transparent 2px, rgba(0,240,255,.022) 3px);
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
.brand{display:flex;align-items:center;gap:12px;margin:2px 0 12px 0;}
.brand-mark{width:42px;height:42px;display:grid;place-items:center;font-size:22px;color:#05060d;font-weight:700;
  background:var(--gold);clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px));}
.brand-name{font-weight:700;font-size:21px;letter-spacing:5px;color:#fff;line-height:1.1;
  text-shadow:1.5px 0 rgba(255,42,109,.85),-1.5px 0 rgba(0,240,255,.85);}
.brand-sub{font-size:10px;letter-spacing:3px;color:var(--cyan);opacity:.85;}
.status{display:flex;align-items:center;gap:9px;padding:8px 12px;border:1px solid var(--line);border-left:3px solid var(--c);
  background:var(--panel);font-size:12.5px;color:var(--text);margin-bottom:14px;}
.status .dot{width:8px;height:8px;background:var(--c);box-shadow:0 0 10px var(--c);animation:pulse 1.6s infinite;flex:none;}
.status-open{--c:#19f5a5}.status-ext{--c:#fcee0a}.status-closed{--c:#ff2a6d}
.status small{display:block;color:var(--muted);font-size:11px;}
@keyframes pulse{0%{opacity:1}50%{opacity:.3}100%{opacity:1}}

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
.section-label{display:flex !important;align-items:center;gap:12px;color:var(--gold) !important;font-size:13px !important;
  font-weight:700 !important;letter-spacing:2px;margin:6px 0 10px 0 !important;}
.section-label::before{content:"//";color:var(--cyan);font-family:var(--mono);}
.section-label::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,rgba(252,238,10,.5),transparent);}
.stMarkdown h4{border-left:3px solid var(--gold);padding-left:11px;margin-top:1.3rem !important;font-weight:700 !important;letter-spacing:.5px;}

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
.stButton, .stDownloadButton{filter:drop-shadow(0 0 6px rgba(252,238,10,.28));transition:.15s;}
.stButton:hover, .stDownloadButton:hover{filter:drop-shadow(0 0 11px rgba(0,240,255,.65));}
.stButton > button, .stDownloadButton > button{
  background:var(--gold) !important;color:#05060d !important;font-weight:700 !important;
  border:none !important;border-radius:0 !important;letter-spacing:.8px;transition:.15s;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px));
}
.stButton > button:hover, .stDownloadButton > button:hover{background:var(--cyan) !important;color:#05060d !important;}
.stButton > button:active{background:var(--pink) !important;}
.stButton > button p{color:#05060d !important;}

/* แท็บ */
button[data-baseweb="tab"]{font-weight:600;color:var(--muted);letter-spacing:.5px;}
button[data-baseweb="tab"][aria-selected="true"]{color:var(--gold) !important;}
div[data-baseweb="tab-highlight"]{background:var(--gold) !important;height:3px !important;border-radius:0;box-shadow:0 0 12px rgba(252,238,10,.6);}
div[data-baseweb="tab-border"]{background:var(--line) !important;}

hr{border-color:var(--line) !important;}

/* กันข้อความในปุ่ม/ตัวเลือกถูกตัดเป็น "..." */
[data-testid="stMain"] label[data-testid="stRadioOption"] p,
.stButton > button p, .stDownloadButton > button p{
  white-space:normal !important;overflow:visible !important;text-overflow:clip !important;line-height:1.25;
}
.stButton > button *, .stDownloadButton > button *,
[data-testid="stMain"] label[data-testid="stRadioOption"] *{
  white-space:normal !important;overflow:visible !important;text-overflow:clip !important;
}
.stButton > button, .stDownloadButton > button{height:auto !important;min-height:38px;padding:6px 10px !important;}
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


def hero(title: str, subtitle: str = "", pill: str = "LIVE"):
    pill_html = f'<div class="hero-pill">● {pill}</div>' if pill else ""
    st.markdown(_html(f"""
        <div class="hero">
        <div class="hero-mark">◆</div>
        <div><div class="hero-title">{title}</div><div class="hero-sub">{subtitle}</div></div>
        {pill_html}
        </div>
    """), unsafe_allow_html=True)


BOOT_HTML = """
<div class="boot"><i class="boot-c c-tl"></i><i class="boot-c c-tr"></i><i class="boot-c c-bl"></i><i class="boot-c c-br"></i>
<div class="boot-top"><span>QUANT STOCK ANALYZER // SYSTEM BOOT</span><span>v2077</span></div>
<div class="boot-bot"><span>SECURE LINK ESTABLISHED</span><span>NIGHT CITY MARKET FEED</span></div>
<div class="boot-in">
<div class="bl" style="--d:.15s">&gt; BOOT SEQUENCE ................ OK</div>
<div class="bl" style="--d:.65s">&gt; LINKING NIGHT CITY MARKET FEED ... OK</div>
<div class="bl" style="--d:1.15s">&gt; LOADING QUANT CORE v2077 ........ OK</div>
<div class="bl" style="--d:1.65s">&gt; SYNCING NEURAL SCANNER .......... OK</div>
<div class="bl ok" style="--d:2.05s">&gt; ACCESS GRANTED</div>
<div class="boot-go">[ ▶ ENTER NIGHT CITY ]</div>
<div class="boot-hint">กดปุ่มด้านบน หรือกดแป้น Enter เพื่อเข้าสู่ระบบ</div>
</div></div>
"""


def boot_once():
    """หน้าบูตแบบเทอร์มินัล: แสดงครั้งเดียวต่อเซสชัน แล้วจางหายเอง"""
    try:
        if not st.session_state.get("_qs_booted"):
            st.session_state["_qs_booted"] = True
            st.markdown(BOOT_HTML, unsafe_allow_html=True)
    except Exception:
        pass


HUD_JS = r"""<!doctype html><html><body><script>
(function(){
  var P, D;
  try{ P=window.parent; D=P.document; }catch(e){ return; }
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
    var s=mkt(), t='';
    DATA.slice(0,4).forEach(function(x){
      if(x[1]==null) return;
      var up=x[2]>=0;
      t+='<span class="hide-sm"><b>'+esc(x[0])+'</b> '+Number(x[1]).toLocaleString('en-US',{maximumFractionDigits:2})+' <span class="'+(up?'u':'d')+'">'+(up?'▲':'▼')+Math.abs(x[2]).toFixed(2)+'%</span></span>';
    });
    h.innerHTML='<span class="st" style="--c:'+s[0]+'"><i></i>'+s[1]+'</span>'
      +'<span class="hide-sm"><span class="tag">BKK</span> <b>'+tm('Asia/Bangkok')+'</b> &nbsp;<span class="tag">NYC</span> <b>'+tm('America/New_York')+'</b></span>'
      +'<span class="sp"></span>'+t;
  }
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
        components.html(HUD_JS.replace("__DATA__", json.dumps(data, ensure_ascii=False)), height=0)
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
  .box{border:1px solid rgba(0,240,255,.2);border-left:3px solid #fcee0a;background:rgba(12,14,28,.78);padding:9px 11px 10px;}
  .t{font-size:10px;letter-spacing:2.2px;color:#00f0ff;display:flex;justify-content:space-between;align-items:center;}
  .n{font-size:12.5px;font-weight:600;margin:3px 0 7px;letter-spacing:.3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
  .n.err{color:#ff2a6d;white-space:normal;font-size:11.5px;line-height:1.3;}
  .row{display:flex;align-items:center;gap:9px;}
  button{background:#fcee0a;color:#05060d;border:0;font:700 12px 'Chakra Petch',sans-serif;letter-spacing:1px;padding:6px 12px;cursor:pointer;
    clip-path:polygon(0 0,calc(100% - 7px) 0,100% 7px,100% 100%,7px 100%,0 calc(100% - 7px));min-width:74px;}
  button:hover{background:#00f0ff;} button.on{background:#ff2a6d;color:#fff;}
  input[type=range]{flex:1;accent-color:#fcee0a;height:4px;min-width:0;}
  .eq{display:flex;gap:2px;align-items:flex-end;height:14px;}
  .eq i{display:block;width:3px;height:3px;background:#00f0ff;}
  .eq.play i{animation:b .7s ease-in-out infinite alternate;}
  .eq.play i:nth-child(2){animation-delay:.12s}.eq.play i:nth-child(3){animation-delay:.25s}.eq.play i:nth-child(4){animation-delay:.07s}.eq.play i:nth-child(5){animation-delay:.33s}
  @keyframes b{from{height:3px}to{height:14px}}
</style></head><body>
<div class="box">
  <div class="t"><span>NIGHT CITY FM</span><span class="eq" id="eq"><i></i><i></i><i></i><i></i><i></i></span></div>
  <div class="n" id="nm">—</div>
  <div class="row"><button id="b">▶ PLAY</button><button id="nx" title="เพลงถัดไป" style="min-width:34px;padding:6px 8px">⏭</button><input id="v" type="range" min="0" max="100" value="35" title="ระดับเสียง"></div>
</div>
<script>
(function(){
  var P=null; try{ P=window.parent; void P.document; }catch(e){ P=null; }
  var b=document.getElementById('b'), v=document.getElementById('v'), eq=document.getElementById('eq'), nm=document.getElementById('nm'), nx=document.getElementById('nx');

  // ตัวเล่นเพลงอยู่ที่หน้าต่างหลัก (ไม่ใช่ใน iframe) เพื่อให้เพลงเล่นต่อเนื่อง ไม่เริ่มใหม่เวลา Streamlit รีโหลดหน้า
  var CODE = "(" + function(){
    if(window.__qs && window.__qs.v===7) return;
    var T=[{n:'Let You Down',f:'bgm_2.mp3'},{n:'wiv — i love u (slowed + reverb)',f:'bgm_1.mp3'}];
    // ลองหลายตำแหน่ง: ในเครื่อง (/app/static) และบน Streamlit Cloud ที่แอปอยู่ใต้ /~/+/
    function urls(f){ var out=[]; ['app/static/'+f,'/app/static/'+f,'/~/+/app/static/'+f].forEach(function(u){ var h; try{ h=new URL(u,document.baseURI).href; }catch(e){ h=u; } if(out.indexOf(h)<0) out.push(h); }); return out; }
    var S=window.__qs={v:7,ti:0,au:null,playing:false,err:false,vol:0.35,subs:[],tracks:T,armed:false};
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
    function enter(b){
      b.classList.add('boot-out');
      S.off=false; set('bgm_off','0');            // กดเข้าระบบ = ตั้งใจเปิดเพลง (แม้เคยกด STOP ไว้)
      if(!S.playing && !S.au) S.play();
    }
    try{ document.removeEventListener('click',window.__qsClickH,true); document.removeEventListener('keydown',window.__qsKeyH,true); }catch(e){}
    window.__qsClickH=function(e){ var g=e.target&&e.target.closest&&e.target.closest('.boot-go'); var b=g&&g.closest('.boot'); if(b && !b.classList.contains('boot-out')) enter(b); };
    window.__qsKeyH=function(e){
      if(e.key==='Enter'){ var b=document.querySelector('.boot:not(.boot-out)'); if(b){ e.preventDefault(); enter(b); } }
    };
    document.addEventListener('click',window.__qsClickH,true);
    document.addEventListener('keydown',window.__qsKeyH,true);
  }.toString() + ")();";
  try{
    if(P){ if(!P.__qs || P.__qs.v!==7){ P.eval(CODE); } }
  }catch(e){
    try{ var sc=P.document.createElement('script'); sc.textContent=CODE; P.document.head.appendChild(sc); }catch(e2){}
  }
  var S=P&&P.__qs;
  if(!S){ nm.className='n err'; nm.textContent='เครื่องเล่นใช้ไม่ได้ในเบราว์เซอร์นี้'; return; }
  v.value=Math.round(S.vol*100);
  function render(){
    var on=S.playing;
    b.textContent=on?'■ STOP':'▶ PLAY'; b.className=on?'on':''; eq.className=on?'eq play':'eq';
    if(S.err){ nm.className='n err'; nm.textContent='ไม่พบไฟล์เพลง (ลองแล้ว: '+(S.tried||'-')+') ตรวจโฟลเดอร์ static/ และ enableStaticServing'; }
    else{ nm.className='n'; nm.textContent=S.tracks[S.ti].n; }
  }
  S.subs=[render]; render();
  b.onclick=function(){ S.playing?S.stop():S.play(); };
  nx.onclick=function(){ S.next(); };
  v.oninput=function(){ S.setVol(v.value/100); };
  S.auto();   // พยายามเล่นเองทุกครั้งที่เข้าเว็บ (ถ้าถูกบล็อก จะเล่นตอนคลิกครั้งแรก)
})();
</script></body></html>"""


def music_player():
    """เครื่องเล่นเพลงพื้นหลัง: เล่นเองทุกครั้งที่เข้าเว็บ (ถ้าเบราว์เซอร์บล็อก จะเล่นตอนคลิกครั้งแรก) — เพลงอยู่ใน static/bgm_2.mp3, bgm_1.mp3 ต้องเปิด enableStaticServing"""
    try:
        import streamlit.components.v1 as components
        components.html(MUSIC_HTML, height=112)
    except Exception:
        pass


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
