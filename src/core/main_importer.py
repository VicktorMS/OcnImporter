import os.path
import shutil

from src.core.import_list_converter import convert_string_array_to_import_data_list
from src.core.source_directory_reader import convert_valid_files_to_dictionary
from src.utils.utils import calculate_date_range
from src.core.constants.dictionaries_constants import (
    START_DATE,
    END_DATE,
    FILE_DATE,
    FILE_NAME
)


def import_files_to_directory(source_directory, destination_directory, import_data_string):
    files_list = convert_valid_files_to_dictionary(source_directory)
    import_data = convert_string_array_to_import_data_list(import_data_string)
    found_data = compare_import_data_list_with_files_list(import_data, files_list)

    copy_files_to_destination_directory(found_data, source_directory, destination_directory)


def copy_files_to_destination_directory(file_list, source_directory, destination_directory):
    for file in file_list:
        file_full_path = os.path.join(source_directory, file[FILE_NAME])
        shutil.copy(file_full_path, destination_directory)


def compare_import_data_list_with_files_list(import_data_list, files_list):
    found_data = []
    for import_data in import_data_list:
        start_date_import_data = import_data[START_DATE]
        end_date_import_data = import_data[END_DATE]

        # Check if the import data has a date range
        if start_date_import_data < end_date_import_data:
            date_range = calculate_date_range(start_date_import_data, end_date_import_data)
        else:
            date_range = [start_date_import_data]  # If no range, use only the start date

        for import_date in date_range:
            for data in files_list:
                if import_date == data[FILE_DATE]:
                    found_data.append(data)
    return found_data



