import unittest

from katas.kyu_6.multiplication_tables import multiplication_table


class MultiplicationTableTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(multiplication_table(2, 2), [[1, 2], [2, 4]])

    def test_equals_2(self):
        self.assertEqual(multiplication_table(3, 3),
                         [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
