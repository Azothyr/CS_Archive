import builtins
from functools import wraps


class PrintOverride:
    def __enter__(self):
        self.original_print = builtins.print
        builtins.print = self.new_print

    def __exit__(self, exc_type, exc_val, exc_tb):
        builtins.print = self.original_print

    def new_print(self, *args, **kwargs):
        symbol = '-'
        num_times = 3
        self.original_print(symbol * num_times + args[0] + symbol * num_times, **kwargs)


def wrap_prints(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with PrintOverride():
            return func(*args, **kwargs)
    return wrapper


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
