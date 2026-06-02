from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def generate_notes(
    retriever,
    topic,
    learning_level
):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    docs = retriever.invoke(topic)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert AI Teacher.

Student Level:
{learning_level}

Create well-structured study notes.

IMPORTANT:
- Use headings.
- Use bullet points.
- Explain concepts clearly.
- Include examples.
- Include key takeaways.
- Include interview questions.
- Use only relevant information from the context.

IMPORTANT:
- Generate clean study notes.
- Do NOT use markdown symbols.
- Do NOT use #, ##, ###.
- Do NOT use **.
- Use simple headings.
- Use bullet points.

Topic:
{topic}

Context:
{context}

Generate detailed notes.
"""

    response = llm.invoke(prompt)

    return response.content