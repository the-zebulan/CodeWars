import unittest

from katas.kyu_7.find_smallest_int import findSmallestInt


class FindSmallestIntegerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(findSmallestInt([78, 56, 232, 12, 11, 43]), 11)

    def test_equals_2(self):
        self.assertEqual(findSmallestInt([78, 56, -2, 12, 8, -33]), -33)


if __name__ == '__main__':
    unittest.main()
