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
<<<<<<< STABLE
import platform
try:
    from script_tools.functions.file_tools import transfer_py_dir_in_current, get_file_path_from_lib
except ModuleNotFoundError:
    from functions.file_tools import transfer_py_dir_in_current, get_file_path_from_lib


def _debug_info():
    return {
        "debug-0": "Start of custom_tool_inserter.py",
        "debug-1": "Getting paths",
        "debug-2": "No repo found, Exiting",
        "debug-3": "custom_tool_inserter.py finished",
        "debug-4": "Exiting",
    }


if __name__ == "__main__":
    debugger.print('debug-0')
    if platform_search.platform_check("Windows"):
        try:
            debugger.print('debug-1')
            repo, scripts_folder = get_path(script_repo=True, tools=True)
            if not repo:
                debugger.print('debug-2')
                exit()
            _exceptions = ["custom_tool_inserter.py"]

            transfer_py_dir(repo, scripts_folder, _exceptions)
        finally:
            debugger.print('debug-3')
            debugger.print('debug-4')
            exit()
=======
from handlers.debug_handler import get_debugger
from script_tools.utils.platform_ops import platform_search_ops as platform_search
from script_tools.utils.file_ops.file_path_ops import get_file_path_from_lib as get_path
from script_tools.utils.file_ops.file_transfer_ops import transfer_current_file_directory as transfer_py_dir

# __debugger = get_debugger(__name__, _all=True, global_switch=True, trace_switch=True, check_stack=True)
__debugger = get_debugger(__name__, global_switch=True)


def debug_info() -> dict:
    return {
        "dunder main enter": "Running custom_tool_inserter.py 'dunder main'",
        "dunder main exit": "Exiting 'dunder main'/custom_tool_inserter.py'",
        "main-1.1": "Start of custom_tool_inserter.py 'main()'",
        "main-2.1": "Getting paths",
        "main-2.2": "RETURNED: repo:--{}, scripts_folder:--{}",
        "main-2.3": "No repo found, Exiting",
        "main-3.1": "Main of custom_tool_inserter.py finished",
    }


def main():
    __debugger.print('main-1.1', start='main-1.1 ', upper=True)
    if platform_search.platform_check("Windows"):
        __debugger.print('main-2.1', start='main-2.1 ', upper=True)
        repo, scripts_folder = get_path(script_repo=True, tools=True)
        if not repo:
            __debugger.print('main-2.3', start='main-2.3 ', upper=True)
            exit()
        __debugger.print('main-2.2', start='main-2.2 ', upper=True)

        _exceptions = ["custom_tool_inserter.py"]
        _file_type_inclusion = [".py", ".json", ".txt", ".md"]
        print('conf inserter-------------------------------' + repo, scripts_folder)
        transfer_py_dir(repo, scripts_folder, _file_type_inclusion, _exceptions)
        __debugger.print('main-3.1', start='main-3.1', upper=True)


if __name__ == "__main__":
    __debugger.print('dunder main enter', start='dunder main', upper=True)
    main()
    __debugger.print('dunder main exit', start='main-3.2', upper=True)
>>>>>>> "
