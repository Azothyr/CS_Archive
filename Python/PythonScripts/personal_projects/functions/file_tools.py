import os


def clear_directory(path):
    """Remove all files and subdirectories from a directory."""
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def print_files_at_location(path):
    """Returns all the files located at file path and it's subdirectories"""
    for root, dirs, files in os.walk(path, topdown=False):
        path_to_files = os.path.join(root)
        dashes = '-' * len(path_to_files)
        print(path_to_files)
        for name in files:
            print(dashes, os.path.join(name))
