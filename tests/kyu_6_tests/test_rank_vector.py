import unittest

from katas.kyu_6.rank_vector import ranks


class RankVectorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(ranks([]), [])

    def test_equals_2(self):
        self.assertEqual(ranks([2]), [1])

    def test_equals_3(self):
        self.assertEqual(ranks([2, 2]), [1, 1])

    def test_equals_4(self):
        self.assertEqual(ranks([9, 3, 6, 10]), [2, 4, 3, 1])

    def test_equals_5(self):
        self.assertEqual(ranks([3, 3, 3, 3, 3, 5, 1]), [2, 2, 2, 2, 2, 1, 7])


if __name__ == '__main__':
    unittest.main()
