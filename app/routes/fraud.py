from fastapi import APIRouter
from app.services.fraud_service import detect_fraud_logic

router = APIRouter()

@router.post("/detect-fraud")
def detect_fraud(data: dict):
    result = detect_fraud_logic(data)
    return result