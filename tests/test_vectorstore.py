from pdf_loader import load_pdf
from text_splitter import split_documents
from embeddings import get_embedding_model
from vector_store import create_vector_store

# Load PDF
docs = load_pdf("data/sample.pdf")

# Split into chunks
chunks = split_documents(docs)

# Load embedding model
embedding_model = get_embedding_model()

# Create vector DB
vectorstore = create_vector_store(chunks, embedding_model)

print("Vector database created successfully!")