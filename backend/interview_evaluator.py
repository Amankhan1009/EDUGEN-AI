from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def evaluate_interview(
    questions,
    answers
):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    interview_text = ""

    for idx, q in enumerate(
        questions,
        start=1
    ):

        interview_text += f"""
Question:
{q['question']}

Answer:
{answers.get(idx, '')}

"""

    prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate.

Provide EXACTLY in this format:

Score: X/10

Strengths:
- point 1
- point 2

Weaknesses:
- point 1
- point 2

Recommendations:
- point 1
- point 2

Interview:

{interview_text}
"""

    response = llm.invoke(prompt)

    return response.content