from langchain_groq import ChatGroq
from langchain_community.document_loaders import (
    PyPDFLoader
)

from dotenv import load_dotenv

import os

load_dotenv()


def generate_resume_questions(
    resume_path,
    interview_round
):

    # Load Resume

    loader = PyPDFLoader(
        resume_path
    )

    docs = loader.load()

    resume_text = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    # LLM

    llm = ChatGroq(
        groq_api_key=os.getenv(
            "GROQ_API_KEY"
        ),
        model_name=
        "llama-3.3-70b-versatile"
    )

    # Prompt

    prompt = f"""
You are a professional technical interviewer.

Analyze ONLY the information present in the candidate's resume.

This is Interview Round:
{interview_round}

STRICT RULES:

1. Every question MUST come directly from the resume.

2. DO NOT ask about technologies, frameworks, concepts, domains, tools, or methodologies that are NOT explicitly mentioned in the resume.

3. DO NOT invent projects, experience, internships, certifications, or skills.

4. DO NOT generate System Design questions unless System Design is explicitly written in the resume.

5. DO NOT generate NLP, LLM, Generative AI, Recommendation Systems, Cloud Architecture, Distributed Systems, Computer Vision, or any other topic unless explicitly mentioned.

6. Focus ONLY on:
   - Projects
   - Skills
   - Tools
   - Certifications
   - Education
   - Experience

7. Generate EXACTLY 10 questions.

8. Make every interview round different:

Round 1:
Ask introductory and overview questions.

Round 2:
Ask implementation-focused and technical-depth questions.

Round 3:
Ask troubleshooting and scenario-based questions.

Round 4+:
Ask advanced follow-up questions.

9. Avoid repeating questions from previous rounds.

10. If a project is mentioned, ask about:
    - design decisions
    - challenges
    - implementation
    - improvements
    - deployment

11. Return ONLY the questions.

Resume:

{resume_text}
"""

    response = llm.invoke(
        prompt
    )

    return response.content