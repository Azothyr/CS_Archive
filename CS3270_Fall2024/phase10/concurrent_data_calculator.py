import concurrent.futures
import asyncio
from tqdm import tqdm
import logging as log
from typing import List, Union
# from timer import function_timer
from data_calculator import DataCalculator
import time


class ConcurrentDataCalculator(DataCalculator):
    # Threshold for using concurrency: default is 10,000,000 data points
    concurrency_threshold = 10_000_000

    def __init__(self, data: List[Union[int, float]]):
        super().__init__(data)

    def _validate_data(self, in_data: List[Union[int, float]]):
        """
        Validate the data to ensure it is a list of integers or floats

        Parameters:
            in_data (List[Union[int, float]]): List of data to validate
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
            log.debug(f"Data size: {len(self.data):,} < Threshold: {ConcurrentDataCalculator.concurrency_threshold:,}."
                      f" Using synchronous method.")
            super()._perform_analysis()
        else:
            log.debug(f"Data size: {len(self.data):,} >= Threshold: {ConcurrentDataCalculator.concurrency_threshold:,}."
                      f" Using concurrent method.")
            asyncio.run(self._perform_analysis_async())

    async def _perform_analysis_async(self):
        """
        Perform the analysis on the data asynchronously.
        """
        start_time = time.time()
        if not self.data:
            self._mean = None
            self._median = None
            self._mode = None
            self._variance = None
            self._standard_deviation = None
            self._min = None
            self._max = None
            self.analysis_time = 0
            return

        # Use ThreadPoolExecutor and asyncio to calculate statistics concurrently
        loop = asyncio.get_event_loop()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            tasks = {
                "_mean": loop.run_in_executor(executor, self._calculate_mean),
                "_median": loop.run_in_executor(executor, self._calculate_median),
                "_mode": loop.run_in_executor(executor, self._calculate_mode),
                "_variance": loop.run_in_executor(executor, self._calculate_variance),
                "_standard_deviation": loop.run_in_executor(executor, self._calculate_standard_deviation),
                "_min": loop.run_in_executor(executor, self._calculate_min),
                "_max": loop.run_in_executor(executor, self._calculate_max)
            }

            completed_tasks = []
            with tqdm(total=len(tasks), desc="Calculating statistics", colour="green",
                      bar_format="{desc}: {percentage:3.0f}% |{bar}| {n:.0f}/{total:.0f}") as progress:
                for attr, coro in tasks.items():
                    try:
                        result = await coro
                        if result is not None:
                            setattr(self, attr, result)
                            completed_tasks.append(attr)
                        else:
                            log.error(f"Calculation for {attr} returned None.")
                        progress.update(1)
                    except Exception as e:
                        log.error(f"Calculation for {attr} failed with exception: {e}")
                        setattr(self, attr, None)

            # Check if any attribute was not calculated due to an exception
            for attr in tasks.keys():
                if attr not in completed_tasks:
                    log.error(f"Calculation for {attr} failed or was incomplete.")
                    setattr(self, attr, None)

        # Record the analysis time accurately
        self.analysis_time = round(time.time() - start_time, 5)
        if self.analysis_time == 0:
            log.warning("Analysis time is zero or too short to measure accurately.")


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
        print(f"Synchronous test complete: {s_calculator.analysis_time:.4f} seconds")

        # Test with concurrent execution.
        c_calculator = ConcurrentDataCalculator(data)
        if c_calculator.analysis_time is None or c_calculator.analysis_time == 0:
            print("Error: Concurrent analysis time is zero or not recorded, indicating an issue with the calculation.")
        else:
            print(f"Concurrent test complete: {c_calculator.analysis_time:.4f} seconds")
            print(f"Speedup: {s_calculator.analysis_time / c_calculator.analysis_time:.2f}x")


    # Example test parameters.
    test_data_size = 10_000_000
    # test_data_size = 9_999_999
    test_step = 2

    # Run the test.
    speed_test_concurrent_vs_synchronous(test_data_size, test_step)
