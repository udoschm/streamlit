import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(
    page_title="LinkedIn & RockYou",
    page_icon="📈",
    initial_sidebar_state="collapsed",
    layout="wide"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


col1, col2 = st.columns(2)

col1.write("# Linkedin Leak 👨‍💼")
col1.markdown(
    """
    | Enthaltene Passwörter | 60 524  310 |
    |-----------------------|------------|
    <br>
    """,
    unsafe_allow_html=True
)


col1.markdown(
    """
    Die Linkedin Leak Liste wird in diesem Projekt als "Angriffsziel" verwendet. Hierfür wurden alle Passwörter mit dem 
    Hashalgorithmus SHA256 gehasht. Damit wurde ein realistischeres Szenario erzeugt werden. Sie enthält rund 60 
    Millionen Passwörter. LinkedIn ist eine Online-Plattform, die sich auf berufliche Netzwerke und Karriereentwicklung 
    spezialisiert hat.\\
    In der folgenden Grafik ist die Längenverteilung der Passwörter des LinkedIn Leaks zu sehen. 
    """
)


col2.write("# RockYou Leak 🤘")
col2.markdown(
    """
    | Enthaltene Passwörter | 26 067 879 |
    |-----------------------|------------|
    <br>
    """,
    unsafe_allow_html=True
)
col2.markdown(
    """
    Das Unternehmen RockYou hatte im Dezember 2009 eine Datenpanne, bei der viele Passwörter offengelegt wurden.
    Diese Passwortliste wurde in diesem Projekt verwendet, um die Künstliche Intelligenz zu trainieren und mit Hashcat
    einen regelbasierten Angriff durchzuführen.
    In der folgenden Grafik kann die Verteilung der Passwortlängen entnommen werden. 
    
    """,
    unsafe_allow_html=True
)


col3, col4 = st.columns(2)

image = "streamlit/images/linkedin_rockyou/linkedin_pwlänge.jpg"
col3.image(image, caption='LinkedIn', use_column_width=True)

image = "streamlit/images/linkedin_rockyou/train_utf-8_repair_normalverteilung_passwortlänge.jpg"
col4.image(image, caption='RockYou', use_column_width=True)


if st.button("Zurück"):
    switch_page("Home")


st.divider()
st.markdown(
    """
    <style>
    body {
    font-size: 12px; 
    } 
    </style>
    <body>
    Quellen: <br>
    https://en.wikipedia.org/wiki/RockYou <br>
    https://github.com/d4ichi/PassGAN/releases <br>
    https://web.archive.org/web/20210113172612/https://www.hashes.org/leaks.php <br>
    hashes.org ist seit Anfang 2021 offline. Dieser Link führt zu der Wayback-Machine. Der Linkedin Leak ist unter ID 68
    zu finden, kann allerdings nicht heruntergeladen werden.
    </body>
    """,
    unsafe_allow_html=True
)
