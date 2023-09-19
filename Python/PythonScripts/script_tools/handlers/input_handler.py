class InputHandler:

    def __init__(self):
        # Dynamic mapping of input types to their handlers.
        # By default, only the 'text' type is mapped to the get_text_input method.
        self.input_map = {
            'text': self.get_text_input
        }

    def add_input_handler(self, input_type, handler):
        """Add a new handler for a specific input type."""
        self.input_map[input_type] = handler

    @staticmethod
    def __default_use_case(prompt, allow_empty, error_message):
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
                       error_message: str = "Input should not be empty. Please try again."):
        return InputHandler.__default_use_case(prompt, allow_empty, error_message)

    def handle_input(self, input_type, *args, **kwargs):
        """Dynamically handle input based on the type."""
        match input_type:
            case self.input_map.get(input_type, None):  # Check if the input_type exists in the mapping
                return self.input_map[input_type](*args, **kwargs)
            case _:  # Default case
                print(f"No handler found for {input_type}. Using the default handler.")
                return self.get_text_input(*args, **kwargs)