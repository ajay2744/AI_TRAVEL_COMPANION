from langchain_huggingface import HuggingFaceEmbeddings
from rag.config import EMBEDDING_MODEL

def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Return the embedding model used for the travel
    knowledge base.
    """

    return HuggingFaceEmbeddings(

        model_name=EMBEDDING_MODEL,

        model_kwargs={
            "device": "cpu",
        },

        encode_kwargs={
            "normalize_embeddings": True,
        },
    )