# DO NOT IMPORT FROM SCRIPT TOOLS
import json
from pathlib import Path
from datetime import datetime
from script_tools.handlers.terminal_handler import TerminalHandler
from script_tools.config.env_handler import EnvHandler

import json
from typing import Any


class JSONConfigManager:
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path) if isinstance(file_path, str) else file_path
        if not self.file_path.exists():
            raise FileNotFoundError(f"JSON file not found: {self.file_path}")

    def read_config(self) -> dict:
        config_data = self.file_path.read_text()
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write_config(self, data: dict):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def save_json(self, destination: Path = None, content: dict = None):
        destination = destination or self.json_path
        content = content or self.config_json

        destination.write_text(json.dumps(content, indent=4))

        # Reload internal json data
        self.config_json = self.load_json()
        self.cache = self.__load_json(self.cache_path) if self.cache_path is not None else None

    def create_directory_or_file(path: str) -> None:
        """Helper function to create a directory or a JSON file."""
        path_obj = Path(path)

        # Check if the provided path has a .json extension, suggesting it's a file
        if path_obj.suffix == '.json':
            path_obj.parent.mkdir(parents=True, exist_ok=True)
            path_obj.touch(exist_ok=True)
            print(f"Successfully created {path}")
            return

    def get(self, key: str) -> Any:
        config_data = self.read_config()
        return config_data.get(key)

    def set(self, key: str, value: Any):
        config_data = self.read_config()
        config_data[key] = value
        self.write_config(config_data)

    def deep_update(self, original, update):
        for key, value in update.items():
            if isinstance(value, dict):
                original[key] = self.deep_update(original.get(key, {}), value)
            else:
                original[key] = value
        return original

    def set_nested_value(self, key: str, value: Any):
        config_data = self.read_config()
        if key in config_data and isinstance(value, dict):
            config_data[key] = self.deep_update(config_data[key], value)
        else:
            config_data[key] = value
        self.write_config(config_data)


