from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import json

load_dotenv()


def generate_interview_questions(
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
You are an AI Technical Interviewer.

Generate exactly 5 interview questions.

Return ONLY valid JSON.

Format:

[
    {{
        "question": "Question text"
    }}
]

Learning Level:
{learning_level}

Topic:
{topic}

Context:
{context}
"""

    response = llm.invoke(prompt)

    text = response.content

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)