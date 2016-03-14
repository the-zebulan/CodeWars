import unittest

from katas.kyu_8.how_good_are_you_really import better_than_average


class BetterThanAverageTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(better_than_average([2, 3], 5))

    def test_true_2(self):
        self.assertTrue(better_than_average(
            [100, 40, 34, 57, 29, 72, 57, 88], 75))

    def test_true_3(self):
        self.assertTrue(better_than_average(
            [12, 23, 34, 45, 56, 67, 78, 89, 90], 69))


if __name__ == '__main__':
    unittest.main()
