# -*- coding: utf-8 -*-
"""
watchlist.py  [watchlist v1]
============================
Watchlist กลาง: แก้ที่หน้าสแกนเนอร์ที่เดียว ทุกหน้า (สแกนเนอร์ / เทียบหุ้น / ปฏิทิน / เรดาร์ข่าว) ดึงไปใช้
บันทึกลงไฟล์ watchlist.json (ไฟล์เดียวกับที่สแกนเนอร์เคยใช้) จึงอยู่ข้ามการรีสตาร์ท
"""
import streamlit as st

import rocket_ui


def _init():
    if "wl_list" not in st.session_state:
        st.session_state["wl_list"] = rocket_ui._load_watch()[: rocket_ui.MAX_SYMBOLS]
    if "wl_text" not in st.session_state:
        st.session_state["wl_text"] = ", ".join(st.session_state["wl_list"])
    st.session_state["rk_text"] = ", ".join(st.session_state["wl_list"])  # ให้โค้ดเดิมที่อ่าน rk_text ได้ค่าตรงกัน


def get() -> list:
    """รายชื่อหุ้นใน Watchlist กลาง"""
    _init()
    return list(st.session_state["wl_list"])


def _sync():
    syms = rocket_ui._parse(st.session_state.get("wl_text", ""))[: rocket_ui.MAX_SYMBOLS]
    st.session_state["wl_list"] = syms
    st.session_state["rk_text"] = ", ".join(syms)
    if syms:
        rocket_ui._save_watch(syms)


def _reset():
    import rocket
    st.session_state["wl_text"] = ", ".join(rocket.DEFAULT_WATCHLIST)
    _sync()


def _submit():
    _sync()


def sidebar():
    """กล่องแก้ Watchlist ในแถบข้าง (เรียกใน with st.sidebar:) — ใช้ฟอร์ม พิมพ์ได้อิสระ กด 💾 ค่อยบันทึก"""
    _init()
    st.markdown("**⭐ Watchlist ของฉัน**")
    with st.form("wl_form", border=False):
        st.text_area("รายชื่อหุ้น", key="wl_text", height=90, label_visibility="collapsed",
                     placeholder="เช่น NVDA, AAPL, SNDK")
        st.form_submit_button("💾 บันทึกรายชื่อ", on_click=_submit, use_container_width=True)
    n = len(st.session_state["wl_list"])
    st.caption(f"{n} ตัว · ใช้ร่วมกันทุกหน้า · พิมพ์แก้ได้เลย (คั่นด้วยจุลภาคหรือเว้นวรรค) แล้วกด 💾 บันทึกรายชื่อ")
    st.button("↺ รายชื่อตั้งต้น", key="wl_reset", on_click=_reset)


def editor():
    """ช่องแก้ Watchlist ในหน้าสแกนเนอร์ (ซ่อนในกล่องพับ) — กด 💾 บันทึกแล้วทุกหน้าใช้รายชื่อใหม่"""
    _init()
    with st.expander("✏️ แก้ไขรายชื่อหุ้น (เพิ่ม / ลบ)", expanded=False):
        with st.form("wl_form", border=False):
            st.text_area("รายชื่อหุ้น", key="wl_text", height=90, label_visibility="collapsed",
                         placeholder="เช่น NVDA, AAPL, SNDK  (คั่นด้วยจุลภาคหรือเว้นวรรค)")
            c1, c2 = st.columns([1, 1])
            c1.form_submit_button("💾 บันทึกรายชื่อ", on_click=_submit, use_container_width=True)
            c2.form_submit_button("↺ รายชื่อตั้งต้น", on_click=_reset, use_container_width=True)


def chips(symbols=None) -> str:
    """HTML แสดงรายชื่อเป็นป้ายเล็กๆ"""
    syms = symbols if symbols is not None else get()
    if not syms:
        return ""
    return "".join(
        f'<span style="display:inline-block;margin:0 6px 6px 0;padding:1px 8px;border:1px solid #00f0ff55;'
        f'color:#fcee0a;font-family:monospace;font-weight:700;font-size:.85rem">{s}</span>' for s in syms)