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
    Künstliche Intelligenzen werden heutzutage für nahezu alles eingesetzt, Jeder kann sich einen Text, Bilder oder 
    sogar Videos erzeugen lassen.
    Ein nächster Logischer Schritt wäre es, eine KI auch für das raten für Passwörter einzusetzen. 
    Dieses Projekt macht genau das.\\
    \\
    Hierzu wurde ein *Generative Adversarial Network* (GAN) verwendet, um aus einer gegebenen Liste, der `rockyou.txt`, 
    neue Passwörter zu generieren.
    Um die KI bewerten zu können, wurde sie mit dem Programm Hashcat verglichen. 
    Hashcat ist ein sehr verbreitetes Programm, dass primär zur erstellung und knacken von Passwörtern eingesetzt wird.\\
    \\
    Als Angriffsziel wurde eine veröffentlichte Datei von LinkedIn verwendet.
    In ihr stehen ca. 60 Millionen Passwörter.\
    """,
    unsafe_allow_html=True
)
if st.button("Woher stammt die LinkedIn und RockYou Liste?"):
    switch_page("Linkedin & RockYou Leak")
st.divider()

st.markdown(
    """
    ## Was ist Hashcat und PassGAN? 
    Hier wird das Open-Source Tool Hashcat und PassGAN erklärt. Es gibt zu jedem Programm eine kurze Definition und 
    Erklärung, wie die beiden Programme eigentlich funktionieren.
    """
)

col7, col8 = st.columns(2)

if col7.button("Funktionsweise GAN"):
    switch_page("Funktionsweise GAN")
if col8.button("Funktionsweise Hashcat"):
    switch_page("Funktionsweise Hashcat")

st.divider()
st.markdown(
    """
    ## Vergleich zwischen Hashcat und PassGAN
    In diesem Abschnitt sind die Ergebnisse dieser Projektarbeit. Es wird Hashcat und PassGAN verglichen. Für diese 
    Ergebnisse wurde die Künstliche Intelligenz bis zur bestmöglichen Qualität trainiert. Es wurde PassGAN mit 
    der von uns erweiterten Top 10 Liste verglichen.
    """
)

if st.button("KI 200k vs. Hashcat Top 17"):
    switch_page("KI 200k vs. Hashcat Top 17")

st.divider()


st.markdown(
    """
    ## Mehr Daten!
    Hier sind alle Daten für sich zu finden, ohne mit anderen Verglichen zu werden. Außerdem wird hier die 
    Trainingsdatei `rockyou.txt` und die Datei, die Angegriffen wurde, gezeigt und beschrieben. 
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

col4, col5, col6 = st.columns(3)
if col4.button("Hashcat 17 Regeln"):
    switch_page("Hashcat 17 Regeln")
if col5.button("Hashcat Best 64 Regel"):
    switch_page("Hashcat Best 64 Regel")
if col6.button("Rockyou Datei"):
    switch_page("Rockyou Datei")
