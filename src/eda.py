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