import unittest

from katas.beta.cat_and_mouse_easy_version import cat_mouse


class CatMouseTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(cat_mouse('C....m'), 'Escaped!')

    def test_equal_2(self):
        self.assertEqual(cat_mouse('C..m'), 'Caught!')

    def test_equal_3(self):
        self.assertEqual(cat_mouse('C.....m'), 'Escaped!')

    def test_equal_4(self):
        self.assertEqual(cat_mouse('C.m'), 'Caught!')

    def test_equal_5(self):
        self.assertEqual(cat_mouse('m...C'), 'Caught!')
