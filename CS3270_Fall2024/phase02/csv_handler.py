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
    if isinstance(path, Path):
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
    else:
        if not Path(path).exists():
            raise FileNotFoundError(f"File not found: {path}")

    try:
        return_data = read_csv(path)
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

    return return_data
