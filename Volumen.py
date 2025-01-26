import streamlit as st
from math import pi, log
from datetime import date

st.subheader("Volumenverdoppelungszeit")
st.write("Ein Online-Minitool von Lennart Schefe :sunglasses:")

today = date.today()

try:
    one_year_before = today.replace(year=today.year - 1)
except ValueError:
    one_year_before = today.replace(year=today.year - 1, day=28)

mode = st.radio("",["Durchmesser", "Halbachsen", "Bekannte Volumina"],horizontal = True)

st.write(mode)

my_date = st.date_input("Datum der 1. Untersuchung:", value=one_year_before, format="DD.MM.YYYY")

help_diameter = "Gesamter Durchmesser, nicht Halbachse. Typischerweise in mm."

x = st.number_input("Durchmesser 1", key=0, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help=help_diameter)
y = st.number_input("Durchmesser 2", key=1, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help=help_diameter)
z = st.number_input("Durchmesser 3", key=2, step=0.1, format="%0.1f", min_value=0.0, value=1.0,
                    help=help_diameter)

volume = (4/3)*pi*(x/2)*(y/2)*(z/2)

st.write(f"Volumen: {volume}, gerundet: {round(volume,3)}")

my_date2 = st.date_input("Datum der 2. Untersuchung:", value="today", format="DD.MM.YYYY")

x2 = st.number_input("Durchmesser 1", key=3, step=0.1, format="%0.1f", min_value=0.0, value=2.0,
                    help=help_diameter)
y2 = st.number_input("Durchmesser 2", key=4, step=0.1, format="%0.1f", min_value=0.0, value=2.0,
                    help=help_diameter)
z2 = st.number_input("Durchmesser 3", key=5, step=0.1, format="%0.1f", min_value=0.0, value=2.0,
                    help=help_diameter)

volume2 = (4/3)*pi*(x2/2)*(y2/2)*(z2/2)

st.write(f"Volumen: {volume2}, gerundet: {round(volume2,3)}")

time_elapsed = my_date2-my_date
st.write(f"Es sind {time_elapsed.days} Tage vergangen.")

if (volume > 0) and (volume2 > 0) and (volume2 > volume) and (time_elapsed.days > 0):
    growth_rate = log(volume2 / volume) / time_elapsed.days
    VDT = log(2) / growth_rate
    st.write(f"Volumenverdoppelungszeit: {round(VDT)} Tage")
else:
    st.write("Volumenverdoppelungszeit: ...")
