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

from __init__ import get_or_initialize_debugger as get_debugger
"""
from utils.platform_ops import platform_search_ops as platform_search
from utils.file_ops.file_path_ops import get_file_path_from_lib as get_path
from utils.file_ops.file_transfer_ops import transfer_py_dir_in_current as transfer_py_dir
from utils import unpack_ops

debugger = get_debugger(global_on=True, trace_on=True)


def _debug_info() -> dict:
    return {
        "dunder main": "Running custom_tool_inserter.py 'dunder main'",
        "main-1.1": "Start of custom_tool_inserter.py 'main()'",
        "main-exception": "main() exception: {}",
        "main-2.1": "Getting paths",
        "main-2.2": "RETURNED: repo:--{}, scripts_folder:--{}",
        "main-2.3": "No repo found, Exiting",
        "main-3.1": "custom_tool_inserter.py finished",
        "main-3.2": "Exiting 'dunder main'/custom_tool_inserter.py'",
    }


def main():
    debugger.print('main-1.1', start='main-1.1 ', upper=True)
    if platform_search.platform_check("Windows"):
        debugger.print('main-2.1', start='main-2.1 ', upper=True)
        repo, scripts_folder = get_path(script_repo=True, tools=True)
        if not repo:
            debugger.print('main-2.3', start='main-2.3 ', upper=True)
            exit()
        debugger.print('main-2.2', start='main-2.2 ', upper=True)

        _exceptions = ["custom_tool_inserter.py"]

        transfer_py_dir(repo, scripts_folder, _exceptions)
        debugger.print('main-3.1', start='main-3.1', upper=True)
        debugger.print('main-3.2', start='main-3.2', upper=True)
        exit()"""


if __name__ == "__main__":
    debugger.print('dunder main', start='dunder main', upper=True)
    main()
