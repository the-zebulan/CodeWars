import unittest

from katas.kyu_6.cat_and_mouse_harder_version import cat_mouse


class CatMouseTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(cat_mouse('..D.....C.m', 2), 'Caught!')

    def test_equal_2(self):
        self.assertEqual(cat_mouse('.CD......m.', 1), 'Escaped!')

    def test_equal_3(self):
        self.assertEqual(cat_mouse('.CD......m.', 10), 'Protected!')

    def test_equal_4(self):
        self.assertEqual(cat_mouse('...m.........C...D', 10), 'Caught!')

    def test_equal_5(self):
        self.assertEqual(cat_mouse('m.C...', 5), 'boring without all three')

    def test_equal_6(self):
        self.assertEqual(
            cat_mouse('...m....D....C.......', 10), 'Protected!')

    def test_equal_7(self):
        self.assertEqual(
            cat_mouse('............C.............D..m...', 8), 'Escaped!')
