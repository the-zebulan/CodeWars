import unittest

from kyu_7.factorial_factory import factorial


class FactorialTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(factorial(0), 1)

    def test_equals_2(self):
        self.assertEqual(factorial(1), 1)

    def test_equals_3(self):
        self.assertEqual(factorial(5), 120)

    def test_none(self):
        self.assertIsNone(factorial(-2))


if __name__ == '__main__':
    unittest.main()
