import streamlit as st
import pandas as pd
from charts import (pie_chart, histogram, line_chart, bar_chart,
                    scatter_plot, box_plot, heatmap,
                    area_chart, count_plot, violin_plot)
from filters import apply_filters

st.set_page_config(page_title="Airport Dashboard",
                   layout="wide")

st.title("✈️ OpenFlights Airport Dashboard")
st.caption("Exploratory Data Analysis | "
           "Instructor: Ali Hassan Sherazi")

# ── Load Data ──────────────────────────────────────────
@st.cache_data
def load_data():
    a_cols = ['AirportID','Name','City','Country','IATA',
              'ICAO','Lat','Lon','Altitude','Timezone',
              'DST','TzDB','Type','Source']
    airports = pd.read_csv('data/airports.dat',
                           header=None, names=a_cols,
                           na_values=['\\N', ''])
    airports.dropna(subset=['Lat','Lon','Country'],
                    inplace=True)
    airports['Altitude'] = pd.to_numeric(
        airports['Altitude'], errors='coerce')

    r_cols = ['Airline','AirlineID','SrcAirport',
              'SrcAirportID','DstAirport','DstAirportID',
              'Codeshare','Stops','Equipment']
    routes = pd.read_csv('data/routes.dat',
                         header=None, names=r_cols,
                         na_values=['\\N', ''])
    return airports, routes

airports, routes = load_data()

# ── Sidebar Filters ────────────────────────────────────
st.sidebar.header("🔍 Filters")

countries = ["All"] + sorted(
    airports['Country'].dropna().unique().tolist())
country_sel = st.sidebar.selectbox("Country", countries)

dst_opts = ["All"] + sorted(
    airports['DST'].dropna().unique().tolist())
dst_sel = st.sidebar.selectbox("DST Type", dst_opts)

alt_min_val = int(airports['Altitude'].min())
alt_max_val = int(airports['Altitude'].max())
alt_min, alt_max = st.sidebar.slider(
    "Altitude Range (feet)",
    alt_min_val, alt_max_val,
    (alt_min_val, alt_max_val))

type_opts = ["All"] + sorted(
    airports['Type'].dropna().unique().tolist())
type_sel = st.sidebar.selectbox("Airport Type", type_opts)

search = st.sidebar.text_input("🔎 Search Airport/City")

if st.sidebar.button("🔄 Reset Filters"):
    st.rerun()

# ── Apply Filters ──────────────────────────────────────
filtered = apply_filters(
    airports,
    country=country_sel,
    dst=dst_sel,
    alt_min=alt_min,
    alt_max=alt_max,
    search_text=search,
    airport_type=type_sel)

# ── KPI Cards ──────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
k1.metric("✈️ Total Airports", len(filtered))
k2.metric("🌍 Countries", filtered['Country'].nunique())
k3.metric("📏 Avg Altitude (ft)",
          f"{filtered['Altitude'].mean():.0f}")
k4.metric("🛣️ Total Routes", len(routes))

st.divider()

# ── Charts ─────────────────────────────────────────────
c1, c2 = st.columns(2)
with c1:
    st.subheader("🌍 Airport Locations (Scatter)")
    st.pyplot(scatter_plot(filtered))
with c2:
    st.subheader("🥧 Top Countries (Pie)")
    st.pyplot(pie_chart(filtered))

c3, c4 = st.columns(2)
with c3:
    st.subheader("📊 Routes by Country (Bar)")
    st.pyplot(bar_chart(routes, filtered))
with c4:
    st.subheader("📈 Altitude Distribution (Histogram)")
    st.pyplot(histogram(filtered))

c5, c6 = st.columns(2)
with c5:
    st.subheader("📉 Airports by Timezone (Line)")
    st.pyplot(line_chart(filtered))
with c6:
    st.subheader("📐 Cumulative Airports (Area)")
    st.pyplot(area_chart(filtered))

c7, c8 = st.columns(2)
with c7:
    st.subheader("📦 Altitude by DST (Box Plot)")
    st.pyplot(box_plot(filtered))
with c8:
    st.subheader("🔥 Correlation Heatmap")
    st.pyplot(heatmap(filtered))

c9, c10 = st.columns(2)
with c9:
    st.subheader("🔢 Airport Types (Count Plot)")
    st.pyplot(count_plot(filtered))
with c10:
    st.subheader("🎻 Altitude Spread (Violin)")
    st.pyplot(violin_plot(filtered))
