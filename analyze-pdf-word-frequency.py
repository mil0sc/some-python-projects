# analyze-pdf-word-frequency.py
# Analyzes a PDF file to determine the top N most frequently occurring words.

import PyPDF2
from collections import Counter
import re


def get_top_n_words(pdf_path, n=10):
    """
    Identifies the top N most frequently occurring words in a PDF.

    Args:
    pdf_path (str): Path to the PDF file.
    n (int): Number of top occurring words to retrieve.
    """
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    words_count = Counter()

    for page_num in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page_num).extractText()
        words = re.findall(r'\b\w+\b', text.lower())
        words_count.update(words)

    return words_count.most_common(n)


# Example usage
pdf_path = 'meetingminutes.pdf'  # Path to the PDF
top_words = get_top_n_words(pdf_path, 10)  # Get top 10 words

for word, freq in top_words:
    print(f"'{word}': {freq}")
