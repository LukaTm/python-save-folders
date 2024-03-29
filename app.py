import os
import shutil

source_directories = [
    # AppData/Local
    os.path.join(os.environ['LOCALAPPDATA']),
    # Appdata/local .. / Appdata/LocalLow
    os.path.join(os.environ['LOCALAPPDATA'], '..', 'LocalLow'),
    # %APPDATA% - AppData/Roaming
    os.path.join(os.environ['APPDATA']),
    # Home Directory - C:\Users\username
    os.path.join(os.path.expanduser('~'), 'Documents'),
]

source_directoriess = [
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
        found_folder = False
        for directory in source_directories:
            folder_path = os.path.join(directory, folder_name)
            if os.path.exists(folder_path):
                # Copy the folder to the destination directory
                shutil.copytree(folder_path, os.path.join(destination_directory, folder_name), dirs_exist_ok=True)
                found_folder = True
                break
        if not found_folder:
            print(f"Could not find folder '{folder_name}' in any of the directories - {source_directories}")
