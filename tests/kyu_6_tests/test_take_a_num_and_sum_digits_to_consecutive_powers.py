import unittest

from katas.kyu_6.take_a_num_and_sum_digits_to_consecutive_powers import \
    sum_dig_pow


class SumDigitsToConsecutivePowersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_equals_2(self):
        self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])

    def test_equals_3(self):
        self.assertEqual(sum_dig_pow(10, 89), [89])

    def test_equals_4(self):
        self.assertEqual(sum_dig_pow(10, 100), [89])

    def test_equals_5(self):
        self.assertEqual(sum_dig_pow(90, 100), [])

    def test_equals_6(self):
        self.assertEqual(sum_dig_pow(89, 135), [89, 135])


if __name__ == '__main__':
    unittest.main()
