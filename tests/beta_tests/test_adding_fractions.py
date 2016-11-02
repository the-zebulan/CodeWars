import unittest

from katas.beta.adding_fractions import add_fracs


class AddingFractionsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(add_fracs(), '')

    def test_equal_2(self):
        self.assertEqual(add_fracs('1/2'), '1/2')

    def test_equal_3(self):
        self.assertEqual(add_fracs('1/2', '1/4'), '3/4')

    def test_equal_4(self):
        self.assertEqual(add_fracs('1/2', '3/4'), '5/4')

    def test_equal_5(self):
        self.assertEqual(add_fracs('2/4', '6/4', '4/4'), '3')

    def test_equal_6(self):
        self.assertEqual(add_fracs('2/3', '1/3', '4/6'), '5/3')

    def test_equal_7(self):
        self.assertEqual(add_fracs('2/3', '1/4', '5/6'), '7/4')

    def test_equal_8(self):
        self.assertEqual(add_fracs('-2/3', '5/3', '-4/6'), '1/3')

    def test_equal_9(self):
        self.assertEqual(add_fracs('-7/3', '-1/3', '-2/3'), '-10/3')

    def test_equal_10(self):
        self.assertEqual(add_fracs('1/4', '5/4', '-1/2', '-1/1'), '0')
