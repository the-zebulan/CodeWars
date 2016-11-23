import unittest

from katas.kyu_7.char_code_calculation import calc


class CalcTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(calc('abcdef'), 6)

    def test_equal_2(self):
        self.assertEqual(calc('ifkhchlhfd'), 6)

    def test_equal_3(self):
        self.assertEqual(calc('aaaaaddddr'), 30)

    def test_equal_4(self):
        self.assertEqual(calc('jfmgklf8hglbe'), 6)

    def test_equal_5(self):
        self.assertEqual(calc('jaam'), 12)
