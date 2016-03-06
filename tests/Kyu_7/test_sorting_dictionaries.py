import unittest

from Kyu_7.sorting_dictionaries import sort_dict


class SortDictTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sort_dict({3: 1, 2: 2, 1: 3}),
                         [(1, 3), (2, 2), (3, 1)])

    def test_equals_2(self):
        self.assertEqual(sort_dict({1: 2, 2: 4, 3: 6}),
                         [(3, 6), (2, 4), (1, 2)])

    def test_equals_3(self):
        self.assertEqual(sort_dict({1: 2, 2: 4, 3: 6}),
                         [(3, 6), (2, 4), (1, 2)])

    def test_equals_4(self):
        self.assertEqual(sort_dict({1: 5, 3: 10, 2: 2, 6: 3, 8: 8}),
                         [(3, 10), (8, 8), (1, 5), (6, 3), (2, 2)])


if __name__ == '__main__':
    unittest.main()
