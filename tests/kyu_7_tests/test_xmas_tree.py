import unittest

from katas.kyu_7.xmas_tree import xMasTree


class XmasTreeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(xMasTree(2), [
            '_#_',
            '###',
            '_#_',
            '_#_'])

    def test_equal_2(self):
        self.assertEqual(xMasTree(3), [
            '__#__',
            '_###_',
            '#####',
            '__#__',
            '__#__'
        ])

    def test_equal_3(self):
        self.assertEqual(xMasTree(4), [
            '___#___',
            '__###__',
            '_#####_',
            '#######',
            '___#___',
            '___#___'
        ])

    def test_equal_4(self):
        self.assertEqual(xMasTree(5), [
            '____#____',
            '___###___',
            '__#####__',
            '_#######_',
            '#########',
            '____#____',
            '____#____'
        ])

    def test_equal_5(self):
        self.assertEqual(xMasTree(6), [
            '_____#_____',
            '____###____',
            '___#####___',
            '__#######__',
            '_#########_',
            '###########',
            '_____#_____',
            '_____#_____'
        ])

    def test_equal_6(self):
        self.assertEqual(xMasTree(7), [
            '______#______',
            '_____###_____',
            '____#####____',
            '___#######___',
            '__#########__',
            '_###########_',
            '#############',
            '______#______',
            '______#______'
        ])
