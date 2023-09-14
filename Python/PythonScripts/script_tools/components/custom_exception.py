from typing import Protocol
from handlers.terminal_handler import TerminalHandler


class CustomExceptionProtocol(Protocol):
    """
    Protocol defining the contract for Custom Exceptions.

    Attributes:
    - error (str): The error message.
    - type (Exception): The type of exception.
    - print_error (bool): Whether to print the error message.
    """
    error: str
    type: Exception
    print_error: bool

    def __init__(self, type: Exception, error: str, print_error: bool) -> None: ...


# Assuming you have already defined the TerminalColors class and CustomExceptionProtocol

class CustomException:
    """Used to modify how an exception is handled."""
    term = TerminalHandler(fore='red', style='bold')

    def __init__(self, type=Exception, error=None, print_error=False):
        self.error = error
        self.type = type
        if print_error:
            # Using the TerminalColors' print method to print in red
            self.term.print(self.error)
        else:
            raise self.type(self.error)


if __name__ == '__main__':
    exception1 = CustomException(error='This is a custom exception print', print_error=True)
    exception2 = CustomException(type=NotImplementedError, error='This is a custom exception raise', print_error=False)
