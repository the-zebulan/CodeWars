import unittest

from katas.kyu_5.josephus_permutation import josephus


class JosephusTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_equal_2(self):
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
                         [2, 4, 6, 8, 10, 3, 7, 1, 9, 5])

    def test_equal_3(self):
        self.assertEqual(josephus(list('CodeWars'), 4),
                         ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])

    def test_equal_4(self):
        self.assertEqual(josephus([1, 2, 3, 4, 5, 6, 7], 3),
                         [3, 6, 2, 7, 5, 1, 4])

    def test_equal_5(self):
        self.assertEqual(josephus([], 3), [])
