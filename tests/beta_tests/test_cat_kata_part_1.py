import unittest

from katas.beta.cat_kata_part_1 import peaceful_yard


class CatKataTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(peaceful_yard(
            ['-----------L',
             '--R---------',
             '------------',
             '------------',
             '------------',
             '--M---------'], 4))

    def test_true_2(self):
        self.assertTrue(peaceful_yard(
            ['------------',
             '------------',
             '-L----------',
             '------------',
             '------------',
             '------------'], 10))

    def test_false_1(self):
        self.assertFalse(peaceful_yard(
            ['------------',
             '---M--------',
             '------------',
             '------------',
             '-------R----',
             '------------'], 6))
