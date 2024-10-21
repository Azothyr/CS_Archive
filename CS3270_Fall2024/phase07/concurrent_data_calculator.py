import concurrent.futures
from tqdm import tqdm
import logging as log
from timer import function_timer
from data_calculator import DataCalculator


class ConcurrentDataCalculator(DataCalculator):
    # Threshold for using concurrency: default is 10,000,000 data points
    concurrency_threshold = 10_000_000

    def __init__(self, data: list[int | float]):
        super().__init__(data)

    def _validate_data(self, in_data: list[int | float]):
        """
        Validate the data to ensure it is a list of integers or floats

        Parameters:
            in_data (list[int | float]): List of data to validate
        """
        if not isinstance(in_data, list):
            raise ValueError("Input data must be a list")

        temp = [i for i in in_data if isinstance(i, (int, float))]
        if len(temp) != len(in_data):
            log.warning("Invalid data found. Only integers and floats are allowed. Skipping invalid data.")

        # If no valid data is found, set the data to a list containing 0
        self._data = temp if temp else []

        # If the data is less than the concurrency threshold, use the synchronous method
        if len(self.data) < ConcurrentDataCalculator.concurrency_threshold:
            print(f"Data size: {len(self.data):,} < Threshold: {ConcurrentDataCalculator.concurrency_threshold:,}."
                  f" Using synchronous method.")
            super()._perform_analysis()
        else:
            print(f"Data size: {len(self.data):,} >= Threshold: {ConcurrentDataCalculator.concurrency_threshold:,}."
                  f" Using concurrent method.")
            self._perform_analysis()

    @function_timer(timer_attr='analysis_time')
    def _perform_analysis(self):
        """
        Perform the analysis on the data
        """

        if not self.data:
            self._mean = None
            self._median = None
            self._mode = None
            self._variance = None
            self._standard_deviation = None
            self._min = None
            self._max = None
        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                tasks = {
                    "_mean": self._calculate_mean,
                    "_median": self._calculate_median,
                    "_mode": self._calculate_mode,
                    "_variance": self._calculate_variance,
                    "_standard_deviation": self._calculate_standard_deviation,
                    "_min": self._calculate_min,
                    "_max": self._calculate_max
                }

                futures = {}
                with tqdm(total=len(tasks), desc="Calculating statistics", colour="green",
                          bar_format="{desc}: {percentage:3.0f}% |{bar}| {n:.0f}/{total:.0f}") as progress:
                    for attr, func in tasks.items():
                        future = executor.submit(func)
                        futures[future] = attr
                        progress.update(0.5)

                    for future in concurrent.futures.as_completed(futures):
                        attr = futures[future]
                        setattr(self, attr, future.result())
                        progress.update(0.5)


if __name__ == "__main__":
    def create_data(starts: list[int] | int, sizes: list[int] | int, steps: list[int] | int) -> list[int]:
        starts, sizes, steps = map(
            lambda value: [value] if isinstance(value, int) else value,
            [starts, sizes, steps]
        )
        if len(starts) != len(sizes) or len(sizes) != len(steps):
            raise ValueError("All lists must be of the same length")

        # Generate data based on the given parameters.
        for start, size, step in zip(starts, sizes, steps):
            yield from range(start, start + size, step)


    def speed_test_concurrent_vs_synchronous(data_size, step=1, start=0):
        # Generate data based on the given parameters.
        data_size *= step
        data = list(create_data(start, data_size, step))
        print(f"\nTesting with {len(data):,} data points")

        # Test with synchronous execution.
        s_calculator = DataCalculator(data)
        print(f"Synchronous test complete: {s_calculator.analysis_time:.5f} seconds")

        # Test with concurrent execution.
        c_calculator = ConcurrentDataCalculator(data)
        print(f"Concurrent test complete: {c_calculator.analysis_time:.5f} seconds")

        # Compare results.
        print(f"Elapsed time for synchronous calculation: {s_calculator.analysis_time:.5f} seconds")
        print(f"Elapsed time for concurrent calculation: {c_calculator.analysis_time:.5f} seconds")
        print(f"Speedup: {s_calculator.analysis_time / c_calculator.analysis_time:.2f}x")


    # Example test parameters.
    test_data_size = 10_000_000
    # test_data_size = 9_999_999
    test_step = 2

    # Run the test.
    speed_test_concurrent_vs_synchronous(test_data_size, test_step)
