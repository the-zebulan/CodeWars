import unittest

from Kyu_7.monotone_travel import is_monotone


class IsMonotoneTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_monotone(range(1, 11)))

    def test_true_2(self):
        self.assertTrue(is_monotone([5, 5, 5, 5, 5, 5, 5]))

    def test_true_3(self):
        self.assertTrue(is_monotone([]))

    def test_true_4(self):
        self.assertTrue(is_monotone([1]))

    def test_false(self):
        self.assertFalse(is_monotone(range(5, 0, -1)))

    def test_false_2(self):
        self.assertFalse(is_monotone(range(5, -40, -1)))


if __name__ == '__main__':
    unittest.main()
