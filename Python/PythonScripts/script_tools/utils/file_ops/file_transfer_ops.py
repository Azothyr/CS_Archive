import os
import shutil
from handlers import debug_handler as debugger


def transfer_py_dir_in_current(source, destination, file_exceptions):
    """
    Transfer .py files from a source directory to a destination directory,
    excluding specified exceptions.
        Args:
        - source (str): The source directory path.
        - destination (str): The destination directory path.
        - file_exceptions (list): A list of filenames to exclude.
    """
    from .file_path_ops import clear_directory, print_files_at_location
    try:
        os.makedirs(destination, exist_ok=True)
        clear_directory(destination)

        for _root, _dirs, _files in os.walk(source):
            # print(_root, _dirs, _files)
            for file_name in _files:
                if file_name.endswith(".py") and file_name not in file_exceptions:
                    # print(f"Copying {file_name} to {destination}...")
                    rel_path = os.path.relpath(_root, source)
                    dest_folder = os.path.join(destination, rel_path)
                    os.makedirs(dest_folder, exist_ok=True)
                    root_file_path = os.path.join(_root, file_name)
                    dest_file_path = os.path.join(dest_folder, file_name)
                    shutil.copy2(root_file_path, dest_file_path)
    except PermissionError:
        print(f"Insufficient permissions to add folder to '{destination}'.\nPlease run file as admin...")
    finally:
        print_files_at_location(destination)
