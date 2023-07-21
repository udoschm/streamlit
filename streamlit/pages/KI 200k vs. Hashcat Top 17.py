import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="KI-500 Iterationen",
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
    Künstliche Intelligenz vs. Hashcat mit 17 Regeln
    </h1>
    """,
    unsafe_allow_html=True
)

# Picture and Text
col0, col99 = st.columns(2)

col0.markdown(
    """
    <div align="center">

    | Passwörter LinkedIn                | 60 516 679        |
    |------------------------------------|-------------------|
    | Gefundene Passwörter PassGAN       | 2 342 207 (3,87%) |
    | Gefundene Passwörter RockYou Datei | 2 937 754 (4,87%) |
    | Gefundene Passwörter top-10 Regel  | 5 286 630 (8,90%) |

    </div><br>
    """,
    unsafe_allow_html=True
)


col99.markdown(
    """
    Hier werden die Ergebnisse von Hashcat und PassGAN verglichen und die Ergebnisse erläutert. Es wurden 200 Millionen
    Passwörter sowohl von der KI als auch von Hashcat erzeugt. Diese wurden dann gegen die LinkedIn Liste verglichen. 
    Hashcat konnte mehr als doppelt so viele Passwörter mit den 17 Regeln wieder herstellen als die von PassGAN 
    generierte Liste.
    """
)


# Picture and Text
col1, col2 = st.columns(2)

# Lade die beiden Bilder
image2_path = "streamlit/images/200k_utf-8_repair_normalverteilung_passwortlänge.jpg"
image1_path = "streamlit/images/train_utf-8_repair_normalverteilung_passwortlänge.jpg"
image3_path = "streamlit/images/crackedpw_ai_200k_cut_repair_normalverteilung_passwortlänge.jpg"

col2.markdown(
    """      
    ## Längenverteilung Passwörter PassGAN
    Die Längenverteilung der Passwörter, die von PassGAN generiert wurden, orientiert sich sehr stark an der 
    `rockyou.txt`. Um also ein Ergebnis zu bekommen, dass alle Paswortlängen gleichermaßen abdeckt, ist es wichtig eine
    Datei für das Training zu verwenden, die relativ gleich verteilt ist. Es könnte auch von Vorteil sein, sich vorher zu
    informieren, wie die Passwortrichtlinien des Unternehmens sind, von der die Datei stammt, die angegriffen  werden 
    soll.
    """
)
with col2:
    selected_image = st.radio("Wähle ein Bild:", (
                                                "Längenverteilung PassGAN",
                                                "Längenverteilung rockyou.txt",
                                                "Längenverteilung gefundene Passwörter"))

if selected_image == "Längenverteilung rockyou.txt":
    col1.image(image1_path, caption="Längenverteilung rockyou.txt", use_column_width=True)
if selected_image == "Längenverteilung PassGAN":
    col1.image(image2_path, caption="Längenverteilung PassGAN", use_column_width=True)
if selected_image == "Längenverteilung gefundene Passwörter":
    col1.image(image3_path, caption="Längenverteilung gefundene Passwörter (PassGAN)", use_column_width=True)


# Picture and Text
col3, col4 = st.columns(2)

image1_path = "streamlit/images/hc_best15_sort_utf-8_repair_normalverteilung_passwortlänge.jpg"
image2_path = "streamlit/images/train_utf-8_repair_normalverteilung_passwortlänge.jpg"
image3_path = "streamlit/images/crackedpw_hc_best15_sort_cut_repair_normalverteilung_passwortlänge.jpg"

col4.markdown(
    """      
    ## Längenverteilung Passwörter Hashcat
    Die Längen der von Hashcat generierten Passwörter ist sehr viel gleich verteilter, als die von PassGAN. Das liegt 
    unter anderem daran, dass die Passwörter mit einer Regel kopiert werden, aus "password" wird zum Beispiel 
    "passwordpassword". Das erklärt auch die Ausreißer bei 12, 14 und 16 Zeichen langen Passwörtern. Durch diese 
    gleich verteilte Liste, können mehr als doppelt so viele Passwörter aus dem LinkedIn Leak wiederhergestellt werden.
    
    """
)
with col4:
    selected_image = st.radio("Wähle ein Bild:", (
                                                "Längenverteilung Hashcat",
                                                "Längenverteilung rockyou.txt",
                                                "Längenverteilung gefundene Passwörter"))

if selected_image == "Längenverteilung Hashcat":
    col3.image(image1_path, caption="Längenverteilung Hashcat", use_column_width=True)
if selected_image == "Längenverteilung rockyou.txt":
    col3.image(image2_path, caption="Längenverteilung rockyou.txt", use_column_width=True)
if selected_image == "Längenverteilung gefundene Passwörter":
    col3.image(image3_path, caption="Längenverteilung gefundene Passwörter (Hashcat)", use_column_width=True)


# Picture and Text
col5, col6 = st.columns(2)

image1_path = "streamlit/images/200k_utf-8_repair_pw_complexity.jpg"
image2_path = "streamlit/images/train_utf-8_repair_pw_complexity.jpg"
image3_path = "streamlit/images/crackedpw_ai_200k_cut_repair_pw_complexity.jpg"

col6.markdown(
    """
    ## Stärke der gefundenen Passwörter PassGAN
    In den folgenden Absätzen wird der Begriff Entropie angesprochen, dies ist ein Wert, welcher
    die Stärke eines Passwortes definiert. Um so höher der Entropie-Wert ist, um so sicherer ist ein Passwort.
    Der Passwortmanager KeePass stuft die Sicherheit der Passwörter wie folgt ein.
    <div align="center">
    
    | Entropie in Bits | Stärke |
    |------------------|--------------|
    | 0-64 | Sehr schwach |
    | 64-80 | Schwach |
    | 80-112 | Mäßig |
    | 112-128 | Stark |
    | > 128 | Sehr Stark |
    
    </div><br>
    Es ist zu sehen, dass sich die Komplexität der erzeugten Passwörter wieder sehr stark an der Komplexität der 
    Trainingsdatei orientiert. Über die Hälfte der generierten Passwörter haben eine Komplexität von 10 bis 20 Bit. Das kann
    unter anderem darauf zurückgeführt werden, dass die von PassGAN generierten Passwörter zum Großteil eine Länge 
    zwischen 5 und 10 Zeichen haben. Da die Entropie der Passwörter unmittelbar mit der Länge zusammenhängt, ist es
    offensichtlich, dass kürzere Passwörter, die eine niedrigere Entropie haben, mit einer höheren Wahrscheinlichkeit 
    gefunden werden. Dies ist bei den wiederhergestellten Passwörtern sehr stark zu erkennen. Hier haben fast 80% eine 
    Entropie von 10 bis 20 Bit.
    """,
    unsafe_allow_html=True
)

with col6:
    selected_image = st.radio("Wähle ein Bild:", (
                                                "Passwörtkomplexität PassGAN",
                                                "Passwörtkomplexität rockyou.txt",
                                                "Passworkomplexität gefundene Passwörter"))

if selected_image == "Passwörtkomplexität PassGAN":
    col5.image(image1_path, caption="Passwörtkomplexität PassGAN", use_column_width=True)
if selected_image == "Passwörtkomplexität rockyou.txt":
    col5.image(image2_path, caption="Passwörtkomplexität rockyou.txt", use_column_width=True)
if selected_image == "Passworkomplexität gefundene Passwörter":
    col5.image(image3_path, caption="Passworkomplexität gefundene Passwörter (PassGAN)", use_column_width=True)


# Picture and Text
col7, col8 = st.columns(2)

image1_path = "streamlit/images/hc_best15_sort_utf-8_repair_pw_complexity.jpg"
image2_path = "streamlit/images/train_utf-8_repair_pw_complexity.jpg"
image3_path = "streamlit/images/crackedpw_hc_best15_sort_cut_repair_pw_complexity.jpg"

col8.markdown(
    """
    ## Stärke der gefundenen Passwörter Hashcat
    Die Entropieverteilung der Passwörter, die von Hashcat erstellt wurde, deckt ein breiteres Spektrum ab als die von 
    PassGAN erstellte Liste oder die `rockyou.txt`. Wie in dem Diagramm zu sehen ist, hat die Liste, die aus Hashcat
    Regeln erstellt wurde, viel mehr komplexere Passwörter generiert. Dies hat im Umkehrschluss dazu beigetragen, dass
    mit dieser Liste mehr Passwörter aus dem LinkedIn Leak wiederhergestellt werden konnten. 
    """
)

with col8:
    selected_image = st.radio("Wähle ein Bild:", (
                                                "Passwörtkomplexität Hashcat",
                                                "Passwörtkomplexität rockyou.txt",
                                                "Passworkomplexität gefundene Passwörter"))

if selected_image == "Passwörtkomplexität Hashcat":
    col7.image(image1_path, caption="Passwörtkomplexität PassGAN", use_column_width=True)
if selected_image == "Passwörtkomplexität rockyou.txt":
    col7.image(image2_path, caption="Passwörtkomplexität rockyou.txt", use_column_width=True)
if selected_image == "Passworkomplexität gefundene Passwörter":
    col7.image(image3_path, caption="Passworkomplexität gefundene Passwörter (Hashcat)", use_column_width=True)

col9, col10 = st.columns(2)

col9.markdown(
    """
    ## Benötigte Zeit PassGAN
    PassGAN benötigt im Vergleich zu Hashcat sehr viel Zeit, um optimal trainiert zu werden. Der Generator, muss sich das
    Feedback des Diskriminators schließlich aneignen. Die KI hat circa 24 Stunden benötigt, um sich auf dieses Level zu
    trainieren.\\
    Das ist ein sehr viel größerer Zeitraum als Hashcat benötigt hat. Hashcat hat für das hier vorgestellte Ergebnis 
    40 Minuten benötigt und hat mehr doppelt so viele Passwörter wie PassGAN knacken können. Das macht Hashcat zum 
    Gewinner dieses Vergleichs.
    """
)

col10.markdown(
    """
    ## Vergleich Hashcat und PassGAN
    Hashcat hat im Vergleich zu PassGAN mehr als doppelt so viele Passwörter wieder herstellen können. 
    Das hat mehrere Gründe. PassGAN hält sich bei der Generierung der Passwörter sehr stark an die Liste, an der sie 
    Trainiert wird. Das ist bei Hashcat nicht der Fall. Hashcat geht die bereitgestellten Regeln durch und wendet diese
    auf jedes Passwort an.\\
    Es ist allerdings sehr schwer, beide Programme miteinander zu vergleichen. Wenn die Zeit in die Bewertung mit 
    einfließt, gewinnt immer Hashcat, da es in den 24 Stunden, die PassGAN benötigt um optimal trainiert zu werden, sehr
    viel mehr regelbasierte Passwörter erzeugen kann. 
    PassGAN kann zwar beeinflusst werden, wie das Training genau abläuft, aber Hashcat hat eine viel Umfangreichere 
    Dokumentation und vorgefertigte Regellisten, was es sehr einfach macht, mehr Passwörter zu erzeugen.
    """
)

if st.button("Zurück"):
    switch_page("Home")

st.divider()
st.markdown(
    """
    <style>
    #quellen {
    font-size: 12px; 
    } 
    </style>
    <div id="quellen">
    Quellen: <br>
    https://keepass.info/help/kb/pw_quality_est.html
    </div>
    """,
    unsafe_allow_html=True
)