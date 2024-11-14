from PyQt5.QtWidgets import QApplication, QFileDialog
import os
import logging as log


class FileHandler:
    """
    FileHandler class for retrieving the file path.

    Attributes:
        default_dir (str): Default directory for the file dialog.
        app (QApplication): A single instance of QApplication for handling dialogs.

    Methods:
        _get_default_directory(): Returns the default directory for the file dialog.
        _get_file_type_and_filter(file_type: str): Returns the file filter based on the file type.
        ensure_app(): Ensures that a single instance of QApplication exists.
        get_file(): Opens a file dialog to select the specified file type.
        get_write_path(): Opens a file dialog to select a save location for the specified file type.
    """
    default_dir: str = ""
    home_dir: str = os.path.expanduser("~")
    app: QApplication = None

    def __init__(self):
        if not FileHandler.default_dir:
            FileHandler.default_dir = self._get_default_directory()

    @classmethod
    def _get_default_directory(cls) -> str:
        """
        Returns the default directory for the file dialog.
        """
        default_dir = "../resources"
        if not os.path.exists(default_dir):
            default_dir = "./resources"
        if not os.path.exists(default_dir):
            default_dir = cls.home_dir
        return default_dir

    @staticmethod
    def _get_file_type_and_filter(file_type: str) -> tuple[str, str]:
        """
        Returns the file filter based on the file type.

        Args:
            file_type (str): The file type to filter for.

        Returns:
            tuple[str, str]: The file type and its corresponding filter.
        """
        file_type = file_type.lower().strip()
        if "." in file_type:
            file_type = file_type.replace(".", "")

        types = ["txt", "csv", "xlsx", "json", "png"]
        if file_type not in types:
            raise ValueError(f"Unsupported file type: {file_type}")

        return file_type, f"Text files (*.{file_type});;All files (*)"

    @classmethod
    def ensure_app(cls):
        """
        Ensures that a single instance of QApplication exists.
        """
        if not cls.app:
            cls.app = QApplication.instance() or QApplication([])

    @classmethod
    def get_file(cls, file_type: str = "txt") -> str:
        """
        Opens a file dialog to select the specified file type.

        Returns:
            str: Path to the selected file.
        """
        cls.ensure_app()

        file_type, file_filter = cls._get_file_type_and_filter(file_type)

        file_path, _ = QFileDialog.getOpenFileName(
            None, f"Select a {file_type} file", cls.default_dir, file_filter
        )

        if not file_path:
            raise FileNotFoundError("No file selected")

        log.info(f"File selected: {file_path}")
        return file_path

    @classmethod
    def get_file_write_path(cls, file_type: str) -> str:
        """
        Opens a file dialog to select the save location for the specified file type.

        Returns:
            str: Path to the selected file.
        """
        cls.ensure_app()

        file_type, file_filter = cls._get_file_type_and_filter(file_type)

        file_path, _ = QFileDialog.getSaveFileName(
            None, f"Save {file_type} file", cls.default_dir, file_filter, f"Out.{file_type}"
        )

        if not file_path:
            raise FileNotFoundError("No path selected")

        log.info(f"Path selected: {file_path}")
        return file_path

    @classmethod
    def get_folder_write_path(cls) -> str:
        """
        Opens a file dialog to select the save location for the specified file type.

        Returns:
            str: Path to the selected file.
        """
        cls.ensure_app()

        file_path = QFileDialog.getExistingDirectory(
            None, f"Select a folder", cls.default_dir
        ) + "/"

        if not file_path:
            raise FileNotFoundError("No path selected")

        log.info(f"Path selected: {file_path}")
        return file_path
