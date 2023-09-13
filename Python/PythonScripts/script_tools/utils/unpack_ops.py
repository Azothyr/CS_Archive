from typing import overload, Union


@overload
def process_args(data: list) -> str: ...


@overload
def process_args(data: list) -> list: ...


def process_args(data: list) -> Union[str, list]:
    if len(data) == 1:
        return data[0]
    else:
        return data
