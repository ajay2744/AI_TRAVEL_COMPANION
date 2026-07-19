"""
RAG Configuration
"""

# ======================================
# Embedding Model
# ======================================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# ======================================
# Chunking
# ======================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ======================================
# Retrieval
# ======================================

SEARCH_TYPE = "mmr"

TOP_K = 3

FETCH_K = 10