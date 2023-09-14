"""
str_basic_ops module

This module provides basic string operations for common string manipulations.
"""


def add_value_to_str(string: str, value, before=False, after=False, sep: str = "", new_line=False) -> str:
    """
        Adds a value to a string with optional placement and separation.

        Args:
        - string (str) -> str: The main string.
        - value (str) -> str: The value to add.
        - before (bool) -> str: If True, adds value before the string.
        - after (bool) -> str: If True, adds value after the string.
        - sep (str) -> str: Separator between the string and value.
        - new_line (bool) -> str: If True, adds a newline after the result.

        Returns:
        - str: The modified string.
        """
    if new_line:
        result = f"{value}{sep}{string}\n" if before else f"{string}{sep}{value}\n"\
            if after else f"{string}{sep}{value}\n"
    else:
        result = f"{value}{sep}{string}" if before else f"{string}{sep}{value}" if after else f"{string}{sep}{value}"
    return result


def upper(string: str) -> str:
    """
    Converts a string to uppercase.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - str: The string in uppercase.
    """
    return string.upper()


def lower(string: str) -> str:
    """
    Converts a string to lowercase.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - str: The string in lowercase.
    """
    return string.lower()


def capitalize(string: str) -> str:
    """
    Capitalizes the first character of a string.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - str: The string with its first character capitalized.
    """
    return string.capitalize()


def wrap(string: str, wrapper=()) -> str:
    """
    Wraps a string with the given wrapper.
    Args:
    - string (str) -> str: The input string.
    - wrapper (tuple) -> str: A tuple containing two strings to wrap the input string.
    Returns:
    - str: The wrapped string.
    """
    return f"{wrapper[0]}{string}{wrapper[1]}"


def replace(string: str, old, new) -> str:
    """
    Replaces occurrences of a substring within a string.
    Args:
    - string (str) -> str: The input string.
    - old (str) -> str: The substring to replace.
    - new (str) -> str: The substring to replace with.
    Returns:
    - str: The string with the replacements.
    """
    return string.replace(old, new)


def remove(string: str, value) -> str:
    """
    Removes all occurrences of a specified value from the string.
    Args:
    - string (str) -> str: The input string.
    - value (str) -> str: The value to remove.
    Returns:
    - str: The string with the value removed.
    """
    return string.replace(value, "")


def count(string: str, value) -> int:
    """
    Counts the occurrences of a specified value in the string.
    Args:
    - string (str) -> str: The input string.
    - value (str) -> str: The value to count.
    Returns:
    - int: Number of occurrences of the value.
    """
    return string.count(value)


def split(string: str, sep: str) -> list[str]:
    """
    Splits a string at every occurrence of the specified separator.
    Args:
    - string (str) -> str: The input string.
    - sep (str) -> str: The separator.
    Returns:
    - list of str: List of substrings.
    """
    return string.split(sep)


def join(string: list[str], sep: str) -> str:
    """
    Joins a list of strings using the specified separator.
    Args:
    - string (list of str) -> str: The list of strings.
    - sep (str) -> str: The separator.
    Returns:
    - str: The joined string.
    """
    return sep.join(string)


def strip(string: str, chars=None) -> str:
    """
    Removes leading and trailing characters.
    Args:
    - string (str) -> str: The input string.
    - chars (str, optional) -> str: Characters to strip. Default is None, which strips whitespace.
    Returns:
    - str: The stripped string.
    """
    return string.strip(chars)


def lstrip(string: str, chars=None) -> str:
    """
    Removes leading characters from the string.
    Args:
    - string (str) -> str: The input string.
    - chars (str, optional) -> str: Characters to remove. Default is None, which strips whitespace.
    Returns:
    - str: The string with leading characters removed.
    """
    return string.lstrip(chars)


def rstrip(string: str, chars=None) -> str:
    """
    Removes trailing characters from the string.
    Args:
    - string (str) -> str: The input string.
    - chars (str, optional) -> str: Characters to remove. Default is None, which strips whitespace.
    Returns:
    - str: The string with trailing characters removed.
    """
    return string.rstrip(chars)


def ljust(string: str, width: int, fillchar:  str = " ") -> str:
    """
    Left-justifies a string in a field of a given width.
    Args:
    - string (str) -> str: The input string.
    - width (int) -> str: Field width.
    - fillchar (str, optional) -> str: Padding character. Default is space.
    Returns:
    - str: The left-justified string.
    """
    return string.ljust(width, fillchar)


def rjust(string: str, width: int, fillchar:  str = " ") -> str:
    """
    Right-justifies a string in a field of a given width.
    Args:
    - string (str) -> str: The input string.
    - width (int) -> str: Field width.
    - fillchar (str, optional) -> str: Padding character. Default is space.
    Returns:
    - str: The right-justified string.
    """
    return string.rjust(width, fillchar)


