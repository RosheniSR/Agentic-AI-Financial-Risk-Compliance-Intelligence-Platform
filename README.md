# Agentic AI Financial Risk & Compliance Intelligence Platform

## Overview

This project is an AI-powered backend system designed to simulate a real-world **FinTech + RegTech platform**. It performs fraud detection, EU regulatory compliance analysis, and generates explainable AI-driven decisions using modern technologies like RAG and LLMs.

---

##  Key Features

* 🔍 Fraud detection using rule-based and extensible ML logic
* 📊 Compliance analysis for EU regulations:

  * GDPR
  * DORA
  * NIS2
* ⚖️ AI-based risk scoring (LOW / MEDIUM / HIGH)
* 🧠 RAG (Retrieval-Augmented Generation) pipeline using FAISS
* 🤖 LLM-based explanation generation (Groq - LLaMA 3.1)
* 📄 Multi-document analysis (PDF input support)
* 🧾 Audit report generation

---

## System Architecture

The backend follows a **modular service-based architecture**:

* FastAPI → API layer
* Services → business logic (fraud, compliance, scoring)
* RAG pipeline → regulatory retrieval
* LLM → explainable AI output

---

## ⚙️ Tech Stack

* Backend: FastAPI
* NLP: Custom processing + sentence-transformers
* Vector DB: FAISS
* LLM: Groq (LLaMA 3.1)
* Language: Python

---

##  Workflow

1. User uploads document (PDF)
2. Text extraction and preprocessing
3. Compliance mapping (GDPR, DORA, NIS2)
4. Risk scoring based on missing requirements
5. RAG retrieves relevant regulatory content
6. LLM generates explanation
7. Final structured JSON response

---

## Sample Output

```json
{
  "compliance_score": 55,
  "risk_level": "MEDIUM",
  "fraud_score": 0,
  "recommended_actions": [
    "Implement cybersecurity risk management framework",
    "Add explicit user consent mechanisms",
    "Establish incident reporting system"
  ]
}
```

---

##  Project Structure

```
app/
 ├── routes/
 ├── services/
 ├── models/
 ├── main.py
```

---

##  Getting Started

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
uvicorn main:app --reload
```

### 4️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

##  Future Enhancements

* Semantic regulation detection (embedding-based)
* Real-time streaming (Kafka integration)
* Frontend dashboard (React / Streamlit)
* Cloud deployment (AWS / Azure)
* Authentication and role-based access

---

## 🤝 Contributing

Open to suggestions and improvements — especially in system design, RAG optimization, and compliance modeling.

---

## 📌 Author

Developed as part of an advanced AI/FinTech project aligned with EU regulatory systems and real-world backend architecture practices.
