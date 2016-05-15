import unittest

from katas.beta.calculator_with_brackets import evaluate


class CalculatorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(evaluate('1 * ( 2 - 1 )'), 1)

    def test_equal_2(self):
        self.assertEqual(evaluate('1'), 1)

    def test_equal_3(self):
        self.assertEqual(evaluate('( 0.5 )'), 0.5)

    def test_equal_4(self):
        self.assertEqual(evaluate(
            '( 22 - ( 1 + 1 ) ) / ( 5 * ( 6 - ( 2 + 2 ) ) )'
        ), 2)

    def test_equal_5(self):
        self.assertEqual(evaluate('( 1.1 + 2.8 ) / ( 3 * 4 )'), 0.325)


if __name__ == '__main__':
    unittest.main()
