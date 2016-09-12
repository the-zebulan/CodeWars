import unittest

from katas.kyu_8.correct_the_mistakes_of_the_character_recognition_software \
    import correct


class CorrectTheMistakesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(correct('L0ND0N'), 'LONDON')

    def test_equal_2(self):
        self.assertEqual(correct('DUBL1N'), 'DUBLIN')

    def test_equal_3(self):
        self.assertEqual(correct('51NGAP0RE'), 'SINGAPORE')

    def test_equal_4(self):
        self.assertEqual(correct('BUDAPE5T'), 'BUDAPEST')

    def test_equal_5(self):
        self.assertEqual(correct('PAR15'), 'PARIS')
