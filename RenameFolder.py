import os
import re

def rename_folders():
    base_folder = os.getcwd()  # Get the current working directory

    for root, dirs, files in os.walk(base_folder):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            weapon_values = []

            # Loop through all files in the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".properties"):
                    file_path = os.path.join(folder_path, file_name)

                    # Read the file content
                    with open(file_path, 'r') as file:
                        for line in file:
                            # Check if the line contains "nbt.Weapon"
                            match = re.match(r"nbt\.Weapon=(\d+)", line.strip())
                            if match:
                                weapon_values.append(match.group(1))

            # If weapon values were found, rename the folder
            if weapon_values:
                weapon_values = sorted(set(weapon_values))  # Remove duplicates and sort
                new_folder_name = f"weapon{'-'.join(weapon_values)}"
                new_folder_path = os.path.join(root, new_folder_name)
                
                # Rename only if the new folder name doesn't already exist
                if not os.path.exists(new_folder_path):
                    os.rename(folder_path, new_folder_path)
                    print(f"Renamed folder: {folder_path} -> {new_folder_path}")
                else:
                    print(f"Folder already exists: {new_folder_path}, skipping rename.")

if __name__ == "__main__":
    rename_folders()