class FunctionalityBase:
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
    def __load_json(destination: Path = None, top_key: str = None) -> dict:
        try:
            data = destination.read_text()
            json_data = json.loads(data)
            return json_data[top_key] if top_key else json_data
        except json.decoder.JSONDecodeError:
            print(f"Error decoding JSON file: {destination}")
            return {}

    def load_json(self, **kwargs) -> dict:
        return self.__load_json(self.json_path, top_key=kwargs.get('top_key', None))

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
        if not self.cache_path:
            return False
        try:
            cached_content = self.cache.get(self.cache_key, {})
            return cached_content != self.config_json
        except AttributeError:
            self.save_json(destination=self.cache_path, content={self.cache_key: {}})
            return True

    def update_json(self, target_path=None, target_dict=None, **kwargs):
        """
            Update the internal JSON configuration with new values.

            This method allows for a deep merge of nested dictionaries, ensuring
            that nested keys in the target dictionary are updated individually
            rather than overwritten entirely.

            Parameters:
            - target_path (str or pathlib.Path, optional): Path to the JSON file that should be loaded and updated.
                                                          If not provided, the default internal configuration is used.
            - target_dict (dict, optional): A dictionary to be updated. This will be the primary dictionary
                                            if provided, otherwise the dictionary loaded from target_path or the
                                            internal configuration will be used.
            - **kwargs:
                - update_dict (dict, optional): Dictionary containing the keys and values to be updated in the target.
                - main_allowed (bool, optional): Flag to determine if the main level of the JSON can be updated.
                                                 Default is False.
                - _all (any type, optional): If provided and main_allowed is True, it will set all values in the
                                             target dictionary to the value of _all.
                - top_key (str, optional): If provided, it determines which top-level key in the internal
                                           configuration will be updated.

            Returns:
            None. The method updates the internal JSON in-place and also writes the changes to the JSON file.

            Raises:
            - json.JSONDecodeError: If there's an error decoding a JSON file.

            Example:
            ```
            obj.update_json(update_dict={'a': {'b': 2}}, main_allowed=True, _all=5)
            ```
            This will update the key 'b' inside nested dictionary 'a' to have value 2, and set all other values
            in the configuration to 5 if main_allowed is True.

            Notes:
            - The method prioritizes target_dict over target_path. If both are provided, the dictionary from
              target_path will be loaded but then immediately overwritten by target_dict.
            """

        def recursive_set_all(_target_dict, value):
            """
            Recursively set all values in `target_dict` to `value`.
            """
            # Iterate over key-value pairs in the dictionary
            for k, v in _target_dict.items():
                if isinstance(v, dict):
                    # If value is a dictionary, recursively call this function
                    recursive_set_all(v, value)
                else:
                    # Otherwise, set the value to the specified `value`
                    _target_dict[k] = value

        def recursive_update(_target_dict, _update_dict):
            """
            Recursively update `target_dict` with values from `update_dict`.
            """
            # Iterate over key-value pairs in the update dictionary
            for k, v in _update_dict.items():
                # If current key maps to a dictionary in both target and update dictionaries
                if isinstance(v, dict) and k in _target_dict and isinstance(_target_dict[k], dict):
                    # Recursively update that dictionary
                    recursive_update(_target_dict[k], v)
                else:
                    # Otherwise, directly update the value in the target dictionary
                    _target_dict[k] = v

        # Check if updating all main level values of JSON is allowed
        if kwargs.get('main_allowed', False) and "_all" in kwargs:
            # Determine which dictionary to update, considering the optional top_key
            target = self.config_json[kwargs.get('top_key')] if 'top_key' in kwargs else self.config_json
            recursive_set_all(target, kwargs["_all"])

            # Save the updated dictionary back to its source file
            self.save_json(destination=self.json_path, content=self.config_json)
            return

        # If a target_path is provided, try to load its content
        if target_path:
            target_path = Path(target_path)
            if target_path.exists():
                try:
                    # Attempt to load JSON from the specified path
                    with target_path.open() as f:
                        target_dict = json.load(f)
                except json.JSONDecodeError as e:
                    # Handle potential decoding errors and set target_dict to an empty dictionary
                    print(f"Error decoding JSON from file {target_path}: {e}")
                    target_dict = {}
            else:
                # If the file does not exist, notify and initialize an empty dictionary
                print(f"File {target_path} does not exist, initializing as empty dictionary.")
                target_dict = {}

        # If target_dict is not provided or determined yet, default to internal configuration
        if target_dict is None:
            target_dict = self.config_json

        # If an 'update_dict' is provided, recursively update target_dict with its values
        if 'update_dict' in kwargs:
            recursive_update(target_dict, kwargs['update_dict'])

        # Save the potentially updated dictionary back to its source file
        self.save_json(destination=self.json_path, content=self.config_json)

    def set_value(self, hierarchical_key, value, delimiter='.', **kwargs):
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
        if self.has_changed() or kwargs.get('force_save', False):
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
        timestamp = file_path.stat().st_mtime
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


class JsonConfigManager(FunctionalityBase):

    def __init__(self, json_path=None, env_var_name=None, default_path=None, cache_path=None, **kwargs):
        """
        Enhanced Initialization with EnvHandler

        :param env_var_name: Environment variable name to fetch the path.
        :param default_path: Default path to be used if the environment variable is not set.
        """
        super().__init__(json_path=json_path, cache_path=cache_path, **kwargs)

        if env_var_name:
            self.env_handler = EnvHandler(env_var_name, default_path)

            # Check and synchronize between env variable and json config
            self.sync_env_with_config()

    def sync_env_with_config(self):
        """Ensure that the env path is synchronized with the json config path."""
        if hasattr(self, 'env_handler'):
            env_path = self.env_handler.get_env_path()
            config_path = self.get_value("path")

            if env_path != config_path:
                self.set_value("path", env_path)

    def get_path(self):
        """Get the path from the config."""
        return self.get_value("path")

    def set_path(self, new_path):
        """Set a new path in the configuration and environment variable."""
        self.set_value("path", new_path)
        if hasattr(self, 'env_handler'):
            self.env_handler.environment.get()
