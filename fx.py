# -*- coding: utf-8 -*-
"""
fx.py  [fx v1]  —  Cyberpunk "Edgerunner" FX layer
===================================================
เลเยอร์เอฟเฟกต์ซ้อนทับธีมเดิม (theme.py) ไม่แตะข้อมูล/ตรรกะใดๆ ของแอป

  fx.control()  วาง "สวิตช์ระดับเอฟเฟกต์" ในแถบข้าง (ใน with st.sidebar:)
  fx.apply()    ฉีด CSS + สคริปต์เอฟเฟกต์ (เรียกครั้งเดียวต่อรอบ หลัง theme.inject())

ระดับ:  เต็มที่ (Edgerunner) / เบา / ปิด     — ถ้าเครื่องตั้ง "ลดการเคลื่อนไหว" จะลดเป็นระดับเบาให้อัตโนมัติ
เอฟเฟกต์:
  เบา   glitch หัวข้อ · แสงกวาดบนหัวหน้า · การ์ด/กล่องเรืองตอนชี้ · ปุ่มสั่น glitch
        · เมนูที่เลือกกะพริบแบบป้ายไฟ · ทรานซิชัน glitch ตอนสลับหน้า
        · กรอบตัดมุมเฉียง · แถบเหลืองหน้าหัวข้อ · เลือกข้อความสีเหลือง · แถบเลื่อนนีออน · ปุ่มสั่นแยกสี
  เต็ม  + ฝนข้อมูล (รหัสหุ้น/คาตาคานะ) · วิกเน็ต + แถบสแกนวิ่ง · จอสั่นกะพริบนิดๆ · เคอร์เซอร์เล็งเป้า
        · สแกนไลน์ · ตัวเลขแยกสีแดง/ฟ้า
        · คลื่นวงแหวนตอนคลิก · หัวข้อ "ถอดรหัส" ตอนเปลี่ยนหน้า · glitch/รอยฉีกจอแบบสุ่ม · มุมกรอบ HUD
"""
import json

import streamlit as st

LEVELS = {"เต็มที่ (Edgerunner)": "full", "เบา": "light", "ปิด": "off"}

