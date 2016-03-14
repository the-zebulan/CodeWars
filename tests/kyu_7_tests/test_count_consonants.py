import unittest

from Kyu_7.count_consonants import consonant_count


class ConsonantCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(consonant_count(''), 0)

    def test_equals_2(self):
        self.assertEqual(consonant_count('aaaaa'), 0)

    def test_equals_3(self):
        self.assertEqual(consonant_count('Bbbbb'), 5)

    def test_equals_4(self):
        self.assertEqual(consonant_count('helLo world'), 7)

    def test_equals_5(self):
        self.assertEqual(consonant_count('h^$&^#$&^elLo world'), 7)


if __name__ == '__main__':
    unittest.main()
