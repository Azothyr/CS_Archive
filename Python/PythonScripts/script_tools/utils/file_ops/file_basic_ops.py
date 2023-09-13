import os
from handlers import debug_handler as debugger
import csv
import json


def write_to_file(destination, content, file_type=None, *args, **kwargs):
    """
    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()

    if file_type == ".json":
        with open(destination, 'w') as f:
            json.dump(content, f)
    elif file_type == ".csv":
        with open(destination, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(content)
    else:  # Default to treating it as a plain text file.
        with open(destination, 'w') as f:
            f.write(content)
    """
    completion_txt = args
    overwrite = kwargs.get('overwrite', False)
    debug = kwargs.get('debug', False)
    try:
        with open(destination, 'w') as f:
            f.write(content)
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
    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()

    if file_type == ".json":
        # Appending to JSON is tricky as JSON doesn't support appending like text.
        # You would typically read the JSON, modify the data, then write it back.
        data = read_file(destination, file_type=".json")
        data.update(content)
        write_to_file(destination, data, file_type=".json")
    elif file_type == ".csv":
        with open(destination, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(content)
    else:
        with open(destination, 'a') as f:
            f.write(content)
    """
    with open(destination, 'a') as f:
        f.write(content)


def read_file(destination, file_type=None, **kwargs):
    """
    if not file_type:
        file_type = os.path.splitext(destination)[1].lower()

    if file_type == ".json":
        with open(destination, 'r') as f:
            return json.load(f)
    elif file_type == ".csv":
        with open(destination, 'r') as f:
            reader = csv.reader(f)
            return list(reader)
    else:
        with open(destination, 'r') as f:
            return f.read()
    """
    try:
        with open(destination, 'r') as f:
            f.readlines()
    finally:
        print(f"Successfully read file: {destination}")
