"""
Last modified: 2023-09-14
This package provides utility functions to interact with the file system.

The package is organized into the following modules:
- file_basic_ops
- file_search_ops
- file_transfer_ops
- file_path_ops

The primary functionalities include:
- file_basic_ops
    - Writing, appending, and reading from files.
- file_search_ops
    - Checking if a given path exists.
    - Finding files with a specific ending.
- file_transfer_ops
    - Transferring .py files from one directory to another.
- file_path_ops
    - Retrieving file paths from a library.
    - Clearing all content from a directory.
    - Printing files at a specific location.
"""
from . import file_basic_ops
from . import file_search_ops
from . import file_transfer_ops
from . import file_path_ops

__all__ = ['file_basic_ops', 'file_search_ops', 'file_transfer_ops', 'file_path_ops']
