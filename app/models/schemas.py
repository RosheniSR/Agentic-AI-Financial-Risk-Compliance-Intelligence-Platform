from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


# ==============================
# 🔷 COMMON BASE RESPONSE
# ==============================

class BaseResponse(BaseModel):
    status: str = "success"
    message: Optional[str] = None


# ==============================
# 🔷 FRAUD MODULE SCHEMAS
# ==============================

class TransactionRequest(BaseModel):
    amount: float = Field(..., example=5000.0)
    frequency: int = Field(..., example=3)


class FraudResponse(BaseModel):
    risk_score: float
    message: str


# ==============================
# 🔷 AGENT DECISION SCHEMAS
# ==============================

class DecisionResponse(BaseModel):
    action: str
    level: str
    ai_message: str


class AgentResponse(BaseModel):
    fraud_analysis: FraudResponse
    decision: DecisionResponse


# ==============================
# 🔷 COMPLIANCE MODULE SCHEMAS (NEW)
# ==============================

class ComplianceRequest(BaseModel):
    document_text: str = Field(
        ...,
        example="This policy ensures data protection, user consent, and cybersecurity measures."
    )


class ComplianceResponse(BaseModel):
    compliance_score: float = Field(..., example=80.0)
    risk_level: str = Field(..., example="LOW")
    
    detected_regulations: Dict[str, Any] = Field(
        ...,
        example={
            "GDPR": ["data protection"],
            "NIS2": ["cybersecurity"]
        }
    )
    
    missing_requirements: Dict[str, Any] = Field(
        ...,
        example={
            "DORA": ["incident reporting"]
        }
    )
    
    ai_explanation: str = Field(
        ...,
        example="The system partially complies with GDPR and NIS2 but lacks DORA incident reporting mechanisms."
    )