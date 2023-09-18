"""
config_handler: Configuration Management for Debugging and Settings

This module provides the ConfigManager class, a utility to manage configurations loaded
from a JSON file. The primary focus of this configuration manager is to manage debug _settings,
both at a global level and at the module-specific level.

Key Features:
- Load and save configurations from and to a specified JSON file.
- Manage global debug _settings.
- Manage module-specific debug _settings.

Classes:
- ConfigManager: Manages configurations loaded from a JSON file, especially debug _settings.

Example:
    config_manager = ConfigManager(config_path="my_config.json")
    global_debug_status = config_manager.get_global_debug()
    specific_module_debug_status = config_manager.get_module_debug("some_module_name")

Note:
    The default configuration file is `_debug_config.json`, but this can be changed by
    providing a different path during initialization.
"""
# DO NOT IMPORT FROM SCRIPT TOOLS
from components.json_config_manager_base import JsonConfigManagerBase


class DebugConfigManager(JsonConfigManagerBase):
    """
    ConfigManager manages configurations loaded from a JSON file.

    It's primary role is to manage debug _settings, including global debug _settings and
    module-specific debug _settings. These configurations can be loaded from, and saved to, a JSON file.

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

    def __init__(self, config_path='script_tools/config/_settings/_debug_config.json', **kwargs):
        """Initialize ConfigManager with a default or provided path to the config JSON file."""
        super().__init__(json_path=config_path, cache_path='script_tools/config/_settings/_configs_cache.json')

    def turn_all_debug_on(self) -> None:
        super().set_value('config_globals-global_debug', True, delimiter='-')
        super().update_json(top_key='module_debug_values', main_allowed=True, _all=True)

    def turn_all_debug_off(self, **kwargs) -> None:
        super().set_value('config_globals-global_debug', False, delimiter='-')
        super().update_json(top_key='module_debug_values', main_allowed=True, _all=False)

    def get_global_debug_value(self) -> bool:
        return super().get_value(hierarchical_key='config_globals-global_debug', delimiter='-', default=False)

    def get_traceback_value(self) -> bool:
        return super().get_value(hierarchical_key='config_globals-traceback_debug', delimiter='-', default=False)

    def get_module_debug_value(self, module_name) -> bool:
        return super().get_value(hierarchical_key=f'module_debug_values-{module_name}', delimiter='-', default=False)
