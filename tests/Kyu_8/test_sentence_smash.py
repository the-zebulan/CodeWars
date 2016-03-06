import unittest

from Kyu_8.sentence_smash import smash


class SmashTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(smash(['hello']), 'hello')

    def test_equals_2(self):
        self.assertEqual(smash(['hello', 'world']), 'hello world')


if __name__ == '__main__':
    unittest.main()
