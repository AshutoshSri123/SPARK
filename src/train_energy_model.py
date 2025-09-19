import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("data/training_dataset.csv")

# Features & target
X = df[["ALLSKY_SFC_SW_DWN", "T2M", "system_size_kw", "panel_efficiency"]]
y = df["annual_generation_kwh"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "models/energy_model.pkl")

print("✅ Model trained and saved to models/energy_model.pkl")
