from rag.loader import load_documents
from rag.splitter import split_documents


documents = load_documents()

chunks = split_documents(documents)

print(f"\nLoaded Documents : {len(documents)}")

print(f"Generated Chunks : {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):

    print("=" * 80)

    print(f"Chunk {i}")

    print("-" * 80)

    print("Source:")

    print(chunk.metadata["source"])

    print()

    print("Length:")

    print(len(chunk.page_content))

    print()

    print(chunk.page_content)