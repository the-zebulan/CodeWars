import unittest

from katas.kyu_6.who_likes_it import likes


class WhoLikesItTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(likes([]), 'no one likes this')

    def test_equals_2(self):
        self.assertEqual(likes(['Peter']), 'Peter likes this')

    def test_equals_3(self):
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')

    def test_equals_4(self):
        self.assertEqual(likes(['Max', 'John', 'Mark']),
                         'Max, John and Mark like this')

    def test_equals_5(self):
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']),
                         'Alex, Jacob and 2 others like this')
