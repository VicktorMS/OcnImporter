from src.core.constants.dictionaries_constants import START_DATE, END_DATE, FILE_DATE
from src.utils.utils import calculate_date_range


def compare_import_data_list_with_files_list(import_data_list, files_list):
    found_data = []
    not_found_data = []

    try:
        # Check if both input lists are not empty
        if not import_data_list:
            raise ValueError("Import data list is empty")
        if not files_list:
            raise ValueError("Files list is empty")

        for import_data in import_data_list:
            start_date_import_data = import_data.get(START_DATE)
            end_date_import_data = import_data.get(END_DATE)

            # Check if the import data has a valid date range
            if start_date_import_data is None or end_date_import_data is None:
                raise ValueError("Import data is missing date information")

            if start_date_import_data < end_date_import_data:
                date_range = calculate_date_range(start_date_import_data, end_date_import_data)
            else:
                date_range = [start_date_import_data]  # If no range, use only the start date

            # Flag to track if import data is found in any files
            found = False

            # Check if any of the files match the import date
            for import_date in date_range:
                for data in files_list:
                    if import_date == data.get(FILE_DATE):
                        found_data.append(data)
                        found = True
                        break
                if found:  # That might cause some issues
                    break

            # If import data is not found in any files, add it to the not_found_data list
            if not found:
                not_found_data.append(import_data)

        return found_data, not_found_data

    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


"""
No Exception Treatment code

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
"""
