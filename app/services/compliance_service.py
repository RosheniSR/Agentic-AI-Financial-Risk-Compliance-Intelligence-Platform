from app.services.nlp_processor import preprocess_text
from app.services.semantic_mapper import detect_regulations_semantic
from app.services.llm_service import generate_explanation

# 🔥 NEW IMPORT
from app.services.reranker import rerank_chunks
import numpy as np

# 🔥 FAISS + EMBEDDING
from app.services.vector_store import search_index
from app.services.embedding_service import model
from app.services.init_vector_db import index, chunks
from app.services.agent_service import generate_actions


def analyze_compliance(document_text: str):

    # -------------------------------
    # STEP 1 — NLP Processing
    # -------------------------------
    nlp_data = preprocess_text(document_text)

    # -------------------------------
    # STEP 2 — SEMANTIC REGULATION DETECTION
    # -------------------------------
    detected_regs, missing_reqs = detect_regulations_semantic(document_text)

    print("Detected Regulations:", detected_regs)
    print("Missing Requirements (Semantic):", missing_reqs)

    # -------------------------------
    # STEP 3 — USE SEMANTIC OUTPUT
    # -------------------------------
    missing = missing_reqs

    # -------------------------------
    # STEP 4 — SCORING
    # -------------------------------
    total_requirements = 5
    missing_count = sum(len(v) for v in missing.values())

    score = 100 - (missing_count * 15)

    if score >= 75:
        level = "LOW"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "HIGH"

    print("Score:", score, "Risk Level:", level)

    # -------------------------------
    # STEP 5 — EMBEDDING
    # -------------------------------
    query_embedding = model.encode(document_text)

    # -------------------------------
    # STEP 6 — FAISS SEARCH
    # -------------------------------
    retrieved_chunks, chunk_embeddings = search_index(
        query_embedding=query_embedding,
        index=index,
        chunks=chunks,
        k=10
    )

    chunk_embeddings = np.array(chunk_embeddings)

    # -------------------------------
    # STEP 7 — REGULATION FILTERING
    # -------------------------------
    filtered_chunks = []
    filtered_embeddings = []

    for i, chunk in enumerate(retrieved_chunks):
        if chunk["regulation"] in detected_regs:
            filtered_chunks.append(chunk["text"])
            filtered_embeddings.append(chunk_embeddings[i])

    # Fallback
    if not filtered_chunks:
        filtered_chunks = [c["text"] for c in retrieved_chunks]
        filtered_embeddings = chunk_embeddings

    print("Filtered Chunks:", filtered_chunks)

    # -------------------------------
    # STEP 8 — RERANKING
    # -------------------------------
    relevant_sections = rerank_chunks(
        query_embedding=query_embedding,
        chunk_embeddings=np.array(filtered_embeddings),
        chunks=filtered_chunks,
        top_k=3,
        threshold=0.5
    )

    relevant_sections = [sec[:300] for sec in relevant_sections]

    print("Final RAG Sections:", relevant_sections)

    # -------------------------------
    # STEP 9 — LLM PROMPT
    # -------------------------------
    prompt = f"""
You are an EU compliance analyst.

Use ONLY the provided regulation sections as reference.

User Document:
{document_text}

Relevant EU Regulation Sections:
{relevant_sections}

Detected Regulations:
{detected_regs}

Missing Requirements:
{missing}

Compliance Score: {score}
Risk Level: {level}

TASK:
Write a short explanation (2–3 lines).
Be clear, professional, and accurate.
Do not hallucinate.
"""

    # -------------------------------
    # STEP 10 — LLM CALL
    # -------------------------------
    try:
        explanation = generate_explanation(prompt)
    except Exception as e:
        print("❌ ERROR in LLM:", e)
        explanation = "AI explanation unavailable."

    # -------------------------------
    # 🔥 STEP 11 — AGENTIC ACTIONS (FIXED POSITION)
    # -------------------------------
    actions = generate_actions(detected_regs, missing)

    # -------------------------------
    # STEP 12 — FINAL RESPONSE
    # -------------------------------
    return {
        "compliance_score": score,
        "risk_level": level,
        "detected_regulations": detected_regs,
        "missing_requirements": missing,
        "ai_explanation": explanation,
        "recommended_actions": actions
    }