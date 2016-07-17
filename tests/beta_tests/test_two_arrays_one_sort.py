import unittest

from katas.beta.two_arrays_one_sort import linked_sort


class LinkedSortTestCase(unittest.TestCase):
    def test_equal_1(self):
        lst = [1, 6, 5, 0]
        lst_2 = ['house', 'car', 'pen', 'jeans']
        result = linked_sort(lst, lst_2, lambda x: x)
        self.assertEqual(lst, [0, 1, 5, 6])
        self.assertEqual(lst_2, ['jeans', 'house', 'pen', 'car'])
        self.assertEqual(result, [0, 1, 5, 6])

    def test_equal_2(self):
        lst = [-71, -6, 35, 0]
        lst_2 = [0, 'Hello', 32, True]
        result = linked_sort(lst, lst_2)
        self.assertEqual(lst, [-6, -71, 0, 35])
        self.assertEqual(lst_2, ['Hello', 0, True, 32])
        self.assertEqual(result, [-6, -71, 0, 35])

    def test_equal_3(self):
        lst = ['D', 'R', 'W', 'F']
        lst_2 = ['Green', 'Blue', 'Red', 'Yellow']
        result = linked_sort(lst, lst_2, lambda x: str(x))
        self.assertEqual(lst, ['D', 'F', 'R', 'W'])
        self.assertEqual(lst_2, ['Green', 'Yellow', 'Blue', 'Red'])
        self.assertEqual(result, ['D', 'F', 'R', 'W'])

    def test_equal_4(self):
        lst = ['D', 'R', 'W', 'D', 'F']
        lst_2 = ['Green1', 'Blue', 'Red', 'Green2', 'Yellow']
        result = linked_sort(lst, lst_2, lambda x: str(x))
        self.assertEqual(lst, ['D', 'D', 'F', 'R', 'W'])
        self.assertEqual(lst_2, ['Green1', 'Green2', 'Yellow', 'Blue', 'Red'])
        self.assertEqual(result, ['D', 'D', 'F', 'R', 'W'])
