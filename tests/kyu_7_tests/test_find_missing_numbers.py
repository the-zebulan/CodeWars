import unittest

from Kyu_7.find_missing_numbers import find_missing_numbers


class FindMissingNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_missing_numbers([-3, -2, 1, 4]), [-1, 0, 2, 3])

    def test_equals_2(self):
        self.assertEqual(find_missing_numbers([-1, 0, 1, 2, 3, 4]), [])

    def test_equals_3(self):
        self.assertEqual(find_missing_numbers([]), [])

    def test_equals_4(self):
        self.assertEqual(find_missing_numbers([0]), [])

    def test_equals_5(self):
        self.assertEqual(find_missing_numbers([-4, 4]),
                         [-3, -2, -1, 0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
