import os
import shutil
from datetime import datetime


class FileOrganizer:

    CATEGORY_MAP = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"],
        "PDFs": [".pdf"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"],
    }

    def __init__(self, folder_path):
        self.folder_path = os.path.abspath(folder_path)
        self.moved_files = []
        self.category_counts = {}
        self.total_processed = 0
        self.errors = []

        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Path does not exist: {self.folder_path}")
        if not os.path.isdir(self.folder_path):
            raise NotADirectoryError(f"Path is not a directory: {self.folder_path}")

    def _get_category(self, extension):
        extension = extension.lower()
        for category, extensions in self.CATEGORY_MAP.items():
            if extension in extensions:
                return category
        return "Others"

    def _ensure_folder(self, category):
        category_path = os.path.join(self.folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        return category_path

    def organize(self):
        entries = os.listdir(self.folder_path)

        known_category_folders = set(self.CATEGORY_MAP.keys()) | {"Others"}

        for entry_name in entries:
            entry_path = os.path.join(self.folder_path, entry_name)

            if os.path.isdir(entry_path):
                continue

            if entry_name == "scan_report.txt" or entry_name == "organizer_report.txt":
                continue

            self.total_processed += 1
            _, extension = os.path.splitext(entry_name)
            category = self._get_category(extension)

            try:
                category_path = self._ensure_folder(category)
                destination_path = os.path.join(category_path, entry_name)

                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(entry_name)
                    counter = 1
                    while os.path.exists(destination_path):
                        new_name = f"{base}_{counter}{ext}"
                        destination_path = os.path.join(category_path, new_name)
                        counter += 1

                shutil.move(entry_path, destination_path)

                self.moved_files.append({
                    "original_name": entry_name,
                    "category": category,
                    "new_path": destination_path,
                })
                self.category_counts[category] = self.category_counts.get(category, 0) + 1

            except (OSError, shutil.Error, PermissionError) as e:
                self.errors.append({"file": entry_name, "error": str(e)})

    def print_summary(self):
        print(f"Folder organized: {self.folder_path}")
        print(f"Total files processed: {self.total_processed}")
        for category, count in self.category_counts.items():
            print(f"  {category}: {count}")
        if self.errors:
            print(f"Errors encountered: {len(self.errors)}")

    def save_report(self, output_file="organizer_report.txt"):
        output_path = os.path.join(self.folder_path, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("=" * 70 + "\n")
            f.write("FILE ORGANIZER - SUMMARY REPORT\n")
            f.write("=" * 70 + "\n")
            f.write(f"Folder organized : {self.folder_path}\n")
            f.write(f"Timestamp        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total files found: {self.total_processed}\n")
            f.write("-" * 70 + "\n")

            f.write("FILES PER CATEGORY:\n")
            if self.category_counts:
                for category, count in sorted(self.category_counts.items()):
                    f.write(f"  {category:<15}: {count} file(s)\n")
            else:
                f.write("  No files were moved.\n")
            f.write("-" * 70 + "\n")

            f.write("MOVED FILES:\n")
            if self.moved_files:
                for item in self.moved_files:
                    f.write(f"  [{item['category']}] {item['original_name']} -> {item['new_path']}\n")
            else:
                f.write("  No files were moved.\n")
            f.write("-" * 70 + "\n")

            if self.errors:
                f.write("ERRORS:\n")
                for err in self.errors:
                    f.write(f"  {err['file']}: {err['error']}\n")
                f.write("-" * 70 + "\n")

            f.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 70 + "\n")

        return output_path


def main():
    folder_path = input("Enter the folder path you want to organize: ").strip()

    try:
        organizer = FileOrganizer(folder_path)
        organizer.organize()
        organizer.print_summary()
        report_path = organizer.save_report("organizer_report.txt")
        print(f"\nReport saved to: {report_path}")
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
