import os
import mimetypes
from pathlib import Path
import subprocess


def is_binary(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and "text" in mime_type:
        return False
    try:
        with open(file_path, "rb") as file:
            file.read(1024).decode("utf-8")
        return False
    except (UnicodeDecodeError, Exception):
        return True


def get_description(file_path):
    ext = Path(file_path).suffix
    return {
        ".py": "Python script",
        ".json": "JSON data file",
        ".md": "Markdown documentation",
    }.get(ext, f"{ext} file")


def summarize_directory(directory):
    summary = {}
    for root, _, files in os.walk(directory):
        for file in files:
            ext = Path(file).suffix
            summary[ext] = summary.get(ext, 0) + 1
    return summary


def get_code_block_marker(file_path):
    ext = Path(file_path).suffix
    return {
        ".py": "python",
        ".json": "json",
        ".md": "markdown",
    }.get(ext, "text")


def convert_and_cleanup_notebooks(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                file_path = os.path.join(root, file)
                print(f"Converting {file_path} to script...")
                try:
                    subprocess.run(["jupyter", "nbconvert", "--to", "script", file_path], check=True)
                    os.remove(file_path)
                    print(f"Removed {file_path} after conversion.")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {file_path}: {e}")
