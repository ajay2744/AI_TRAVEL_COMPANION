from rag.embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "Tell me about Mysore Palace"
)

print()

print("Embedding Dimension :", len(vector))

print()

print(vector[:10])