# @L = ระดับเบาขึ้นไป (ทุกอย่างที่ไม่ใช่ปิด)   @F = เฉพาะระดับเต็ม
CSS = r"""
<style>
/* ===================== LIGHT ===================== */
/* โลโก้ QUANT: สั่น glitch สั้นๆ ทุก 20 วินาที */
@L .brand-name{animation:qsLogo 20s infinite steps(1);}
@keyframes qsLogo{
  0%{transform:translate(-3px,0) skewX(-7deg);text-shadow:-5px 0 rgba(255,42,109,.95),5px 0 rgba(0,240,255,.95)}
  .6%{transform:translate(4px,1px) skewX(5deg);text-shadow:5px 0 rgba(255,42,109,.95),-5px 0 rgba(252,238,10,.9)}
  1.2%{transform:translate(-2px,-1px) skewX(-3deg);text-shadow:-3px 0 rgba(0,240,255,.95),3px 0 rgba(255,42,109,.9)}
  1.8%,100%{transform:none;text-shadow:1.5px 0 rgba(255,42,109,.85),-1.5px 0 rgba(0,240,255,.85)}
}

/* หัวหน้า: แสงกวาด + ป้ายเรือง */
@L .hero::before{
  content:"";position:absolute;top:0;bottom:0;left:-160px;width:140px;pointer-events:none;z-index:1;
  background:linear-gradient(100deg,transparent,rgba(255,255,255,.10),rgba(0,240,255,.10),transparent);
  transform:skewX(-18deg);animation:qsSheen 10s ease-in-out infinite;
}
/* พักจนเกือบครบ 10 วิ แล้วกวาด 1 รอบ (~3 วิ) */
@keyframes qsSheen{0%,70%{left:-160px}100%{left:calc(100% + 160px)}}

/* หัวข้อส่วน: เส้นวิ่ง */
@L .section-label::after{background:linear-gradient(90deg,rgba(0,240,255,.15),rgba(0,240,255,.9),rgba(252,238,10,.7),rgba(0,240,255,.15)) !important;
  background-size:240% 100% !important;animation:qsLine 4.5s linear infinite;}
@keyframes qsLine{0%{background-position:0 0}100%{background-position:240% 0}}

/* การ์ดตัวเลข: เส้นไฟวิ่งด้านบน + เรืองตอนชี้ */
@L div[data-testid="stMetric"]{position:relative;overflow:hidden;}
@L div[data-testid="stMetric"]::before{
  content:"";position:absolute;top:0;left:-40%;width:40%;height:2px;pointer-events:none;
  background:linear-gradient(90deg,transparent,#fff,var(--cyan),transparent);animation:qsRun 10s linear infinite;
}
/* วิ่ง 1 รอบ (~3.6 วิ) แล้วพักจนครบ 10 วิ */
@keyframes qsRun{0%{left:-40%}36%,100%{left:100%}}
@L div[data-testid="stMetric"]:hover{box-shadow:inset 0 0 26px rgba(252,238,10,.13),inset 0 0 2px rgba(252,238,10,.6);}
@L details[data-testid="stExpander"]{transition:.18s;}
@L details[data-testid="stExpander"]:hover{box-shadow:inset 0 0 22px rgba(0,240,255,.10),0 0 14px rgba(0,240,255,.10);border-color:rgba(0,240,255,.5) !important;}
@L details[data-testid="stExpander"][open]{box-shadow:inset 3px 0 14px -6px rgba(252,238,10,.5);}
@L div[data-testid="stDataFrame"]{box-shadow:0 0 0 1px rgba(0,240,255,.04),0 0 22px rgba(0,240,255,.05);}
@L div[data-testid="stAlert"]{box-shadow:inset 0 0 20px rgba(0,240,255,.05);}

/* ปุ่ม: เรือง + สั่น glitch ตอนชี้ */
@L .stButton > button:active, @L [data-testid="stFormSubmitButton"] > button:active{transform:translate(2px,2px) scale(.98);}

/* แถบซ้าย: เมนูที่เลือกกะพริบแบบป้ายไฟ */
@L section[data-testid="stSidebar"]{position:relative;}
@L section[data-testid="stSidebar"] label[data-testid="stRadioOption"]{transition:transform .32s cubic-bezier(.22,1,.36,1),text-shadow .32s ease;will-change:transform;}
@L section[data-testid="stSidebar"] label[data-testid="stRadioOption"]:hover{transform:translateX(5px);}

/* ทรานซิชัน glitch ตอนสลับหน้า */
@L .qs-switch{animation:qsSwitch .38s ease-out 1;}
@keyframes qsSwitch{0%{opacity:0;transform:translateY(8px)}100%{opacity:1;transform:none}}
/* หน้าบูตต้องเต็มจอเสมอ: ปิดชั้นเอฟเฟกต์ทั้งหมดขณะบูต */
html:has(.boot) #qs-rain, html:has(.boot) #qs-scan, html:has(.boot) #qs-corners{display:none !important;}

/* ===================== FULL ===================== */
/* วิกเน็ต + จอสั่นกะพริบนิดๆ */
@F .stApp::before{
  content:"";position:fixed;inset:0;pointer-events:none;z-index:9997;
  background:radial-gradient(ellipse at center,transparent 52%,rgba(0,0,0,.55) 100%);
}

/* ตัวเลข/หัวข้อเรืองแบบป้ายนีออน */
@F div[data-testid="stMetricValue"]{text-shadow:0 0 14px rgba(0,240,255,.35);}

/* เคอร์เซอร์ลูกศรสามเหลี่ยมนีออนทั้งเว็บ (ฟ้า = ปกติ / เหลือง = ตอนชี้ของที่กดได้) — ช่องพิมพ์คงเป็นเคอร์เซอร์ข้อความ */
@F, @F body, @F *:not(input):not(textarea){cursor:url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='32'%20height='32'%20viewBox='0%200%2032%2032'%3E%3Cpath%20d='M5%204%20L27%2016%20L11%2027%20Z'%20fill='%2305060d'%20fill-opacity='.88'%20stroke='%2300f0ff'%20stroke-opacity='.35'%20stroke-width='4.2'%20stroke-linejoin='round'/%3E%3Cpath%20d='M5%204%20L27%2016%20L11%2027%20Z'%20fill='none'%20stroke='%2300f0ff'%20stroke-width='1.7'%20stroke-linejoin='round'/%3E%3C/svg%3E") 5 4, pointer !important;}
@F button, @F button *, @F a, @F a *, @F label, @F label *, @F summary, @F summary *, @F [role="tab"], @F [role="tab"] *, @F [role="button"], @F [role="button"] *, @F select{
  cursor:url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='32'%20height='32'%20viewBox='0%200%2032%2032'%3E%3Cpath%20d='M5%204%20L27%2016%20L11%2027%20Z'%20fill='%2305060d'%20fill-opacity='.88'%20stroke='%23fcee0a'%20stroke-opacity='.35'%20stroke-width='4.2'%20stroke-linejoin='round'/%3E%3Cpath%20d='M5%204%20L27%2016%20L11%2027%20Z'%20fill='none'%20stroke='%23fcee0a'%20stroke-width='1.7'%20stroke-linejoin='round'/%3E%3C/svg%3E") 5 4, pointer !important;}

/* ชั้นเอฟเฟกต์ที่สร้างด้วยสคริปต์ */
#qs-rain{position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:2;opacity:.20;mix-blend-mode:screen;
  -webkit-mask-image:radial-gradient(ellipse at 50% 45%,transparent 30%,#000 100%);mask-image:radial-gradient(ellipse at 50% 45%,transparent 30%,#000 100%);}
#qs-scan{position:fixed;left:0;right:0;top:-160px;height:150px;pointer-events:none;z-index:9996;
  background:linear-gradient(180deg,transparent,rgba(0,240,255,.045) 60%,rgba(0,240,255,.10) 96%,transparent);animation:qsScan 30s linear infinite;}
/* กวาดลงมา 1 รอบ (~9 วิ) แล้วพักจนครบ 30 วิ */
@keyframes qsScan{0%{top:-160px}30%,100%{top:100vh}}
#qs-corners i{position:fixed;width:26px;height:26px;pointer-events:none;z-index:9995;border:2px solid var(--cyan);opacity:.55;}
#qs-corners .a{top:8px;left:8px;border-right:0;border-bottom:0}#qs-corners .b{top:8px;right:8px;border-left:0;border-bottom:0}
#qs-corners .c{bottom:34px;left:8px;border-right:0;border-top:0}#qs-corners .d{bottom:34px;right:8px;border-left:0;border-top:0}
.qs-rip{position:fixed;width:12px;height:12px;margin:-6px 0 0 -6px;border:2px solid var(--gold);pointer-events:none;z-index:9999;
  animation:qsRip .6s ease-out forwards;}
@keyframes qsRip{0%{transform:scale(1) rotate(0);opacity:1;border-color:#fcee0a}60%{border-color:#00f0ff}100%{transform:scale(7) rotate(90deg);opacity:0;border-color:#ff2a6d}}
.qs-tear{position:fixed;left:0;right:0;pointer-events:none;z-index:9998;mix-blend-mode:screen;
  background:linear-gradient(90deg,transparent,rgba(255,42,109,.35) 20%,rgba(0,240,255,.45) 60%,transparent);
  animation:qsTear .26s steps(3) forwards;}
@keyframes qsTear{0%{transform:translateX(-6%);opacity:1}50%{transform:translateX(5%);opacity:.9}100%{transform:translateX(-2%);opacity:0}}
html:not([data-fx="full"]) #qs-rain, html:not([data-fx="full"]) #qs-scan, html:not([data-fx="full"]) #qs-corners{display:none !important;}
@media (max-width:760px){#qs-rain,#qs-corners{display:none !important;}}
/* ===================== EDGERUNNER+ (แต่งเพิ่ม) ===================== */
/* เลือกข้อความ = เหลืองนีออน + แถบเลื่อนไล่สีฟ้า-ชมพู */
@L ::selection{background:#fcee0a;color:#05060d;}
@L ::-webkit-scrollbar{width:8px;height:8px;}
@L ::-webkit-scrollbar-track{background:#05060d;}
@L ::-webkit-scrollbar-thumb{background:linear-gradient(180deg,var(--cyan),var(--pink));}
@L ::-webkit-scrollbar-thumb:hover{background:var(--gold);}

/* กรอบตัดมุมเฉียง (chamfer) แบบ HUD: การ์ดตัวเลข + กล่องแจ้งเตือน */
@L div[data-testid="stMetric"]{clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px));}
@L div[data-testid="stAlert"]{clip-path:polygon(0 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%);}

/* หัวข้อ h2/h3: แถบเหลืองด้านซ้ายแบบป้ายนีออน */
@L [data-testid="stMain"] [data-testid="stMarkdownContainer"] h2,
@L [data-testid="stMain"] [data-testid="stMarkdownContainer"] h3{
  border-left:3px solid var(--gold);padding-left:.6rem;text-shadow:-1px 0 rgba(255,42,109,.35),1px 0 rgba(0,240,255,.35);
}

/* ปุ่ม: ตอนชี้ สั่นสั้นๆ + เงาแยกสี (chromatic aberration) */
@L .stButton > button, @L .stDownloadButton > button, @L [data-testid="stFormSubmitButton"] > button{transition:transform .22s cubic-bezier(.22,1,.36,1),box-shadow .25s ease,background .15s,color .15s,border-color .15s;}
@L .stButton > button:hover, @L .stDownloadButton > button:hover, @L [data-testid="stFormSubmitButton"] > button:hover{
  transform:translateY(-1px);animation:qsShake .42s ease-in-out 1;
  box-shadow:0 0 14px rgba(252,238,10,.30),-2px 0 0 rgba(255,42,109,.65),2px 0 0 rgba(0,240,255,.65);
}

/* เมนูแถบซ้าย + การ์ดตัวเลข: ตอนชี้สั่นสั้นๆ แบบเดียวกับปุ่ม (เมนูมีตัวอักษรแยกสีแดง/ฟ้าด้วย) */
@L section[data-testid="stSidebar"] label[data-testid="stRadioOption"]:hover{
  text-shadow:-1px 0 rgba(255,42,109,.6),1px 0 rgba(0,240,255,.6);
}
/* การ์ดตัวเลข: ตอนชี้ลอยขึ้นนุ่มๆ (ไม่สั่น) */
@L div[data-testid="stMetric"]{transition:transform .3s cubic-bezier(.22,1,.36,1),box-shadow .3s ease;}
@L div[data-testid="stMetric"]:hover{transform:translateY(-2px);}

/* FULL: ตัวเลขใหญ่แยกสีแดง/ฟ้าเล็กน้อย + เส้นสแกนไลน์จางๆ */
@F div[data-testid="stMetricValue"]{text-shadow:-1px 0 rgba(255,42,109,.7),1px 0 rgba(0,240,255,.7),0 0 14px rgba(0,240,255,.35);}
/* (เอาเส้นสแกนไลน์สีดำพาดจอออกแล้ว) */

/* สั่นนุ่มๆ ตอนชี้ปุ่ม: ไหลต่อเนื่อง (ไม่กระตุกเป็นขั้น) แอมพลิจูดเล็ก ค่อยๆ เบาลงจนนิ่ง */
@keyframes qsShake{0%{transform:translate(0,-1px)}18%{transform:translate(-3px,-1px)}38%{transform:translate(2.5px,-1px)}58%{transform:translate(-1.5px,-1px)}78%{transform:translate(.8px,-1px)}100%{transform:translate(0,-1px)}}

@media (prefers-reduced-motion:reduce){
  @L .hero-title, @L .brand-name, @L .hero::before, @L .hero-mark, @L .hero-pill, @L div[data-testid="stMetric"]::before,
  @L .section-label::after{animation:none !important;}
  @L .stButton > button:hover, @L .stDownloadButton > button:hover, @L [data-testid="stFormSubmitButton"] > button:hover, @L section[data-testid="stSidebar"] label[data-testid="stRadioOption"]:hover, @L div[data-testid="stMetric"]:hover{animation:none !important;}
}
</style>
"""

