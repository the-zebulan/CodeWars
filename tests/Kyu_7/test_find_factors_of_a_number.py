import unittest

from Kyu_7.find_factors_of_a_number import factors


class FactorsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(factors(-4), -1)

    def test_equals_2(self):
        self.assertEqual(factors(0), -1)

    def test_equals_3(self):
        self.assertEqual(factors(-12), -1)

    def test_equals_4(self):
        self.assertEqual(factors('a'), -1)

    def test_equals_5(self):
        self.assertEqual(factors(4.5), -1)

    def test_equals_6(self):
        self.assertEqual(factors('hello world'), -1)

    def test_equals_7(self):
        self.assertEqual(factors(54), [54, 27, 18, 9, 6, 3, 2, 1])

    def test_equals_8(self):
        self.assertEqual(factors(49), [49, 7, 1])

    def test_equals_9(self):
        self.assertEqual(factors(1), [1])


if __name__ == '__main__':
    unittest.main()
