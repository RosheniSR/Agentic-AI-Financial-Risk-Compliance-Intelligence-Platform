from app.services.document_loader import load_pdf_text
from app.services.text_chunker import chunk_text
from app.services.embedding_service import create_embeddings
from app.services.vector_store import create_faiss_index

# -------------------------------
# GLOBAL STORAGE
# -------------------------------
chunks = []
embeddings = []


# -------------------------------
# PROCESS FUNCTION
# -------------------------------
def process_document(text, regulation_name):
    text_chunks = chunk_text(text)

    for chunk in text_chunks:
        chunks.append({
            "text": chunk,
            "regulation": regulation_name
        })


# -------------------------------
# LOAD DOCUMENTS
# -------------------------------
gdpr_text = load_pdf_text("data/gdpr.pdf")
dora_text = load_pdf_text("data/dora.pdf")
nis2_text = load_pdf_text("data/nis2.pdf")

# -------------------------------
# PROCESS EACH REGULATION
# -------------------------------
process_document(gdpr_text, "GDPR")
process_document(dora_text, "DORA")
process_document(nis2_text, "NIS2")

# -------------------------------
# CREATE EMBEDDINGS (TEXT ONLY)
# -------------------------------
texts = [chunk["text"] for chunk in chunks]   # ✅ IMPORTANT
embeddings = create_embeddings(texts)

# -------------------------------
# CREATE FAISS INDEX
# -------------------------------
index = create_faiss_index(embeddings)