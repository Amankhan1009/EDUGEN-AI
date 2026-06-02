
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os



load_dotenv()

# ---------------- CREATE HYBRID AI TUTOR ----------------

def create_rag_chain(
    retriever,
    chat_history,
    learning_level
):

    # ---------------- LLM ----------------

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    # ---------------- PERSONALIZED MODES ----------------

    if learning_level == "Beginner":

        tutor_style = """
- Explain concepts in VERY simple language.
- Avoid technical jargon.
- Use analogies and real-life examples.
- Teach step-by-step.
"""

    elif learning_level == "Intermediate":

        tutor_style = """
- Balance simple explanations with technical depth.
- Introduce important terminology gradually.
- Give practical intuition and examples.
"""

    else:

        tutor_style = """
- Give detailed technical explanations.
- Use AI/ML terminology and jargon.
- Explain architecture, mathematics, and implementation details.
"""

    # ---------------- HYBRID QA FUNCTION ----------------

    def hybrid_qa(question):

        # ---------------- RETRIEVE DOCUMENTS ----------------

        docs = retriever.invoke(question)

        # ---------------- COMBINE CONTEXT ----------------

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # ---------------- CHECK RETRIEVED DOCS ----------------

        has_relevant_docs = len(docs) > 0

        # ---------------- RAG MODE ----------------

        if has_relevant_docs:

            prompt = f"""
You are EduGen AI, a personalized AI tutor.

Student Level:
{learning_level}

Tutor Instructions:
{tutor_style}

Previous Conversation:
{chat_history}

IMPORTANT:
- Use the provided document context.
- Explain educationally.
- Keep answers aligned with student level.

Document Context:
{context}

Question:
{question}

Answer:
"""

        # ---------------- GENERAL AI MODE ----------------

        else:

            prompt = f"""
You are EduGen AI, a personalized AI tutor.

Student Level:
{learning_level}

Tutor Instructions:
{tutor_style}

Previous Conversation:
{chat_history}

IMPORTANT:
- No relevant document context was found.
- Use general AI knowledge.
- Explain educationally.

Question:
{question}

Answer:
"""

        # ---------------- GENERATE RESPONSE ----------------

        response = llm.invoke(prompt)

        answer = response.content

        # ---------------- SOURCE CITATIONS ----------------

        sources = []
        

        for doc in docs:

            if "page" in doc.metadata:

                page_number = doc.metadata["page"] + 1

                source_file=doc.metadata.get(
                    "source_file", 
                    "Unknown PDF")
                sources.append(
                    f"{source_file} - Page {page_number}"
                )

        # Remove duplicate pages
        sources = list(set(sources))

        # ---------------- RETURN RESULT ----------------

        return {
            "answer": answer,
            "sources": sources
        }

    # ---------------- RETURN HYBRID FUNCTION ----------------

    return hybrid_qa
