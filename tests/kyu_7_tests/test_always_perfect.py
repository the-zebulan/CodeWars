import unittest

from katas.kyu_7.always_perfect import check_root


class CheckRootTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(check_root('4,5,6,7'), '841, 29')

    def test_equals_2(self):
        self.assertEqual(check_root('3,s,5,6'), 'incorrect input')

    def test_equals_3(self):
        self.assertEqual(check_root('11,13,14,15'), 'not consecutive')

    def test_equals_4(self):
        self.assertEqual(check_root('10,11,12,13,15'), 'incorrect input')

    def test_equals_5(self):
        self.assertEqual(check_root('10,11,12,13'), '17161, 131')
