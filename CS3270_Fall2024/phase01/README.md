# Weather Data Processing Script

This Python script reads weather data from a CSV file, processes the data into various data structures, and logs the information for debugging and further analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Logging](#logging)
- [Output](#output)
- [Dataset](#dataset)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Utah-Valley-University/phase-1-optimal-python-development-lifecycle-Azothyr.git
   ```   

2. **Install Dependencies:**

   The script requires Python 3 and the following Python packages:

   - `pandas`
   - `logging`
   - `pathlib`

   You can install the necessary packages using `pip`:

   ```bash
   pip install pandas
   ```
   ```bash
   pip install logging
   ```
   ```bash
   pip install pathlib
   ```
   
## Usage

1. **Place the Dataset:**

   Ensure that the weather dataset (`GlobalWeatherRepository.csv`) is located in the `resources` directory of your project.

2. **Run the Script:**

   Execute the script using Python:

    ```bash
    python main.py
    ```
    
    The script reads the data, processes it, and logs the output.

## Functions

`read_data_from_csv(path) -> pd.DataFrame`

Reads the data from a CSV file and returns a Pandas DataFrame.
- **Parameters**:
  - path (pathlib.Path): Path to the CSV file.
- **Returns**:
  - pd.DataFrame: DataFrame containing the data from the CSV file.
    
`process_weather_info_to_data_structures(data) -> tuple`

Processes the weather data into various Python data structures.

- **Parameters**:
data (pd.DataFrame): DataFrame containing the weather data.
- **Returns**:
    - tuple: A tuple containing the processed data:
      - list: Countries
      - list: Cities
      - list: Dates
      - list: Times
      - list: Weather conditions
      - dict: Temperature (Fahrenheit and Celsius)
      - list: Humidity
      - dict: Wind speed (mph and kph)
      - list: Latitude
      - list: Longitude

`main()`

Main function that orchestrates the reading and processing of the weather data.

## Logging
The script uses Python's built-in logging module to provide informative messages during execution. The logging levels used are:

- `INFO`: General information about the process.

- `DEBUG`: Detailed information, typically useful for diagnosing issues.
Logging configuration is set to DEBUG level by default, so all messages will be printed to the console.

## Output
The script logs the following output:

- INFO:
  - Confirms successful reading and preprocessing of data.
- DEBUG:
  - Shows a sample of the data from the CSV file.
  - Displays the first item from each processed data structure.

Sample output:

``` plaintext
info:root:    
    Data read successfully

DEBUG:root:       
    country     location_name   ...     moon_phase      moon_illumination
0  Afghanistan  Kabul           ...     Waxing Gibbous  55
[1 rows x 41 columns]

INFO:root:    
    Data preprocessed successfully
    
DEBUG:root:
['Afghanistan', 'Kabul', '2024-05-16', '13:15', 'Partly Cloudy', dict_keys(['fahrenheit', 'celsius']), 24, dict_keys(['mph', 'kph']), 34.52, 69.18]
```

## Dataset

The current iteration uses a hardcoded dataset (`GlobalWeatherRepository.csv`) located in the `resources` directory. 
The dataset contains weather information for various locations around the world and can be downloaded from the following link:
https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository
