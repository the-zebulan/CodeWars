import unittest

from katas.kyu_7.return_the_closest_number_multiple_of_10 import \
    closest_multiple_10


class ClosestMultipleOf10TestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(closest_multiple_10(54), 50)

    def test_equal_2(self):
        self.assertEqual(closest_multiple_10(55), 60)
