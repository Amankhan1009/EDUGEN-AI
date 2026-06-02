from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import json

load_dotenv()

def generate_flashcards(
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
You are an AI Flashcard Generator.

Generate exactly 10 flashcards.

Return ONLY valid JSON.

Format:

[
 {{
   "question": "Question",
   "answer": "Answer"
 }}
]

Student Level:
{learning_level}

Topic:
{topic}

Context:
{context}
"""

    response = llm.invoke(prompt)

    flashcards = response.content

    flashcards = flashcards.replace(
        "```json",
        ""
    )

    flashcards = flashcards.replace(
        "```",
        ""
    )

    return json.loads(flashcards)