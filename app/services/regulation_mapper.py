REGULATIONS = {
    "GDPR": ["data protection", "personal data", "privacy"],
    "DORA": ["risk management", "incident reporting", "resilience"],
    "NIS2": ["cybersecurity", "network security", "incident response"]
}

def map_regulations(tokens):

    # 🔥 Convert tokens → FULL TEXT
    text = " ".join(tokens).lower()

    mapped = {}

    # -------------------
    # GDPR
    # -------------------
    if "data protection" in text:
        mapped.setdefault("GDPR", []).append("data protection")

    if "user consent" in text or "consent" in text:
        mapped.setdefault("GDPR", []).append("user consent")

    # -------------------
    # DORA
    # -------------------
    if "incident reporting" in text or "incident" in text:
        mapped.setdefault("DORA", []).append("incident reporting")

    # -------------------
    # NIS2
    # -------------------
    if "cybersecurity" in text or "security" in text:
        mapped.setdefault("NIS2", []).append("cybersecurity")

    if "risk management" in text or "risk" in text:
        mapped.setdefault("NIS2", []).append("risk management")

    return mapped