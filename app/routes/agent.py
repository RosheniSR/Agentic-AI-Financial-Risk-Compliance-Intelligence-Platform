from fastapi import APIRouter
from app.services.fraud_service import detect_fraud_logic
from app.services.agent_service import agent_decision_logic

router = APIRouter()

@router.post("/decision-agent")
def decision_agent(data: dict):
    # Step 1: Get fraud score
    fraud_result = detect_fraud_logic(data)
    risk_score = fraud_result["risk_score"]

    # Step 2: Make decision
    decision = agent_decision_logic(risk_score)

    return {
        "fraud_analysis": fraud_result,
        "decision": decision
    }