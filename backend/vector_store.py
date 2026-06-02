from langchain_community.vectorstores import Chroma
import os

def create_vector_store(
    chunks,
    embedding_model
):

    persist_directory = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "vectorstore"
        )
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )

    return vectorstore