import streamlit as st
import re

from resume_interview_generator import (
    generate_resume_questions
)
from interview_evaluator import (
    evaluate_interview
)

from interview_report_pdf import (
    create_interview_report_pdf
)


def render_resume_interview(
    generate_resume_interview_button
):

    if generate_resume_interview_button:

        if st.session_state.resume_file is None:

            st.warning(
                "⚠️ Please upload a resume first."
            )

        else:

            with st.spinner(
                "🎓 Generating Resume Questions..."
            ):
                st.session_state.resume_answers = {}
                st.session_state.resume_result = None
                questions = (
                    generate_resume_questions(
                        st.session_state.resume_file,
                        st.session_state.resume_interview_round
                    )
                )

                st.session_state.resume_questions = (
                    questions
                )
                st.session_state.resume_interview_round += 1

                st.success(
                    "✅ Resume Questions Generated!"
                )

    if st.session_state.resume_questions:

        st.header(
            "💼 Resume Interview Questions"
        )

        st.caption(
            f"Interview Round {st.session_state.resume_interview_round - 1}"
        )

        questions = (
            st.session_state.resume_questions
            .split("\n")
        )

        clean_questions = []

        import re

        for q in questions:

            q = q.strip()

            # Remove:
            # 1.
            # 2.
            # 3)
            # etc.

            q = re.sub(
                r'^\d+[\.\)]\s*',
                '',
                q
            )

            if q:

                clean_questions.append(q)

        for idx, q in enumerate(
            clean_questions,
            start=1
        ):

            st.subheader(
                f"Question {idx}"
            )

            st.write(q)

            answer = st.text_area(
                "Your Answer",
                key=f"resume_answer_{st.session_state.resume_interview_round}_{idx}"
            )

            st.session_state.resume_answers[
                idx
            ] = answer
        
    submit_resume_interview = st.button(
        "✅ Submit Resume Interview"
    )

    if submit_resume_interview:

        formatted_questions = []

        for q in clean_questions:

            formatted_questions.append(
                {
                    "question": q
                }
            )

        result = evaluate_interview(
            formatted_questions,
            st.session_state.resume_answers
        )

        st.session_state.resume_result = (
            result
        )
        

        score_match = re.search(
            r'(\d+(?:\.\d+)?)\s*/\s*10',
            result
        )

        if score_match:

            score = float(
                score_match.group(1)
            )

            st.session_state.resume_history.append(
                {
                    "round":
                    st.session_state.resume_interview_round - 1,
                    "score":
                    score
                }
            )

    if st.session_state.resume_result:

        st.divider()

        st.header(
            "📊 Resume Interview Evaluation"
        )

        st.write(
            st.session_state.resume_result
        )

        pdf_file = create_interview_report_pdf(
            st.session_state.resume_result,
            filename=
            "resume_interview_report.pdf"
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label=
                "📄 Download Resume Interview Report",
                data=file,
                file_name=
                "Resume_Interview_Report.pdf",
                mime=
                "application/pdf"
            )