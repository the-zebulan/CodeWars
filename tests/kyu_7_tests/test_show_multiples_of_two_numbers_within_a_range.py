import unittest

from katas.kyu_7.show_multiples_of_two_numbers_within_a_range import multiples


class MultiplesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(multiples(2, 4, 40),
                         [4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_equal_2(self):
        self.assertEqual(multiples(3, 4, 40), [12, 24, 36])

    def test_equal_3(self):
        self.assertEqual(multiples(7, 4, 80), [28, 56])

    def test_equal_4(self):
        self.assertEqual(multiples(7, 4, 20), [])
