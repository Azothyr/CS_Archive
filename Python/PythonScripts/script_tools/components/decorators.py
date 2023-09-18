"""
decorators.py
-------------

This module provides various utility decorators to be used across the application.
"""


def singleton(cls):
    """
    A decorator that turns a class into a Singleton class. This ensures that only
    one instance of the class is ever created. If the class has been instantiated
    before, the previously created instance is returned.

    Args:
        cls (type): The class to be decorated.

    Returns:
        instance: The single instance of the decorated class.

    Usage:
        @singleton
        class MyClass:
            ...
    """
    instances = {}

    def get_instance(*args, **kwargs):
        """
        Creates or returns the single instance of the decorated class.
        """
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
