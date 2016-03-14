import unittest

from kyu_7.find_duplicates import duplicates


class FindDuplicatesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(duplicates(
            [1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1])

    def test_equals_2(self):
        self.assertEqual(duplicates([0, 1, 2, 3, 4, 5]), [])


if __name__ == '__main__':
    unittest.main()
