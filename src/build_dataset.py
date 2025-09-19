import pandas as pd
from utils.nasa_power import fetch_nasa_data

# Example cities (lat, lon)
cities = {
    "Delhi": (28.61, 77.21),
    "Mumbai": (19.07, 72.87),
    "Bengaluru": (12.97, 77.59),
}

rows = []
for name, (lat, lon) in cities.items():
    irradiance, temperature = fetch_nasa_data(lat, lon)
    system_size_kw = 5
    panel_efficiency = 0.18

    # Simulated formula for annual generation
    annual_gen = irradiance * system_size_kw * panel_efficiency * 365 * 0.75  # 0.75 = perf ratio

    rows.append({
        "city": name,
        "latitude": lat,
        "longitude": lon,
        "ALLSKY_SFC_SW_DWN": irradiance,
        "T2M": temperature,
        "system_size_kw": system_size_kw,
        "panel_efficiency": panel_efficiency,
        "annual_generation_kwh": annual_gen
    })

df = pd.DataFrame(rows)
df.to_csv("data/training_dataset.csv", index=False)
print("✅ Dataset saved at data/training_dataset.csv")
