import unittest
from parse_expenses import parse_expenses
import datetime

class TestParseExpenses(unittest.TestCase):

    def test_valid_expenses(self):
        expenses_data = '''2023-01-02 -34.01 USD
2023-01-03 2.59 DKK
2023-01-03 -2.72 EUR'''
        expected_result = [
            (datetime.datetime(2023, 1, 2), -34.01, 'USD'),
            (datetime.datetime(2023, 1, 3), 2.59, 'DKK'),
            (datetime.datetime(2023, 1, 3), -2.72, 'EUR')
        ]
        self.assertEqual(parse_expenses(expenses_data), expected_result)

    def test_with_comments_and_empty_lines(self):
        expenses_data = '''# This is a comment
2023-01-02 -34.01 USD

2023-01-03 2.59 DKK
# Another comment
2023-01-03 -2.72 EUR'''
        expected_result = [
            (datetime.datetime(2023, 1, 2), -34.01, 'USD'),
            (datetime.datetime(2023, 1, 3), 2.59, 'DKK'),
            (datetime.datetime(2023, 1, 3), -2.72, 'EUR')
        ]
        self.assertEqual(parse_expenses(expenses_data), expected_result)

    def test_invalid_data_format(self):
        expenses_data = '''2023-01-02 -34.01 USD
2023-01-03 2.59
2023-01-03 -2.72 EUR'''
        with self.assertRaises(ValueError):
            parse_expenses(expenses_data)

if __name__ == '__main__':
    unittest.main()