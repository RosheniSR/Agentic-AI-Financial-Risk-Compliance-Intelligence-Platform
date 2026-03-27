from dotenv import load_dotenv
import os
from app.services.llm_service import generate_explanation

load_dotenv()


# ---------------------------------------------------
# 🔹 EXISTING: TRANSACTION DECISION AGENT (KEEP THIS)
# ---------------------------------------------------
def agent_decision_logic(risk_score: float):

    # Step 1: Decision logic
    if risk_score >= 0.8:
        action = "FREEZE_ACCOUNT"
        level = "HIGH"
    elif risk_score >= 0.5:
        action = "FLAG_TRANSACTION"
        level = "MEDIUM"
    else:
        action = "ALLOW"
        level = "LOW"

    # Step 2: LLM Prompt
    prompt = f"""
A financial transaction has been analyzed.

Risk Score: {risk_score}
Decision: {action}
Risk Level: {level}

Explain this decision in EXACTLY 2 short sentences.
Keep each sentence under 12 words.
Do NOT give long explanations.
"""

    # Step 3: Call LLM
    ai_message = generate_explanation(prompt)

    return {
        "action": action,
        "level": level,
        "ai_message": ai_message
    }


# ---------------------------------------------------
# 🔥 NEW: COMPLIANCE ACTION AGENT
# ---------------------------------------------------
def generate_actions(detected, missing):
    actions = []

    for reg, reqs in missing.items():
        for req in reqs:

            # 🔹 NIS2 Fix
            if req == "risk management":
                actions.append("Implement a formal cybersecurity risk management framework")

            # 🔹 GDPR Fix
            elif req == "user consent":
                actions.append("Add explicit user consent mechanisms for all users")

            # 🔹 DORA Fix
            elif req == "incident reporting":
                actions.append("Establish an incident detection and reporting system")

    return actions


# ---------------------------------------------------
# 🔥 OPTIONAL: AI-ENHANCED AGENT (SMART MODE)
# ---------------------------------------------------
def generate_ai_actions(detected, missing):
    """
    Use LLM to generate smarter compliance suggestions
    """

    prompt = f"""
You are a compliance advisor.

Detected Regulations:
{detected}

Missing Requirements:
{missing}

Suggest 2–3 clear actions to fix compliance gaps.
Keep it short and practical.
Do not hallucinate.
"""

    try:
        response = generate_explanation(prompt)
    except Exception as e:
        print("Agent AI Error:", e)
        response = "Unable to generate AI recommendations."

    return response