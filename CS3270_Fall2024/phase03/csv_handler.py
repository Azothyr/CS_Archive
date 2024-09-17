from pandas import DataFrame, read_csv
from pathlib import Path


class CSVHandler:
    """
    CSVHandler class for reading CSV files and returning the data as a DataFrame.

    Attributes:
        file_path (str | Path): Path to the CSV file to read.

    Methods:
        read_data(): Reads the data from the CSV file and returns it as a DataFrame.
    """

    def __init__(self, file_path: str | Path):
        self.file_path = file_path

    def read_data(self) -> DataFrame:
        """
        Reads the data from the CSV file and returns it as a DataFrame.

        Returns:
            DataFrame: Dataframe of the CSV data.
        """
        file = Path(self.file_path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            data = read_csv(self.file_path)
        except Exception as e:
            raise Exception(f"Error reading file: {e}")

        return data
