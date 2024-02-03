# validate-csv-data.py
# Validates data within a CSV file, including checks for empty rows, consistent column counts,
# empty cells, and data types for specific columns.

import csv


def check_csv(file_path):
    """
    Performs data validation checks on a CSV file, reporting any discrepancies found.

    Args:
    file_path (str): The path to the CSV file to be validated.
    """
    # Optional: Define the expected number of columns in the CSV file.
    expected_col_count = 5

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader, start=1):
            # Check if the row is empty and report it.
            if not row:
                print(f"Empty row found at line {i}.")
                continue

            # Verify that each row has the expected number of columns.
            if len(row) != expected_col_count:
                print(f"Row {i} has an inconsistent number of columns: {len(row)} instead of {expected_col_count}.")

            # Check each cell in the row for empty values.
            for j, cell in enumerate(row, start=1):
                if cell == '':
                    print(f"Row {i} has an empty value in column {j}.")

            # Example specific check: Verify that the first column contains integers.
            try:
                int(row[0])
            except ValueError:
                print(f"Invalid data in column 1 of row {i} (expected integer).")

            # Additional checks for other columns can be added here as needed.


# Indicate the beginning of the CSV file check and call the function with a specific file path.
print("Checking CSV file for errors...")
check_csv('edited_example1.csv')  # Replace 'edited_example1.csv' with the actual CSV file path.
