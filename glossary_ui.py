# -*- coding: utf-8 -*-
"""หน้า ศัพท์ & เริ่มต้นใช้งาน — รวมคำที่เจอในเว็บ อ่านเป็นตารางเดียว ค้นคำได้"""
import html as _h

import streamlit as st

# (คำ, แปลง่ายๆ, อ่านยังไง)
_SECTIONS = [
    ("A · อารมณ์ตลาด / หน้าแรก", [
        ("คะแนนกลัว-โลภ (0–100)", "อุณหภูมิความกลัวของตลาด เฉลี่ยจาก 4 ช่อง", "0 = กลัวสุด · 50 = กลางๆ · 100 = โลภสุด · สีบอกอารมณ์ ไม่ได้บอกว่าดีหรือไม่ดี"),
        ("VIX", "ดัชนีความกลัว ยิ่งสูงยิ่งกลัว", "ต่ำกว่า 16 นิ่ง · 16–22 เริ่มระแวง · 22–30 ตื่นกลัว · 30 ขึ้นไป ตื่นกลัวสูงมาก"),
        ("มิเตอร์ Cyberpsychosis", "VIX ในหน้าตาแบบเกม ลูกศร \"← ตอนนี้\" ชี้ว่าอยู่ช่วงไหน", "แถบเต็ม = ตลาดกลัวมาก"),
        ("S&P 500 / SPY", "ดัชนีหุ้นใหญ่ 500 ตัวของสหรัฐ (SPY คือกองทุนที่ตามดัชนีนี้)", "ใช้เป็นตัววัดตลาดรวม"),
        ("แรงส่งของตลาด", "ราคาตลาดอยู่เหนือหรือใต้เส้นเฉลี่ย 6 เดือนกี่ %", "บวก = แข็ง · ลบ = อ่อน"),
        ("ห่างจากจุดสูงสุด 52 สัปดาห์", "ตลาดต่ำกว่าจุดสูงสุดของปีกี่ %", "ต่ำกว่า 3% ใกล้ยอด · 3–10% ย่อปกติ · เกิน 10% ลงลึก"),
        ("ดัชนี SET ขึ้น \"—\"", "ดึงข้อมูลไม่ได้ (ข้อจำกัดของ Yahoo ฟรี)", "ไม่ใช่เว็บเสีย"),
    ]),
    ("B · หุ้นซิ่ง: ตารางคัดหุ้น", [
        ("RSI", "2 สัปดาห์ที่ผ่านมาคนขายหรือคนซื้อมากกว่า", "ต่ำกว่า 30 ขายหนัก · 30–35 ใกล้โซนขายหนัก · สูงกว่า 70 ซื้อหนัก"),
        ("Oversold / Overbought", "ขายเกินไป / ซื้อเกินไป", "Oversold ไม่ได้แปลว่าลงจบ ต้องรอเห็นเด้ง"),
        ("EMA20", "เส้นราคาเฉลี่ย 20 วัน", "ราคาห่างจากเส้นมาก = มักถูกดึงกลับ"),
        ("ATR", "หุ้นแกว่งเฉลี่ยวันละกี่ดอลลาร์ (และกี่ %)", "สูง = แกว่งแรง · ใช้ตั้งจุดตัดขาดทุน"),
        ("ปริมาณ x ปกติ (Volume)", "วันนี้ซื้อขายมากกว่าปกติกี่เท่า", "2 เท่าขึ้นไป = คนแห่ผิดปกติ"),
        ("จากจุดสูง 20 วัน %", "ต่ำกว่าจุดสูงสุด 20 วันกี่ %", "ลบมาก = ลงลึก"),
        ("5 วัน %", "ราคาเปลี่ยนกี่ % ใน 5 วัน", ""),
        ("ผ่านพิสูจน์ (ข้อ)", "ผ่านเงื่อนไขที่ทดสอบย้อนหลังแล้วช่วยได้นิดหน่อย", "2 ข้อดีกว่า 1 ข้อ แต่ไม่ใช่การรับประกันกำไร"),
        ("แท่งเขียว / แดง", "วันนี้ปิดสูง / ต่ำกว่าราคาเปิด", "แดงหลังร่วงแรง = ยังไม่เห็นคนรับ"),
        ("หางล่างยาว", "ลงลึกกลางวันแต่ดีดกลับ", "แปลว่ามีคนรับซื้อ"),
        ("ทำต่ำใหม่", "ราคาต่ำกว่าเมื่อวาน", "แรงขายยังไม่จบ"),
        ("เด้ง (Bounce)", "ราคาดีดกลับหลังลงแรง", ""),
        ("งบ (Earnings)", "วันที่บริษัทประกาศผลประกอบการ", "ราคากระโดดแรงทั้งขึ้นลง รู้วันไว้ก่อนเสมอ"),
    ]),
    ("C · แผนความเสี่ยง & สมุดเทรด", [
        ("Entry", "ราคาที่ซื้อ", ""),
        ("Stop loss", "ราคาที่ตั้งไว้ว่าลงถึงนี้ต้องขายออก", "ตั้งก่อนซื้อทุกครั้ง"),
        ("1.5 × ATR", "จุดตัดขาดทุนห่างจากราคาซื้อ 1.5 เท่าของความแกว่งรายวัน", "ไม่ใกล้จนโดนเขี่ยง่าย"),
        ("R", "เงินที่ยอมเสียต่อ 1 ไม้ (ถ้าโดนตัดขาดทุนเสีย 1R)", "ตัวสำคัญที่สุดในการคุมพอร์ต"),
        ("1R / 2R / 3R", "กำไร 1, 2, 3 เท่าของที่ยอมเสีย", ""),
        ("R/R", "กำไรที่หวัง ÷ เงินที่ยอมเสีย", "4.4:1 = เสี่ยง 1 หวังได้ 4.4"),
        ("ยอมเสียต่อไม้ (%)", "ถ้าโดนตัดขาดทุน ยอมเสียกี่ % ของพอร์ต", "เช่น 1% ของ 100,000 = 1,000"),
        ("ไม้ (Position)", "การซื้อ 1 ครั้ง · ขนาดไม้ = ซื้อกี่หุ้น", "เว็บคำนวณให้จากเงินที่ยอมเสีย"),
        ("FLATLINE", "ราคาถึงหรือต่ำกว่าจุดตัดขาดทุน", "ต้องตัดสินใจทันที"),
        ("DANGER", "ราคาห่างจุดตัดขาดทุนไม่ถึง 1.5%", "ใกล้โดนแล้ว"),
        ("HOLD / PROFIT", "ถือต่อ / กำลังกำไร", ""),
    ]),
    ("D · คุณภาพ & การเติบโต", [
        ("CAGR", "อัตราโตเฉลี่ยต่อปี (แบบทบต้น)", ""),
        ("รายได้โต", "ยอดขายโตไหม", "✅ โตทุกปี · ⚠️ ไม่โต"),
        ("กำไรขั้นต้นโต", "กำไรหลังหักต้นทุนสินค้า", "✅ โตตามยอดขาย · ⚠️ ขายโตแต่กำไรไม่โต"),
        ("กำไรสุทธิโต", "กำไรที่เหลือถึงผู้ถือหุ้น", "✅ โตตามยอดขาย · ⚠️ ไม่โต"),
        ("อัตรากำไรสุทธิ", "ขาย 100 เหลือกำไรกี่บาท", "✅ สูงกว่าคู่แข่ง · ⚠️ ต่ำกว่าคู่แข่งมาก (เทียบในธุรกิจเดียวกัน)"),
        ("ROIC", "เอาเงินไปทำกำไรเก่งแค่ไหน", "✅ 15% ขึ้นไป · ⚠️ ต่ำกว่า 15%"),
        ("FCF", "เงินสดจริงที่เหลือหลังลงทุน", "✅ บวกทุกปี · ⚠️ ติดลบบ่อย"),
        ("D/E", "หนี้เทียบกับเงินผู้ถือหุ้น", "✅ ไม่เกิน 1.5 เท่า · ⚠️ เกิน 1.5 เท่า (ธนาคาร/ประกันใช้ตัวนี้ไม่ได้)"),
    ]),
    ("E · มูลค่า: ราคาแพงไหม", [
        ("P/E", "ราคา ÷ กำไรต่อหุ้น (คืนทุนกี่ปี)", "✅ ต่ำกว่าคู่แข่ง · ⚠️ สูงกว่าคู่แข่งมาก (เทียบในอุตสาหกรรมเดียวกัน)"),
        ("Forward P/E", "ใช้กำไรที่นักวิเคราะห์คาดปีหน้า", "✅ ต่ำกว่า P/E ปกติ = คาดว่ากำไรโต · ⚠️ เป็นแค่คำคาดการณ์"),
        ("PEG", "P/E ปรับตามการโตของกำไร", "✅ ต่ำกว่า 1 · ⚠️ เกิน 2"),
        ("DCF (มูลค่าแท้จริง)", "ประมาณเงินสดอนาคตแล้วคิดกลับเป็นมูลค่าวันนี้", "ไวต่อสมมติฐานมาก ใช้เป็นเครื่องเตือน ไม่ใช่ราคาที่แท้จริง"),
        ("ส่วนเผื่อความปลอดภัย", "ราคาถูกหรือแพงกว่า DCF กี่ %", "✅ บวก (ถูกกว่า) · ⚠️ ลบมาก (แพงกว่า)"),
    ]),
    ("F · โมเมนตัม & มุมเสริม", [
        ("Relative Strength (1–99)", "จัดอันดับว่าแข็งกว่าหุ้นอื่นแค่ไหน", "✅ สูง (ราว 70 ขึ้นไป เป็นเกณฑ์ที่คนนิยมใช้) · ⚠️ ต่ำกว่า 50"),
        ("ชนะ SPY (6 เดือน)", "ชนะหรือแพ้ดัชนี", "✅ บวก · ⚠️ ลบ"),
        ("โมเมนตัม 12-1 เดือน", "ผลตอบแทน 1 ปี ตัดเดือนล่าสุดทิ้ง", "✅ บวก · ⚠️ ลบ"),
        ("เทรนด์ (ราคา > SMA50 > SMA200)", "ขาขึ้นชัดไหม (SMA = เส้นเฉลี่ย)", "✅ \"ใช่\" · ⚠️ \"ไม่\""),
        ("ปริมาณ 20÷90 วัน", "ช่วงนี้คนสนใจมากกว่าปกติไหม", "✅ มากกว่า 1 · ⚠️ น้อยกว่า 1"),
        ("ปริมาณวันขึ้น÷วันลง", "คนซื้อหนักกว่าคนขายไหม", "✅ มากกว่า 1 · ⚠️ น้อยกว่า 1"),
        ("Piotroski F-Score (0–9)", "ตรวจสุขภาพการเงิน 9 ข้อ", "✅ 8–9 · ⚠️ 0–2"),
        ("Rule of 40", "โตเร็วโดยไม่เผาเงินไหม", "✅ เกิน 40 · ⚠️ ต่ำกว่า 40 (ใช้กับซอฟต์แวร์เป็นหลัก)"),
        ("หุ้นเปลี่ยนต่อปี", "บริษัทซื้อคืนหรือออกหุ้นใหม่", "✅ ติดลบ (ซื้อคืน) · ⚠️ บวก (ถูกเจือจาง)"),
    ]),
    ("G · วัฏจักรหุ้น & หุ้นเด่น", [
        ("Stage 1–4 (วัฏจักรหุ้น)", "หุ้นวนอยู่ 4 ช่วง: พักฐาน → ขาขึ้น → ใกล้ยอด → ขาลง", "✅ Stage 2 (ขาขึ้น) = ช่วงที่แนวคิดนี้มองว่าน่าสนใจ · ⚠️ Stage 3 ถือได้แต่ไม่ควรเติม · ⚠️ Stage 4 ไม่ควรเข้า"),
        ("เส้น MA30 สัปดาห์", "เส้นราคาเฉลี่ย 30 สัปดาห์ (ราว 150 วันทำการ) ใช้เป็นเส้นแบ่งขาขึ้น/ขาลง", "✅ ราคาเหนือเส้นและเส้นชี้ขึ้น · ⚠️ ราคาใต้เส้นและเส้นชี้ลง"),
        ("ห่างเส้น MA30 (%)", "ราคาสูงกว่าเส้นกี่ % บอกว่าวิ่งมาไกลแค่ไหน", "✅ ไม่เกิน 15% = ช่วงต้น · ⚠️ เกิน 30% = วิ่งไกล รอย่อ (เกณฑ์เป็นกฎหัวแม่มือ ไม่ใช่มาตรฐาน)"),
        ("Stage 1 กับ 3 แยกยาก", "เส้นแบนทั้งคู่ ต้องดูว่าก่อนหน้านั้นขึ้นมาหรือลงมา", "เว็บบอกได้แค่ประมาณ · ใช้เป็นแนวคิด ไม่ใช่คำตัดสิน"),
        ("แนวรับ / แนวต้าน", "ระดับราคาที่ราคามักหยุดลง / หยุดขึ้น", "✅ ซื้อใกล้แนวรับ ตัดขาดทุนใต้แนวรับ · ⚠️ ราคาชิดแนวต้านมักขึ้นต่อยาก"),
        ("R:R (กำไรที่หวัง ÷ ขาดทุนที่ยอมรับ)", "ถ้าผิดทางเสียเท่าไหร่ เทียบกับถ้าถูกทางได้เท่าไหร่", "✅ 2 ขึ้นไป = คุ้ม · ⚠️ ต่ำกว่า 1 = เสี่ยงมากกว่าที่ได้ · ใช้ในหน้าหุ้นซิ่ง (หน้า TOP PICKS ไม่ใช้ เพราะแนวต้านเล็กๆ ทำให้ตัวเลขเพี้ยน)"),
        ("ระดับที่ใช้รอ (TOP PICKS)", "เส้น MA30 และแนวรับใกล้สุด ใช้เป็นระดับอ้างอิงตอนรอราคาย่อ", "✅ ใช้ตั้งออเดอร์รอหรือจดเตือน · ⚠️ ไม่ได้แปลว่าราคาจะย่อลงไปถึง"),
        ("คะแนนรวม (TOP PICKS)", "เฉลี่ย 4 เสา: คุณภาพ · เติบโต · ราคา · แรงตลาด", "✅ สูงหลายเสาพร้อมกัน · ⚠️ คะแนนรวมสูงแต่เสาใดเสาหนึ่งต่ำมาก ให้ดูเสานั้นก่อน"),
        ("หุ้นดี ≠ จังหวะดี", "บริษัทดีกับราคาที่ควรซื้อตอนนี้ เป็นคนละเรื่อง", "คะแนนสูง + วิ่งไกลจากเส้น MA30 = เก็บเข้าลิสต์รอ รอย่อแล้วค่อยพิจารณา"),
    ]),
]

