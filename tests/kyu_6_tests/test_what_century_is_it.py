import unittest

from katas.kyu_6.what_century_is_it import whatCentury


class WhatCenturyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(whatCentury('1999'), '20th')

    def test_equals_2(self):
        self.assertEqual(whatCentury('2011'), '21st')

    def test_equals_3(self):
        self.assertEqual(whatCentury('2154'), '22nd')

    def test_equals_4(self):
        self.assertEqual(whatCentury('2259'), '23rd')

    def test_equals_5(self):
        self.assertEqual(whatCentury('1124'), '12th')

    def test_equals_6(self):
        self.assertEqual(whatCentury('2000'), '20th')

    def test_equals_7(self):
        self.assertEqual(whatCentury('1234'), '13th')

    def test_equals_8(self):
        self.assertEqual(whatCentury('2000'), '20th')
