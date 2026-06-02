from embeddings import get_embedding_model
from retriever import get_retriever

embedding_model = get_embedding_model()

retriever = get_retriever(embedding_model)

query = "What is machine learning?"

results = retriever.invoke(query)

print(results[0].page_content)