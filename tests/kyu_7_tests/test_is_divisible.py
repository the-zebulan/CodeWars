import unittest

from kyu_7.is_divisible import is_divisible


class IsDivisibleTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_divisible(12, 3, 4))

    def test_false(self):
        self.assertFalse(is_divisible(3, 3, 4))

    def test_false_2(self):
        self.assertFalse(is_divisible(8, 3, 4, 2, 5))


if __name__ == '__main__':
    unittest.main()
