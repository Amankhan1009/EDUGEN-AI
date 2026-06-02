from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en"
    )

    return embedding_model