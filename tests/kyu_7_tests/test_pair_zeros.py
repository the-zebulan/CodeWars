import unittest

from katas.kyu_7.pair_zeros import pair_zeros


class PairZerosTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(pair_zeros([0, 1, 0, 2]), [0, 1, 2])

    def test_equal_2(self):
        self.assertEqual(pair_zeros([0, 1, 0, 0]), [0, 1, 0])

    def test_equal_3(self):
        self.assertEqual(pair_zeros([1, 0, 7, 0, 1]), [1, 0, 7, 1])

    def test_equal_4(self):
        self.assertEqual(pair_zeros([0, 1, 7, 0, 2, 2, 0, 0, 1, 0]),
                         [0, 1, 7, 2, 2, 0, 1, 0])

    def test_equal_5(self):
        self.assertEqual(pair_zeros([]), [])

    def test_equal_6(self):
        self.assertEqual(pair_zeros([1]), [1])

    def test_equal_7(self):
        self.assertEqual(pair_zeros([1, 2, 3]), [1, 2, 3])

    def test_equal_8(self):
        self.assertEqual(pair_zeros([0]), [0])

    def test_equal_9(self):
        self.assertEqual(pair_zeros([0, 0]), [0])

    def test_equal_10(self):
        self.assertEqual(pair_zeros([1, 0, 1, 0, 2, 0, 0]), [1, 0, 1, 2, 0])

    def test_equal_11(self):
        self.assertEqual(pair_zeros([0, 0, 0]), [0, 0])

    def test_equal_12(self):
        self.assertEqual(pair_zeros([1, 0, 1, 0, 2, 0, 0, 3, 0]),
                         [1, 0, 1, 2, 0, 3, 0])

    def test_equal_13(self):
        self.assertEqual(pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                         [0, 0, 0, 0, 0, 0])

    def test_equal_14(self):
        self.assertEqual(pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                         [0, 0, 0, 0, 0, 0, 0])
