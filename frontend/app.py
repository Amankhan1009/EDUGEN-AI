import streamlit as st
import sys
import os

# ---------------- ADD BACKEND PATH ----------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "backend"
        )
    )
)

# ---------------- COMPONENTS ----------------

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.notes_ui import render_notes
from components.flashcards_ui import render_flashcards
from components.interview_ui import render_interview
from components.quiz_ui import render_quiz
from components.chat_ui import render_chat
from components.resume_interview_ui import render_resume_interview

# ---------------- PAGE CONFIG ----------------
# ---------------- TITLE ----------------

st.markdown(
    """
    <div style="text-align:center; margin-bottom:20px;">
        <h1>📚 EduGen AI</h1>
        <p style="font-size:22px;color:gray;">
            Personalized AI Tutor using Advanced RAG
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------
if "latest_quiz" not in st.session_state:
    st.session_state.latest_quiz = None

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

if "quizzes" not in st.session_state:
    st.session_state.quizzes = []

if "performance_history" not in st.session_state:
    st.session_state.performance_history = []

if "current_file" not in st.session_state:
    st.session_state.current_file = None

if "generated_notes" not in st.session_state:
    st.session_state.generated_notes = None

if "flashcards" not in st.session_state:
    st.session_state.flashcards = None

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = None

if "interview_answers" not in st.session_state:
    st.session_state.interview_answers = {}

if "interview_result" not in st.session_state:
    st.session_state.interview_result = None

# ---------------- RESUME SESSION STATE ----------------
if "resume_file" not in st.session_state:
    st.session_state.resume_file = None

if "resume_questions" not in st.session_state:
    st.session_state.resume_questions = None

if "resume_interview_round" not in st.session_state:
    st.session_state.resume_interview_round = 1


if "resume_answers" not in st.session_state:
    st.session_state.resume_answers = {}

if "resume_result" not in st.session_state:
    st.session_state.resume_result = None

if "resume_history" not in st.session_state:
    st.session_state.resume_history = []

# ---------------- SIDEBAR ----------------

sidebar_data = render_sidebar()

uploaded_files = sidebar_data["uploaded_files"]

learning_level = sidebar_data["learning_level"]

quiz_topic = sidebar_data["quiz_topic"]

generate_quiz_button = sidebar_data["generate_quiz_button"]

notes_topic = sidebar_data["notes_topic"]

generate_notes_button = sidebar_data["generate_notes_button"]

flashcard_topic = sidebar_data["flashcard_topic"]

generate_flashcards_button = sidebar_data["generate_flashcards_button"]

interview_topic = sidebar_data["interview_topic"]

generate_interview_button = sidebar_data["generate_interview_button"]

# ---------------- RESUME INTERVIEW ----------------

uploaded_resume = sidebar_data[
    "uploaded_resume"
]

generate_resume_interview_button = sidebar_data[
    "generate_resume_interview_button"
]


# ---------------- CREATE UPLOAD DIRECTORY ----------------

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)
# ---------------- RESUME DIRECTORY ----------------

RESUME_DIR = "resumes"

os.makedirs(
    RESUME_DIR,
    exist_ok=True
)

# ---------------- HANDLE PDF UPLOAD ----------------

if uploaded_files:

    uploaded_paths = []

    for uploaded_file in uploaded_files:

        upload_path = os.path.join(
            UPLOAD_DIR,
            uploaded_file.name
        )

        # Save uploaded PDF
        with open(upload_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        uploaded_paths.append(upload_path)

    st.sidebar.success(
        f"✅ {len(uploaded_paths)} PDFs uploaded successfully!"
    )

    # Save uploaded file paths
    st.session_state.current_file = uploaded_paths

# =====================================================
# HANDLE RESUME UPLOAD
# =====================================================
if uploaded_resume:

    resume_path = os.path.join(
        RESUME_DIR,
        uploaded_resume.name
    )

    with open(
        resume_path,
        "wb"
    ) as f:

        f.write(
            uploaded_resume.getbuffer()
        )

    st.session_state.resume_file = (
        resume_path
    )

    st.sidebar.success(
        "✅ Resume Uploaded Successfully!"
    )
# =====================================================
# CUSTOM TAB STYLING
# =====================================================

st.markdown("""
<style>

/* Center Tabs */
div[data-baseweb="tab-list"] {
    justify-content: center;
}

/* Tab Styling */
button[data-baseweb="tab"] {
    font-size: 18px;
    font-weight: 600;
    padding: 10px 18px;
}

/* Selected Tab */
button[data-baseweb="tab"][aria-selected="true"] {
    border-bottom: 3px solid #FF4B4B;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# 📈 PERFORMANCE DASHBOARD
# =====================================================

render_dashboard()


# =====================================================
# 📑 MAIN APPLICATION TABS
# =====================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "💬 Chat",
        "📝 Quiz",
        "📚 Notes",
        "🃏 Flashcards",
        "🎯 Interview",
        "💼 Resume Interview"
    ]
)


# =====================================================
# 💬 CHAT TAB
# =====================================================

with tab1:

    render_chat(
        learning_level
    )


# =====================================================
# 📝 QUIZ TAB
# =====================================================

with tab2:

    render_quiz(
        generate_quiz_button,
        quiz_topic,
        learning_level
    )


# =====================================================
# 📚 NOTES TAB
# =====================================================

with tab3:

    render_notes(
        generate_notes_button,
        notes_topic,
        learning_level
    )


# =====================================================
# 🃏 FLASHCARDS TAB
# =====================================================

with tab4:

    render_flashcards(
        generate_flashcards_button,
        flashcard_topic,
        learning_level
    )


# =====================================================
# 🎯 MOCK INTERVIEW TAB
# =====================================================

with tab5:

    render_interview(
        generate_interview_button,
        interview_topic,
        learning_level
    )

# =====================================================
# 💼 RESUME INTERVIEW TAB
# =====================================================

with tab6:

    render_resume_interview(
        generate_resume_interview_button
    )