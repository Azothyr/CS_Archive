import platform
from script_tools.handlers.debug_handler import get_debugger
debugger = get_debugger(__name__)


def _debug_info():
    return {
        "platform_check-1": "'{}' is running",
    }


def platform_check(input_platform):
    """
    Checks if the given platform is running.
        Args:
        - path (str): The path to check.
        Raises:
        - ValueError: If the path does not exist.
    """
    if platform.system() == input_platform:
        debugger.print('platform_check-1', input_platform)
        return True
    return False
