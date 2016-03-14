import unittest

from katas.kyu_7.summing_a_numbers_digits import sumDigits


class SumDigitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sumDigits(10), 1)

    def test_equals_2(self):
        self.assertEqual(sumDigits(99), 18)

    def test_equals_3(self):
        self.assertEqual(sumDigits(-32), 5)


if __name__ == '__main__':
    unittest.main()