_COL = ["#00f0ff", "#fcee0a", "#ff2a6d", "#19f5a5", "#ff9f43", "#8b5cf6"]   # สีประจำหมวด A–G (หมวดที่เกินวนสีซ้ำ)

_CSS = """<style>
.gl-term{--c:#00f0ff}
.gl-strip{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:13px;letter-spacing:1.5px;color:#5ee7ff!important;-webkit-text-fill-color:#5ee7ff;
 border:1px solid rgba(0,240,255,.3);background:rgba(0,240,255,.05);padding:7px 12px;margin:2px 0 12px;display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;
 clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,10px 100%,0 calc(100% - 10px))}
.gl-strip b{color:#fcee0a!important;-webkit-text-fill-color:#fcee0a;font-weight:400}
.gl-cur{display:inline-block;width:8px;height:14px;background:#00f0ff;vertical-align:-2px;margin-left:4px;animation:glb 1.1s steps(2) infinite}
@keyframes glb{50%{opacity:0}}
.gl-core{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px;margin:0 0 12px}
.gl-card{--c:#00f0ff;border:1px solid rgba(255,255,255,.1);border-top:3px solid var(--c);background:linear-gradient(160deg,rgba(255,255,255,.05),rgba(10,12,22,.8) 60%);
 padding:10px 13px;clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}
.gl-card .k{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:22px;letter-spacing:2px;color:var(--c)!important;-webkit-text-fill-color:var(--c);text-shadow:0 0 10px var(--c)}
.gl-card .q{font-size:13px;color:#e6f1ff!important;-webkit-text-fill-color:#e6f1ff;margin-top:2px}
.gl-card .a{font-size:12px;color:#9aa4c4!important;-webkit-text-fill-color:#9aa4c4;margin-top:3px;line-height:1.5}
.gl-box{border:1px solid rgba(0,240,255,.3);border-left:4px solid #fcee0a;background:rgba(10,12,22,.78);padding:11px 15px;margin:0 0 14px;line-height:1.75;
 clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px))}
.gl-box b{color:#fcee0a!important;-webkit-text-fill-color:#fcee0a}
.gl-box .flow{color:#00f0ff!important;-webkit-text-fill-color:#00f0ff;font-weight:600}
.gl-wrap{overflow-x:auto;margin:6px 0 4px}
.gl-t{width:100%;border-collapse:collapse;font-size:.95rem}
.gl-t th{text-align:left;padding:8px 10px;border-bottom:2px solid #00f0ff;color:#00f0ff!important;-webkit-text-fill-color:#00f0ff;font-weight:700;letter-spacing:1px;white-space:nowrap}
.gl-t td{padding:8px 10px;border-bottom:1px solid rgba(255,255,255,.07);vertical-align:top;line-height:1.55;color:#e6f1ff!important;-webkit-text-fill-color:#e6f1ff}
.gl-t tr:hover td{background:rgba(0,240,255,.06)}
.gl-t td.t{font-weight:700;white-space:nowrap;border-left:3px solid var(--c);color:var(--c)!important;-webkit-text-fill-color:var(--c);text-shadow:0 0 8px rgba(255,255,255,.12)}
.gl-t td.g{font-size:.78rem;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6;white-space:nowrap}
.gl-ok{color:#19f5a5!important;-webkit-text-fill-color:#19f5a5}
.gl-wn{color:#ff9f43!important;-webkit-text-fill-color:#ff9f43}
.gl-foot{font-family:'Share Tech Mono',ui-monospace,monospace;font-size:12px;color:#7d86a6!important;-webkit-text-fill-color:#7d86a6;margin-top:6px;letter-spacing:1px}
@media (prefers-reduced-motion:reduce){.gl-cur{animation:none}}
</style>"""

