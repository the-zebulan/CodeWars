import unittest

from katas.beta.closest_sum import closest_sum


class ClosestSumTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(closest_sum([-1, 2, 1, -4], 1), 2)

    def test_equal_2(self):
        self.assertEqual(closest_sum([5, 4, 0, 3], 3), 7)

    def test_equal_3(self):
        self.assertEqual(closest_sum([1, 2, 3, 4], 4), 6)

    def test_equal_4(self):
        self.assertEqual(closest_sum([-2, 2, -3, 1], 3), 1)


if __name__ == '__main__':
    unittest.main()
