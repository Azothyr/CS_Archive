import pytest
import json
from pathlib import Path
from script_tools.components.json_config_manager_base import JSONConfigManager

# Define the path for your test JSON file
TEST_JSON_FILE = Path("../Scripts_Private/Python/PythonScripts/script_tools/tests/test_config.json")


@pytest.fixture(scope="module")
def setup_test_json_file():
    """Set up a test JSON file before testing and remove it after testing."""
    data = {
        "level1": {
            "level2": {
                "level3": "value"
            }
        },
        "root_key": "root_value"
    }

    # Create parent directories if they don't exist
    TEST_JSON_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write data to the test JSON file
    TEST_JSON_FILE.write_text(json.dumps(data))
    yield  # This line is where the testing functions start running
    # Clean up after testing
    TEST_JSON_FILE.unlink()


@pytest.mark.usefixtures("setup_test_json_file")
class TestJSONConfigManager:

    def test_read_config(self):
        manager = JSONConfigManager(TEST_JSON_FILE)
        result = manager.read_config()
        assert result["root_key"] == "root_value"
        assert result["level1"]["level2"]["level3"] == "value"

    def test_set(self):
        manager = JSONConfigManager(TEST_JSON_FILE)
        manager.set("new_key", "new_value")
        assert manager.get("new_key") == "new_value"

    @pytest.mark.parametrize(
        "key, value",
        [
            ("level1.level2.level3", "new_value"),
            ("root_key", "updated_root_value"),
        ],
        ids=[
            "Test nested set on level3",
            "Test set on root key"
        ]
    )
    def test_set_nested(self, key, value):
        manager = JSONConfigManager(TEST_JSON_FILE)
        manager.set(key, value)
        assert manager.get(key) == value

    def test_get_nonexistent_key(self):
        manager = JSONConfigManager(TEST_JSON_FILE)
        result = manager.get("nonexistent_key")
        assert result is None

    def test_set_nested_dictionary(self):
        manager = JSONConfigManager(TEST_JSON_FILE)
        new_data = {"nested_key": "nested_value"}
        manager.set("level1.level2", new_data)
        assert manager.get("level1.level2.nested_key") == "nested_value"
        assert manager.get("level1.level2.level3") is None

    def test_nonexistent_file_init(self):
        with pytest.raises(FileNotFoundError):
            JSONConfigManager("nonexistent.json")

    def test_set_all_nested(self):
        manager = JSONConfigManager(TEST_JSON_FILE)
        manager.set_all_nested("new_value")
        config_data = manager.read_config()
        assert self.check_all_values(config_data, "new_value")

    @staticmethod
    def check_all_values(data, check_value):
        for key, value in data.items():
            if isinstance(value, dict):
                # Call the static method directly instead of trying to call it on the dictionary
                if not TestJSONConfigManager.check_all_values(value, check_value):
                    return False
            elif value != check_value:
                return False
        return True

    def test_logging_verbose(self, capfd):
        manager = JSONConfigManager(TEST_JSON_FILE, verbose=True)
        manager.set("key", "value")
        captured = capfd.readouterr()
        assert f"Successfully read JSON file: {TEST_JSON_FILE}" in captured.out
        assert f"Successfully wrote to JSON file: {TEST_JSON_FILE}" in captured.out
