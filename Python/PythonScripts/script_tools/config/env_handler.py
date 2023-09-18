from functools import singledispatch
from pathlib import Path
from script_tools.handlers.input_handler import InputHandler
from script_tools.handlers.hash_handler import HashHandler
from script_tools.components.json_config_manager_base import JSONConfigManager


def __initial_info():
    _src = {
        "name": "DEFAULT_ENV",
        "comp1": ["C:/GitRepos/Scripts_Private/Python/PythonScripts/script_tools", "C:/GitRepos/MayaPythonToolbox"],
        "comp2": ["C:/Repos/Scripts_Private/Python/PythonScripts/script_tools", "C:/Repos/MayaPythonToolbox"],
        "custom": "Documents/custom_scripts",
        "arg_map": "Documents/custom_scripts/maya_scripts/config/_settings/arg_map_index.json"
    }
    required_keys_actions = {
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
    return _src, required_keys_actions



class EnvHandler:
    def __init__(self, file_path: str):
        self.config_manager = JSONConfigManager(file_path)

        # Check if repo paths exist
        python_repo_base_path = Path(self.get('python_repo_base', None))
        maya_repo_base_path = Path(self.get('maya_repo_base', None))
        custom_script_path = Path(self.get('custom_script_path', None))

    def get(self, key: str, default: any = None):
        return self.config_manager.get(key) if self.config_manager.get(key) else default

    @singledispatch
    def set(self, key: str, value: any):
        # Default implementation (e.g., for simple types)
        self.config_manager.set_value(key, value)

    @set.register(dict)
    def _(self, key: str, value: dict):
        # Special implementation for dictionaries
        if self.is_nested_dict(value):
            self.update(key, value)
        else:
            self.config_manager.set_value(key, value)

    @staticmethod
    def is_nested_dict(d):
        # Check if the dictionary contains another dictionary
        return any(isinstance(val, dict) for val in d.values())

    def update(self, key: str, value: dict):
        self.config_manager.set_nested_value(key, value)


class EnvHandlerOld():
        self.__required_keys = self.__check_environment_info().get('required_keys').keys()
        self.__refresh_needed = False if str(Path.home()) == self.config_json.get('user') else True

    @staticmethod
    def __request_user_input(prompt: str) -> str:
        return InputHandler().get_text_input(prompt, allow_empty=True)

    def __check_environment(self):
        # 1. Verify environment name
        info = self.__check_environment_info()
        env_name = self.config_json.get('environment_name')
        if env_name is None or self.environment_name != env_name:
            self.set_value('src_env.environment_name', self.environment_name, force_save=True)

        # Helper function to check if a given path exists
        def path_exists(path: str | Path) -> bool:
            return Path(path).resolve().exists()

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
                self.set_value(f'src_env.{key}', str(new_value), force_save=True)
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
                user_response = self.__request_user_input(
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



if __name__ == "__main__":
    """
    Path.home() / "Documents/custom_scripts/_pkg_config.json"
    """

    print('creating env')
    env = EnvHandler()
    print(env)
