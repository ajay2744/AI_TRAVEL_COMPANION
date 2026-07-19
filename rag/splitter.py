from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)
from langchain_core.documents import Document
from .config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(
    documents: list[Document],
) -> list[Document]:
    """
    Split loaded documents into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents(documents)

    return chunks