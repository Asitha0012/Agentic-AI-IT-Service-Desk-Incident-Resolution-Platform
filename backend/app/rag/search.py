from ollama import embed
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333", timeout=60)
COLLECTION = "aura_kb"

def search_kb(question: str, limit: int = 4):
    q = embed(model="embeddinggemma", input=question).embeddings[0]
    hits = client.query_points(
        collection_name=COLLECTION,
        query=q,
        limit=limit,
        with_payload=True,
    ).points
    
    return [
        {
            "source": h.payload["source"],
            "score": float(h.score),
            "text": h.payload["text"],
        }
        for h in hits
    ]