import unittest

from katas.beta.how_sexy_is_your_name import sexy_name


class SexyNameTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sexy_name('BOB'), 'PRETTY SEXY')

    def test_equal_2(self):
        self.assertEqual(sexy_name('DONALD TRUMP'), 'THE ULTIMATE SEXIEST')

    def test_equal_3(self):
        self.assertEqual(sexy_name('FABIO'), 'VERY SEXY')

    def test_equal_4(self):
        self.assertEqual(sexy_name('BILL GATES'), 'THE ULTIMATE SEXIEST')

    def test_equal_5(self):
        self.assertEqual(sexy_name('SCARLETT JOHANSSON'),
                         'THE ULTIMATE SEXIEST')

    def test_equal_6(self):
        self.assertEqual(sexy_name(''), 'NOT TOO SEXY')

    def test_equal_7(self):
        self.assertEqual(sexy_name('PHUG'), 'NOT TOO SEXY')

    def test_equal_8(self):
        self.assertEqual(sexy_name('CODEWARS'), 'THE ULTIMATE SEXIEST')

    def test_equal_9(self):
        self.assertEqual(sexy_name('WWWWWU'), 'PRETTY SEXY')

    def test_equal_10(self):
        self.assertEqual(sexy_name('PAMELA ANDERSON'),
                         'THE ULTIMATE SEXIEST')
