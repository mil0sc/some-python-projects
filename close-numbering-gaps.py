# CloseNumberingGaps.py
# This script sequentially renumbers files with a specified prefix in a directory to close any gaps in their numbering.

import os

# Setup: Specify the target folder and the file prefix.
folder = '/Users/milosz/Desktop/testFolder'
prefix = 'spam'
# Convert the specified folder path to an absolute path.
folder = os.path.abspath(folder)

# Verify the existence of the folder to proceed.
if not os.path.exists(folder):
    print(f"The folder {folder} does not exist. Exiting.")
    exit(1)

# Data Collection: Identify all files in the folder starting with the prefix.
all_files = os.listdir(folder)
relevant_files = [filename for filename in all_files if filename.startswith(prefix)]

# Analyze File Numbers: Extract the numerical part of each relevant file's name and sort them.
file_numbers = [int(filename[len(prefix):filename.index('.')]) for filename in relevant_files]
file_numbers.sort()

# Renaming to Close Gaps: Adjust file numbering to eliminate any gaps.
expected_number = 1  # Start with 1 as the first expected number in the sequence.

for number in file_numbers:
    if number != expected_number:
        # Construct old and new file names based on current and expected numbering.
        old_name = f"{prefix}{str(number).zfill(3)}.txt"
        new_name = f"{prefix}{str(expected_number).zfill(3)}.txt"

        # Generate full paths for the current (old) and new file names.
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        # Rename the file to close the numbering gap.
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

    expected_number += 1  # Increment the expected number for the next iteration.
