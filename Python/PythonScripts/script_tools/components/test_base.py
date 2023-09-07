import unittest
from abc import ABC, abstractmethod


class TestBase(ABC):
    @abstractmethod
    def test_basic_functionality(self):
        ...


if __name__ == '__main__':
    unittest.main()
