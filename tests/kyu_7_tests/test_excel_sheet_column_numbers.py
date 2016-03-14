import unittest

from katas.kyu_7.excel_sheet_column_numbers import title_to_number


class TitleToNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(title_to_number('A'), 1)

    def test_equals_2(self):
        self.assertEqual(title_to_number('Z'), 26)

    def test_equals_3(self):
        self.assertEqual(title_to_number('AA'), 27)

    def test_equals_4(self):
        self.assertEqual(title_to_number('AZ'), 52)

    def test_equals_5(self):
        self.assertEqual(title_to_number('BA'), 53)


if __name__ == '__main__':
    unittest.main()
