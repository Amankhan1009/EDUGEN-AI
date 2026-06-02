import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "backend"
        )
    )
)

from resume_interview_generator import (
    generate_resume_questions
)

resume_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "resumes",
        "Resume.pdf"
    )
)

questions = generate_resume_questions(
    resume_path
)

print("\n")
print("=" * 50)
print("RESUME INTERVIEW QUESTIONS")
print("=" * 50)
print("\n")

print(questions)