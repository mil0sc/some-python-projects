# Phase 1: Setup
import os

folder = '/Users/milosz/Desktop/testFolder'
prefix = 'spam'
folder = os.path.abspath(folder)

if not os.path.exists(folder):
    print(f"The folder {folder} does not exist. Exiting.")
    exit(1)

# Phase 2: Data Collection
all_files = os.listdir(folder)
relevant_files = [filename for filename in all_files if filename.startswith(prefix)]

# Phase 3: Analyze File Numbers
file_numbers = [int(filename[len(prefix):filename.index('.')]) for filename in relevant_files]
file_numbers.sort()

# Phase 4: Renaming to Close Gaps
expected_number = 1

for number in file_numbers:
    if number != expected_number:
        old_name = f"{prefix}{str(number).zfill(3)}.txt"
        new_name = f"{prefix}{str(expected_number).zfill(3)}.txt"

        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

    expected_number += 1



