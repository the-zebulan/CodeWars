import unittest

from katas.kyu_6.help_the_bookseller import stock_list


class StockListTestCase(unittest.TestCase):
    def setUp(self):
        self.a = ['ABAR 200', 'CDXE 500', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
        self.b = ['A', 'B']

    def test_equals(self):
        self.assertEqual(stock_list(self.a, self.b), '(A : 200) - (B : 1140)')

    def test_equals_2(self):
        self.assertEqual(stock_list(self.a, []), '')

    def test_equals_3(self):
        self.assertEqual(stock_list([], self.b), '')
