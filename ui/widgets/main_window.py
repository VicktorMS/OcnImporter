from functools import partial

from PySide6.QtWidgets import QMainWindow
from ui.widgets.ui_main_window import Ui_MainWindow
from src.ui.controllers.input_handler import InputHandler


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("OCN Importer")
        InputHandler(self)

