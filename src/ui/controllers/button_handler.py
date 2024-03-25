from src.core.import_list_converter import convert_string_array_to_import_data_list


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
        string_array = self.main_controller.import_list
        import_list = convert_string_array_to_import_data_list(string_array)
        print("Hello ", import_list)

    def setup_copy_button_callback(self):
        self.main_window.copy_import_results_btn.clicked.connect(lambda: print("Copy Btn"))

    def hide_development_buttons(self):
        self.main_window.check_import_btn.hide()
        self.main_window.use_import_list_file_btn.hide()
        self.main_window.export_import_results_btn.hide()
