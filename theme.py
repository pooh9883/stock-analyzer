# -*- coding: utf-8 -*-
"""
theme.py
========
ดีไซน์ทั้งเว็บ: สไตล์ Cyberpunk (เหลือง-ฟ้า-ชมพูนีออน มุมตัด สแกนไลน์ ตัวเลขฟอนต์โมโน)
ระบบ Boot Sequence เต็มจอคลุมทับ และคลิกเปิด Dashboard พร้อมเล่นเพลงทันที
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

/* radio แนวนอนในหน้าหลัก */
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

/* หัวข้อส่วน */
.section-label{display:flex !important;align-items:center;gap:12px;color:var(--gold) !important;font-size:13px !important;
  font-weight:700 !important;letter-spacing:2px;margin:6px 0 10px 0 !important;}
.section-label::before{content:"//";color:var(--cyan);font-family:var(--mono);}
.section-label::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,rgba(252,238,10,.5),transparent);}
.stMarkdown h4{border-left:3px solid var(--gold);padding-left:11px;margin-top:1.3rem !important;font-weight:700 !important;letter-spacing:.5px;}

/* การ์ด / ตัวเลข */
div[data-testid="stMetric"]{
  background:linear-gradient(160deg,rgba(0,240,255,.07),rgba(12,14,28,.7) 55%) !important;
  border:1px solid var(--line) !important;border-top:2px solid var(--cyan) !important;border-radius:0 !important;padding:14px 16px 10px 16px !important;
  backdrop-filter:blur(6px);transition:.15s;
  clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px));
}
div[data-testid="stMetric"]:hover{border-color:var(--gold) !important;border-top-color:var(--gold) !important;}
div[data-testid="stMetricValue"]{font-family:var(--mono) !important;font-weight:400 !important;font-size:1.95rem !important;letter-spacing:.5px;}
div[data-testid="stMetricLabel"]{color:var(--muted) !important;letter-spacing:1px;}

details[data-testid="stExpander"]{
  background:var(--panel) !important;border:1px solid var(--line) !important;border-left:3px solid var(--cyan) !important;border-radius:0 !important;
  backdrop-filter:blur(6px);margin-bottom:10px !important;
}

/* ปุ่ม */
.stButton, .stDownloadButton{filter:drop-shadow(0 0 6px rgba(252,238,10,.28));transition:.15s;}
.stButton > button, .stDownloadButton > button{
  background:var(--gold) !important;color:#05060d !important;font-weight:700 !important;
  border:none !important;border-radius:0 !important;letter-spacing:.8px;transition:.15s;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px));
}
.stButton > button:hover, .stDownloadButton > button:hover{background:var(--cyan) !important;color:#05060d !important;}
.stButton > button p{color:#05060d !important;}

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

/* ---------- แถบสถานะล่างจอ (HUD) ---------- */
.hud{position:fixed;left:0;right:0;bottom:0;height:28px;z-index:9990;display:flex;align-items:center;gap:22px;padding:0 16px;
  background:rgba(5,6,13,.94);border-top:1px solid var(--cyan);box-shadow:0 -6px 24px rgba(0,240,255,.08);
  font-family:var(--mono);font-size:11.5px;letter-spacing:1px;color:var(--muted);white-space:nowrap;overflow:hidden;}
.block-container{padding-bottom:3.2rem !important; min-height: 100vh;}
</style>
"""


