import unittest

from katas.beta.ordered_count_of_characters import ordered_count


class OrderedCountTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(ordered_count('abracadabra'),
                         [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])

    def test_equal_2(self):
        self.assertEqual(ordered_count('Code Wars'),
                         [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1),
                          ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
