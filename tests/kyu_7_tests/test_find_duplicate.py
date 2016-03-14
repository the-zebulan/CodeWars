import unittest

from kyu_7.find_duplicate import find_dup


class FindDuplicateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_dup([5, 4, 3, 2, 1, 1]), 1)

    def test_equals_2(self):
        self.assertEqual(find_dup([1, 3, 2, 5, 4, 5, 7, 6]), 5)


if __name__ == '__main__':
    unittest.main()
