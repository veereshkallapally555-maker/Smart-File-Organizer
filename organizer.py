import shutil
from pathlib import Path

FILE_TYPES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",

    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".tar": "Archives",
    ".gz": "Archives"
}

def get_category(extension):
    return FILE_TYPES.get(extension.lower(), "Others")

def move_file(file_path, category):
    destination = file_path.parent / category
    destination.mkdir(exist_ok=True)
    shutil.move(str(file_path), str(destination / file_path.name))

def main():
    print("=== Smart File Organizer ===")

    folder = get_folder_path()

    if folder is None:
        return
    print("folder found: ",folder)

    show_files(folder)

def get_folder_path():
    folder = input("Enter folder path: ").strip()
    path = Path(folder)

    if path.exists() and path.is_dir():
        return path

    print("❌ Folder does not exist or the path is not a directory.")
    return None

def show_files(folder):
    print("\n Files Found \n")

    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            move_file(item, category)
            print(f"moved{item.name} --> {category}")


if __name__ == "__main__":
    main()
