import unittest

from beta.digit_sum import sum_digits


class SumDigitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_digits(4523), 5)

    def test_equals_2(self):
        self.assertEqual(sum_digits(65536), 7)

    def test_equals_3(self):
        self.assertEqual(sum_digits(0), 0)

    def test_equals_4(self):
        self.assertEqual(sum_digits(100), 1)

    def test_equals_5(self):
        self.assertEqual(sum_digits(41), 5)

    def test_equals_6(self):
        self.assertEqual(sum_digits(99), 9)


if __name__ == '__main__':
    unittest.main()
