import os
import shutil

#Customize this to the folder you want to clean
TARGET_FOLDER = "Downloads"

# File type categories
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh"],
}

def organize_files(folder_path):
    print(f"📂 Organizing files in: {folder_path}")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for category, extensions in CATEGORIES.items():
            if ext in extensions:
                category_path = os.path.join(folder_path, category)
                os.makedirs(category_path, exist_ok=True)
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"✅ Moved {filename} to {category}/")
                moved = True
                break

        if not moved:
            uncategorized_path = os.path.join(folder_path, "Others")
            os.makedirs(uncategorized_path, exist_ok=True)
            shutil.move(file_path, os.path.join(uncategorized_path, filename))
            print(f"📦 Moved {filename} to Others/")

if __name__ == "__main__":
    organize_files(TARGET_FOLDER)
