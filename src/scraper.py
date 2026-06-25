import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

cities = [
    "Chennai",
    "Mumbai",
    "Delhi",
    "London",
    "New York"
]

os.makedirs("data/raw/scraped", exist_ok=True)

weather_data = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for city in cities:

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed: {city}")
        continue

    data = response.json()

    current = data["current_condition"][0]

    weather_data.append({
        "City": city,
        "Temperature (°C)": current["temp_C"],
        "Humidity (%)": current["humidity"],
        "Wind Speed (km/h)": current["windspeedKmph"],
        "Pressure": current["pressure"],
        "Visibility": current["visibility"],
        "Condition": current["weatherDesc"][0]["value"]
    })

    print(f"{city} scraped successfully")

    time.sleep(2)

df = pd.DataFrame(weather_data)

df.to_csv(
    "data/raw/scraped/weather_scraped.csv",
    index=False
)

print(df)