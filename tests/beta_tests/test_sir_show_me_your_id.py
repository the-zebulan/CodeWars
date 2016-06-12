import unittest

from katas.beta.sir_show_me_your_id import show_me


class ShowMeTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(show_me('Francis'))

    def test_true_2(self):
        self.assertTrue(show_me('Jean-Eluard'))

    def test_true_3(self):
        self.assertTrue(show_me('Bernard-Henry-Levy'))

    def test_false_1(self):
        self.assertFalse(show_me('Le Mec'))

    def test_false_2(self):
        self.assertFalse(show_me('Meme Gertrude'))

    def test_false_3(self):
        self.assertFalse(show_me('A-a-a-a----a-a'))

    def test_false_4(self):
        self.assertFalse(show_me('Z-------------'))

    def test_false_5(self):
        self.assertFalse(show_me('Jean-luc'))

    def test_false_6(self):
        self.assertFalse(show_me('Jean--Luc'))

    def test_false_7(self):
        self.assertFalse(show_me('JeanLucPicard'))

    def test_false_8(self):
        self.assertFalse(show_me('-Jean-Luc'))

    def test_false_9(self):
        self.assertFalse(show_me('Jean-Luc-Picard-'))


if __name__ == '__main__':
    unittest.main()
