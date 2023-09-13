"""
Debugging and Command Handling Utilities

This module provides utilities for:
- Debugging: Using `DebugHandler` class to print debug messages.
- Command Line Argument Parsing: Using `CmdHandler` to handle and parse command line arguments.
"""
import sys
from handlers.config_manager import ConfigManager


class DebugHandler:
    """
    DebugHandler handles the display of debug messages for a given module.

    Attributes:
    - module_name (str): Name of the module.
    - config_manager (ConfigManager): A manager for configurations.
    - debug (bool): A flag determining whether to show debug messages.

    Methods:
    - print_debug(debug_key, *args): Print the debug message corresponding to the given key.

    REQUIRES _debug_info() function in module that returns a dictionary of debug keys and messages.
    """

    def __init__(self, module_name, config_manager=None):
        self.module_name = module_name
        self.config_manager = config_manager or ConfigManager()
        self.debug = self._get_debug_status()

    def __repr__(self):
        return f"DebugHandler({self.module_name}, {self.config_manager})"

    def print(self, debug_key, wrap=None, start=None, end=None, replace=None,
              upper=False, lower=False, capitalize=False, *args):
        """Print the debug message for the provided key if debugging is enabled."""
        if not self.debug:
            return

        debug_messages = self._get_debug_messages()
        message = debug_messages.get(debug_key, f"Debug key '{debug_key}' not found!")
        formatted_message = message.format(*args)
        if start:
            formatted_message = start + formatted_message
        if end:
            formatted_message = formatted_message + end
        if upper:
            formatted_message = formatted_message.upper()
        if lower:
            formatted_message = formatted_message.lower()
        if capitalize:
            formatted_message = formatted_message.capitalize()
        if wrap:
            formatted_message = f"{wrap} {formatted_message} {wrap}"
        if replace:
            formatted_message = replace.format(formatted_message)
        print(formatted_message)

    def _get_debug_messages(self):
        """Retrieve debug messages from the module's _debug_info function."""
        _module = sys.modules[self.module_name]
        if not hasattr(_module, '_debug_info'):
            raise NotImplementedError(f"Module {self.module_name} requires _debug_info function for debugging.")
        return _module._debug_info()

    def _get_debug_status(self):
        """Check if debugging is globally enabled and if the current module should display debug messages."""
        global_debug = self.config_manager.get_global_debug()
        if not global_debug:
            return False
        return self.config_manager.get_module_debug(self.module_name)
