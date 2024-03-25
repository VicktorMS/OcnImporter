from src.core.import_list_converter import convert_string_array_to_import_data_list
from src.core.main_importer import import_files_to_directory
from src.core.source_directory_reader import convert_valid_files_to_dictionary



class ButtonHandler:
    def __init__(self, MainWindow, MainController):
        self.main_window = MainWindow
        self.main_controller = MainController

        self.setup_button_callbacks()
        self.hide_development_buttons()

    def setup_button_callbacks(self):
        self.setup_paste_button_callback()
        self.setup_import_button_callback()
        self.setup_copy_button_callback()

    def setup_paste_button_callback(self):
        self.main_window.paste_import_list_btn.clicked.connect(lambda: print("Paste Btn"))

    def setup_import_button_callback(self):
        self.main_window.import_btn.clicked.connect(lambda: self.process_data_string())

    def process_data_string(self):
        destination_path = self.main_controller.destination_dir_path
        source_path = self.main_controller.source_dir_path
        import_list = self.main_controller.import_list
        import_files_to_directory(source_path, destination_path, import_list)

    def setup_copy_button_callback(self):
        self.main_window.copy_import_results_btn.clicked.connect(lambda: print("Copy Btn"))

    def hide_development_buttons(self):
        self.main_window.check_import_btn.hide()
        self.main_window.use_import_list_file_btn.hide()
        self.main_window.export_import_results_btn.hide()
