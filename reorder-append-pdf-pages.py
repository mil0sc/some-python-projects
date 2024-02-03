# reorder-append-pdf-pages.py
# Reorders a subset of pages in a PDF document based on user input, appends the rest in the original order, and saves the result as a new file.

import PyPDF2
import os


def reorder_pages(pdf_path, new_order, output_filename):
    """
    Reorders pages in a PDF file according to a specified new order and appends any remaining pages in their original sequence.

    Args:
    pdf_path (str): Path to the original PDF file.
    new_order (list of int): List specifying the new order for a subset of pages. Page numbers are 1-indexed.
    output_filename (str): Name of the output file with reordered pages.
    """
    # Append '.pdf' to the output filename if it's not already present.
    if not output_filename.endswith('.pdf'):
        output_filename += '.pdf'

    # Initialize PdfFileReader for reading the original PDF and PdfFileWriter for creating the new PDF.
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    pdf_writer = PyPDF2.PdfFileWriter()

    # Validate that all specified page numbers in new_order are within the PDF's page count.
    if not all(1 <= page_num <= pdf_reader.numPages for page_num in new_order):
        raise ValueError("Page numbers in new_order must be within the range of the PDF's page count.")

    # Add pages in the specified new order to the PdfFileWriter object.
    for page_num in new_order:
        page_obj = pdf_reader.getPage(page_num - 1)  # Adjust for zero-based indexing.
        pdf_writer.addPage(page_obj)

    # Determine and append the remaining pages in their original order.
    remaining_pages = set(range(1, pdf_reader.numPages + 1)) - set(new_order)
    for page_num in sorted(remaining_pages):
        page_obj = pdf_reader.getPage(page_num - 1)
        pdf_writer.addPage(page_obj)

    # Save the new PDF with reordered pages to the specified output file.
    with open(output_filename, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

    # Confirmation message.
    print(f"Reordered pages and saved to {output_filename}")


# Example function call with a PDF file path, specified new order for the initial pages, and an output file name.
pdf_path = 'meetingminutes.pdf'  # Example PDF file path.
new_order = [2, 1, 3, 4]  # Example new order for the beginning pages.
output_filename = 'reordered.pdf'  # Desired name for the output file.

reorder_pages(pdf_path, new_order, output_filename)
