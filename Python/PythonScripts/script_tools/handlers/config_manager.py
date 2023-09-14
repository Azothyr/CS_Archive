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
from handlers.terminal_handler import TerminalHandler
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

    def __init__(self, config_path='script_tools/config.json'):
        """Initialize ConfigManager with a default or provided path to the config JSON file."""
        self.config_path = config_path
        self.config = self.load_config()
        self.config_last_modified = last_modified(self.config_path)

    def __repr__(self) -> str:
        global_opts = '{\n' + "\n".join([f'\t{k}, {v}' for k, v in self.config['config_globals'].items()]) + "\n}"
        module_opts = '{\n' + "\n".join([f'\t{k}, {v}' for k, v in self.config['module_debug'].items()]) + "\n}"
        _last_modified_val = self.config_last_modified
        background = TerminalHandler(back='white')
        bold = TerminalHandler(style='bold')
        faint = TerminalHandler(fore='black', style='faint')
        underline = TerminalHandler(style='underline')
        header_txt = bold.wrap(f"\nConfigManager---{self.config_path} "
                               f"{underline.wrap(f'(Last Modified: {_last_modified_val})')}\n")
        header = TerminalHandler(fore='cyan').wrap(header_txt)
        body = faint.wrap(f"config_globals: {global_opts}\n'module_debug'= {module_opts}\n")
        return header + background.wrap(body)

    def load_config(self) -> dict:
        """Load and return the configuration data from the file."""
        with open(self.config_path, 'r') as file:
            return json.load(file)

    def save_config(self) -> None:
        """Save the current configuration data to the file."""
        with open(self.config_path, 'w') as file:
            json.dump(self.config, file, indent=4)
        self.config = self.load_config()

    def set_config_globals(self, global_debug: bool = None, traceback: bool = None, **kwargs) -> None:
        """
        Update global debug configurations based on the provided parameters.

        If global_debug is specified, updates the global debug setting.
        If traceback is specified, updates the traceback setting.
        """
        # Set the global debug value if provided
        if global_debug is not None:
            self.config['config_globals']['global_debug'] = global_debug

        # Set the traceback value if provided
        if traceback is not None:
            self.config['config_globals']['traceback_debug'] = traceback

        # Update config json file
        self.save_config()

    def set_debug_config(self, global_debug: bool = None, module_name: str = None,
                         module_debug_value: bool = None, **kwargs) -> None:
        """
        Update debug configurations based on the provided parameters.

        If Turn_all_on is specified, sets all modules to True.
        If Turn_all_off is specified, sets all modules to False.

        If global_debug is specified, updates the global debug setting.
        If module_name and module_debug_value are specified, updates the debug setting for that module.
        """
        # If all_modules is provided, set all modules to the provided value
        if kwargs.get('all_modules', None) is not None:
            global_debug = kwargs['all_modules']
            self.config['module_debug'] = {k: global_debug for k in self.config['module_debug']}
            self.config['config_globals']['global_debug'] = global_debug
            self.save_config()
            return

        # Set the global debug value if provided
        self.set_config_globals(global_debug)

        # If module name and debug value are not provided set that modules value in the config
        if module_name and module_debug_value is not None:
            # If module provided is not in the config, add it
            if 'module_debug' not in self.config:
                self.config['module_debug'] = {}
            self.config['module_debug'][module_name] = module_debug_value

        # Update config json file
        self.save_config()

    def turn_all_debug_on(self) -> None: self.set_debug_config(True, all_modules=True)

    def turn_all_debug_off(self) -> None: self.set_debug_config(False, all_modules=False)

    def get_global_debug(self) -> bool: return self.config.get('config_globals', {}).get('global_debug', False)

    def get_traceback(self) -> bool: return self.config.get('config_globals', {}).get('traceback_debug', False)

    def get_module_debug(self, module_name) -> bool: return self.config.get('module_debug', {}).get(module_name, False)

