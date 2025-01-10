import os

def lowercase_folders():
    base_folder = os.getcwd()  # Get the current working directory

    for root, dirs, _ in os.walk(base_folder):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            lower_folder_name = folder.lower()
            new_folder_path = os.path.join(root, lower_folder_name)

            # Rename only if the new folder name is different
            if folder_path != new_folder_path:
                os.rename(folder_path, new_folder_path)
                print(f"Renamed folder: {folder_path} -> {new_folder_path}")

if __name__ == "__main__":
    lowercase_folders()
