import unittest

from Beta.narcissistic_numbers import is_narcissistic


class NarcissisticTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_narcissistic(153))

    def test_true_2(self):
        self.assertTrue(is_narcissistic(371))

    def test_true_3(self):
        self.assertTrue(is_narcissistic(407))

    def test_true_4(self):
        self.assertTrue(is_narcissistic(1634))

    def test_false(self):
        self.assertFalse(is_narcissistic(201))

    def test_false_2(self):
        self.assertFalse(is_narcissistic(259))

    def test_false_3(self):
        self.assertFalse(is_narcissistic(595))

    def test_false_4(self):
        self.assertFalse(is_narcissistic(825))


if __name__ == '__main__':
    unittest.main()
