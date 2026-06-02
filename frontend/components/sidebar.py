import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.header("📄 Upload Study Material")

        uploaded_files = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
            accept_multiple_files=True
        )

        st.divider()

        learning_level = st.selectbox(
            "🎯 Select Learning Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        st.divider()

        st.markdown("""
        ### 🚀 Features
        - Hybrid RAG + General AI
        - Conversational Memory
        - Personalized Tutor Modes
        - Source Citations
        - Semantic Search
        - Groq LLM Integration
        """)

        st.divider()

        st.subheader("📝 Quiz Generator")

        quiz_topic = st.text_input(
            "Enter Quiz Topic"
        )

        generate_quiz_button = st.button(
            "Generate Quiz"
        )

        st.divider()

        st.subheader("📝 Notes Generator")

        notes_topic = st.text_input(
            "Enter Notes Topic"
        )

        generate_notes_button = st.button(
            "Generate Notes"
        )

        st.divider()

        st.subheader("🃏 Flashcard Generator")

        flashcard_topic = st.text_input(
            "Enter Flashcard Topic"
        )

        generate_flashcards_button = st.button(
            "Generate Flashcards"
        )

        st.divider()

        st.subheader("🎯 Mock Interview")

        interview_topic = st.text_input(
            "Interview Topic"
        )

        generate_interview_button = st.button(
            "Start Interview"
        )

        # ==========================================
        # 💼 Resume Interview Prep
        # ==========================================

        st.divider()

        st.subheader(
            "💼 Resume Interview Prep"
        )

        uploaded_resume = st.file_uploader(
            "Upload Resume",
            type=["pdf"],
            key="resume_upload"
        )

        generate_resume_interview_button = st.button(
            "Generate Resume Questions"
        )

        return {
            "uploaded_files": uploaded_files,
            "learning_level": learning_level,
            "quiz_topic": quiz_topic,
            "generate_quiz_button": generate_quiz_button,
            "notes_topic": notes_topic,
            "generate_notes_button": generate_notes_button,
            "flashcard_topic": flashcard_topic,
            "generate_flashcards_button": generate_flashcards_button,
            "interview_topic": interview_topic,
            "generate_interview_button": generate_interview_button,

            "uploaded_resume": uploaded_resume,
            "generate_resume_interview_button":
                generate_resume_interview_button
        }


