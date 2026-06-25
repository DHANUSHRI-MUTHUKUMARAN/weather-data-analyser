import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error
)

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv("data/processed/weather_cleaned.csv")

# Features
features = [
    "Lag1",
    "Lag7",
    "Rolling Avg 7",
    "Rolling Avg 30",
    "Month"
]

target = "Avg Temp (°C)"

X = df[features]
y = df[target]

# ---------------------------------
# Train Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ---------------------------------
# Linear Regression
# ---------------------------------

linear = LinearRegression()

linear.fit(X_train, y_train)

linear_pred = linear.predict(X_test)

# ---------------------------------
# Random Forest
# ---------------------------------

forest = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

forest.fit(X_train, y_train)

forest_pred = forest.predict(X_test)

# ---------------------------------
# Naive Model
# ---------------------------------

naive_pred = X_test["Lag1"]

# ---------------------------------
# Evaluation Function
# ---------------------------------

def evaluate(name, y_true, prediction):

    mae = mean_absolute_error(
        y_true,
        prediction
    )

    rmse = root_mean_squared_error(
        y_true,
        prediction
    )

    print(f"\n{name}")
    print("-"*35)
    print(f"MAE  : {mae:.3f}")
    print(f"RMSE : {rmse:.3f}")

evaluate("Naive", y_test, naive_pred)
evaluate("Linear Regression", y_test, linear_pred)
evaluate("Random Forest", y_test, forest_pred)

# ---------------------------------
# Save Best Model
# ---------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    forest,
    "models/random_forest_weather.pkl"
)

print("\nRandom Forest model saved.")

# ---------------------------------
# Prediction Plot
# ---------------------------------

plt.figure(figsize=(12,6))

plt.plot(
    y_test.values[:200],
    label="Actual"
)

plt.plot(
    forest_pred[:200],
    label="Predicted"
)

plt.legend()

plt.title("Actual vs Predicted Temperature")

plt.tight_layout()

os.makedirs("images/ml", exist_ok=True)

plt.savefig(
    "images/ml/actual_vs_predicted.png",
    dpi=300
)

plt.close()

print("Prediction plot saved.")