from fastapi import APIRouter, UploadFile, File
from typing import List

from app.services.compliance_service import analyze_compliance
from app.services.document_loader import load_pdf_text
from app.services.report_generator import generate_audit_report
from app.services.fraud_service import detect_fraud   # ✅ ADD
from app.services.regulation_mapper import map_regulations  # ✅ ADD

router = APIRouter()


# -------------------------------
# 📄 UPLOAD + ANALYZE
# -------------------------------
@router.post("/upload-and-analyze")
async def upload_and_analyze(files: List[UploadFile] = File(...)):
    results = []

    for file in files:
        content = await file.read()

        # Save temp file
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(content)

        # 📄 Extract text
        text = load_pdf_text(file_path)

        # 🔒 SAFETY LIMIT (VERY IMPORTANT)
        text = text[:3000]

        # 📊 Compliance Analysis
        analysis = analyze_compliance(text)

        # 💸 Fraud Detection
        fraud_result = detect_fraud(text)

        # 📜 Regulation Mapping
        mapped_regs = map_regulations(text)

        # 🧠 BUILD FINAL RESPONSE
        results.append({
            "file_name": file.filename,

            "analysis": {
                "compliance_score": analysis.get("compliance_score", 0),
                "risk_level": analysis.get("risk_level", "UNKNOWN"),
                "ai_explanation": analysis.get("ai_explanation", ""),
                "recommended_actions": analysis.get("recommended_actions", [])
            },

            "fraud_score": fraud_result.get("fraud_score", 0),
            "fraud_flags": fraud_result.get("flags", []),

            "mapped_regulations": mapped_regs
        })

    return {"results": results}


# -------------------------------
# 📑 GENERATE REPORT
# -------------------------------
@router.post("/generate-report")
async def generate_report(data: dict):
    file_path = generate_audit_report(data["results"])
    return {"report_path": file_path}