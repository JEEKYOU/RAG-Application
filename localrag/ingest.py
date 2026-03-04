import uuid
import ollama
from qdrant_client.models import PointStruct
from chunker import chunk_markdown
from vector_store import create_collection, upsert_points
from config import EMBEDDING_MODEL, COLLECTION_NAME

def embed(text):
    response = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=text
    )
    return response["embedding"]

def ingest():
    with open("wiki.md", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_markdown(text)
    print(f"Total chunks: {len(chunks)}")

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

    upsert_points(points)
    print("Ingestion complete.")

if __name__ == "__main__":
    create_collection()
    ingest()
