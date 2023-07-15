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

st.markdown(
    """
    Die Rockyou Datei wurde als Basis für die KI und die Hashcat-Regeln benutzt.\
    Die Datei alleine konnte bereits 4,85% der Passwörter knacken.\
    
    <center>| Enthaltene Passwörter | 26 067 879         |
    |-----------------------|--------------------|
    | Gecrackte Passwörter  | 2 937 754 (4.85%)  | <\center>
   
    
    """
)

st.markdown(
    """
    Die folgenden Diagramme beziehen sich auf die Passwörter, welche durch die Liste geknackt worden sind.
    """
)

image = "steamlit/images/crackedpw_train_cut_cracktime.jpg"
st.image(image, caption='Cracktime')

st.markdown(
    """Man kann anhand der Cracktime erkennen, das hauptsächlich Passwörter gecrackt worden sind, welche eine 
    niedrige Cracktime besitzen. Dies hängt damit zusammen, das die Passwörter relativ kurz sind. Die meisten 
    Passwörter haben 6 Zeichen. Daraus lässt sich wiederrum eine niedirge Entropie ableiten. Des weiteren beinhalteten 
    die passwörter hauptsächlich Kleinbuchstaben und Zahlen."""
)

image = "steamlit/images/crackedpw_train_cut_pw_complexity.jpg"
st.image(image, caption='Passwortkomplexität')

st.markdown(
    """
    Hallo! Ich bin Text!
    """
)

image = "steamlit/images/crackedpw_train_cut_normalverteilung_passwortlänge.jpg"
st.image(image, caption='Passwortlänge')

st.markdown(
    """
    Hallo! Ich bin Text!
    """
)

image = "steamlit/images/crackedpw_train_cut_percentage_distribution_of_letters.jpg"
st.image(image, "Verteilung der Zeichen")

if st.button("Zurück"):
    switch_page("hello")
