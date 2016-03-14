import unittest

from kyu_7.are_there_doubles import double_check


class DoubleCheckTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(double_check('aabc'))

    def test_true_2(self):
        self.assertTrue(double_check('a 11 c d'))

    def test_true_3(self):
        self.assertTrue(double_check('AabBcC'))

    def test_true_4(self):
        self.assertTrue(double_check('a b  c'))

    def test_false(self):
        self.assertFalse(double_check('abca'))

    def test_false_2(self):
        self.assertFalse(double_check('a b c d e f g h i h k'))


if __name__ == '__main__':
    unittest.main()
