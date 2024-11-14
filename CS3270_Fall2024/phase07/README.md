# Phase 07: Multithreading Concurrency

In this phase, I added the `ConcurrentCSVHandler`, `ConcurrentDataCalculator`, and `timer` decorator. The `ConcurrentCSVHandler` class extends the `CSVHandler` class to perform the chunk processing in a concurrent manner, and the `ConcurrentDataCalculator` class extends the `DataCalculator` class to perform data calculations concurrently. This concurrency was achieved using a `ThreadPoolExecutor` to submit tasks for parallel execution. The `timer` decorator was applied to key methods to measure the execution time, specifically to the `ConcurrentCSVHandler._perform_analysis` and `ConcurrentDataCalculator.get_data` methods. Additionally, the `tqdm` library was used to display progress during calculations.

To optimize performance, a threshold was added to the `ConcurrentDataCalculator` class to only utilize multithreading for data sets exceeding a specified size. This avoids the overhead of thread creation for smaller data sets and enhances the overall performance of the concurrent version.

The `main.py` script was updated to showcase the new functionality in action.

## Enhancements:
- **Asynchronous Analysis**: The `ConcurrentDataCalculator` uses `asyncio` to perform data analysis concurrently, providing better performance for large data sets by running calculations asynchronously.
- **Accurate Timing**: The `analysis_time` attribute now records the precise time taken for concurrent operations, ensuring more reliable benchmarking.
- **Error Handling**: Enhanced error handling and logging have been added to catch issues during async execution and record missing or failed computations.

## Added Functionality:
- `ConcurrentCSVHandler` class for concurrent CSV processing.
- `ConcurrentDataCalculator` class for concurrent and asynchronous data analysis.
- Threshold logic to determine when to use synchronous vs. concurrent methods.
- `timer` decorator for timing execution.
- `tqdm` for progress visualization.


## Test Cases

| Test Name                    | Description                                                 | Inputs                                                           | Expected Outputs                                 | Success Criteria                                              |
|------------------------------|-------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------|
| `test_get_data_with_columns` | Tests column selection during data retrieval.               | Columns = `['column1', 'column2']`, start_row = 0, end_row = 100 | DataFrame with selected columns.                 | Output DataFrame contains specified columns.                  |
| `test_get_data_with_filters` | Validates data filtering during processing.                 | Filters = `{'column1': '>50', 'column2': '<100'}`                | Filtered DataFrame with matching conditions.     | Output DataFrame meets filter criteria.                       |
| `test_small_data_analysis`   | Tests analysis with small data size (synchronous path).     | Data = `[0, 1, 2, ..., 999]`                                     | Analysis results (mean, median, etc.) are valid. | Analysis executes without concurrency for small data.         |
| `test_large_data_analysis`   | Tests analysis with large data size (concurrent path).      | Data = `[0, 1, 2, ..., 9,999,999]`                               | Analysis results (mean, median, etc.) are valid. | Analysis executes using concurrency for large data.           |
| `test_threshold_behavior`    | Ensures threshold logic selects the correct execution path. | Data = `[0, 1, 2, ..., 999]`                                     | Synchronous processing for data below threshold. | Method execution switches between synchronous and concurrent. |
