import unittest

from katas.kyu_6.ttt17_split_odd_and_even import split_odd_and_even


class SplitOddAndEvenTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(split_odd_and_even(123), [1, 2, 3])

    def test_equal_2(self):
        self.assertEqual(split_odd_and_even(223), [22, 3])

    def test_equal_3(self):
        self.assertEqual(split_odd_and_even(111), [111])

    def test_equal_4(self):
        self.assertEqual(split_odd_and_even(13579), [13579])

    def test_equal_5(self):
        self.assertEqual(split_odd_and_even(2468642), [2468642])

    def test_equal_6(self):
        self.assertEqual(split_odd_and_even(135246), [135, 246])

    def test_equal_7(self):
        self.assertEqual(split_odd_and_even(123456), [1, 2, 3, 4, 5, 6])

    def test_equal_8(self):
        self.assertEqual(split_odd_and_even(8123456), [8, 1, 2, 3, 4, 5, 6])

    def test_equal_9(self):
        self.assertEqual(split_odd_and_even(82123456), [82, 1, 2, 3, 4, 5, 6])

    def test_equal_10(self):
        self.assertEqual(split_odd_and_even(88123456), [88, 1, 2, 3, 4, 5, 6])
