import unittest

from Beta.reorganize_the_weapons import identify_weapon


class WeaponsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(identify_weapon('Laval'), 'Laval-Shado Valious')

    def test_equals_2(self):
        self.assertEqual(identify_weapon('Cragger'), 'Cragger-Vengdualize')

    def test_equals_3(self):
        self.assertEqual(identify_weapon('Lagravis'), 'Lagravis-Blazeprowlor')

    def test_equals_4(self):
        self.assertEqual(identify_weapon('Crominus'), 'Crominus-Grandorius')

    def test_equals_5(self):
        self.assertEqual(identify_weapon('Tormak'), 'Tormak-Tygafyre')

    def test_equals_6(self):
        self.assertEqual(identify_weapon('LiElla'), 'LiElla-Roarburn')

    def test_equals_7(self):
        self.assertEqual(identify_weapon('Anything Else!'), 'Not a character')


if __name__ == '__main__':
    unittest.main()
