from functools import partial

from PySide6.QtWidgets import QMainWindow
from ui.widgets.ui_main_window import Ui_MainWindow
from src.ui.controllers.input_handler import InputHandler
from src.ui.controllers.button_handler import ButtonHandler
from src.ui.controllers.main_controller import MainController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("OCN Importer")
        self.main_controller = MainController()

        InputHandler(self, self.main_controller)
        ButtonHandler(self, self.main_controller)

    def handle_on_click_import(self):
        print("Hello")