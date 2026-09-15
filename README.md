# 📂 Smart File Organizer

A Python automation tool that organizes files into separate folders based on their file extensions.

The project provides a simple command-line interface (CLI) that allows users to either organize files automatically or preview what changes would be made before moving anything.

---

## ✨ Features

- 📁 Organizes files automatically based on file extension
- 🖼️ Supports Images
- 📄 Supports Documents
- 🎵 Supports Audio
- 🎬 Supports Videos
- 📦 Supports Archives
- ❓ Places unknown file types into an `Others` folder
- 📂 Creates category folders automatically when needed
- 👀 Preview mode to see what files would be moved
- ⚠️ Prevents overwriting existing files
- 🔍 Validates the provided folder path
- 📊 Displays an organization summary
- 🖥️ Interactive command-line interface

---

## 📁 Supported File Types

| Category | Extensions |
|----------|------------|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac` |
| Videos | `.mp4`, `.avi`, `.mov`, `.mkv` |
| Archives | `.zip`, `.rar`, `.tar`, `.gz` |
| Others | Unknown or unsupported extensions |

---

## 📂 Project Structure

```text
Smart-File-Organizer/
│
├── organizer.py
├── README.md
├── .gitignore
└── test_folder/
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/veereshkallapally555-maker/Smart-File-Organizer.git
```

### 2. Open the project

Open the project folder in VS Code.

### 3. Run the program

```bash
python organizer.py
```

### 4. Enter the folder path

The program will ask for the folder you want to organize.

### 5. Choose an option

```text
Choose an option:
1. Organize files
2. Preview changes
```

**Organize files** moves the files into their appropriate folders.

**Preview changes** shows which files would be moved without actually moving them.

---

## 🖥️ Example

```text
=== Smart File Organizer ===

Enter folder path: test_folder

Folder found: test_folder

Choose an option:
1. Organize files
2. Preview changes

Enter choice (1-2): 1

=== Files Found ===

=== Organization Summary ===
📁 Documents: 1 file(s)
📁 Images: 1 file(s)
📁 Audio: 1 file(s)
📁 Videos: 1 file(s)

✅ Total files moved: 4
```

---

## 🛠️ Technologies Used

- Python 3
- pathlib
- shutil

---

## 📚 Concepts Demonstrated

- Functions
- Dictionaries
- Loops
- Conditional statements
- File handling
- Path manipulation
- File organization automation
- Git
- GitHub

---

## 🔮 Future Improvements

- GUI version
- Logging
- Progress bar
- Configuration file
- Unit tests

---

## 👨‍💻 Author

**Veeresh Kallapally**

- GitHub: [@veereshkallapally555-maker](https://github.com/veereshkallapally555-maker)
- LinkedIn: [Veeresh Kallapally](https://www.linkedin.com/in/veeresh-kallapally-a87164390/)
