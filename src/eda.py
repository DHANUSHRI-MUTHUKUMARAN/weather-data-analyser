import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/processed/weather_cleaned.csv")

os.makedirs("images", exist_ok=True)

sns.set_style("whitegrid")

# -----------------------------
# Monthly Average Temperature
# -----------------------------

monthly = (
    df.groupby(["City", "Month"])["Avg Temp (°C)"]
      .mean()
      .reset_index()
)

plt.figure(figsize=(12,6))

sns.lineplot(
    data=monthly,
    x="Month",
    y="Avg Temp (°C)",
    hue="City",
    marker="o"
)

plt.title("Monthly Average Temperature by City")
plt.tight_layout()

plt.savefig(
    "images/01_monthly_temperature.png",
    dpi=300
)

plt.close()

print("Saved 01_monthly_temperature.png")

# -----------------------------
# Seasonal Rainfall
# -----------------------------

seasonal = (
    df.groupby(["City","Season"])["Rainfall (mm)"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(12,6))

sns.barplot(
    data=seasonal,
    x="Season",
    y="Rainfall (mm)",
    hue="City"
)

plt.title("Seasonal Rainfall by City")

plt.tight_layout()

plt.savefig(
    "images/02_seasonal_rainfall.png",
    dpi=300
)

plt.close()

print("Saved 02_seasonal_rainfall.png")

# -----------------------------
# Temperature Distribution
# -----------------------------

plt.figure(figsize=(12,6))

sns.histplot(
    data=df,
    x="Avg Temp (°C)",
    hue="City",
    bins=30,
    kde=True,
    element="step"
)

plt.title("Temperature Distribution Across Cities")
plt.xlabel("Average Temperature (°C)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "images/03_temperature_distribution.png",
    dpi=300
)

plt.close()

print("Saved 03_temperature_distribution.png")

# -----------------------------
# Correlation Heatmap
# -----------------------------

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(10,8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "images/04_correlation_heatmap.png",
    dpi=300
)

plt.close()

print("Saved 04_correlation_heatmap.png")

# -----------------------------
# Wind Speed Distribution
# -----------------------------

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df,
    x="City",
    y="Max Wind (km/h)"
)

plt.title("Wind Speed Distribution by City")

plt.tight_layout()

plt.savefig(
    "images/05_wind_distribution.png",
    dpi=300
)

plt.close()

print("Saved 05_wind_distribution.png")

# -----------------------------
# Temperature Heatmap
# -----------------------------

pivot = df.pivot_table(
    values="Avg Temp (°C)",
    index="City",
    columns="Month",
    aggfunc="mean"
)

plt.figure(figsize=(12,5))

sns.heatmap(
    pivot,
    annot=True,
    cmap="YlOrRd",
    fmt=".1f"
)

plt.title("Average Monthly Temperature Heatmap")

plt.tight_layout()

plt.savefig(
    "images/06_temperature_heatmap.png",
    dpi=300
)

plt.close()

print("Saved 06_temperature_heatmap.png")

# -----------------------------
# Average Temperature by City
# -----------------------------

city_avg = (
    df.groupby("City")["Avg Temp (°C)"]
      .mean()
      .reset_index()
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=city_avg,
    x="City",
    y="Avg Temp (°C)"
)

plt.title("Average Temperature by City")

plt.tight_layout()

plt.savefig(
    "images/07_city_temperature.png",
    dpi=300
)

plt.close()

print("Saved 07_city_temperature.png")

# -----------------------------
# Total Rainfall by City
# -----------------------------

rainfall = (
    df.groupby("City")["Rainfall (mm)"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=rainfall,
    x="City",
    y="Rainfall (mm)"
)

plt.title("Total Rainfall by City")

plt.tight_layout()

plt.savefig(
    "images/08_city_rainfall.png",
    dpi=300
)

plt.close()

print("Saved 08_city_rainfall.png")