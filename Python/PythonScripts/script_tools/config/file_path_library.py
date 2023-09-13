from utils import format_ops as formatter
from handlers import map_handler as handler



class PathLib:
    def __init__(self, **kwargs):
        self.__kwargs = kwargs
        self.__library = handler.get_path_map(**self.__kwargs)

    def __repr__(self):
        return formatter.format_dict_to_print(self.__library)

    def get_library(self):
        return self.__library

    def refresh_library(self):
        self.__library = handler.get_path_map(**self.__kwargs)


if __name__ == "__main__":
    pathlib = PathLib()
    print(pathlib)
