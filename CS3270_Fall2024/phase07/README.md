# Phase 07: Multithreading Concurrency

In this phase I added the `ConcurrentCSVHandler`, `ConcurrentDataCalculator`, and `timer` decorator. The `ConcurrentCSVHandler`
class that extends the `CSVHandler` class to perform the chunk processing in a concurrent manner. And the `ConcurrentDataCalculator`
class extends the `DataCalculator` class to perform the data calculations in a concurrent manner. Both additions were achieved
by creating a `ThreadPoolExecutor` and submitting the tasks to the executor. The `timer` was added as a decorator to an
override method of the `ConcurrentCSVHandler`.`_perform_analysis` and `ConcurrentDataCalculator`.`get_data` methods to time the
execution of the methods. TQDM was also added to the `DataCalculator` and `ConcurrentDataCalculator` to show the progress
of the calculations. Due to the concurrency being less effective than the synchronous version of the `DataCalculator`
class. I added a threshold of data points at the `ConcurrentDataCalculator`'s class level, so the threading will only
be used if the number of data points is greater than the threshold. This was done to avoid the overhead of creating
threads for small data sets and should hopefully improve the performance of the concurrent version. The `main.py` was
updated to show the new functionality in action.

## Added Functionality

- `ConcurrentCSVHandler` class extends the `CSVHandler` class to perform the chunk processing in a concurrent manner.
- `ConcurrentDataCalculator` class extends the `DataCalculator` class to perform the data calculations in a concurrent manner.
- threshold of data points was added to the `ConcurrentDataCalculator` class to avoid the overhead of creating threads for small data sets.
- `timer` decorator was added to time the execution of the `ConcurrentCSVHandler`.`_perform_analysis` and `ConcurrentDataCalculator`.`get_data` methods.
- `TQDM` module was added to show the progress of the calculations in the `DataCalculator` and `ConcurrentDataCalculator`.
- `main.py` was updated to show the new functionality in action.