import asyncio
import aiofiles
from pandas import DataFrame, concat
import concurrent.futures
from functools import reduce
from csv_handler import CSVHandler
import pandas as pd
import logging as log


class ConcurrentCSVHandler(CSVHandler):
    """
    ConcurrentCSVHandler class for asynchronously reading and processing CSV files.
    Inherits from CSVHandler and overrides methods to add asynchronous capabilities.
    """

    async def _read_data_in_chunks_async(self):
        """
        Reads data from the CSV file in chunks synchronously within an async wrapper.

        Yields:
            DataFrame: A chunk of the CSV data as a DataFrame.
        """
        try:
            log.debug(f"Reading file asynchronously: {self.file_path}")
            for chunk in pd.read_csv(self.file_path, chunksize=self.chunk_size):
                yield chunk
        except Exception as e:
            log.error(f"Error reading file asynchronously: {e}")
            raise e

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
        data = []

        # Use ThreadPoolExecutor to process chunks concurrently
        with concurrent.futures.ThreadPoolExecutor() as executor:
            chunks = asyncio.run(self._read_all_chunks())
            futures = [
                executor.submit(self._process_chunk, chunk, columns, start_row, end_row, filters)
                for chunk in chunks
            ]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result is not None:
                    data.append(result)

        # Use reduce to concatenate all chunks into a single DataFrame
        return reduce(lambda x, y: concat([x, y]), data) if data else DataFrame()

    async def _read_all_chunks(self):
        """
        Helper method to read all chunks asynchronously.

        Returns:
            List[DataFrame]: A list of chunks read asynchronously.
        """
        chunks = []
        async for chunk in self._read_data_in_chunks_async():
            chunks.append(chunk)
        return chunks


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
    synchronous_time = speed_test(CSVHandler(str(file_path)), num_tests=10, show_order=False, show_data=False)
    print(f"Synchronous test complete\n"
          f"Executing asynchronous test")
    asynchronous_time = speed_test(ConcurrentCSVHandler(str(file_path)), num_tests=10, show_order=False, show_data=False)
    print(f"Asynchronous test complete\n")

    print(f"Synchronous elapsed time: {synchronous_time} seconds\n"
          f"Asynchronous elapsed time: {asynchronous_time} seconds\n"
          f"{"Asynchronous" if asynchronous_time < synchronous_time else "Synchronous"} test is faster by "
          f"{abs(synchronous_time - asynchronous_time):.4f} seconds")