_CORE = [
    ("VIX", "ตลาดกลัวแค่ไหน", "ดูก่อนเริ่มวัน · ตัดสินว่าจะลงหนักหรือเบา", "#00f0ff"),
    ("RSI", "ลงแรงแค่ไหน", "ต่ำกว่า 30 = ขายหนัก · ใช้ตอนคัดหุ้น", "#fcee0a"),
    ("ATR", "แกว่งวันละเท่าไหร่", "ใช้ตั้งจุดตัดขาดทุน", "#ff2a6d"),
    ("R", "ยอมเสียเท่าไหร่", "ก่อนกดซื้อทุกครั้ง · ตัวสำคัญที่สุด", "#19f5a5"),
]


def _how(txt):
    """ทำให้ ✅ เป็นสีเขียว และ ⚠️ เป็นสีส้ม ส่วนที่เหลือเป็นข้อความปกติ"""
    outp = []
    for seg in txt.split(" · "):
        s = _h.escape(seg)
        if seg.startswith("✅"):
            s = "<span class='gl-ok'>" + s + "</span>"
        elif seg.startswith("⚠️"):
            s = "<span class='gl-wn'>" + s + "</span>"
        outp.append(s)
    return " · ".join(outp)


def _table(rows, with_group=False):
    head = "<tr>" + ("<th>หมวด</th>" if with_group else "") + "<th>คำ</th><th>แปลง่ายๆ</th><th>อ่านยังไง</th></tr>"
    body = ""
    for r in rows:
        g, idx, t, m, rd = (r if with_group else ("", r[0]) + tuple(r[1:]))
        body += ("<tr>" + ("<td class='g'>" + _h.escape(g) + "</td>" if with_group else "")
                 + "<td class='t' style='--c:" + _COL[idx % len(_COL)] + "'>" + _h.escape(t) + "</td><td>" + _h.escape(m)
                 + "</td><td>" + _how(rd) + "</td></tr>")
    return "<div class='gl-wrap'><table class='gl-t'>" + head + body + "</table></div>"


