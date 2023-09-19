"""
This module provides utility functions to interact with the file system.

The primary functionalities include:
- Checking if a given path exists.
- Clearing all content from a directory.
- Printing files at a specific location.
- Retrieving file paths from a library.
- Transferring .py files from one directory to another.
- Finding files with a specific ending.
- Writing, appending, and reading from files.
"""
import os
import shutil
try:
    from PythonScripts.script_tools.info.file_path_library import  PathLib
except ModuleNotFoundError:
    from script_tools.info.file_path_library import PathLib


def check_for_path(path):
    """
    Checks if the given path exists.
        Args:
        - path (str): The path to check.
        Raises:
        - ValueError: If the path does not exist.
    """
    if not os.path.exists(path):
        raise ValueError(f"'{path}' does not exist")


def clear_directory(path):
    """
    Remove all files and subdirectories from a directory.
        Args:
        - path (str): The directory path to clear.
    """
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def print_files_at_location(path):
    """
    Prints all the files located at the specified path and its subdirectories.
        Args:
        - path (str): The path to inspect.
    """
    for root, dirs, files in os.walk(path, topdown=False):
        path_to_files = os.path.join(root)
        seperator = '|' + ('-' * (len(path_to_files)-2)) + '>'
        print("\n", path_to_files)
        for name in files:
            print(seperator, os.path.join(name))
        print(end='\n')


def get_file_path_from_lib(**kwargs):
    """
    Returns the path to a Windows folder using a specified library.
        Args:
        - **kwargs: Arbitrary keyword arguments which may include 'runs', 'library', and 'debug'.
        Returns:
        - str or tuple: The desired path(s) as a string or tuple of strings.
        Raises:
        - OverflowError: If the function is stuck in a loop trying to retrieve the path.
    """
    runs = kwargs.get('runs', 0)

    if runs >= 1:
        raise OverflowError("Get file path from library stuck in loop")

    # Getting the library
    library = kwargs.get('library', PathLib(debug=kwargs.get('debug', False)))

    options = library.get_lib()
    values = []

    for key, value in kwargs.items():
        if value and key in options:  # Check if the value is True and the key exists in options
            values.append(options[key])

    if not values:
        library.refresh_lib()   # Assuming PathLib has a method refresh_lib() that refreshes the paths
        return get_file_path_from_lib(runs=runs + 1, library=library, **kwargs)
    elif len(values) > 1:
        return tuple(values)
    else:
        return values[0]


def transfer_py_dir_in_current(source, destination, file_exceptions):
    """
    Transfer .py files from a source directory to a destination directory,
    excluding specified exceptions.
        Args:
        - source (str): The source directory path.
        - destination (str): The destination directory path.
        - file_exceptions (list): A list of filenames to exclude.
    """
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


def write_to_file(destination, text, *args, **kwargs):
    """
    Writes specified text to a file. If the directory does not exist and 'create_dir' is True, the directory is created.
        Args:
        - destination (str): The destination file path where the text should be written.
        - text (str): The content to write to the file.
        - *args: Additional arguments, typically for completion text.
        - **kwargs: Arbitrary keyword arguments which may include 'overwrite', 'create_dir', and 'debug'.
        Raises:
        - FileNotFoundError: If the file is not found and 'create_dir' is False.
    """
    completion_txt = args
    overwrite = kwargs.get('overwrite', False)
    create_dir = kwargs.get('create_dir', False)
    debug = kwargs.get('debug', False)
    try:
        with open(destination, 'w') as f:
            f.write(text)
    except FileNotFoundError:
        if create_dir:
            if debug:
                print(f"Creating directory for '{destination}'")
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            write_to_file(destination, text, completion_txt)
        else:
            raise FileNotFoundError(f"Could not find '{destination}'")
    else:
        if completion_txt:
            print(completion_txt)
        else:
            if debug:
                print(f"Successfully wrote to {destination}")


def append_to_file(destination, text, completion_txt=None):
    """
    Appends specified text to a file.
        Args:
        - destination (str): The destination file path where the text should be appended.
        - text (str): The content to append to the file.
        - completion_txt (str, optional): Text to display upon successful operation. Default is a success message.
    """
    try:
        with open(destination, 'a') as f:
            f.write(text)
    finally:
        if completion_txt:
            print(completion_txt)
        else:
            print(f"Successfully appended to {destination}")


def read_from_file(destination):
    """
    Reads from a specified file and then reads the provided text.
        Args:
        - destination (str): The destination file path from which to read.
        - text (str): Text parameter (usage in context is unclear).
        - completion_txt (str, optional): Text to display upon successful operation. Default is a success message.
        Raises:
        - Any IO related exceptions which may occur during file operations.
    """
    try:
        with open(destination, 'r') as f:
            f.readlines()
    finally:
        print(f"Successfully appended to {destination}")
