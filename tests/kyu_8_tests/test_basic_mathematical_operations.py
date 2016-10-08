import unittest

from katas.kyu_8.basic_mathematical_operations import basic_op


class BasicOperationsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(basic_op('+', 4, 7), 11)

    def test_equal_2(self):
        self.assertEqual(basic_op('-', 15, 18), -3)

    def test_equal_3(self):
        self.assertEqual(basic_op('*', 5, 5), 25)

    def test_equal_4(self):
        self.assertEqual(basic_op('/', 49, 7), 7)
