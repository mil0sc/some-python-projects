# encrypt-pdfs-in-folder.py
# Searches through a specified folder (and its subfolders) for PDF files, encrypts them with a given password,
# and deletes the original unencrypted files. This script ensures that all PDF documents in the folder are securely encrypted.

import os
import PyPDF2


def encrypt_pdfs(folder, password):
    """
    Encrypts all PDF files in a specified folder with a given password.

    Args:
    folder (str): The path to the folder containing PDF files to encrypt.
    password (str): The password to use for encrypting the PDF files.
    """
    # Walk through all folders and files in the specified directory.
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):  # Check if the file is a PDF.
                file_path = os.path.join(foldername, filename)  # Full path to the file
                pdf_reader = PyPDF2.PdfFileReader(open(file_path, 'rb'))
                if not pdf_reader.isEncrypted:  # Proceed if the PDF is not already encrypted.
                    pdf_writer = PyPDF2.PdfFileWriter()
                    # Copy all pages from the reader to the writer.
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))

                    # Encrypt the copy of the PDF with the provided password.
                    pdf_writer.encrypt(password)

                    # Define the path for the encrypted PDF.
                    encrypted_path = file_path[:-4] + '_encrypted.pdf'
                    # Write the encrypted PDF to a new file.
                    with open(encrypted_path, 'wb') as encrypted_file:
                        pdf_writer.write(encrypted_file)

                    # Verify if the new file is encrypted successfully.
                    test_reader = PyPDF2.PdfFileReader(open(encrypted_path, 'rb'))
                    if test_reader.isEncrypted and test_reader.decrypt(password):
                        print(f'Encrypted {file_path}')
                        os.remove(file_path)  # Remove the original unencrypted file after successful encryption.
                    else:
                        print(f'Failed to encrypt {file_path}')


# Example usage of the function to encrypt PDFs in a specified directory with a password.
encrypt_pdfs('/Users/milosz/', '')
