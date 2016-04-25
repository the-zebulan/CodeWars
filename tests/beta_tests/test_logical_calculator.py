import unittest

from katas.beta.logical_calculator import logical_calc


class LogicalCalculatorTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(logical_calc([True, False], 'OR'))

    def test_true_2(self):
        self.assertTrue(logical_calc([True, False], 'XOR'))

    def test_false_1(self):
        self.assertFalse(logical_calc([True, True, False], 'AND'))

    def test_false_2(self):
        self.assertFalse(logical_calc([True, False], 'AND'))


if __name__ == '__main__':
    unittest.main()
