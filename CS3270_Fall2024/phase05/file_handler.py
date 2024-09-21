from PyQt5.QtWidgets import QApplication, QFileDialog
import os
import logging as log


class FileHandler:
    """
    FileHandler class for retrieving the file path.

    Attributes:
        default_dir (str): Default directory for the file dialog

    Methods:
        _get_default_directory(): Returns the default directory for the file dialog
        retrieve_file(): Opens a file dialog to select the CSV file to process

    Example:
        >>> handler = FileHandler()
        >>> os.path.basename(handler.default_dir)  # Based on the existence of certain directories
        'resources'  # Or 'resources' or your home directory based on the environment
    """
    def __init__(self):
        self.default_dir = self._get_default_directory()

    @staticmethod
    def _get_default_directory() -> str:
        """
        Returns the default directory for the file dialog.
        """
        default_dir = "../resources"
        if not os.path.exists(default_dir):
            default_dir = "./resources"
        if not os.path.exists(default_dir):
            default_dir = os.path.expanduser("~")
        return default_dir

    def retrieve_file(self) -> str:
        """
        Opens a file dialog to select the CSV file to process.

        Returns:
            str: Path to the selected file
        """
        # Create an application instance
        app = QApplication([])

        # Open a file dialog to select the data file
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Select a CSV file", self.default_dir, "CSV files (*.csv);;All files (*)"
        )

        if not file_path:
            raise FileNotFoundError("No file selected")

        log.info(f"File selected: {file_path}")
        return file_path
