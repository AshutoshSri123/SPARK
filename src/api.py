from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/energy_model.pkl")

# FastAPI app
app = FastAPI(title="SPARK Energy Prediction API")

# Request schema
class PredictionRequest(BaseModel):
    irradiance: float
    temperature: float
    system_size_kw: float
    panel_efficiency: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "SPARK API is running"}

# Prediction endpoint
@app.post("/predict")
def predict_energy(data: PredictionRequest):
    input_df = pd.DataFrame([{
        "ALLSKY_SFC_SW_DWN": data.irradiance,
        "T2M": data.temperature,
        "system_size_kw": data.system_size_kw,
        "panel_efficiency": data.panel_efficiency
    }])
    prediction = model.predict(input_df)[0]
    return {"annual_generation_kwh": prediction}
