# Phase 04: Refactor to use Generators, Iterators, & logging

Much of the code from the previous phase remains unchanged, due to the fact that all but the use of generators has already been implemented in some form. However, there are some changes made that are described below.

## Generators

The `csv_handler.read_data` method has been refactored to be `csv_handler.read_data_in_chunks`. This method now takes a parameter `chunk_size` that determines the amount of rows to be read from a csv file per yield. The method now returns a generator that yields a chunk of data at a time. This allows for the data to be read in chunks, rather than all at once, which can be useful for large datasets.

## Iterators

The current use of iterators can be found in the `data_calculator` class, where the `__iter__` method has been implemented. This method returns an iterator that iterates over the data in the `data` attribute of the class.

## Logging

The previous use of logging called in the main guard of `main.py` was set to use only the default `logging.BasicConfig` but now it has been refactored to show a formatted data and time, the log level, and the message. Additionally the logging calls have been updated in all modules to give a more in depth look at what is happening in the program.