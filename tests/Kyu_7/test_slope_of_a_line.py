import unittest

from Kyu_7.slope_of_a_line import getSlope


class GetSlopeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(getSlope([1, 1], [2, 2]), 1)

    def test_equals_2(self):
        self.assertEqual(getSlope([11, 1], [1, 11]), -1)

    def test_none(self):
        self.assertIsNone(getSlope([1, 1], [1, 2]))

    def test_none_2(self):
        self.assertIsNone(getSlope([1, 1], [1, 1]))


if __name__ == '__main__':
    unittest.main()
