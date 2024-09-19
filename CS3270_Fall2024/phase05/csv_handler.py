from pandas import DataFrame, read_csv
from pathlib import Path
import logging as log


class CSVHandler:
    """
    CSVHandler class for reading CSV files and returning the data as a DataFrame in chunks.

    Attributes:
        file_path (str | Path): Path to the CSV file to read.

    Methods:
        read_data_in_chunks(): Reads the data from the CSV file in chunks using a generator.
    """

    def __init__(self, file_path: str | Path):
        self.file_path = file_path

    def read_data_in_chunks(self, chunk_size: int = 1000):
        """
        Reads the data from the CSV file in chunks using a generator.

        Parameters:
            chunk_size (int): Number of rows per chunk to read (default is 1000).

        Yields:
            DataFrame: Chunk of the CSV data.
        """
        file = Path(self.file_path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}\n")

        try:
            log.info(f"Reading file: {self.file_path}")
            for chunk in read_csv(self.file_path, chunksize=chunk_size):
                yield chunk
        except Exception as e:
            log.error(f"Error reading file: {e}")
            raise
