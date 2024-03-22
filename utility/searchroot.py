import os
from pprint import pprint

def collect_files_by_kind(root_dir,suffix):
    """
    Collect all .md file paths under the given root directory.

    Parameters:
    - root_dir: The root directory from which to start searching for .md files.

    Returns:
    - A list of strings, where each string is the relative path to a .md file found under the root directory.
    """
    md_files = []  # List to store the relative paths of .md files
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(f'.{suffix}'):
                relative_path = os.path.relpath(os.path.join(root, file), start=root_dir)
                windows_path = './{}'.format(relative_path.replace('\\', '/') )
                if  windows_path.count('/') > 1:
                    md_files.append(windows_path)
    return md_files

if __name__ == "__main__":
    # Example usage
    root_directory = './docs'  # Change this to your actual root directory
    md_file_paths = collect_files_by_kind(root_directory,suffix="md")
    pprint(md_file_paths)
