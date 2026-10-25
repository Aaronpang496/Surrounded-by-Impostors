from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hidden Impostor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("🚀 Hidden Impostor")

st.caption(
    "Choose Solo for you + 10 AI, "
    "or Two players for you + a friend + 9 AI."
)

game_file = Path(__file__).resolve().parent / "game.html"

if not game_file.is_file():
    st.error("game.html is missing. Add it beside app.py.")
    st.stop()

game_html = game_file.read_text(encoding="utf-8")

components.html(
    game_html,
    height=850,
    scrolling=False,
)

st.caption(
    "Keyboard controls: click inside the game first. "
    "Yellow uses WASD; Blue uses the arrow keys. "
    "Touch controls are also available."
)
