import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cities = [
    "Chennai",
    "Mumbai",
    "Delhi",
    "London",
    "New York"
]

# Create folders automatically
os.makedirs("data/raw/json", exist_ok=True)
os.makedirs("data/raw/csv", exist_ok=True)

weather_data = []

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

    # Save raw JSON
    with open(f"data/raw/json/{city}.json", "w") as file:
        json.dump(data, file, indent=4)

    weather_data.append({
        "City": city,
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Humidity (%)": data["main"]["humidity"],
        "Pressure (hPa)": data["main"]["pressure"],
        "Wind Speed (m/s)": data["wind"]["speed"],
        "Visibility (m)": data["visibility"],
        "Condition": data["weather"][0]["main"],
        "Description": data["weather"][0]["description"],
        "Country": data["sys"]["country"],
        "Latitude": data["coord"]["lat"],
        "Longitude": data["coord"]["lon"]
    })

df = pd.DataFrame(weather_data)

df.to_csv("data/raw/csv/current_weather.csv", index=False)

print("\nWeather data collected successfully!\n")
print(df)