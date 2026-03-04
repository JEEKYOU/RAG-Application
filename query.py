import ollama
from qdrant_client import QdrantClient

COLLECTION = "wiki"

client = QdrantClient("localhost", port=6333)

def embed(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]

def retrieve(query):
    query_vector = embed(query)

    hits = client.search(
        collection_name=COLLECTION,
        query_vector=query_vector,
        limit=5
    )

    return [hit.payload["text"] for hit in hits]

def answer(query):
    context = "\n\n".join(retrieve(query))

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "Answer strictly using provided context."},
            {"role": "user", "content": f"""
Context:
{context}

Question:
{query}
"""}
        ]
    )

    return response["message"]["content"]

if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        print(answer(q))
