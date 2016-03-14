import unittest

from kyu_6.find_the_divisors import divisors


class FindTheDivisorsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(divisors(12), [2, 3, 4, 6])

    def test_equals_2(self):
        self.assertEqual(divisors(25), [5])

    def test_equals_3(self):
        self.assertEqual(divisors(13), '13 is prime')

    def test_equals_4(self):
        self.assertEqual(divisors(15), [3, 5])


if __name__ == '__main__':
    unittest.main()
