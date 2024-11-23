import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.metrics import accuracy_score


def clean_data(data):
    for col in data.columns:
        # Fill missing values with median for numeric columns and mode for categorical columns
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].median())


def encode_data(training_data, testing_data):
    label_encoders = {}
    for col in training_data.select_dtypes(include='object').columns:
        # Train the LabelEncoder on the combined training and test data to ensure consistency
        label_encoder = LabelEncoder()
        combined_data = pd.concat([training_data[col], testing_data[col]], axis=0)
        label_encoder.fit(combined_data)

        # Transform both training and test data
        training_data[col] = label_encoder.transform(training_data[col])
        testing_data[col] = label_encoder.transform(testing_data[col])

        # Save the label encoder for later use (for new incoming data)
        label_encoders[col] = label_encoder

    return label_encoders


def combine_col_rows(data, combine_table, combine_type):
    for new_col, old_cols in combine_table.items():
        if combine_type == 'mean':
            data[new_col] = data[old_cols].mean(axis=1)
        elif combine_type == 'string':
            data[new_col] = data[old_cols].apply(
                lambda x: ''.join(sorted(set(''.join(str(val) for val in x if pd.notna(val)))))
                , axis=1)
        data.drop(columns=old_cols, inplace=True)


def train_model():
    training_file = os.path.join(os.path.dirname(__file__), 'WeatherTrainingData.csv')
    testing_file = os.path.join(os.path.dirname(__file__), 'WeatherTestData.csv')

    if not os.path.exists(training_file) or not os.path.exists(testing_file):
        raise FileNotFoundError("Training or testing data not found")

    # Load training and testing data
    training_data = pd.read_csv(training_file)
    testing_data = pd.read_csv(testing_file)

    # Drop columns with too many missing values or that aren't useful
    columns_to_drop = ['row ID', 'Evaporation', 'Sunshine']
    training_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
    testing_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    # Combine and then drop columns by getting their mean (for columns with similar data)
    numeric_combine_table = {
        'Temp': ['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm'],
        'WindSpeed': ['WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm'],
        'Humidity': ['Humidity9am', 'Humidity3pm'],
        'Pressure': ['Pressure9am', 'Pressure3pm'],
        'Cloud': ['Cloud9am', 'Cloud3pm'],
    }
    category_combine_table = {
        'WindDir': ['WindGustDir', 'WindDir9am', 'WindDir3pm']
    }
    combine_col_rows(training_data, numeric_combine_table, 'mean')
    combine_col_rows(testing_data, numeric_combine_table, 'mean')
    combine_col_rows(training_data, category_combine_table, 'string')
    combine_col_rows(testing_data, category_combine_table, 'string')

    # New Dataset after combining columns:
    # Location, Rainfall, RainToday, *RainTomorrow, Temp, WindSpeed, Humidity, Pressure, Cloud, WindDir

    # Fill missing values with median or mode
    clean_data(training_data)
    clean_data(testing_data)

    # Encode categorical columns
    label_encoders = encode_data(training_data, testing_data)

    # Features and labels for training
    X = training_data.drop('RainTomorrow', axis=1)
    y = training_data['RainTomorrow']

    test_size = 0.2
    random_state = 42
    estimators = 100

    # Split the data into training and validation sets (80% train, 20% validation)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Train the model using Random Forest Algorithm
    model = RandomForestClassifier(n_estimators=estimators, random_state=random_state)
    model.fit(X_train, y_train)

    # Save the trained model and label encoders
    joblib.dump(model, 'rain_predictor.pkl')
    joblib.dump(label_encoders, 'label_encoders.pkl')

    # Evaluate the model on the validation set to calculate accuracy
    y_val_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_val_pred) * 100
    print(f"Validation Accuracy: {accuracy:.0f}%")


if __name__ == "__main__":
    train_model()
