from PySide6.QtCore import Signal, QObject
from src.ui.controllers.main_controller import MainController


class InputValidator(QObject):

    def __init__(self, MainWindow, MainController):
        super().__init__()
        self.main_window = MainWindow
        self.main_controller = MainController
        self.check_if_inputs_are_valid()

    def check_if_inputs_are_valid(self):
        self.connect_line_edit_to_validator(self.main_window.source_dir_line_edit)
        self.connect_line_edit_to_validator(self.main_window.destination_dir_line_edit)
        self.connect_text_edit_to_validator(self.main_window.input_import_list_text_edit)

    def connect_text_edit_to_validator(self, text_edit):
        self.check_for_blank_string(text_edit.toPlainText())
        text_edit.textChanged.connect(lambda: self.check_for_blank_string(text_edit.toPlainText()))

    def connect_line_edit_to_validator(self, line_edit):
        self.check_for_blank_string(line_edit.text())
        line_edit.textChanged.connect(lambda: self.check_for_blank_string(line_edit.text()))

    def check_for_blank_string(self, line_edit):
        if line_edit == "" or line_edit is None:
            print("Inputs aren't valid")
        else:
            # print("Inputs are valid")
            self.main_controller.valid_inputs_signal.emit(True)