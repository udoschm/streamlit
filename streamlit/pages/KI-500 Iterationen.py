import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI 500 000 Iterationen",
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
    KI 500 000 Iterationen ⚙️
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
    | Geknackte Passwörter                   | 2 329 527 (3,85%) |

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
    Auf dieser Seite werden die Ergebnisse der Künstlichen Intelligenz mit 500 Tausend Iterationen thematisiert.
    In den folgenden Absätzen wird der Begriff Entropie angesprochen, dies ist ein Wert, welcher 
    die Stärke eines Passwortes definiert. Um so höher Entropie-Wert ist, desto sicherer ist ein Passwort.
    Der Passwortmanager KeePass stuft die Sicherheit der Passwörter wie folgt ein (siehe linke Tabelle).
"""
)


col7, col8 = st.columns(2)

image = "streamlit/images/500k/500k_utf-8_repair_pw_complexity.jpg"
col7.image(image, caption='Passwortkomplexität aller Passwörter in der generierten Liste', use_column_width=True)

col8.markdown(
    """
In der dieser Abbildung ist die Passwortkomplexität der generierten Passwortliste in Entropie-Bits dargestellt.
Es ist sehr deutlich zu sehen, dass die generierten Passwörter eine sehr schwache Entropie aufweisen, 50,49% aller 
Passwörter besitzen eine Entropie von unter 20. 32,72% der Passwörter weisen eine Entropie von unter 30 Entropie-Bits auf.
Passwörter mit einer Entropie von mehr als 80 existieren nicht.
"""
)

col9, col10 = st.columns(2)

image = "streamlit/images/500k/crackedpw_ai_500k_cut_repair_pw_complexity.jpg"
col9.image(image, caption='Passwortkomplexität der geknackten Passwörter', use_column_width=True)

col10.markdown(
    """ 
Dies spiegelt sich auch im Ergebnis wider, 74,18% der geknackten Passwörter besitzt eine Entropie von unter 20.
Es werden keine Passwörter mit einer Entropie von über 50 gefunden.
Bei den Ergebnissen der KI mit 200 und 750 Tausend Iterationen zeichnet sich ein ähnliches Bild ab.
Man kann also festhalten, dass die KI mit 500 000 Iterationen hauptsächlich sehr schwache Passwörter gefunden hat.
"""
)

col11, col12 = st.columns(2)

image = "streamlit/images/500k/500k_utf-8_repair_normalverteilung_passwortlänge.jpg"
col11.image(image, caption='Verteilung der Passwortlänge in der Hashcat generierten Liste', use_column_width=True)

col12.markdown(
    """    
Die Ergebnisse aus der Entropie lassen sich auch aus der Längenverteilung ableiten, auch hier sieht man das die 
Künstliche Intelligenz hauptsächlich kurze Passwörter generiert hat.
Der Grund hierfür ist die Input-Datei, welche die 'rockyou.txt' war. Diese besitzt eine ähnliche Verteilung.
"""
)



col13, col14 = st.columns(2)

image = "streamlit/images/500k/crackedpw_ai_500k_cut_repair_normalverteilung_passwortlänge.jpg"
col13.image(image, caption='Verteilung der Passwortlänge der geknackten Passwörter', use_column_width=True)

col14.markdown(
    """
Diese Abbildung zeigt die Längenverteilung der Ergebnisse, welche die KI erzielt hat, auf.
Man kann festhalten das fast ausschließlich Passwörter der Länge 6 - 9 und einige wenige der Länge 10 oder mehr gefunden
wurden. Da die Datei, welche zum Cracken benutzt, wurde schon eine ähnliche Verteilung ausweist, ist dieses Ergebnis 
nicht verwunderlich.
"""
)

col15, col16 = st.columns(2)
col17, col18 = st.columns(2)

if col15.button("Ab zur KI mit 750k Iterationen"):
    switch_page("KI-750 Iterationen")
if col17.button("Zurück"):
    switch_page("Home")


