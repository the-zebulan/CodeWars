import unittest

from katas.kyu_4.roman_numerals_decoder import solution


class RomanNumeralsDecoderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution('I'), 1)

    def test_equals_2(self):
        self.assertEqual(solution('IV'), 4)

    def test_equals_3(self):
        self.assertEqual(solution('XXI'), 21)

    def test_equals_4(self):
        self.assertEqual(solution('MMVIII'), 2008)

    def test_equals_5(self):
        self.assertEqual(solution('MDCLXVI'), 1666)


if __name__ == '__main__':
    unittest.main()
