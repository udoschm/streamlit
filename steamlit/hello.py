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
import streamlit as st

# Buttons nebeneinander anordnen
col1, col2, col3 = st.columns(3)

if col1.button("KI-200-Iterationen"):
    switch_page("KI-200 Iterationen")
if col2.button("KI-500-Iterationen"):
    switch_page("KI-500 Iterationen")
if col3.button("KI-750-Iterationen"):
    switch_page("KI-750 Iterationen")

# Weitere Buttons hinzufügen
col4, col5, col6 = st.columns(3)

if col4.button("Hashcat 17 Regeln"):
    switch_page("Hashcat 17 Regeln")
if col5.button("Hashcat Best 64 Regel"):
    switch_page("Hashcat Best 64 Regel")
if col6.button("Rockyou Datei"):
    switch_page("Rockyou Datei")


