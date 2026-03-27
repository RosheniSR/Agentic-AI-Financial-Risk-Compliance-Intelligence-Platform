from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_audit_report(data, filename="audit_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    for item in data:
        elements.append(Paragraph(f"File: {item['file_name']}", styles["Heading2"]))
        elements.append(Spacer(1, 10))

        analysis = item["analysis"]

        elements.append(Paragraph(f"Score: {analysis['compliance_score']}", styles["Normal"]))
        elements.append(Paragraph(f"Risk: {analysis['risk_level']}", styles["Normal"]))
        elements.append(Paragraph(f"Explanation: {analysis['ai_explanation']}", styles["Normal"]))

        elements.append(Spacer(1, 20))

    doc.build(elements)

    return filename
