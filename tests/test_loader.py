from rag.loader import load_documents


documents = load_documents()

print(f"\nLoaded {len(documents)} documents\n")

for i, doc in enumerate(documents, start=1):

    print("=" * 60)

    print(f"Document {i}")

    print("-" * 60)

    print("Source:")
    print(doc.metadata["source"])

    print()

    print(doc.page_content)