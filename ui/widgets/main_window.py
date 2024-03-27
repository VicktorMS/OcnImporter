from functools import partial

from PySide6.QtWidgets import QMainWindow
from ui.widgets.ui_main_window import Ui_MainWindow
from src.ui.controllers.input_handler import InputHandler
from src.ui.controllers.button_handler import ButtonHandler
from src.ui.controllers.main_controller import MainController

"""
This is the main class responsible for handling the UI.

This class inherits objects from `UI_MainWindow`, which is an auto-generated class resulting from compiling a .ui file. 
This inheritance allows access to every GUI element defined in the .ui file, facilitating interaction and control over the UI.
"""


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("OCN Importer")
        self.main_controller = MainController()
        self.setFixedSize(720, 640)

        ButtonHandler(self, self.main_controller)
        InputHandler(self, self.main_controller)
