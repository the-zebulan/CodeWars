import unittest

from kyu_6.bit_counting import countBits


class CountBitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(countBits(0), 0)

    def test_equals_2(self):
        self.assertEqual(countBits(4), 1)

    def test_equals_3(self):
        self.assertEqual(countBits(7), 3)

    def test_equals_4(self):
        self.assertEqual(countBits(9), 2)

    def test_equals_5(self):
        self.assertEqual(countBits(10), 2)


if __name__ == '__main__':
    unittest.main()
