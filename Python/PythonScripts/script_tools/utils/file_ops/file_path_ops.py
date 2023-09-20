import os
from script_tools.config.path_library_manager import PathManager as path_library
from script_tools.handlers import map_handler
from script_tools.handlers.debug_handler import get_debugger as get_debugger
__debugger = get_debugger(__name__)


def debug_info():
    return {
        "get dirs-start": "Start of get_childern_of_filedir method",
        "get dirs-end": "SUCCESS: Returning list of files and subdirectories under",

        "clear-start": "Start of clear_directory method",
        "clear-1.0": "WARNING: Clearing: {}",
        "clear-1.1": "Removing file: {}",
        "clear-1.2": "Removing directory: {}",
        "clear-end": "SUCCESS: Cleared directory and sub directories under: {}",

        "path from lib-start": "Start of get_file_path_from_lib method",
        "path from lib-1.1": "RUN #{}",
        "path from lib_except-1.1": "ERROR: get_file_path_from_lib stuck in loop",
        "path from lib-2.1": "Library: {}",
        "path from lib-2_error": "The Library provided is not a dictionary ---> {}",
        "path from lib-2.2": "Values: {}",
        "path from lib-3.1": "Checking if values are found in library, adding them if not.",
        "path from lib-end1": "Multiple values found, returning tuple",
        "path from lib-end2": "Single value found, returning string",
    }


def get_children_of_filedir(path, **kwargs) -> list:
    """
    Prints all the files located at the specified path and its subdirectories.
        Args:
        - path (str): The path to inspect.
    """
    __debugger.print('get dirs-start')
    # get dirs-1.(~): Checking if the function is stuck in a loop
    result = []
    for root, dirs, files in os.walk(path, topdown=False):
        path_to_files = os.path.join(root)
        seperator = '|' + ('-' * (len(path_to_files)-5)) + '>'
        result.append(path_to_files)
        for name in files:
            result.append(seperator + os.path.join(name))
    __debugger.print('get dirs-end')
    return result


def clear_directory(path) -> None:
    """
    Remove all files and subdirectories from a directory.
        Args:
        - path (str): The directory path to clear.
    """
    __debugger.print('clear-start')
    __debugger.print('clear-1.0')
    # clear-1.(~): Walking through the directory and removing all files and subdirectories
    print('clear dir-----here')
    for root, dirs, files in os.walk(path, topdown=False):
        print(root, dirs, files)
        for name in files:
            print(name)
            __debugger.print('clear-1.1', os.path.join(root, name))
            os.remove(os.path.join(root, name))
        for name in dirs:
            __debugger.print('clear-1.2', os.path.join(root, name))
            os.rmdir(os.path.join(root, name))
    __debugger.print('clear-end', path)


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
    __debugger.print('path from lib-start')
    # path from lib-1.(~): Checking if the function is stuck in a loop
    runs = kwargs.get('runs', 0)
    if runs >= 1:
        raise OverflowError(repr(__debugger.print('path from lib_except-1.1')))
    __debugger.print('path from lib-1.1', runs)

    # path from lib-2.(~): Getting the library and the values to check against
    library = kwargs.get('library', path_library())

    options = library.get_library()
    changed = library.has_changed()
    __debugger.print('path from lib-1.2', changed)
    values = []
    __debugger.print('path from lib-2.1', options)
    if not changed:
        for key, value in kwargs.items():
            if not isinstance(options, dict):
                __debugger.print('path from lib-2_error', options)
                break
            if value and key in options:  # Check if the value is True and the key exists in options
                values.append(options[key])
        __debugger.print('path from lib-2.2', values)

    # path from lib-3.(~): Checking if the values are valid
    if changed or not values:
        __debugger.print('path from lib-3.1')
        map_handler.update_path_map()
        return get_file_path_from_lib(runs=runs + 1, library=library, **kwargs)
    elif len(values) > 1:
        __debugger.print('path from lib-end1')
        return tuple(values)
    else:
        __debugger.print('path from lib-end2')
        return values[0]
