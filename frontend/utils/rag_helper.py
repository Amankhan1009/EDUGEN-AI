from pdf_loader import load_pdf
from text_splitter import split_documents
from embeddings import get_embedding_model
from vector_store import create_vector_store
from retriever import get_retriever


def build_retriever(pdf_paths):

    docs = load_pdf(
        pdf_paths
    )

    chunks = split_documents(
        docs
    )

    embedding_model = get_embedding_model()

    create_vector_store(
        chunks,
        embedding_model
    )

    return get_retriever(
        embedding_model
    )