from pandas import DataFrame, read_csv
from pathlib import Path


def read_data_from_csv(path: str | Path) -> DataFrame:
    """
    Read the data from the csv file

    Parameters:
        path (str | Path): Path to the csv file

    Return:
         DataFrame: Dataframe of the data
    """
    return read_csv(path)