# สคริปต์เอฟเฟกต์ (รันใน document ของหน้าหลัก ผ่านการฉีด <script> ครั้งเดียว)
FXJS = r"""
(function(){
  if(window.__qsFx && window.__qsFx.v===2) return;
  var F=window.__qsFx={v:2,level:'full'}, D=document, H=D.documentElement;
  var GL='NVDATSLAAMDMUMETAGOOGLAMZNAVGOアイウエオカキクケコサシスセソタチツテト0123456789ABCDEF$%+-';
  var cv=null,cx=null,drops=[],cw=0,ch=0,fs=16,raf=0,lastT=0,timers=[],gl=0,sc=null,co=null;
  function el(tag,id,cls){var e=D.createElement(tag); if(id)e.id=id; if(cls)e.className=cls; return e;}
  function reduced(){try{return window.matchMedia('(prefers-reduced-motion: reduce)').matches;}catch(e){return false;}}

  /* ---------- ฝนข้อมูล ---------- */
  function size(){ if(!cv) return; cw=cv.width=window.innerWidth; ch=cv.height=window.innerHeight;
    var n=Math.ceil(cw/fs); drops=[]; for(var i=0;i<n;i++) drops.push(Math.random()*-60); }
  function frame(t){
    raf=requestAnimationFrame(frame);
    if(D.hidden||t-lastT<55) return; lastT=t;
    cx.globalCompositeOperation='destination-out'; cx.fillStyle='rgba(0,0,0,.13)'; cx.fillRect(0,0,cw,ch);
    cx.globalCompositeOperation='source-over'; cx.font=fs+'px "Share Tech Mono",monospace';
    for(var i=0;i<drops.length;i++){
      if(Math.random()>.55 && drops[i]<0){ drops[i]+=1; continue; }
      var x=i*fs, y=drops[i]*fs, c=GL.charAt((Math.random()*GL.length)|0);
      cx.fillStyle=(Math.random()>.93)?'#fcee0a':'#00f0ff'; cx.fillText(c,x,y);
      if(y>ch && Math.random()>.975) drops[i]=Math.random()*-20; else drops[i]+=1;
    }
  }
  function rainOn(){
    if(window.innerWidth<760) return;
    if(!cv){ cv=el('canvas','qs-rain'); D.body.appendChild(cv); cx=cv.getContext('2d'); window.addEventListener('resize',size); }
    size(); if(!raf) raf=requestAnimationFrame(frame);
  }
  function rainOff(){ if(raf){cancelAnimationFrame(raf);raf=0;} if(cx) cx.clearRect(0,0,cw,ch); }

  /* ---------- ชั้นตกแต่ง ---------- */
  function layers(){
    if(!sc){ sc=el('div','qs-scan'); D.body.appendChild(sc); }
    if(!co){ co=el('div','qs-corners'); co.innerHTML='<i class="a"></i><i class="b"></i><i class="c"></i><i class="d"></i>'; D.body.appendChild(co); }
  }

  /* ---------- glitch สุ่ม + รอยฉีกจอ ---------- */
  function burst(){
    if(F.level==='off'||D.hidden) return;
    H.classList.add('qs-gl'); setTimeout(function(){H.classList.remove('qs-gl');},360);
    if(F.level==='full'){
      var n=1+((Math.random()*3)|0);
      for(var i=0;i<n;i++){ var t=el('div',null,'qs-tear'); t.style.top=((Math.random()*92)|0)+'vh'; t.style.height=(4+((Math.random()*26)|0))+'px';
        D.body.appendChild(t); (function(x){setTimeout(function(){x.remove();},300);})(t); }
    }
  }
  function schedule(){}  /* ปิด glitch/รอยฉีกจอแบบสุ่ม เพื่อไม่ให้หลุดโฟกัส */

  /* ---------- คลื่นวงแหวนตอนคลิก ---------- */
  D.addEventListener('pointerdown',function(e){
    if(F.level!=='full') return;
    var r=el('div',null,'qs-rip'); r.style.left=e.clientX+'px'; r.style.top=e.clientY+'px'; D.body.appendChild(r);
    setTimeout(function(){r.remove();},650);
  },true);

  /* ---------- ทรานซิชัน glitch ตอนสลับหน้า ---------- */
  D.addEventListener('click',function(e){
    if(F.level==='off') return;
    var t=e.target&&e.target.closest&&e.target.closest('section[data-testid="stSidebar"] label[data-testid="stRadioOption"]');
    if(!t) return;
    [120].forEach(function(d){ setTimeout(function(){
      var m=D.querySelector('[data-testid="stMain"] .block-container'); if(!m) return;
      m.classList.remove('qs-switch'); void m.offsetWidth; m.classList.add('qs-switch');
      setTimeout(function(){m.classList.remove('qs-switch');},420);
    },d); });
  },true);

  /* ---------- หัวข้อ "ถอดรหัส" (ทุกหน้า) ---------- */
  var SC='!<>-_\\/[]{}=+*^?#ABCDEF0123456789アイウエオ';
  var SEL='.hero-title,.hero-sub,[data-testid="stMain"] h1';
  /* เก็บทุกข้อความในองค์ประกอบ (รองรับหัวข้อที่มี span/อีโมจิซ้อนอยู่ข้างใน) */
  function textNodes(e){
    var a=[], w=D.createTreeWalker(e,NodeFilter.SHOW_TEXT,null), n;
    while((n=w.nextNode())){ if(n.nodeValue&&n.nodeValue.trim()) a.push(n); }
    return a;
  }
  function sigOf(ns){ return ns.map(function(n){return n.nodeValue;}).join('\u0001'); }
  function scramble(e,ns){
    var fins=ns.map(function(n){return n.nodeValue;}), last=fins.slice(), i=-1, tot=14, iv=0;
    e.__qsRun=true; e.__qsTxt=fins.join('\u0001');
    function done(restore){
      clearInterval(iv); e.__qsRun=false;
      if(restore) ns.forEach(function(n,j){ if(n.isConnected) n.nodeValue=fins[j]; });
    }
    function tick(){
      if(!e.isConnected){ done(false); return; }
      for(var j=0;j<ns.length;j++){
        /* ข้อความถูกเปลี่ยนจากข้างนอก (เช่น สลับหน้าระหว่างถอดรหัส) -> เลิกของเก่า แล้วให้ scan() ถอดรหัสข้อความใหม่ */
        if(!ns[j].isConnected||ns[j].nodeValue!==last[j]){ done(false); e.__qsTxt=null; setTimeout(scan,0); return; }
      }
      i++;
      if(i>=tot){ done(true); return; }
      ns.forEach(function(n,j){
        var fin=fins[j], keep=Math.floor(fin.length*i/tot), s='';
        for(var k=0;k<fin.length;k++){ var c=fin.charAt(k); s+=(k<keep||c===' ')?c:SC.charAt((Math.random()*SC.length)|0); }
        n.nodeValue=s; last[j]=s;
      });
    }
    tick();                             /* เฟรมแรก (รหัสมั่ว) ใส่ทันที ก่อนที่ข้อความจริงจะถูกวาดบนจอ */
    iv=setInterval(tick,38);
  }
  var deb=0;
  function scan(){
    if(F.level!=='full') return;
    D.querySelectorAll(SEL).forEach(function(e){
      if(e.__qsRun) return;
      var ns=textNodes(e); if(!ns.length) return;
      if(e.__qsTxt!==sigOf(ns)) scramble(e,ns);
    });
  }
  try{ new MutationObserver(function(){ scan(); }).observe(D.body,{childList:true,subtree:true,characterData:true}); }catch(e){}

  /* ---------- สั่งงานตามระดับ ---------- */
  F.set=function(l){
    if(l==='full' && reduced()) l='light';
    F.level=l; H.setAttribute('data-fx',l);
    if(l==='full'){ layers(); rainOn(); scan(); } else { rainOff(); }
    schedule();
  };
})();
"""


