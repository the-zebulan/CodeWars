import unittest

from Beta.find_gcf import largestFactor


class LargestFactorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(largestFactor(50, 25), 25)

    def test_equals_2(self):
        self.assertEqual(largestFactor(81, 63), 9)

    def test_equals_3(self):
        self.assertEqual(largestFactor(24, 54), 6)

    def test_equals_4(self):
        self.assertEqual(largestFactor(67, 19), 1)


if __name__ == '__main__':
    unittest.main()
