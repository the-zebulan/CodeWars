import unittest

from katas.kyu_8.beginner_lost_without_a_map import maps


class MapsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(maps([1, 2, 3]), [2, 4, 6])

    def test_equal_2(self):
        self.assertEqual(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_equal_3(self):
        self.assertEqual(maps([]), [])
