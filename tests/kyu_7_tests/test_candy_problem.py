import unittest

from kyu_7.candy_problem import candies


class CandiesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(candies([5, 8, 6, 4]), 9)

    def test_equals_2(self):
        self.assertEqual(candies([1, 2, 4, 6]), 11)

    def test_equals_3(self):
        self.assertEqual(candies([1, 6]), 5)

    def test_equals_4(self):
        self.assertEqual(candies([]), -1)


if __name__ == '__main__':
    unittest.main()
