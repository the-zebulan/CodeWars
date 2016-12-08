import unittest

from katas.beta.rotate_a_square_matrix_in_place import rotate_in_place


class RotateInPlaceTestCase(unittest.TestCase):
    def test_equal_1(self):
        matrix = [[1, 2], [3, 4]]
        rotate_in_place(matrix)
        self.assertEqual(matrix, [[3, 1], [4, 2]])

    def test_equal_2(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_in_place(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
