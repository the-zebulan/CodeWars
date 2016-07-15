import unittest

from katas.kyu_6.find_the_odd_int import find_it


class FindTheOddIntegerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_it(
            [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
