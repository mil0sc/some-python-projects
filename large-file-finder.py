import os

# Define the target folder for the search.
folder = '/Users/milosz/Desktop'
# Convert the folder path to an absolute path to ensure consistency.
folder = os.path.abspath(folder)

# Check if the folder exists to prevent errors.
if not os.path.exists(folder):
    print(f"The folder {folder} does not exist. Exiting.")
    exit(1)

# Lists to store the paths and sizes of large folders and files.
large_folders = []
large_files = []

# Walk through the directory tree.
for foldername, subfolders, filenames in os.walk(folder):
    folder_size = 0  # Initialize the total size of the current folder.

    # Check the size of each file in the current directory.
    for filename in filenames:
        file_path = os.path.join(foldername, filename)  # Full path to the file.
        file_size = os.path.getsize(file_path)  # Size of the file in bytes.
        file_size_mb = file_size / (1024 * 1024)  # Convert file size to megabytes.

        # If the file is larger than 100MB, add it to the large_files list.
        if file_size_mb > 100:
            large_files.append((file_path, file_size_mb))

        folder_size += file_size  # Add the file size to the total folder size.

    folder_size_mb = folder_size / (1024 * 1024)  # Convert total folder size to megabytes.

    # If the folder's total size is larger than 100MB, add it to the large_folders list.
    if folder_size_mb > 100:
        large_folders.append((foldername, folder_size_mb))

# Print the list of folders that are larger than 100MB.
if large_folders:
    print("The following folders are larger than 100MB:")
    for folder_name, folder_size in large_folders:
        print(f"{folder_name} - {folder_size:.2f} MB")
else:
    print("No folders larger than 100MB were found.")

# Print the list of files that are larger than 100MB.
if large_files:
    print("The following files are larger than 100MB:")
    for file_name, file_size in large_files:
        print(f"{file_name} - {file_size:.2f} MB")
else:
    print("No files larger than 100MB were found.")
