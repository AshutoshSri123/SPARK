import pandas as pd
from fetch_nasa_power import fetch_nasa_power

# Sample coordinates (lat, lon) for different cities
locations = [
    (28.6139, 77.2090),  # New Delhi, India
    (19.0760, 72.8777),  # Mumbai, India
    (40.7128, -74.0060), # New York, USA
    (51.5074, -0.1278),  # London, UK
    (-33.8688, 151.2093) # Sydney, Australia
]

all_data = []

for lat, lon in locations:
    df = fetch_nasa_power(lat, lon)
    all_data.append(df)

# Combine into one DataFrame
final_df = pd.concat(all_data, ignore_index=True)

# Save combined dataset
final_df.to_csv("data/training_dataset.csv", index=False)
print("Training dataset saved to data/training_dataset.csv")
