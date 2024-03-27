from PySide6.QtCore import QObject, Signal

"""
This class represents the main controller for the application.

The MainController class serves as the central controller for the application's logic. 
It manages the application state and data, including the source directory path, destination directory path, and import list. 
It also emits signals to indicate changes in the application state, such as the validity of input data.
"""


class MainController(QObject):
    is_inputs_valid = Signal(bool)

    def __init__(self):
        super().__init__()
        self.source_dir_path = ""
        self.destination_dir_path = ""
        self.import_list = ""

    @property
    def import_list(self):
        return self._import_list

    @import_list.setter
    def import_list(self, value):
        self._import_list = value

    @property
    def source_dir_path(self):
        return self._source_dir_path

    @source_dir_path.setter
    def source_dir_path(self, value):
        self._source_dir_path = value

    @property
    def destination_dir_path(self):
        return self._destination_dir_path

    @destination_dir_path.setter
    def destination_dir_path(self, value):
        self._destination_dir_path = value