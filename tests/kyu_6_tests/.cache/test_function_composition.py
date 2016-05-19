import unittest

from katas.kyu_6.function_composition import compose


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.add_1 = lambda a: a + 1
        self.sub_2 = lambda b: b - 2
        self.mul_3 = lambda c: c * 3

    def test_equal_1(self):
        self.assertEqual(compose(self.add_1, self.mul_3)(2), 7)

    def test_equal_2(self):
        self.assertEqual(compose(self.mul_3, self.sub_2)(7), 15)

    def test_equal_3(self):
        self.assertEqual(compose(self.sub_2, self.add_1)(3), 2)


if __name__ == '__main__':
    unittest.main()
