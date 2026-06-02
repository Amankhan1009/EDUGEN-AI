import streamlit as st

from utils.rag_helper import build_retriever
from interview_report_pdf import (
    create_interview_report_pdf
)

from interview_generator import (
    generate_interview_questions
)

from interview_evaluator import (
    evaluate_interview
)


def render_interview(
    generate_interview_button,
    interview_topic,
    learning_level
):

    # ---------------- GENERATE QUESTIONS ----------------

    if generate_interview_button:

        if st.session_state.current_file is None:

            st.warning(
                "⚠️ Please upload PDFs first."
            )

        elif not interview_topic.strip():

            st.warning(
                "⚠️ Please enter an interview topic."
            )

        else:

            with st.spinner(
                "🎯 Preparing Interview..."
            ):

                retriever = build_retriever(
                    st.session_state.current_file
                )

                questions = generate_interview_questions(
                    retriever,
                    interview_topic,
                    learning_level
                )

                st.session_state.interview_questions = questions

                st.success(
                    "✅ Interview Ready!"
                )

    # ---------------- DISPLAY QUESTIONS ----------------

    if st.session_state.interview_questions:

        st.divider()

        st.header(
            "🎯 Mock Interview"
        )

        for idx, q in enumerate(
            st.session_state.interview_questions,
            start=1
        ):

            st.subheader(
                f"Question {idx}"
            )

            st.write(
                q["question"]
            )

            answer = st.text_area(
                "Your Answer",
                key=f"interview_answer_{idx}"
            )

            st.session_state.interview_answers[idx] = answer

        submit_interview = st.button(
            "✅ Submit Interview"
        )

        if submit_interview:

            result = evaluate_interview(
                st.session_state.interview_questions,
                st.session_state.interview_answers
            )

            st.session_state.interview_result = result

    # ---------------- SHOW RESULT ----------------

    if st.session_state.interview_result:

        st.divider()

        st.header(
            "📊 Interview Evaluation"
        )

        st.write(
            st.session_state.interview_result
        )

        pdf_file = create_interview_report_pdf(
            st.session_state.interview_result
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Interview Report",
                data=file,
                file_name="Interview_Report.pdf",
                mime="application/pdf"
            )