# brute-force-pdf-password.py
# Attempts to decrypt an encrypted PDF by brute-forcing through passwords listed in a dictionary file.
# It tries each password in both lowercase and uppercase forms.

import PyPDF2


def brute_force_pdf_password(pdf_path, dictionary_path):
    """
    Tries to decrypt an encrypted PDF using a list of potential passwords from a dictionary file.

    Args:
    pdf_path (str): Path to the encrypted PDF file.
    dictionary_path (str): Path to the dictionary file containing potential passwords.

    Returns:
    str: The successful password if found, otherwise None.
    """
    # Open the encrypted PDF file.
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Check if the PDF is encrypted; if not, exit the function.
    if not pdf_reader.isEncrypted:
        print("PDF file is not encrypted.")
        pdf_file.close()
        return

    # Iterate through each word in the dictionary file.
    with open(dictionary_path, 'r') as file:
        for word in file:
            word = word.strip()  # Clean the word of newline characters.
            # Try decrypting the PDF with both lowercase and uppercase variants of the word.
            for password in [word.lower(), word.upper()]:
                if pdf_reader.decrypt(password):
                    pdf_file.close()  # Close the PDF file after successful decryption.
                    return password  # Return the successful password.

    pdf_file.close()  # Ensure the PDF file is closed if no password is found.
    return None  # Indicate failure to find a successful password.


# Example usage
pdf_path = 'encrypted_empty.pdf'  # Path to the encrypted PDF.
dictionary_path = 'dictionary.txt'  # Path to the dictionary of potential passwords.
password = brute_force_pdf_password(pdf_path, dictionary_path)

# Print the result of the brute force attempt.
if password:
    print(f"Hacked password: {password}")
else:
    print("Failed to hack the password.")
