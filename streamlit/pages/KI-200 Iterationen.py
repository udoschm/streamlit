import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI 200 000 Iterationen",
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

st.markdown(
    """
    <h1 style='text-align: center;'>
    KI 200 000 Iterationen 🤖
    </h1>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns(2)
# Picture and Text
st.markdown(
    """
    <div align="center">

    | Anzahl der Passwörter in der Zieldatei | 26 067 879        |
    |----------------------------------------|-------------------|
    | Geknackte Passwörter                   | 2 342 307 (3.87%) |

    </div><br><br><br>
    """,
    unsafe_allow_html=True
)


col5, col6 = st.columns(2)


col5.markdown(
"""    
    <div align="center">

    | Entropie in Bits | Stärke       |
    |------------------|--------------|
    | 0-64             | Sehr schwach |
    | 64-80            | Schwach      |
    | 80-112           | Mäßig        |
    | 112-128          | Stark        |
    | > 128            | Sehr Stark   |

    </div><br>
    """,
    unsafe_allow_html=True
)

col6.markdown(
    """
    Auf dieser Seite werden die Ergebnisse der Künstlichen Intelligenz mit 200 Tausend Iterationen thematisiert.
    Diese hat das beste Ergebnis bei den verschiedenen Iterationen geliefert.
    In den folgenden Absätzen wird der Begriff Entropie angesprochen, dies ist ein Wert, welcher 
    die Stärke eines Passwortes definiert. Umso höher Entropie-Wert ist, desto sicherer wird ein Passwort.
    Der Passwortmanager KeePass stuft die Sicherheit der Passwörter wie folgt ein (siehe linke Tabelle).
"""
)


col7, col8 = st.columns(2)

image = "streamlit/images/200k/200k_utf-8_repair_pw_complexity.jpg"
col7.image(image, caption='Passwortkomplexität aller Passwörter in der generierten Liste', use_column_width=True)

col8.markdown(
    """
In der dieser Abbildung ist die Passwortkomplexität der generierten Passwortliste in Entropie-Bits dargestellt.
Es ist sehr deutlich zu sehen, dass die generierten Passwörter eine sehr schwache Entropie aufweisen, 53,20% aller 
Passwörter besitzt eine Entropie von unter 20.
"""
)

col9, col10 = st.columns(2)

image = "streamlit/images/200k/crackedpw_ai_200k_cut_repair_pw_complexity.jpg"
col9.image(image, caption='Passwortkomplexität der geknackten Passwörter', use_column_width=True)

col10.markdown(
    """ 
Dies spiegelt sich auch im Ergebnis wider, 77,27% der geknackten Passwörter besitzen eine Entropie von unter 20.
Es werden keine Passwörter mit einer Entropie von über 40 gefunden.
Man kann also festhalten, dass die KI mit 200 000 Iterationen hauptsächlich sehr schwache Passwörter gefunden hat.
"""
)

col11, col12 = st.columns(2)

image = "streamlit/images/200k/200k_utf-8_repair_normalverteilung_passwortlänge.jpg"
col11.image(image, caption='Verteilung der Passwortlänge in der Hashcat generierten Liste', use_column_width=True)

col12.markdown(
    """    
Die Ergebnisse aus der Entropie lassen sich auch aus der Längenverteilung ableiten, auch hier sieht man das die 
Künstliche Intelligenz hauptsächlich kurze Passwörter generiert hat.
Der Grund hierfür ist die Input-Datei, welche die 'rockyou.txt' war. Diese besitzt eine ähnliche Verteilung.
"""
)



col13, col14 = st.columns(2)

image = "streamlit/images/200k/crackedpw_ai_200k_cut_repair_normalverteilung_passwortlänge.jpg"
col13.image(image, caption='Verteilung der Passwortlänge der geknackten Passwörter', use_column_width=True)

col14.markdown(
    """
Diese Abbildung zeigt die Längenverteilung der Ergebnisse, welche die KI in der LinkedIN Datei gefunden hat.
Man kann festhalten das fast ausschließlich Passwörter der Länge 6 - 9 und einige wenige der Länge 10 oder mehr gefunden
worden sind. Da die Datei, welche zum Cracken benutzt wurde, eine ähnliche Verteilung aufweist, ist diese Verteilung 
nicht verwunderlich.
"""
)

col15, col16 = st.columns(2)
col17, col18 = st.columns(2)

if col15.button("Ab zur KI mit 500k Iterationen"):
    switch_page("KI-500 Iterationen")
if col17.button("Zurück"):
    switch_page("Home")


