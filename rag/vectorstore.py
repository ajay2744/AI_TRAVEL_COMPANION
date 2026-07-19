from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB_DIR = Path(__file__).parent / "vector_db"


def build_vector_store(
    chunks: list[Document],
    embedding_model: HuggingFaceEmbeddings,
) -> FAISS:
    """
    Build a FAISS vector store from document chunks.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model,
    )

    return vector_store


def save_vector_store(
    vector_store: FAISS,
):
    """
    Save FAISS index to disk.
    """

    VECTOR_DB_DIR.mkdir(
        exist_ok=True,
        parents=True,
    )

    vector_store.save_local(
        str(VECTOR_DB_DIR),
    )


def load_vector_store(
    embedding_model: HuggingFaceEmbeddings,
) -> FAISS:
    """
    Load FAISS index from disk.
    """

    return FAISS.load_local(
        folder_path=str(VECTOR_DB_DIR),
        embeddings=embedding_model,
        allow_dangerous_deserialization=True,
    )