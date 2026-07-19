from pathlib import Path

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)
from langchain_core.documents import Document


DATA_DIR = Path(__file__).parent / "data"


def load_documents() -> list[Document]:
    """
    Load all markdown documents from the knowledge base.
    """

    loader = DirectoryLoader(
        path=str(DATA_DIR),
        glob="*.md",
        loader_cls=TextLoader,
    )

    documents = loader.load()

    return documents