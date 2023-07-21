import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hashcat erweiterte top10-Regel",
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
    Hashcat erweiterte top10-Regel 😼
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
    | Geknackte Passwörter                   | 5 386 630 (8,90%) |

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
Hashcat bietet die Funktionalität, eine bestehende Passwortliste mit verschiedensten Regeln zu erweitern.
Die Hashcat-Regel "top10", enthält insgesamt 10 verschiedene Regeln. \n
Wenn die top10-Regel auf ein Wort angewendet wird, entstehen also insgesamt 10 neue Wörter.
Die top10-Regel wurde um insgesamt 7 Regeln erweitert, um noch mehr Ergebnisse zu erzielen.
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
    In den folgenden Absätzen wird der Begriff Entropie angesprochen, dies ist ein Wert, welcher 
    die Stärke eines Passwortes definiert. Um so höher Entropie-Wert ist, um so sicherer wird ein Passwort angesehen.
    Der Passwortmanager KeePass stuft die Sicherheit der Passwörter wie folgt ein (siehe linke Tabelle).
"""
)


col7, col8 = st.columns(2)

image = "steamlit/images/hc_top10/hc_best15_sort_utf-8_repair_pw_complexity.jpg"
col7.image(image, caption='Passwortkomplexität aller Passwörter in der generierten Liste', use_column_width=True)

col8.markdown(
    """
In der dieser Abbildung ist die Passwortkomplexität der generierten Passwortliste in Entropie-Bits dargestellt.    
Man kann anhand der Abbildung erkennen, dass die meisten Passwörter in der von Hashcat generierten Liste, sich in dem
Bereich zwischen 20 und 40 Entropie-Bits bewegt. Das bedeutet das eine Liste mit vielen sehr schwachen Passwörtern
generiert wurde.
Mit dieser Passwortliste konnten insgesamt 5 386 630 Passwörter erraten werden, was 8,90% entspricht.
"""
)

col9, col10 = st.columns(2)

image = "steamlit/images/hc_top10/crackedpw_hc_best15_sort_cut_repair_pw_complexity.jpg"
col9.image(image, caption='Passwortkomplexität der geknackten Passwörter', use_column_width=True)

col10.markdown(
    """ 
Das hier links dargestellte Diagramm zeigt die Entropie der geknackten Passwörter auf.       
Man kann hier deutlich erkennen, dass fast ausnahmslos Passwörter mit einer sehr schwachen Entropie geknackt wurden.
Dies hat den Hintergrund, dass sich die Verteilung in der generierten Passwortliste auch hauptsächlich in diesem Bereich
bewegt. Ein weiterer möglicher Grund ist, es das schwache Passwörter leichter gecrackt werden können. Dies liegt daran, 
dass ein Passwort mit niedriger Entropie einen kleineren Zeichenraum besitzen und somit die Wahrscheinlichkeit das 
Passwort zu erraten höher ist, da es weniger Möglichkeiten gibt.
"""
)

col11, col12 = st.columns(2)

image = "steamlit/images/hc_top10/hc_best15_sort_utf-8_repair_normalverteilung_passwortlänge.jpg"
col11.image(image, caption='Verteilung der Passwortlänge in der Hashcat generierten Liste', use_column_width=True)

col12.markdown(
    """    
Die von Hashcat generierte Passwortliste wurde außerdem, auf die Verteilung der Länge je Passwort untersucht.
Jedes Passwort wurde entsprechend einkategorisiert, diese Kategorisierung wird hier im Diagramm aufgezeigt.
Man kann der Darstellung entnehmen, dass die Passwortlängen relativ gleich verteilt sind.
In Deutschland benutzen 14% der Menschen ein Passwort, was maximal 8 Zeichen hat und 35% der deutschen Bevölkerung 
hat ein Passwort mit einer maximalen Länge von 10 Zeichen.
Überträgt man diese Informationen auf die Verteilung der Passwortliste, hätte man höchstwahrscheinlich gute Chancen
viele Passwörter von Deutschen zu knacken, da hier die Verteilung ähnlich ist.
Die Qualität der Passwörter muss natürlich mit berücksichtigt werden.
"""
)



col13, col14 = st.columns(2)

image = "steamlit/images/hc_top10/crackedpw_hc_best15_sort_cut_repair_normalverteilung_passwortlänge.jpg"
col13.image(image, caption='Verteilung der Passwortlänge der geknackten Passwörter', use_column_width=True)

col14.markdown(
    """
Nun zu den Ergebnissen, welche Passwortlängen durch die generierte Liste jeweils herausgefunden werden konnten.        
Hier kann man erkennen, dass die erweiterte top10-Passwortliste hauptsächlich Passwörter der Länge 6,7,8,9,10 knacken
konnte. Dieses Ergebnis ist nicht verwunderlich, wenn man es mit dem Diagramm mit der Entropie vergleicht.
Die Passwortlänge ist ein Faktor, welcher mit in die Berechnung der Entropie mit einfließt.
Des Weiteren beinhaltet die von Hashcat generierte Liste auch zu einem hohen Prozentsatz Passwörter mit dieser Länge, 
was diese Verteilung erklärt.
"""
)

col15, col16 = st.columns(2)
col17, col18 = st.columns(2)

if col15.button("Ab zur Hashcat Best 64 Regel"):
    switch_page("Hashcat Best 64 Regel")
if col17.button("Zurück"):
    switch_page("Home")


st.markdown(
    """
    <style>
    abc {
    font-size: 12px; 
    } 
    </style>
    <abc>
    Quellen: <br>
    https://de.statista.com/statistik/daten/studie/988439/umfrage/laenge-von-passwoertern-in-deutschland/#:~:text=Zum%20Zeitpunkt%20der%20Erhebung%20gaben,bis%20zu%20zehn%20Zeichen%20haben.
    </abc>
    """,
    unsafe_allow_html=True
)
