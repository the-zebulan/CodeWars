import unittest

from katas.kyu_8.is_it_a_number import isDigit


class IsDigitTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(isDigit('-234.4'))

    def test_true_2(self):
        self.assertTrue(isDigit('34.65'))

    def test_true_3(self):
        self.assertTrue(isDigit('-0'))

    def test_true_4(self):
        self.assertTrue(isDigit('0.0'))

    def test_false_1(self):
        self.assertFalse(isDigit('s2324'))

    def test_false_2(self):
        self.assertFalse(isDigit('3 4'))

    def test_false_3(self):
        self.assertFalse(isDigit('3-4'))

    def test_false_4(self):
        self.assertFalse(isDigit('3 4   '))

    def test_false_5(self):
        self.assertFalse(isDigit(''))

    def test_false_6(self):
        self.assertFalse(isDigit(' '))


if __name__ == '__main__':
    unittest.main()
