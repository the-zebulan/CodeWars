import unittest

from katas.kyu_6.lotto_6_of_49 import \
    check_for_winning_category, number_generator


class Lotto6of49TestCase(unittest.TestCase):
    def setUp(self):
        self.winning_numbers = number_generator()

    def test_equal_1(self):
        self.assertEqual(len(self.winning_numbers), 7)

    def test_equal_2(self):
        self.assertEqual(len(set(self.winning_numbers[:6])), 6)

    def test_equal_3(self):
        self.assertEqual(self.winning_numbers[:6],
                         sorted(self.winning_numbers[:6]))

    def test_equal_4(self):
        self.assertEqual(check_for_winning_category(
            [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]
        ), 1)

    def test_equal_5(self):
        self.assertEqual(check_for_winning_category(
            [1, 2, 3, 4, 5, 6, 0], [1, 2, 3, 4, 5, 6, 7]
        ), 2)

    def test_equal_6(self):
        self.assertEqual(check_for_winning_category(
            [1, 2, 3, 34, 35, 39, 1], [1, 2, 3, 4, 5, 6, 7]
        ), 8)

    def test_equal_7(self):
        self.assertEqual(check_for_winning_category(
            [11, 12, 13, 34, 35, 39, 1], [1, 2, 3, 4, 5, 6, 7]
        ), -1)

    def test_equal_8(self):
        self.assertEqual(check_for_winning_category(
            [1, 12, 13, 34, 35, 39, 1], [1, 2, 3, 4, 5, 6, 1]
        ), -1)

    def test_not_equal_1(self):
        self.assertNotEqual(number_generator(), self.winning_numbers)

    def test_true_1(self):
        self.assertTrue(0 <= self.winning_numbers[6] <= 9)

    def test_true_2(self):
        self.assertTrue(all(1 <= a <= 49 for a in self.winning_numbers[:6]))

    def test_true_3(self):
        self.assertTrue(0 <= self.winning_numbers[6] <= 9)
