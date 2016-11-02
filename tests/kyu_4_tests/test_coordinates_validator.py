import unittest

from katas.kyu_4.coordinates_validator import is_valid_coordinates


class IsValidCoordinatesTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_valid_coordinates('-23, 25'))

    def test_true_2(self):
        self.assertTrue(is_valid_coordinates('4, -3'))

    def test_true_3(self):
        self.assertTrue(is_valid_coordinates('24.53525235, 23.45235'))

    def test_true_4(self):
        self.assertTrue(is_valid_coordinates('04, -23.234235'))

    def test_true_5(self):
        self.assertTrue(is_valid_coordinates('43.91343345, 143'))

    def test_false_1(self):
        self.assertFalse(is_valid_coordinates('23.234, - 23.4234'))

    def test_false_2(self):
        self.assertFalse(is_valid_coordinates('2342.43536, 34.324236'))

    def test_false_3(self):
        self.assertFalse(is_valid_coordinates('N23.43345, E32.6457'))

    def test_false_4(self):
        self.assertFalse(is_valid_coordinates('99.234, 12.324'))

    def test_false_5(self):
        self.assertFalse(is_valid_coordinates('6.325624, 43.34345.345'))

    def test_false_6(self):
        self.assertFalse(is_valid_coordinates('0, 1,2'))

    def test_false_7(self):
        self.assertFalse(is_valid_coordinates('0.342q0832, 1.2324'))

    def test_false_8(self):
        self.assertFalse(is_valid_coordinates('23.245, 1e1'))
