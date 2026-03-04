import ollama
from vector_store import search
from config import EMBEDDING_MODEL

def embed_query(query):
    response = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=query
    )
    return response["embedding"]

def retrieve(query):
    query_vector = embed_query(query)
    hits = search(query_vector)

    return [hit.payload["text"] for hit in hits]
