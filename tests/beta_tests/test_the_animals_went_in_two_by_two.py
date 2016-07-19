import unittest

from katas.beta.the_animals_went_in_two_by_two import two_by_two


class TwoByTwoTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(two_by_two([
            'goat', 'goat', 'rabbit', 'rabbit', 'rabbit', 'duck', 'horse',
            'horse', 'swan'
        ]), {'goat': 2, 'horse': 2, 'rabbit': 2})

    def test_equal_2(self):
        self.assertEqual(two_by_two(['goat']), {})

    def test_equal_3(self):
        self.assertEqual(two_by_two([
            'dog', 'cat', 'dog', 'cat', 'beaver', 'cat'
        ]), {'cat': 2, 'dog': 2})

    def test_false_1(self):
        self.assertFalse(two_by_two([]))
