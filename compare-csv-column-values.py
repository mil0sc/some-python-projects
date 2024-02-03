# compare-csv-column-values.py
# Compares numerical values in a specified column across all rows of a CSV file, reporting which rows have larger or smaller values.

import csv


def compare_values_in_column(csv_file_path, column_index):
    """
    Reads a CSV file and compares values in a specified column, reporting relative sizes between rows.

    Args:
    csv_file_path (str): Path to the CSV file.
    column_index (int): Zero-based index of the column to compare.
    """
    # Open the CSV file and read its contents.
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Convert reader object to a list for easy access.

    # Iterate through each row to compare its value in the specified column with all other rows.
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):  # Start from the next row to avoid repeating comparisons.
            try:
                # Attempt to convert column values to float for numerical comparison.
                value1 = float(rows[i][column_index])
                value2 = float(rows[j][column_index])

                # Compare values and print findings.
                if value1 > value2:
                    print(f"Row {i + 1} has a larger value than Row {j + 1} in column {column_index + 1}.")
                elif value1 < value2:
                    print(f"Row {i + 1} has a smaller value than Row {j + 1} in column {column_index + 1}.")
            except ValueError:
                # Handle the case where data cannot be converted to float (e.g., non-numeric data).
                print("Non-numeric data found. Skipping comparison.")


# Example function call
compare_values_in_column('example1.csv', 2)  # Example CSV file path and column index for comparison.
