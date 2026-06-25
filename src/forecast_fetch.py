import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API Key
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

cities = [
    "Chennai",
    "Mumbai",
    "Delhi",
    "London",
    "New York"
]

# Create folders
os.makedirs("data/raw/forecast_json", exist_ok=True)
os.makedirs("data/raw/forecast_csv", exist_ok=True)

for city in cities:

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Failed for {city}")
        print(data)
        continue

    # Save complete JSON
    with open(f"data/raw/forecast_json/{city}.json", "w") as f:
        json.dump(data, f, indent=4)

    forecast = []

    for item in data["list"]:

        forecast.append({
            "City": city,
            "Datetime": item["dt_txt"],
            "Temperature (°C)": item["main"]["temp"],
            "Feels Like (°C)": item["main"]["feels_like"],
            "Humidity (%)": item["main"]["humidity"],
            "Pressure (hPa)": item["main"]["pressure"],
            "Wind Speed (m/s)": item["wind"]["speed"],
            "Condition": item["weather"][0]["main"],
            "Description": item["weather"][0]["description"]
        })

    df = pd.DataFrame(forecast)

    df.to_csv(
        f"data/raw/forecast_csv/{city}_forecast.csv",
        index=False
    )

    print(f"{city} Forecast Saved ({len(df)} records)")