import unittest

from katas.kyu_7.sorted_union import unite_unique


class UniteUniqueTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(unite_unique([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_equal_2(self):
        self.assertEqual(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]),
                         [1, 3, 2, 5, 4])

    def test_equal_3(self):
        self.assertEqual(unite_unique([4, 3, 2, 2]), [4, 3, 2])

    def test_equal_4(self):
        self.assertEqual(unite_unique([4, 'a', 2], []), [4, 'a', 2])

    def test_equal_5(self):
        self.assertEqual(unite_unique([], [4, 'a', 2]), [4, 'a', 2])

    def test_equal_6(self):
        self.assertEqual(unite_unique([], [4, 'a', 2], []), [4, 'a', 2])

    def test_equal_7(self):
        self.assertEqual(unite_unique([]), [])

    def test_equal_8(self):
        self.assertEqual(unite_unique([], []), [])

    def test_equal_9(self):
        self.assertEqual(unite_unique([], [1, 2]), [1, 2])

    def test_equal_10(self):
        self.assertEqual(unite_unique([], [1, 2, 1, 2], [2, 1, 1, 2, 1]),
                         [1, 2])


if __name__ == '__main__':
    unittest.main()
