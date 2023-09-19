from functools import singledispatch
from pathlib import Path
from script_tools.handlers.input_handler import InputHandler
from script_tools.components.json_config_manager_base import JSONConfigManager


def _initial_info():
    return {
        "_src": {
            "name": "DEFAULT_ENV",
            "comp1": ["C:/GitRepos/Scripts_Private/Python/PythonScripts/script_tools", "C:/GitRepos/MayaPythonToolbox"],
            "comp2": ["C:/Repos/Scripts_Private/Python/PythonScripts/script_tools", "C:/Repos/MayaPythonToolbox"],
            "custom": "Documents/custom_scripts",
            "arg_map": "Documents/custom_scripts/maya_scripts/config/_settings/arg_map_index.json"
        },
        "required_keys_actions": {
            "user": {"prompt": "Please enter this computer profile's user name:\n>>> "},
            "custom_script_path": {"prompt": "Please enter the file path to the top folder you would like the"
                                             " custom scripts to write to: (e.g. C:/custom_scripts)\n>>> ",
                                   "action": lambda x: Path(x)},
            "python_repo_base": {"prompt": "Please enter the repo base path:\n>>> ",
                                 "action": lambda x: Path(x)},
            "maya_repo_base": {"prompt": "Please enter the repo base path:\n>>> ",
                               "action": lambda x: Path(x)},
            "arg_map_path": {"prompt": "Please enter the arg map path:\n>>> ",
                             "action": lambda x: Path(x)}
        }
    }


class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.configs = {}
        return cls._instance

    def add_config(self, key, file_path):
        # Add a new JSONConfigManager instance to the dictionary
        self.configs[key] = JSONConfigManager(file_path)

    def __init__(self, file_path, environment_name: str = "DEFAULT_ENV"):
        try:
            self.config_manager = JSONConfigManager(file_path)
        except FileNotFoundError:
            self.__handle_file_not_found(str(Path(file_path.resolve())))
        self.__setup_environment(environment_name)

    def get(self, key: str, default: any = None):
        return self.config_manager.get(key) if (self.config_manager.get(key)
                                                is not None) else default

    @singledispatch
    def set(self, key: str, value: any):
        # Default implementation (e.g., for simple types)
        self.config_manager.set(key, value)

    @set.register(dict)
    def _(self, key: str, value: dict):
        # Special implementation for dictionaries
        if self.is_nested_dict(value):
            self.update(key, value)
        else:
            self.config_manager.set(key, value)

    @set.register(Path)
    def _(self, key: str, value: Path):
        # Special implementation for Path objects
        self.config_manager.set(key, str(value))

    def update(self, key: str, value: dict):
        self.config_manager.set_single_nested(key, value)

    @staticmethod
    def is_nested_dict(d):
        return any(isinstance(val, dict) for val in d.values())

    def __handle_file_not_found(self, file_path: str):
        def request_user_input(prompt: str) -> str:
            return input(prompt).strip().lower()

        value = request_user_input(f'No config file found at {file_path}.\n'
                                   f'Would you like to create one at the location?\n(yes/no)>>> ')
        match value:
            case "yes":
                # Code to handle 'yes' case, like creating a new file.
                self.config_manager.write_config({})
            case "no":
                # Code to handle 'no' case, like maybe exiting the program or logging an error.
                print(f"\nRESULT: Config file was not found and will not be created.")
            case _:
                print(f'\nERROR: Invalid input received. Please type "yes" or "no".\n')
                # Recursively call the method again to re-prompt the user.
                self.__handle_file_not_found(file_path)

    def __setup_environment(self, env_name: str):
        # 1. Verify environment name
        info = _initial_info()
        if env_name is None or self.get("environment.name") != env_name:
            self.set('environment.name', env_name)

        # Helper function to check if a given path exists
        def path_exists(_path: str | Path) -> bool:
            return Path(_path).resolve().exists()

        # 2. Resolve component paths
        if path_exists(info['comp1'][0]) and path_exists(info['comp1'][1]):
            info['required_keys']['python_repo_base']['resolved_path'] = Path(info['comp1'][0])
            info['required_keys']['maya_repo_base']['resolved_path'] = Path(info['comp1'][1])
        elif path_exists(info['comp2'][0]) and path_exists(info['comp2'][1]):
            info['required_keys']['python_repo_base']['resolved_path'] = Path(info['comp2'][0])
            info['required_keys']['maya_repo_base']['resolved_path'] = Path(info['comp2'][1])
        else:
            info['required_keys']['python_repo_base']['resolved_path'] = None
            info['required_keys']['maya_repo_base']['resolved_path'] = None

        # 3. Check custom script path and argument map path
        if path_exists(Path.home() / info['custom']):
            info['required_keys']['custom_script_path']['resolved_path'] = Path.home() / info['custom']
        else:
            info['required_keys']['custom_script_path']['resolved_path'] = None

        if path_exists(Path.home() / info['arg_map']):
            info['required_keys']['arg_map_path']['resolved_path'] = Path.home() / info['arg_map']
        else:
            info['required_keys']['arg_map_path']['resolved_path'] = None

        # 4. Iterate over required keys
        for key, details in info['required_keys'].items():
            if key == 'user':
                new_value = Path.home()
                self.set(f'environment_paths.{key}', str(new_value))
                continue  # skip the rest of this loop iteration

            # Check if 'resolved_path' is available and use it if it exists
            if 'resolved_path' in details:
                new_path = details['resolved_path']
                if not new_path:
                    io = self.__request_user_input(
                        "\n<<Previous path was not found. Please provide a valid path.>>\n\n" + details['prompt'])
                    new_path = details['action'](io)
            else:
                io = self.__request_user_input(details['prompt'])
                new_path = details['action'](io)

            # Ensure path validity or offer creation of missing paths
            if not new_path or not new_path.exists():
                user_response = self.__handle_file_not_found(
                    f"Value for {key} is required.\n"
                    f" The provided path {new_path} does not exist.\n"
                    "Would you like to create it? (yes/no):\n>>> "
                )
                if user_response.strip().lower() == "yes":
                    create_directory_or_file(new_path)
                    if not new_path.exists():
                        raise ValueError(f"Failed to create the path: {new_path}")
                else:
                    raise ValueError(
                        f"Value for {key} is required, input was {new_path} but should be a path that exists.")




if __name__ == '__main__':
    pass
