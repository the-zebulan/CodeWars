import unittest

from katas.kyu_5.by_the_power_set_of_castle_grayskull import power


class PowerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(power([1, 2, 3]), [
            [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
        ])

    def test_equals_2(self):
        self.assertEqual(power([1, 2, 3, 4]), [
            [], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4],
            [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]
        ])
