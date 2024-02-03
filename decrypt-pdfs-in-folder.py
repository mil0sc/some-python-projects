# decrypt-pdfs-in-folder.py
# Searches through a specified folder for PDF files encrypted with a specific naming pattern ('_encrypted.pdf'),
# attempts to decrypt them using a given password, and saves the decrypted version with a '_decrypted' suffix in the filename.

import os
import PyPDF2


def decrypt_pdfs(folder, password):
    """
    Decrypts PDF files in the specified folder using the provided password.

    Args:
    folder (str): The directory to search for encrypted PDF files.
    password (str): The password to use for decrypting the PDF files.
    """
    # Walk through the directory, accessing all subfolders and files.
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Target files with a specific naming convention indicating encryption.
            if filename.endswith('_encrypted.pdf'):
                file_path = os.path.join(foldername, filename)  # Construct the full file path.
                with open(file_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfFileReader(file)
                    # Check if the file is encrypted and attempt to decrypt it.
                    if pdf_reader.isEncrypted and pdf_reader.decrypt(password):
                        pdf_writer = PyPDF2.PdfFileWriter()
                        # Copy each page of the original PDF into the writer object.
                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        # Define the filename for the decrypted PDF.
                        decrypted_path = file_path[:-14] + '_decrypted.pdf'
                        # Write the decrypted content to a new PDF file.
                        with open(decrypted_path, 'wb') as decrypted_file:
                            pdf_writer.write(decrypted_file)
                        print(f'Decrypted {file_path}')
                    else:
                        # Notify the user if decryption was unsuccessful.
                        print(f'Incorrect password for {file_path}')


# Example function call to decrypt PDFs within a specified directory.
# Replace '/path/to/folder' with the actual folder path and 'your_password' with the decryption password.
decrypt_pdfs('/path/to/folder', 'your_password')
