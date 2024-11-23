import pytest
import pandas as pd
import os
from io import StringIO
from model import clean_data, encode_data, combine_col_rows

# Sample data for tests
TRAINING_DATA = """Location,Rainfall,RainToday,MinTemp,MaxTemp,Temp9am,Temp3pm,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,WindGustDir,WindDir9am,WindDir3pm,RainTomorrow
Sydney,0.2,No,10,25,15,20,35,20,15,80,75,1015,1012,2,3,N,N,N,Yes
Melbourne,0.0,No,15,30,20,25,40,25,20,70,65,1018,1015,1,2,NE,E,SE,No
"""

TESTING_DATA = """Location,Rainfall,RainToday,MinTemp,MaxTemp,Temp9am,Temp3pm,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,WindGustDir,WindDir9am,WindDir3pm,RainTomorrow
Sydney,0.1,No,12,26,17,22,30,18,13,85,70,1016,1013,3,2,E,SE,S,No
Melbourne,0.0,Yes,16,32,21,27,45,28,22,75,60,1020,1017,1,1,NW,NE,E,Yes
"""


@pytest.fixture
def mock_data_files(monkeypatch):
    """Fixture to mock file paths and data loading."""
    def mock_read_csv(filepath, *args, **kwargs):
        if isinstance(filepath, StringIO):
            return pd.read_csv(filepath, *args, **kwargs)
        elif 'WeatherTrainingData.csv' in filepath:
            return pd.read_csv(StringIO(TRAINING_DATA))
        elif 'WeatherTestData.csv' in filepath:
            return pd.read_csv(StringIO(TESTING_DATA))
        else:
            return pd.read_csv(filepath, *args, **kwargs)

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

    def mock_exists(filepath):
        return True if 'WeatherTrainingData.csv' in filepath or 'WeatherTestData.csv' in filepath else os.path.exists(filepath)

    monkeypatch.setattr(os.path, 'exists', mock_exists)


def test_clean_data():
    data = pd.read_csv(StringIO(TRAINING_DATA))
    clean_data(data)
    assert data.isnull().sum().sum() == 0, "All missing values should be filled"


def test_encode_data():
    training_data = pd.read_csv(StringIO(TRAINING_DATA))
    testing_data = pd.read_csv(StringIO(TESTING_DATA))
    label_encoders = encode_data(training_data, testing_data)

    assert 'RainToday' in label_encoders, "RainToday should be label encoded"
    assert training_data['RainToday'].dtype == 'int32' or training_data['RainToday'].dtype == 'int64', "Encoded columns should be of integer type"


def test_combine_col_rows():
    data = pd.read_csv(StringIO(TRAINING_DATA))
    combine_table = {
        'Temp': ['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm']
    }
    combine_col_rows(data, combine_table, 'mean')
    assert 'Temp' in data.columns, "New column 'Temp' should be created"
    for col in ['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm']:
        assert col not in data.columns, f"Old column '{col}' should be dropped"


if __name__ == "__main__":
    pytest.main()
