from PySide6.QtCore import Signal, QObject
from src.ui.controllers.main_controller import MainController
from src.ui.controllers.input_validator import InputValidator


class InputHandler(QObject):

    def __init__(self, MainWindow, MainController):
        super().__init__()
        self.main_window = MainWindow
        self.main_controller = MainController
        InputValidator(MainWindow, MainController)

        self.update_source_dir_path_in_main_controller()
        self.update_destination_dir_path_in_main_controller()
        self.update_import_list_in_main_controller()

    def update_import_list_in_main_controller(self):
        self.main_window.input_import_list_text_edit.textChanged.connect(
            lambda: setattr(
                self.main_controller,
                'import_list',
                self.main_window.input_import_list_text_edit.toPlainText()
            )
        )

    def update_source_dir_path_in_main_controller(self):
        self.main_window.source_dir_line_edit.textChanged.connect(
            lambda: setattr(
                self.main_controller,
                'source_dir_path',
                self.main_window.source_dir_line_edit.text()
            )
        )

    def update_destination_dir_path_in_main_controller(self):
        self.main_window.destination_dir_line_edit.textChanged.connect(
            lambda: setattr(
                self.main_controller,
                'destination_dir_path',
                self.main_window.destination_dir_line_edit.text()
            )
        )