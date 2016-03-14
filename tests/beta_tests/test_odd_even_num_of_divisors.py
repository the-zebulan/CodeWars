import unittest

from beta.odd_even_num_of_divisors import oddity


class OddityTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(oddity(1), 'odd')

    def test_equals_2(self):
        self.assertEqual(oddity(5), 'even')

    def test_equals_3(self):
        self.assertEqual(oddity(16), 'odd')

    def test_equals_4(self):
        self.assertEqual(oddity(100), 'odd')


if __name__ == '__main__':
    unittest.main()
