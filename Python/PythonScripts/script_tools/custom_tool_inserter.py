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
from handlers.debug_handler import DebugHandler
from utils.platform_ops import platform_search_ops as platform_search
from utils.file_ops.file_path_ops import get_file_path_from_lib as get_path
from utils.file_ops.file_transfer_ops import transfer_py_dir_in_current as transfer_py_dir
debugger = DebugHandler(__name__)
# debugger.config_manager.turn_on_debug(all_modules=True)
# debugger.config_manager.turn_off_debug(all_modules=True)


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
