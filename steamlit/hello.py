import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# KI-Passwortfracking Analyse 👋")

st.markdown(
    """
    In diesem Projekt geht es um lalala
    """
)
if st.button("KI-200-Interrationen"):
    switch_page("KI-200 Iterationen")
if st.button("KI-500-Interrationen"):
    switch_page("KI-500 Iterationen")
if st.button("KI-750-Interrationen"):
    switch_page("KI-750 Iterationen")
if st.button("Hashcat 17 Regeln"):
    switch_page("Hashcat 17 Regeln")
if st.button("Hashcat Best 64 Regel"):
    switch_page("Hashcat Best 64 Regel")
if st.button("Rockyou Datei"):
    switch_page("Rockyou Datei")
