import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

# Ensure folder exists
os.makedirs("model_registry", exist_ok=True)

# Training data
X_train = np.array([
    [100, 1],
    [200, 2],
    [150, 1],
    [300, 3],
    [5000, 10],
    [7000, 15],
])

# Train model
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X_train)

# Versioning
MODEL_VERSION = "v1"
model_path = f"model_registry/fraud_model_{MODEL_VERSION}.pkl"

# Save model
joblib.dump(model, model_path)

print(f"✅ Model saved at {model_path}")