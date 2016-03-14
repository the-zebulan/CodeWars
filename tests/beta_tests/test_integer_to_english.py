import unittest

from Beta.integer_to_english import int_to_english


class IntegerToEnglishTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(int_to_english(1), 'one')

    def test_equals_2(self):
        self.assertEqual(int_to_english(25), 'twenty five')

    def test_equals_3(self):
        self.assertEqual(int_to_english(161), 'one hundred sixty one')

    def test_equals_4(self):
        self.assertEqual(int_to_english(25161045656),
                         'twenty five billion one hundred sixty one million '
                         'forty five thousand six hundred fifty six')


if __name__ == '__main__':
    unittest.main()
