from langchain_core.documents import Document

from rag.embeddings import get_embedding_model
from rag.vectorstore import load_vector_store
from rag.config import SEARCH_TYPE, TOP_K, FETCH_K
from pathlib import Path
from rag.models import RetrievalResult


def retrieve_context(
    query: str,
    k: int = 3,
) -> RetrievalResult:
    """
    Retrieve relevant travel context.
    """

    embedding_model = get_embedding_model()

    vector_store = load_vector_store(
        embedding_model,
    )

    # documents = vector_store.similarity_search(
    #     query=query,
    #     k=k,
    # )
    retriever = vector_store.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={
            "k": TOP_K,
            "fetch_k": FETCH_K,
        },
    )
    documents = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    sources = []

    for doc in documents:

        source = Path(
            doc.metadata["source"]
        ).name

        if source not in sources:
            sources.append(source)

    return RetrievalResult(
        context=context,
        sources=sources,
    )
