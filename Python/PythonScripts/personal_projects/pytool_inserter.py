r"""
**MUST RUN ADMIN CMD AND SET THE SYS VARIABLES do not run it multiple times**
code: setx PYTHONPATH "%PYTHONPATH%;C:\Users\.\Documents\maya\customscripts" /M
setx PATH "%PATH%;C:\Users\.\Documents\maya\customscripts" /M
(to check the path and python path in cmd you need to close the terminal and reopen it
 then using echo %PATH% and echo %PYTHONPATH%)
Get all .py _files in the directory and subdirectories this script is run from
Return: Writes Maya userSetup.py and places all custom scripts in Maya directory
Set a sys env variable "pythonpath" with script folder path value.
"""
import os
import platform
import shutil
from azothyr_tools.functions.file_tools import clear_directory, print_files_at_location


if __name__ == "__main__":
    if platform.system() == "Windows":
        scripts_folder = os.path.join(os.path.expanduser('~\\documents\\custom_scripts\\azothyr_tools'))

        os.makedirs(scripts_folder, exist_ok=True)

        clear_directory(scripts_folder)

        cwd = os.getcwd()
        file_exceptions = ["pytool_inserter.py"]
        try:
            for _root, _dirs, _files in os.walk(cwd):
                for file_name in _files:
                    if file_name.endswith(".py") and file_name not in file_exceptions:
                        rel_path = os.path.relpath(_root, cwd)
                        dest_folder = os.path.join(scripts_folder, rel_path)
                        os.makedirs(dest_folder, exist_ok=True)
                        src_file_path = os.path.join(_root, file_name)
                        dest_file_path = os.path.join(dest_folder, file_name)
                        shutil.copy2(src_file_path, dest_file_path)
        except PermissionError:
            print(f"Insufficient permissions to add folder to '{scripts_folder}'.\nPlease run file as admin...")
        finally:
            print_files_at_location(scripts_folder)
