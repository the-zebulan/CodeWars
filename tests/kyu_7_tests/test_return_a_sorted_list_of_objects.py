import unittest

from katas.kyu_7.return_a_sorted_list_of_objects import sort_list


class SortListTestCase(unittest.TestCase):
    def test_equals_1(self):
        self.assertEqual(sort_list('x', []), [])

    def test_equals_2(self):
        self.assertEqual(sort_list(
            'b', [{'a': 2, 'b': 2}, {'a': 3, 'b': 40}, {'a': 1, 'b': 12}]
        ), [{'a': 3, 'b': 40}, {'a': 1, 'b': 12}, {'a': 2, 'b': 2}])

    def test_equals_3(self):
        self.assertEqual(sort_list(
            'a', [{'a': 4, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 40},
                  {'a': 1, 'b': 12}]
        ), [{'a': 4, 'b': 3}, {'a': 3, 'b': 40}, {'a': 2, 'b': 2},
            {'a': 1, 'b': 12}])


if __name__ == '__main__':
    unittest.main()
