import shutil  # Provides high-level file operations.
import os  # Provides a way of using operating system dependent functionality.

# Define the source folder path and target extensions.
folder = '/Users/milosz/Documents/TestFolder'
extensions_to_look_for = ['.pdf', '.jpg',]
# Convert the folder path to an absolute path (resolves any relative path).
folder = os.path.abspath(folder)

# Check if the source folder exists to avoid errors.
if not os.path.exists(folder):
    print(f"The folder {folder} does not exist. Exiting.")
    exit(1)

# Ensure there's at least one extension to look for.
if not extensions_to_look_for:
    print("You must specify at least one file extension to back up. Exiting.")
    exit(1)

# Traverse the directory tree starting at 'folder'.
for foldername, subfolders, filenames in os.walk(folder):
    # Iterate through each file in the current foldername.
    for filename in filenames:
        # Extract the file extension of the current file.
        file_extension = os.path.splitext(filename)[1]

        # Check if the file's extension is one of the extensions we're looking for.
        if file_extension in extensions_to_look_for:
            # Construct the full path to the file to copy.
            file_to_copy = os.path.join(foldername, filename)
            # Copy the file to the target directory.
            shutil.copy(file_to_copy, '/Users/milosz/Desktop/londyn')
