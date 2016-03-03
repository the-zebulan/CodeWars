import unittest

from Kyu_4.roman_numerals_encoder import solution


class RomanNumeralsEncoderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(solution(1), 'I')

    def test_equals_2(self):
        self.assertEqual(solution(4), 'IV')

    def test_equals_3(self):
        self.assertEqual(solution(6), 'VI')


if __name__ == '__main__':
    unittest.main()
