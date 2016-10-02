import unittest

from katas.kyu_8.is_there_a_vowel_in_there import is_vow


class IsVowelTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(is_vow(
            [118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113,
             114, 113, 120, 106]),
            [118, 'u', 120, 121, 'u', 98, 122, 'a', 120, 106, 104, 116, 113,
             114, 113, 120, 106])

    def test_equal_2(self):
        self.assertEqual(is_vow(
            [101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103]),
            ['e', 121, 110, 113, 113, 103, 121, 121, 'e', 107, 103])

    def test_equal_3(self):
        self.assertEqual(is_vow([118, 103, 110, 109, 104, 106]),
                         [118, 103, 110, 109, 104, 106])

    def test_equal_4(self):
        self.assertEqual(is_vow([107, 99, 110, 107, 118, 106, 112, 102]),
                         [107, 99, 110, 107, 118, 106, 112, 102])
