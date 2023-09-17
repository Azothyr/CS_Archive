import os
import csv
import json
from script_tools.handlers.debug_handler import get_debugger
__debugger = get_debugger(__name__)


def debug_info():
    return {
        "write-start": "Start of write to file",
        "write-0.1":
            "PASSED VALUES--\ndestination:\n>>>>>{}\ncontent:\n>>>>>{}"
            "\nfile_type:\n>>>>>{}\nargs:\n>>>>>{!r}\nkwargs:\n>>>>>{!r}",
        "write-1.1": "No file_type provided, using file extension-->{}",
        "write-end": "SUCCESS: Wrote content to: {}",
    }


def write_to_file(destination, content, file_type=None, *args, **kwargs):
    # write 0.(~): Start of method and getting passed values
    __debugger.print('write-0.0')
    __debugger.print('write-0.1', destination, content, file_type, args, kwargs)
    try:
        # write 1.(~): Attempting to write to file
        if not file_type:
            file_type = os.path.splitext(destination)[1].lower()
            __debugger.print('write-1.1', file_type, upper=True)

        completion_txt = args
        overwrite = kwargs.get('overwrite', False)

        if file_type == ".json":
            with open(destination, 'w') as file:
                json.dump(content, file, indent=4)
        elif file_type == ".csv":
            with open(destination, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(content)
        else:  # Default to treating it as a plain text file.
            with open(destination, 'w') as file:
                file.write(content)
    except FileNotFoundError:
        __debugger.print('write-')
        if kwargs.get('create_dir', False):
            print(f"Creating directory for '{destination}'")
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            write_to_file(destination, content, file_type, *args, **kwargs)
        else:
            raise FileNotFoundError(f"Could not find '{destination}'")
    else:
        __debugger.print('write-end', destination)


def append_to_file(destination, content, file_type=None, **kwargs):
    """
    debugger = get_debugger()

    file_ops = importlib.import_module('file_ops')
    result = file_ops.write(destination, content, file_type)
    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()

    if file_type == ".json":
        # Appending to JSON is tricky as JSON doesn't support appending like text.
        # You would typically read the JSON, modify the data, then write it back.
        data = read_file(destination, file_type=".json")
        data.update(content)
        write(destination, data, file_type=".json")
    elif file_type == ".csv":
        with open(destination, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(content)
    else:
        with open(destination, 'a') as file:
            file.write(content)
    """
    with open(destination, 'a') as file:
        file.write(content)


def read_file(destination, file_type=None, **kwargs):
    """
    debugger = get_debugger()

    file_ops = importlib.import_module('file_ops')
    result = file_ops.write(destination, content, file_type)
    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()

    if file_type == ".json":
        with open(destination, 'r') as file:
            return json.load(file)
    elif file_type == ".csv":
        with open(destination, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    else:
        with open(destination, 'r') as file:
            return file.read()
    """
    try:
        with open(destination, 'r') as file:
            file.readlines()
    finally:
        print(f"Successfully read file: {destination}")
