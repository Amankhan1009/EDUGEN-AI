from langchain_community.document_loaders import PyPDFLoader

# ---------------- LOAD MULTIPLE PDFs ----------------

def load_pdf(pdf_paths):

    all_docs = []

    for pdf_path in pdf_paths:

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        # Add source filename metadata
        for doc in docs:

            doc.metadata["source_file"] = pdf_path.split("/")[-1]

        all_docs.extend(docs)

    return all_docs
