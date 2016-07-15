import unittest

from katas.kyu_7.sort_by_example import example_sort


class ExampleSortTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(example_sort([1, 2, 3, 4, 5], [2, 3, 4, 1, 5]),
                         [2, 3, 4, 1, 5])

    def test_equal_2(self):
        self.assertEqual(example_sort([1, 2, 3, 3, 3, 4, 5], [2, 3, 4, 1, 5]),
                         [2, 3, 3, 3, 4, 1, 5])

    def test_equal_3(self):
        self.assertEqual(example_sort([1, 2, 3, 3, 3, 5], [2, 3, 4, 1, 5]),
                         [2, 3, 3, 3, 1, 5])

    def test_equal_4(self):
        self.assertEqual(example_sort(
            [1, 2, 3, 3, 3, 5], [3, 4, 5, 6, 9, 11, 12, 13, 1, 7, 8, 2, 10]
        ), [3, 3, 3, 5, 1, 2])

    def test_equal_5(self):
        self.assertEqual(example_sort(
            ['a', 'a', 'b', 'f', 'd', 'a'], ['c', 'a', 'd', 'b', 'e', 'f']
        ), ['a', 'a', 'a', 'd', 'b', 'f'])

    def test_equal_6(self):
        self.assertEqual(example_sort(
            ['Alice', 'Bryan', 'Chad', 'Darrell', 'Ellie', 'Fiona'],
            ['Alice', 'Bryan', 'Chad', 'Darrell', 'Ellie', 'Fiona']
        ), ['Alice', 'Bryan', 'Chad', 'Darrell', 'Ellie', 'Fiona'])
