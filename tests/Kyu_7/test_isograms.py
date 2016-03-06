import unittest

from Kyu_7.isograms import is_isogram


class IsogramTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_isogram('Dermatoglyphics'))

    def test_true_2(self):
        self.assertTrue(is_isogram('isogram'))

    def test_true_3(self):
        self.assertTrue(is_isogram(''))

    def test_false(self):
        self.assertFalse(is_isogram('aba'))

    def test_false_2(self):
        self.assertFalse(is_isogram('moOse'))

    def test_false_3(self):
        self.assertFalse(is_isogram('isIsogram'))


if __name__ == '__main__':
    unittest.main()
