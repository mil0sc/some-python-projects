# extract-pages-with-text.py
# Extracts pages that contain a specific text string from a source PDF and saves them as a new PDF file.

import PyPDF2


def create_pdf_with_text(source_pdf_path, target_pdf_path, search_text):
    """
    Creates a new PDF containing only the pages from the source PDF that include the specified text.

    Args:
    source_pdf_path (str): Path to the source PDF.
    target_pdf_path (str): Path for the newly created PDF.
    search_text (str): Text to search for within the PDF pages.
    """
    pdf_reader = PyPDF2.PdfFileReader(source_pdf_path)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        if search_text in page.extractText():
            pdf_writer.addPage(page)

    with open(target_pdf_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

    print(f"Created '{target_pdf_path}' from pages containing '{search_text}'.")


# Example usage
source_pdf_path = 'source.pdf'  # Path to the original PDF
target_pdf_path = 'specific_text_pages.pdf'  # Output PDF path
search_text = 'Your Specific Text Here'  # Text to search for

create_pdf_with_text(source_pdf_path, target_pdf_path, search_text)
