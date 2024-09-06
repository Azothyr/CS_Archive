# CSV Data Processing Script

This Python script allows users to select and read data from a CSV file, processes the data into a Pandas DataFrame, and logs the information for debugging and further analysis.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Logging](#logging)
- [Output](#output)
- [Dataset](#dataset)

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Azothyr/CS_Archive.git
   ```

2. Navigate to the `Phase02` directory:
    
    ```bash
    cd CS_Archive/CS3270_Fall2024/Phase02
    ```

3. **Install Dependencies:**

   The script requires Python 3 and the following Python packages:

   - `pandas`
   - `PyQt5`
   - `logging`
   - `pathlib`
   - `numpy`
   - `scipy`

   You can install the necessary packages using `pip`:

   ```bash
   pip install pandas PyQt5 logging pathlib numpy scipy
   ```

---

## Usage

1. **Place the Dataset:**
    By default, the script will open a file dialog starting in the `resources` directory. If this directory does not exist, it will default to the user's home directory.

2. **Run the Script:**

   Execute the script using Python at the directory where `main.py` is located:

    ```bash
    python main.py
    ```
    
    The script will prompt the user to select a CSV file, read the data, process it, and log the output.
3. 
---

## Modules

### csv_handler.py

`read_data_from_csv(path: str | Path) -> DataFrame`

    Reads the data from a CSV file and returns a Pandas DataFrame.

- **Parameters**:
    - `path (str | Path)`: Path to the CSV file.
- **Returns**:
    - `DataFrame`: DataFrame containing the data from the CSV file.

### file_handler.py

`retrieve_file() -> str`

    Opens a file dialog to select the data file to process.

- **Returns**:
  - `str`: Path to the selected file.


### calculator.py

`DataCalculator`

    Class that processes the data from the CSV file.

- **Attributes**:
  - `data (list[int | float])`: List of data to analyze.
  - `mean (float)`: Mean of the data.
  - `median (float)`: Median of the data.
  - `mode (float)`: Mode of the data.
  - `standard_deviation (float)`: Standard deviation of the data.
  - `min (float)`: Minimum value in the data.
  - `max (float)`: Maximum value in the data.

- **Methods**:
  - `validate_data(in_data: list[int | float])`: Validates the data to ensure it is not empty and contains only numerical values.
  - `get_data() -> list[int | float]`: Returns the data.
  - `calculate_mean() -> float`: Calculates the mean of the data.
  - `calculate_median() -> float`: Calculates the median of the data.
  - `calculate_mode() -> sp.mode`: Calculates the mode of the data.
  - `calculate_variance() -> float`: Calculates the variance of the data.
  - `calculate_standard_deviation() -> float`: Calculates the standard deviation of the data.
  - `calculate_min() -> float`: Calculates the minimum value in the data.
  - `calculate_max() -> float`: Calculates the maximum value in the data.

### main.py

`main()`

    Main function that orchestrates the reading and processing of the weather data.

---

## Logging
The script uses Python's built-in logging module to provide informative messages during execution. The logging levels used are:

- `INFO`: General information about the process.

- `DEBUG`: Detailed information, typically useful for diagnosing issues.

Logging configuration is set to DEBUG level by default, so all messages will be printed to the console.

---

## Output
The script logs the following output:

- INFO:
  - Confirms successful reading and preprocessing of data.

- DEBUG:
  - Shows a sample of the data from the CSV file.
  - Displays the first item from each processed data structure.

Sample output:

![](/resources/Phase02-output1.png)
![](/resources/Phase02-output2.png)

---

## Dataset

The current iteration uses a CSV dataset selected by the user through a file dialog. By default, the file dialog will open in the `resources` directory if it exists, or in the user's home directory otherwise.

The default dataset provided in the resource folder is available for use and was downloaded from this Kaggle repository: [Global Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository).

---

## Creating the package

Required packages:
- `setuptools`
- `wheel`

Install using pip:

```bash
pip install setuptools wheel
```

At the root of the repository, run the following command:

```bash
python setup.py sdist bdist_wheel
```

This command will create a `dist` directory containing the package distribution files.