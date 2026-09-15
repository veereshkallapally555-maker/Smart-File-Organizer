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

def move_file(file_path, category, dry_run=False):
    destination = file_path.parent / category
    target = destination / file_path.name

    if target.exists():
        print(
            f"⚠️ Skipped: {file_path.name} "
            f"already exists in {category}"
        )
        return False

    if dry_run:
        print(f"👀 Would move {file_path.name} --> {category}")
        return True

    destination.mkdir(exist_ok=True)
    shutil.move(str(file_path), str(target))
    return True

def main():
    print("=== Smart File Organizer ===")

    folder = get_folder_path()

    if folder is None:
        return

    print("Folder found:", folder)

    print("\nChoose an option:")
    print("1. Organize files")
    print("2. Preview changes")

    choice = input("Enter choice (1-2): ").strip()

    if choice == "1":
        show_files(folder, dry_run=False)

    elif choice == "2":
        show_files(folder, dry_run=True)

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

def get_folder_path():
    folder = input("Enter folder path: ").strip()
    path = Path(folder)

    if path.exists() and path.is_dir():
        return path

    print("❌ Folder does not exist or the path is not a directory.")
    return None

def show_files(folder, dry_run=False):
    print("\n=== Files Found ===\n")

    counts = {}

    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item.suffix)

            if move_file(item, category, dry_run):
                counts[category] = counts.get(category, 0) + 1

    print("\n=== Organization Summary ===")

    if not counts:
        print("No files to organize.")
        return

    for category, count in counts.items():
        print(f"📁 {category}: {count} file(s)")

    action = "would be moved" if dry_run else "moved"
    print(f"\n✅ Total files {action}: {sum(counts.values())}")


if __name__ == "__main__":
    main()
