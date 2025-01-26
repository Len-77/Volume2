import streamlit as st
from math import pi, log
from datetime import date

# Language dictionaries
translations = {
    "German": {
        "title": "Volumenverdoppelungszeit",
        "subtitle": "Ein Online-Minitool von Lennart Schefe",
        "date1_label": "Datum der 1. Untersuchung:",
        "date2_label": "Datum der 2. Untersuchung:",
        "mode_label": "Modus auswählen:",
        "modes": ["Durchmesser", "Halbachsen", "Bekannte Volumina"],
        "diameter_help": "Gesamter Durchmesser, nicht Halbachse. Typischerweise in mm.",
        "semi_axes_help": "Nur Halbachse, nicht gesamter Durchmesser. Typischerweise in mm.",
        "report_help": "Nur zutreffend, wenn Angaben in mm oder ml gemacht.",
        "volume_label": "Volumen",
        "diameter_label": "Durchmesser",
        "semi_axes_label": "Halbachse",
        "rounded": "gerundet",
        "time_elapsed": "Es sind {days} Tage vergangen.",
        "vdt": "Volumenverdoppelungszeit: {vdt} Tage",
        "text_area_label": "Befundtext",
        "text_area_value": (
            "Am {date1} betrug das Volumen {volume1} ml, {days} Tage später, "
            "am {date2} betrug das Volumen {volume2} ml. "
            "Dies entspricht einer Volumenverdoppelungszeit von {vdt} Tagen."
        ),
        "vdt_placeholder": "Volumenverdoppelungszeit: ...",
    },
    "English": {
        "title": "Volume Doubling Time",
        "subtitle": "An online mini-tool by Lennart Schefe",
        "date1_label": "Date of 1st examination:",
        "date2_label": "Date of 2nd examination:",
        "mode_label": "Select mode:",
        "modes": ["Diameter", "Semi-axes", "Known volumes"],
        "diameter_help": "Full diameter, not semi-axis. Typically in mm.",
        "semi_axes_help": "Only semi-axes, not full diameter. Typically in mm.",
        "report_help": "Only applicable if values were provided in mm or ml.",
        "volume_label": "Volume",
        "diameter_label": "Diameter",
        "semi_axes_label": "Semi-axis",
        "rounded": "rounded",
        "time_elapsed": "{days} days have passed.",
        "vdt": "Volume Doubling Time: {vdt} days",
        "text_area_label": "Report Text",
        "text_area_value": (
            "On {date1}, the volume was {volume1} ml, {days} days later, "
            "on {date2}, the volume was {volume2} ml. "
            "This corresponds to a volume doubling time of {vdt} days."
        ),
        "vdt_placeholder": "Volume Doubling Time: ...",
    }
}

# Language selection
col1, col2, col3, col4 = st.columns(4)
with col4:
    language = st.selectbox("", ["German", "English"])

# Get the translations for the selected language
t = translations[language]

st.subheader(t["title"])
st.write(t["subtitle"])

today = date.today()

# Handle leap years for one year ago calculation
try:
    one_year_before = today.replace(year=today.year - 1)
except ValueError:
    one_year_before = today.replace(year=today.year - 1, day=28)

# Mode selection
mode = st.radio(t["mode_label"], t["modes"], horizontal=True)

# Handle each mode
if mode == t["modes"][0]:  # Diameter Mode
    my_date = st.date_input(t["date1_label"], value=one_year_before, format="DD.MM.YYYY")
    x = st.number_input(t["diameter_label"] + " 1", key=0, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["diameter_help"])
    y = st.number_input(t["diameter_label"] + " 2", key=1, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["diameter_help"])
    z = st.number_input(t["diameter_label"] + " 3", key=2, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["diameter_help"])
    volume = (4 / 3) * pi * (x / 2) * (y / 2) * (z / 2)
    st.write(t["volume_label"] + f": {volume}")
    my_date2 = st.date_input(t["date2_label"], value=today, format="DD.MM.YYYY")
    x2 = st.number_input(t["diameter_label"] + " 1", key=3, step=0.1, format="%0.1f", min_value=0.0, value=2.0, help=t["diameter_help"])
    y2 = st.number_input(t["diameter_label"] + " 2", key=4, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["diameter_help"])
    z2 = st.number_input(t["diameter_label"] + " 3", key=5, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["diameter_help"])
    volume2 = (4 / 3) * pi * (x2 / 2) * (y2 / 2) * (z2 / 2)

elif mode == t["modes"][1]:  # Semi-Axes Mode
    my_date = st.date_input(t["date1_label"], value=one_year_before, format="DD.MM.YYYY")
    x = st.number_input(t["semi_axes_label"] + " 1", key=0, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["semi_axes_help"])
    y = st.number_input(t["semi_axes_label"] + " 2", key=1, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["semi_axes_help"])
    z = st.number_input(t["semi_axes_label"] + " 3", key=2, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["semi_axes_help"])
    volume = (4 / 3) * pi * x * y * z
    x2 = st.number_input(t["semi_axes_label"] + " 1", key=3, step=0.1, format="%0.1f", min_value=0.0, value=2.0, help=t["semi_axes_help"])
    y2 = st.number_input(t["semi_axes_label"] + " 2", key=4, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["semi_axes_help"])
    z2 = st.number_input(t["semi_axes_label"] + " 3", key=5, step=0.1, format="%0.1f", min_value=0.0, value=1.0, help=t["semi_axes_help"])
    volume2 = (4 / 3) * pi * x2 * y2 * z2
    my_date2 = st.date_input(t["date2_label"], value=today, format="DD.MM.YYYY")

elif mode == t["modes"][2]:  # Known Volumes Mode
    my_date = st.date_input(t["date1_label"], value=one_year_before, format="DD.MM.YYYY")
    volume = st.number_input(t["volume_label"] + " 1", step=0.1, format="%0.1f", min_value=0.0, value=1.0)
    my_date2 = st.date_input(t["date2_label"], value=today, format="DD.MM.YYYY")
    volume2 = st.number_input(t["volume_label"] + " 2", step=0.1, format="%0.1f", min_value=0.0, value=2.0)

# Calculate time elapsed
time_elapsed = my_date2 - my_date
st.write(t["time_elapsed"].format(days=time_elapsed.days))

# Calculate VDT if conditions are met
if volume > 0 and volume2 > 0 and volume2 > volume and time_elapsed.days > 0:
    growth_rate = log(volume2 / volume) / time_elapsed.days
    VDT = log(2) / growth_rate
    st.write(t["vdt"].format(vdt=round(VDT)))
    st.text_area(t["text_area_label"], value=t["text_area_value"].format(
        date1=my_date.strftime("%d.%m.%Y"),
        volume1=round(volume, 1),
        days=time_elapsed.days,
        date2=my_date2.strftime("%d.%m.%Y"),
        volume2=round(volume2, 1),
        vdt=round(VDT)
    ), help = t["report_help"])
else:
    st.write(t["vdt_placeholder"])
