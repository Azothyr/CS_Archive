import os
from azothyr_tools.info.path_map import paths
from azothyr_tools.cus_funcs import format_tool as formatter
from azothyr_tools.cus_funcs import file_tools


def __check_for_repo(container):
    """
    Update the library with tool and maya repo paths based on the existence
    of specific directories.
    """
    tool_src, maya_src = None, None  # Initialize with None as default

    if os.path.isdir("C:\\GitRepos"):
        tool_src = os.path.join("\'C:\\GitRepos\\Scripts_Private\\Python\\PythonScripts\\script_tools\'")
        maya_src = os.path.join("\'C:\\GitRepos\\MayaPythonToolbox\\ScriptsInMaya\'")
    elif os.path.isdir("C:\\Repos"):
        tool_src = os.path.join("\'C:\\Repos\\Scripts_Private\\Python\\PythonScripts\\script_tools\'")
        maya_src = os.path.join("\'C:\\Repos\\MayaPythonToolbox\\ScriptsInMaya\'")

    container["script_repo"] = tool_src
    container["maya_repo"] = maya_src


def __add_subfolders_to_lib(key, path, container):
    folder_exceptions = ["__pycache__", ".pytest_cache", ".idea", "tests"]
    file_exceptions = ["__init__.py", "__cpython__.py", "cpython-311.pyc"]
    _arg_maps = {}
    root_path = path

    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in folder_exceptions]

        relative_path = dirpath.replace(root_path, "").lstrip("\\")
        split_path = relative_path.split('\\')
        joined_path = '_'.join(split_path)
        key_name_prefix = f"{key}_"

        # For folders
        for dir_name in dirnames:
            key_name_suffix = f"{joined_path if relative_path else ''}{dir_name}"
            key_name = key_name_prefix + key_name_suffix
            container[key_name] = f"{container[key][0:-1]}, '{dir_name}')"

        # For files
        for file_name in filenames:
            if file_name in file_exceptions:
                continue
            elif file_name.endswith("_arg_map.py"):
                _arg_maps[file_name.split('_')[0]] = f"os.path.join(base_path, '{file_name}')"
                continue
            key_name_suffix = f"{file_name.split('.')[0]}"
            key_name = key_name_prefix + key_name_suffix
            container[key_name] = f"{container[key][0:-1]}, '{file_name}')"

    container['arg_maps'].update(_arg_maps)


def refresh_path_map():
    """Refreshes the paths dictionary"""

    maya_version = "2024"
    rewrite_roots = {
        "user": "os.path.expanduser('~')",
        "documents": "os.path.join(os.path.expanduser('~'), 'Documents')",
        "custom_scripts": "os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts')",
        "tools": "os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'azothyr_tools')",
        "maya": "os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts')",
        "user_setup": f"os.path.join(os.path.expanduser('~\\\\Documents\\\\maya\\\\{maya_version}\\\\scripts\\\\userSetup.py'))",
        "maya_exe": f"\'C:\\\\Program Files\\\\Autodesk\\\\Maya{maya_version}\\\\bin\'",
        "arg_maps": {"All": "os.path.join(base_path, 'arg_map.py')"},
        "error": '\"Invalid Key\"'
    }

    parent_dirs = {
        'maya': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts'),
        'tools': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'azothyr_tools')
    }
    # Add folders inside maya_scripts and azothyr_tools
    # Add folders inside maya_scripts and azothyr_tools
    for key, path in parent_dirs.items():
        __add_subfolders_to_lib(key, path, rewrite_roots)

    __check_for_repo(rewrite_roots)

    # path_map = f"{rewrite_roots['maya_path_map'])"
    path_map = 'path_map.py'
    text_to_write = ["import os",
                     "",
                     "",
                     "paths = {",
                     ',\n'.join(formatter.format_dict_to_print(rewrite_roots, "\'").split('\n')),
                     "}",
                     ""]

    file_tools.write_to_file(path_map, '\n'.join(text_to_write))


def check_for_change():
    """Checks if the path map has changed"""
    pass


def get_path_map():
    """Returns the path map"""
    return paths


if __name__ == "__main__":
    refresh_path_map()
