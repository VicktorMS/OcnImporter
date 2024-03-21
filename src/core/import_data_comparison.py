from src.utils.utils import calculate_date_range
from src.constants.dictionaries_constants import (
    START_DATE,
    END_DATE,
    FILE_DATE
)


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
    print(found_data)
    return found_data



