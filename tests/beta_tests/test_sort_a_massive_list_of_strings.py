import unittest

from katas.beta.sort_a_massive_list_of_strings import sort


class SortTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(list(sort([])), [])

    def test_equal_2(self):
        self.assertEqual(list(sort(['z', 'x', 'w', 'y'])),
                         ['w', 'x', 'y', 'z'])

    def test_equal_3(self):
        self.assertEqual(list(sort(['b', 'ba', 'ab', 'bb', 'c'])),
                         ['ab', 'b', 'ba', 'bb', 'c'])
