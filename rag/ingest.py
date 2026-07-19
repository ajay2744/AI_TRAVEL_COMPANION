from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vectorstore import (
    build_vector_store,
    save_vector_store,
)


def ingest():

    print("Loading documents...")

    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    print()

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Generated {len(chunks)} chunks")

    print()

    print("Loading embedding model...")

    embedding_model = get_embedding_model()

    print()

    print("Creating FAISS index...")

    vector_store = build_vector_store(
        chunks,
        embedding_model,
    )

    save_vector_store(
        vector_store,
    )

    print()

    print("Vector store created successfully.")


if __name__ == "__main__":
    ingest()