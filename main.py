from src.core.import_list_converter import convert_string_array_to_import_data_list
import tests.constants.data_entry_constants as test_data
from src.core.source_directory_reader import convert_valid_files_to_dictionary
from PySide6.QtWidgets import QApplication, QWidget
from ui.widgets.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

    ##TODO: Criar arquivo de configuração que contenha um dicionario como nome-formato do sensores
