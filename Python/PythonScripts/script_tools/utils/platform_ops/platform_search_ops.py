import platform
from script_tools.handlers.debug_handler import get_debugger
__debugger = get_debugger(__name__)


def debug_info():
    return {
        "platform_check-start": "Start of platform_check method",
        "platform_check-end1": "CONFIRMED: '{}' is running",
        "platform_check-end2": "ERROR: '{}' is not running",
    }


def platform_check(input_platform):
    """
    Checks if the given platform is running.
        Args:
        - path (str): The path to check.
        Raises:
        - ValueError: If the path does not exist.
    """
    __debugger.print('platform_check-start')
    if platform.system() == input_platform:
        __debugger.print('platform_check-end1', input_platform)
        return True
    __debugger.print('platform_check-end2', input_platform)
    return False
