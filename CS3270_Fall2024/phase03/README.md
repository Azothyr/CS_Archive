# Phase 3: Refactoring to Object-Oriented Design

This Python application processes CSV files by selecting the file through a GUI file dialog and analyzing the data using various statistical methods (mean, median, mode, etc.). The refactor applies advanced OOP principles to organize the code into separate classes for better structure and maintainability.

## Design and Object-Oriented Principles

The application has been refactored to make use of the following OOP principles:

1. **Encapsulation**: 
   - The functionalities related to file handling and CSV data reading are now encapsulated within their own classes (`FileHandler` and `CSVHandler`). As they are signified as private methods, they are not directly accessible from outside the class. This ensures that the internal implementation details are hidden behind name mangling and will be for internal use while the public method is callable.

2. **Abstraction**:
   - The `FileHandler` and `CSVHandler` classes abstract the details of how file paths are retrieved and how CSV data is read. Other parts of the code, such as `main.py`, only interact with these classes at a high level, without worrying about the specifics.

3. **Separation of Concerns**:
   - The refactor separates different responsibilities into their respective classes:
     - `FileHandler`: Responsible for selecting a file through a dialog.
     - `CSVHandler`: Responsible for reading the CSV file and returning the data as a DataFrame.
     - `DataCalculator`: Handles the statistical calculations (mean, median, mode, etc.).

## Refactored Classes and their Responsibilities

1. **File Handling**:
   - The `FileHandler` class is responsible for opening a file dialog to select a CSV file. It provides the file path to the rest of the application.

2. **CSV Reading**:
   - The `CSVHandler` class reads the CSV file using the provided file path and converts the data into a `pandas.DataFrame`.

3. **Data Analysis**:
   - The `DataCalculator` class processes the data by calculating various statistics such as mean, median, mode, etc.
