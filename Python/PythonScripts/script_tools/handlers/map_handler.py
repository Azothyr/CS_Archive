import os
from script_tools.config.path_library_Manager import PathManager
from script_tools.handlers.debug_handler import get_debugger

__debugger = get_debugger(__name__)


def debug_info():
    """Returns a dictionary of debug messages for the module."""
    return {
        "set repo-start": "Setting repo paths",
        "set repo_except-1.1": "Tool repo not implemented or correctly provided",
        "set repo-1.1": "Repos set to: {}, Map repo set to: {}",
        "set repo-1.2": "Repo paths set, refreshing path map",
        "set repo-end": "SUCCESS: Set repo paths",

        "add subfolders-start": "Adding subfolders to path map",
        "add subfolders-1.1": "Working on key: {}, path: {}",
        "add subfolders-1.2": "Added folder to path map: KEY: {} --- VALUE: {}",
        "add subfolders-1.3": "Added file to path map: KEY: {} --- VALUE: {}",
        "add subfolders-end": "SUCCESS: Added subfolders to path map",

        "refresh-start": "Refreshing path map",
        "refresh-maya-end": "SUCCESS: Refreshed maya path map->{}",
        "refresh-repo-path-end": "SUCCESS: Refreshed scripts path map->{}",
        "refresh-arg-end": "SUCCESS: Refreshed arg path map->{}",

        "cfc-start": "Path map is up to date",
        "cfc_except-1.1": "Checking change method stuck in loop",
        "cfc_except-1.2": "Script cannot be completed because it is not being run on the correct computer",
        "cfc-2.1": "Repo paths not found",
        "cfc-2.2": "Attempting to set repo paths",
        "cfc-2.3": "repo paths set, refreshing path map",
        "cfc-2.4": "Repo paths found",
        "cfc-2.5": "key: script_repo ---path: {}",
        "cfc-3.1": "cfc-3.1>>Checking value: {}",
        "cfc-3.2": "Checking against: {}",
        "cfc-3.3": "Value not found: {}\n refreshing path map",
        "cfc-end": "Path map is up to date",

        "get path map-start": "Getting path map",
    }