def control():
    """(ซ่อนสวิตช์แล้ว) คงฟังก์ชันไว้ให้โค้ดเดิมที่เรียก fx.control() ไม่พัง — เอฟเฟกต์ใช้ระดับเต็มที่เสมอ"""
    return


def _css(level: str) -> str:
    L = 'html:not([data-fx="off"])'
    F = 'html[data-fx="full"]'
    return CSS.replace("@L", L).replace("@F", F)


def apply():
    """ฉีด CSS + สคริปต์เอฟเฟกต์ (ปลอดภัย: ถ้าพลาดข้ามเงียบๆ)"""
    try:
        level = LEVELS.get(st.session_state.get("fx_level", "เต็มที่ (Edgerunner)"), "full")
        st.markdown(_css(level), unsafe_allow_html=True)
        import streamlit.components.v1 as components
        boot = ("<!doctype html><html><body><script>(function(){var P,D;try{P=window.parent;D=P.document;}catch(e){return;}"
                "if(!P.__qsFx||P.__qsFx.v!==2){var s=D.createElement('script');s.id='qs-fx-js';s.textContent=" + json.dumps(FXJS)
                + ";D.head.appendChild(s);}"
                "if(P.__qsFx){P.__qsFx.set('" + level + "');}})();</script></body></html>")
        components.html(boot, height=0)
    except Exception:
        pass