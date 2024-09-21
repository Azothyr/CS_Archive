# Phase 5: Unit Testing and Doc Testing

In this phase, I was able to implement unit and doc testing for the `data_calculator`, `test_data_calculator.py`, and `data_calculator.py` files.

## Unit Testing

The primary package used for unit testing in this phase is the `pytest` package. But to make it so I did not have to install the pytest mocker package, I used `monkeypatch` fixture from the built-in `unittest.mock` module. This allowed me to mock pieces of the code needed to perform the test cases. such as mocking a csv file and having it not raise exceptions that would be correct under normal circumstances but would cause the test to fail.

## Doc Testing

The doc testing was done using the built-in `doctest` module. This allowed me to test the docstrings in the each of the modules. The `doctest` module was able to run the tests and verify that the docstrings were correct.

## Test Cases

| Test Name | Description                                  | Use Case Reference | Inputs | Expected Outputs           | Success Criteria                                                                         |
|-----------|----------------------------------------------|--------------------|--------|----------------------------|------------------------------------------------------------------------------------------|
| Test 1    | Tests addition operation                     | Use Case 1         | None   | Correct addition result    | Will correctly add the number from the provided memory address to the accumulator        |
| Test 2    | Tests out-of-range addition operation        | Use Case 1         | None   | Error thrown               | Will correctly throw an error when the memory address is out of range                    |
