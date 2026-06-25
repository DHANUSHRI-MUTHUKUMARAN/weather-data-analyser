import os
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv("data/processed/weather_cleaned.csv")

df["Date"] = pd.to_datetime(df["Date"])

os.makedirs("images/time_series", exist_ok=True)

cities = df["City"].unique()

for city in cities:

    city_df = (
        df[df["City"] == city]
        .sort_values("Date")
        .set_index("Date")
    )

    series = city_df["Avg Temp (°C)"]

    decomposition = seasonal_decompose(
        series,
        model="additive",
        period=365
    )

    fig = decomposition.plot()

    fig.set_size_inches(15,10)

    plt.suptitle(
        f"{city} Temperature Decomposition",
        fontsize=16
    )

    plt.tight_layout()

    plt.savefig(
        f"images/time_series/{city}_decomposition.png",
        dpi=300
    )

    plt.close()

    print(f"{city} decomposition saved.")

from statsmodels.tsa.stattools import adfuller

print("\n" + "=" * 50)
print("ADF Stationarity Test")
print("=" * 50)

for city in cities:

    city_df = (
        df[df["City"] == city]
        .sort_values("Date")
    )

    result = adfuller(city_df["Avg Temp (°C)"])

    print(f"\n{city}")

    print(f"ADF Statistic : {result[0]:.4f}")

    print(f"P-value       : {result[1]:.4f}")

    if result[1] < 0.05:
        print("Series is Stationary")
    else:
        print("Series is Non-Stationary")
import numpy as np

print("\n" + "=" * 50)
print("Temperature Trend")
print("=" * 50)

for city in cities:

    city_df = (
        df[df["City"] == city]
        .sort_values("Date")
        .reset_index(drop=True)
    )

    x = np.arange(len(city_df))

    y = city_df["Avg Temp (°C)"]

    slope, intercept = np.polyfit(x, y, 1)

    print(f"{city}: {slope:.6f} °C/day")