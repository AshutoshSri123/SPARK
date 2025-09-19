from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Import NASA fetcher
from utils.nasa_power import fetch_nasa_data

# Load trained model
model = joblib.load("models/energy_model.pkl")

# FastAPI app
app = FastAPI(title="SPARK Energy Prediction API")

# Request schema
class LocationRequest(BaseModel):
    latitude: float
    longitude: float
    system_size_kw: float
    panel_efficiency: float = 0.18  # default avg efficiency

@app.get("/")
def read_root():
    return {"message": "SPARK API is running"}

@app.post("/predict")
def predict_energy(data: LocationRequest):
    # Fetch irradiance + temperature
    irradiance, temperature = fetch_nasa_data(data.latitude, data.longitude)

    # Prepare input for model
    input_df = pd.DataFrame([{
        "ALLSKY_SFC_SW_DWN": irradiance,
        "T2M": temperature,
        "system_size_kw": data.system_size_kw,
        "panel_efficiency": data.panel_efficiency
    }])

    # Predict energy
    prediction = model.predict(input_df)[0]

    return {
        "latitude": data.latitude,
        "longitude": data.longitude,
        "irradiance": irradiance,
        "temperature": temperature,
        "system_size_kw": data.system_size_kw,
        "panel_efficiency": data.panel_efficiency,
        "predicted_annual_generation_kwh": prediction
    }
