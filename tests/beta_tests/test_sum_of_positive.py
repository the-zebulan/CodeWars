import unittest

from katas.beta.sum_of_positive import positive_sum


class PositiveSumTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)

    def test_equal_2(self):
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)

    def test_equal_3(self):
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)

    def test_equal_4(self):
        self.assertEqual(positive_sum([]), 0)

    def test_equal_5(self):
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)


if __name__ == '__main__':
    unittest.main()
