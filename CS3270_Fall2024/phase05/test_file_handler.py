import pytest
from .file_handler import FileHandler
from PyQt5.QtWidgets import QFileDialog
import os


def test_get_default_directory(monkeypatch):
    # Mock the os.path.exists function to return True
    monkeypatch.setattr(os.path, "exists", lambda x: True)
    handler = FileHandler()
    assert handler._get_default_directory() == "../resources"

    # Mock the os.path.exists function to return False
    monkeypatch.setattr(os.path, "exists", lambda x: False)
    handler = FileHandler()
    assert handler._get_default_directory() == os.path.expanduser("~")


def test_retrieve_file(monkeypatch):
    handler = FileHandler()

    # Mock QFileDialog.getOpenFileName to return a valid file path
    monkeypatch.setattr(QFileDialog, "getOpenFileName", lambda *args, **kwargs: ("test.csv", None))
    file_path = handler.retrieve_file()
    assert file_path == "test.csv"

    # Mock QFileDialog.getOpenFileName to simulate no file selected
    monkeypatch.setattr(QFileDialog, "getOpenFileName", lambda *args, **kwargs: ("", None))
    with pytest.raises(FileNotFoundError):
        handler.retrieve_file()
