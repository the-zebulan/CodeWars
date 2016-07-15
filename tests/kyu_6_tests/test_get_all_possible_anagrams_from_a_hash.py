import unittest

from katas.kyu_6.get_all_possible_anagrams_from_a_hash import get_words


class GetWordsTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_words({1: ['a', 'b', 'c']}),
                         ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_equals_2(self):
        self.assertEqual(get_words({2: ['a'], 1: ['b', 'c']}),
                         ['aabc', 'aacb', 'abac', 'abca', 'acab', 'acba',
                          'baac', 'baca', 'bcaa', 'caab', 'caba', 'cbaa'])
