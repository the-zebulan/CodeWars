import unittest

from katas.beta.find_duplicate import duplicate


class FindDuplicateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(duplicate([2, 3, 4, 1, 3]), 3)

    def test_equals_2(self):
        self.assertEqual(duplicate([1, 2, 3, 1, 2, 3]), 1)

    def test_equals_3(self):
        self.assertEqual(duplicate([66, 55, 44, 33, 22, 44, 11, 11]), 44)


if __name__ == '__main__':
    unittest.main()
