"""
decorators.py
-------------

This module provides various utility decorators to be used across the application.
"""


def singleton(cls):
    """
    A decorator that turns a class into a Singleton class.
    """
    class SingletonWrapper(cls):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(SingletonWrapper, cls).__new__(cls)
                # Now, __init__ will be called on the created instance
                cls._instance.__initialized = False
            return cls._instance

        def __init__(self, *args, **kwargs):
            if not self.__initialized:
                super(SingletonWrapper, self).__init__(*args, **kwargs)
                self.__initialized = True

        @classmethod
        def get_instance(cls, *args, **kwargs):
            return cls(*args, **kwargs)

        @classmethod
        def has_instance(cls):
            return cls._instance is not None

    SingletonWrapper.__name__ = cls.__name__
    return SingletonWrapper

