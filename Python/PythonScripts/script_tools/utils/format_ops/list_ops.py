

def format_list_to_print(lyst):
    result = "\n".join([f"{i}: {v}" for i, v in enumerate(lyst)])
    return result


def format_list_with_index(lyst):
    result = "\n".join([f"{i}: {v}" for i, v in enumerate(lyst, 1)])
    return result
