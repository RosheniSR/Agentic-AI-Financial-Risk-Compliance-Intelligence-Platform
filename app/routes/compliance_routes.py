from fastapi import APIRouter
from app.models.compliance_model import ComplianceRequest
from app.services.compliance_service import analyze_compliance

router = APIRouter()

@router.post("/check-compliance")
def check_compliance_api(request: ComplianceRequest):
    return analyze_compliance(request.document_text)