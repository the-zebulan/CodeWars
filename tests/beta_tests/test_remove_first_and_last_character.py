import unittest

from katas.beta.remove_first_and_last_character import remove_char


class RemoveFirstAndLastCharacterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')

    def test_equals_2(self):
        self.assertEqual(remove_char('country'), 'ountr')

    def test_equals_3(self):
        self.assertEqual(remove_char('person'), 'erso')

    def test_equals_4(self):
        self.assertEqual(remove_char('place'), 'lac')

    def test_equals_5(self):
        self.assertEqual(remove_char('ok'), '')
