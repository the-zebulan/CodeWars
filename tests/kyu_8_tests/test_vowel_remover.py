import unittest

from Kyu_8.vowel_remover import shortcut


class ShortcutTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(shortcut('hello'), 'hll')


if __name__ == '__main__':
    unittest.main()
