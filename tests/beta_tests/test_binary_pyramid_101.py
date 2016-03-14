import unittest

# function spelling mistake is from CodeWars
from beta.binary_pyramid_101 import binary_piramid


class BinaryPyramidTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(binary_piramid(1, 4), '1111010')

    def test_equals_2(self):
        self.assertEqual(binary_piramid(1, 6), '101001101')

    def test_equals_3(self):
        self.assertEqual(binary_piramid(6, 20), '1110010110100011')

    def test_equals_4(self):
        self.assertEqual(binary_piramid(21, 60), '1100000100010001010100')


if __name__ == '__main__':
    unittest.main()
