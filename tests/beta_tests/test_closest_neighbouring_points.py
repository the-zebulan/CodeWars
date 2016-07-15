import unittest

from katas.beta.closest_neighbouring_points import closest_points


class ClosestPointsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(closest_points(
            [(5, 10), (3, 6), (1, 4), (6, 2), (4, 3), (0, 4), (10, 3), (9, 1)]),
            [8, [[(0, 4), (1, 4)]], 1.0])

    def test_equals_2(self):
        self.assertEqual(closest_points(
            [(8, 14), (16, 5), (5, 5), (15, 18), (17, 10), (0, 14), (4, 15),
             (19, 17), (13, 16), (10, 18), (14, 13), (12, 14), (11, 15),
             (7, 15)]),
            [14, [[(7, 15), (8, 14)], [(11, 15), (12, 14)]], 1.4142])
