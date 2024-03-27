from PySide6.QtCore import Signal, QObject
from src.ui.controllers.main_controller import MainController

"""
This class represents the input validation logic for the application.

The InputValidator class is responsible for validating input fields in the UI. 
It connects to various UI elements such as line edits and text edits to monitor changes and validate input data. 
When all input fields are valid, it emits a signal indicating valid inputs to the MainController.
"""


class InputValidator(QObject):
    def __init__(self, MainWindow, MainController):
        super().__init__()
        self.main_window = MainWindow
        self.main_controller = MainController
        self.check_if_inputs_are_valid()

    def check_if_inputs_are_valid(self):
        self.check_if_all_inputs_are_valid()
        self.connect_line_edit_to_validator(self.main_window.source_dir_line_edit)
        self.connect_line_edit_to_validator(self.main_window.destination_dir_line_edit)
        self.connect_text_edit_to_validator(self.main_window.input_import_list_text_edit)

    def connect_text_edit_to_validator(self, text_edit):
        text_edit.textChanged.connect(lambda: self.check_if_all_inputs_are_valid())

    def connect_line_edit_to_validator(self, line_edit):
        line_edit.textChanged.connect(lambda: self.check_if_all_inputs_are_valid())

    def check_if_all_inputs_are_valid(self):
        source_dir = self.main_window.source_dir_line_edit.text()
        destination_dir = self.main_window.destination_dir_line_edit.text()
        import_list = self.main_window.input_import_list_text_edit.toPlainText()

        if source_dir and destination_dir and import_list:
            self.main_controller.is_inputs_valid.emit(True)
        else:
            self.main_controller.is_inputs_valid.emit(False)
