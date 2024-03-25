from src.core.data_comparator import compare_import_data_list_with_files_list
from src.core.import_list_converter import convert_string_array_to_import_data_list
from src.core.files_manipulator import convert_valid_files_to_dictionary, copy_files_to_destination_directory


def import_files_to_directory(source_directory, destination_directory, import_data_string):
    files_list = convert_valid_files_to_dictionary(source_directory)
    import_data = convert_string_array_to_import_data_list(import_data_string)
    found_data, not_found_data = compare_import_data_list_with_files_list(import_data, files_list)

    copy_files_to_destination_directory(found_data, source_directory, destination_directory)
