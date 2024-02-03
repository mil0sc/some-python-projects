# RegexFileSearcher.py
# This program searches for and displays lines from .txt files in a specified folder that match a user-defined regular expression.

import os
import re

# Prompt user for the target folder path and validate its existence and access permissions.
target_folder = input("Please enter the path to the folder containing .txt files: ")
if os.path.exists(target_folder) and os.access(target_folder, os.R_OK):
    print(f"The folder '{target_folder}' exists and is accessible for reading.")
else:
    print(f"Error: The folder '{target_folder}' either does not exist or is not accessible.")
    exit(1)

# Request a regular expression from the user for searching within the text files.
user_regex = input("Please enter the regular expression you wish to search for: ")
print(f"Regular expression to search: {user_regex}")

# List all .txt files in the specified folder.
all_files = os.listdir(target_folder)
txt_files = [f for f in all_files if f.endswith('.txt')]
print("List of .txt files:", txt_files)

# Compile the user-provided regular expression for efficient matching.
compiled_regex = re.compile(user_regex)

# Initialize a dictionary to store matches found in files.
matches = {}

# Search each text file for lines matching the regular expression.
for txt_file in txt_files:
    file_path = os.path.join(target_folder, txt_file)
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file.readlines(), 1):
                if compiled_regex.search(line):
                    matches.setdefault(txt_file, []).append((line_number, line.strip()))
    except IOError:
        print(f"Could not read {txt_file}. Skipping.")

# Display summary of matches found, if any.
if matches:
    print("\nSummary of all matches:")
    for filename, match_list in matches.items():
        print(f"In {filename}:")
        for line_number, line_text in match_list:
            print(f"  Line {line_number}: {line_text}")
else:
    print("No matches found.")
