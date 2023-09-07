import os


class PathLib:
    def __init__(self, **kwargs):
        self.__folders = {"maya": "maya_scripts", "tools": "azothyr_tools"}

        self.__library = {
            "": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts"),
            "user": os.path.expanduser("~"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "custom_scripts": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts"),
            "maya_scripts": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "maya_scripts"),
            "tools": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "azothyr_tools"),
            "folder": self.get_folder(kwargs.get("folder", "error")),
            "error": "Invalid folder name"
        }
        self.__library["maya"] = self.__library["maya_scripts"]
        self.__library["azothyr"] = self.__library["tools"]
        self.__library["azothyr_tools"] = self.__library["tools"]

    def get_folder(self, folder_name: str):
        if folder_name in self.__folders:
            return self.__folders[folder_name]
        else:
            return self.__library['error']

    def get_lib(self):
        return self.__library
