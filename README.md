# Weather Data Analyzer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge\&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

<p align="center">
An end-to-end Weather Data Analytics project that collects, analyzes, visualizes, and forecasts weather data using Python, Machine Learning, and Streamlit.
</p>

---

## Overview

Weather data plays an important role in agriculture, transportation, tourism, and disaster management. This project demonstrates a complete data analytics workflow by collecting weather information from APIs and web scraping, preprocessing historical datasets, performing exploratory and time series analysis, training forecasting models, and visualizing insights through an interactive Streamlit dashboard.

---

## Features

### Data Collection

* Current weather using OpenWeather API
* Historical weather using Open-Meteo API
* Weather forecast collection
* Web scraping with BeautifulSoup

### Data Preprocessing

* Missing value handling
* Duplicate removal
* Feature engineering
* Outlier detection
* Date-time processing

### Exploratory Data Analysis

* Monthly temperature trends
* Seasonal rainfall analysis
* Correlation heatmap
* Temperature distribution
* Wind speed analysis
* City comparison

### Time Series Analysis

* Seasonal decomposition
* Trend analysis
* Stationarity testing (ADF Test)

### Machine Learning

* Naive Forecast
* Linear Regression
* Random Forest Regressor
* Model comparison using MAE and RMSE

### Interactive Dashboard

* City selection
* KPI cards
* Interactive Plotly charts
* Temperature trends
* Rainfall analysis
* City comparison

---

## Tech Stack

| Category         | Technologies                    |
| ---------------- | ------------------------------- |
| Language         | Python                          |
| Data Collection  | Requests, BeautifulSoup4        |
| APIs             | OpenWeather API, Open-Meteo API |
| Data Analysis    | Pandas, NumPy                   |
| Visualization    | Matplotlib, Seaborn, Plotly     |
| Time Series      | Statsmodels                     |
| Machine Learning | Scikit-learn                    |
| Dashboard        | Streamlit                       |
| Version Control  | Git & GitHub                    |

---

## Project Structure

```text
weather-data-analyser/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│   ├── ml/
│   ├── time_series/
│   └── ...
│
├── models/
│
├── src/
│   ├── api_fetch.py
│   ├── forecast_fetch.py
│   ├── historical_fetch.py
│   ├── scraper.py
│   ├── compare_sources.py
│   ├── combine_historical.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── time_series_analysis.py
│   └── forecasting.py
│
├── report/
└── presentation/
```

---

## Project Workflow

```text
Weather APIs + Web Scraping
             │
             ▼
      Data Collection
             │
             ▼
     Data Cleaning & Feature Engineering
             │
             ▼
 Exploratory Data Analysis (EDA)
             │
             ▼
     Time Series Analysis
             │
             ▼
 Machine Learning Forecasting
             │
             ▼
   Interactive Streamlit Dashboard
```

---


## Installation

Clone the repository:

```bash
git clone https://github.com/DHANUSHRI-MUTHUKUMARAN/weather-data-analyser.git
```

Navigate to the project folder:

```bash
cd weather-data-analyser
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

---

## Running Individual Modules

```bash
python src/api_fetch.py
python src/forecast_fetch.py
python src/historical_fetch.py
python src/combine_historical.py
python src/scraper.py
python src/compare_sources.py
python src/data_cleaning.py
python src/eda.py
python src/time_series_analysis.py
python src/forecasting.py
```

---

## Results

* Successfully collected weather data from multiple sources.
* Built a cleaned historical weather dataset.
* Performed exploratory and time series analysis.
* Trained forecasting models using Linear Regression and Random Forest.
* Developed an interactive dashboard for weather visualization.

---

## Future Enhancements

* Real-time weather updates
* Interactive weather maps
* LSTM-based forecasting
* Additional cities and climate variables
* Cloud deployment

---

## Author

**Dhanushri M**

Aspiring Data Analyst | Python Developer | Machine Learning Enthusiast

**GitHub:**
https://github.com/DHANUSHRI-MUTHUKUMARAN

---

## If you found this project useful

Please consider giving this repository a **Star ⭐**. It helps others discover the project and supports future improvements.

---

## License

This project is licensed under the **MIT License**.
