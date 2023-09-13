# Tests Directory

## Overview

This directory contains tests that validate the functionality and reliability of our application, ranging from unit tests to integration tests.

## Structure & Specifics

- Test files should be named to mirror the module or component they're testing. For instance, tests for the `PathLib` class from the `info.file_path_library` module are located in `path_lib_tests.py`.

### Path Library Tests (`path_lib_tests.py`)

These tests are designed to validate the correct functioning of the PathLib class from the `info.file_path_library` module.

1. **Path Existence**: Tests that for each given key, the corresponding path exists.
2. **User Path Structure**: Ensures that the "user" key returns a path ending with the user's home directory.
3. **Key-Value Matching**: Validates that certain keys always return their expected path values.

## Best Practices

1. **Descriptive Test Names**: Use clear naming for test functions, indicating what they're testing.
2. **Isolation**: Tests should be isolated and not depend on the state created by other tests.
3. **Mocking**: Use mock objects/services where necessary, especially when avoiding real external service hits.
4. **Coverage**: Aim for extensive test coverage, emphasizing crucial paths and logic.

## Running the Tests

To run all tests in this directory:

```bash
pytest
```
To run a specific test file:

```bash
# Example: pytest <test_file_name>.py

cd .\tests

pytest math_functions_tests.py
```