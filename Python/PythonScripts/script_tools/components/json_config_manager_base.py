"""
JSONConfigManager
-----------------

A utility class designed to manage configurations stored in a JSON format. It provides
methods to read, write, set, and get values both at the root and nested levels of the JSON
structure. The class also includes features for displaying the content in a user-friendly format
with styling, and also reports the last modification date of the file.

Author: Zac Peterson
Date: 2023/09/19
"""
import json
from typing import Any
from pathlib import Path
from datetime import datetime
from script_tools.handlers.terminal_handler import TerminalHandler


class JSONConfigManager:
    """
    A manager for handling configurations in a JSON file.

    Attributes:
        file_path (Path): The path to the JSON file.
        verbose (bool): Flag for logging verbosity.

    Methods:
        read_config: Reads the content of the JSON configuration file.
        write_config: Writes a dictionary to the JSON file.
        get: Retrieves a value using its key, supports nested keys.
        set: Sets a value using its key, supports nested keys.
        set_all_nested: Sets all values, even in nested dictionaries, to a given value.
        set_single_nested: Sets a value for a key, supports updating single nested dictionaries.
    """
    def __init__(self, file_path: str | Path, verbose: bool = False):
        self.file_path = Path(file_path) if isinstance(file_path, str) else file_path
        if not self.file_path.exists():
            raise FileNotFoundError(f"JSON file not found: {self.file_path}")
        self._deep_update({"ENV_PATH": str(file_path)}, self.read_config())
        self.verbose = verbose

    def __repr__(self) -> str:
        formatted_items = []
        content = self.read_config()
        for k, v in content.items():
            if not isinstance(v, dict):
                formatted_items.append(f'\t{k}, {v}')
            else:
                formatted_items.append(f'\t{k}:')  # Showing key for nested dict
                for nested_k, nested_v in v.items():
                    formatted_items.append(f'\t\t{nested_k}, {nested_v}')
        representation = '{\n' + "\n".join(formatted_items) + "\n}"
        _last_modified_val = self.__get_last_modified_time(self.file_path)
        background = TerminalHandler(back='white')
        bold = TerminalHandler(style='bold')
        faint = TerminalHandler(fore='black', style='faint')
        underline = TerminalHandler(style='underline')
        header_txt = bold.wrap(f"\nConfigManager---{self.file_path} "
                               f"{underline.wrap(f'(Last Modified: {_last_modified_val})')}\n")
        header = TerminalHandler(fore='cyan').wrap(header_txt)
        body = faint.wrap(representation)
        return header + background.wrap(body)

    def log(self, message: str): print(message) if self.verbose else None

    def read_config(self) -> dict:
        """
        Reads the content of the JSON configuration file.

        Returns:
            dict: The content of the JSON file.

        Raises:
            JSONDecodeError: If there's an issue decoding the JSON file.
        """
        try:
            config_data = self.file_path.read_text()
            self.log(f"Successfully read JSON file: {self.file_path}")
            return json.loads(config_data)
        except json.decoder.JSONDecodeError:
            self.log(f"Error decoding JSON file: {self.file_path}")
            raise

    def write_config(self, data: dict) -> None:
        """Writes a dictionary to the JSON file."""
        try:
            self.file_path.write_text(json.dumps(data, indent=4))
            self.log(f"Successfully wrote to JSON file: {self.file_path}")
        except Exception as e:
            self.log(f"Error writing to JSON file: {self.file_path}. Error: {str(e)}")
            raise

    def get(self, key: str) -> Any:
        """
        Retrieves a value using its key.

        Args:
            key (str): The key to search for, supports dot notation for nested keys.

        Returns:
            Any: The value associated with the key. None if the key is not found.
        """
        keys = key.split('.')
        config_data = self.read_config()
        for k in keys:
            config_data = config_data.get(k)
            if config_data is None:
                return None
        return config_data

    def set(self, key: str, value: Any):
        """
        Sets a value using its key.

        Args:
            key (str): The key to set the value for, supports dot notation for nested keys.
            value (Any): The value to set.
        """
        keys = key.split('.')
        config_data = self.read_config()
        temp = config_data
        for k in keys[:-1]:
            temp = temp.setdefault(k, {})
        temp[keys[-1]] = value
        self.write_config(config_data)

    def set_all_nested(self, value: Any) -> int:
        """
        Sets all values, even in nested dictionaries, to a given value.

        Args:
            value (Any): The value to set.

        Returns:
            int: The number of values that were set.
        """

        def recursive_set_all(_target_dict, universal_value):
            count = 0
            # Iterate over key-value pairs in the dictionary
            for k, v in _target_dict.items():
                if isinstance(v, dict):
                    # If value is a dictionary, recursively call this function
                    count += recursive_set_all(v, universal_value)
                else:
                    # Otherwise, set the value to the specified `value`
                    _target_dict[k] = universal_value
                    count += 1
            return count

        config_data = self.read_config()
        updated_entries_count = recursive_set_all(config_data, value)
        self.write_config(config_data)
        return updated_entries_count

    def _deep_update(self, original, update):
        """
        Recursively updates the original dictionary with values from the update dictionary.

        Args:
            original (dict): The original dictionary.
            update (dict): The update dictionary with values to be merged into the original.

        Returns:
            dict: The updated dictionary.
        """
        for key, value in update.items():
            if isinstance(value, dict):
                # Recursively merge nested dictionaries
                original[key] = self._deep_update(original.get(key, {}), value)
            else:
                original[key] = value
        return original

    def set_single_nested(self, key: str, value: Any):
        """
        Sets a value for a single nested key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set.
        """
        config_data = self.read_config()
        if key in config_data and isinstance(value, dict):
            config_data[key] = self._deep_update(config_data[key], value)
        else:
            config_data[key] = value
        self.write_config(config_data)

    @staticmethod
    def __get_last_modified_time(file_path):
        """
        Gets the last modification time of the file.

        Args:
            file_path (Path): The file path.

        Returns:
            str: The formatted timestamp of the last modification.
        """
        timestamp = file_path.stat().st_mtime
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
