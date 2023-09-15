from script_tools.utils.format_ops import dict_ops as dict_formatter
from script_tools.handlers.map_handler import get_path_map


class PathLib:
    def __init__(self, **kwargs):
        self.__kwargs = kwargs
        self.__library = get_path_map(**self.__kwargs)

    def __repr__(self):
        return dict_formatter.format_dict_to_print(self.__library)

    def get_library(self):
        return self.__library

    def refresh_library(self):
        self.__library = get_path_map(**self.__kwargs)


if __name__ == "__main__":
    pathlib = PathLib()
    print(pathlib)
