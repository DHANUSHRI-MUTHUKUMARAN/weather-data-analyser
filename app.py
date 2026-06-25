import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# Page Config
# ------------------------

st.set_page_config(
    page_title="Weather Data Analyzer",
    page_icon="🌦",
    layout="wide"
)

st.title("🌦 Weather Data Analyzer Dashboard")

# ------------------------
# Load Data
# ------------------------

df = pd.read_csv("data/processed/weather_cleaned.csv")

# ------------------------
# Sidebar
# ------------------------

st.sidebar.header("Filters")

city = st.sidebar.selectbox(
    "Select City",
    sorted(df["City"].unique())
)

metric = st.sidebar.selectbox(
    "Metric",
    [
        "Avg Temp (°C)",
        "Rainfall (mm)",
        "Max Wind (km/h)"
    ]
)

city_df = df[df["City"] == city]

# ------------------------
# KPI Cards
# ------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Temperature",
    f"{city_df['Avg Temp (°C)'].mean():.1f} °C"
)

col2.metric(
    "Total Rainfall",
    f"{city_df['Rainfall (mm)'].sum():.1f} mm"
)

col3.metric(
    "Average Wind",
    f"{city_df['Max Wind (km/h)'].mean():.1f} km/h"
)

col4.metric(
    "Records",
    len(city_df)
)

# ------------------------
# Tabs
# ------------------------

tab1, tab2, tab3 = st.tabs([
    "📈 Trends",
    "🌧 Rainfall",
    "🌍 Comparison"
])

# ------------------------
# Trends
# ------------------------

with tab1:

    fig = px.line(
        city_df,
        x="Date",
        y=metric,
        title=f"{metric} Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

# ------------------------
# Rainfall
# ------------------------

with tab2:

    rainfall = (
        city_df.groupby("Month")["Rainfall (mm)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        rainfall,
        x="Month",
        y="Rainfall (mm)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ------------------------
# City Comparison
# ------------------------

with tab3:

    compare = (
        df.groupby("City")["Avg Temp (°C)"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        compare,
        x="City",
        y="Avg Temp (°C)",
        color="City"
    )

    st.plotly_chart(fig, use_container_width=True)