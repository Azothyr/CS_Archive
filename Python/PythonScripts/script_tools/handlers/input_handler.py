# Desc: A class that handles user input.
import keyboard
import pyperclip


class InputHandler:

    @staticmethod
    def _handle_backspace(user_input):
        user_input = user_input[:-1]
        print("\b \b", end="", flush=True)
        return user_input

    @staticmethod
    def _handle_ctrl_z(user_input, history):
        if history:
            last_input = history.pop()
            user_input = last_input
            # Printing spaces to 'overwrite' previous content and then moving back.
            print("\b" * len(user_input) + " " * len(user_input) + "\b" * len(user_input), end="", flush=True)
        return user_input

    @staticmethod
    def _handle_ctrl_c(user_input):
        print("\nExiting due to user request.")
        exit(0)

    @staticmethod
    def _handle_ctrl_v(user_input):
        paste_content = pyperclip.paste()
        user_input += paste_content
        print(paste_content, end="", flush=True)
        return user_input

    @staticmethod
    def __with_escape_key(prompt, escape_key, allow_empty, error_message):
        key_actions = {
            'backspace': InputHandler._handle_backspace,
            'ctrl+z': lambda _user_input: InputHandler._handle_ctrl_z(_user_input, input_history),
            'ctrl+c': InputHandler._handle_ctrl_c,
            'ctrl+v': InputHandler._handle_ctrl_v,
            # Add more key-specific actions here
        }
        print(prompt, end="", flush=True)  # Flush ensures that the prompt is displayed
        user_input = ""
        input_history = []  # To keep track of inputs for the undo function
        while True:
            key_event = keyboard.read_event()
            key_name = key_event.name
            event_type = key_event.event_type
            if event_type == 'down':
                if key_name in key_actions:
                    user_input = key_actions[key_name](user_input)
                elif key_name == escape_key:
                    print("\nExiting due to user request.")
                    exit(0)
                elif key_name == 'enter':
                    break
                elif len(key_name) == 1:
                    input_history.append(user_input)  # Save current state before appending new char
                    user_input += key_name
                    print(key_name, end="", flush=True)
        return user_input.strip() or ("" if allow_empty else print("\n" + error_message))

    @staticmethod
    def __without_escape_key(prompt, allow_empty, error_message):
        while True:
            user_input = input(prompt)
            if user_input.strip():  # Check if the input is non-empty
                return user_input
            elif allow_empty:
                return ""
            else:
                print(error_message)

    @staticmethod
    def get_text_input(prompt: str = "Please enter something: ", allow_empty: bool = False,
                       escape_key: str | bool | None = None,
                       error_message: str = "Input should not be empty. Please try again."):
        """
        Prompt the user for input and return it.
        Keyword Args:
        - prompt (str): The message to display to the user.
        - allow_empty (bool): Whether to allow empty input.
        - escape_key (str): The key to press to exit the program.
        - error_message (str): The message to display to the user if they enter empty input.
        Returns:
        - str: The input from the user.
        """
        if escape_key is False or escape_key is None:
            return InputHandler.__without_escape_key(prompt, allow_empty, error_message)
        else:
            return InputHandler.__with_escape_key(prompt, escape_key, allow_empty,
                                                  error_message="Input should not be empty. Please try again."
                                                                " Or hit Esc to exit.")
