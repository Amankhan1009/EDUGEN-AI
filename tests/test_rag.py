# from embeddings import get_embedding_model
# from retriever import get_retriever
# from rag_chain import create_rag_chain

# # Load embedding model
# embedding_model = get_embedding_model()

# # Load retriever
# retriever = get_retriever(embedding_model)

# # Create RAG chain
# qa_chain = create_rag_chain(retriever)

# # Ask question
# query = "Explain machine learning in simple words."

# response = qa_chain.invoke(query)

# print("\nAnswer:\n")
# print(response["result"])

from embeddings import get_embedding_model
from retriever import get_retriever
from rag_chain import create_rag_chain

# Load embeddings
embedding_model = get_embedding_model()

# Load retriever
retriever = get_retriever(embedding_model)

# TEST RETRIEVAL FIRST
query = "What is machine learning?"

docs = retriever.invoke(query)

print("\n========== RETRIEVED CHUNKS ==========\n")

for i, doc in enumerate(docs):
    print(f"\n--- Chunk {i+1} ---\n")
    print(doc.page_content[:1000])

# Create RAG chain
qa_chain = create_rag_chain(retriever)

# Generate final answer
response = qa_chain.invoke(query)

print("\n========== FINAL ANSWER ==========\n")

print(response["result"])