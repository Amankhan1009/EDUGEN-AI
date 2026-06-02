from pdf_loader import load_pdf

docs = load_pdf("data/sample.pdf")

print(docs[0].page_content)