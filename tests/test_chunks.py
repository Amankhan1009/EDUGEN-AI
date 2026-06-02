from pdf_loader import load_pdf
from text_splitter import split_documents

docs = load_pdf("data/sample.pdf")

chunks = split_documents(docs)

print(chunks[0].page_content)
print(f"\nTotal Chunks: {len(chunks)}")