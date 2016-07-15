import unittest

from katas.beta.sum_the_repeats import repeat_sum


class RepeatSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]), 10)

    def test_equals_2(self):
        self.assertEqual(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]), 0)

    def test_equals_3(self):
        self.assertEqual(repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]), 9)
