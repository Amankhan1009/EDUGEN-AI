import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import (
    getSampleStyleSheet
)

def create_notes_pdf(
    notes,
    filename="notes.pdf"
):
    
    export_dir = "exports"

    os.makedirs(
        export_dir,
        exist_ok=True
    )

    filename = os.path.join(
        export_dir,
        filename
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    for line in notes.split("\n"):

        line = line.replace("**", "")
        line = line.replace("###", "")
        line = line.replace("##", "")
        line = line.replace("#", "")

        if line.strip():

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 5)
            )

    doc.build(content)
    return filename



def create_flashcards_pdf(
    flashcards,
    filename="flashcards.pdf"
):
    

    export_dir = "exports"

    os.makedirs(
        export_dir,
        exist_ok=True
    )

    filename = os.path.join(
        export_dir,
        filename
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "EduGen AI Flashcards",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 20)
    )

    for idx, card in enumerate(
        flashcards,
        start=1
    ):

        content.append(
            Paragraph(
                f"<b>Flashcard {idx}</b>",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Question:</b> {card['question']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 5)
        )

        content.append(
            Paragraph(
                f"<b>Answer:</b> {card['answer']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

    doc.build(content)

    return filename