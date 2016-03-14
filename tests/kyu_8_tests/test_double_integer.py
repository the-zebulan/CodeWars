import unittest

from katas.kyu_8.double_integer import doubleInteger


class DoubleIntegerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(doubleInteger(2), 4)

    def test_equals_2(self):
        self.assertEqual(doubleInteger(10), 20)


if __name__ == '__main__':
    unittest.main()
