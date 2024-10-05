from pandas import DataFrame, read_csv, concat
import logging as log
from pathlib import Path
from functools import reduce


class CSVHandler:
    """
    CSVHandler class for reading and processing CSV files in chunks with optional filtering,
    column selection, and row range handling.

    Attributes:
        file_path (str): Path to the CSV file to be read.

    Methods:
        _read_data_in_chunks(chunk_size: int):
            Private method that reads the CSV file in chunks using a generator.

        _validate_columns(chunk: DataFrame, columns: list[str]) -> list[str]:
            Helper method to validate if the requested columns exist in the chunk.

        _apply_filters(chunk: DataFrame, filters: dict) -> DataFrame:
            Helper method that applies user-defined filters on a DataFrame chunk.

        get_data(columns: list[str] = None, start_row: int = None,
                 end_row: int = None, filters: dict = None) -> DataFrame:
            Public method that processes the CSV data based on user input for
            columns, rows, and filtering conditions.
    """

    def __init__(self, file_path: str):
        """
        Initializes CSVHandler with the path to the CSV file.

        Parameters:
            file_path (str): Path to the CSV file to read.
        """
        self.file_path = file_path
        self.missing_columns_logged = False  # Track if we've already logged missing columns

    def _read_data_in_chunks(self, chunk_size: int = 1000) -> DataFrame:
        """
        Private method to read data from the CSV file in chunks using a generator.

        Parameters:
            chunk_size (int): Number of rows per chunk (default is 1000).

        Yields:
            DataFrame: A chunk of the CSV data as a DataFrame.
        """
        file = Path(self.file_path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}/n")

        try:
            log.info(f"Reading file: {self.file_path}")
            for chunk in read_csv(self.file_path, chunksize=chunk_size):
                yield chunk
        except Exception as e:
            log.error(f"Error reading file: {e}")
            raise e

    def _validate_columns(self, chunk: DataFrame, columns: list[str]) -> list[str]:
        """
        Helper method to validate the existence of user-specified columns in the chunk.

        Parameters:
            chunk (DataFrame): The current chunk of data.
            columns (list[str]): List of columns to validate.

        Returns:
            list[str]: A list of valid column names that exist in the chunk.

        Logs a warning if any of the requested columns are missing from the chunk.
        """
        valid_columns = list(filter(lambda col: col in chunk.columns, columns))
        missing_columns = [col for col in columns if col not in valid_columns]

        if missing_columns and not self.missing_columns_logged:
            log.warning(f"Columns {missing_columns} not found in data.")
            self.missing_columns_logged = True  # Only log missing columns once

        return valid_columns

    def _apply_filters(self, chunk: DataFrame, filters: dict) -> DataFrame:
        """
        Helper method to apply user-defined filtering conditions on a DataFrame chunk.

        Parameters:
            chunk (DataFrame): The current chunk of data.
            filters (dict): A dictionary where keys are column names and values are filter conditions (e.g., '>50').

        Returns:
            DataFrame: The filtered chunk of data.

        Filters are applied row by row. Valid conditions include:
        - Null or empty conditions are skipped.
        - Greater than (>): Example, 'humidity > 50'
        - Greater than or equal to (>=): Example, 'temperature_fahrenheit >= 70'
        - Less than (<): Example, 'wind_mph < 10'
        - Less than or equal to (<=): Example, 'precip_in <= 35'
        - Equal to (==): Example, 'condition_text == "Clear"'
        - Starts with (start=): Example, 'city start= Lond'
        - Ends with (end=): Example, 'city end= on'
        - Contains (contains=): Example, 'city contains= on'
        - Invalid conditions are skipped with a warning.
        """
        def apply_condition(row, column, condition):
            try:
                if not condition:
                    return True
                if ">" in condition:
                    if "=" in condition:
                        value = float(condition.split(">=")[1]) if ">=" in condition else\
                            float(condition.split("=>")[1])
                        return row[column] >= value
                    value = float(condition.split(">")[1])
                    return row[column] > value
                elif "<" in condition:
                    if "=" in condition:
                        value = float(condition.split("<=")[1]) if "<=" in condition\
                            else float(condition.split("=<")[1])
                        return row[column] <= value
                    value = float(condition.split("<")[1])
                    return row[column] < value
                elif "==" in condition:
                    value = condition.split("==")[1]
                    return row[column] == value
                elif "start=" in condition:
                    value = condition.split("start=")[1]
                    return row[column].lower().startswith(value)
                elif "end=" in condition:
                    value = condition.split("end=")[1]
                    return row[column].lower().endswith(value)
                elif "contains=" in condition:
                    value = condition.split("contains=")[1]
                    return value.lower() in row[column].lower()
                else:
                    raise ValueError(condition)
            except (IndexError, ValueError) as e:
                log.error(f"Error processing filter '{condition}' for column '{column}': {e}")
                return False

        for column, condition in filters.items():
            if column not in chunk.columns:
                if not self.missing_columns_logged:
                    log.warning(f"Column '{column}' not found in data. Skipping filter.")
                    self.missing_columns_logged = True  # Only log missing columns once
                continue

            # Use filter to apply condition row by row
            chunk = chunk[chunk.apply(lambda row: apply_condition(row, column, condition), axis=1)]

        return chunk

    def get_data(self, columns: list[str] | None = None, start_row: int | None = None, end_row: int | None = None,
                 filters: dict | None = None) -> DataFrame:
        """
        Public method to retrieve and process data based on user inputs for columns, row ranges, and filters.

        Parameters:
            columns (list[str]): List of column names to retrieve (default is None, retrieves all columns).
            start_row (int): Row number to start processing from (default is None, starts from the first row).
            end_row (int): Row number to stop processing at (default is None, processes until the end).
            filters (dict): Optional filtering criteria for specific columns (default is None).

        Returns:
            DataFrame: A DataFrame containing the processed data based on user inputs.
        """
        data = []  # To collect the processed chunks

        # Reading the CSV file in chunks
        for chunk in self._read_data_in_chunks():
            # Apply row range filtering (if provided)
            if start_row is not None or end_row is not None:
                chunk = chunk.iloc[start_row:end_row]

            # Apply column filtering (if provided)
            if columns:
                valid_columns = self._validate_columns(chunk, columns)
                chunk = chunk[valid_columns]

            # Apply filtering conditions (if provided)
            if filters:
                chunk = self._apply_filters(chunk, filters)

            # Collect the processed chunk
            if not chunk.empty:
                data.append(chunk)

        # Use reduce to concatenate all chunks into a single DataFrame
        return reduce(lambda x, y: concat([x, y]), data) if data else DataFrame()  # Return empty DataFrame if no data


if __name__ == "__main__":
    from main import configure_logging
    configure_logging()

    dir = Path(__file__).parent
    file_path = dir / "GlobalWeatherRepository.csv"
    csv_handler = CSVHandler(str(file_path))

    # Example 1: Get data for specific columns
    col = ['humidity', 'wind_mph', 'nonexistent_column']
    data = csv_handler.get_data(columns=col)
    print(data)

    # Example 2: Get rows between 1000 and 2000
    data = csv_handler.get_data(start_row=1000, end_row=2000)
    print(data)

    # Example 3: Get data with filtering (e.g., humidity > 50, wind_mph < 10)
    filters = {'humidity': '>50', 'wind_mph': '<10', 'nonexistent_column': '==5'}
    data = csv_handler.get_data(filters=filters)
    print(data)
