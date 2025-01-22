import os
import glob


def rename_png_icons():
    # Get the current directory (where the script is located)
    folder_path = os.getcwd()

    # Use glob to search for all PNG files in the current directory
    png_files = glob.glob("*.png")

    renamed_files = []

    # Rename the PNG files if they have spaces in their names
    for png in png_files:
        if False and " " in png:
            new_name = png.replace(" ", "-")
            os.rename(png, new_name)
            renamed_files.append(new_name)
            print(f"Renamed '{png}' to '{new_name}'")
        else:
            renamed_files.append(png)
            print(f"No spaces found in '{png}', no renaming needed.")

    if not png_files:
        print(f"No PNG icons found in '{folder_path}'.")

    # List the renamed files
    print("\nUpdated PNG icons in the folder:")
    for png in renamed_files:
        print("addon/assets/icons/" + png)


if __name__ == "__main__":
    # Call the function to rename PNG icons and list them
    rename_png_icons()
