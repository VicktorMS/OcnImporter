from PySide6.QtWidgets import QApplication, QWidget
from ui.widgets.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

    ##TODO: Criar arquivo de configuração que contenha um dicionario como nome-formato do sensores
