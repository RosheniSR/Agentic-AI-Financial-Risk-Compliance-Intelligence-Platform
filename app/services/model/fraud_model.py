import joblib
import numpy as np

MODEL_VERSION = "v1"
MODEL_PATH = f"model_registry/fraud_model_{MODEL_VERSION}.pkl"

# Load model once
model = joblib.load(MODEL_PATH)

def predict_fraud(amount, frequency):
    data = np.array([[amount, frequency]])
    prediction = model.predict(data)

    if prediction[0] == -1:
        return 0.9
    else:
        return 0.1