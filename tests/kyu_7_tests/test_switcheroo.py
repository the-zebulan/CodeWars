import unittest

from katas.kyu_7.switcheroo import switcheroo


class SwitcherooTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(switcheroo('abc'), 'bac')

    def test_equal_2(self):
        self.assertEqual(switcheroo('aaabcccbaaa'), 'bbbacccabbb')

    def test_equal_3(self):
        self.assertEqual(switcheroo('ccccc'), 'ccccc')

    def test_equal_4(self):
        self.assertEqual(switcheroo('abababababababab'), 'babababababababa')

    def test_equal_5(self):
        self.assertEqual(switcheroo('aaaaa'), 'bbbbb')
