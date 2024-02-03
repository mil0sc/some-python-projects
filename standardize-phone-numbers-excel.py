# standardize-phone-numbers-excel.py
# Reads phone numbers from an Excel file, standardizes their format to (area code) first three digits-last four digits,
# and writes the updated numbers to a new Excel file. This ensures phone number consistency across records.

import pandas as pd  # For handling data in a tabular form.
import re  # For performing regex operations to clean and standardize phone numbers.


def standardize_phone_number(phone):
    """
    Standardizes a phone number to the format: (area code) first three digits-last four digits.

    Args:
    phone (str): A phone number in various possible formats.

    Returns:
    str: The standardized phone number.
    """
    # Remove any characters that are not digits.
    digits_only = re.sub(r'\D', '', phone)

    # Extract the area code and the first and second parts of the local number.
    area_code = digits_only[-10:-7]  # Extracts the area code from the last 10 digits.
    local_first = digits_only[-7:-4]  # Extracts the first 3 digits of the local number.
    local_second = digits_only[-4:]  # Extracts the last 4 digits of the local number.

    # Combine the parts into the standardized format.
    standardized = f"({area_code}) {local_first}-{local_second}"

    return standardized


# Load the original Excel file containing phone numbers into a DataFrame.
df = pd.read_excel("PhoneNumbers.xlsx")

# Apply the standardization function to each phone number in the 'Phone Number' column.
df['Phone Number'] = df['Phone Number'].apply(standardize_phone_number)

# Save the DataFrame with standardized phone numbers to a new Excel file.
df.to_excel("PhoneNumbers_Standardized.xlsx", index=False)

print("Phone numbers have been standardized and saved to 'PhoneNumbers_Standardized.xlsx'.")
