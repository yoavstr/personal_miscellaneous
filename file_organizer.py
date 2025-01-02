import os
import shutil

# Define the folder path (change this to your Downloads folder path)
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# Mapping of file extensions to folder names
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.pptx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.dmg', '.sh'],
    'Other': []  # For uncategorized file types
}

def create_folder_if_not_exists(folder_path):
    """Creates a folder if it does not exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_file(file_name, source_folder, destination_folder):
    """Move the file from source_folder to destination_folder."""
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)
    
    # Move the file
    shutil.move(source_path, destination_path)
    print(f"Moved: {file_name} to {destination_folder}")

def organize_downloads():
    """Organize files in the Downloads folder by type."""
    # Create folders for each file type category
    for category in FILE_CATEGORIES.keys():
        create_folder_if_not_exists(os.path.join(DOWNLOADS_FOLDER, category))
    
    # List all files in the Downloads folder
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        # Skip if it is a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(file_name)

        # Determine the folder based on the file extension
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                move_file(file_name, DOWNLOADS_FOLDER, os.path.join(DOWNLOADS_FOLDER, category))
                moved = True
                break

        # Move to 'Other' folder if no matching category
        if not moved:
            move_file(file_name, DOWNLOADS_FOLDER, os.path.join(DOWNLOADS_FOLDER, 'Other'))

if __name__ == "__main__":
    organize_downloads()
