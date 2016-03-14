import unittest

from beta.array_2_binary import arr2bin


class ArrayToBinaryTestCase(unittest.TestCase):
    def test_equals_(self):
        self.assertEqual(arr2bin([1, 2]), '11')

    def test_equals_2(self):
        self.assertEqual(arr2bin([1, 2, 3, 4, 5]), '1111')

    def test_equals_3(self):
        self.assertEqual(arr2bin([1, 10, 100, 1000]), '10001010111')

    def test_false(self):
        self.assertFalse(arr2bin([1, 2, 'a']))

    def test_false_2(self):
        self.assertFalse(arr2bin([94, 23, 73, True, 61]))


if __name__ == '__main__':
    unittest.main()
