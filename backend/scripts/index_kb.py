import hashlib
from pathlib import Path
from ollama import embed
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

PROJECT_ROOT = Path(__file__).resolve().parents[2]
KB = PROJECT_ROOT / "data" / "kb"
COLLECTION = "aura_kb"
client = QdrantClient(url="http://localhost:6333", timeout=60)

def chunks(text, size=700, overlap=100):
    words = text.split()
    out = []
    start = 0
    while start < len(words):
        end = min(len(words), start+size)
        out.append(" ".join(words[start:end]))
        if end == len(words): break
        start = end - overlap
    return out

all_points = []
for path in KB.glob("*.md"):
    text = path.read_text(encoding="utf-8")
    for idx, chunk in enumerate(chunks(text)):
        vec = embed(model="embeddinggemma", input=chunk).embeddings[0]
        pid = int(hashlib.sha1(f"{path.name}:{idx}".encode()).hexdigest()[:12], 16)
        all_points.append(PointStruct(
            id=pid,
            vector=vec,
            payload={"source": path.name, "chunk_id": idx, "text": chunk}
        ))

if not all_points:
    print(f"No markdown documents found in {KB} to index.")
    exit(0)

if not client.collection_exists(COLLECTION):
    dim = len(all_points[0].vector)
    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )
client.upsert(collection_name=COLLECTION, points=all_points)
print(f"indexed {len(all_points)} chunks")