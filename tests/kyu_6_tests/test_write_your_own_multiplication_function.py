import unittest

from katas.kyu_6.write_your_own_multiplication_function import multiply


class MultiplyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(multiply(13, 7), 91)