def center(string: str, width: int, fillchar:  str = " ") -> str:
    """
    Centers a string in a field of a given width.
    Args:
    - string (str) -> str: The input string.
    - width (int) -> str: Field width.
    - fillchar (str, optional) -> str: Padding character. Default is space.
    Returns:
    - str: The centered string.
    """
    return string.center(width, fillchar)


def zfill(string: str, width: int) -> str:
    """
    Pads a string on the left with zeros.
    Args:
    - string (str) -> str: The input string.
    - width (int) -> str: Total width of the string after padding.
    Returns:
    - str: The padded string.
    """
    return string.zfill(width)


def swapcase(string: str) -> str:
    """
    Swaps the case of the string characters.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - str: The string with swapped cases.
    """
    return string.swapcase()


def title(string: str) -> str:
    """
    Converts the first character of each word to uppercase.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - str: The titled string.
    """
    return string.title()


def isalnum(string: str) -> bool:
    """
    Checks if the string consists only of alphanumeric characters.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is alphanumeric, False otherwise.
    """
    return string.isalnum()


def isalpha(string: str) -> bool:
    """
    Checks if the string consists only of alphabetic characters.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is alphabetic, False otherwise.
    """
    return string.isalpha()


def isdigit(string: str) -> bool:
    """
    Checks if the string consists only of digits.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is digits, False otherwise.
    """
    return string.isdigit()


def islower(string: str) -> bool:
    """
    Checks if the string consists only of lowercase characters.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is lowercase, False otherwise.
    """
    return string.islower()


def isupper(string: str) -> bool:
    """
    Checks if the string consists only of uppercase characters.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is uppercase, False otherwise.
    """
    return string.isupper()


def isspace(string: str) -> bool:
    """
    Checks if the string consists only of whitespace characters.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is whitespace, False otherwise.
    """
    return string.isspace()


def istitle(string: str) -> bool:
    """
    Checks if the string is titlecased.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - bool: True if string is titlecased, False otherwise.
    """
    return string.istitle()


def startswith(string: str, prefix) -> bool:
    """
    Checks if the string starts with the specified prefix.
    Args:
    - string (str) -> str: The input string.
    - prefix (str) -> str: The prefix.
    Returns:
    - bool: True if string starts with prefix, False otherwise.
    """
    return string.startswith(prefix)


def endswith(string: str, suffix) -> bool:
    """
    Checks if the string ends with the specified suffix.
    Args:
    - string (str) -> str: The input string.
    - suffix (str) -> str: The suffix.
    Returns:
    - bool: True if string ends with suffix, False otherwise.
    """
    return string.endswith(suffix)


def find(string: str, value: str) -> int:
    """
    Finds the first occurrence of the specified value in the string.
    Args:
    - string (str) -> str: The input string.
    - value (str) -> str: The value to search for.
    Returns:
    - int: The index of the first occurrence of the value, or -1 if not found.
    """
    return string.find(value)


def rfind(string: str, value: str) -> int:
    """
    Finds the last occurrence of the specified value in the string.
    Args:
    - string (str) -> str: The input string.
    - value (str) -> str: The value to search for.
    Returns:
    - int: The index of the last occurrence of the value, or -1 if not found.
    """
    return string.rfind(value)


def index(string: str, value: str) -> int:
    """
    Finds the first occurrence of the specified value in the string.
    Args:
    - string (str) -> str: The input string.
    - value (str) -> str: The value to search for.
    Returns:
    - int: The index of the first occurrence of the value.
    Raises:
    - ValueError: If the value is not found.
    """
    return string.index(value)


def rindex(string: str, value: str) -> int:
    """
    Finds the last occurrence of the specified value in the string.
    Args:
    - string (str) -> str: The input string.
    - value (str) -> str: The value to search for.
    Returns:
    - int: The index of the last occurrence of the value.
    Raises:
    - ValueError: If the value is not found.
    """
    return string.rindex(value)


def splitlines(string: str) -> list[str]:
    """
    Splits the string at line breaks.
    Args:
    - string (str) -> str: The input string.
    Returns:
    - list of str: List of substrings.
    """
    return string.splitlines()


def partition(string: str, sep: str) -> tuple[str, str, str]:
    """
    Splits the string at the first occurrence of the specified separator.
    Args:
    - string (str) -> str: The input string.
    - sep (str) -> str: The separator.
    Returns:
    - tuple of str: The split string.
    """
    return string.partition(sep)


def rpartition(string: str, sep: str) -> tuple[str, str, str]:
    """
    Splits the string at the last occurrence of the specified separator.
    Args:
    - string (str) -> str: The input string.
    - sep (str) -> str: The separator.
    Returns:
    - tuple of str: The split string.
    """
    return string.rpartition(sep)
