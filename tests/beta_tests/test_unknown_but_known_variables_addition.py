import unittest

from katas.beta.the_unknown_but_known_variables_addition import the_var


class TheVarTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(the_var('d+g'), 11)

    def test_equal_2(self):
        self.assertEqual(the_var('a+z'), 27)

    def test_equal_3(self):
        self.assertEqual(the_var('g+v'), 29)

    def test_equal_4(self):
        self.assertEqual(the_var('x+n'), 38)

    def test_equal_5(self):
        self.assertEqual(the_var('b+y'), 27)
