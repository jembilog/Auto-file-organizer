# 🧹 Auto File Organizer Bot

This Python bot automatically organizes files in your folder into categories like Documents, Images, Videos, and more!

---

## 🔧 How It Works

- Scans a target folder (default: `Downloads`)
- Moves files into subfolders based on their extension:
  - `.pdf` → `Documents/`
  - `.jpg` → `Images/`
  - `.zip` → `Archives/`
  - and more...

---

## 📦 Setup

1. Make sure you have Python installed.
2. Edit `organizer.py` and change this line:

```python
TARGET_FOLDER = "Downloads"