def __add_subfolders_to_lib(key: str, path: str, primary_container: dict, **kwargs):
    """Adds subfolders to the path map"""
    __debugger.print('add subfolders-start')
    folder_exceptions = ["__pycache__", ".pytest_cache", ".idea", "tests"]
    file_exceptions = ["__init__.py", "__cpython__.py", "cpython-311.pyc"]
    key_exceptions = ["secondary_comp", "primary_comp"]

    _arg_maps = kwargs.get('arg_map_container', {})
    root_path = path
    # Checking if the key is an exception
    if key in key_exceptions:
        return
    # Working down paths given and adding their sub folders to primary_container and potentially arg_maps if provided
    # add subfolders-1.(~): Adding subfolders to the path map
    __debugger.print('add subfolders-1.1', key, path)
    for dirpath, dirnames, filenames in os.walk(root_path):
        # checking folder names against exceptions
        dirnames[:] = [d for d in dirnames if d not in folder_exceptions]

        # Parsing file path string to use in returning key name, path for the path map
        relative_path = dirpath.replace(root_path, "").lstrip("\\")
        split_path = relative_path.split('\\')
        joined_path = '_'.join(split_path)
        key_name_prefix = f"{key}_"

        # 1.2 Working through folders and adding them to the primary_container dictionary with modified key names
        for dir_name in dirnames:
            key_name_suffix = f"{joined_path if relative_path else ''}{dir_name}"
            key_name = key_name_prefix + key_name_suffix
            primary_container[key_name] = f"{primary_container[key][0:-1]}, '{dir_name}')"
            __debugger.print('add subfolders-1.2', key_name, primary_container[key_name])

        # 1.3 Working through files, if the file is an arg_map add it to the arg_map dictionary
        for file_name in filenames:
            if file_name in file_exceptions:
                continue
            elif file_name.endswith("_arg_map.json") or file_name.endswith("_arg_map.py"):
                _arg_maps[file_name.split('_')[0]] = \
                    Path(\\Documents\\custom_scripts\\maya_scripts\\config\\_settings\\{file_name}.json')"
                continue
            key_name_suffix = f"{file_name.split('.')[0]}"
            key_name = key_name_prefix + key_name_suffix
            primary_container[key_name] = f"{primary_container[key][0:-1]}, '{file_name}')"
            __debugger.print('add subfolders-1.3', key_name, primary_container[key_name])


def _refresh_path_map(primary_container: dict[str] = None, write_paths: dict[str] = None,
                      arg_container: dict[str] = None, **kwargs) -> None:
    """Refreshes the paths dictionary"""
    # Add folders inside maya_scripts and script_tools to the path map
    __debugger.print('refresh-start')
    for key, path in write_paths.items():
        __add_subfolders_to_lib(key, path, primary_container, arg_map_container=arg_container, **kwargs)

    # Write the path map to the path map file
    custom_scripts_path = write_paths.get('custom_path_map')
    arg_map_path = write_paths['maya_arg_map_path']
    script_repo_path = write_paths['script_config_path']
    arg_path_library = PathManager(json_path=arg_map_path,
                                   cache_path=arg_map_path.replace('_index.json', '_cache.json'))
    print(arg_path_library.cache_path)
    custom_path_library = PathManager(json_path=custom_scripts_path,
                                      cache_path=custom_scripts_path.replace('_library.json', '_cache.json'))
    script_repo_library = PathManager(json_path=script_repo_path,
                                      cache_path=write_paths["script_config_cache"])
    # Add arg_maps to the arg_map Library
    if arg_container and arg_map_path:
        arg_path_library.update_json(update_dict=arg_container, target_path=arg_map_path)
        __debugger.print('refresh-arg-end', arg_map_path)
    # Add folders inside maya_scripts and script_tools to the path map
    if primary_container:
        if script_repo_library:
            script_repo_library.update_json(update_dict=primary_container, target_path=script_repo_path)
            __debugger.print('refresh-repo-path-end', script_repo_path)
        if custom_path_library:
            custom_path_library.update_json(update_dict=primary_container, target_path=custom_scripts_path)
            __debugger.print('refresh-maya-end', custom_scripts_path)


def _check_for_change(primary_container: dict[str] = None, write_paths: dict[str] = None,
                      comp_container: dict[str] = None, arg_maps: dict[str] = None, **kwargs) -> bool:
    """Checks if the path map has changed"""
    # cfc-1
    run_count = kwargs.pop('run', 0)
    if run_count >= 2:
        raise OverflowError(__debugger.print('cfc_except-1.1'))
    _repo = comp_container['primary_comp'] if os.path.isdir(comp_container['primary_comp']) \
        else comp_container['secondary_comp'] if os.path.isdir(comp_container['secondary_comp']) else None
    if not _repo:
        raise ValueError(__debugger.print('cfc_except-1.2'))

    # cfc-2 Check if the repo paths exist, if not set them

    if primary_container.get('script_repo', None) is None or primary_container.get('maya_repo', None) is None:
        __debugger.print('cfc-2.1')
        __debugger.print('cfc-2.2')
        primary_container, write_paths = __set_repo(primary_container, write_paths, _repo)
        __debugger.print('cfc-2.3')
        _refresh_path_map(primary_container, write_paths, arg_maps)
        return _check_for_change(primary_container, write_paths, comp_container, arg_maps, run=run_count + 1, **kwargs)
    else:
        __debugger.print('cfc-2.4')
        __debugger.print('cfc-2.5', primary_container.get('script_repo'))

    val_to_check = [f"{_repo}\\Scripts_Private\\Python\\PythonScripts\\script_tools",
                    f"{_repo}\\MayaPythonToolbox\\maya_scripts"]

    check_against = [primary_container.get('maya_repo').replace("\"", ""),
                     primary_container.get('script_repo').replace("\"", "")]
    # cfc-3
    for value in val_to_check:
        __debugger.print('cfc-3.1', value)
        __debugger.print('cfc-3.2', ', '.join(check_against))
        if value not in check_against:
            __debugger.print('cfc-3.3', value)
            _refresh_path_map(primary_container, write_paths)
            return True
    # cfc-end
    __debugger.print('cfc-end')
    return False


if __name__ == "__main__":
    update_path_map()
