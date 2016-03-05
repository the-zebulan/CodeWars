import unittest

from Kyu_6.dont_drink_the_water import separate_liquids


class SeparateLiquidsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(separate_liquids(
            [['H', 'H', 'W', 'O'], ['W', 'W', 'O', 'W'], ['H', 'H', 'O', 'O']]),
            [['O', 'O', 'O', 'O'], ['W', 'W', 'W', 'W'], ['H', 'H', 'H', 'H']])

    def test_equals_2(self):
        self.assertEqual(separate_liquids(
            [['A', 'A', 'O', 'H'], ['A', 'H', 'W', 'O'],
             ['W', 'W', 'A', 'W'], ['H', 'H', 'O', 'O']]),
            [['O', 'O', 'O', 'O'], ['A', 'A', 'A', 'A'],
             ['W', 'W', 'W', 'W'], ['H', 'H', 'H', 'H']])

    def test_equals_3(self):
        self.assertEqual(separate_liquids([['A', 'H', 'W', 'O']]),
                         [['O', 'A', 'W', 'H']])

    def test_equals_4(self):
        self.assertEqual(separate_liquids([['A'], ['H'], ['W'], ['O']]),
                         [['O'], ['A'], ['W'], ['H']])

    def test_equals_5(self):
        self.assertEqual(separate_liquids([]), [])


if __name__ == '__main__':
    unittest.main()
