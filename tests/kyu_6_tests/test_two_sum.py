import unittest

from katas.kyu_6.two_sum import two_sum


class TwoSumTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sorted(two_sum([1, 2, 3], 4)), [0, 2])

    def test_equal_2(self):
        self.assertEqual(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])

    def test_equal_3(self):
        self.assertEqual(sorted(two_sum([2, 2, 3], 4)), [0, 1])
