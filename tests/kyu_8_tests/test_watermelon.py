import unittest

from katas.kyu_8.watermelon import divide


class DivideTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(divide(4))

    def test_true_2(self):
        self.assertTrue(divide(88))

    def test_false(self):
        self.assertFalse(divide(2))

    def test_false_2(self):
        self.assertFalse(divide(67))


if __name__ == '__main__':
    unittest.main()
