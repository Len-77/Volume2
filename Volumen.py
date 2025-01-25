import streamlit as st
from math import pi
import pyperclip

st.subheader("Volumenberechnung")
st.write("Ein Online-Minitool von Lennart Schefe")
x = st.number_input("Durchmesser 1", step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
y = st.number_input("Durchmesser 2", step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
z = st.number_input("Durchmesser 3", step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
volume = (4/3)*pi*(x/2)*(y/2)*(z/2)

st.subheader("Volumen:")
st.subheader(volume)

#if st.button("Kopieren",0):
#    pyperclip.copy(volume)
#    st.write("Das Volumen wurde in die Zwischenablage kopiert.")

my_digits = st.slider("Runden auf:",0,10,3)
rounded_volume = round(volume,my_digits)
st.write("Stellen.")

st.subheader("Gerundetes Volumen:")
st.subheader(rounded_volume)

#if st.button("Kopieren",1):
#    pyperclip.copy(rounded_volume)
#    st.write("Das gerundete Volumen wurde in die Zwischenablage kopiert.")

# Text to copy
text_to_copy = "Hello, Streamlit!"

st.write("Click the button below to copy text to clipboard:")

# Example text to copy
rounded_volume = "123.45"

st.write("Click the button below to copy the text to your clipboard:")

if st.button("Copy to Clipboard"):
    st.markdown(f"""
        <script>
            navigator.clipboard.writeText("{rounded_volume}");
        </script>
        """, unsafe_allow_html=True)
    st.success("Text copied to clipboard!")
