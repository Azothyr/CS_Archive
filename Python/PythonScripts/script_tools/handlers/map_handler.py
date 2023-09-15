import os
from script_tools.config.path_map import paths
from script_tools.utils.file_ops.file_basic_ops import write_to_file as write
from script_tools.utils.format_ops import dict_ops as formatter
from script_tools.handlers.debug_handler import get_debugger as get_debugger
debugger = get_debugger(__name__)


def _debug_info():
    """Returns a dictionary of debug messages for the module."""
    return {
        'Block 2.1': "CFC BLOCK 2.1>>Repo paths not found",
        'Block 2.2': "CFC BLOCK 2.2>>Attempting to set repo paths",
        'Block 2.3': "CFC BLOCK 2.3>>repo paths set, refreshing path map",
        'Block 2.4': "CFC BLOCK 2.4>>Repo paths found",
        'Block 2.5': 'f"CFC BLOCK 2.5>>key: script_repo ---path: {}"',
        'Block 3.1': 'f"CFC BLOCK 3.1>>Checking value: {}"',
        'Block 3.2': 'f"CFC BLOCK 3.2>>Checking against: {}"',
        'Block 3.3': 'f"CFC BLOCK 3.3>>Value not found: {}\n refreshing path map"',
        'CFC End': 'CFC END>>Path map is up to date'
    }


def __set_repo(primary_container, secondary_container, _src=None):
    """
    Update the library with tool and maya repo paths based on the existence
    of specific directories.
    """
    if _src:
        _src = _src
        repo_paths = [f"{_src}\\Scripts_Private\\Python\\PythonScripts\\script_tools",
                      f"{_src}\\MayaPythonToolbox\\maya_scripts"]
        map_src = "\\config\\path_map.py"
    else:
        raise NotImplementedError("Tool repo not implemented yet")

    primary_container["script_repo"] = f"\"{repo_paths[0]}\""
    secondary_container["repo_map_path"] = repo_paths[0] + map_src
    primary_container["maya_repo"] = f"\"{repo_paths[1]}\""
    return primary_container, secondary_container


def __add_subfolders_to_lib(key, path, primary_container):
    """Adds subfolders to the path map"""
    folder_exceptions = ["__pycache__", ".pytest_cache", ".idea", "tests"]
    file_exceptions = ["__init__.py", "__cpython__.py", "cpython-311.pyc"]
    key_exceptions = ["secondary_comp", "primary_comp"]

    _arg_maps = {}
    root_path = path

    if key in key_exceptions:
        return

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
            primary_container[key_name] = f"{primary_container[key][0:-1]}, '{dir_name}')"

        # For files
        for file_name in filenames:
            if file_name in file_exceptions:
                continue
            elif file_name.endswith("_arg_map.py"):
                _arg_maps[file_name.split('_')[0]] = f"os.path.join(base_path, '{file_name}')"
                continue
            key_name_suffix = f"{file_name.split('.')[0]}"
            key_name = key_name_prefix + key_name_suffix
            primary_container[key_name] = f"{primary_container[key][0:-1]}, '{file_name}')"

    primary_container['arg_maps'].update(_arg_maps)


def refresh_path_map(primary_container, secondary_container, repo=True, custom=True, **kwargs):
    """Refreshes the paths dictionary"""
    # Add folders inside maya_scripts and script_tools to the path map
    for key, path in secondary_container.items():
        __add_subfolders_to_lib(key, path, primary_container)

    text_to_write = ["import os",
                     "",
                     "",
                     "paths = {",
                     ',\n'.join(formatter.format_dict_to_print(primary_container, "\'").split('\n')),
                     "}",
                     ""]

    scripts_path = secondary_container.get('custom_path_map')
    repo_path = secondary_container['repo_map_path']
    if repo:
        write(repo_path, '\n'.join(text_to_write), create_dir=kwargs.get('create_dir', False))
    if custom:
        write(scripts_path, '\n'.join(text_to_write), create_dir=True)


def check_for_change(primary_container, secondary_container, comp_container, run=0, **kwargs):
    """Checks if the path map has changed"""
    # CFC BLOCK 1
    if run >= 2:
        raise OverflowError("CFC BLOCK 1>>Checking change method stuck in loop")
    _repo = comp_container['primary_comp'] if os.path.isdir(comp_container['primary_comp']) \
        else comp_container['secondary_comp'] if os.path.isdir(comp_container['secondary_comp']) else None
    if not _repo:
        raise ValueError("CFC BLOCK 1>>Script cannot be completed because it is not being run on the correct computer")

    # CFC BLOCK 2
    _repo_paths = [primary_container.get('maya_repo', None), primary_container.get('script_repo', None)]
    if (not paths and primary_container.get('maya_repo', None) is None or
            primary_container.get('script_repo', None) is None):
        debugger.print('Block 2.1')
        debugger.print('Block 2.2')
        primary_container, secondary_container = __set_repo(primary_container, secondary_container, _repo)
        debugger.print('Block 2.3')
        refresh_path_map(primary_container, secondary_container)
        return check_for_change(primary_container, secondary_container, comp_container, run=1, **kwargs)
    else:
        debugger.print('Block 2.4')
        debugger.print('Block 2.5', primary_container.get('script_repo'))

    val_to_check = [f"{_repo}\\Scripts_Private\\Python\\PythonScripts\\script_tools",
                    f"{_repo}\\MayaPythonToolbox\\maya_scripts"]

    check_against = [primary_container.get('maya_repo').replace("\"", ""),
                     primary_container.get('script_repo').replace("\"", "")]
    # CFC BLOCK 3
    for value in val_to_check:
        debugger.print('Block 3.1', value)
        debugger.print('Block 3.2', ', '.join(check_against))
        if value not in check_against:
            debugger.print('Block 3.3', value)
            refresh_path_map(primary_container, secondary_container, custom=False)
            return True

    debugger.print('CFC End')
    return False


def get_path_map():
    """Returns the path map"""
    # Set the paths dictionary
    maya_version = "2024"
    rewrite_roots = {
        "user": "os.path.expanduser('~')",
        "documents": "os.path.join(os.path.expanduser('~'), 'Documents')",
        "custom_scripts": "os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts')",
        "tools": "os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools')",
        "maya": "os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts')",
        "user_setup": f"os.path.join(os.path.expanduser('~\\\\Documents\\\\maya\\\\{maya_version}"
                      f"\\\\scripts\\\\userSetup.py'))",
        "maya_exe": f"\'C:\\\\Program Files\\\\Autodesk\\\\Maya{maya_version}\\\\bin\'",
        "arg_maps": {"All": "os.path.join(base_path, 'arg_map.py')"},
        "error": '\"Invalid Key\"'
    }
    parent_dirs = {
        'maya': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'maya_scripts'),
        'tools': os.path.join(os.path.expanduser('~'), 'Documents', 'custom_scripts', 'script_tools'),
        'custom_path_map': os.path.join(os.path.expanduser('~'),
                                        'Documents', 'custom_scripts', '..', '../config', 'path_map.py')
    }
    repos_on_comps = {
        'primary_comp': "C:\\GitRepos",
        'secondary_comp': "C:\\Repos"
    }

    wait = True
    run = 0
    while wait:
        wait = check_for_change(rewrite_roots, parent_dirs, repos_on_comps, run)
        run = run + 1
    return paths


if __name__ == "__main__":
    get_path_map()
