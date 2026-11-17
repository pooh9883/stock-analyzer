# -*- coding: utf-8 -*-
"""STAGE · จัดหุ้นเข้า 4 ช่วงวัฏจักรตามแนวคิดของ Stan Weinstein
ใช้เส้นค่าเฉลี่ย 30 สัปดาห์ (ประมาณ 150 วันทำการ) ดูว่าราคาอยู่เหนือ/ใต้เส้น และเส้นชี้ขึ้น/ลง/แบน

  Stage 1  พักฐาน        เส้นแบน ราคาวนอยู่รอบเส้น หลังลงมานาน
  Stage 2  ขาขึ้น        ราคาเหนือเส้น และเส้นชี้ขึ้น
  Stage 3  ใกล้ยอด       เส้นแบน/เริ่มโค้งลง ราคาแกว่งข้าง หลังขึ้นมานาน
  Stage 4  ขาลง          ราคาใต้เส้น และเส้นชี้ลง

หมายเหตุ: นี่คือกฎหัวแม่มือ ไม่ใช่สูตรตายตัว · แยก Stage 1 กับ Stage 3 ได้แค่ประมาณ
(เส้นแบนทั้งคู่ ต้องดูว่าก่อนหน้านั้นขึ้นมาหรือลงมา) จึงติดป้าย "ประมาณการ" ในหน้าจอ
ไฟล์นี้เป็น pandas ล้วน ไม่พึ่ง streamlit ทดสอบแยกได้"""
import numpy as np
import pandas as pd

MA_DAYS = 150          # 30 สัปดาห์ × 5 วันทำการ
SLOPE_BACK = 20        # เทียบเส้นเมื่อ 20 วันทำการก่อน (ราว 1 เดือน)
FLAT = 1.0             # เส้นเปลี่ยนไม่เกิน ±1% ใน 1 เดือน = "แบน"
EXT_EARLY = 15.0       # ห่างเส้นไม่เกิน 15% = ช่วงต้นของ Stage 2
EXT_FAR = 30.0         # ห่างเส้นเกิน 30% = วิ่งไกลแล้ว

NAMES = {1: "พักฐาน", 2: "ขาขึ้น", 3: "ใกล้ยอด", 4: "ขาลง"}
COLORS = {1: "#7d86a6", 2: "#19f5a5", 3: "#ff9f43", 4: "#ff2a6d"}


def classify(close, volume=None):
    """close/volume = pandas Series รายวันของหุ้น 1 ตัว · คืน dict หรือ None ถ้าข้อมูลไม่พอ"""
    c = pd.Series(close).dropna().astype(float)
    n = len(c)
    if n < MA_DAYS + SLOPE_BACK + 5:
        return None
    ma = c.rolling(MA_DAYS).mean()
    ma_now = float(ma.iloc[-1])
    ma_prev = float(ma.iloc[-1 - SLOPE_BACK])
    if not (ma_now > 0 and ma_prev > 0):
        return None
    px = float(c.iloc[-1])
    slope = (ma_now / ma_prev - 1) * 100            # เส้นเปลี่ยนกี่ % ในรอบ 1 เดือน
    ext = (px / ma_now - 1) * 100                   # ราคาห่างเส้นกี่ %
    above = px > ma_now

    # ก่อนหน้านั้นเส้นขึ้นมาหรือลงมา (เทียบเส้นเมื่อ ~3 เดือนก่อน) + ตำแหน่งในช่วงสูง-ต่ำ 1 ปี
    long_slope = None
    if n >= MA_DAYS + 65 and not np.isnan(ma.iloc[-1 - 63]):
        long_slope = (ma_now / float(ma.iloc[-1 - 63]) - 1) * 100
    win = c.iloc[-252:]
    lo, hi = float(win.min()), float(win.max())
    pos52 = (px - lo) / (hi - lo) if hi > lo else 0.5
    came_up = (long_slope > 0) if long_slope is not None else (pos52 >= 0.5)

    approx = False
    if above and slope > FLAT:
        stage = 2
    elif (not above) and slope < -FLAT:
        stage = 4
    else:
        # เส้นแบน หรือราคากับเส้นขัดกัน → แยก 1 กับ 3 จากทิศทางก่อนหน้า (ประมาณการ)
        stage = 3 if came_up else 1
        approx = True

    # เกาะอยู่เหนือเส้นมากี่วันติดต่อกัน
    age = 0
    for v, m in zip(c.iloc[::-1].values, ma.iloc[::-1].values):
        if np.isnan(m) or v <= m:
            break
        age += 1
        if age >= 250:
            break

    vr = None
    if volume is not None:
        v = pd.Series(volume).reindex(c.index).fillna(0)
        if len(v) >= 90 and float(v.tail(90).mean()) > 0:
            vr = float(v.tail(20).mean()) / float(v.tail(90).mean())

    if stage == 2:
        sub = "early" if ext <= EXT_EARLY else ("mid" if ext <= EXT_FAR else "far")
    else:
        sub = None
    return {"stage": stage, "sub": sub, "ext": ext, "slope": slope, "ma": ma_now, "px": px,
            "age": age, "vol_ratio": vr, "approx": approx, "pos52": pos52}


def label(s):
    """(ข้อความสั้นสำหรับป้าย, สี)"""
    if not s:
        return "ไม่ทราบช่วง", "#7d86a6"
    st_ = s["stage"]
    txt = "STAGE %d · %s" % (st_, NAMES[st_])
    if st_ == 2:
        txt += {"early": " · ช่วงต้น", "mid": " · ช่วงกลาง", "far": " · วิ่งไกลแล้ว"}[s["sub"]]
    col = COLORS[st_]
    if st_ == 2 and s["sub"] == "far":
        col = "#ff9f43"
    return txt, col


def advice(s):
    """คำแนะนำแนวคิดตามช่วง (ไม่ใช่คำสั่งซื้อขาย) เป็นภาษาง่ายๆ"""
    if not s:
        return ""
    st_ = s["stage"]
    if st_ == 2:
        if s["sub"] == "early":
            return "ขาขึ้นช่วงต้น ราคายังอยู่ใกล้เส้น เป็นช่วงที่แนวคิดนี้มองว่าน่าสนใจที่สุด · ทยอยเข้าตามแผน ตั้งจุดตัดขาดทุนก่อนเสมอ"
        if s["sub"] == "mid":
            return "ขาขึ้นช่วงกลาง ราคาเริ่มห่างเส้น · ทยอยเข้าได้แต่อย่าไล่ ถ้ารอให้ย่อใกล้เส้นจะได้ราคาดีกว่า"
        return "ขาขึ้นแต่วิ่งไกลจากเส้นแล้ว (ห่างเกิน 30%) · รอย่อก่อน ไม่ไล่ราคา เพราะจุดตัดขาดทุนจะอยู่ไกลและเสี่ยงมาก"
    if st_ == 1:
        return "พักฐาน ยังไม่เห็นขาขึ้นชัด · เฝ้าดูได้ ถ้าจะลองลงก็ไม้เล็กมาก"
    if st_ == 3:
        return "ใกล้ยอด/แกว่งข้าง · ถือได้แต่ไม่ควรเติม และควรเตรียมจุดตัดขาดทุนหรือเลื่อนจุดตัดขาดทุนขึ้น"
    return "ขาลง · แนวคิดนี้ไม่แนะนำให้เข้าหรือถือระยะยาว"
