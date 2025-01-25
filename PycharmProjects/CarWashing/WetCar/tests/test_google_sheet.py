import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarWashing.settings")
django.setup()
from django.test import TestCase
from unittest.mock import patch
from google_sheets.sheet import write_to_sheet, gc


class AddDataGSTestCase(TestCase):
    @patch("google_sheets.sheet.write_to_sheet")  # Mocking the full path of the method
    def test_add_data(self, mock_write_to_sheet):
        # Mock the behavior of `write_to_sheet` if needed (optional)
        #mock_write_to_sheet.return_value = None

        # Invoke the mocked function instead of the real one
        test_data = ["Hello", "22.01"]
        mock_write_to_sheet(test_data)

        # Check the mocked function call
        mock_write_to_sheet.assert_called_once_with(test_data)

