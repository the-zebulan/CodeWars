import unittest

from katas.kyu_7.pauls_misery import paul


class PaulTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(paul(['life', 'eating', 'life']), 'Super happy!')

    def test_equal_2(self):
        self.assertEqual(paul([
            'life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']),
            'Super happy!')

    def test_equal_3(self):
        self.assertEqual(paul([
            'Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata',
            'eating']), 'Happy!')

    def test_equal_4(self):
        self.assertEqual(paul(['Petes kata'] * 7), 'Sad!')

    def test_equal_5(self):
        self.assertEqual(paul(['Petes kata'] * 10), 'Miserable!')
