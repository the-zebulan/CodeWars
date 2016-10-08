import unittest

from katas.beta.multiply_list_by_integer_with_restrictions import multiply


class MultiplyTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(multiply(2, [1, 2, 3]), [2, 4, 6])

    def test_equal_2(self):
        self.assertEqual(multiply(2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
