from PySide6.QtCore import QObject, Signal


class MainController(QObject):
    is_inputs_valid = Signal(bool)

    def __init__(self):
        super().__init__()
        self.source_dir_path = ""
        self.destination_dir_path = ""
        self.import_list = ""

    @property
    def import_list(self):
        return self._import_list

    @import_list.setter
    def import_list(self, value):
        self._import_list = value

    @property
    def source_dir_path(self):
        return self._source_dir_path

    @source_dir_path.setter
    def source_dir_path(self, value):
        self._source_dir_path = value

    @property
    def destination_dir_path(self):
        return self._destination_dir_path

    @destination_dir_path.setter
    def destination_dir_path(self, value):
        self._destination_dir_path = value