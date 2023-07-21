import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hashcat best64 Regel",
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
    Hashcat best64 Regel 🙀
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
    | Geknackte Passwörter                   | 11 024 306 (18.22%) |

    </div><br><br><br>
    """,
    unsafe_allow_html=True
)

col3, col4 = st.columns(2)

col3.markdown(
    """
    <div align="center">

    | Regel | Funktionsweise                                                        | Beispiel  |
    |-------|-----------------------------------------------------------------------|-----------|
    | :     | Das Wort wird unverändert in die erweiterte Passwortliste geschrieben | Passwort  |
    | $1    | An das Wort wird die Zahl "1" angehängt                               | Passwort1 |
    | u     | Alle Buchstaben werden großgeschrieben                                | PASSWORT  |
    | l     | Alle Buchstaben werden kleingeschrieben                               | passwort  |
    | so0   | Der Buchstabe "o" wird durch die Zahl 0 ersetzt                       | Passw0rt  |
    | f     | Alle Großbuchstaben werden zu Kleinbuchstaben und umgekehrt           | pASSWORT  |

    </div><br>
""",
    unsafe_allow_html=True
)


col4.markdown(
    """
Hashcat bietet die Funktionalität eine bestehende Passwortliste mit verschiedensten Regeln zu erweitern.
Die Hashcat-Regel "best64", enthält über 80 verschiedene Regeln. \n
Wenn die best64-Regel auf ein Wort angewendet wird entstehen also über 80 neue Wörter.
Um die Funktionsweise der Regeln besser verstehen zu können, werden insgesamt 6 beispielhafte Regeln auf das Wort 
"Passwort" angewendet.
"""
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
    In den folgenden Absätzen wird der Begriff Entropie angesprochen, dies ist ein Wert welcher 
    die Stärke eines Passwortes definiert. Um so höher Entropie Wert ist, um so sicherer wird ein Passwort angesehen.
    Der Passwortmanager KeePass stuft die Sicherheit der Passwörter wie folgt ein (siehe linke Tabelle).
"""
)


col7, col8 = st.columns(2)

image = "steamlit/images/hc_best64/train_best64_sort_utf-8_repair_pw_complexity.jpg"
col7.image(image, caption='Passwortkomplexität aller Passwörter in der generierten Liste', use_column_width=True)

col8.markdown(
    """
    Man kann in der Abbildung erkennen, dass die generierte Passwortliste alle Entropie bereiche abdeckt.
    Das Diagramm zeigt auch an, dass sich die Entropie stark auf die untere Hälfte konzentriert.
    Dies bedeutet nach der Definition von KeePass, dass die meisten generierten Passwörter sehr schwach sind.
    
    
"""
)

col9, col10 = st.columns(2)

image = "steamlit/images/hc_best64/crackedpw_train_best64_sort_cut_repair_pw_complexity.jpg"
col9.image(image, caption='Passwortkomplexität der geknackten Passwörter', use_column_width=True)

col10.markdown(
    """ 
Nun zu den Passwörtern, welche mithilfe der best64-Passwortliste geknackt werden konnten.
Es wurde hier das beste Ergebnis des kompletten Projekts erzielt.
Mit dieser Passwortliste konten 11 024 306 Passwörter, was 18.22% entspricht in Klartext umgewandelt werden.
Man kann hier deutlich erkennen, dass viele Passwörter mit einer Entropie von unter 20 geknackt wurden.
Wenn man die obere Abbildung mit dieser vergleicht, lässt sich ein Zusammenhang feststellen.
Die Graphen schlagen bei der gleichen Entropie werden aus.
Das ist natürlich nicht verwunderlich, wenn in der Passwortliste, welche zum Knacken benutzt wurde, viele Passwörter
mit Entropie 30 sind das auch viele Passwörter mit einer Entropie von 30 gefunden worden.

"""
)

col11, col12 = st.columns(2)

image = "steamlit/images/hc_best64/train_best64_sort_utf-8_repair_normalverteilung_passwortlänge.jpg"
col11.image(image, caption='Verteilung der Passwortlänge in der Hashcat generierten Liste', use_column_width=True)

col12.markdown(
    """    
Es ist hier die Längenverteilung der Passwörter in der Passwortliste, welche mit der best64-Regel erstellt wurde zu
sehen. Man kann hier eine relative schöne Normalverteilung sehen. Das Hoch ist bei der Passwortlänge 10 mit 16,77%.
Eine normal verteile Liste ist gut, es Passwörter mit jeder Länge enthält, aber im mittleren Bereich am meisten 
Passwörter beinhaltet.
"""
)



col13, col14 = st.columns(2)

image = "steamlit/images/hc_best64/crackedpw_train_best64_sort_cut_repair_normalverteilung_passwortlänge.jpg"
col13.image(image, caption='Verteilung der Passwortlänge der geknackten Passwörter', use_column_width=True)

col14.markdown(
    """
    Es ist hier die Verteilung der Passwörter dargestellt, welche mithilfe der best64-Liste geknackt werden konnten.
    Man kann deutlich erkennen, das vor allem Passwörter mit der Länge 6 bis 10 geknackt worden.
    Auch die ursprüngliche Liste hatte viele Passwörter in diesem Bereich, das Ergebnis ist also nicht verwunderlich.

"""
)

col15, col16 = st.columns(2)
col17, col18 = st.columns(2)

if col15.button("Ab zu den 17 Hashcat Regeln"):
    switch_page("Hashcat 17 Regeln")
if col17.button("Zurück"):
    switch_page("Home")

