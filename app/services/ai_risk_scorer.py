def calculate_ai_compliance_score(missing_elements):

    # 🔥 Define total expected requirements per regulation
    expected_requirements = {
        "GDPR": 2,   # data protection, user consent
        "DORA": 1,   # incident reporting
        "NIS2": 1    # cybersecurity measures
    }

    # 🔥 Weights (importance)
    weights = {
        "GDPR": 40,
        "DORA": 30,
        "NIS2": 30
    }

    total_score = 100
    penalty = 0

    # -------------------------------
    # 🔥 SMART PENALTY CALCULATION
    # -------------------------------
    for regulation, expected_count in expected_requirements.items():

        missing_items = missing_elements.get(regulation, [])
        missing_count = len(missing_items)

        if missing_count > 0:
            # proportion of missing
            ratio = missing_count / expected_count

            # apply weighted penalty proportionally
            penalty += weights[regulation] * ratio

    # -------------------------------
    # 🔥 FINAL SCORE
    # -------------------------------
    final_score = max(0, int(total_score - penalty))

    # -------------------------------
    # 🔥 RISK LEVEL LOGIC (TUNED)
    # -------------------------------
    if final_score >= 75:
        level = "LOW"
    elif final_score >= 45:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return final_score, level