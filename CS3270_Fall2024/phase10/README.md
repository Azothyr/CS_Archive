# Weather Data Analysis Project

This project is a 3-tier web application for uploading, analyzing, and visualizing CSV data. The base language for this project is `Python`, the web framework was built using `Flask` for the backend with `Jinja` templating for dynamic HTML pages, and `JavaScript` to create an interactive user experience. Data is stored in an `SQLite` database and managed with `SQLAlchemy`.

## Updates in Phase 10
- **Rain Prediction Model**: A machine learning model predicts whether it will rain tomorrow based on the user-provided input. The model is built using `scikit-learn` and is trained from the `Random Forest Classifier algorithm`.
- **Model Training**: The model is trained on the `RainTomorrow` column from the `WeatherTestData.csv` and the `WeatherTrainingData.csv` files.
- **Model Prediction**: Users can adjust values like temperature, humidity, wind direction, etc., and the model will predict whether it will rain tomorrow in the specefied Australian location.
- **Model Accuracy**: The model has an accuracy of around 85% on the test data.
- **Model Output**: The model output is displayed on the `/model` page.
- **Revamped UI**: Some UI elements have been updated to improve the user experience as well as UI for using the rain prediction model.
- **Updated Readme**: The readme file has been updated to include the new features, ML training tests, and instructions for using the rain prediction model.

![](./phase10-Output04.png)


## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [How to Use the Application](#how-to-use-the-application)
- [File Overview](#file-overview)
- [Additional Notes](#additional-notes)
- [Tests](#tests)

## Features

- **Upload CSV Data**: Users can upload weather data in CSV format.
- **Store Data**: The uploaded data is stored in an SQLite database.
- **Data Preview**: Users can preview the uploaded data in a scrollable table.
- **Data Analysis**: Users can select a numeric column and see statistics like mean, median, variance, etc.
- **Visualization**: Users can create custom visualizations by choosing independent (x-axis) and dependent (y-axis) variables.
- **Rain Prediction Model**: A machine learning model predicts whether it will rain tomorrow based on the user-provided input.

## Setup Instructions

1. **Prerequisites**: Make sure Python 3.x is installed. (I used Python 3.9 for this project.)

2. **Install Required Packages**:
   - Dependencies:
     - Flask
     - SQLAlchemy
     - Werkzeug
     - Pandas
     - Matplotlib
     - Typing
     - Numpy
     - Scipy
     - Tqdm
     - Logging
     - Concurrent.futures
     - Asyncio
     - Time
     - Joblib
     - Scikit-Learn
   - Dependencies can be installed using the following command:
    ```bash
    pip install flask sqlalchemy werkzeug pandas matplotlib matplotlib typing numpy scipy tqdm logging concurrent.futures asyncio time joblib scikit-learn
    ```

3. **Run the Application**:
    - navigate to the project directory using the terminal
      ```bash
      cd  <path/to/project/directory>
      ```
    - In the project directory, start the server by running:
      ```bash
      flask run
      ```
      it should look something like this:
      ![](./phase09-Output01.png)
    - Then open `http://127.0.0.1:5000` in your web browser to use the app.

4. **Folders**:
    - To make it easier to run right off the bat, the `uploads` & `static` folder are created for you at runtime in the root directory for storing uploaded and generated visualization files.

## Project Structure

This is a 3-tier app with:
- **Frontend**: HTML, CSS, and JavaScript for the user interface.
- **Backend**: Flask app (in `app.py`) that handles routes, data processing, and API calls.
- **Database**: SQLite database (`dataset.db`) managed with SQLAlchemy.

## How to Use the Application

### **Homepage**:
- Open the app in your browser (`http://127.0.0.1:5000`).
- You will see a homepage that greets you and has two buttons: "Analyze your own data" and "See Australian weather predictive model."
<br><img src="./phase10-Output01.png" alt="drawing" width=""/><br>

### Data Analysis and Visualization

#### **Upload a CSV File**:
- On the home page (`/`), use the "Upload CSV File" button to upload a weather data CSV.
- After uploading, you should see a preview of the data in a table.
<br><img src="./phase09-Output02.png" alt="app2" width="500"/><br>

#### **Data Analysis**:
- After uploading, click "Go to Analysis Page."
- Choose a numeric column for analysis, and click "Analyze" to get stats like mean, median, etc.
<br><img src="./phase09-Output02.png" alt="app3" width="500"/><br>

#### **Create Visualizations**:
- On the analysis page, choose an independent (x-axis) and dependent (y-axis) variable.
- Click "Generate Visualization" to create a scatter plot (if both variables are numeric) or a box plot (if the independent variable is categorical and the dependent variable is numeric).
- The visualization will appear as an image on the page.
<br><img src="./phase09-Output04.png" alt="drawing" width="500"/><br>

### Australian Weather Predictive Model

#### **Rain Prediction Model**:

- Go to the `/model` page to use the rain prediction feature.
- Provide inputs like temperature, humidity, wind direction, etc., and click "Predict Rain Tomorrow." The model will provide a prediction based on the input values.

<br><img src="./phase10-Output02.png" alt="drawing" height="450" width="500"/><img src="./phase10-Output03.png" alt="drawing" height="450" width="500"/><br>

## File Overview

- **app.py**: The main Flask file that sets up routes for uploading, analyzing, visualizing, and predicting data.
- **index.html**: Homepage where you can upload CSV files and preview data.
- **analysis.html**: Analysis page where you can perform statistical analysis and create visualizations.
- **model.html**: Page where users can input weather variables and get a prediction for rain tomorrow.
- **model.py**: Machine learning model that trained the data and predicts if it will rain tomorrow. Created the `label_encoder.pkl` and `rain_predictor.pkl` files that are being used in the `/model.html` page.
- **labels_encoder.pkl**: Encodes the categorical columns in the dataset.
- **rain_predictor.pkl**: The trained model that predicts if it will rain tomorrow.
- **layout.html**: Base HTML layout shared across different pages.
- **static/**: Stores generated visualization images as PNG files.
- **uploads/**: Temporary storage for uploaded CSV files.
- **dataset.db**: SQLite database for storing uploaded weather data.
- **concurrent_data_calculator.py**: Utility for performing concurrent calculations of statistical measures on numeric columns.

## Additional Notes

- **Data Storage**: Uploaded data is saved in an SQLite database. SQLAlchemy manages the data efficiently.
- **Error Handling**: The application includes user-friendly error messages for issues like invalid input values or selection of non-existent columns.
- **Machine Learning Model**: A machine learning model built using `scikit-learn` predicts if it will rain tomorrow based on user inputs. The model uses categorical encoding for variables like wind direction and rainfall status.
- **Validation Accuracy**: The current validation accuracy of the rain prediction model is 84%, indicating that the model performs well on the training data.

## Tests

The `test_model.py` includes test cases for various functions related to data cleaning, encoding, and processing in a pandas environment.

| Test Name               | Description                                                 | Inputs                                                                                                         | Expected Outputs                                               | Success Criteria                                                |
|-------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------|
| `test_clean_data`       | Tests the `clean_data` function for filling missing values. | Sample DataFrame (`TRAINING_DATA`)                                                                             | DataFrame with no missing values.                              | All missing values in the DataFrame are filled.                 |
| `test_encode_data`      | Validates the encoding of categorical columns.              | Sample training and testing DataFrames (`TRAINING_DATA`, `TESTING_DATA`)                                       | Encoded training and testing DataFrames.                       | The categorical columns are properly encoded.                   |
| `test_combine_col_rows` | Ensures columns are combined correctly using mean values.   | Sample DataFrame (`TRAINING_DATA`), Combine table = `{ 'Temp': ['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm'] }` | DataFrame with combined `Temp` column and old columns removed. | The `Temp` column is created, and original columns are dropped. |

