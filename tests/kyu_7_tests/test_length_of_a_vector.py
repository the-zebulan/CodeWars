import unittest

from katas.kyu_7.length_of_a_vector import vector_length


class VectorLengthTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(vector_length([[0, 1], [0, 0]]), 1)

    def test_equals_2(self):
        self.assertEqual(vector_length([[0, 3], [4, 0]]), 5)

    def test_equals_3(self):
        self.assertEqual(vector_length([[1, -1], [1, -1]]), 0)
