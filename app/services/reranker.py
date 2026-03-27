from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def rerank_chunks(query_embedding, chunk_embeddings, chunks, top_k=3, threshold=0.5):
    """
    Re-rank FAISS retrieved chunks using cosine similarity
    """

    similarities = cosine_similarity(
        [query_embedding],
        chunk_embeddings
    )[0]

    scored_chunks = []

    for i, score in enumerate(similarities):
        scored_chunks.append((chunks[i], score))

    # Sort by score (descending)
    scored_chunks.sort(key=lambda x: x[1], reverse=True)

    # Filter weak chunks
    filtered = [chunk for chunk, score in scored_chunks if score >= threshold]

    # Fallback if everything filtered out
    if not filtered:
        filtered = [chunk for chunk, _ in scored_chunks[:top_k]]

    return filtered[:top_k]