import unittest

from katas.kyu_5.sum_of_pairs import sum_pairs


class SumOfPairsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sum_pairs([11, 3, 7, 5], 10), [3, 7])

    def test_equal_2(self):
        self.assertEqual(sum_pairs([4, 3, 2, 3, 4], 6), [4, 2])

    def test_equal_3(self):
        self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])

    def test_equal_4(self):
        self.assertEqual(sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])

    def test_equal_5(self):
        self.assertEqual(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])

    def test_equal_6(self):
        self.assertEqual(sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])

    def test_equal_7(self):
        self.assertEqual(sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])

    def test_equal_8(self):
        self.assertEqual(sum_pairs([0, 2, 0], 0), [0, 0])

    def test_equal_9(self):
        self.assertEqual(sum_pairs([5, 9, 13, -3], 10), [13, -3])

    def test_is_none_1(self):
        self.assertIsNone(sum_pairs([0, 0, -2, 3], 2))

    def test_is_none_2(self):
        self.assertIsNone(sum_pairs([20, -13, 40], -7))


if __name__ == '__main__':
    unittest.main()
