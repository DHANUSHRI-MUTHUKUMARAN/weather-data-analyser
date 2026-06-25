import os
import pandas as pd
import numpy as np

# =====================================================
# Load Dataset
# =====================================================

INPUT_FILE = "data/processed/historical_weather.csv"
OUTPUT_FILE = "data/processed/weather_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("ORIGINAL DATASET INFORMATION")
print("=" * 60)
print(df.info())

# =====================================================
# Convert Date Column
# =====================================================

df["Date"] = pd.to_datetime(df["Date"])

# Sort dataset
df = df.sort_values(["City", "Date"]).reset_index(drop=True)

# =====================================================
# Missing Values
# =====================================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna().reset_index(drop=True).copy()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# =====================================================
# Remove Duplicates
# =====================================================

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df = df.drop_duplicates().reset_index(drop=True).copy()

# =====================================================
# Date Features
# =====================================================

df["Year"] = df["Date"].dt.year
df["Quarter"] = df["Date"].dt.quarter
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.day_name()

# =====================================================
# Season Feature
# =====================================================

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8, 9]:
        return "Monsoon"
    else:
        return "Autumn"

df["Season"] = df["Month"].apply(get_season)

# =====================================================
# Derived Temperature Features
# =====================================================

df["Avg Temp (°C)"] = (
    df["Max Temp (°C)"] +
    df["Min Temp (°C)"]
) / 2

df["Temp Range (°C)"] = (
    df["Max Temp (°C)"] -
    df["Min Temp (°C)"]
)

# =====================================================
# Rolling Features
# =====================================================

df["Rolling Avg 7"] = (
    df.groupby("City")["Avg Temp (°C)"]
      .transform(lambda x: x.rolling(7, min_periods=1).mean())
)

df["Rolling Avg 30"] = (
    df.groupby("City")["Avg Temp (°C)"]
      .transform(lambda x: x.rolling(30, min_periods=1).mean())
)

# =====================================================
# Lag Features
# =====================================================

df["Lag1"] = (
    df.groupby("City")["Avg Temp (°C)"]
      .shift(1)
)

df["Lag7"] = (
    df.groupby("City")["Avg Temp (°C)"]
      .shift(7)
)

df["Lag1"] = df["Lag1"].fillna(df["Avg Temp (°C)"])
df["Lag7"] = df["Lag7"].fillna(df["Avg Temp (°C)"])

# =====================================================
# Advanced Feature Engineering
# =====================================================

# Monthly average temperature
df["Monthly Avg Temp"] = (
    df.groupby(["City", "Year", "Month"])["Avg Temp (°C)"]
      .transform("mean")
)

# Temperature anomaly
df["Temp Anomaly"] = (
    df["Avg Temp (°C)"] -
    df["Monthly Avg Temp"]
)

# Rainy day indicator
df["Rainy Day"] = (
    df["Rainfall (mm)"] > 0
).astype(int)

# Rainfall Category
def rainfall_category(rain):

    if rain == 0:
        return "No Rain"
    elif rain < 10:
        return "Light"
    elif rain < 30:
        return "Moderate"
    else:
        return "Heavy"

df["Rainfall Category"] = (
    df["Rainfall (mm)"]
    .apply(rainfall_category)
)

# Temperature Category
def temperature_category(temp):

    if temp < 10:
        return "Cold"
    elif temp < 20:
        return "Cool"
    elif temp < 30:
        return "Warm"
    else:
        return "Hot"

df["Temperature Category"] = (
    df["Avg Temp (°C)"]
    .apply(temperature_category)
)

# Weekend
df["Is Weekend"] = (
    df["DayOfWeek"]
    .isin(["Saturday", "Sunday"])
)

# Cumulative Rainfall
df["Cumulative Rainfall"] = (
    df.groupby("City")["Rainfall (mm)"]
      .cumsum()
)

# =====================================================
# Outlier Detection (IQR)
# =====================================================

Q1 = df["Avg Temp (°C)"].quantile(0.25)
Q3 = df["Avg Temp (°C)"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["Outlier"] = (
    (df["Avg Temp (°C)"] < lower_bound) |
    (df["Avg Temp (°C)"] > upper_bound)
)

print(f"\nOutliers Detected: {df['Outlier'].sum()}")

# =====================================================
# Arrange Columns
# =====================================================

column_order = [
    "Date",
    "City",
    "Year",
    "Quarter",
    "Month",
    "Day",
    "DayOfWeek",
    "Season",
    "Max Temp (°C)",
    "Min Temp (°C)",
    "Avg Temp (°C)",
    "Temp Range (°C)",
    "Rainfall (mm)",
    "Rainy Day",
    "Rainfall Category",
    "Max Wind (km/h)",
    "Rolling Avg 7",
    "Rolling Avg 30",
    "Lag1",
    "Lag7",
    "Monthly Avg Temp",
    "Temp Anomaly",
    "Temperature Category",
    "Is Weekend",
    "Cumulative Rainfall",
    "Outlier"
]

df = df[column_order]

# =====================================================
# Save Dataset
# =====================================================

os.makedirs("data/processed", exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"Final Shape : {df.shape}")
print(f"Columns     : {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())

print(f"\nDataset saved to:\n{OUTPUT_FILE}")