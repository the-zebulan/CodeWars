import unittest

from katas.kyu_8.ones_and_zeros import binary_array_to_number


class BinaryArrayToNumberTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(binary_array_to_number([0, 0, 0, 1]), 1)

    def test_equal_2(self):
        self.assertEqual(binary_array_to_number([0, 0, 1, 0]), 2)

    def test_equal_3(self):
        self.assertEqual(binary_array_to_number([1, 1, 1, 1]), 15)

    def test_equal_4(self):
        self.assertEqual(binary_array_to_number([0, 1, 1, 0]), 6)


if __name__ == '__main__':
    unittest.main()
