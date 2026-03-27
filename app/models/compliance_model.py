from pydantic import BaseModel

class ComplianceRequest(BaseModel):
    document_text: str