import pytest
from csv_handler import CSVHandler
import pandas as pd

# Mock CSV data for testing
MOCK_CSV_CONTENT = """col1,col2
1,2
3,4
5,6
7,8
9,10
"""


@pytest.fixture
def mock_csv_file(tmpdir):
    # Create a temporary CSV file used by pytest for the lifetime of the test
    csv_file = tmpdir.join("test.csv")
    # Write the constant MOCK_CSV_CONTENT to the file
    with open(csv_file, "w") as file:
        file.write(MOCK_CSV_CONTENT)
    return csv_file


def test_read_data_in_chunks(mock_csv_file):
    handler = CSVHandler(mock_csv_file)
    chunks = list(handler.read_data_in_chunks(chunk_size=2))

    assert len(chunks) == 3  # There are 5 rows in the CSV file, so 2 chunks of 2 rows and 1 chunk of 1 row
    assert isinstance(chunks[0], pd.DataFrame)
    assert len(chunks[0]) == 2  # First chunk should have 2 rows


def test_file_not_found():
    handler = CSVHandler("non_existent_file.csv")
    with pytest.raises(FileNotFoundError):
        list(handler.read_data_in_chunks())


def test_read_data_in_chunks_exception(monkeypatch, mock_csv_file):
    # Simulate an exception during file reading
    def mock_read_csv(*args, **kwargs):
        raise Exception("Error reading file")

    # Replace the read_csv function with the mock function
    monkeypatch.setattr("csv_handler.read_csv", mock_read_csv)

    # Initialize the CSVHandler with the mock CSV file
    handler = CSVHandler(mock_csv_file)

    with pytest.raises(Exception, match="Error reading file"):
        list(handler.read_data_in_chunks())
