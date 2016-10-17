import unittest

from katas.kyu_7.numbers_with_this_digit_inside import \
    numbers_with_digit_inside


class DigitInsideTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(numbers_with_digit_inside(5, 6), [0, 0, 0])

    def test_equal_2(self):
        self.assertEqual(numbers_with_digit_inside(7, 6), [1, 6, 6])

    def test_equal_3(self):
        self.assertEqual(numbers_with_digit_inside(11, 1), [3, 22, 110])

    def test_equal_4(self):
        self.assertEqual(numbers_with_digit_inside(20, 0), [2, 30, 200])

    def test_equal_5(self):
        self.assertEqual(numbers_with_digit_inside(44, 4),
                         [9, 286, 5955146588160])
