from rag.retriever import retrieve_context


query = "Tell me about Ajay Heritage Fort."

context = retrieve_context(
    query=query,
    k=3,
)

print(context)