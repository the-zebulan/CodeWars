import unittest

from katas.kyu_7.factorial import factorial


class FactorialTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(factorial(0), 1)

    def test_equal_2(self):
        self.assertEqual(factorial(1), 1)

    def test_equal_3(self):
        self.assertEqual(factorial(2), 2)

    def test_equal_4(self):
        self.assertEqual(factorial(3), 6)

    def test_equal_5(self):
        self.assertEqual(factorial(4), 24)

    def test_equal_6(self):
        self.assertEqual(factorial(5), 120)

    def test_equal_7(self):
        self.assertEqual(factorial(6), 720)

    def test_equal_8(self):
        self.assertEqual(factorial(7), 5040)
