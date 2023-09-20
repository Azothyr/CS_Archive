from script_tools.utils.format_ops import dict_ops as dict_formatter
from script_tools.components.json_config_manager_base import JsonConfigManager
from script_tools.config.config_manager import EnvHandler
# from script_tools.handlers.debug_handler import get_debugger
from script_tools.components.decorators import singleton


@singleton
class PathManager(JsonConfigManager):
    @staticmethod
    def __get_environment():
        # __debugger = get_debugger(__name__)
        env_handler = EnvHandler()
        print(env_handler.get_value('python_repo_base'))
        if env_handler.get_value('config_paths.path_library_config') is None:
            config_path = env_handler.get_value('python_repo_base') + '\\config\\_settings\\_path_library.json'
            print(config_path)
            env_handler.set_value('config_paths.path_library_config', config_path)
        if env_handler.get_value('config_paths.python_repo_cache') is None:
            cache_path = env_handler.get_value('python_repo_base') + '\\config\\_settings\\_configs_cache.json'
            print(cache_path)
            env_handler.set_value('config_paths.path_library_cache', cache_path)
        return env_handler

    def __init__(self, **kwargs):
        self.__env_handler = self.__get_environment()
        print(self.__env_handler.get_value('config_paths.path_library_config'))
        super().__init__(json_path=self.__env_handler.get_value('config_paths.path_library_config'),
                         cache_path=self.__env_handler.get_value('config_paths.python_repo_cache')),
        self.__kwargs = kwargs
        self.__library = self.config_json

    def __repr__(self) -> str: return dict_formatter.format_dict_to_print(self.__library)

    @property
    def get_library(self) -> str: return self.__library

    @property
    def get_library_path(self) -> str: return self.__env_handler.get_value('config_paths.path_library_config')

    @staticmethod
    def update_library():
        """Returns the path map"""
        # self.__debugger.print('get path map-start')
        # get path-1.(~) Set the paths dictionary
        custom_scripts_paths_return = {}

        # wait = True
        # while wait:
        #     wait = _check_for_change(run=0)


if __name__ == "__main__":
    path_manager = PathManager()
    print(path_manager)
