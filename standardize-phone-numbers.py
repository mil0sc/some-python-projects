# standardize-phone-numbers.py
# Converts phone numbers from various formats to a standardized format.
# The standardized format is: (area code) first three digits-last four digits.

import re


def standardize_phone_number(phone):
    """
    Takes a phone number in various formats and standardizes it to the format: (area code) first three digits-last four digits.

    Args:
    phone (str): The phone number in a non-standard format.

    Returns:
    str: The phone number in the standardized format.
    """
    # Remove any non-digit characters from the phone number.
    digits_only = re.sub(r'\D', '', phone)

    # Extract the area code and local number components from the last 10 digits.
    area_code = digits_only[-10:-7]  # Extracts the area code.
    local_first = digits_only[-7:-4]  # Extracts the first part of the local number.
    local_second = digits_only[-4:]  # Extracts the second part of the local number.

    # Format the extracted components into the desired standardized format.
    standardized = f"({area_code}) {local_first}-{local_second}"

    return standardized


# Test the function with a list of phone numbers in various formats.
phone_numbers = ['(123) 456-7890', '123.456.7890', '+
