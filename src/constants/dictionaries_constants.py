# Import Data Dictionary
SENSOR_PARAM_UCD = "param_ucd"
SENSOR_NAME = "sensor"
SENSOR_FORMAT = "format"
START_DATE = "start_date"
END_DATE = "end_date"
""" EXAMPLE
{
    'param_ucd': 'BRM_1_ANNANERY', 
    'sensor': 'YOUNG', 
    'format': 'yng_gz',
    'start_date': datetime.datetime(2023, 12, 15, 17, 0), 
    'end_date': datetime.datetime(2023, 12, 15, 17, 0)
 }
 """

# File Dictionary from Search Directory
FILE_CODE = "file_code"
FILE_FORMAT = "file_format"
FILE_NAME = "file_name"
FILE_DATE = "file_date"

""" EXAMPLE
{
    'file_code': '23701',
    'file_format': 'yng_gz',
    'file_name': '23701_2023-12-14-20-00.yng_gz',
    'file_date': datetime.datetime(2023, 12, 14, 20, 0)
}
"""
