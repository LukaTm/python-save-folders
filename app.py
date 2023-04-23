import os
import shutil

source_directories = [
    os.path.join(os.environ['APPDATA'], 'Local'),
    os.path.join(os.environ['APPDATA'], 'LocalLow'),
    os.path.join(os.environ['APPDATA'], 'Roaming'),
    os.path.join(os.path.expanduser('~'), 'Documents'),
]

# CURRENT DIRECTORY
current_directory = os.getcwd()
file_path = os.path.join(current_directory,'folders.txt')

destination_directory = os.path.join(os.getcwd(), 'all_files')

# Create the destination directory if it does not exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Open the txt file containing the folder names
with open(file_path, 'r') as f:
    for line in f:
        folder_name = line.strip()
        for directory in source_directories:
            if os.path.exists(os.path.join(directory, folder_name)):
                # Copy the folder to the destination directory
                shutil.copytree(os.path.join(directory, folder_name),
                                os.path.join(destination_directory, folder_name))
                break
