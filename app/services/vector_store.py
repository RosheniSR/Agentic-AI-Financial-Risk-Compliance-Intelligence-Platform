import faiss
import numpy as np
from app.services.embedding_service import model


# 🔹 Create FAISS index
def create_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index


# 🔹 Search with regulation-aware structure
def search_index(query_embedding, index, chunks, k=10):
    """
    Returns:
    - chunks with regulation info
    - embeddings for reranking
    """

    D, I = index.search(query_embedding.reshape(1, -1), k)

    results = []
    embeddings = []

    for idx in I[0]:
        chunk = chunks[idx]

        text = chunk["text"]
        reg = chunk["regulation"]

        results.append({
            "text": text,
            "regulation": reg
        })

        # Generate embedding for reranking
        emb = model.encode(text)
        embeddings.append(emb)

    return results, embeddings