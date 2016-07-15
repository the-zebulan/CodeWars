import unittest

from katas.kyu_7.paperboy import cheapest_quote


class CheapestQuoteTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(cheapest_quote(1), 0.10)

    def test_equals_2(self):
        self.assertEqual(cheapest_quote(5), 0.49)

    def test_equals_3(self):
        self.assertEqual(cheapest_quote(10), 0.97)

    def test_equals_4(self):
        self.assertEqual(cheapest_quote(20), 1.93)

    def test_equals_5(self):
        self.assertEqual(cheapest_quote(40), 3.85)

    def test_equals_6(self):
        self.assertEqual(cheapest_quote(41), 3.95)

    def test_equals_7(self):
        self.assertEqual(cheapest_quote(80), 7.70)

    def test_equals_8(self):
        self.assertEqual(cheapest_quote(26), 2.52)

    def test_equals_9(self):
        self.assertEqual(cheapest_quote(0), 0.0)

    def test_equals_10(self):
        self.assertEqual(cheapest_quote(499), 48.06)
