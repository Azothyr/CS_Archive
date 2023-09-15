import inspect
import traceback
from types import ModuleType
from typing import Tuple
# DO NOT IMPORT CONFIG OR DEBUG HANDLER HERE


def _stack_check(**kwargs) -> str:
    """
    Checks if the given stack is correct.
    ...
    """
    print_in_betweens = kwargs.get('print_in_betweens', False)
    offset = 0
    module_count = 0
    result = []
    result.append('-----TOP OF THE STACK-----')
    try:
        while True:
            _module = inspect.getmodule(inspect.stack()[0+offset][0])
            if _module:
                if _module.__name__ == '__main__':
                    main_mod = _module.__file__.split('\\')[-1].split('.')[0]
                    result.append(f'{module_count} -> STACK {offset}: <module \'{_module.__name__}\' from \'{main_mod}\'>')
                else:
                    result.append(f'{module_count} -> STACK {offset}: \'{_module.__name__}\'')
                module_count += 1
            elif print_in_betweens:
                # (e.g., built-ins, lambdas, interactive session)'
                result.append(f'STACK {offset}: Not associated with a specific module')
            offset += 1
    except IndexError:
        last = f"-----LAST STACK: {offset-1}-----"
        result.append(last)
        result = '\n'.join(result[::-1])
        return result


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


def get_caller_module(**kwargs) -> str | ModuleType | None:
    """
    Get the module that called this function (the caller) or the module that called + provided offset

    Keyword Args:
        offset (int): The number of frames to go back in the stack. Default is 0 (the caller).

    Returns:
        ModuleType: The module that called this function or caller based on provided offset.
    """
    offset = kwargs.get('offset', 0)
    caller_of_module = inspect.getmodule(inspect.stack()[0+offset][0]).__name__
    if caller_of_module == '__main__':
        caller_of_module = __get_caller(offset=offset)
        return caller_of_module
    return caller_of_module


def __get_traceback_line(stack: traceback) -> str: return stack.line


def __get_traceback_file(stack: traceback) -> str: return stack.filename


def __get_traceback_module(stack: traceback) -> str: return stack.name


def __get_traceback_line_num(stack: traceback) -> str: return stack.lineno


def get_traceback_stack(**kwargs) -> dict[str]:
    """
    Get the stack of the module that called this function (the caller) or the module that called + provided offset
    Keyword Args:
    -offset (int): The number of frames to go back in the stack. Default is 0 (the caller).
    -line_num (bool): Whether to include the line number in the result. Default is False.
    -module (bool): Whether to include the module name in the result. Default is False.
    -file (bool): Whether to include the file name in the result. Default is False.
    -line (bool): Whether to include the line in the result. Default is False.
    Returns:
    -list[str]: The stack of the module that called this function or caller based on provided offset.
    """
    result = {}

    # Get the last(from offset) entry from the stack (which by default should be the caller of this function)
    stack = traceback.extract_stack()[-1*(1+kwargs.get('offset', 0))]

    # Parse values from the kwargs
    if kwargs.get('line_num', False):
        result['line_num'] = __get_traceback_line_num(stack)
    if kwargs.get('module', False):
        result['module'] = __get_traceback_module(stack)
    if kwargs.get('file', False):
        result['file'] = __get_traceback_file(stack)
    if kwargs.get('line', False):
        result['line'] = __get_traceback_line(stack)

    return result
