import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="RockYou Datei",
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
    RockYou Datei 👻
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
    | Geknackte Passwörter                   | 2 937 754 (4.85%) |

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
    """Die `rockyou.txt`-Datei wurde zum Trainieren der KI verwendet, als auch für die regelbasierten Angriffe bei 
    Hashcat. Es wurde deshalb überprüft, wie viele Passwörter diese Passwortliste ohne weitere Veränderungen knacken 
    kann. \n In den folgenden Absätzen wird der Begriff Entropie angesprochen, dies ist ein Wert welcher die Stärke 
    eines Passwortes definiert. Um so höher Entropie-Wert ist, um so sicherer wird ein Passwort angesehen. Der 
    Passwortmanager KeePass stuft die Sicherheit der Passwörter wie folgt ein (siehe linke Tabelle)."""
)

col7, col8 = st.columns(2)

image = "steamlit/images/rockyou/train_utf-8_repair_pw_complexity.jpg"
col7.image(image, caption='Passwortkomplexität aller Passwörter in der generierten Liste', use_column_width=True)

col8.markdown(
    """
    Dieses Balkendiagramm zeigt die jeweilige Entropie, welche die Passwörter besitzen.
    Man kann erkennen, dass die RockYou-Datei viele Passwörter mit niedriger Entropie besitzt.
    Über 50% der Passwörter besitzen eine Entropie, welche kleiner 20 ist.
"""
)

col9, col10 = st.columns(2)

image = "steamlit/images/rockyou/crackedpw_train_cut_repair_pw_complexity.jpg"
col9.image(image, caption='Passwortkomplexität der geknackten Passwörter', use_column_width=True)

col10.markdown(
    """ 
Wir gehen nun zur Verteilung über, welche die Passwörter beinhaltet, die die RockYou-Datei geschafft hat zu cracken.
Auch diese Verteilung ist ähnlich zu der kompletten Liste. Fast 50% der Passwörter, die gefunden wurden, besitzt eine 
Entropie, welche kleiner ist als 20. Über 35% der Passwörter besitzen eine Entropie kleiner 40.
Insgesamt hat die RockYou-Liste 4,85% aller Passwörter, welche in dem LinkedIn-Leak enthalten sind, geschafft zu knacken.

"""
)

col11, col12 = st.columns(2)

image = "steamlit/images/rockyou/train_utf-8_repair_normalverteilung_passwortlänge.jpg"
col11.image(image, caption='Verteilung der Passwortlänge in der Hashcat generierten Liste', use_column_width=True)

col12.markdown(
    """    
In dieser Abbildung ist die Längenverteilung der kompletten 'rockyou.txt'-Datei zu sehen.
Man kann erkennen, dass sich die RockYou-Liste sich hauptsächlich auf kürzere Passwörter konzentriert.
Lediglich 9,13% der Passwörter sind länger als 10 Zeichen.
"""
)

col13, col14 = st.columns(2)

image = "steamlit/images/rockyou/crackedpw_train_cut_repair_normalverteilung_passwortlänge.jpg"
col13.image(image, caption='Verteilung der Passwortlänge der geknackten Passwörter', use_column_width=True)

col14.markdown(
    """
    Es ist hier die Verteilung der Passwörter dargestellt, welche mithilfe der RockYou-Datei geknackt werden konnten.
    Wenn man das Diagramm, mit dem der kompletten Liste vergleicht, sieht man, dass die Längenverteilung sehr ähnlich ist.

"""
)

col15, col16 = st.columns(2)
col17, col18 = st.columns(2)

if col15.button("Was ist der RockYou Leak?"):
    switch_page("Linkedin & RockYou Leak")
if col17.button("Zurück"):
    switch_page("Home")

