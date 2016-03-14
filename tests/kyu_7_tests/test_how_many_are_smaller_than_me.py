import unittest

from kyu_7.how_many_are_smaller_than_me import smaller


class SmallerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])

    def test_equals_2(self):
        self.assertEqual(smaller([1, 2, 3]), [0, 0, 0])

    def test_equals_3(self):
        self.assertEqual(smaller([1, 2, 0]), [1, 1, 0])

    def test_equals_4(self):
        self.assertEqual(smaller([1, 2, 1]), [0, 1, 0])

    def test_equals_5(self):
        self.assertEqual(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])

    def test_equals_6(self):
        self.assertEqual(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]),
                         [4, 1, 5, 5, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
