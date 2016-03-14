import unittest

from kyu_7.binary_addition import add_binary


class AddBinaryTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(add_binary(1, 1), '10')

    def test_equals_2(self):
        self.assertEqual(add_binary(0, 1), '1')

    def test_equals_3(self):
        self.assertEqual(add_binary(1, 0), '1')

    def test_equals_4(self):
        self.assertEqual(add_binary(2, 2), '100')

    def test_equals_5(self):
        self.assertEqual(add_binary(51, 12), '111111')


if __name__ == '__main__':
    unittest.main()
