
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import json

load_dotenv()

# ---------------- GENERATE QUIZ ----------------

def generate_quiz(
    retriever,
    topic,
    learning_level
):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    # Retrieve relevant docs
    docs = retriever.invoke(topic)

    # Combine context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Quiz prompt
    prompt = f"""
You are an AI Quiz Generator.

Generate exactly 5 MCQs.

For every question include a topic field.

IMPORTANT:
The topic must be directly related to the question.
Do NOT randomly assign topics.
Examples:

Question about K-Means → topic = "K-Means"
Question about Clustering → topic = "Clustering"
Question about Neural Networks → topic = "Neural Networks"
Question about Machine Learning → topic = "Machine Learning"
Return ONLY valid JSON.

Format:

[
  {{
  "question": "Question text",
  "topic": "Neural Networks",
  "options": {{
    "A": "Option A",
    "B": "Option B",
    "C": "Option C",
    "D": "Option D"
  }},
  "answer": "A",
  "explanation": "Explanation"
}}
]

Student Level:
{learning_level}

IMPORTANT:

Generate questions ONLY about:
{topic}

Do NOT generate questions from other machine learning topics.

If retrieved context contains unrelated concepts,
ignore them completely.

All 5 questions must be directly related to:
{topic}

Context:
{context}

Topic:
{topic}
"""

    response = llm.invoke(prompt)
    quiz_text = response.content
    quiz_text = quiz_text.strip()
    # Remove markdown if model adds it
    quiz_text = quiz_text.replace("```json", "")
    quiz_text = quiz_text.replace("```", "")

    quiz_data = json.loads(quiz_text)

    return quiz_data

    