import unittest

from Beta.basic_arabic_to_roman_numerals import arabic_to_roman


class ArabicToRomanTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(arabic_to_roman(-1), 'NaR')

    def test_equals_2(self):
        self.assertEqual(arabic_to_roman(0), 'NaR')

    def test_equals_3(self):
        self.assertEqual(arabic_to_roman(1000), 'NaR')

    def test_equals_4(self):
        self.assertEqual(arabic_to_roman(1), 'I')

    def test_equals_5(self):
        self.assertEqual(arabic_to_roman(2), 'II')

    def test_equals_6(self):
        self.assertEqual(arabic_to_roman(3), 'III')

    def test_equals_7(self):
        self.assertEqual(arabic_to_roman(4), 'IV')

    def test_equals_8(self):
        self.assertEqual(arabic_to_roman(5), 'V')

    def test_equals_9(self):
        self.assertEqual(arabic_to_roman(6), 'VI')

    def test_equals_10(self):
        self.assertEqual(arabic_to_roman(599), 'DXCIX')


if __name__ == '__main__':
    unittest.main()
