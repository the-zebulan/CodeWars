import unittest

from katas.kyu_7.find_the_vowels import vowel_indices


class VowelIndicesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(vowel_indices("Mmmm"), [])

    def test_equals_2(self):
        self.assertEqual(vowel_indices("super"), [2, 4])

    def test_equals_3(self):
        self.assertEqual(vowel_indices("Super"), [2, 4])

    def test_equals_4(self):
        self.assertEqual(vowel_indices("Apple"), [1, 5])


if __name__ == '__main__':
    unittest.main()
