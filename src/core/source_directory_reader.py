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

