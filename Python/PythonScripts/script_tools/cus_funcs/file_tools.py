import os
import shutil
try:
    from script_tools.info.file_path_library import PathLib
except ModuleNotFoundError:
    from info.file_path_library import PathLib


def check_for_path(path):
    """Checks if the given path exists"""
    if not os.path.exists(path):
        raise ValueError(f"'{path}' does not exist")


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
        seperator = '|' + ('-' * (len(path_to_files)-2)) + '>'
        print("\n", path_to_files)
        for name in files:
            print(seperator, os.path.join(name))
        print(end='\n')


def get_file_path_from_lib(**kwargs):
    """Returns the path to a Windows folder"""
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


def transfer_py_dir_in_current(source, destination, file_exceptions):
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
    """Returns all files and their path with the given ending in the given directory and subdirectories"""
    files = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.endswith(ending):
                files.append((name, os.path.join(root, name)))
    return files


def write_to_file(destination, text, *args, **kwargs):
    completion_txt = args
    overwrite = kwargs.get('overwrite', False)
    create_dir = kwargs.get('create_dir', False)
    try:
        with open(destination, 'w') as f:
            f.write(text)
    except FileNotFoundError:
        if create_dir:
            print(f"Creating directory for '{destination}'")
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            write_to_file(destination, text, completion_txt)
        else:
            raise FileNotFoundError(f"Could not find '{destination}'")
    else:
        if completion_txt:
            print(completion_txt)
        else:
            print(f"Successfully wrote to {destination}")


def append_to_file(destination, text, completion_txt=None):
    try:
        with open(destination, 'a') as f:
            f.write(text)
    finally:
        if completion_txt:
            print(completion_txt)
        else:
            print(f"Successfully appended to {destination}")


def read_from_file(destination, text, completion_txt=None):
    try:
        with open(destination, 'r') as f:
            f.read(text)
    finally:
        if completion_txt:
            print(completion_txt)
        else:
            print(f"Successfully appended to {destination}")
