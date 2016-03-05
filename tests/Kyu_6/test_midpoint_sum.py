import unittest

from Kyu_6.midpoint_sum import midpoint_sum


class MidpointSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(midpoint_sum([4, 1, 7, 9, 3, 9]), 3)

    def test_equals_2(self):
        self.assertEqual(midpoint_sum([1, 0, 1]), 1)

    def test_equals_3(self):
        self.assertEqual(midpoint_sum([9, 0, 1, 2, 3, 4]), 2)

    def test_equals_4(self):
        self.assertEqual(midpoint_sum([0, 0, 4, 0]), 2)

    def test_equals_5(self):
        self.assertEqual(midpoint_sum([-10, 3, 7, 8, -6, -13, 21]), 4)

    def test_equals_6(self):
        self.assertEqual(midpoint_sum([
            1, 1, 1, 1, -5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 52)

    def test_none(self):
        self.assertIsNone(midpoint_sum([0, 0]))

    def test_none_2(self):
        self.assertIsNone(midpoint_sum([0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
