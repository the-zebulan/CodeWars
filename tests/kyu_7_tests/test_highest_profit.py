import unittest

from kyu_7.highest_profit import min_max


class HighestProfitTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(min_max([1, 2, 3, 4, 5]), [1, 5])

    def test_equals_2(self):
        self.assertEqual(min_max([2334454, 5]), [5, 2334454])

    def test_equals_3(self):
        self.assertEqual(min_max([1]), [1, 1])


if __name__ == '__main__':
    unittest.main()
