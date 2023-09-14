

def format_dict_to_print(dictionary, key_wrapper="", val_wrapper=""):
    result = "\n".join([f"{key_wrapper}{k}{key_wrapper}: {val_wrapper}{v}{val_wrapper}"
                        for k, v in dictionary.items()])
    return result


def format_dict_with_index(dictionary, idx_wrapper="", val_wrapper=""):
    result = "\n".join([f"{idx_wrapper}{i}{idx_wrapper}: {val_wrapper}{v}{val_wrapper}"
                        for i, v in enumerate(dictionary, 1)])
    return result


def format_dict_to_list(dictionary, key_wrapper="", val_wrapper=""):
    result = [f"{key_wrapper}{k}{key_wrapper}: {val_wrapper}{v}{val_wrapper}"
              for k, v in dictionary.items()]
    return result


def format_dict_to_tuple(dictionary, key_wrapper="", val_wrapper=""):
    result = [(f"{key_wrapper}{k}{key_wrapper}", f"{val_wrapper}{v}{val_wrapper}")
              for k, v in dictionary.items()]
    return result
