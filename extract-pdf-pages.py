# extract-pdf-pages.py
# This script extracts specified pages from a PDF document and saves those pages into a new PDF file.
# It verifies the existence of the specified pages and handles page indexing properly, ensuring the output PDF
# contains exactly the desired pages.

import PyPDF2
import os


def extract_pages(pdf_path, page_numbers, output_filename):
    """
    Extracts specific pages from a PDF file and creates a new PDF file with those pages.

    Args:
    pdf_path (str): The path to the original PDF file.
    page_numbers (list of int): A list of page numbers to extract.
    output_filename (str): The name of the output PDF file.
    """
    # Append '.pdf' to output_filename if it's not already present.
    if not output_filename.endswith('.pdf'):
        output_filename += '.pdf'

    # Initialize a PdfFileReader object for reading from the original PDF.
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    # Initialize a PdfFileWriter object for writing extracted pages to a new PDF.
    pdf_writer = PyPDF2.PdfFileWriter()

    # Iterate over the list of page numbers to extract.
    for page_num in page_numbers:
        # Validate page numbers against the document's range.
        if page_num < 1 or page_num > pdf_reader.numPages:
            print(f"Page {page_num} is out of range. Skipping.")
            continue  # Skip invalid page numbers.

        # Adjust for PyPDF2's zero-based indexing and extract the page.
        page_obj = pdf_reader.getPage(page_num - 1)
        pdf_writer.addPage(page_obj)

    # Write the extracted pages to the specified output file.
    with open(output_filename, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

    # Confirmation message.
    print(f"Extracted pages {page_numbers} from '{pdf_path}' into '{output_filename}'.")


# Define the path to your source PDF, the pages to extract, and the desired name of the output PDF.
pdf_path = 'meetingminutes.pdf'  # Example PDF file path.
page_numbers = [1, 19]  # Example page numbers to extract.
output_filename = 'extracted_pages.pdf'  # Name for the output PDF.

# Call the function with the specified arguments.
extract_pages(pdf_path, page_numbers, output_filename)
