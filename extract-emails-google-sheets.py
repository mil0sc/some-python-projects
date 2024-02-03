# extract-emails-google-sheets.py
# Connects to a Google Sheets document by its ID, reads email addresses from a specified column using a regular expression,
# and compiles a list of these emails. It starts from the second row to skip the header and prints out all found email addresses.

import ezsheets
import re

# Specify the ID of your Google Sheet (replace the placeholder ID with your actual Google Sheet ID).
spreadsheet_id = ''

# Use ezsheets to authenticate and access the spreadsheet by its ID.
ss = ezsheets.Spreadsheet(spreadsheet_id)

# Access the first sheet within the spreadsheet.
sheet = ss[0]

# Define the column from which to extract email addresses, assuming it's the third column ('C').
emails_column = sheet.getColumn(3)

# Compile a regular expression pattern to identify email addresses.
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')

# Initialize a list to store found email addresses.
email_list = []

# Iterate through each entry in the specified column, skipping the header.
for email in emails_column[1:]:  # Starts from the second element to skip the header.
    if email:  # Ensure the cell is not empty.
        # Find all matches of the email pattern in the current cell's text.
        found_emails = email_pattern.findall(email)
        # Extend the email list with any found matches.
        email_list.extend(found_emails)

# Output or otherwise process the compiled list of email addresses.
for email in email_list:
    print(email)
