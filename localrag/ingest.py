import uuid
import ollama
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from chunker import chunk_markdown

COLLECTION = "wiki"

client = QdrantClient("localhost", port=6333)

def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        ),
    )

def embed(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]

def ingest():
    with open("wiki.md", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_markdown(text)
    points = []

    for chunk in chunks:
        vector = embed(chunk)
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text": chunk}
            )
        )

    client.upsert(collection_name=COLLECTION, points=points)

if __name__ == "__main__":
    create_collection()
    ingest()
    print("Ingestion complete.")
