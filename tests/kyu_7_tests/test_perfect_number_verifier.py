import unittest

from katas.kyu_7.perfect_number_verifier import isPerfect


class IsPerfectTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(isPerfect(6))

    def test_true_2(self):
        self.assertTrue(isPerfect(28))

    def test_true_3(self):
        self.assertTrue(isPerfect(8128))

    def test_false(self):
        self.assertFalse(isPerfect(1))

    def test_false_2(self):
        self.assertFalse(isPerfect(120))

    def test_false_3(self):
        self.assertFalse(isPerfect(4986))


if __name__ == '__main__':
    unittest.main()
