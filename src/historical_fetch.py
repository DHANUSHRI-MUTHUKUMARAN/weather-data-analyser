import os
import requests
import pandas as pd

# City coordinates
cities = {
    "Chennai": (13.0827, 80.2707),
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "London": (51.5074, -0.1278),
    "New York": (40.7128, -74.0060)
}

os.makedirs("data/raw/historical", exist_ok=True)

START_DATE = "2021-01-01"
END_DATE = "2025-12-31"

for city, (lat, lon) in cities.items():

    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&start_date={START_DATE}"
        f"&end_date={END_DATE}"
        "&daily=temperature_2m_max,"
        "temperature_2m_min,"
        "precipitation_sum,"
        "windspeed_10m_max"
        "&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed: {city}")
        continue

    data = response.json()

    df = pd.DataFrame({
        "Date": data["daily"]["time"],
        "Max Temp (°C)": data["daily"]["temperature_2m_max"],
        "Min Temp (°C)": data["daily"]["temperature_2m_min"],
        "Rainfall (mm)": data["daily"]["precipitation_sum"],
        "Max Wind (km/h)": data["daily"]["windspeed_10m_max"]
    })

    df["City"] = city

    df.to_csv(
        f"data/raw/historical/{city}_historical.csv",
        index=False
    )

    print(f"{city}: {len(df)} records saved")