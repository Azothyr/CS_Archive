import os
from config.path_library_handler import PathLib
from handlers.debug_handler import get_or_initialize_debugger


def _debug_info():
    return {
        "": "",
    }


def get_top_down_filedir(path, **kwargs) -> list:
    """
    Prints all the files located at the specified path and its subdirectories.
        Args:
        - path (str): The path to inspect.
    """
    debugger = debugger.get_or_initialize_debugger()
    result = []
    for root, dirs, files in os.walk(path, topdown=False):
        path_to_files = os.path.join(root)
        seperator = '|' + ('-' * (len(path_to_files)-2)) + '>'
        result.append(path_to_files)
        for name in files:
            result.append(seperator + os.path.join(name))
    return result


def clear_directory(path) -> None:
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


def get_file_path_from_lib(**kwargs) -> str or tuple:
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
    library = kwargs.get('library', PathLib())

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
