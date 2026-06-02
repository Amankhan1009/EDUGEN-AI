import streamlit as st

from utils.rag_helper import build_retriever

from flashcard_generator import generate_flashcards
from pdf_export import create_flashcards_pdf


def render_flashcards(
    generate_flashcards_button,
    flashcard_topic,
    learning_level
):

    if generate_flashcards_button:

        if st.session_state.current_file is None:

            st.warning(
                "⚠️ Please upload PDFs first."
            )

        elif not flashcard_topic.strip():

            st.warning(
                "⚠️ Please enter a flashcard topic."
            )

        else:

            with st.spinner(
                "🃏 Generating Flashcards..."
            ):

                retriever = build_retriever(
                    st.session_state.current_file
                )

                flashcards = generate_flashcards(
                    retriever,
                    flashcard_topic,
                    learning_level
                )

                st.session_state.flashcards = flashcards

                st.success(
                    "✅ Flashcards Generated!"
                )

    if st.session_state.flashcards:

        st.header(
            "🃏 Flashcards"
        )

        for i, card in enumerate(
            st.session_state.flashcards,
            start=1
        ):

            with st.expander(
                f"Flashcard {i}"
            ):

                st.write(
                    f"Q: {card['question']}"
                )

                st.success(
                    f"A: {card['answer']}"
                )

        pdf_file = create_flashcards_pdf(
            st.session_state.flashcards
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Flashcards PDF",
                data=file,
                file_name="EduGen_Flashcards.pdf",
                mime="application/pdf"
            )