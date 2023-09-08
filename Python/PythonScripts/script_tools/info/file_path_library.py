import os


class PathLib:
    def __init__(self, **kwargs):
        self.__folders = {"maya": "maya_scripts", "tools": "azothyr_tools"}

        maya_version = kwargs.get("maya_version", "2024")
        basic_paths = {
            "": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts"),
            "user": os.path.expanduser("~"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "custom_scripts": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts"),
            "maya_scripts": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "maya_scripts"),
            "tools": os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "azothyr_tools"),
            "maya_userSetup": os.path.join(os.path.expanduser(f"~\\Documents\\maya\\{maya_version}\\scripts\\userSetup.py")),
            "maya_exe": f"C:\\Program Files\\Autodesk\\Maya{maya_version}\\bin",
            "error": "Invalid folder name"
        }

        self.__library = basic_paths.copy()  # Initialize with the basic paths first
        self.__library["folder"] = self.get_folder(kwargs.get("folder", "error"))  # Add the dynamic folder path

        self.__library["maya"] = self.__library["maya_scripts"]
        self.__library["azothyr"] = self.__library["tools"]
        self.__library["azothyr_tools"] = self.__library["tools"]

        # Add folders inside maya_scripts and azothyr_tools
        self.__add_subfolders_to_lib("maya")
        self.__add_subfolders_to_lib("tools")

        # Check for repo paths
        self.__check_for_repo()

    def __repr__(self):
        return "\n".join([f"{k}: {v}" for k, v in self.__library.items()])

    def get_folder(self, folder_name: str):
        if folder_name in self.__folders:
            return self.__folders[folder_name]
        else:
            return self.__library['error']

    def get_lib(self):
        return self.__library

    def __add_subfolders_to_lib(self, main_folder):
        path = self.__library[main_folder]
        # List all folders in the given path
        subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        # Add each subfolder to the library
        for subfolder in subfolders:
            self.__library[f"{main_folder}_{subfolder}"] = os.path.join(path, subfolder)

    def __check_for_repo(self):
        """
        Update the library with tool and maya repo paths based on the existence
        of specific directories.
        """
        tool_src, maya_src = None, None  # Initialize with None as default

        if os.path.isdir("C:\\GitRepos"):
            tool_src = os.path.join("C:\\GitRepos\\Scripts_Private\\Python\\PythonScripts\\script_tools")
            maya_src = os.path.join("C:\\GitRepos\\MayaPythonToolbox\\ScriptsInMaya")
        elif os.path.isdir("C:\\Repos"):
            tool_src = os.path.join("C:\\Repos\\Scripts_Private\\Python\\PythonScripts\\script_tools")
            maya_src = os.path.join("C:\\Repos\\MayaPythonToolbox\\ScriptsInMaya")

        self.__library["script_repo"] = tool_src
        self.__library["maya_repo"] = maya_src

