import unittest

from katas.kyu_8.vowel_remover import shortcut


class ShortcutTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(shortcut('hello'), 'hll')
