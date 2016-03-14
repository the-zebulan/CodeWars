import unittest

from Kyu_5.maximum_subarray_sum import maxSequence


class MaximumSubarraySumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_equals_2(self):
        self.assertEqual(maxSequence([]), 0)


if __name__ == '__main__':
    unittest.main()
