import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI-Passwortcracking",
    page_icon="🖥️",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Passwortcracking mit Hilfe von künstlicher Intelligenz 🖥️")

st.markdown(
    """
    Künstliche Intelligenzen werden heutzutage für nahezu alles eingesetzt. Jeder kann sich einen Text, Bilder
    oder sogar Videos erzeugen lassen.\\
    Der nächste logische Schritt wäre es, eine KI für das knacken von Passwörtern einzusetzen. Genau das macht
    dieses Projekt. Es verwendet eine KI, ein Generative Adversarial Network um genau zu sein um aus einer
    Passwortliste mehr sinvoll erzeugte Passwörter zu generieren.\\
    Um vergleichen zu können wie sinnvoll es ist für so eine Aufgabe eine KI zu verwenden, wird als Gegenspieler
    das sehr beim Passwortcracking verbreitete Tool Hashcat verwendet. Hashcat funktioniert fundamental anders
    als die KI. Anstatt sich an gegebenen Passwörtern zu trainieren, folgt es bestimmten Regeln, die im
    vorhinein festgelegt werden können. Das ist ein relativ simpler Ansatz, liefert aber in kürzester Zeit viele
    Passwörter.
    Die KI hat hat mit unterschiedlich vielen Iterationen, Passwortlisten generiert.
    Grundlage für die Generation war die Rockyou Passwortliste.
    Diese wurde auch für Hashcat benutzt, hier wurde einmal eine Regel mit 17 Regeln angewendet und einmal mit 64 Regeln.
    Das Angriffsziele war ein LinkedIN Leak.

    """
)

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


