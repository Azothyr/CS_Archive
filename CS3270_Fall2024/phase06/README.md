# Phase 06: Data Patterns, Trends, and Visualization

In this phase I was able to update the `CSVHandler` class to perform filtering on the data while still performing the tasks in a compiled chunked concurrent manner. 
The `main.py` shows this in action by filtering the data to only include the data for contries that start with the letter `C` and create graphs for their
`Temperature Trends`, `Air Quality (PM2.5) over Time`, `Humidity over Time`, `Temperature Distribution`, and `Precipitation vs Temperature`.


## Added Functionality

- `CSVHandler` class now has a `get_data` that is the primary method of the function. It takes in a list of `columns`, `start_row`, `end_row`, and a dictionary of `filters` to apply to the data in the columns provided.
- `CSVHandler` class now has a `_validate_columns` method that checks for the provided columns in the data.
- `CSVHandler` class now has a `_apply_filters` method that takes the filtered columns and further filters the data based on the provided conditions.

## Tests

The `test_csv_handler.py` has been updated to include tests for the new functionality of the `CSVHandler` class as follows:
- `test_column_selection` tests for correct filtering of data based on provided columns.
- `test_row_range_selection` tests for correct filtering of data based on provided row range.
- `test_filter_application` tests for correct filtering of data based on provided filters.
- `test_filter_application_invalid_column` tests for proper handling of an invalid column in the filters.
- `test_file_not_found` tests for correct handling of a file not found exception.