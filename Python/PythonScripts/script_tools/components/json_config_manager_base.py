# DO NOT IMPORT FROM SCRIPT TOOLS
import json
import os
from datetime import datetime
from script_tools.handlers.terminal_handler import TerminalHandler


class JsonConfigManagerBase:
    def __init__(self, json_path=None, cache_path=None):
        """Initialize JsonManager with a default or provided path to the JSON file."""
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"JSON file not found: {json_path}")
        self.json_path = json_path
        self.config_json = self.__load_json(self.json_path)
        self.cache_key = self.json_path.split('/')[-1].split('.')[0]
        self.cache_path = self.json_path.replace('.json', '_cache.json') if not cache_path else cache_path

        if not os.path.exists(self.cache_path):
            with open(self.cache_path, 'w') as cache_file:
                json.dump({self.cache_key: {}}, cache_file)
        self.cache = self.__load_json(self.cache_path)
        if self.get_value(self.cache_key, data=self.cache) is None:
            self.update_json(target_path=self.cache_path, update_dict={self.cache_key: self.config_json})

        self.cache = self.__load_json(self.cache_path, top_key=self.cache_key)

    def __repr__(self) -> str:
        formatted_items = []
        for k, v in self.config_json.items():
            if not isinstance(v, dict):
                formatted_items.append(f'\t{k}, {v}')
            else:
                formatted_items.append(f'\t{k}:')  # Showing key for nested dict
                for nested_k, nested_v in v.items():
                    formatted_items.append(f'\t\t{nested_k}, {nested_v}')
        representation = '{\n' + "\n".join(formatted_items) + "\n}"
        _last_modified_val = self.__get_last_modified_time(self.json_path)
        background = TerminalHandler(back='white')
        bold = TerminalHandler(style='bold')
        faint = TerminalHandler(fore='black', style='faint')
        underline = TerminalHandler(style='underline')
        header_txt = bold.wrap(f"\nConfigManager---{self.json_path} "
                               f"{underline.wrap(f'(Last Modified: {_last_modified_val})')}\n")
        header = TerminalHandler(fore='cyan').wrap(header_txt)
        body = faint.wrap(representation)
        return header + background.wrap(body)

    @staticmethod
    def __load_json(destination: str = None, top_key: str = None) -> dict:
        """Load and return the json data from the file."""
        try:
            with open(destination, 'r') as file:
                data = file.read()
                return json.loads(data)[top_key] if top_key else json.loads(data) if data else {}
        except json.decoder.JSONDecodeError:
            print(f"Error decoding JSON file: {destination}")
            return {}  # Return an empty dictionary if there's a decoding error

    def load_json(self) -> dict:
        """Load and return the json data from the file."""
        return self.__load_json(self.json_path)

    def save_json(self, destination: str = None, content: dict = None):
        """Save the current json data to the file."""
        if destination is None:
            destination = self.json_path
        if content is None:
            content = self.config_json

        # First save to _settings
        with open(self.cache_path, 'w') as cache_file:
            json.dump({self.cache_key: content}, cache_file, indent=4)

        # Then save to the actual destination
        with open(destination, 'w') as file:
            json.dump(content, file, indent=4)

        # Reload internal json data
        self.config_json = self.__load_json(self.json_path)
        self.cache = self.__load_json(self.cache_path)

    def compare_with_config(self, external_dict: dict) -> bool:
        """
        Compare the provided dictionary with the dictionary in the JSON file.

        :param external_dict: Dictionary to compare.
        :return: True if the dictionaries are the same, False otherwise.
        """
        # Load current JSON content
        current_dict = self.load_json()

        # Compare the dictionaries
        return current_dict == external_dict

    def has_changed(self) -> bool:
        """
        Check if the current JSON data is different from the cache.
        Returns True if there's a difference, False otherwise.
        """
        try:
            cached_content = self.cache.get(self.cache_key, {})
            return cached_content != self.config_json
        except AttributeError:
            self.save_json(destination=self.cache_path, content={self.cache_key: {}})
            return True

    def update_json(self, target_dict=None, update_dict=None, target_path=None, **kwargs):
        def load_json_from_path(path):
            with open(path, 'r') as file:
                return json.load(file)

        def save_json_to_path(path, data):
            with open(path, 'w') as file:
                json.dump(data, file, indent=4)

        def recursive_set_all(_target_dict, value):
            """
            Recursively set all values in `target_dict` to `value`.
            """
            for k, v in _target_dict.items():
                if isinstance(v, dict):
                    recursive_set_all(v, value)
                else:
                    _target_dict[k] = value

        def recursive_update(_target_dict, _update_dict):
            """
            Recursively update `target_dict` with values from `update_dict`.
            """
            for k, v in _update_dict.items():
                if isinstance(v, dict) and k in _target_dict and isinstance(_target_dict[k], dict):
                    recursive_update(target_dict[k], v)
                else:
                    _target_dict[k] = v

        # If main_allowed (kwargs passed from __main__ mod) is True, allow updating the main level of the json
        if kwargs.get('main_allowed', False) and "_all" in kwargs:
            recursive_set_all(self.config_json[kwargs.get('top_key')] if 'top_key' in kwargs.keys() else
                              self.config_json, kwargs["_all"])
            self.save_json(destination=self.json_path, content=self.config_json)
        else:

            # If a target_path is provided, load that JSON file
            # If no target_dict is given (or loaded), default to self.config_json
            if target_path:
                try:
                    target_dict = load_json_from_path(target_path)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {target_path}: {e}")
                    target_dict = {}
                    print(f'2:{target_dict}')
            if not target_dict:
                try:
                    save_json_to_path(target_path, {})
                    target_dict = load_json_from_path(target_path)
                except json.JSONDecodeError as e:
                    raise e

            # Now, you're sure target_dict is a dictionary
            recursive_update(target_dict, update_dict or {})

            # Save the updated dictionary back to the file
            save_json_to_path(target_path, target_dict) if target_path and target_dict else None

    def set_value(self, hierarchical_key, value, delimiter='.'):
        """
        Set a value in the json data using a hierarchical key.

        :param hierarchical_key: String key in format "level1.level2.level3"
        :param value: The value to set
        :param delimiter: The delimiter between levels. Default is '.'.

        example:
        config = JsonConfigManagerBase(json_path="path_to_json")
        config.set_value("top_level", "new_value")  # Setting a top-level value
        config.set_value("level1.level2", "new_value")  # Setting a nested value
        config.set_value("level1.level2.level3", "new_value")  # Deeper nesting
        """
        keys = hierarchical_key.split(delimiter)
        data = self.config_json

        for key in keys[:-1]:  # All keys except the last one
            if key not in data or not isinstance(data[key], dict):
                data[key] = {}
            data = data[key]

        data[keys[-1]] = value
        if self.has_changed():
            self.save_json(destination=self.json_path, content=self.config_json)

    def get_value(self, hierarchical_key, data=None, default=None, delimiter='.'):
        """
        Get a value from the json data using a hierarchical key.

        :param hierarchical_key: String key in format "level1.level2.level3"
        :param data: The data to search through. If None provided, the config_json will be used.
        :param default: The value to return if the hierarchical key does not exist.
        :param delimiter: The delimiter between levels. Default is '.'.

        example:
        config = JsonConfigManagerBase(json_path="path_to_json")
        val1 = config.get_value("top_level")  # Getting a top-level value
        val2 = config.get_value("level1.level2")  # Getting a nested value
        val3 = config.get_value("level1.level2.level3")  # Deeper nesting

        Args:
        """
        keys = hierarchical_key.split(delimiter)
        data = self.config_json if data is None else data

        for key in keys:
            if key in data:
                data = data[key]
            else:
                return default  # Key does not exist, return default value

        return data

    @staticmethod
    def __get_last_modified_time(file_path):
        """Return the last modified time of the configuration file."""
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
