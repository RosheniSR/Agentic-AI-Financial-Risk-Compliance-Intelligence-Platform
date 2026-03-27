# 🔥 REQUIRED RULES PER REGULATION
REQUIRED_ELEMENTS = {
    "GDPR": ["data protection", "user consent"],
    "DORA": ["incident reporting"],
    "NIS2": ["cybersecurity", "risk management"]
}


def check_compliance(mapped_regs):

    missing = {}

    for reg, required_items in REQUIRED_ELEMENTS.items():

        detected_items = mapped_regs.get(reg, [])

        missing_items = []

        # 🔥 Check each requirement inside regulation
        for item in required_items:
            if item not in detected_items:
                missing_items.append(item)

        # 🔥 Only add if something is missing
        if missing_items:
            missing[reg] = missing_items

    return missing