from pathlib import Path
from functools import singledispatch
from script_tools.components.decorators import singleton
from script_tools.handlers.input_handler import InputHandler
from script_tools.components.json_config_manager_base import JSONConfigManager


def _initial_info():
    return {
        "_src": {
            "comp1": ["C:/GitRepos/Scripts_Private/Python/PythonScripts/script_tools", "C:/GitRepos/MayaPythonToolbox"],
            "comp2": ["C:/Repos/Scripts_Private/Python/PythonScripts/script_tools", "C:/Repos/MayaPythonToolbox"],
            "custom": "Documents/custom_scripts",
            "arg_map": "maya_scripts/config/_settings/arg_map_index.json"
        },
        "required_keys_actions": {
            "user": {"prompt": "Please enter this computer profile's user name:\n>>> "},
            "custom_script_path": {"prompt": "Please enter the file path to the top folder you would like the"
                                             " custom scripts to write to: (e.g. C:/custom_scripts)\n>>> ",
                                   "action": lambda x: Path(x)},
            "python_repo": {"prompt": "Please enter the repo base path:\n>>> ",
                            "action": lambda x: Path(x)},
            "maya_repo": {"prompt": "Please enter the repo base path:\n>>> ",
                          "action": lambda x: Path(x)},
            "arg_map_path": {"prompt": "Please enter the arg map path:\n>>> ",
                             "action": lambda x: Path(x)},
            "error_message": lambda x: f"The provided path\n{x}\ndoes not exist.\n\nWould you like to create it? "
                                       "(yes/no):\n>>> "
        }
    }


