import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="GAN",
    page_icon="🖥️",
    initial_sidebar_state="collapsed",
    # layout="wide"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("# Funktionsweise des Generative Adversarial Network (GAN) 🖥️")


st.markdown(
    """
    Ein Generative Adversarial Network besteht aus zwei Teilen, der Generator und der Diskriminator. Der Generator, wie 
    der Name schon vermuten lässt, generiert Dinge, in diesem Fall Passwörter. Der Diskriminator lernt zwischen den 
    vom Generator erzeugten Passwörtern und echten aus der `rockyou.txt` zu unterscheiden.\
    In diesem Netzwerk verliert immer einer der beiden Teile. Dies wird durch eine Verlustfunktion erreicht.
    
    ## Diskriminator 
    Der Diskriminator ist in ein Klassifizierer. Er versucht zwischen echten Passwörtern und den Passwörtern, die vom 
    Generator erzeugt wurden, unterscheiden. Der Diskriminator muss allerdings trainiert werden. Das passiert, indem der
    Generator versucht Passwörter zu erzeugen oder ein Passwort aus der Trainingsdatei genommen wird. Dann versucht der 
    Diskriminator zu erraten, ob das Passwort echt oder generiert wurde.\
    
    ## Generator
    Der Generator lernt durch Feedback des Diskriminators gefälschte Daten zu erzeugen. Damit wird der Generator immer 
    besser darin, den Diskriminator auszutricksen.\
    
    ## Training
    Während der Diskriminator trainiert wird, wird der Generator nicht verändert. Während er trainiert wird, lernt der 
    Diskriminator die Schwächen des Generators zu erkennen. \
    Auch wenn der Generator trainiert wird, wird der Diskriminator nicht verändert.\
    Ab einem bestimmten Punkt wird der Diskriminator immer schlechter, da er nicht mehr zwischen echten und erzeugten 
    Passwörtern unterscheiden kann. Wenn der Diskriminator dem Generator schlechtes Feedback bereitstellt, kann der 
    Generator auch nicht mehr besser werden. Die Konsequenz daraus kann sein, dass der Generator immer schlechtere 
    Passwörter generiert. 
    """
)

image = "streamlit/images/GAN.png"
st.image(image, caption='GAN Struktur', use_column_width=True)

st.markdown(
    """
    #### Was ist Hashcat?
    """
)

if st.button("Funktionsweise Hashcat"):
    switch_page("Funktionsweise Hashcat")
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
    https://developers.google.com/machine-learning/gan/gan_structure
    </body>
    """,
    unsafe_allow_html=True
)