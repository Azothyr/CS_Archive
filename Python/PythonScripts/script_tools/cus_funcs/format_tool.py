def format_dict_to_print(dictionary, symbol_around_k="", symbol_around_v=""):
    result = "\n".join([f"{symbol_around_k}{k}{symbol_around_k}: {symbol_around_v}{v}{symbol_around_v}"
                        for k, v in dictionary.items()])
    return result


def format_dict_with_index(dictionary, symbol_around_i="", symbol_around_v=""):
    result = "\n".join([f"{symbol_around_i}{i}{symbol_around_i}: {symbol_around_v}{v}{symbol_around_v}"
                        for i, v in enumerate(dictionary, 1)])
    return result


def format_dict_to_list(dictionary, symbol_around_k="", symbol_around_v=""):
    result = [f"{symbol_around_k}{k}{symbol_around_k}: {symbol_around_v}{v}{symbol_around_v}"
              for k, v in dictionary.items()]
    return result


def format_dict_to_tuple(dictionary, symbol_around_k="", symbol_around_v=""):
    result = [(f"{symbol_around_k}{k}{symbol_around_k}", f"{symbol_around_v}{v}{symbol_around_v}")
              for k, v in dictionary.items()]
    return result


def format_list_to_print(lyst):
    result = "\n".join([f"{i}: {v}" for i, v in enumerate(lyst)])
    return result


def format_list_with_index(lyst):
    result = "\n".join([f"{i}: {v}" for i, v in enumerate(lyst, 1)])
    return result
