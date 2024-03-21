from src.constants.sensor_types_constants import sensors_formats
from pathlib import Path


def is_file_format_valid(file_name):
    file_suffix = Path(file_name).suffix.lstrip(".")
    return file_suffix in sensors_formats.values()


