import unittest

from katas.beta.float_or_integer_verifier import i_or_f


class IntegerOrFloatTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(i_or_f('1'))

    def test_true_2(self):
        self.assertTrue(i_or_f('1.0'))

    def test_true_3(self):
        self.assertTrue(i_or_f('1e1'))

    def test_true_4(self):
        self.assertTrue(i_or_f('1E-1'))

    def test_true_5(self):
        self.assertTrue(i_or_f('1e+1'))


if __name__ == '__main__':
    unittest.main()
