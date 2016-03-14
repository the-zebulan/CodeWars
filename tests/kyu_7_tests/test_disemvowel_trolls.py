import unittest

from katas.kyu_7.disemvowel_trolls import disemvowel


class DisemvowelTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(disemvowel('This website is for losers LOL!'),
                         'Ths wbst s fr lsrs LL!')


if __name__ == '__main__':
    unittest.main()