@singleton
class ConfigManager:
    @classmethod
    def initialize(cls, file_path: Path):
        if not ConfigManager.has_instance():  # type: singleton
            instance = cls().set_instance(cls(file_path))
            instance.__setup_default_environment(file_path)
        else:
            instance = cls.get_instance()  # type: singleton

        cls.name = "ENV_MANAGER"
        cls.environment_manager = None
        cls.configs = None

        return instance

    def add_config(self, key: str, name: str, file_path:  str | Path):
        # Add a new JSONConfigManager instance to the dictionary
        self.configs[key] = JSONConfigManager(name, file_path)
        self.environment_manager.set(f'environment.configs.{key}',
                                     file_path if not isinstance(file_path, Path) else str(file_path))

    def get_config(self, key):
        # Retrieve a JSONConfigManager instance by its key
        return self.configs.get(key, None)

    def __setup_default_environment(self, file_path: Path,):
        """Set up the default environment. Can be called externally if needed."""
        string_file_path = str(file_path)
        try:
            self.environment_manager = JSONConfigManager(self.name, string_file_path)
            self.environment_manager.write_config({self.name: string_file_path})
        except FileNotFoundError:
            prompt = _initial_info()['required_keys_actions']['error_message'](string_file_path)
            self.__handle_file_not_found(prompt, file_path)
            if not file_path.exists():
                raise FileNotFoundError(f"Could not find the file: {file_path}")
        else:
            self.environment_manager = JSONConfigManager(self.name, string_file_path)
            self.environment_manager.write_config({self.name: string_file_path})
        finally:
            self.__setup_environment()

    def get(self, key: str, default: any = None):
        print(f"Getting {key}")
        print(f"Default: {default}")
        return self.environment_manager.get(key) if (self.environment_manager is not None) else default

    @singledispatch
    def set(self, key: str, value: any):
        # Default implementation (e.g., for simple types)
        self.environment_manager.set(key, value)

    @set.register(dict)
    def _(self, key: str, value: dict):
        # Special implementation for dictionaries
        if self.is_nested_dict(value):
            self.update(key, value)
        else:
            self.environment_manager.set(key, value)

    @set.register(Path)
    def _(self, key: str, value: Path):
        # Special implementation for pathlib Path objects
        self.environment_manager.set(key, str(value))

    def update(self, key: str, value: dict):
        self.environment_manager.set_single_nested(key, value)

    @staticmethod
    def is_nested_dict(d):
        return any(isinstance(val, dict) for val in d.values())

    def __handle_file_not_found(self, message: str, file_path: Path = None):
        _prompt_msg = message
        user_input = InputHandler().handle_input('confirm', _prompt_msg)
        if user_input == "yes":
            self.create_directory_or_file(self.name, Path(file_path))

    @staticmethod
    def create_directory_or_file(name: str, path: Path):
        # Create a directory or file based on the provided Path.
        try:
            if '.' in path.name:  # Assuming it's a file if it has an extension
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()
                JSONConfigManager(name, path).write_config({})
            else:
                path.mkdir(parents=True, exist_ok=True)
            print(f"Successfully created {path}")
            if not path.exists():
                raise ValueError(f"Failed to create the path: {path}")
        except Exception as e:
            print(f"Failed to create {path}. Error: {e}")

    def __setup_environment(self):
        # 1. Verify environment name and set it if it's valid
        source_info = _initial_info()['_src']
        key_actions = _initial_info()['required_keys_actions']

        # Helper function to check if a given path exists
        def path_exists(_path: str) -> bool:
            return Path(_path).resolve().exists()

        # 2. Resolve component paths
        # C:\..\Scripts_Private\Python\PythonScripts\script_tools
        # C:\..\MayaPythonToolbox
        if path_exists(source_info['comp1'][0]) and path_exists(source_info['comp1'][1]):
            key_actions['python_repo']['resolved_path'] = Path(source_info['comp1'][0])
            key_actions['maya_repo']['resolved_path'] = Path(source_info['comp1'][1])
        elif path_exists(source_info['comp2'][0]) and path_exists(source_info['comp2'][1]):
            key_actions['python_repo']['resolved_path'] = Path(source_info['comp2'][0])
            key_actions['maya_repo']['resolved_path'] = Path(source_info['comp2'][1])
        else:
            key_actions['python_repo']['resolved_path'] = None
            key_actions['maya_repo']['resolved_path'] = None

        # 3. Check custom script path
        # C:\..\Documents\custom_scripts
        if path_exists(str(Path.home() / source_info['custom'])):
            key_actions['custom_script_path']['resolved_path'] = Path.home() / source_info['custom']
        else:
            key_actions['custom_script_path']['resolved_path'] = None

        # 4. Check arg map path
        # C:\..\MayaPythonToolbox\maya_scripts\config\_settings\arg_map_index.json
        if path_exists(str(Path(key_actions['maya_repo']['resolved_path'] / source_info['arg_map']))):
            key_actions['arg_map_path']['resolved_path'] = str(Path(key_actions['maya_repo']['resolved_path'] /
                                                                    source_info['arg_map']))
        else:
            key_actions['arg_map_path']['resolved_path'] = None

        # 4. Iterate over required keys
        for key, details in key_actions.items():
            if key == 'error_message':
                continue
            if key == 'user':
                new_value = Path.home()
                print(new_value)
                self.set(f'environment.src_paths.{key}', str(new_value))
                continue  # skip the rest of this loop iteration

            # Check if 'resolved_path' is available and use it if it exists
            if 'resolved_path' in details:
                new_path = details['resolved_path']
                if not new_path:
                    user_input = InputHandler().handle_input('text', details['prompt'])
                    new_path = details['action'](user_input)
                details['resolved_path'] = str(Path(new_path).resolve())
            else:
                user_input = InputHandler().handle_input('text', details['prompt'])
                new_path = details['action'](user_input)
                details['resolved_path'] = str(Path(new_path).resolve())

            # Ensure path validity or offer creation of missing paths
            if not new_path or not path_exists(new_path):
                prompt = _initial_info()['required_keys_actions']['error_message'](str(new_path))
                self.__handle_file_not_found(prompt, new_path)

        # Update the environment with the new value
        for key, path in key_actions.items():
            if not isinstance(path, dict) or 'resolved_path' not in path:
                continue
            if not path['resolved_path']:
                raise ReferenceError(f"On last step of initialization, could not find the path for {key}")
            self.set(f'environment.src_paths.{key}', path['resolved_path'])


if __name__ == '__main__':
    # Example usage:
    def _exit() -> None:
        """A function to print a message when option 2 is selected."""
        TEST_JSON_FILE.unlink(missing_ok=True)
        print("Exiting...")
        exit(0)

    handler = InputHandler({
        'menu_options': {
            'validator': InputHandler._is_option,
            'actions': {
                'exit': _exit,
                '': _exit,
                ' ': _exit,
                '  ': _exit,
                'q': _exit,
                'quit': _exit
            },
            'error_message': 'Please select a valid option or hit Enter to exit.'
        }
    })

    TEST_JSON_FILE = Path("../tests/test_config.json").resolve()
    ConfigManager.initialize(TEST_JSON_FILE)
    prompt_msg = "Press ENTER or type 'exit' to end script.\n>>> "
    handler.handle_input('menu_options', prompt_msg)
