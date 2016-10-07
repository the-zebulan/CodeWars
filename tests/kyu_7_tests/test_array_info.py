import unittest

from katas.kyu_7.array_info import array_info


class ArrayInfoTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(array_info(
            [1, 2, 3.33, 4, 5.01, 'bass', 'kick', ' ']
        ), [[8], [3], [2], [2], [1]])

    def test_equal_2(self):
        self.assertEqual(array_info([0.001, 2, ' ']),
                         [[3], [1], [1], [None], [1]])

    def test_equal_3(self):
        self.assertEqual(array_info([]), 'Nothing in the array!')

    def test_equal_4(self):
        self.assertEqual(array_info([' ']),
                         [[1], [None], [None], [None], [1]])
