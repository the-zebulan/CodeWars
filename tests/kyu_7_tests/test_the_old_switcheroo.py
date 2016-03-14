import unittest

from Kyu_7.the_old_switcheroo import vowel_2_index


class VowelToIndexTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(vowel_2_index('this is my string'),
                         'th3s 6s my str15ng')

    def test_equals_2(self):
        self.assertEqual(vowel_2_index(
            'Codewars is the best site in the world'),
            'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld')

    def test_equals_3(self):
        self.assertEqual(vowel_2_index(''), '')


if __name__ == '__main__':
    unittest.main()
