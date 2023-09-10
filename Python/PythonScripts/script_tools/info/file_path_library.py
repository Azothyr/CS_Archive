try:
    from script_tools.cus_funcs import format_tool as formatter
    from script_tools.info import map_handler as handler
except ModuleNotFoundError:
    from cus_funcs import format_tool as formatter
    from info import map_handler as handler


class PathLib:
    def __init__(self):
        self.__library = handler.get_path_map()

    def __repr__(self):
        return formatter.format_dict_to_print(self.__library)

    def get_lib(self):
        return self.__library

    def refresh_lib(self):
        self.__library = handler.get_path_map()


if __name__ == "__main__":
    pathlib = PathLib()
    print(pathlib)
