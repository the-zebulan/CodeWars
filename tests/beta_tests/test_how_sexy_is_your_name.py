import unittest

from katas.beta.how_sexy_is_your_name import sexyName


class SexyNameTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sexyName('BOB'), 'PRETTY SEXY')

    def test_equal_2(self):
        self.assertEqual(sexyName('DONALD TRUMP'), 'THE ULTIMATE SEXIEST')

    def test_equal_3(self):
        self.assertEqual(sexyName('FABIO'), 'VERY SEXY')

    def test_equal_4(self):
        self.assertEqual(sexyName('BILL GATES'), 'THE ULTIMATE SEXIEST')

    def test_equal_5(self):
        self.assertEqual(sexyName('SCARLETT JOHANSSON'),
                         'THE ULTIMATE SEXIEST')

    def test_equal_6(self):
        self.assertEqual(sexyName(''), 'NOT TOO SEXY')

    def test_equal_7(self):
        self.assertEqual(sexyName('PHUG'), 'NOT TOO SEXY')

    def test_equal_8(self):
        self.assertEqual(sexyName('CODEWARS'), 'THE ULTIMATE SEXIEST')

    def test_equal_9(self):
        self.assertEqual(sexyName('WWWWWU'), 'PRETTY SEXY')

    def test_equal_10(self):
        self.assertEqual(sexyName('PAMELA ANDERSON'),
                         'THE ULTIMATE SEXIEST')


if __name__ == '__main__':
    unittest.main()
