import unittest

from katas.kyu_7.vampire_numbers import vampire_test


class VampireTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(vampire_test(21, 6))

    def test_true_2(self):
        self.assertTrue(vampire_test(204, 615))

    def test_true_3(self):
        self.assertTrue(vampire_test(30, -51))

    def test_true_4(self):
        self.assertTrue(vampire_test(210, 600))

    def test_false(self):
        self.assertFalse(vampire_test(-246, -510))
