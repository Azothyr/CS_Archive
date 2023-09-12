import json
import sys


def update_config(global_debug=None, module_name=None, module_debug_value=None):
    """
    Update the configuration with the specified values.
        Args:
        - global_debug (bool): The global debug setting to update to.
        - module_name (str): The name of the module for which to update the debug setting.
        - module_debug_value (bool): The debug setting for the specified module.
    """
    # Step 1: Load the existing configuration
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Step 2: Modify the configuration
    if global_debug is not None:
        config['global_debug'] = global_debug

    if module_name and module_debug_value is not None:
        if 'module_debug' not in config:
            config['module_debug'] = {}
        config['module_debug'][module_name] = module_debug_value

    # Step 3: Write back to the file
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)


class DebugHandler:
    def __init__(self, module_name):
        self.module_name = module_name
        self.debug = self._get_debug_status()

    def print_debug(self, debug_key, *args):
        if not self.debug:
            return

        debug_messages = self._get_debug_messages()
        message = debug_messages.get(debug_key, f"Debug key '{debug_key}' not found!")
        formatted_message = message.format(*args)
        print(formatted_message)

    def _get_debug_messages(self):
        # This method retrieves the _debug_info function from the specified module and gets the messages
        _module = sys.modules[self.module_name]
        if not hasattr(_module, '_debug_info'):
            raise NotImplementedError(f"Module {self.module_name} requires _debug_info function for debugging.")
        return _module._debug_info()

    def _get_debug_status(self):
        with open('config.json', 'r') as file:
            config = json.load(file)

        # First, check global setting
        global_debug = config.get('global_debug', False)

        if not global_debug:
            return False  # If global debugging is off, we don't even check the module-specific toggle.

        # If global debugging is on, we check for module-specific toggle
        return config.get('module_debug', {}).get(self.module_name, True)  # Defaults to True if not specified

