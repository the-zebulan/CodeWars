import unittest

from katas.kyu_7.all_unique import has_unique_chars


class HasUniqueCharsTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(has_unique_chars('abcdef'))

    def test_false(self):
        self.assertFalse(has_unique_chars('++-'))

    def test_false_2(self):
        self.assertFalse(has_unique_chars('  nAa'))


if __name__ == '__main__':
    unittest.main()
