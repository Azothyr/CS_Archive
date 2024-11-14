# Phase 08: PySpark

In this phase, the application was adapted to run on a PySpark cluster, enabling distributed data processing for improved performance and scalability. The `ClusterCSVHandler` class was developed to handle CSV data efficiently within a PySpark environment. Additionally, the project incorporates specific configurations and code modifications to ensure compatibility and optimal performance when running on a PySpark cluster.

## Changes
### 1. Cluster Integration
- **PySpark Environment**: The functionality runs on a PySpark cluster via the `py4j` library, which enables Python programs to interact with Java objects on a Spark cluster.
- **Py4j Integration**: The `ClusterCSVHandler` class was developed to handle CSV data processing using PySpark via the Py4J library. 
> Due to this, it is required to have java installed on the cluster (of system if you ).


- #### Packages used
  - `py4j`: Py4J library for Python-Java integration.
  - `pyspark`: PySpark library for distributed data processing.
  - `pyspark.sql`: PySpark SQL module for working with structured data.
  - `pyspark.sql.SparkSession`: The main entry point for PySpark functionality.
  - `pyspark.sql.DataFrame`: A distributed collection of data organized into named columns.

### 2. Spark Session Configuration
To run on a PySpark cluster, it is essential to create a properly configured `SparkSession` that connects to the cluster and optimizes resource usage:
- **Master URL**: The `master` parameter was set to `"local[*]"` for development and testing purposes but should be configured to the appropriate cluster URL (e.g., `"spark://<cluster-host>:<port>"`) for deployment.
- **Memory Configuration**: Increased executor and driver memory (`spark.executor.memory` and `spark.driver.memory`) were set to `"8g"` to handle larger datasets.
- **Driver Host**: The `driver.host` was configured as `"localhost"` for local runs; it should be set to the appropriate IP or host when running in a distributed environment.

### 3. Data Reading and Handling
- **Reading Data**: The `_read_data` method was modified to use the Spark CSV reader with `header=True` and `inferSchema=True` for schema inference. This ensures the data is read as a `DataFrame` suitable for distributed processing.
- **Data Processing**: The `_process_data` method was updated to accept an optional list of columns for selective column processing.

### 4. Error Handling and Runtime Checks
Error handling was enhanced to provide more detailed runtime error messages when reading data or configuring the Spark session. This ensures that issues are logged effectively for debugging in a distributed environment.

## Added Functionality
- **Cluster Based Processing**: The application now runs on a PySpark cluster for distributed data processing.
- **Enhanced Error Handling**: Catches and logs exceptions during data reading and processing.
- **Memory Configuration**: Configurable memory settings for both driver and executor.
- **Test Suite Enhancements**: Updated test cases to ensure compatibility and validate the new functionalities.

### New Functions
- **`ClusterCSVHandler` Class**: A class to handle CSV data processing using PySpark.
  - **`__init__`**: Initializes the `ClusterCSVHandler` instance with a spark session and the provided file path.
    - _Arguments_:
      - `file_path` (str): The path to the CSV file.
      - `master` (str): The URL of the Spark cluster master. Default is `"local[*]"`.
      - `driver_host` (str): The host of the Spark driver. Default is `"localhost"`.
      - `executor_memory` (str): The memory allocated to each executor. Default is `"8g"`.
      - `driver_memory` (str): The memory allocated to the driver. Default is `"8g"`.
      - `driver_host` (str): The host of the Spark driver. Default is `"localhost"`.
  - **`set_log_level`**: Sets the log level for the Spark session.
    - _Arguments_:
      - `level` (str): The log level to set. Default is `"ERROR"`.
  - **`_read_data`**: Reads the CSV data using PySpark and returns a DataFrame.
    - _Returns_:
      - `DataFrame`: The PySpark DataFrame containing the CSV data.
  - **`_process_data`**: Processes the DataFrame by selecting specific columns.
    - _Arguments_:
      - `columns` (list): A list of column names to select. Default is `None`.
    - _Returns_:
      - `DataFrame`: The processed DataFrame with selected columns.
  - **`get_data`**: Public method to read and process the CSV data.
    - _Arguments_:
      - `columns` (list): A list of column names to select. Default is `None`.
    - _Returns_:
        - `DataFrame`: The processed DataFrame with selected columns.

## Tests
The `test_cluster_csv_handler.py` includes test cases for the `ClusterCSVHandler` class. These test cases ensure the correct functioning of data reading, processing, and error handling in a PySpark environment.

| Test Name                                | Description                                               | Inputs                                        | Expected Outputs                                              | Success Criteria                                             |
|------------------------------------------|-----------------------------------------------------------|-----------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| `test_cluster_handler_initialization`    | Tests initialization of the `ClusterCSVHandler` class.    | File path = `dummy.csv`                       | Instance with `file_path` set to `dummy.csv`.                 | The class is correctly initialized with the given file path. |
| `test_cluster_handler_read_data_failure` | Ensures `_read_data` handles file read errors gracefully. | Invalid file path                             | `RuntimeError` with message containing `Failed to read data`. | The error is raised with an informative message.             |
| `test_cluster_handler_process_data`      | Validates the column selection during data processing.    | Sample DataFrame, Columns = `['name']`        | Processed DataFrame with selected columns only.               | The output DataFrame contains only the `name` column.        |
| `test_cluster_handler_get_data_failure`  | Tests `get_data` method for missing file handling.        | File path = `dummy.csv`, Columns = `['name']` | `RuntimeError` with message containing `Failed to read data`. | The error is raised with an informative message.             |