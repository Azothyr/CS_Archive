from pyspark.sql import SparkSession, DataFrame


class ClusterCSVHandler:
    """
    Args:
        file_path: The path to the CSV file that needs to be processed.
        master: The master URL for the Spark cluster. Default is "local[*]".
        app_name: The name of the Spark application. Default is "CSVHandler".
        driver_host: The host address for the Spark driver. Default is "localhost".
    """
    def __init__(self, file_path: str, master: str = "local[*]", app_name: str = "CSVHandler",
                 executor_memory: str = "8g", driver_memory: str = "8g", driver_host: str = "localhost"):
        """
        Args:
            file_path: The path to the CSV file that needs to be processed.
            master: The master URL for the Spark cluster. Default is "local[*]".
            app_name: The name of the Spark application. Default is "CSVHandler".
            driver_host: The host address for the Spark driver. Default is "localhost".
        """
        try:
            self.spark = SparkSession.builder \
                .master(master) \
                .config("spark.driver.host", driver_host) \
                .config("spark.executor.memory", executor_memory) \
                .config("spark.driver.memory", driver_memory) \
                .appName(app_name) \
                .getOrCreate()
        except Exception as e:
            raise RuntimeError(f"Failed to create Spark session: {e}")

        self.file_path = file_path

    def set_log_level(self, level: str = "ERROR"):
        """
        Set the log level for the Spark session.

        Parameters:
            level (str): The log level to set (e.g., "ERROR", "WARN", "INFO", "DEBUG", "TRACE").
        """
        self.spark.sparkContext.setLogLevel(level)

    def _read_data(self) -> DataFrame:
        try:
            return self.spark.read.csv(self.file_path, header=True, inferSchema=True)
        except Exception as e:
            raise RuntimeError(f"Failed to read data: {e}")

    @staticmethod
    def _process_data(data: DataFrame, columns: list[str] | None = None) -> DataFrame:
        if columns is not None:
            data = data.select(columns)

        return data

    def get_data(self, columns: list[str] | None = None) -> DataFrame:
        """
        Public method to retrieve and process the data from the CSV file.

        Parameters:
            columns (list[str] | None): List of columns to retrieve

        Returns:
            DataFrame: Processed data
        """
        return self._process_data(self._read_data(), columns)


if __name__ == "__main__":
    from pathlib import Path
    import time

    def speed_test(csv_handler: ClusterCSVHandler, num_tests: int = 10, show_order: bool = False,
                   show_data: bool = False) -> float:
        """
        Args:
            csv_handler: An instance of `ClusterCSVHandler` responsible for handling CSV data operations.
            num_tests: The number of test iterations to run. Defaults to 10.
            show_order: Flag to indicate whether to print the order of the tests. Defaults to False.
            show_data: Flag to indicate whether to display the retrieved data. Defaults to False.
        """
        start_time = time.time()
        columns = ["wind_mph", "sunset", "sunrise", "uv_index", "temperature_fahrenheit", "humidity", "wind_degree"]

        for i in range(1, num_tests + 1):
            try:
                data = csv_handler.get_data(columns=columns)
                if show_order:
                    print(f"Test {i}")
                if show_data:
                    data.show()
            except Exception as e:
                print(f"Error processing data on attempt[{i}]: {e}")
                return 0

        # Return the elapsed time to the 4th decimal place
        return round(time.time() - start_time, 4)


    file_path = Path(Path(__file__).parent.parent / "resources" / "GlobalWeatherRepository.csv").resolve()
    if not file_path.exists():
        raise FileNotFoundError("File not found")

    print(f"Executing test")
    elapsed_time = speed_test(ClusterCSVHandler(str(file_path)), num_tests=10, show_order=False, show_data=True)
    print(f"Test complete\nElapsed time: {elapsed_time} seconds")
