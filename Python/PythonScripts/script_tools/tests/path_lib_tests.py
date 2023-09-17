import pytest
import os
from ..config.path_library_Manager import PathLib


@pytest.fixture
def path_lib():
    return PathLib().get_library()


# 1. Test that for a given key, the returned path exists.
@pytest.mark.parametrize("key", ["user", "documents", "custom_scripts", "maya_scripts",
                                 "tools", "tools_components", "tools_tests", "maya_ui", "maya_components"]
                         )  # Add keys that you expect to always exist
def test_path_exists(path_lib, key):
    assert os.path.exists(path_lib[key])


# 2. Test that for a given key, the returned path matches a certain structure.
# For this example, let's test that the "user" key always returns a path that ends with the user's home directory.
def test_user_path_structure(path_lib):
    expected_path = os.path.expanduser("~")
    assert path_lib["user"].endswith(expected_path)


# 3. Test that certain keys always return a specific value.
@pytest.mark.parametrize("key, expected_path", [
    ("maya", os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "maya_scripts")),
    ("azothyr", os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "azothyr_tools")),
    ("tools_components", os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "azothyr_tools",
                                      "components")),
    ("tools_tests", os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "azothyr_tools", "tests")),
    ("maya_ui", os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "maya_scripts", "ui")),
    ("maya_components", os.path.join(os.path.expanduser("~"), "Documents", "custom_scripts", "maya_scripts",
                                     "components"))
])
def test_key_value_match(path_lib, key, expected_path):
    assert path_lib[key] == expected_path
