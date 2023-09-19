import ast


def _prompt_return():
    return_prompt = ('\nPress 1 for multi-line return\n'
                     'Press 2 for single-line return\n'
                     'press 3 for joined return\n'
                     'Press enter to go back\n\n'
                     '>>')

    return input(return_prompt)


def _prompt_tool():
    tool_prompt = ('\nPress 1 to create a list from one or more inputs\n'
                   'Press 2 to split a string into a list\n'
                   'Press enter to quit\n\n'
                   '>>')

    return input(tool_prompt)


def _get_return(return_choice):
    return_options = {
        '1': print_list_values,
        '2': print_list,
        '3': print_joined_list
    }

    return_format = return_options.get(return_choice)

    if not return_format:
        print("\nInvalid return format choice!")
        return None

    return return_format


def _get_tool(tool_choice):
    tool_options = {
        '1': ls_multi_inputs,
        '2': ls_split_input,
        '': exit_program
    }

    tool = tool_options.get(tool_choice)
    if tool is exit_program:
        return exit_program, None
    else:
        return_type = _get_return(_prompt_return())
        return tool, return_type


def print_joined_list(lyst):
    join_value = input('\nEnter the value you would like to have the list joined with\nor press enter for none\n\n>>')
    print(f"Joining with: '{join_value}'")
    joined_string = join_value.join(lyst)
    print(f"Joined string length: {len(joined_string)}")
    print(joined_string)


def print_list(lyst):
    print(lyst)


def print_list_values(lyst):
    for item in lyst:
        print(item)


def ls_split_input(value=None, splitter=None):
    if value is None:
        value = input('\nEnter string you would like to split: ')
    if splitter is None:
        splitter = input('\nEnter character you would like to split at: ')
    return value.split(splitter)


def ls_multi_inputs(value=None):
    result = []

    if value is not None:  # If an initial value is provided
        result.append(value)

    while True:  # Keep looping until broken out of
        value = input("Enter a list or single value or press enter to finish: ").strip()

        if not value:  # If the user just hits Enter (empty string), break out of the loop
            break

        # Check if the input starts with [ and ends with ] which might indicate a list
        if value.startswith('[') and value.endswith(']'):
            try:
                extracted_list = ast.literal_eval(value)
                if isinstance(extracted_list, list):
                    result.extend(extracted_list)
            except ValueError:
                print("\nCouldn't parse the provided list. Try entering values one by one.")
        else:  # If it's just a single value
            result.append(value)

    return result


def exit_program():
    print("\nExiting program.")
    exit()


def main():
    while True:
        tool, print_type = _get_tool(_prompt_tool())
        if tool:
            result = tool()
            print_type(result)


if __name__ == '__main__':
    main()
    # file = 'C:\\GitRepos\\Scripts_Private\\Python\\PythonScripts\\result.txt'
    # with open(file, 'r') as f:
    #     lines = f.readlines()
    #
    # assignment = []
    # date = []
    # for line in lines:
    #     line = line.strip()
    #     if line[-7] == " ":
    #         assignment.append(line[:-7])
    #         date.append(line[-6:])
    #     else:
    #         assignment.append(line[:-6])
    #         date.append(line[-5:])
    #
    # for _homework in assignment:
    #     print(_homework)
    # for _date in date:
    #     print(_date)
