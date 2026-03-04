config.py# ==============================
# MODEL CONFIGURATION
# ==============================

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "mistral"

# ==============================
# VECTOR DATABASE CONFIG
# ==============================

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "wiki"

# nomic-embed-text outputs 768-d vectors
VECTOR_SIZE = 768
DISTANCE_METRIC = "cosine"

# ==============================
# CHUNKING CONFIG
# ==============================

MAX_CHUNK_TOKENS = 800
CHUNK_OVERLAP = 100
MIN_CHUNK_TOKENS = 200

# ==============================
# RETRIEVAL CONFIG
# ==============================

TOP_K = 5
MIN_SIMILARITY_SCORE = 0.3  # optional future filtering

# ==============================
# PROMPT CONFIGURATION
# ==============================

SYSTEM_PROMPT = """
You are an internal company assistant.

Rules:
- Answer ONLY using the provided context.
- If the answer is not in context, say: 
  "I don't have enough information in the wiki to answer that."
- Be concise and factual.
"""

# ==============================
# FUTURE PRODUCTION FLAGS
# ==============================

ENABLE_RERANKING = False
ENABLE_HYBRID_SEARCH = False
ENABLE_QUERY_LOGGING = True
