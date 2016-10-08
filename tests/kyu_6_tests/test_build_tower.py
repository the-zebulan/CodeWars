import unittest

from katas.kyu_6.build_tower import tower_builder


class TowerBuilderTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(tower_builder(1), ['*'])

    def test_equal_2(self):
        self.assertEqual(tower_builder(2), [
            ' * ',
            '***'])

    def test_equal_3(self):
        self.assertEqual(tower_builder(3), [
            '  *  ',
            ' *** ',
            '*****'])

    def test_equal_4(self):
        self.assertEqual(tower_builder(6), [
            '     *     ',
            '    ***    ',
            '   *****   ',
            '  *******  ',
            ' ********* ',
            '***********'])
