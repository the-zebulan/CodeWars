import unittest

from katas.kyu_7.character_counter import validate_word


class ValidateWordTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate_word('abcabc'))

    def test_true_2(self):
        self.assertTrue(validate_word('Abcabc'))

    def test_true_3(self):
        self.assertTrue(validate_word('AbcCBa'))

    def test_true_4(self):
        self.assertTrue(validate_word('?!?!?!'))

    def test_true_5(self):
        self.assertTrue(validate_word('abc123'))

    def test_true_6(self):
        self.assertTrue(validate_word('abc!abc!'))

    def test_false(self):
        self.assertFalse(validate_word('AbcabcC'))

    def test_false_2(self):
        self.assertFalse(validate_word('pippi'))

    def test_false_3(self):
        self.assertFalse(validate_word('abcabcd'))

    def test_false_4(self):
        self.assertFalse(validate_word('abc:abc'))


if __name__ == '__main__':
    unittest.main()
