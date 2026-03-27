from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load model once (global)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Regulation requirements
REGULATIONS = {
    "GDPR": ["data protection", "user consent"],
    "DORA": ["incident reporting"],
    "NIS2": ["cybersecurity", "risk management"]
}

# Convert requirements into embeddings (precompute)
regulation_embeddings = {}

for reg, requirements in REGULATIONS.items():
    regulation_embeddings[reg] = model.encode(requirements)


def detect_regulations_semantic(text: str):
    text = text.lower()

    detected = {}
    missing = {}

    # ---------------- NIS2 ----------------
    if "cybersecurity" in text:
        detected.setdefault("NIS2", []).append("cybersecurity")

    if "risk management" not in text:
        missing.setdefault("NIS2", []).append("risk management")

    # ---------------- GDPR ----------------
    if "data protection" in text:
        detected.setdefault("GDPR", []).append("data protection")

    if "user consent" in text:
        detected.setdefault("GDPR", []).append("user consent")

    if "user consent" not in text:
        missing.setdefault("GDPR", []).append("user consent")

    if "data" in text and "user consent" not in text:
        missing.setdefault("GDPR", []).append("user consent")

    # ---------------- DORA ----------------
    if "incident reporting" in text:
        detected.setdefault("DORA", []).append("incident reporting")

    if "incident" in text and "report" not in text:
        missing.setdefault("DORA", []).append("incident reporting")

    return detected, missing