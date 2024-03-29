import unittest
from datetime import datetime, timedelta

from src.utils.utils import calculate_date_range


class TestUtils(unittest.TestCase):
    """Tests for utility functions on utils.py"""

    def test_date_range(self):
        start_date = datetime(2023, 12, 20, 16, 00)
        end_date = datetime(2023, 12, 21, 13, 00)
        date_range = calculate_date_range(start_date, end_date)

        expected_dates = [start_date + timedelta(hours=i) for i in range(0, 22)]

        self.assertEqual(date_range, expected_dates, "The date range is not as expected")

    def test_same_dates_range(self):
        date = datetime(2023, 4, 26, 16, 00)
        date_range = calculate_date_range(date, date)

        self.assertEqual(date_range, date, "Shouldn't return any range, only the same date")
