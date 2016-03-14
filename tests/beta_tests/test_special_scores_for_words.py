import unittest

from katas.beta.special_scores_for_words import find_word


class FindWordTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_word(8, 888), 'southern')

    def test_equals_2(self):
        self.assertEqual(find_word(7, 1412), 'support')

    def test_none(self):
        self.assertIsNone(find_word(9, 500))


if __name__ == '__main__':
    unittest.main()
