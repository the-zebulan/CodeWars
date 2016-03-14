import unittest

from katas.kyu_7.remove_duplicates import unique


class UniqueTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unique([]), [])

    def test_equals_2(self):
        self.assertEqual(unique([5, 2, 1, 3]), [5, 2, 1, 3])

    def test_equals_3(self):
        self.assertEqual(unique([1, 5, 2, 0, 2, -3, 1, 10]),
                         [1, 5, 2, 0, -3, 10])


if __name__ == '__main__':
    unittest.main()
