# InsertNumberingGap.py
# This script renumbers files with a specific prefix in a directory to insert a gap at a specified position.

import os

# Setup: Define the target folder and file prefix.
folder = '/Users/milosz/Desktop/testFolder'
prefix = 'spam'
folder = os.path.abspath(folder)  # Ensure the folder path is absolute.

# Check if the folder exists to avoid errors.
if not os.path.exists(folder):
    print(f"The folder {folder} does not exist. Exiting.")
    exit(1)

# Data Collection: Gather all files starting with the specified prefix.
all_files = os.listdir(folder)
relevant_files = [filename for filename in all_files if filename.startswith(prefix)]

# Analyze File Numbers: Extract and sort the numerical part of the file names.
file_numbers = [int(filename[len(prefix):filename.index('.')]) for filename in relevant_files]
file_numbers.sort()

# Renaming to Insert Gap: Determine the gap position based on user input.
gap_position = int(input("Enter the position where you want to insert the gap: "))

# Validate the gap position.
if gap_position <= 0 or gap_position > max(file_numbers):
    print("Invalid gap position. Exiting.")
    exit(1)

# Rename files to insert the gap, working in reverse order to avoid overwriting files.
for number in reversed(file_numbers):
    if number >= gap_position:
        # Format old and new file names to maintain leading zeros.
        old_name = f"{prefix}{str(number).zfill(3)}.txt"
        new_name = f"{prefix}{str(number + 1).zfill(3)}.txt"

        # Construct full paths for the old and new file names.
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        # Perform the file rename operation.
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")
