
from langchain_community.vectorstores import Chroma
import os

def get_retriever(embedding_model):

    # Correct vectorstore path
    persist_directory = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "vectorstore"
        )
    )

    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 10,
            "fetch_k": 20
        }
    )

    return retriever
