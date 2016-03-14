import unittest

from kyu_7.hamming_distance_binary_codes import hamming_distance


class HammingDistanceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(hamming_distance('100101', '101001'), 2)

    def test_equals_2(self):
        self.assertEqual(hamming_distance('1010', '0101'), 4)

    def test_equals_3(self):
        self.assertEqual(hamming_distance(
            '100101011011010010010', '101100010110010110101'), 9)


if __name__ == '__main__':
    unittest.main()
