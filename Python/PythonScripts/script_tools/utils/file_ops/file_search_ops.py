import os
import importlib
from datetime import datetime


def path_exists(file_path):
    """
    Checks if the given path exists.
        Args:
        - path (str): The path to check.
        Raises:
        - ValueError: If the path does not exist.
    """
    if not os.path.exists(file_path):
        print(f"'{file_path}' does not exist")
        return False
    return True


def get_files_with_ending(path, ending):
    """
    Retrieve all files with a specified ending in a directory and its subdirectories.
        Args:
        - path (str): The directory to search in.
        - ending (str): The file ending to search for.
        Returns:
        - list: A list of tuples where each tuple consists of the filename and its full path.
    """
    files = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.endswith(ending):
                files.append((name, os.path.join(root, name)))
    return files


def get_last_modified_time(file_path):
    """Return the last modified time of the configuration file."""
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
