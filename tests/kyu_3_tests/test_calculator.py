import unittest

from katas.kyu_3.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Calculator().evaluate('2 / 2 + 3 * 4 - 6'), 7)

    def test_equals_2(self):
        self.assertEqual(Calculator().evaluate('10 * 20 / 30'), 6)
