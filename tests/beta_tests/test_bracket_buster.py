import unittest

from katas.beta.bracket_buster import bracket_buster


class BracketBusterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bracket_buster('Don\'t [pass to Ramone]'),
                         ['pass to Ramone'])

    def test_equals_2(self):
        self.assertEqual(bracket_buster(1337), 'Take a seat on the bench.')

    def test_equals_3(self):
        self.assertEqual(bracket_buster('[I\'m] glad y\'all [set it]] off'),
                         ['I\'m', 'set it'])


if __name__ == '__main__':
    unittest.main()
