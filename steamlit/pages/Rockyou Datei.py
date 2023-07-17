import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(
    page_title="Rockyou Datei",
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
    rockyou.txt Datei👋
    </h1>
    """,
    unsafe_allow_html=True
)

# Picture and Text
col0, col99 = st.columns(2)

col0.markdown(
    """
    <div align="center">

    | Enthaltene Passwörter | 26 067 879         |
    |-----------------------|--------------------|
    | Gecrackte Passwörter  | 2 937 754 (4.85%)  |

    </div><br>
    """,
    unsafe_allow_html=True
)


col99.markdown(
    """
    In 2009 wurde eine Firma mit dem Namen RockYou gehackt und die dort hinterlegten Passwörter gestohlen. Das hätte 
    kein Problem dargestellt, wenn die Passwörter nicht im Klartext, also für jeden lesbar, gespeichert worden wären.\
    Diese Datei wurde im Verlauf dieses Projekts als Ausgangsdatei verwendet, heißt, die verwendete KI wurde an diesen
    Passwörtern trainiert. Auch Hashcat hat nur die `rockyou.txt` verwendet, um anhand von festgelegten Regeln eine neue
    Passwortliste zu erstellen.\
    Die Datei alleine konnte bereits 4,85% der Passwörter knacken.\
    """
)


# Picture and Text
col1, col2 = st.columns(2)

image = "steamlit/images/crackedpw_train_cut_cracktime.jpg"
col1.image(image, caption='Cracktime', use_column_width=True)

col2.markdown(
    """      
    Die folgenden Diagramme beziehen sich auf die Passwörter, welche durch die Liste geknackt worden sind.
    Man kann anhand der Cracktime erkennen, das hauptsächlich Passwörter gecrackt worden sind, welche eine 
    niedrige Cracktime besitzen. Dies hängt damit zusammen, das die Passwörter relativ kurz sind. Die meisten 
    Passwörter haben 6 Zeichen. Daraus lässt sich wiederrum eine niedirge Entropie ableiten. Des weiteren beinhalteten 
    die passwörter hauptsächlich Kleinbuchstaben und Zahlen.
    """
)


# Picture and Text
col3, col4 = st.columns(2)

image = "steamlit/images/crackedpw_train_cut_pw_complexity.jpg"
col3.image(image, caption='Passwortkomplexität', use_column_width=True)

col4.markdown(
    """
    Hallo! Ich bin Text!
    """
)

# Picture and Text
col5, col6 = st.columns(2)

image = "steamlit/images/crackedpw_train_cut_normalverteilung_passwortlänge.jpg"
col5.image(image, caption='Passwortlänge', use_column_width=True)

col6.markdown(
    """
    Hallo! Ich bin Text!
    """
)

# Picture and Text
col7, col8 = st.columns(2)

image = "steamlit/images/crackedpw_train_cut_percentage_distribution_of_letters.jpg"
col7.image(image, "Verteilung der Zeichen", use_column_width=True)

col8.markdown(
    """
    Hallo! Ich bin Text!
    """
)


if st.button("Zurück"):
    switch_page("hello")
