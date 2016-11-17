import unittest

from katas.kyu_7.keep_the_order import keep_order


class KeepOrderTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(keep_order([1, 2, 3, 4, 7], 5), 4)

    def test_equal_2(self):
        self.assertEqual(keep_order([1, 2, 3, 4, 7], 0), 0)

    def test_equal_3(self):
        self.assertEqual(keep_order([1, 1, 2, 2, 2], 2), 2)

    def test_equal_4(self):
        self.assertEqual(keep_order([1, 2, 3, 4], 5), 4)

    def test_equal_5(self):
        self.assertEqual(keep_order([1, 2, 3, 4], -1), 0)

    def test_equal_6(self):
        self.assertEqual(keep_order([1, 2, 3, 4], 2), 1)

    def test_equal_7(self):
        self.assertEqual(keep_order([1, 2, 3, 4], 0), 0)

    def test_equal_8(self):
        self.assertEqual(keep_order([1, 2, 3, 4], 1), 0)

    def test_equal_9(self):
        self.assertEqual(keep_order([1, 2, 3, 4], 2), 1)

    def test_equal_10(self):
        self.assertEqual(keep_order([1, 2, 3, 4], 3), 2)
