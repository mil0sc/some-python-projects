# convert-csv-to-excel.py
# Converts a CSV file into an Excel workbook with a single sheet containing the CSV data.

import csv
from openpyxl import Workbook


def csv_to_excel(csv_file_path, excel_file_path):
    """
    Reads data from a CSV file and writes it to a new Excel workbook.

    Args:
    csv_file_path (str): The path to the source CSV file.
    excel_file_path (str): The path where the output Excel file will be saved.
    """
    # Initialize a new Excel workbook and select the default sheet.
    wb = Workbook()
    ws = wb.active

    # Open and read the CSV file, appending each row to the Excel sheet.
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            ws.append(row)  # Add the CSV row to the Excel sheet.

    # Save the populated workbook to the specified Excel file path.
    wb.save(excel_file_path)


# Example usage of the function.
csv_to_excel('example.csv', 'output.xlsx')
