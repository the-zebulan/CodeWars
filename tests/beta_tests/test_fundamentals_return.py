import unittest

from beta.fundamentals_return import add, divide, exponent, mod, multiply, subt


class FundamentalsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(add(1, 2), 3)

    def test_equals_2(self):
        self.assertEqual(multiply(1, 2), 2)

    def test_equals_3(self):
        self.assertEqual(divide(2, 1), 2)

    def test_equals_4(self):
        self.assertEqual(mod(1, 2), 1)

    def test_equals_5(self):
        self.assertEqual(exponent(1, 2), 1)

    def test_equals_6(self):
        self.assertEqual(subt(1, 2), -1)

    def test_equals_7(self):
        self.assertEqual(add(5, 7), 12)

    def test_equals_8(self):
        self.assertEqual(multiply(5, 2), 10)

    def test_equals_9(self):
        self.assertEqual(divide(40, 10), 4)

    def test_equals_10(self):
        self.assertEqual(mod(5, 10), 5)

    def test_equals_11(self):
        self.assertEqual(exponent(2, 10), 1024)

    def test_equals_12(self):
        self.assertEqual(subt(5832, 1832), 4000)


if __name__ == '__main__':
    unittest.main()
