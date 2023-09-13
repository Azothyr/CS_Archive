import os
import csv
import json
import importlib


def get_debugger():
    debug_handler = importlib.import_module('handlers.debug_handler')
    return debug_handler.DebugHandler(__name__)


def _debug_info():
    console_spacer = '>' * 5
    return {
        "write_to_file-0":
            "Start of file_basic_ops.py\ndestination:\n>>>>>{}\ncontent:\n>>>>>{}"
            "\nfile_type:\n>>>>>{}\nargs:\n>>>>>{!r}\nkwargs:\n>>>>>{!r}",
        "write_to_file-1": "No file_type provided, using file extension: {}",
    }


def write_to_file(destination, content, file_type=None, *args, **kwargs):
    debugger = get_debugger()
    debugger.print('write_to_file-0', destination, content, file_type, args, kwargs)

    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()
        debugger.print('write_to_file-1', file_type, upper=True)
    exit()
    if file_type == ".json":
        with open(destination, 'w') as file:
            json.dump(content, file)
    elif file_type == ".csv":
        with open(destination, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(content)
    else:  # Default to treating it as a plain text file.
        with open(destination, 'w') as file:
            file.write(content)
    completion_txt = args
    overwrite = kwargs.get('overwrite', False)
    debug = kwargs.get('debug', False)
    try:
        with open(destination, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        if kwargs.get('create_dir', False):
            if debug:
                print(f"Creating directory for '{destination}'")
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            write_to_file(destination, content, completion_txt)
        else:
            raise FileNotFoundError(f"Could not find '{destination}'")
    else:
        if completion_txt:
            print(completion_txt)
        else:
            if debug:
                print(f"Successfully wrote to {destination}")


def append_to_file(destination, content, file_type=None, **kwargs):
    """
    debugger = get_debugger()

    file_ops = importlib.import_module('file_ops')
    result = file_ops.write_to_file(destination, content, file_type)
    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()

    if file_type == ".json":
        # Appending to JSON is tricky as JSON doesn't support appending like text.
        # You would typically read the JSON, modify the data, then write it back.
        data = read_file(destination, file_type=".json")
        data.update(content)
        write_to_file(destination, data, file_type=".json")
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
    result = file_ops.write_to_file(destination, content, file_type)
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
