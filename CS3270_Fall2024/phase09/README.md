# Weather Data Analysis Project

This project is a 3-tier web application for uploading, analyzing, and visualizing csv data. I built it using `Flask` for the back end, `Jinja` templating for dynamic HTML pages, and `JavaScript` to make it more interactive. The data is stored in an `SQLite` database with `SQLAlchemy` to manage everything on the back end.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [How to Use the Application](#how-to-use-the-application)
- [File Overview](#file-overview)

## Features

- **Upload CSV Data**: Users can upload weather data in CSV format.
- **Store Data**: The uploaded data is stored in an SQLite database.
- **Data Preview**: Users can see a preview of the uploaded data in a scrollable table.
- **Data Analysis**: Users can select a numeric column and see stats like mean, median, variance, etc.
- **Visualization**: Users can create custom visualizations by choosing independent (x-axis) and dependent (y-axis) variables.

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
   - Dependencies can be installed using the following command:
    ```bash
    pip install flask sqlalchemy werkzeug pandas matplotlib matplotlib typing numpy scipy tqdm logging concurrent.futures asyncio time
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

1. **Upload a CSV File**:
    - On the home page (`/`), use the "Upload CSV File" button to upload a weather data CSV.
    - After uploading, you should see a preview of the data in a table.
      ![](./phase09-Output02.png)

2. **Data Analysis**:
    - After uploading, click "Go to Analysis Page."
    - Choose a numeric column for analysis, and click "Analyze" to get stats like mean, median, etc.
      ![](./phase09-Output03.png)

3. **Create Visualizations**:
    - On the analysis page, choose an independent (x-axis) and dependent (y-axis) variable.
    - Click "Generate Visualization" to create a scatter plot (if both variables are numeric) or a box plot (if the independent variable is categorical and the dependent variable is numeric).
    - The visualization will appear as an image on the page.
      ![](./phase09-Output04.png)

## File Overview

- **app.py**: The main Flask file that sets up routes for uploading, analyzing, and visualizing data.
- **index.html**: Homepage where you can upload CSV files and preview data.
- **analysis.html**: Analysis page where you can perform statistical analysis and create visualizations.
- **layout.html**: Base HTML layout with shared structure and styles.
- **static/**: Stores generated visualization images as PNG files.
- **uploads/**: Temporary storage for uploaded CSV files.
- **dataset.db**: SQLite database that stores the uploaded weather data.
- **data_calculator.py** and **concurrent_data_calculator.py**: Utility files for handling statistical calculations on numeric columns.

## Additional Notes

- **Data Storage**: Uploaded data is saved in an SQLite database. SQLAlchemy is used to manage the data.
- **Error Handling**: If there’s an error with the selected variables for visualization, the app shows a user-friendly error message.
- **Dependencies**: `matplotlib` is used for visualizations, `pandas` for data handling, and `SQLAlchemy` for database management.
