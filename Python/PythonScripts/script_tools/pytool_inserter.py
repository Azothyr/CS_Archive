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
import platform
try:
    from script_tools.cus_funcs.file_tools import transfer_py_dir_in_current, get_file_path_from_lib
except ModuleNotFoundError:
    from cus_funcs.file_tools import transfer_py_dir_in_current, get_file_path_from_lib


if __name__ == "__main__":
    if platform.system() == "Windows":
        print('Getting paths')
        repo, scripts_folder = get_file_path_from_lib(script_repo=True, tools=True, debug=True)
        if not repo:
            print("No repo found")
            exit()
        _exceptions = ["pytool_inserter.py"]

        transfer_py_dir_in_current(repo, scripts_folder, _exceptions)
