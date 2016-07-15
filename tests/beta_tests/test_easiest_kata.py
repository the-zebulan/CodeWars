import unittest

from katas.beta.easiest_kata import addition_calc


class AdditionCalcTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(addition_calc(1, 2), 3)

    def test_equals_2(self):
        self.assertEqual(addition_calc(997, 1087), 2084)
