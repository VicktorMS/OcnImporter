# This file contains testing variables, change to suit your needs
from datetime import datetime

SOURCE_DIRECTORY_EXAMPLE = "/home/victormoraes/Documents/Projetos/OCEANOP/ocn_importer/TESTES/HIST"
DESTINATION_DIRECTORY_EXAMPLE = "/home/victormoraes/Documents/Projetos/OCEANOP/ocn_importer/TESTES/PROD"

# Source directory with random files and actual file_date.
BAD_SOURCE_DIRECTORY_EXAMPLE = "/home/victormoraes/Documents/Projetos/OCEANOP/ocn_importer/TESTES/BAD_HIST"

# Examples of an expected user input for import list
IMPORT_LIST_JSON_EXAMPLE1 = [
    "[CRT_1_ANNANERY][MIROS]: 2023-12-03 13:00->2023-12-03 13:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-03 13:00->2023-12-03 13:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-09 06:00->2023-12-09 06:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-09 06:00->2023-12-09 06:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-10 15:00->2023-12-10 15:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-10 15:00->2023-12-10 15:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-11 11:00->2023-12-11 11:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-11 11:00->2023-12-11 11:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-11 20:00->2023-12-11 20:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-11 20:00->2023-12-11 20:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-13 20:00->2023-12-13 20:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-13 20:00->2023-12-13 20:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-13 23:00->2023-12-14 00:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-13 23:00->2023-12-14 00:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-14 20:00->2023-12-14 20:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-14 20:00->2023-12-14 20:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-15 09:00->2023-12-15 09:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-15 09:00->2023-12-15 09:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-17 09:00->2023-12-17 09:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-17 09:00->2023-12-17 09:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-18 09:00->2023-12-18 09:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-18 09:00->2023-12-18 09:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-18 17:00->2023-12-18 17:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-18 17:00->2023-12-18 17:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-18 20:00->2023-12-18 20:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-18 20:00->2023-12-18 20:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-19 17:00->2023-12-19 17:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-19 17:00->2023-12-19 17:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-20 08:00->2023-12-20 08:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-20 08:00->2023-12-20 08:00",
    "[CRT_1_ANNANERY][MIROS]: 2023-12-21 16:00->2023-12-21 16:00",
    "[RDR_1_ANNANERY][MIROS]: 2023-12-21 16:00->2023-12-21 16:00"
]
IMPORT_LIST_JSON_EXAMPLE2 = [
    "[BRM_1_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[BRM_2_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[TMP_1_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[UMD_1_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[ANM_1_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[ANM_2_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[BRM_1_ANNANERY][YOUNG]: 2023-12-16 13:00->2023-12-16 13:00",
    "[BRM_2_ANNANERY][YOUNG]: 2023-12-16 13:00->2023-12-16 13:00",
    "[TMP_1_ANNANERY][YOUNG]: 2023-12-16 13:00->2023-12-16 13:00",
    "[UMD_1_ANNANERY][YOUNG]: 2023-12-16 13:00->2023-12-16 13:00",
    "[ANM_1_ANNANERY][YOUNG]: 2023-12-16 13:00->2023-12-16 13:00",
    "[ANM_2_ANNANERY][YOUNG]: 2023-12-16 13:00->2023-12-16 13:00",
    "[BRM_1_ANNANERY][YOUNG]: 2023-12-22 17:00->2023-12-23 11:00",
    "[BRM_2_ANNANERY][YOUNG]: 2023-12-22 17:00->2023-12-23 11:00",
    "[TMP_1_ANNANERY][YOUNG]: 2023-12-22 17:00->2023-12-23 11:00",
    "[UMD_1_ANNANERY][YOUNG]: 2023-12-22 17:00->2023-12-23 11:00",
    "[ANM_1_ANNANERY][YOUNG]: 2023-12-22 17:00->2023-12-23 11:00",
    "[ANM_1_ANNANERY][YOUNG]: 2023-12-15 17:00->2023-12-15 17:00",
    "[TEST_ANNANERY][YOUNG]: 2023-12-24 17:00->2023-12-24 17:00",
    "[TEST_ANNANERY][YOUNG]: 2023-12-24 19:00->2023-12-24 20:00",
    "[N/A_ANNANERY][YOUNG]: 2025-12-24 19:00->2025-12-24 20:00"

]

# Example of a processed json import list
IMPORT_LIST_DICTIONARY_LIST_EXAMPLE = [
            {
                'param_ucd': 'BRM_1_ANNANERY',
                'sensor': 'YOUNG',
                'format': 'yng_gz',
                'start_date': datetime(2023, 12, 14, 19, 0),
                'end_date': datetime(2023, 12, 14, 20, 0)
            },
            {
                'param_ucd': 'BRM_1_ANNANERY',
                'sensor': 'YOUNG',
                'format': 'yng_gz',
                'start_date': datetime(2023, 12, 15, 7, 0),
                'end_date': datetime(2023, 12, 15, 7, 0)
            }
        ]

# Example of a list of processed files in a directory (Source Directory)
SOURCE_DIRECTORY_FILE_LIST_EXAMPLE = [
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-09-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 9, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-10-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 10, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-07-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 7, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-13-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 13, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-16-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 16, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-11-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 11, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-23-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 23, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-14-19-00.yng_gz",
                "file_date": datetime(2023, 12, 14, 19, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-14-22-00.yng_gz",
                "file_date": datetime(2023, 12, 14, 22, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-14-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 14, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-12-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 12, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-06-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 6, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-01-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 1, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-20-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 20, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-22-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 22, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-19-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 19, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-18-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 18, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-03-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 3, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-14-21-00.yng_gz",
                "file_date": datetime(2023, 12, 14, 21, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-14-23-00.yng_gz",
                "file_date": datetime(2023, 12, 14, 23, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-05-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 5, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-00-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 0, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-17-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 17, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-21-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 21, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-14-20-00.yng_gz",
                "file_date": datetime(2023, 12, 14, 20, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-14-18-00.yng_gz",
                "file_date": datetime(2023, 12, 14, 18, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-04-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 4, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-08-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 8, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-15-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 15, 0),
            },
            {
                "file_code": "23701",
                "file_format": "yng_gz",
                "file_name": "23701_2023-12-15-02-00.yng_gz",
                "file_date": datetime(2023, 12, 15, 2, 0),
            },
        ]
