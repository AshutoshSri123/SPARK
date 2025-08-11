import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("data/training_dataset.csv")

# --- STEP 1: Simulate panel specs for now ---
# Assume each location gets a 5 kW system
df['system_size_kw'] = 5

# Assume efficiency between 15% and 22%
np.random.seed(42)
df['panel_efficiency'] = np.random.uniform(0.15, 0.22, size=len(df))

# Annual energy generation (simulated for now)
# kWh/year = irradiance (kWh/m²/day) * 365 days * system_size * efficiency * performance_ratio
performance_ratio = 0.75
df['annual_generation_kwh'] = (
    df['ALLSKY_SFC_SW_DWN'] * 365 * df['system_size_kw'] * df['panel_efficiency'] * performance_ratio
)

# --- STEP 2: Train/test split ---
X = df[['ALLSKY_SFC_SW_DWN', 'T2M', 'system_size_kw', 'panel_efficiency']]
y = df['annual_generation_kwh']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- STEP 3: Train model ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- STEP 4: Evaluate ---
score = model.score(X_test, y_test)
print(f"Model R² score: {score:.3f}")

# --- STEP 5: Save model ---
joblib.dump(model, "models/energy_model.pkl")
print("Model saved to models/energy_model.pkl")
