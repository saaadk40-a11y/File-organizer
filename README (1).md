# File Organizer

## Project Overview

The **File Organizer** is a Python application that scans a given folder, sorts files into category folders based on their extension (Images, Documents, PDFs, Videos, Audio, Archives, Code, Others), and generates a detailed summary report of everything it did.

---

## Objective

- To automatically organize a messy folder by file type.
- To practice Object-Oriented Programming (OOP) and file handling in Python.
- To generate a clear, timestamped summary report of the operation.

---

## Features

- Reads all files from a given folder.
- Creates category folders automatically based on file extension.
- Moves files into their respective category folders.
- Avoids overwriting files with the same name (auto-renames duplicates, e.g. `photo_1.jpg`).
- Skips folders and the report file itself so re-runs don't break.
- Generates a `.txt` summary report containing:
  - Total number of files processed
  - Number of files per category
  - Full list of moved files (old name → new location)
  - Timestamp of execution
- Handles invalid directory errors gracefully.

---

## Libraries Used

- **os** – to list folder contents and check paths.
- **shutil** – to move files safely.
- **datetime** – to timestamp the report.

---

## Programming Concepts Used

- Object-Oriented Programming (`FileOrganizer` class)
- File Handling
- Functions
- Loops
- Dictionaries (extension → category mapping)
- Exception Handling

---

## Workflow

1. Enter the folder path to organize.
2. Check if the directory exists.
3. Read all files in the folder (subfolders are left untouched).
4. Determine each file's category from its extension.
5. Create the category folder if it doesn't already exist.
6. Move the file into that folder (auto-renaming on conflicts).
7. Generate and save `organizer_report.txt` with full details.

---

## How to Run

```bash
python file_organizer.py
```

You'll be prompted to enter the folder path. Once it finishes, check the same folder for:
- New category subfolders (`Images/`, `Documents/`, `PDFs/`, etc.)
- `organizer_report.txt` with the full summary

---

## Category Mapping

| Category  | Extensions |
|---|---|
| Images | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp |
| Documents | .doc, .docx, .txt, .xlsx, .xls, .ppt, .pptx, .csv |
| PDFs | .pdf |
| Videos | .mp4, .mkv, .avi, .mov, .wmv |
| Audio | .mp3, .wav, .aac, .flac |
| Archives | .zip, .rar, .7z, .tar, .gz |
| Code | .py, .js, .html, .css, .java, .cpp, .c, .json |
| Others | anything not listed above |

---

## Learning Outcomes

- Learned how to structure a real task using OOP (a `FileOrganizer` class holding state and behavior).
- Learned to safely move files with `shutil.move()`, including handling naming conflicts.
- Practiced file handling by generating a formatted `.txt` report.
- Used `datetime` to timestamp program execution.
- Practiced exception handling for invalid folder paths and file system errors.
- Improved understanding of dictionaries, loops, and functions in a practical context.

---

## Uploading this project to GitHub

```bash
git init
git add .
git commit -m "Add File Organizer: OOP-based file sorter with report generation"
git branch -M main
git remote add origin https://github.com/<your-username>/file-organizer.git
git push -u origin main
```

---

## Conclusion

This project automatically organizes a cluttered folder into clean, categorized subfolders and produces a clear report of every action taken. It reinforced practical skills in Python file handling, OOP design, and exception handling.
