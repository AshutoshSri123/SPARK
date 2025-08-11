import requests
import pandas as pd
from datetime import datetime

def fetch_nasa_power(lat, lon, start_year=2015, end_year=2020):
    """
    Fetches NASA POWER solar irradiance and temperature data for a location.
    Data is monthly averaged over the given period.
    """
    url = (
        f"https://power.larc.nasa.gov/api/temporal/climatology/point"
        f"?parameters=ALLSKY_SFC_SW_DWN,T2M"
        f"&community=RE"
        f"&longitude={lon}"
        f"&latitude={lat}"
        f"&format=JSON"
    )

    print(f"Fetching data for lat={lat}, lon={lon}...")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data['properties']['parameter'])
    df['LAT'] = lat
    df['LON'] = lon
    return df

if __name__ == "__main__":
    # Example: New Delhi coordinates
    lat, lon = 28.6139, 77.2090
    df = fetch_nasa_power(lat, lon)

    # Save dataset
    filename = f"data/nasa_power_{lat}_{lon}.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
