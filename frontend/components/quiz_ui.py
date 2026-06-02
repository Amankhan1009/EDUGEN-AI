import streamlit as st

from utils.rag_helper import build_retriever

from quiz_generator import generate_quiz


def render_quiz(
    generate_quiz_button,
    quiz_topic,
    learning_level
):

    # ---------------- QUIZ GENERATION ----------------

    if generate_quiz_button:

        if st.session_state.current_file is None:

            st.warning(
                "⚠️ Please upload PDFs first."
            )

        else:

            with st.spinner(
                "🧠 Generating Quiz..."
            ):

                retriever = build_retriever(
                    st.session_state.current_file
                )

                retrieved_docs = retriever.invoke(
                    quiz_topic
                )

                if not quiz_topic.strip():

                    st.warning(
                        "⚠️ Please enter a quiz topic."
                    )

                    st.stop()

                quiz = generate_quiz(
                    retriever,
                    quiz_topic,
                    learning_level
                )

                st.session_state.latest_quiz = quiz

                st.session_state.user_answers = {}

                st.session_state.quizzes.append({
                    "topic": quiz_topic,
                    "content": quiz
                })

                st.success(
                    "✅ Quiz Generated Successfully!"
                )

    # ---------------- INTERACTIVE QUIZ ----------------

    if st.session_state.latest_quiz:

        st.header(
            "📝 Interactive Quiz"
        )

        for idx, q in enumerate(
            st.session_state.latest_quiz
        ):

            st.subheader(
                f"Q{idx + 1}. {q['question']}"
            )

            selected = st.radio(
                "Choose Answer",
                [None] + list(
                    q["options"].keys()
                ),
                format_func=lambda x:
                "Select an answer..."
                if x is None
                else f"{x}. {q['options'][x]}",
                key=f"quiz_{idx}"
            )

            st.session_state.user_answers[idx] = selected

        if st.button(
            "✅ Submit Quiz"
        ):

            unanswered = []

            for idx in range(
                len(
                    st.session_state.latest_quiz
                )
            ):

                if st.session_state.user_answers.get(
                    idx
                ) is None:

                    unanswered.append(
                        idx + 1
                    )

            if unanswered:

                st.warning(
                    f"Please answer all questions. Missing: {unanswered}"
                )

                st.stop()

            score = 0

            total = len(
                st.session_state.latest_quiz
            )

            topic_stats = {}

            for idx, q in enumerate(
                st.session_state.latest_quiz
            ):

                topic = q["topic"]

                if topic not in topic_stats:

                    topic_stats[topic] = {
                        "correct": 0,
                        "wrong": 0
                    }

                if (
                    st.session_state.user_answers.get(
                        idx
                    )
                    == q["answer"]
                ):

                    score += 1

                    topic_stats[topic][
                        "correct"
                    ] += 1

                else:

                    topic_stats[topic][
                        "wrong"
                    ] += 1

            strong_topics = []

            weak_topics = []

            for topic, stats in (
                topic_stats.items()
            ):

                if (
                    stats["correct"]
                    > stats["wrong"]
                ):

                    strong_topics.append(
                        topic
                    )

                else:

                    weak_topics.append(
                        topic
                    )

            performance = round(
                (score / total) * 100,
                2
            )

            st.session_state.performance_history.append({
                "topic":
                st.session_state.quizzes[-1]["topic"],
                "score":
                performance
            })

            st.success(
                f"🎯 Score: {score}/{total}"
            )

            st.info(
                f"📊 Performance: {performance}%"
            )

            st.subheader(
                "✅ Strong Areas"
            )

            for topic in strong_topics:

                st.write(
                    f"✅ {topic}"
                )

            st.subheader(
                "❌ Weak Areas"
            )

            for topic in weak_topics:

                st.write(
                    f"❌ {topic}"
                )

            st.subheader(
                "📚 Recommendations"
            )

            if performance >= 80:

                st.success(
                    "🌟 Excellent work! Keep it up!"
                )

            elif performance >= 60:

                st.info(
                    "👍 Good progress. Review a few concepts and try again."
                )

            else:

                st.warning(
                    "📚 More practice recommended."
                )

            for topic in weak_topics:

                st.write(
                    f"📖 Revise {topic}"
                )

            for idx, q in enumerate(
                st.session_state.latest_quiz
            ):

                with st.expander(
                    f"Review Question {idx + 1}"
                ):

                    st.write(
                        f"Correct Answer: {q['answer']}"
                    )

                    st.write(
                        q["explanation"]
                    )