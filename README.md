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
