import unittest

from katas.beta.professor_oaks_trouble_new_pokedex_prototype import PokeScan


class PokeScanTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(PokeScan('Squirtle', 0, 'water').info(),
                         'Squirtle, a wet and weak Pokemon.')

    def test_equal_2(self):
        self.assertEqual(PokeScan('Charmander', 0, 'fire').info(),
                         'Charmander, a fiery and weak Pokemon.')

    def test_equal_3(self):
        self.assertEqual(PokeScan('Bulbasaur', 0, 'grass').info(),
                         'Bulbasaur, a grassy and weak Pokemon.')

    def test_equal_4(self):
        self.assertEqual(PokeScan('Squirtle', 20, 'water').info(),
                         'Squirtle, a wet and weak Pokemon.')

    def test_equal_5(self):
        self.assertEqual(PokeScan('Charmander', 20, 'fire').info(),
                         'Charmander, a fiery and weak Pokemon.')

    def test_equal_6(self):
        self.assertEqual(PokeScan('Bulbasaur', 20, 'grass').info(),
                         'Bulbasaur, a grassy and weak Pokemon.')

    def test_equal_7(self):
        self.assertEqual(PokeScan('Squirtle', 21, 'water').info(),
                         'Squirtle, a wet and fair Pokemon.')

    def test_equal_8(self):
        self.assertEqual(PokeScan('Charmander', 21, 'fire').info(),
                         'Charmander, a fiery and fair Pokemon.')

    def test_equal_9(self):
        self.assertEqual(PokeScan('Bulbasaur', 21, 'grass').info(),
                         'Bulbasaur, a grassy and fair Pokemon.')

    def test_equal_10(self):
        self.assertEqual(PokeScan('Squirtle', 50, 'water').info(),
                         'Squirtle, a wet and fair Pokemon.')

    def test_equal_11(self):
        self.assertEqual(PokeScan('Charmander', 50, 'fire').info(),
                         'Charmander, a fiery and fair Pokemon.')

    def test_equal_12(self):
        self.assertEqual(PokeScan('Bulbasaur', 50, 'grass').info(),
                         'Bulbasaur, a grassy and fair Pokemon.')

    def test_equal_13(self):
        self.assertEqual(PokeScan('Squirtle', 51, 'water').info(),
                         'Squirtle, a wet and strong Pokemon.')

    def test_equal_14(self):
        self.assertEqual(PokeScan('Charmander', 51, 'fire').info(),
                         'Charmander, a fiery and strong Pokemon.')

    def test_equal_15(self):
        self.assertEqual(PokeScan('Bulbasaur', 51, 'grass').info(),
                         'Bulbasaur, a grassy and strong Pokemon.')

    def test_equal_16(self):
        self.assertEqual(PokeScan('Squirtle', 100, 'water').info(),
                         'Squirtle, a wet and strong Pokemon.')

    def test_equal_17(self):
        self.assertEqual(PokeScan('Charmander', 100, 'fire').info(),
                         'Charmander, a fiery and strong Pokemon.')

    def test_equal_18(self):
        self.assertEqual(PokeScan('Bulbasaur', 100, 'grass').info(),
                         'Bulbasaur, a grassy and strong Pokemon.')
