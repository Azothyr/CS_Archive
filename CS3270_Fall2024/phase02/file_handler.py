from PyQt5.QtWidgets import QApplication, QFileDialog
import os


def retrieve_file() -> str:
    """
    Open a file dialog to select the data file to process

    Return:
        str: Path to the selected file
    """
    # Create an application instance
    app = QApplication([])

    # Set the default directory to the resources directory
    default_dir = "../resources"
    if not os.path.exists(default_dir):
        default_dir = "./resources"
    if not os.path.exists(default_dir):
        # Get the user's home directory
        default_dir = os.path.expanduser("~")

    # Open a file dialog to select the data file
    file_path, _ = QFileDialog.getOpenFileName(
        None, "Select a CSV file", default_dir, "CSV files (*.csv);;All files (*)"
    )

    if not file_path:
        raise FileNotFoundError("No file selected")

    return file_path
