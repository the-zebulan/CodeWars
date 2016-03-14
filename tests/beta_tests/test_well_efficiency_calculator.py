import unittest

from beta.well_efficiency_calculator import is_efficient


class IsEfficientTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_efficient(10, 10, 2.5))

    def test_true_2(self):
        self.assertTrue(is_efficient(12, 3, 1.5))

    def test_true_3(self):
        self.assertTrue(is_efficient(17, 11, 3))

    def test_false(self):
        self.assertFalse(is_efficient(12, 3, 7.5))

    def test_false_2(self):
        self.assertFalse(is_efficient(8, 9, 6))

    def test_false_3(self):
        self.assertFalse(is_efficient(0, 0, 2.3))


if __name__ == '__main__':
    unittest.main()
