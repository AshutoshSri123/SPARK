import requests

def fetch_nasa_data(lat: float, lon: float):
    """
    Fetch average annual solar irradiance and temperature
    for given latitude and longitude using NASA POWER API.
    """
    url = f"https://power.larc.nasa.gov/api/temporal/climatology/point?parameters=ALLSKY_SFC_SW_DWN,T2M&community=RE&longitude={lon}&latitude={lat}&format=JSON"
    response = requests.get(url)
    data = response.json()["properties"]["parameter"]

    # Compute mean values across months
    irradiance = sum(data["ALLSKY_SFC_SW_DWN"].values()) / len(data["ALLSKY_SFC_SW_DWN"])
    temperature = sum(data["T2M"].values()) / len(data["T2M"])

    return irradiance, temperature
