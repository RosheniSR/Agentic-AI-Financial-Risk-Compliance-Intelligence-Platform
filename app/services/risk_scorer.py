def calculate_ai_compliance_score(missing_elements):

    # 🔥 Total possible requirements
    TOTAL_REQUIREMENTS = 5  # GDPR(2) + DORA(1) + NIS2(2)

    # 🔥 Count missing items
    missing_count = sum(len(v) for v in missing_elements.values())

    # 🔥 Balanced scoring (NOT aggressive)
    score = max(0, int(100 - (missing_count * 15)))

    # 🔥 Risk levels (better distribution)
    if score >= 75:
        level = "LOW"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return score, level