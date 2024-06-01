import unittest
import json
from task_code import read_files_in_directory, extract_translations, write_result_file

class TestTaskCode(unittest.TestCase):
    def test_read_files_in_directory(self):
        # Test case 1: Test with valid directory path
        directory_path = 'french'  # Adjust the folder path accordingly
        expected_output = {'products.json': {'key': 'TBT:value'}}
        self.assertEqual(read_files_in_directory(directory_path), expected_output)

        # Test case 2: Test with invalid directory path
        directory_path = 'invalid_directory_path'
        expected_output = {}
        self.assertEqual(read_files_in_directory(directory_path), expected_output)

    def test_extract_translations(self):
        # Test case 1: Test with valid input data
        data = {'key': 'TBT:value'}
        translations = {}
        file_name = 'test_file.json'
        expected_output = {'test_file.json': {'key': 'TBT:value'}}
        extract_translations(data, translations, file_name)
        self.assertEqual(translations, expected_output)

        # Test case 2: Test with invalid input data
        data = {'key': 'invalid_value'}
        translations = {}
        file_name = 'test_file.json'
        expected_output = {}
        extract_translations(data, translations, file_name)
        self.assertEqual(translations, expected_output)

    def test_write_result_file(self):
        # Test case 1: Test with valid input data
        translations = {'test_file.json': {'key': 'TBT:value'}}
        expected_output = {'test_file.json': {'key': 'TBT:value'}}
        write_result_file(translations)
        with open('result.json', 'r') as file:
            result_data = json.load(file)
        self.assertEqual(result_data, expected_output)

        # Test case 2: Test with invalid input data
        translations = {'test_file.json': {'key': 'invalid_value'}}
        expected_output = {'test_file.json': {'key': 'invalid_value'}}
        write_result_file(translations)
        with open('result.json', 'r') as file:
            result_data = json.load(file)
        self.assertEqual(result_data, expected_output)

if __name__ == '__main__':
    unittest.main()
expected_output = {
    'products.json': {'key': 'TBT:value'},
    'discounts.json': {'discount-advanced': 'TBT:Discount Advanced Search'},
    # Lisa siia ka muud failid ja nende oodatud väljundid
}