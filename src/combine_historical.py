import os
import glob
import pandas as pd

# Folder containing historical CSVs
folder = "data/raw/historical"

# Find all CSV files
files = glob.glob(os.path.join(folder, "*.csv"))

if not files:
    print("No CSV files found!")
    exit()

dfs = []

for file in files:
    print(f"Reading: {file}")
    df = pd.read_csv(file)
    dfs.append(df)

# Merge all data
combined = pd.concat(dfs, ignore_index=True)

# Create output folder
os.makedirs("data/processed", exist_ok=True)

# Save combined dataset
output_file = "data/processed/historical_weather.csv"
combined.to_csv(output_file, index=False)

print("\nDataset Created Successfully!")
print(f"Total Rows : {len(combined)}")
print(f"Total Columns : {len(combined.columns)}")

print("\nFirst 5 Rows")
print(combined.head())