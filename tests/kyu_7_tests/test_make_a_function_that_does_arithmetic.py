import unittest

from katas.kyu_7.make_a_function_that_does_arithmetic import arithmetic


class ArithmeticTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(arithmetic(1, 2, 'add'), 3)

    def test_equal_2(self):
        self.assertEqual(arithmetic(8, 2, 'subtract'), 6)

    def test_equal_3(self):
        self.assertEqual(arithmetic(5, 2, 'multiply'), 10)

    def test_equal_4(self):
        self.assertEqual(arithmetic(8, 2, 'divide'), 4)
