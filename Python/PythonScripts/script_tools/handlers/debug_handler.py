"""
Debugging and Command Handling Utilities

This module provides utilities for:
- Debugging: Using the `DebugHandler` class to print debug messages.
- Defining a debugging behavior contract: Using the `DebugHandlerProtocol`.
- (If you end up including `CmdHandler` in this file) Command Line Argument Parsing: Using `CmdHandler` to handle and parse command line arguments.
"""
import sys
import importlib
from typing import Protocol
from handlers.config_manager import ConfigManager


class DebugHandlerProtocol(Protocol):
    """
    Protocol defining the contract for debug handling behaviors.

    Attributes:
    - module_name (str): Name of the module.
    - config_manager (ConfigManager): A manager for configurations.
    - debug (bool): A flag determining whether to show debug messages.

    Methods:
    - print(): Define how to display debug messages based on various parameters.
    """
    module_name: str
    config_manager: ConfigManager
    debug: bool

    def print(self, debug_key: str, *args: str, wrap: str = None, start: str = None, end: str = None, replace: str = None,
              upper: bool = False, lower: bool = False, capitalize: bool = False) -> None: ...


class DebugHandler:
    """
    DebugHandler handles the display of debug messages for a given module based on the behavior contract set by DebugHandlerProtocol.

    Attributes:
    - module_name (str): Name of the module.
    - config_manager (ConfigManager): A manager for configurations.
    - debug (bool): A flag determining whether to show debug messages.

    Methods:
    - print(debug_key, *args): Print the debug message corresponding to the given key with optional formatting.

    REQUIRES _debug_info() function in module that returns a dictionary of debug keys and messages.
    """
    def __init__(self, module_name, config_manager=None):
        self.module_name = module_name
        self.config_manager = config_manager or ConfigManager()
        self.debug = self._get_debug_status()

    def __repr__(self) -> str:
        """Return a string representation of the DebugHandler's module name and config state from the ConfigManager."""
        return f"DebugHandler({self.module_name}, {self.config_manager})"

    def print(self, debug_key, *args, wrap=None, start=None, end=None, replace=None,
              upper=False, lower=False, capitalize=False) -> None:
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

    def _get_debug_messages(self) -> dict:
        """Retrieve debug messages from the module's _debug_info function."""
        _module = sys.modules[self.module_name]
        if not hasattr(_module, '_debug_info'):
            raise NotImplementedError(f"Module {self.module_name} requires _debug_info function for debugging.")
        return _module._debug_info()

    def _get_debug_status(self) -> bool:
        """Check if debugging is globally enabled and if the current module should display debug messages."""
        global_debug = self.config_manager.get_global_debug()
        if not global_debug:
            return False
        return self.config_manager.get_module_debug(self.module_name)


def get_debugger(on=False, _all=False, *args, **kwargs) -> DebugHandlerProtocol:
    _debug_handler = importlib.import_module('handlers.debug_handler')
    if on:
        _debug_handler.config_manager.set_debug_config(global_debug=True)
    else:
        _debug_handler.config_manager.set_debug_config(global_debug=False)
    # _debug_handler.config_manager.update_debug_config(module_name='utils.file_ops.file_basic_ops',
    #                                             module_debug_value=True)
    # _debug_handler.config_manager.set_debug_config(global_debug=True)
    # _debug_handler.config_manager.turn_on_debug(all_modules=True)
    # _debug_handler.config_manager.turn_off_debug(all_modules=True)
    # _debug_handler.print('main-0.0')
    # print(f'--GLOBAL DEBUG--\t>>{_debug_handler.config_manager.get_global_debug()}')
    return _debug_handler.DebugHandler(__name__)
