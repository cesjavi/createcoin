import os
import sys

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Skip binary files
        return

    new_content = content.replace('bitcoin', 'tugo')
    new_content = new_content.replace('Bitcoin', 'Tugo')
    new_content = new_content.replace('BITCOIN', 'TUGO')

    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated content in: {filepath}")

def process_directory(root_dir):
    # Walk bottom-up to handle directory renaming correctly
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Skip .git directory
        if '.git' in dirpath.split(os.sep):
            continue

        # Rename and update files
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            # Update content
            replace_in_file(filepath)

            # Rename file if needed
            if 'bitcoin' in filename.lower():
                new_filename = filename.replace('bitcoin', 'tugo')
                new_filename = new_filename.replace('Bitcoin', 'Tugo') # Handle Case
                new_filename = new_filename.replace('BITCOIN', 'TUGO')

                new_filepath = os.path.join(dirpath, new_filename)
                os.rename(filepath, new_filepath)
                print(f"Renamed file: {filepath} -> {new_filepath}")

        # Rename directories
        for dirname in dirnames:
            if 'bitcoin' in dirname.lower():
                old_dirpath = os.path.join(dirpath, dirname)
                new_dirname = dirname.replace('bitcoin', 'tugo')
                new_dirname = new_dirname.replace('Bitcoin', 'Tugo')
                new_dirname = new_dirname.replace('BITCOIN', 'TUGO')
                new_dirpath = os.path.join(dirpath, new_dirname)
                os.rename(old_dirpath, new_dirpath)
                print(f"Renamed directory: {old_dirpath} -> {new_dirpath}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 rename_project.py <directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' not found.")
        sys.exit(1)

    print(f"Processing directory: {target_dir}")
    process_directory(target_dir)
    print("Done.")