def render_glossary():
    total = sum(len(rows) for _n, rows in _SECTIONS)
    cards = "".join(
        "<div class='gl-card' style='--c:" + c + "'><div class='k'>" + k + "</div><div class='q'>" + q + "</div><div class='a'>" + a + "</div></div>"
        for k, q, a, c in _CORE)
    st.markdown(
        _CSS
        + "<div class='gl-strip'><span>&gt; CODEX.DB</span><span>ENTRIES <b>" + str(total) + "</b></span>"
        "<span>SECTORS <b>" + str(len(_SECTIONS)) + "</b></span><span>STATUS <b>ONLINE</b><i class='gl-cur'></i></span></div>"
        "<div class='section-label'>4 ตัวที่ต้องจำให้แม่น</div><div class='gl-core'>" + cards + "</div>"
        "<div class='gl-box'><b>ลำดับใช้จริง</b><br><span class='flow'>"
        "VIX (ตลาดเป็นไง) → RSI (ตัวไหนลงแรง) → เช็คบริษัท (ดีไหม · แพงไหม · มีแรงไหม) → ATR (ตั้งจุดตัดขาดทุนตรงไหน) → R (เสียได้เท่าไหร่)</span><br><br>"
        "<b>3 ข้อที่ต้องจำ</b><br>"
        "1. เกณฑ์เป็นกฎคร่าวๆ ไม่ใช่ตายตัว<br>"
        "2. ตัวเลขตัวเดียวตัดสินไม่ได้ ดูภาพรวม<br>"
        "3. ตัวเลขสองตัวขัดกัน = ยังสรุปไม่ได้ (เช่น PEG ถูกแต่ DCF แพง)<br><br>"
        "ไม่ต้องจำคำอังกฤษ ถ้าอ่านภาษาไทยในเว็บแล้วเข้าใจ</div>"
        "<div class='section-label'>ค้นคำ</div>",
        unsafe_allow_html=True,
    )
    q = st.text_input("🔎 ค้นคำ (พิมพ์ เช่น RSI, หนี้, แพง)", key="gl_q", placeholder="พิมพ์คำที่อยากรู้ความหมาย", label_visibility="collapsed").strip().lower()
    if q:
        hits = []
        for si, (name, rows) in enumerate(_SECTIONS):
            for t, m, rd in rows:
                if q in (t + " " + m + " " + rd).lower():
                    hits.append((name.split(" · ")[0] + " · " + name.split(" · ")[1], si, t, m, rd))
        if hits:
            st.markdown(_table(hits, with_group=True) + "<div class='gl-foot'>MATCH " + str(len(hits)) + " ENTRIES</div>", unsafe_allow_html=True)
        else:
            st.caption("ไม่เจอคำนี้ ลองพิมพ์คำสั้นลง หรือล้างช่องค้นหาเพื่อดูทุกหมวด")
        return
    tabs = st.tabs([n.split(" · ")[0] + " " + n.split(" · ")[1] for n, _ in _SECTIONS])
    for si, (tab, (_, rows)) in enumerate(zip(tabs, _SECTIONS)):
        with tab:
            st.markdown(_table([(si,) + tuple(r) for r in rows]) + "<div class='gl-foot'>" + str(len(rows)) + " ENTRIES</div>", unsafe_allow_html=True)
    st.caption("เกณฑ์ทั้งหมดเป็นแนวทางคร่าวๆ เพื่อการเรียนรู้ ไม่ใช่คำแนะนำซื้อขาย")