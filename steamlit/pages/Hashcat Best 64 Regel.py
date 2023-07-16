import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hashcat Best 64 Regel",
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

st.write("# Hashcat Best 64 Regel 👋")

# Picture and Text
col1, col2 = st.columns(2)

image = "steamlit/images/crackedpw_train_cut_pw_complexity.jpg"
col1.image(image, caption='Passwortkomplexität', use_column_width=True)

col2.markdown(
    """
    
    Die "Hashcat Best 64 Regel" Liste ist in diesem Projekt die größte Datei.\
    
    
    <div align="center">

    | Enthaltene Passwörter | -         |
    |-----------------------|--------------------|
    | Gecrackte Passwörter  | -  |

    </div>
    

    """,
    unsafe_allow_html=True
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

image = "steamlit/images/crackedpw_train_cut_pw_complexity.jpg"
col5.image(image, caption='Passwortkomplexität', use_column_width=True)

col6.markdown(
    """
    Hallo! Ich bin Text!
    """
)

# Picture and Text
col7, col8 = st.columns(2)

image = "steamlit/images/crackedpw_train_cut_pw_complexity.jpg"
col7.image(image, caption='Passwortkomplexität', use_column_width=True)

col8.markdown(
    """
    Hallo! Ich bin Text!
    """
)



image = "steamlit/images/68_linkedin_found_without_hashes_utf-8_repair_cracktime.jpg"
st.image(image, output_format="JPG")

if st.button("Zurück"):
    switch_page("hello")


