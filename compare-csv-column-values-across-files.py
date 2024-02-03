# compare-csv-column-values-across-files.py
# Compares numerical values in a specified column between two CSV files, reporting which rows contain larger values.

import csv


def compare_rows_and_report_larger_value(csv_file_path1, csv_file_path2, column_index):
    """
    Compares values in a specified column between two CSV files and reports comparisons of those values.

    Args:
    csv_file_path1 (str): Path to the first CSV file.
    csv_file_path2 (str): Path to the second CSV file.
    column_index (int): The one-based index of the column to compare.
    """
    # Adjust column index for zero-based indexing used in programming.
    column_index -= 1

    # Open both CSV files.
    with open(csv_file_path1, mode='r') as file1, open(csv_file_path2, mode='r') as file2:
        reader1, reader2 = csv.reader(file1), csv.reader(file2)

        # Skip header rows in both files.
        next(reader1), next(reader2)

        # Convert rows from both readers to lists for direct access.
        rows1, rows2 = list(reader1), list(reader2)

        # Iterate through each row in both lists for comparison.
        for i, row1 in enumerate(rows1):
            for j, row2 in enumerate(rows2):
                try:
                    # Check if the specified column index is within the range of both rows.
                    if column_index >= len(row1) or column_index >= len(row2):
                        print(
                            f"Column index out of range for comparison at Row {i + 1} in File 1 or Row {j + 1} in File 2.")
                        continue

                    # Compare numerical values from the specified column in both rows.
                    value1, value2 = float(row1[column_index]), float(row2[column_index])
                    if value1 > value2:
                        print(
                            f"Row {i + 1} in File 1 (Value: {value1}) is larger than Row {j + 1} in File 2 (Value: {value2}) in Column {column_index + 1}.")
                    elif value1 < value2:
                        print(
                            f"Row {j + 1} in File 2 (Value: {value2}) is larger than Row {i + 1} in File 1 (Value: {value1}) in Column {column_index + 1}.")
                    else:
                        print(
                            f"Row {i + 1} in File 1 and Row {j + 1} in File 2 have the same value ({value1}) in Column {column_index + 1}.")
                except ValueError as e:
                    # Handle non-numeric data that cannot be converted to float.
                    print(f"Error processing comparison at Row {i + 1} in File 1 and Row {j + 1} in File 2: {e}")


# Example usage of the function.
compare_rows_and_report_larger_value('example1.csv', 'example2.csv', 2)
