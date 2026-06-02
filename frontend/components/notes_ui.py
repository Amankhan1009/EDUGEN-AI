import streamlit as st

from utils.rag_helper import build_retriever

from notes_generator import generate_notes
from pdf_export import create_notes_pdf


def render_notes(
    generate_notes_button,
    notes_topic,
    learning_level
):

    if generate_notes_button:

        if st.session_state.current_file is None:

            st.warning(
                "⚠️ Please upload PDFs first."
            )

        else:

            with st.spinner(
                "📝 Generating Notes..."
            ):

                retriever = build_retriever(
                    st.session_state.current_file
                )

                notes = generate_notes(
                    retriever,
                    notes_topic,
                    learning_level
                )

                st.session_state.generated_notes = notes

                st.success(
                    "✅ Notes Generated Successfully!"
                )

    if st.session_state.generated_notes:

        st.divider()

        st.header(
            "📝 AI Generated Notes"
        )

        st.markdown(
            st.session_state.generated_notes
        )

        pdf_file = create_notes_pdf(
            st.session_state.generated_notes
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Notes PDF",
                data=file,
                file_name="EduGen_Notes.pdf",
                mime="application/pdf"
            )