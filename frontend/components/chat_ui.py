import streamlit as st

from utils.rag_helper import build_retriever

from rag_chain import create_rag_chain


def render_chat(
    learning_level
):

    # ---------------- DISPLAY CHAT HISTORY ----------------

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):
            st.write(
                message["content"]
            )

    # ---------------- CHAT INPUT ----------------

    user_question = st.chat_input(
        "Ask your question..."
    )

    if not user_question:
        return

    # Save user message

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message(
        "user"
    ):
        st.write(
            user_question
        )

    # Check PDF

    if st.session_state.current_file is None:

        with st.chat_message(
            "assistant"
        ):

            st.warning(
                "⚠️ Please upload a PDF first."
            )

        return

    with st.spinner(
        "⚙️ Preparing AI Tutor..."
    ):

        retriever = build_retriever(
            st.session_state.current_file
        )

        chat_history = ""

        for message in st.session_state.messages:

            role = message["role"]

            content = message["content"]

            chat_history += (
                f"{role}: {content}\n"
            )

        qa_chain = create_rag_chain(
            retriever,
            chat_history,
            learning_level
        )

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "🤖 Thinking..."
        ):

            result = qa_chain(
                user_question
            )

            answer = result["answer"]

            sources = result["sources"]

            st.write(
                answer
            )

            if len(sources) > 0:

                st.markdown(
                    "### 📚 Sources"
                )

                for source in sources:

                    st.write(
                        f"- {source}"
                    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })