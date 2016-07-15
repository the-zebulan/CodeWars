import unittest

from katas.kyu_7.number_pairs import get_larger_numbers


class GetLargerNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_larger_numbers(
            [13, 64, 15, 17, 88], [23, 14, 53, 17, 80]
        ), [23, 64, 53, 17, 88])

    def test_equals_2(self):
        self.assertEqual(get_larger_numbers(
            [34, -64, 15, 17, 88], [23, 14, 53, 17, 80]
        ), [34, 14, 53, 17, 88])
