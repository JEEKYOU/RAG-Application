from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from config import *

def get_client():
    return QdrantClient(QDRANT_HOST, port=QDRANT_PORT)

def create_collection():
    client = get_client()
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        ),
    )
    print("Collection created.")

def upsert_points(points):
    client = get_client()
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def search(query_vector):
    client = get_client()
    return client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=TOP_K
    )
