import os
import shutil

print("Maya directory is ")
# Prompt the user for the source directory containing Python files
source_dir = input("Enter the path of the source directory containing Python files: ")
# Prompt the user for the destination directory where Python files will be copied
dest_dir = input("Enter the path of the destination directory where Python files will be copied: ")

# Loop through all files in the source directory
for file_name in os.listdir(source_dir):
    # Check if the file is a Python file
    if file_name.endswith(".py"):
        # Get the full path of the file
        file_path = os.path.join(source_dir, file_name)
        # Check if a file with the same name already exists in the destination directory
        if os.path.exists(os.path.join(dest_dir, file_name)):
            print(f"A file with the name {file_name} already exists in the destination directory.")
        else:
            # Copy the file to the destination directory
            shutil.copy(file_path, dest_dir)
            print(f"{file_name} has been copied to the destination directory.")
