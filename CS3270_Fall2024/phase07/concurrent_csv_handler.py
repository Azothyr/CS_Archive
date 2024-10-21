from pandas import DataFrame, concat
import concurrent.futures
from functools import reduce
from csv_handler import CSVHandler


class ConcurrentCSVHandler(CSVHandler):
    """
    ConcurrentCSVHandler class for asynchronously reading and processing CSV files.
    It inherits from CSVHandler and only overrides methods that need to be asynchronous.
    """

    def get_data(self, columns: list[str] | None = None, start_row: int | None = None,
                 end_row: int | None = None, filters: dict | None = None) -> DataFrame:
        """
        Public method to asynchronously retrieve and process the data from the CSV file.

        Parameters:
            columns (list[str] | None): List of columns to retrieve
            start_row (int | None): Starting row index
            end_row (int | None): Ending row index
            filters (dict | None): Dictionary of filters for each column

        Returns:
            DataFrame: Processed data
        """
        data = []  # To collect the processed chunks

        # Use ThreadPoolExecutor to process chunks concurrently
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._process_chunk, chunk, columns, start_row, end_row, filters)
                       for chunk in self._read_data_in_chunks()]

            for future in concurrent.futures.as_completed(futures):
                data.append(future.result())

        # Use reduce to concatenate all chunks into a single DataFrame
        return reduce(lambda x, y: concat([x,y]), data) if data else DataFrame()  # Return empty DataFrame if no data


if __name__ == "__main__":
    from pathlib import Path
    import time

    def speed_test(csv_handler: CSVHandler, num_tests: int = 10, show_order: bool = False,
                   show_data: bool = False) -> float:
        start_time = time.time()
        columns = ["wind_mph", "sunset", "sunrise", "uv_index", "temperature_fahrenheit", "humidity", "wind_degree"]
        filters = {'humidity': '>50', 'wind_mph': '<10', 'temperature_fahrenheit': '>70', 'wind_degree': '>=0'}

        for i in range(1, num_tests+1):
            try:
                data = csv_handler.get_data(columns=columns, filters=filters)
                if show_order:
                    print(f"Test {i}")
                if show_data:
                    print(data)
            except Exception as e:
                print(f"Error processing data on attempt[{i}]: {e}")
                return 0

        # Return the elapsed time to the 4th decimal place
        return round(time.time() - start_time, 4)

    file_path = Path(__file__).parent.parent / "resources" / "GlobalWeatherRepository.csv"
    if not file_path.exists():
        raise FileNotFoundError("File not found")

    print(f"Executing synchronous test")
    synchronous_time = speed_test(CSVHandler(str(file_path)), num_tests=10)
    print(f"Synchronous test complete\n"
          f"Executing asynchronous test")
    asynchronous_time = speed_test(ConcurrentCSVHandler(str(file_path)), num_tests=10)
    print(f"Asynchronous test complete\n")

    print(f"Synchronous elapsed time: {synchronous_time} seconds\n"
          f"Asynchronous elapsed time: {asynchronous_time} seconds\n"
          f"Time difference: {abs(synchronous_time - asynchronous_time):.4f} seconds")
