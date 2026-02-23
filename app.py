import streamlit as st
from ui import init_state, render_sidebar, render_scene


def main():
    st.set_page_config(
        page_title="Birthday Quest 🎂",
        page_icon="🎂",
        layout="centered",
    )

    init_state()

    st.title("🎂 Birthday Quest")

    render_sidebar()
    render_scene()


if __name__ == "__main__":
    main()