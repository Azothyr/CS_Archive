r"""
**MUST RUN ADMIN CMD AND SET THE SYS VARIABLES do not run it multiple times**
code: setx PYTHONPATH "%PYTHONPATH%;C:\Users\.\Documents\custom_scripts" /M
setx PATH "%PATH%;C:\Users\.\Documents\custom_scripts" /M
(to check the path and python path in cmd you need to close the terminal and reopen it
 then using echo %PATH% and echo %PYTHONPATH%)
Get all .py _files in the directory and subdirectories this script is run from
Return: Writes Maya userSetup.py and places all custom scripts in Maya directory
Set a sys env variable "pythonpath" with script folder path value.
"""
from pathlib import Path
# from handlers.debug_handler import get_debugger
# from utils.platform_ops import platform_search_ops as platform_search
# from utils.file_ops.file_path_ops import get_file_path_from_lib as get_path
# from utils.file_ops.file_transfer_ops import transfer_current_file_directory as transfer_py_dir

#
# # __debugger = get_debugger(__name__, _all=True, global_switch=True, trace_switch=True, check_stack=True)
# __debugger = get_debugger(__name__, global_switch=True)
#
#
# def debug_info() -> dict:
#     return {
#         "dunder main enter": "Running custom_tool_inserter.py 'dunder main'",
#         "dunder main exit": "Exiting 'dunder main'/custom_tool_inserter.py'",
#         "main-1.1": "Start of custom_tool_inserter.py 'main()'",
#         "main-2.1": "Getting paths",
#         "main-2.2": "RETURNED: repo:--{}, scripts_folder:--{}",
#         "main-2.3": "No repo found, Exiting",
#         "main-3.1": "Main of custom_tool_inserter.py finished",
#     }
#
#
# def main():
#     __debugger.print('main-1.1', start='main-1.1 ', upper=True)
#     if platform_search.platform_check("Windows"):
#         __debugger.print('main-2.1', start='main-2.1 ', upper=True)
#         repo, scripts_folder = get_path(script_repo=True, tools=True)
#         if not repo:
#             __debugger.print('main-2.3', start='main-2.3 ', upper=True)
#             exit()
#         __debugger.print('main-2.2', start='main-2.2 ', upper=True)
#
#         _exceptions = ["custom_tool_inserter.py"]
#         _file_type_inclusion = [".py", ".json", ".txt", ".md"]
#         print('conf inserter-------------------------------' + repo, scripts_folder)
#         transfer_py_dir(repo, scripts_folder, _file_type_inclusion, _exceptions)
#         __debugger.print('main-3.1', start='main-3.1', upper=True)
#
#
# if __name__ == "__main__":
#     __debugger.print('dunder main enter', start='dunder main', upper=True)
#     main()
#     __debugger.print('dunder main exit', start='main-3.2', upper=True)

if __name__ == "__main__":
    import os
    from pathlib import Path

    base_repo_path = Path(os.environ.get('GITHUB_REPO_PATH', 'C:\\GitRepos'))  # Default to 'C:\GitRepos' if not set
    base_repo_path = Path("C:/GitRepos") if Path("C:/GitRepos").exists() else Path("C:/Repos")

    {
        "base_repo_path": "C:\\GitRepos"
    }
    {
        "base_repo_path": "C:\\Repos"
    }

    with open('config.json', 'r') as f:
        config = json.load(f)

    base_repo_path = Path(config["base_repo_path"])

    base_repo_path = input("Please enter the base repo path: ")

    repo1 = base_repo_path / "repo1"
    repo2 = base_repo_path / "repo2"

    # Set environment variable, not persistent, so it will be lost when the script ends
    my_path = Path("/some/directory")
    os.environ['MY_PATH_VARIABLE'] = str(my_path)

    config_path = Path(os.environ.get('CONFIG_PATH', 'default_config_path'))
    if config_path.exists() and config_path.is_file():
        content = config_path.read_text()

