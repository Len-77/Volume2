import streamlit as st
from math import pi, log

st.subheader("Volumenverdoppelungszeit")
st.write("Ein Online-Minitool von Lennart Schefe")

my_date = st.date_input("Datum der 1. Untersuchung:", value="today", format="DD/MM/YYYY")

x = st.number_input("Durchmesser 1", key=0, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
y = st.number_input("Durchmesser 2", key=1, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
z = st.number_input("Durchmesser 3", key=2, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
volume = (4/3)*pi*(x/2)*(y/2)*(z/2)

st.write("Volumen:")
st.write(volume)

my_date2 = st.date_input("Datum der 2. Untersuchung:", value="today", format="DD/MM/YYYY")

x2 = st.number_input("Durchmesser 1", key=3, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
y2 = st.number_input("Durchmesser 2", key=4, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
z2 = st.number_input("Durchmesser 3", key=5, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help="Gesamter Durchmesser, nicht Halbachse.")
volume2 = (4/3)*pi*(x2/2)*(y2/2)*(z2/2)

st.write("Volumen:")
st.write(volume2)

time_elapsed = my_date2-my_date
growth_rate = log(volume2 / volume) / time_elapsed.days
VDT = log(2) / growth_rate

st.write("Vergangene Tage:")
st.write(time_elapsed.days)

st.write("Volumenverdoppelungszeit:")
st.write(round(VDT))
