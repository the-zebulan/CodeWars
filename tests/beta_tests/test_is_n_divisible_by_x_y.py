import unittest

from beta.is_n_divisible_by_x_y import is_divisible


class IsDivisibleTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_divisible(48, 3, 4))

    def test_true_2(self):
        self.assertTrue(is_divisible(12, 3, 4))

    def test_false(self):
        self.assertFalse(is_divisible(3, 3, 4))

    def test_false_2(self):
        self.assertFalse(is_divisible(8, 3, 4))


if __name__ == '__main__':
    unittest.main()
