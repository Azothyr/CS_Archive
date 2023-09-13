"""
config_handler: Configuration Management for Debugging and Settings

This module provides the ConfigManager class, a utility to manage configurations loaded
from a JSON file. The primary focus of this configuration manager is to manage debug settings,
both at a global level and at the module-specific level.

Key Features:
- Load and save configurations from and to a specified JSON file.
- Manage global debug settings.
- Manage module-specific debug settings.

Classes:
- ConfigManager: Manages configurations loaded from a JSON file, especially debug settings.

Example:
    config_manager = ConfigManager(config_path="my_config.json")
    global_debug_status = config_manager.get_global_debug()
    specific_module_debug_status = config_manager.get_module_debug("some_module_name")

Note:
    The default configuration file is `config.json`, but this can be changed by
    providing a different path during initialization.
"""
import json
from utils.file_ops.file_basic_ops import write_to_file as write
from utils.file_ops.file_search_ops import get_last_modified_time as last_modified


class ConfigManager:
    """
    ConfigManager manages configurations loaded from a JSON file.

    It's primary role is to manage debug settings, including global debug settings and
    module-specific debug settings. These configurations can be loaded from, and saved to, a JSON file.

    Attributes:
    - config_path (str): Path to the configuration JSON file.
    - config (dict): The loaded configuration data.

    Methods:
    - load_config(): Loads the configuration from the file.
    - save_config(): Saves the configuration to the file.
    - update_debug_config(global_debug, module_name, module_debug_value): Updates the debug configurations.
    - get_global_debug(): Returns the global debug status.
    - get_module_debug(module_name): Returns the debug status for a specific module.
    """

    def __init__(self, config_path=None):
        """Initialize ConfigManager with a default or provided path to the config JSON file."""
        self.config_path = config_path
        self.config = self.load_config()
        self.config_last_modified = last_modified(self.config_path)

    def __repr__(self):
        module_opts = '{\n' + "\n".join([f'\t{k}, {v}' for k, v in self.config['module_debug'].items()]) + "\n}"
        _last_modified_val = self.config_last_modified
        return (f"\nConfigManager---{self.config_path} (Last Modified: {_last_modified_val})"
                f"\n'global_debug': {self.config['global_debug']}"
                f"\n'module_debug'= {module_opts}")

    def load_config(self):
        """Load and return the configuration data from the file."""
        with open(self.config_path, 'r') as file:
            return json.load(file)

    def save_config(self):
        """Save the current configuration data to the file."""
        with open(self.config_path, 'w') as file:
            json.dump(self.config, file, indent=4)
        self.config = self.load_config()

    def update_debug_config(self, global_debug=None, module_name=None, module_debug_value=None):
        """
        Update debug configurations based on the provided parameters.

        If global_debug is specified, updates the global debug setting.
        If module_name and module_debug_value are specified, updates the debug setting for that module.
        """
        if global_debug is not None:
            self.config['global_debug'] = global_debug

        if module_name and module_debug_value is not None:
            if 'module_debug' not in self.config:
                self.config['module_debug'] = {}
            self.config['module_debug'][module_name] = module_debug_value

        self.save_config()

    def __switch(self, switch=None, *args, **kwargs):
        if switch is not None:
            _all = kwargs.get('all_modules', False)
            self.config['global_debug'] = switch
            if args:
                try:
                    if _all:
                        for module_name in self.config['module_debug']:
                            self.config['module_debug'][module_name] = switch
                    elif len(args) > 1:
                        for arg in args:
                            if arg is not None and arg != '' and arg != 'null':
                                self.config['module_debug'][arg] = switch
                    else:
                        if args[0] is not None and args[0] != '' and args[0] != 'null':
                            self.config['module_debug'][args[0]] = switch
                except KeyError:
                    return f"Module {args} not found in config file"
            self.save_config()
            return f"Debug turned to {switch}"
        else:
            return "No switch provided"

    def turn_on_debug(self, module_names=None, all_modules=False):
        print(self.__switch(True, module_names, all_modules=all_modules))

    def turn_off_debug(self, module_names=None, all_modules=False):
        print(self.__switch(False, module_names, all_modules=all_modules))

    def get_global_debug(self):
        """Return the current global debug setting, defaulting to False if not set."""
        return self.config.get('global_debug', False)

    def get_module_debug(self, module_name):
        """
        Return the debug setting for a specific module.

        If not set, defaults to True.
        """
        return self.config.get('module_debug', {}).get(module_name, True)
