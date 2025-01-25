import streamlit as st
from math import pi
import pyperclip

st.subheader("Volumenverdoppelungszeit")
st.write("Ein Online-Minitool von Lennart Schefe")

my_date = st.date_input("Datum der 1. Untersuchung:", value="today", format="DD/MM/YYYY")

x = st.number_input("Durchmesser 1", 0, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
y = st.number_input("Durchmesser 2", 1, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
z = st.number_input("Durchmesser 3", 2, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
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

x2 = st.number_input("Durchmesser 1", 3, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
y2 = st.number_input("Durchmesser 2", 4, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
z2 = st.number_input("Durchmesser 3", 5, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
volume2 = (4/3)*pi*(x2/2)*(y2/2)*(z2/2)

#if st.button("Kopieren",1):
#    pyperclip.copy(rounded_volume)
#    st.write("Das gerundete Volumen wurde in die Zwischenablage kopiert.")


my_date2 = st.date_input("Datum der 2. Untersuchung:", value="today", format="DD/MM/YYYY")
time_elapsed=my_date2-my_date

st.write(time_elapsed.days)
