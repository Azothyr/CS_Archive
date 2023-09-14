import json
from utils.file_ops.file_search_ops import path_exists as exists
from utils.file_ops.file_basic_ops import write_to_file as write
from utils.file_ops.file_basic_ops import read_file as load
from utils.file_ops.file_search_ops import get_last_modified_time as last_modified


class JsonManagerBase:
    def __init__(self, json_path=None):
        """Initialize JsonManager with a default or provided path to the JSON file."""
        if not exists(json_path):
            raise FileNotFoundError(f"JSON file not found: {json_path}")
        self.json_path = json_path
        self.json = self.load_json()
        self.json_last_modified = last_modified(self.json_path)
    """
    def __repr__(self):
        module_opts = '{\n' + "\n".join([f'\t{k}, {v}' for k, v in self.json['module_debug'].items()]) + "\n}"
        _last_modified_val = self.json_last_modified
        return (f"\njsonManager---{self.json_path} (Last Modified: {_last_modified_val})"
                f"\n'global_debug': {self.json['global_debug']}"
                f"\n'module_debug'= {module_opts}")
    """

    def load_json(self):
        """Load and return the json data from the file."""
        load(self.json_path)

    def save_json(self):
        """Save the current json data to the file."""
        write(self.json_path, self.json, file_type=".json")

    def update_json(self, global_debug=None, module_name=None, module_debug_value=None):
        """
        Update debug configurations based on the provided parameters.

        If global_debug is specified, updates the global debug setting.
        If module_name and module_debug_value are specified, updates the debug setting for that module.
        """
        if global_debug is not None:
            self.json['global_debug'] = global_debug

        if module_name and module_debug_value is not None:
            if 'module_debug' not in self.json:
                self.json['module_debug'] = {}
            self.json['module_debug'][module_name] = module_debug_value

        self.save_json()

    # sorted_rules = sorted(self.rules.items(), key=lambda x: x[1]['priority'], reverse=True)
