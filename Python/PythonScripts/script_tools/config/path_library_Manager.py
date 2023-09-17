from script_tools.utils.format_ops import dict_ops as dict_formatter
from script_tools.components.json_config_manager_base import JsonConfigManagerBase


class PathLib(JsonConfigManagerBase):
    def __init__(self, **kwargs):
        super().__init__(json_path='script_tools/config/_settings/_path_library.json',
                         cache_path='script_tools/config/_settings/_configs_cache.json')
        self.__kwargs = kwargs
        self.__library = self.config_json

    def __repr__(self):
        return dict_formatter.format_dict_to_print(self.__library)

    def get_library(self):
        return self.__library


if __name__ == "__main__":
    pathlib = PathLib()
    print(pathlib)
