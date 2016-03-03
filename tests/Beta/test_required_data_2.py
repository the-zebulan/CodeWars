import unittest

from Beta.required_data_2 import given_nth_value


class RequiredData2TestCase(unittest.TestCase):
    def setUp(self):
        self.list_1 = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31, 34, -16, -16, 8, 8]
        self.list_2 = [3, 3, -1, 10, 6, 8, -5, 'Yes', 4, 22, 31]
        self.list_3 = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31]

    def test_equals(self):
        self.assertEqual(given_nth_value(self.list_1, 5, 'min'), 4)

    def test_equals_2(self):
        self.assertEqual(given_nth_value(self.list_1, 6, 'max'), 6)

    def test_equals_3(self):
        self.assertEqual(given_nth_value(self.list_1, 13, 'max'), 'No way')

    def test_equals_4(self):
        self.assertEqual(given_nth_value(self.list_2, 4, 'max'),
                         'Invalid entry list')

    def test_equals_5(self):
        self.assertEqual(given_nth_value([], 4, 'max'),
                         'No values in the array')

    def test_equals_6(self):
        self.assertEqual(given_nth_value(self.list_3, 2, 'mix'),
                         'Valid entries: \'max\' or \'min\'')

    def test_equals_7(self):
        self.assertEqual(given_nth_value(self.list_3, 2, 'MaX'), 22)


if __name__ == '__main__':
    unittest.main()
