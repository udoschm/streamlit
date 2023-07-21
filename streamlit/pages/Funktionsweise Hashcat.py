import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Funktionsweise von Hashcat",
    page_icon="🐱",
    initial_sidebar_state="collapsed",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Funktionsweise von Hashcat 🐱")

st.markdown(
    """
   Hashcat behauptet von sich selbst das weltweit schnellste und fortschrittlichste Programm zur
   Passwortwiederherstellung zu sein.
   """
)


image = "streamlit/images/hc_logo.jpg"
st.image(image, caption='Hashcat Logo', width=450)

st.markdown(
    """
   Es unterstützt insgesamt fünf verschiedene Angriffsmodus und über 300 hochoptimierte Hashing-Algorithmen. 
   Hashcat wird allerdings nicht nur zur Passwortwiederherstellung verwendet, sondern auch bei Penetrationstests.
   Außerdem wird das Tool auch von Cyberkriminellen genutzt.
   
   Passwörter sind eine gängige Methode um sich zu authentifizieren, um seine Identität nachzuweisen, beispielsweise
   bei der Anmeldung an einem Computer. Das Passwort wird in der Regel allerdings nicht als Klartext abgespeichert, 
   sondern als Hashwert, was zu mehr Sicherheit beitragen soll.
   Dieser Hashwert wird durch eine Hashfunktion berechnet (beispielsweise SHA256), Hashfunktionen sind 
   sogenannte Einwegfunktionen. Dies bedeutet, dass das Ergebnis nicht zurückgerechnet werden kann.
   Hier ein Beispiel:<br>
   Wenn das Wort "Passwort" in die SHA256-Hashfunktion geben wird, kommt folgender Hash heraus: 
   "a36c101570cc4410993de5385ad7034adb2dae6a05139ac7672577803084634d". Es ist allerdings nicht möglich aus dem Hash
   das Wort "Passwort" zurückzurechnen.
   
   Hier kommt Hashcat ins Spiel, es versucht durch Ausprobieren heraus zu finden, welches Wort hinter dem Hash steckt.
   Es können dazu die folgenden Hashcat Methoden verwendet werden:
   * **Wörterbuchangriffe**: <br>Hashcat nimmt eine Liste mit Passwörtern und probiert diese nach und nach durch.
   * **Kombinationsangriffe**: <br>Es werden mehrere Wörterbücher (Passwortlisten) kombiniert.
   * **Maskenangriffe**: <br>Es werden Passwörter in einem bestimmten Format ausprobiert (z.B. 10 Zeichen).
   * **Regelbasierte Angriffe**: <br>Eine Passwortliste wird durch bestimmte Regeln erweitert.
   * **Brute-Force-Angriffe**: <br>Es werden verschiedene Zeichenkombinationen ausprobiert.
   
   In diesem Projekt wurden regelbasierte Angriffe & Wörterbuchangriffe verwendet, um zu versuchen möglichst viele
   Passwörter zu knacken.
   Die Passwortliste 'rockyou.txt' wurde mit Regeln vergrößert und anschließend diese Liste durchprobiert.
   
   
   """,
    unsafe_allow_html=True
)


st.markdown(
    """
    #### Was ist ein Generative Adverserial Network (GAN)?
    """
)

if st.button("Funktionsweise GAN"):
    switch_page("Funktionsweise GAN")
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
    https://github.com/hashcat/hashcat<br>
    https://www.security-insider.de/was-ist-hashcat-a-1077200/<br>
    https://www.kali.org/tools/hashcat/
    </body>
    """,
    unsafe_allow_html=True
)



