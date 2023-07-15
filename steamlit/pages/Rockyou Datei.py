import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Rockyou Datei",
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

st.write("# Rockyou Datei👋")

image = "steamlit/images/crackedpw_train_cut_cracktime.jpg"
st.image(image, caption='Cracktime')

image = "steamlit/images/crackedpw_train_cut_pw_complexity.jpg"
st.image(image, caption='Passwortkomplexität')

image = "steamlit/images/crackedpw_train_cut_normalverteilung_passwortlänge.jpg"
st.image(image, caption='Passwortlänge')

image = "steamlit/images/crackedpw_train_cut_percentage_distribution_of_letters.jpg"
st.image(image, "Verteilung der Zeichen")

if st.button("Zurück"):
    switch_page("hello")
