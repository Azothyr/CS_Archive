import inspect
from typing import Tuple


def __get_caller(**kwargs) -> str:
    """
    Get the name of the module that called this function (the caller) or the module that called + provided offset

    Keyword Args:
        offset (int): The number of frames to go back in the stack. Default is 0 (the caller).

    Returns:
        str: The name of the module that called this function or caller based on provided offset.
    """
    offset = kwargs.get('offset', 0)
    caller = inspect.stack()[1 + offset][1].split('\\')[-1].split('.')[0]
    return caller


def get_caller_module(**kwargs) -> str | Tuple[str, bool]:
    """
    Get the module that called this function (the caller) or the module that called + provided offset

    Keyword Args:
        offset (int): The number of frames to go back in the stack. Default is 0 (the caller).

    Returns:
        ModuleType: The module that called this function or caller based on provided offset.
    """
    caller_of_module = inspect.getmodule(inspect.stack()[2][0]).__name__
    if caller_of_module == '__main__':
        caller_of_module = __get_caller(offset=2)
        return caller_of_module, True
    print(caller_of_module)
    return caller_of_module
