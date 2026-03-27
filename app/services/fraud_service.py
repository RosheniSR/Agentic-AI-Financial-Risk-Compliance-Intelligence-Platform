from app.services.model.fraud_model import predict_fraud


# -------------------------------
# 🔹 EXISTING ML FRAUD LOGIC
# -------------------------------
def detect_fraud_logic(data):
    """
    Structured fraud detection (amount, frequency based)
    """
    amount = data.get("amount", 0)
    frequency = data.get("frequency", 1)

    risk_score = predict_fraud(amount, frequency)

    return {
        "fraud_score": risk_score,
        "flags": ["High transaction risk"] if risk_score > 50 else []
    }


# -------------------------------
# 🔹 NEW TEXT-BASED FRAUD (USED IN YOUR PIPELINE)
# -------------------------------
def detect_fraud(text):
    """
    Text-based fraud detection from documents
    """

    flags = []
    score = 0

    text_lower = text.lower()

    if "suspicious" in text_lower:
        flags.append("Suspicious keyword detected")
        score += 30

    if "unauthorized" in text_lower:
        flags.append("Unauthorized activity mentioned")
        score += 40

    if "fraud" in text_lower:
        flags.append("Fraud-related content detected")
        score += 50

    return {
        "fraud_score": score,
        "flags": flags
    }