import unittest

from katas.kyu_4.roman_numerals_encoder import solution


class RomanNumeralsEncoderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(1), 'I')

    def test_equals_2(self):
        self.assertEqual(solution(4), 'IV')

    def test_equals_3(self):
        self.assertEqual(solution(6), 'VI')
