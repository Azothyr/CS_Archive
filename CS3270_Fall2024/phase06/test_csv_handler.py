import pytest
import pandas as pd
from csv_handler import CSVHandler

# Mock CSV data for testing
MOCK_CSV_CONTENT = """humidity,wind_mph,temp
24,8.3,70
94,6.9,75
29,9.4,65
61,7.4,80
89,8.1,85
"""


@pytest.fixture
def mock_csv_file(tmpdir):
    """
    Create a temporary CSV file for testing, using the MOCK_CSV_CONTENT.
    """
    csv_file = tmpdir.join("test.csv")
    with open(csv_file, "w") as file:
        file.write(MOCK_CSV_CONTENT)
    return csv_file


def test_read_data_in_chunks(mock_csv_file):
    """
    Test reading the CSV file in chunks using the CSVHandler.
    """
    handler = CSVHandler(mock_csv_file)
    chunks = list(handler._read_data_in_chunks(chunk_size=2))

    assert len(chunks) == 3  # 5 rows, chunk size 2 => 3 chunks (2 + 2 + 1)
    assert isinstance(chunks[0], pd.DataFrame)
    assert len(chunks[0]) == 2  # First chunk should have 2 rows
    assert len(chunks[-1]) == 1  # Last chunk should have 1 row


def test_read_data_in_chunks_exception(monkeypatch, mock_csv_file):
    """
    Simulate an exception during file reading and verify that it is handled properly.
    """

    def mock_read_csv(*args, **kwargs):
        raise Exception("Error reading file")

    monkeypatch.setattr("csv_handler.read_csv", mock_read_csv)

    handler = CSVHandler(mock_csv_file)
    with pytest.raises(Exception, match="Error reading file"):
        list(handler._read_data_in_chunks())


def test_column_selection(mock_csv_file):
    """
    Test if `get_data` correctly filters the specified columns.
    """
    handler = CSVHandler(mock_csv_file)
    result = handler.get_data(columns=['humidity', 'wind_mph'])

    # Verify the result contains only the specified columns
    assert list(result.columns) == ['humidity', 'wind_mph']
    assert len(result) == 5  # Should have 5 rows as in the CSV


def test_row_range_selection(mock_csv_file):
    """
    Test row range selection, ensuring rows between the specified start and end are returned.
    """
    handler = CSVHandler(mock_csv_file)
    result = handler.get_data(start_row=1, end_row=3)

    # Check the returned data contains the correct number of rows and correct data
    assert len(result) == 2  # Only rows between index 1 and 3 (exclusive)
    assert result.iloc[0]['humidity'] == 94  # First row in the range should be row 1
    assert result.iloc[1]['humidity'] == 29  # Second row in the range should be row 2


def test_filter_application(mock_csv_file):
    """
    Test filtering functionality based on conditions provided in the filters parameter.
    """
    handler = CSVHandler(mock_csv_file)
    result = handler.get_data(filters={'humidity': '>50', 'wind_mph': '<8'})

    # Verify that only rows matching the filters are returned
    assert len(result) == 2  # Only two rows should match humidity > 50 and wind_mph < 8
    assert all(result['humidity'] > 50)
    assert all(result['wind_mph'] < 8)


def test_filter_application_invalid_column(mock_csv_file, caplog):
    """
    Test filtering on a non-existent column and ensure it is handled gracefully with a warning.
    """
    handler = CSVHandler(mock_csv_file)
    result = handler.get_data(filters={'nonexistent_column': '==5'})

    # Expect the result to still be a valid DataFrame with all rows (since the filter should be skipped)
    assert len(result) == 5  # All rows should be returned since the filter was invalid
    assert "Column 'nonexistent_column' not found in data. Skipping filter." in caplog.text


def test_file_not_found():
    """
    Test handling of non-existent file error.
    """
    handler = CSVHandler("non_existent_file.csv")
    with pytest.raises(FileNotFoundError):
        list(handler._read_data_in_chunks())
