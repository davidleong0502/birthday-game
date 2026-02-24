import streamlit as st
from content import build_scenes
from game import Game, Player
import os


PHOTOS = [
    "assets/photo1.jpg",
    "assets/photo2.jpg",
    "assets/photo3.jpg",
    "assets/photo4.jpg",
]


def inject_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Lato:wght@300;400;700&display=swap');

    .stApp {
        background-color: #fdf6ee !important;
    }

    .block-container {
        background-color: #fdf6ee !important;
        padding-top: 2rem !important;
    }

    .stApp, .stApp p, .stApp div, .stApp span, .stApp label {
        color: #3d2b1f !important;
        font-family: 'Lato', sans-serif !important;
    }

    .stApp h1 {
        font-family: 'Playfair Display', serif !important;
        color: #c4714f !important;
        text-align: center !important;
        font-size: 2.8rem !important;
    }

    .stApp h2, .stApp h3 {
        font-family: 'Playfair Display', serif !important;
        color: #6b4c38 !important;
    }

    .stButton button {
        background-color: #c4714f !important;
        color: #fdf6ee !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Lato', sans-serif !important;
        font-weight: 700 !important;
        padding: 0.6rem 1.2rem !important;
        transition: background-color 0.2s !important;
    }

    .stButton button:hover {
        background-color: #d4845f !important;
    }

    [data-testid="stSidebar"] {
        background-color: #f5ead8 !important;
        border-right: 1px solid #dcc9b0 !important;
    }

    [data-testid="stSidebar"] .stButton button {
        background-color: #eedfc8 !important;
        color: #6b4c38 !important;
        border: 1px solid #dcc9b0 !important;
    }

    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #dcc9b0 !important;
    }

    .stProgress > div > div > div {
        background-color: #c4714f !important;
    }

    .stProgress > div > div {
        background-color: #dcc9b0 !important;
    }

    [data-testid="stMetricValue"] {
        color: #c4714f !important;
        font-family: 'Playfair Display', serif !important;
        font-size: 2rem !important;
    }

    [data-testid="stMetricLabel"] {
        color: #7a5c48 !important;
    }

    .stAlert {
        border-radius: 10px !important;
        background-color: #eedfc8 !important;
        color: #3d2b1f !important;
        border: none !important;
        border-left: 3px solid #c9a98a !important;
    }

    .stImage img {
        border-radius: 16px !important;
        box-shadow: 0 8px 32px rgba(107,76,56,0.15) !important;
        border: 2px solid #e8d5bf !important;
    }

    hr {
        border-color: #dcc9b0 !important;
    }

    #MainMenu, footer, header {
        visibility: hidden !important;
    }
    </style>
    """, unsafe_allow_html=True)


def init_state():
    if "gf_name" not in st.session_state:
        st.session_state.gf_name = "Bubba"
    if "player" not in st.session_state:
        st.session_state.player = Player()
    if "game" not in st.session_state:
        st.session_state.game = Game(
            build_scenes(st.session_state.gf_name), start_id="start"
        )
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""
    if "final_message" not in st.session_state:
        st.session_state.final_message = ""


def reset_game():
    st.session_state.player = Player()
    st.session_state.game = Game(
        build_scenes(st.session_state.gf_name), start_id="start"
    )
    st.session_state.feedback = ""
    st.session_state.final_message = ""


def render_sidebar():
    with st.sidebar:
        st.header("Bubba's Quest")

        if st.button("Reset game"):
            reset_game()
            st.rerun()

        st.divider()
        st.subheader("Progress")

        pts = st.session_state.player.inv.get("bubba_points", 0)
        st.metric("Bubba points", f"{pts} / 3")
        st.progress(min(pts / 3, 1.0))

        inv = {k: v for k, v in st.session_state.player.inv.items() if k != "bubba_points"}
        if inv:
            st.subheader("Tokens")
            for k, v in inv.items():
                st.write(f"{k}: {v}")

        st.divider()
        if st.session_state.game.can_go_back():
            if st.button("Back"):
                st.session_state.game.go_back()
                st.session_state.feedback = ""
                st.rerun()


def render_scene():
    scene = st.session_state.game.cur_scene()

    st.subheader(scene.title)
    st.write(scene.text)

    if scene.id == "final":
        st.divider()
        # Photo gallery
        available = [p for p in PHOTOS if os.path.exists(p)]
        if available:
            cols = st.columns(2)
            for col, photo in zip(cols, available):
                with col:
                    st.image(photo, use_container_width=True)
        st.divider()

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(scene.a.label, use_container_width=True, key="btn_a"):
            st.session_state.feedback = st.session_state.game.move(
                st.session_state.player, scene.a
            )
            st.rerun()
    with col2:
        if st.button(scene.b.label, use_container_width=True, key="btn_b"):
            st.session_state.feedback = st.session_state.game.move(
                st.session_state.player, scene.b
            )
            st.rerun()


def run():
    st.set_page_config(
        page_title="Birthday Quest",
        page_icon="🎂",
        layout="centered",
    )
    inject_styles()
    init_state()

    st.title("Birthday Quest")
    st.markdown(
        "<p style='text-align:center; color:#c9a98a; font-size:0.95rem; "
        "margin-top:-0.8rem; font-family: Lato, sans-serif; letter-spacing: 2px;'>"
        "a little something for Sern</p>",
        unsafe_allow_html=True,
    )

    render_sidebar()
    render_scene()
