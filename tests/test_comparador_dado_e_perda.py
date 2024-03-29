import unittest
from datetime import datetime, timedelta
from src.core.main_importer import calculate_date_range, compare_import_data_list_with_files_list
from tests.constants.data_entry_constants import SOURCE_DIRECTORY_FILE_LIST_EXAMPLE, IMPORT_LIST_DICTIONARY_LIST_EXAMPLE
from src.core.constants.dictionaries_constants import FILE_DATE, START_DATE


class TestComparadorDadoEPerda(unittest.TestCase):
    def setUp(self):
        self.source_directory_files_list = SOURCE_DIRECTORY_FILE_LIST_EXAMPLE
        self.import_list = IMPORT_LIST_DICTIONARY_LIST_EXAMPLE

    def test_import_data_comparison(self):
        # Execute the function to be tested
        result = compare_import_data_list_with_files_list(self.import_list, self.source_directory_files_list)

        # Verify if the result is correct
        self.assertEqual(len(result), 3)  # There should be only one found data
        self.assertEqual(result[0][FILE_DATE], self.import_list[0][START_DATE])
        self.assertEqual(result[2][FILE_DATE], self.import_list[1][START_DATE])


if __name__ == '__main__':
    unittest.main()