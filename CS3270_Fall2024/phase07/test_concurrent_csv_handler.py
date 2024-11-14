import pytest
from concurrent_csv_handler import ConcurrentCSVHandler
from pandas import DataFrame


@pytest.fixture
def mock_csv_file(tmp_path, monkeypatch):
    # Create a temporary CSV file for testing
    csv_path = tmp_path / "test_data.csv"
    csv_path.write_text("column1,column2\n10,20\n30,40\n50,60\n")

    # Monkeypatch Path to use the temporary file path
    monkeypatch.setattr("csv_handler.Path", lambda _: csv_path)
    return csv_path


@pytest.fixture
def concurrent_csv_handler(mock_csv_file):
    return ConcurrentCSVHandler(str(mock_csv_file))


def test_get_data_with_columns(concurrent_csv_handler):
    data = concurrent_csv_handler.get_data(columns=["column1", "column2"], start_row=0, end_row=2)
    assert isinstance(data, DataFrame)
    assert not data.empty
    assert "column1" in data.columns
    assert "column2" in data.columns


def test_get_data_with_filters(concurrent_csv_handler):
    filters = {"column1": ">15", "column2": "<50"}
    data = concurrent_csv_handler.get_data(filters=filters)
    assert isinstance(data, DataFrame)
    assert not data.empty
    assert all(data["column1"] > 15)
    assert all(data["column2"] < 50)