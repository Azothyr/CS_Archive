"""
Debugging and Command Handling Utilities

This module provides utilities for: - Debugging: Using the `DebugHandler` class to print debug messages. - Defining a
debugging behavior contract: Using the `DebugHandlerProtocol`. - (If you end up including `CmdHandler` in this file)
Command Line Argument Parsing: Using `CmdHandler` to handle and parse command line arguments."""
import sys
from typing import Protocol
from handlers.config_manager import ConfigManager
from utils.stack_ops import get_caller_module, get_traceback_stack
_debugger = None


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

    def print(self, debug_key: str, *args: str, wrap: str = None, start: str = None, end: str = None,
              replace: str = None,
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
        self.traceback = self._get_traceback_status()

    def __repr__(self) -> str:
        """Return a string representation of the DebugHandler's module name and config state from the ConfigManager."""
        return f"DebugHandler({self.module_name}, {self.config_manager})"

    def print(self, debug_key, *args, **kwargs) -> None:
        """Print the debug message for the provided key if debugging is enabled."""
        if not self.debug:
            return

        debug_messages = self._get_debug_messages()
        message = debug_messages.get(debug_key, f"Debug key '{debug_key}' not found!")
        output = message.format(*args)

        if self.traceback:
            # gets the stack of the method calling this method
            stack = get_traceback_stack(offset=2, line_num=True, module=True, file=True, line=True)
            output = \
                f"File \"{stack['file']}\", line {stack['line_num']}, in {stack['line']} {stack['module']}\n    {output}"

        print(output)

    def _get_debug_messages(self) -> dict:
        """Retrieve debug messages from the module's _debug_info function."""
        _module = sys.modules[self.module_name]
        if not hasattr(_module, '_debug_info'):
            raise NotImplementedError(f"Module {self.module_name} requires _debug_info function for debugging.")
        return _module._debug_info()

    def _get_debug_status(self) -> bool:
        return (
                self.config_manager.get_global_debug() and self.config_manager.get_module_debug(self.module_name)) \
            if self.config_manager.get_global_debug() else False

    def _get_traceback_status(self) -> bool:
        return self.config_manager.get_traceback()


def get_debugger(module=None, **kwargs) -> DebugHandler:
    print(f'PASSED MODULE {module}')
    module_t = get_caller_module()
    exit()
    if module is None:
        raise ValueError("Module name must be provided to get_or_initialize_debugger.")
    global _debugger
    if _debugger is None:
        _debugger = __get_debugger(module, **kwargs)
    if _debugger.module_name != kwargs.get('module', None):
        _debugger = __get_debugger(module, **kwargs)
    return _debugger


def __get_debugger(module: bool | None = None,
                   module_val: bool | None = None,
                   global_on: bool | None = None,
                   trace_on: bool | None = None,
                   _all: bool | None = None) -> DebugHandler:
    """_all can only be called by the main module."""
    def set_all(switch: bool):
        _debug_handler.config_manager.set_debug_config(all_modules=switch)

    _debug_handler = DebugHandler(module)

    # If the module is being run directly, return a DebugHandler with the given parameters.
    result = None
    if module == '__main__':
        result = set_all(True) if _all and _all is True else set_all(True) if _all and _all is False else None
    if result is None:
        if module_val is not None or global_on is not None:
            _debug_handler.config_manager.set_debug_config(module_debug_value=module_val, global_debug=global_on)

    # turn on traceback for terminal
    if trace_on is not None:
        _debug_handler.config_manager.set_config_globals(traceback=trace_on)

    return _debug_handler
