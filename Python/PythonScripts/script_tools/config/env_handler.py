from pathlib import Path
from script_tools.handlers.input_handler import InputHandler
from script_tools.handlers.hash_handler import HashHandler
from script_tools.components.json_config_manager_base import JsonConfigManagerBase

"""
This module defines the EnvHandler class which is responsible for managing
and updating the environment. It ensures that the environment is checked and 
updated as needed, leveraging the Singleton pattern to make sure there is only 
one instance of the environment handler at any given time.

Classes:
- EnvHandler: Manages the environment settings and refreshes as required.
"""


class EnvHandler(JsonConfigManagerBase):
    """
    Singleton class to handle and manage the environment configuration.

    Attributes:
        _instance: Stores the singleton instance of the class.
        _initialized: Flag to determine if the class was already initialized.
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """Override of the `__new__` method to implement the Singleton pattern."""
        if cls._instance is None:
            cls._instance = super(EnvHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self, json_path: str = Path.home() / "Documents/custom_scripts/_pkg_config.json",
                 environment_name: str = "DEFAULT_ENV", force_refresh: bool = False):
        """
        Initializes the environment handler.

        Args:
            json_path (str): Path to the JSON configuration.
            environment_name (str): Name of the environment.
        """
        # Check if already initialized
        if EnvHandler._initialized:
            return
        super().__init__(json_path=json_path, cache_path="off", create=True)
        self.__environment_name = self.config_json.get("environment_name", environment_name)
        self.__environment = self.config_json
        self.__required_keys = self.__check_environment_info().get('required_keys').keys()
        self.__refresh_needed = False if str(Path.home()) == self.config_json.get('user') else True

        # Check if repo paths exist
        python_repo_base_path = Path(self.config_json.get('python_repo_base', ""))
        maya_repo_base_path = Path(self.config_json.get('maya_repo_base', ""))
        custom_script_path = Path(self.config_json.get('custom_script_path', ""))

        # Instantiate HashHandler objects if paths are valid
        self.__script_repo_hasher = HashHandler(python_repo_base_path) if python_repo_base_path.exists() else None
        self.__maya_repo_hasher = HashHandler(maya_repo_base_path) if maya_repo_base_path.exists() else None
        # self.__custom_script_hasher = HashHandler(custom_script_path) if maya_repo_base_path.exists() else None
        # if self.__custom_script_hasher:
        #     print(self.__custom_script_hasher.cache_directory_hash())
        if self.__script_repo_hasher is None or self.__maya_repo_hasher is None:
            self.__refresh_needed = True

        # Update environment if refresh is needed
        if self.__refresh_needed or force_refresh:
            self.__check_environment()
            self.__script_repo_hasher = HashHandler(python_repo_base_path) if self.__script_repo_hasher is None else (
                self.__script_repo_hasher)
            print(self.__script_repo_hasher.cache_directory_hash())
            self.__maya_repo_hasher = HashHandler(maya_repo_base_path)if self.__maya_repo_hasher is None else (
                self.__maya_repo_hasher)
            print(self.__maya_repo_hasher.cache_directory_hash())

        # Set initialized flag to True
        EnvHandler._initialized = True

    @property
    def environment_name(self):
        return self.__environment_name

    @property
    def environment(self):
        return self.__environment

    @property
    def user(self):
        return self.environment.get('user')

    @property
    def script_path(self):
        return self.environment.get('script_path')

    @property
    def repo_base(self):
        return self.environment.get('repo_base')

    @property
    def arg_map_path(self):
        return self.environment.get('arg_map_path')

    def __repr__(self):
        return f"EnvHandler({self.environment_name}\n {self.environment})"

    @staticmethod
    def __request_user_input(prompt: str) -> str:
        """Prompt the user for input."""
        return InputHandler().get_text_input(prompt, allow_empty=True)

    @staticmethod
    def __check_environment_info():
        return {  # This will pass what is needed for the action to be performed based on the key in env check
            "name": "DEFAULT_ENV",
            "comp1": ["C:/GitRepos/Scripts_Private/Python/PythonScripts/script_tools", "C:/GitRepos/MayaPythonToolbox"],
            "comp2": ["C:/Repos/Scripts_Private/Python/PythonScripts/script_tools", "C:/Repos/MayaPythonToolbox"],
            "custom": "Documents/custom_scripts",
            "arg_map": "Documents/custom_scripts/maya_scripts/config/_settings/arg_map_index.json",
            "required_keys": {
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

    def __check_environment(self):
        """
        Check the environment settings based on the provided configuration.

        This method performs the following operations:
        1. Verifies the environment name.
        2. Resolves the paths of components based on given rules.
        3. Checks for custom script and argument map paths.
        4. Iterates over required keys to ensure the validity of the paths and optionally creates missing ones.
        """

        # 1. Verify environment name
        info = self.__check_environment_info()
        env_name = self.config_json.get('environment_name')
        if env_name is None or self.environment_name != env_name:
            self.set_value('environment_name', self.environment_name, force_save=True)

        # Helper function to check if a given path exists
        def path_exists(path):
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

        # Helper function to create directories or JSON files
        def create_directory_or_file(path):
            """Helper function to create a directory or a JSON file."""
            path_obj = Path(path)

            # Check if the provided path has a .json extension, suggesting it's a file
            if path_obj.suffix == '.json':
                path_obj.parent.mkdir(parents=True, exist_ok=True)
                path_obj.touch(exist_ok=True)
                print(f"Successfully created {path}")
                return

            # If it's not a .json file, proceed to create the directory
            try:
                path_obj.mkdir(parents=True, exist_ok=True)
                print(f"Successfully created directory {path}")
            except Exception as e:
                print(f"Failed to create directory {path}. Reason: {e}")

        # 4. Iterate over required keys
        for key, details in info['required_keys'].items():
            if key == 'user':
                new_value = Path.home()
                self.set_value(key, str(new_value), force_save=True)
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
                    f"Value for {key} is required. The provided path {new_path} does not exist.\n"
                    "Would you like to create it? (yes/no):\n>>> "
                )
                if user_response.strip().lower() == "yes":
                    create_directory_or_file(new_path)
                    if not new_path.exists():
                        raise ValueError(f"Failed to create the path: {new_path}")
                else:
                    raise ValueError(
                        f"Value for {key} is required, input was {new_path} but should be a path that exists.")

            # Save the resolved path
            self.set_value(key, str(new_path), force_save=True)


if __name__ == "__main__":
    env = EnvHandler()
