from src.utils.utils import sensor_name_to_format
from datetime import datetime
from src.constants.dictionaries_constants import (
    SENSOR_PARAM_UCD,
    SENSOR_NAME,
    SENSOR_FORMAT,
    START_DATE,
    END_DATE,
)


# Processa informacoes sobre perdas de um array do pyPerdas
def convert_string_array_to_import_data_list(string_array):
    import_data_list = []
    for string in string_array:
        import_data = extract_import_data_from_string(string)
        import_data_list.append(import_data)
    return remove_duplicate_import_data(import_data_list)


def remove_duplicate_import_data(import_data_array):
    filtered_import_data = []
    unique_start_dates = set()
    unique_end_dates = set()

    for import_data in import_data_array:
        start_date = import_data[START_DATE]
        end_date = import_data[END_DATE]

        if (end_date not in unique_end_dates) and (start_date not in unique_start_dates):
            unique_end_dates.add(end_date)
            unique_start_dates.add(start_date)
            filtered_import_data.append(import_data)

    return filtered_import_data


def extract_import_data_from_string(raw_data):
    parts_import_data = raw_data.split()

    time_period = parts_import_data[2].split("->")

    sensor = parts_import_data[0].split('][')
    part_initial_date = parts_import_data[1]

    start_datetime = f"{part_initial_date} {time_period[0]}"
    end_datetime = f"{time_period[1]} {parts_import_data[3]}"

    param_and_ucd = sensor[0].lstrip('[')
    sensor_name = sensor[1].rstrip(':').replace(']', '')

    start_date = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M')

    import_data_dict = {
        SENSOR_PARAM_UCD: param_and_ucd,
        SENSOR_NAME: sensor_name,
        SENSOR_FORMAT: sensor_name_to_format(sensor_name), # Refactor
        START_DATE: start_date,
        END_DATE: end_date,
    }

    return import_data_dict