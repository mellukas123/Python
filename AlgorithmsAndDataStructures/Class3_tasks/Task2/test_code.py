import unittest
from unittest.mock import patch
from task_code import clean_data, save_to_csv

class TestTaskCode(unittest.TestCase):
    @patch('task_code.json.load')
    def test_clean_data(self, mock_load):
        mock_load.return_value = {
            'data': [
                {'id': '1', 'name': 'Product 1', 'category': 'Electronics'},
                {'id': '2', 'name': 'Product 2', 'category': 'Clothing'}
            ]
        }
        expected_output = [
            {'id': '1', 'name': 'Product 1', 'category': 'Electronics', 'price': '', 'currency': '', 'stock': '', 'description': '', 'manufacturer': '', 'warranty': '', 'extra_field': ''},
            {'id': '2', 'name': 'Product 2', 'category': 'Clothing', 'price': '', 'currency': '', 'stock': '', 'description': '', 'manufacturer': '', 'warranty': '', 'extra_field': ''}
        ]
        self.assertEqual(clean_data(), expected_output)

    @patch('task_code.csv.DictWriter')
    def test_save_to_csv(self, mock_dict_writer):
        cleaned_data = [
            {'id': '1', 'name': 'Product 1', 'category': 'Electronics', 'price': '', 'currency': '', 'stock': '', 'description': '', 'manufacturer': '', 'warranty': '', 'extra_field': ''},
            {'id': '2', 'name': 'Product 2', 'category': 'Clothing', 'price': '', 'currency': '', 'stock': '', 'description': '', 'manufacturer': '', 'warranty': '', 'extra_field': ''}
        ]
        save_to_csv(cleaned_data, 'test.csv')
        mock_dict_writer.assert_called_once_with('test.csv', fieldnames=['id', 'name', 'category', 'price', 'currency', 'stock', 'description', 'manufacturer', 'warranty', 'extra_field'])
        mock_dict_writer.return_value.writeheader.assert_called_once()
        mock_dict_writer.return_value.writerows.assert_called_once_with(cleaned_data)

if __name__ == '__main__':
    unittest.main()
