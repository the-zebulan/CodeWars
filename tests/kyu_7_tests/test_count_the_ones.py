import unittest

from katas.kyu_7.count_the_ones import hamming_weight


class CountTheOnesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(hamming_weight(10), 2)

    def test_equal_2(self):
        self.assertEqual(hamming_weight(21), 3)

    def test_equal_3(self):
        self.assertEqual(hamming_weight(7052), 7)

    def test_equal_4(self):
        self.assertEqual(hamming_weight(9667), 7)

    def test_equal_5(self):
        self.assertEqual(hamming_weight(738), 5)

    def test_equal_6(self):
        self.assertEqual(hamming_weight(476), 6)

    def test_equal_7(self):
        self.assertEqual(hamming_weight(870), 6)

    def test_equal_8(self):
        self.assertEqual(hamming_weight(9154), 6)

    def test_equal_9(self):
        self.assertEqual(hamming_weight(2095), 6)

    def test_equal_10(self):
        self.assertEqual(hamming_weight(1959), 8)

    def test_equal_11(self):
        self.assertEqual(hamming_weight(7293), 9)

    def test_equal_12(self):
        self.assertEqual(hamming_weight(7364), 6)

    def test_equal_13(self):
        self.assertEqual(hamming_weight(1835), 7)

    def test_equal_14(self):
        self.assertEqual(hamming_weight(1303), 6)

    def test_equal_15(self):
        self.assertEqual(hamming_weight(6192), 4)

    def test_equal_16(self):
        self.assertEqual(hamming_weight(1852), 7)

    def test_equal_17(self):
        self.assertEqual(hamming_weight(1489), 6)


if __name__ == '__main__':
    unittest.main()
