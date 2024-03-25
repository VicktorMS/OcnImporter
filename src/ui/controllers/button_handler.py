from src.ui.controllers.main_controller import MainController


class ButtonHandler:
    def __init__(self, MainWindow, MainController):
        self.main_window = MainWindow
        self.main_controller = MainController

        self.on_paste_button_clicked()
        self.on_copy_button_clicked()
        self.on_import_button_clicked()

        # Development
        self.hide_in_development_buttons()

    def disable_button_if_invalid_inputs(self):
        pass

    def on_paste_button_clicked(self):
        self.main_window.paste_import_list_btn.clicked.connect(lambda: print("Paste Btn"))

    def on_import_button_clicked(self):
        self.main_window.import_btn.clicked.connect(
            lambda: print(
                "Source path: ", self.main_controller.source_dir_path,
                "\nDestination path: ", self.main_controller.destination_dir_path,
                "\nImport List: ", self.main_controller.import_list
            ))

    def on_copy_button_clicked(self):
        self.main_window.copy_import_results_btn.clicked.connect(lambda: print("Copy Btn"))







    # This method is only for development
    def hide_in_development_buttons(self):
        self.main_window.check_import_btn.hide()
        self.main_window.use_import_list_file_btn.hide()
        self.main_window.export_import_results_btn.hide()