import os
import pandas as pd

# Read datasets
api = pd.read_csv("data/raw/csv/current_weather.csv")
scraped = pd.read_csv("data/raw/scraped/weather_scraped.csv")

# Rename scraped columns to match API
scraped = scraped.rename(columns={
    "Pressure": "Pressure (hPa)",
    "Visibility": "Visibility (m)",
    "Wind Speed (km/h)": "Wind Speed (km/h)"
})

# Convert numeric columns
numeric_cols = [
    "Temperature (°C)",
    "Humidity (%)",
    "Pressure (hPa)",
    "Visibility (m)"
]

for col in numeric_cols:
    api[col] = pd.to_numeric(api[col], errors="coerce")
    scraped[col] = pd.to_numeric(scraped[col], errors="coerce")

# Merge
comparison = api.merge(
    scraped,
    on="City",
    suffixes=("_API", "_Scraped")
)

# Differences
comparison["Temp Difference"] = (
    comparison["Temperature (°C)_API"]
    - comparison["Temperature (°C)_Scraped"]
)

comparison["Humidity Difference"] = (
    comparison["Humidity (%)_API"]
    - comparison["Humidity (%)_Scraped"]
)

comparison["Pressure Difference"] = (
    comparison["Pressure (hPa)_API"]
    - comparison["Pressure (hPa)_Scraped"]
)

os.makedirs("data/processed", exist_ok=True)

comparison.to_csv(
    "data/processed/weather_comparison.csv",
    index=False
)

print(comparison)