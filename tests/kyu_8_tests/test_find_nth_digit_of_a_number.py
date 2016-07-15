import unittest

from katas.kyu_8.find_nth_digit_of_a_number import find_digit


class FindDigitTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(find_digit(5673, 4), 5)

    def test_equal_2(self):
        self.assertEqual(find_digit(129, 2), 2)

    def test_equal_3(self):
        self.assertEqual(find_digit(-2825, 3), 8)

    def test_equal_4(self):
        self.assertEqual(find_digit(0, 20), 0)

    def test_equal_5(self):
        self.assertEqual(find_digit(65, 0), -1)

    def test_equal_6(self):
        self.assertEqual(find_digit(24, -8), -1)

    def test_equal_7(self):
        self.assertEqual(find_digit(-1234, 2), 3)

    def test_equal_8(self):
        self.assertEqual(find_digit(-5540, 1), 0)

    def test_equal_9(self):
        self.assertEqual(find_digit(678998, 0), -1)

    def test_equal_10(self):
        self.assertEqual(find_digit(-67854, -57), -1)

    def test_equal_11(self):
        self.assertEqual(find_digit(0, -3), -1)
