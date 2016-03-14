import unittest

from Beta.cyclops_number import cyclops


class CyclopsTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(cyclops(5))

    def test_true_2(self):
        self.assertTrue(cyclops(27))

    def test_false(self):
        self.assertFalse(cyclops(1))

    def test_false_2(self):
        self.assertFalse(cyclops(3))

    def test_false_3(self):
        self.assertFalse(cyclops(13))


if __name__ == '__main__':
    unittest.main()
