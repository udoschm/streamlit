import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hashcat 17 Regeln",
    page_icon="📈",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Hashcat 17 Regeln 👋")

image = "images/68_linkedin_found_without_hashes_utf-8_repair_cracktime.jpg"
st.image(image, output_format="JPG")

if st.button("Zurück"):
    switch_page("hello")


