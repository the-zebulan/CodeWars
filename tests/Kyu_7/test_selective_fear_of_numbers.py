import unittest

from Kyu_7.selective_fear_of_numbers import am_I_afraid


class AmIAfraidTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(am_I_afraid('Sunday', -666))

    def test_true_2(self):
        self.assertTrue(am_I_afraid('Tuesday', 965))

    def test_true_3(self):
        self.assertTrue(am_I_afraid('Friday', 2))

    def test_false(self):
        self.assertFalse(am_I_afraid('Monday', 13))

    def test_false_2(self):
        self.assertFalse(am_I_afraid('Tuesday', 2))


if __name__ == '__main__':
    unittest.main()
