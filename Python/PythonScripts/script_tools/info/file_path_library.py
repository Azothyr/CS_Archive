from azothyr_tools.cus_funcs import format_tool as formatter
from azothyr_tools.info import map_handler as handler


class PathLib:
    def __init__(self):
        self.__library = handler.get_path_map()

    def __repr__(self):
        return formatter.format_dict_to_print(self.__library)

    def get_lib(self):
        return self.__library


if __name__ == "__main__":
    pathlib = PathLib()
    print(pathlib)
