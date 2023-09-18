"""
Debugging and Command Handling Utilities

This module provides utilities for: - Debugging: Using the `DebugHandler` class to print debug messages. - Defining a
debugging behavior contract: Using the `DebugHandlerProtocol`. - (If you end up including `CmdHandler` in this file)
Command Line Argument Parsing: Using `CmdHandler` to handle and parse command line arguments."""
# DO NOT IMPORT FROM SCRIPT TOOLS
import sys
from types import ModuleType
from typing import Protocol
from script_tools.config.debug_config_manager import DebugConfigManager
from script_tools.utils.stack_ops import get_caller_module, get_traceback_stack, _stack_check
from script_tools.handlers.terminal_handler import TerminalHandler

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
    config_manager: DebugConfigManager
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
        self.config_manager = config_manager or DebugConfigManager()
        self.debug = self._get_debug_status()
        self.traceback = self._get_traceback_status()

        if module_name not in self.config_manager.config_json['module_debug_values']:
            self.config_manager.set_value(f"module_debug_values-{module_name}", self._get_debug_status(), delimiter='-')

    def __repr__(self) -> str:
        """Return a string representation of the DebugHandler's module name and config state from the ConfigManager."""
        return f"DebugHandler({self.module_name}, {self.config_manager})"

    def _get_debug_messages(self) -> dict:
        """Retrieve debug messages from the module's _debug_info function."""
        _module: ModuleType = sys.modules[self.module_name]
        if not hasattr(_module, 'debug_info'):
            raise NotImplementedError(f"Module {self.module_name} requires debug_info function for debugging.")
        return _module.debug_info()

    def print(self, debug_key, *args, **kwargs) -> None:
        """Print the debug message for the provided key if debugging is enabled."""
        if not self.debug:
            return

        console = TerminalHandler()
        debug_messages = self._get_debug_messages()
        message = debug_messages.get(debug_key, f"Debug key '{debug_key}' not found!")
        if args:
            message = message.format(*args)

        console.change_style(fore='magenta')
        splitter = console.wrap("-"*5)

        override = kwargs.get('override', None)
        if override is None:
            for word in message.replace(":", "").split(" "):
                if word.lower() in self.config_manager.config_json['debug_formatting'].keys():
                    console.change_style(fore=self.config_manager.config_json['debug_formatting'][word.lower()],
                                         style=("italic", "underline"))
                    message = message.replace(word, console.wrap(word))
            output = f"<{debug_key.upper()}{splitter}{message}>"
        else:
            console.change_style(fore='red', back='white', style=("bold", "underline"))
            output = console.wrap(f"<{debug_key.upper()}{splitter}{message}>")

        if self.traceback:
            # gets the stack of the method calling this method
            stack = get_traceback_stack(offset=2, line_num=True, module=True, file=True, line=False)
            output = \
                f"File \"{stack['file']}\", line {stack['line_num']}, in {stack['module']}\n\t{output}"

        print(output)

    def _get_debug_status(self) -> bool:
        return (
                self.config_manager.get_global_debug_value() and
                self.config_manager.get_module_debug_value(self.module_name)
        ) if self.config_manager.get_global_debug_value() else False

    def _get_traceback_status(self) -> bool:
        return self.config_manager.get_traceback_value()


def get_debugger(module: bool | None = None, **kwargs) -> DebugHandler:
    """
    Get a DebugHandler for the given module. If a DebugHandler for the given module does not exist, create one.
    """
    temp = DebugHandler(module_name='__main__')
    __get_stack = temp.config_manager.get_value('config_globals-stack_check', delimiter='-')
    print(f'\nPASSED MODULE {module.upper()}') if __get_stack else None
    module_check = get_caller_module(offset=2)
    print(f'GOT MODULE {module_check.upper()}') if __get_stack else None
    print(_stack_check()) if __get_stack else None
    kwargs['main_allowed'] = False
    if module != module_check:
        if module == '__main__':
            kwargs['main_allowed'] = True
            if kwargs.get('global_switch', False):
                print(f"WARNING: Module name '{module}' does not match caller module '{module_check}'.") if\
                    __get_stack else None
            else:
                print(f"WARNING: {module} shows as '{module_check}'.") if __get_stack else None
    if module is None:
        raise ValueError("Module name must be provided to get debugger.")
    global _debugger
    if _debugger is None:
        _debugger = __setup_debugger(module_name=module, **kwargs)
    if _debugger.module_name != module:
        _debugger = __setup_debugger(module_name=module, **kwargs)
    return _debugger


def __setup_debugger(**kwargs) -> DebugHandler:
    """"""
    _debug_handler = DebugHandler(module_name=kwargs.get('module_name'))
    
    # If main_allowed (kwargs passed from __main__ mod) is True, allow updating the globals of the json
    if kwargs.get('main_allowed', False):
        # If _all is in kwargs of __main__, set all module debug values to the value of _all
        if kwargs.get('_all', None) is not None:
            if kwargs.get('_all'):
                _debug_handler.config_manager.turn_all_debug_on()
            else:
                _debug_handler.config_manager.turn_all_debug_off()
        # If global_switch is in kwargs of __main__, set the global debug value to the value of global_switch
        if kwargs.get('global_switch', None) is not None:
            _debug_handler.config_manager.set_value('config_globals-global_debug', kwargs.get('global_switch'),
                                                    delimiter='-')
        if kwargs.get('trace_switch', None) is not None:
            _debug_handler.config_manager.set_value('config_globals-traceback_debug', kwargs.get('trace_switch'),
                                                    delimiter='-')
        if kwargs.get('check_stack', None) is not None:
            _debug_handler.config_manager.set_value('config_globals-stack_check', kwargs.get('check_stack'),
                                                    delimiter='-')
    return _debug_handler
