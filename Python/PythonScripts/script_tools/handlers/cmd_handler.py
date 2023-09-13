import argparse


class CmdHandler:
    """
    CmdHandler is used to define and parse command-line arguments.

    Attributes:
    - parser (ArgumentParser): An instance of argparse.ArgumentParser.
    - args (Namespace): The parsed command-line arguments.

    Methods:
    - add_debug_argument(): Adds a debugging switch argument.
    - parse_arguments(): Parses the command-line arguments and sets the args attribute.
    - add_argument(*args, **kwargs): Adds an argument to the parser.
    """

    def __init__(self, description='DEFAULT COMMAND HANDLER'):
        self.parser = argparse.ArgumentParser(description=description)
        self.args = None

    def add_debug_argument(self):
        """Add a debug argument to the parser."""
        self.parser.add_argument("-d", "--debug", help="Enable debugging mode.", action="store_true")

    def parse_arguments(self):
        """Parse the command-line arguments."""
        self.args = self.parser.parse_args()

        # Check if debug mode is enabled
        if self.args and getattr(self.args, 'debug', False):
            print("Debugging mode enabled!")

    def add_argument(self, *args, **kwargs):
        """Add an argument to the parser."""
        self.parser.add_argument(*args, **kwargs)


if __name__ == "__main__":
    handler = CmdHandler(description="A custom command handler.")
    handler.add_debug_argument()
    handler.parse_arguments()
