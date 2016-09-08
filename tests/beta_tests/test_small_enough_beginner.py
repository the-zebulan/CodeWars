import unittest

from katas.beta.small_enough_beginner import small_enough


class SmallEnoughTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(small_enough([66, 101], 200))

    def test_true_2(self):
        self.assertTrue(small_enough([101, 45, 75, 105, 99, 107], 107))

    def test_true_3(self):
        self.assertTrue(
            small_enough([80, 117, 115, 104, 45, 85, 112, 115], 120)
        )

    def test_true_4(self):
        self.assertTrue(small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    def test_true_5(self):
        self.assertTrue(
            small_enough([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12)
        )

    def test_false_1(self):
        self.assertFalse(
            small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100)
        )

    def test_false_2(self):
        self.assertFalse(small_enough([1, 1, 1, 1, 1, 2], 1))

    def test_false_3(self):
        self.assertFalse(small_enough([78, 33, 22, 44, 88, 9, 6], 87))
