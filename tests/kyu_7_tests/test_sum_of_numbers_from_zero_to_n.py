import unittest

from katas.kyu_7.sum_of_numbers_from_zero_to_n import show_sequence


class ShowSequenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(show_sequence(6), '0+1+2+3+4+5+6 = 21')

    def test_equal_2(self):
        self.assertEqual(show_sequence(7), '0+1+2+3+4+5+6+7 = 28')

    def test_equal_3(self):
        self.assertEqual(show_sequence(0), '0=0')

    def test_equal_4(self):
        self.assertEqual(show_sequence(-1), '-1<0')

    def test_equal_5(self):
        self.assertEqual(show_sequence(-10), '-10<0')
