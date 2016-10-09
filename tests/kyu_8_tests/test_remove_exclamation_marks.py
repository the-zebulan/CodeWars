import unittest

from katas.kyu_8.remove_exclamation_marks import remove_exclamation_marks


class RemoveExclamationMarksTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(remove_exclamation_marks('Hello World!'),
                         'Hello World')

    def test_equal_2(self):
        self.assertEqual(remove_exclamation_marks('Hello World!!!'),
                         'Hello World')

    def test_equal_3(self):
        self.assertEqual(remove_exclamation_marks('Hi! Hello!'), 'Hi Hello')

    def test_equal_4(self):
        self.assertEqual(remove_exclamation_marks(''), '')

    def test_equal_5(self):
        self.assertEqual(remove_exclamation_marks('Oh, no!!!'), 'Oh, no')
