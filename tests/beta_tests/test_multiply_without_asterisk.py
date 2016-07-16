import unittest

from katas.beta.multiply_without_asterisk import MyNumber


class MyNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.a = MyNumber(7)
        self.b = MyNumber(8)
        self.c = MyNumber(1)
        self.d = MyNumber(2)

    def test_equal_1(self):
        self.assertEqual((self.a - 1)(self.b - 1), 42)

    def test_equal_2(self):
        self.assertEqual((self.a)(self.b), 56)

    def test_equal_3(self):
        self.assertEqual((1 - self.a) ^ 2, 36)

    def test_equal_4(self):
        self.assertEqual((self.b - self.a)(self.b + self.a), 15)

    def test_equal_5(self):
        self.assertEqual((2 * self.a * self.b) / (7 * self.b), 2)

    def test_equal_6(self):
        self.assertEqual((self.b - self.a) ^ (self.b + self.a), 1)

    def test_equal_7(self):
        self.assertEqual((self.a - 1)(self.a)(self.a + 1), 336)

    def test_equal_8(self):
        self.assertEqual((1 + self.c)(self.c + 2)(1 * self.c * 3)(self.c), 18)

    def test_equal_9(self):
        self.assertEqual((1 - self.d)(self.d / 2)(12 / self.d)(self.d), -12)

    def test_equal_10(self):
        self.assertEqual((2 ^ (2 + self.c))(self.d), 16)

    def test_equal_11(self):
        self.assertEqual(((1 + self.d) ^ 2)(5 / self.c), 45)

    def test_equal_12(self):
        self.assertEqual(((8 + self.c) % 5)(7 % self.d)(5), 20)

    def test_equal_13(self):
        self.assertEqual((self.c)(4)(5)(6)(7), 840)

    def test_equal_14(self):
        self.assertEqual((self.d + 4)(0), 0)

    def test_equal_15(self):
        self.assertEqual(int(self.a), 7)

    def test_equal_16(self):
        self.assertEqual(str(self.a), '7')

    def test_not_equal_1(self):
        self.assertNotEqual(self.a, 42)
