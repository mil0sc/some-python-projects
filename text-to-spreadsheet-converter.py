# text-to-spreadsheet-converter.py Reads the content from a list of text files and writes each file's content into a
# separate column of an Excel spreadsheet. This allows for easy comparison and analysis of multiple text files within
# a single workbook.

from openpyxl import Workbook


def text_files_to_spreadsheet(text_files, spreadsheet_name='text_contents.xlsx'):
    """
    Creates an Excel spreadsheet with each text file's content in its own column.

    Args:
    text_files (list of str): A list of text file paths to be converted.
    spreadsheet_name (str, optional): The name of the resulting Excel file. Defaults to 'text_contents.xlsx'.
    """
    # Initialize a new workbook and select the active worksheet.
    wb = Workbook()
    ws = wb.active

    # Iterate over the list of text files.
    for column, text_file in enumerate(text_files, start=1):
        # Open each text file for reading.
        with open(text_file, 'r') as file:
            # Read all lines from the file.
            lines = file.readlines()

            # Write each line from the text file into the spreadsheet, one line per row.
            for row, line in enumerate(lines, start=1):
                # Remove trailing newline characters before writing to the cell.
                ws.cell(row=row, column=column).value = line.strip()

    # Save the populated workbook to the specified file.
    wb.save(spreadsheet_name)
    print(f"Spreadsheet '{spreadsheet_name}' is created with the content of text files.")


# Example usage:
# Define a list of text files to be converted into an Excel spreadsheet.
text_files = ['file1.txt', 'file2.txt', 'file3.txt']
# Call the function to create the spreadsheet with the content of the specified text files.
text_files_to_spreadsheet(text_files)
