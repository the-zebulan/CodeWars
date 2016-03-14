import unittest

from katas.beta.alien_beer_morse_code import morse_converter


class MorseConverterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(morse_converter(".----"), 1)

    def test_equals_2(self):
        self.assertEqual(morse_converter("..----------..."), 207)

    def test_equals_3(self):
        self.assertEqual(morse_converter("----.--.....---...--"), 9723)

    def test_equals_4(self):
        self.assertEqual(morse_converter('.----.----.----.----.----'), 11111)

    def test_equals_5(self):
        self.assertEqual(morse_converter(
            '..----------...-....----------'), 207600)

    def test_equals_6(self):
        self.assertEqual(morse_converter('---------------'), 0)

    def test_equals_7(self):
        self.assertEqual(morse_converter('..---.--------....--'), 2193)

    def test_equals_8(self):
        self.assertEqual(morse_converter(
            '.----..---...--....-.....-....--...---..----.-----'), 1234567890)


if __name__ == '__main__':
    unittest.main()
