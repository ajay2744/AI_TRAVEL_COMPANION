from pydantic import BaseModel


class RetrievalResult(BaseModel):
    """
    Result returned by the retriever.
    """

    context: str

    sources: list[str]