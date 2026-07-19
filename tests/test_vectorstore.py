from rag.embeddings import get_embedding_model
from rag.vectorstore import load_vector_store

embedding_model = get_embedding_model()

vector_store = load_vector_store(
    embedding_model,
)

print()

print(vector_store)