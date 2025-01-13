import os
import subprocess
from pathlib import Path
from datetime import datetime
from kg_rememberall.utils.file_processing import (
    is_binary,
    get_description,
    summarize_directory,
    get_code_block_marker,
    convert_and_cleanup_notebooks,
)


def download_repo(repo_url, destination_folder):
    """
    Clone a repository or download its contents.

    Args:
        repo_url (str): URL of the repository to download.
        destination_folder (str): Path to the directory where the repository will be saved.

    Returns:
        str: Path to the downloaded repository.
    """
    dest_path = Path(destination_folder)
    dest_path.mkdir(parents=True, exist_ok=True)

    repo_name = Path(repo_url).stem
    repo_dir = dest_path / repo_name

    if repo_dir.exists():
        print(f"Directory {repo_dir} already exists. Skipping download.")
        return str(repo_dir)

    try:
        subprocess.run(["git", "clone", repo_url, str(repo_dir)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        raise

    return str(repo_dir)


def create_combined_markdown(src_dir, output_file, max_lines=512):
    """
    Combine repository contents into a Markdown summary.

    Args:
        src_dir (str): Directory containing repository files.
        output_file (str): Path to save the Markdown summary.
        max_lines (int): Maximum lines of content to preview from each file.
    """
    errors = []

    with open(output_file, "w") as markdown_file:
        markdown_file.write("# Combined Context for Repository\n\n")
        markdown_file.write(f"Source Directory: {src_dir}\n")
        markdown_file.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Directory summary
        markdown_file.write("## Directory Summary\n\n")
        summary = summarize_directory(src_dir)
        for ext, count in summary.items():
            markdown_file.write(f"* {ext if ext else 'No extension'}: {count} files\n")
        markdown_file.write("\n")

        # File previews
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if not is_binary(file_path):
                    description = get_description(file_path)
                    code_marker = get_code_block_marker(file_path)

                    markdown_file.write(f"## File: {file}\n\n")
                    markdown_file.write(f"*Description*: {description}\n\n")

                    markdown_file.write(f"```{code_marker}\n")
                    try:
                        with open(file_path, "r") as input_file:
                            lines = input_file.readlines()
                            markdown_file.writelines(lines[:max_lines])
                            if len(lines) > max_lines:
                                markdown_file.write("\n*Content truncated for brevity.*\n")
                    except Exception as e:
                        errors.append(f"Error reading file {file_path}: {e}")
                        markdown_file.write(f"Error reading file: {e}\n")
                    markdown_file.write("\n```\n\n")

    # Log errors, if any
    if errors:
        print("Errors encountered during processing:")
        for error in errors:
            print(error)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Clone and summarize a repository.")
    parser.add_argument("--repo-url", required=True, help="URL of the repository to clone.")
    parser.add_argument("--dest-folder", default="data/raw", help="Directory to save the repository.")
    parser.add_argument("--output-file", required=True, help="Path to save the Markdown summary.")

    args = parser.parse_args()

    # Clone or download the repository
    repo_path = download_repo(args.repo_url, args.dest_folder)

    # Convert notebooks to scripts
    convert_and_cleanup_notebooks(repo_path)

    # Generate Markdown summary
    create_combined_markdown(repo_path, args.output_file)
    print(f"Markdown summary saved to: {args.output_file}")


if __name__ == "__main__":
    main()
