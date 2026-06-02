from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


def create_interview_report_pdf(
    report,
    filename="interview_report.pdf"
):

    export_dir = "exports"

    os.makedirs(
        export_dir,
        exist_ok=True
    )

    filepath = os.path.join(
        export_dir,
        filename
    )

    doc = SimpleDocTemplate(
        filepath
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "EduGen AI Interview Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    for line in report.split("\n"):

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

    return filepath