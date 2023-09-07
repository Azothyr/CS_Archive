def get_user_input(prompt="Please enter something: "):
    """
    Prompt the user for input and return it.
    Args:
    - prompt (str): The message to display to the user.
    Returns:
    - str: The input from the user.
    """
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Check if the input is non-empty
            return user_input
        print("Input should not be empty. Please try again.")


if __name__ == "__main__":
    # Demo usage
    data = get_user_input("Enter your name: ")
    print(f"Hello, {data}!")
