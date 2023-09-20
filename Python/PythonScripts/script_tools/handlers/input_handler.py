"""
InputHandler Module
-------------------

This module provides the InputHandler class that offers a flexible way to handle
different kinds of user input, map them to specific actions, and validate them based on
predefined criteria.

Example:
    handler = InputHandler({
        'menu_options': {
            'validator': InputHandler._is_option,
            'actions': {
                '1': lambda: print("Option 1"),
                '2': lambda: print("Option 2"),
            },
            'error_message': 'Please select a valid option or hit Enter to exit.'
        }
    })
    handler.handle_input('menu_options', 'Choose an option (1-2): ')

Author: Zac Peterson
Created: 2023/09/19
"""

from typing import Callable, Dict, Union, Any

ActionDict = Dict[str, Callable[[], None]]
InputDetails = Dict[str, Union[Callable[[str, Dict[str, Any]], bool], ActionDict, str]]
InputMap = Dict[str, InputDetails]


class InputHandler:
    """
    InputHandler class for handling various user inputs.

    Attributes:
        input_map (InputMap): A dictionary that maps input types to their handling details.
    """

    def __init__(self, input_map: InputMap = None):
        """
        Initializes an InputHandler instance with an optional input map.

        Args:
            input_map (InputMap, optional): A map of input types to handling details. Defaults to an empty dict.
        """
        if input_map is None:
            input_map = {'text': {
                'validator': InputHandler._is_text,
                'error_message': 'Text input cannot be empty.'
            },
                'confirm': {
                    'validator': InputHandler._is_confirmation,
                    'actions': {
                        'yes': InputHandler.confirm_action,
                        'no': InputHandler.decline_action
                    },
                    'error_message': 'Please answer with "yes" or "no".'
                },
                'file': {
                    'validator': InputHandler._is_confirmation,
                    'actions': {
                        'yes': InputHandler.confirm_action,
                        'no': InputHandler.decline_action
                    },
                    'error_message': "The provided path does not exist.\nWould you like to create it?"
                                     " (yes/no):\n>>> "
                },
                'exit': {
                    'validator': InputHandler._wait_for_exit,
                    'actions': {"": InputHandler._exit
                                },
                    'error_message': "ERROR: This should never be displayed. Console exit condition broken."
                },
            }
        self.input_map = input_map

    @staticmethod
    def _wait_for_exit(value, _):
        """Private method to validate if the input is an exit command or empty."""
        return value.strip().lower() in [None, "", " ", "exit", "quit", "q"]

    @staticmethod
    def _exit():
        """Private method to validate if the input is an exit command or empty."""
        print("Console exit condition triggered.")
        exit(0)  # This will exit the program

    @staticmethod
    def _is_text(input_str, _):
        """
        Check if the given string is non-empty.

        Args:
            input_str (str): The input string to validate.

        Returns:
            bool: True if the input string is non-empty, False otherwise.
        """
        return bool(input_str.strip())

    @staticmethod
    def _is_confirmation(value, _):
        """Private method to validate if the input is a confirmation."""
        return value.strip().lower() in ["yes", "no"]

    @staticmethod
    def confirm_action():
        print("Confirmed!")

    @staticmethod
    def decline_action():
        print("Not confirmed!")

    @staticmethod
    def _is_option(value: str, input_details: InputDetails) -> bool:
        """
        Validates if the input is one of the valid actions or empty.

        Args:
            value (str): The user input value.
            input_details (InputDetails): A dictionary containing the input details.

        Returns:
            bool: True if the value matches one of the valid actions or is empty, False otherwise.
        """
        actions = input_details.get('actions', {})
        return value in actions.keys() or value == ""

    def handle_input(self, input_type: str, prompt: str):
        """
        Handles user input based on a specific input type and prompt.

        Args:
            input_type (str): The type of input to handle.
            prompt (str): The prompt to display to the user.
        """
        input_details = self.input_map.get(input_type, {})

        validator = input_details.get('validator', None)
        if not validator:
            print(f"No validator found for {input_type}.")
            return

        while True:
            user_input = input(prompt).strip().lower()

            if validator(user_input, input_details):
                actions = input_details.get('actions', {})
                action = actions.get(user_input, lambda *args, **kwargs: None)
                action()
                if user_input.lower() == "exit":
                    self._exit()
                break
            else:
                print(input_details['error_message'])
        return user_input


if __name__ == '__main__':
    # Example usage:
    def option_2() -> None:
        """A function to print a message when option 2 is selected."""
        print("Option 2 selected!")


    handler = InputHandler({
        'menu_options': {
            'validator': InputHandler._is_option,
            'actions': {
                '1': lambda: print("Option 1 selected!"),
                '2': option_2,
                '3': lambda: print("Option 3 selected!"),
                '4': lambda: print("Option 4 selected!"),
                # '5': lambda: print("Option 5 selected!"),
                'yes': lambda: print("Confirmed!"),
                'no': lambda: print("Not confirmed!")
            },
            'error_message': 'Please select a valid option or hit Enter to exit.'
        }
    })

    prompt_msg = 'Choose an option (1-5), "yes" or "no", or hit Enter to exit: '
    handler.handle_input('menu_options', prompt_msg)
