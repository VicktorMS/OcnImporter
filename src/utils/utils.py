from datetime import timedelta
from src.core.constants.sensor_types_constants import sensors_formats


def sensor_name_to_format(sensor_name):
    try:
        return sensors_formats[sensor_name]
    except KeyError:
        print(f"The sensor '{sensor_name}' was not found in the dictionary.")
        return None


def format_to_sensor_name(formato):
    for sensor_name, sensor_format in sensors_formats.items():
        if sensor_format == format:
            print(f"The format '{format}' was not found in the dictionary.")
            return sensor_name
    return None


def calculate_date_range(start_date, end_date):
    dates = []
    current_date = start_date
    interval_minutes = 60

    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(minutes=interval_minutes)

    return dates
