import unittest

from katas.kyu_7.caeser_encryption import caeser


class CaeserTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(caeser('hello world', 0), 'HELLO WORLD')

    def test_equals_2(self):
        self.assertEqual(caeser('hello', 7), 'OLSSV')

    def test_equals_3(self):
        self.assertEqual(caeser('This is a message', 0), 'THIS IS A MESSAGE')

    def test_equals_4(self):
        self.assertEqual(caeser('who are you?', 18), 'OZG SJW QGM?')

    def test_equals_5(self):
        self.assertEqual(caeser('..5tyu..', 25), '..5SXT..')

    def test_equals_6(self):
        self.assertEqual(caeser('..#$%^..', 0), '..#$%^..')

    def test_equals_7(self):
        self.assertEqual(caeser('..#$%^..', 26), '..#$%^..')

    def test_equals_8(self):
        self.assertEqual(caeser('final one', 9), 'ORWJU XWN')
