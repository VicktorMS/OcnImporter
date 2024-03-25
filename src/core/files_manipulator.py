import os
import shutil
from src.core.validators.file_validation import is_file_format_valid
from datetime import datetime
from src.core.constants.dictionaries_constants import (
    FILE_CODE,
    FILE_FORMAT,
    FILE_NAME,
    FILE_DATE,
)


def convert_valid_files_to_dictionary(search_directory):
    if os.path.exists(search_directory):
        data_list = []
        files_in_directory = os.listdir(search_directory)

        for file in files_in_directory:
            if is_file_format_valid(file):
                data_list.append(parse_file_name(file))

        return data_list


def parse_file_name(file_name):
    if file_name:
        # Example file name: 23701_2023-12-19-23-00.yng_gz
        separated_file_name = file_name.split(".")

        code_and_date = separated_file_name[0].split("_")
        date = datetime.strptime(code_and_date[1], '%Y-%m-%d-%H-%M')

        # Example result in Array ['23701_2023', '12', '19', '23', '00.yng_gz']
        file_name_dict = {
            FILE_CODE: code_and_date[0],
            FILE_FORMAT: separated_file_name[1],
            FILE_NAME: file_name,
            FILE_DATE: date
        }

        return file_name_dict
    else:
        return None


def copy_files_to_destination_directory(file_list, source_directory, destination_directory):
    # Check if the source and destination directories exist
    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' not found.")
        return
    if not os.path.exists(destination_directory):
        print(f"Destination directory '{destination_directory}' not found.")
        return

    # Loop over each file in the list and attempt to copy it to the destination directory
    for file in file_list:
        file_full_path = os.path.join(source_directory, file.get(FILE_NAME))
        try:
            shutil.copy(file_full_path, destination_directory)
            print(f"File '{file.get(FILE_NAME)}' successfully copied to '{destination_directory}'.")
        except FileNotFoundError:
            print(f"File '{file.get(FILE_NAME)}' not found in the source directory.")
        except PermissionError:
            print(f"Permission denied to copy file '{file.get(FILE_NAME)}' to the destination directory.")
        except Exception as e:
            print(f"An error occurred while copying file '{file.get(FILE_NAME)}': {e}")