def _html(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


def ensure_streamlit_theme(app_dir) -> bool:
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


BOOT_COMPONENT = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    background: #05060d;
    font-family: 'Share Tech Mono', 'IBM Plex Mono', monospace;
    color: #00f0ff;
    overflow: hidden;
  }
  .boot {
    position: fixed;
    inset: 0;
    z-index: 99999999;
    background: #05060d;
    display: flex;
    justify-content: center;
    align-items: center;
    background-image: repeating-linear-gradient(0deg, transparent 0 2px, rgba(0,240,255,.04) 3px);
  }
  .boot-in {
    font-size: 14px;
    letter-spacing: 1.2px;
    width: min(520px, 86vw);
  }
  .bl {
    white-space: nowrap;
    overflow: hidden;
    width: 0;
    opacity: 0;
    color: var(--cyan, #00f0ff);
    margin: 5px 0;
    animation: bootOn 0s var(--d) forwards, bootType 0.4s steps(46, end) var(--d) forwards;
  }
  .bl.ok {
    color: #fcee0a;
    text-shadow: 2px 0 rgba(255,42,109,.8), -2px 0 rgba(0,240,255,.8);
    font-size: 17px;
    font-weight: 700;
    margin-top: 12px;
  }
  .boot-go {
    opacity: 0;
    margin-top: 24px;
    text-align: center;
    color: #05060d;
    background: #fcee0a;
    border: 2px solid #fcee0a;
    padding: 12px 18px;
    font-weight: 700;
    letter-spacing: 4px;
    font-size: 15px;
    cursor: pointer;
    animation: bootOn 0s 2.5s forwards, goPulse 1.3s ease-in-out 2.5s infinite;
  }
  .boot-go:hover {
    background: #00f0ff;
    border-color: #00f0ff;
    box-shadow: 0 0 25px rgba(0,240,255,0.8);
  }
  .boot-hint {
    opacity: 0;
    margin-top: 10px;
    text-align: center;
    color: #7d86a6;
    font-size: 11.5px;
    letter-spacing: 1px;
    animation: bootOn 0s 2.7s forwards;
  }
  @keyframes goPulse {
    0%, 100% { box-shadow: 0 0 4px rgba(252,238,10,.35); }
    50% { box-shadow: 0 0 18px rgba(0,240,255,.85); }
  }
  @keyframes bootOn { to { opacity: 1; } }
  @keyframes bootType { to { width: 100%; } }
  .fade-out {
    animation: bootExit 0.6s cubic-bezier(.7, 0, .3, 1) forwards;
  }
  @keyframes bootExit {
    0% { transform: none; filter: none; opacity: 1; }
    50% { transform: scaleY(.006); filter: brightness(2.2); opacity: 1; }
    100% { transform: scaleY(.006) scaleX(0); opacity: 0; visibility: hidden; pointer-events: none; }
  }
</style>
</head>
<body>
<div class="boot" id="screen">
  <div class="boot-in">
    <div class="bl" style="--d:.15s">&gt; BOOT SEQUENCE ................ OK</div>
    <div class="bl" style="--d:.65s">&gt; LINKING NIGHT CITY MARKET FEED ... OK</div>
    <div class="bl" style="--d:1.15s">&gt; LOADING QUANT CORE v2077 ........ OK</div>
    <div class="bl" style="--d:1.65s">&gt; SYNCING NEURAL SCANNER .......... OK</div>
    <div class="bl ok" style="--d:2.05s">&gt; ACCESS GRANTED</div>
    <div class="boot-go" id="enter-btn">[ ▶ ENTER NIGHT CITY ]</div>
    <div class="boot-hint">คลิกปุ่มเพื่อเข้าสู่ระบบและเริ่มสตรีมเสียง</div>
  </div>
</div>
<script>
  var btn = document.getElementById('enter-btn');
  var scr = document.getElementById('screen');
  
  function launch(){
    try {
      if(window.parent && window.parent.__qs && window.parent.__qs.play) {
        window.parent.__qs.play();
      }
    } catch(e) {}

    scr.classList.add('fade-out');
    
    setTimeout(function(){
      try {
        if(window.parent && window.parent.streamlitEmit) {
          window.parent.streamlitEmit('set_state', {key: '_qs_booted', value: true});
        }
      } catch(e) {}
      // รีโหลดหน้าเพื่อให้ Streamlit เรนเดอร์ Dashboard เต็มรูปแบบ
      try {
        window.parent.location.reload();
      } catch(e) {
        window.location.reload();
      }
    }, 550);
  }

  btn.addEventListener('click', launch);
  document.addEventListener('keydown', function(e){
    if(e.key === 'Enter' || e.key === ' ') { launch(); }
  });
</script>
</body>
</html>
"""


def boot_once():
    """แสดงหน้าจอ Boot แบบเต็มจอเฉพาะเมื่อยังไม่เคยเข้าสู่ระบบในเซสชันนี้"""
    if not st.session_state.get("_qs_booted", False):
        import streamlit.components.v1 as components
        
        # สร้าง Placeholder เต็มหน้าจอเพื่อเคลียร์เนื้อหาอื่นชั่วคราว
        placeholder = st.empty()
        with placeholder.container():
            # เรนเดอร์หน้า Boot ครอบทับทุกอย่างด้วยความสูงเต็มจอเบราว์เซอร์
            components.html(BOOT_COMPONENT, height=850, scrolling=False)
            st.stop()


def hero(title: str, subtitle: str = "", pill: str = "LIVE"):
    pill_html = f'<div class="hero-pill">● {pill}</div>' if pill else ""
    st.markdown(_html(f"""
        <div class="hero">
        <div class="hero-mark">◆</div>
        <div><div class="hero-title">{title}</div><div class="hero-sub">{subtitle}</div></div>
        {pill_html}
        </div>
    """), unsafe_allow_html=True)


HUD_JS = r"""<!doctype html><html><body><script>
(function(){
  var P, D;
  try{ P=window.parent; D=P.document; }catch(e){ return; }
  var DATA=__DATA__;
  function esc(x){return String(x).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
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
})();
</script></body></html>"""


def hud(markets: dict = None):
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
  <div class="n" id="nm">Let You Down</div>
  <div class="row"><button id="b">▶ PLAY</button><button id="nx" title="เพลงถัดไป" style="min-width:34px;padding:6px 8px">⏭</button><input id="v" type="range" min="0" max="100" value="35" title="ระดับเสียง"></div>
</div>
<script>
(function(){
  var P=null; try{ P=window.parent; void P.document; }catch(e){ P=null; }
  var b=document.getElementById('b'), v=document.getElementById('v'), eq=document.getElementById('eq'), nm=document.getElementById('nm'), nx=document.getElementById('nx');

  var CODE = "(" + function(){
    if(window.__qs && window.__qs.v===11) return;
    var T=[{n:'Let You Down',u:'app/static/bgm_2.mp3'},{n:'wiv — i love u',u:'app/static/bgm_1.mp3'}];
    var S=window.__qs={v:11,ti:0,au:null,playing:false,vol:0.35,tracks:T};
    var ls=null; try{ ls=window.localStorage; }catch(e){}
    function get(k){ try{return ls&&ls.getItem(k);}catch(e){return null;} }
    function set(k,x){ try{ ls&&ls.setItem(k,x); }catch(e){} }
    var sv=get('bgm_vol'); if(sv!==null && !isNaN(parseFloat(sv))) S.vol=parseFloat(sv)/100;
    S.emit=function(){ if(S.onUpdate) S.onUpdate(); };
    
    S.init=function(){
      if(S.au) return;
      var a = new Audio(T[S.ti].u);
      S.au = a;
      a.loop = false;
      a.volume = S.vol;
      a.onended = function(){ S.ti=(S.ti+1)%T.length; S.load(); S.play(); };
    };
    
    S.load=function(){
      if(!S.au) S.init();
      S.au.src = T[S.ti].u;
      S.au.load();
    };

    S.play=function(){
      S.init();
      S.au.play().then(function(){
        S.playing=true; S.emit();
      }).catch(function(e){
        S.playing=false; S.emit();
      });
    };

    S.stop=function(){
      if(S.au) S.au.pause();
      S.playing=false; S.emit();
    };

    S.next=function(){
      S.ti = (S.ti+1)%T.length;
      S.load();
      if(S.playing) S.play();
      S.emit();
    };

    S.setVol=function(x){
      S.vol = x;
      set('bgm_vol', String(Math.round(x*100)));
      if(S.au) S.au.volume = x;
    };
  }.toString() + ")();";

  try{
    if(P){ if(!P.__qs || P.__qs.v!==11){ P.eval(CODE); } }
  }catch(e){
    try{ var sc=P.document.createElement('script'); sc.textContent=CODE; P.document.head.appendChild(sc); }catch(e2){}
  }

  var S = P && P.__qs;
  if(!S) return;

  v.value = Math.round(S.vol * 100);
  
  function render(){
    var on = S.playing;
    b.textContent = on ? '■ STOP' : '▶ PLAY';
    b.className = on ? 'on' : '';
    eq.className = on ? 'eq play' : 'eq';
    nm.textContent = S.tracks[S.ti].n;
  }

  S.onUpdate = render;
  render();

  b.onclick = function(){
    if(S.playing){ S.stop(); } else { S.play(); }
    render();
  };
  nx.onclick = function(){ S.next(); render(); };
  v.oninput = function(){ S.setVol(v.value/100); };
})();
</script></body></html>"""


def music_player():
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
