import unittest

from katas.kyu_8.find_the_position import position


class PositionTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(position('a'), 'Position of alphabet: 1')

    def test_equal_2(self):
        self.assertEqual(position('z'), 'Position of alphabet: 26')

    def test_equal_3(self):
        self.assertEqual(position('e'), 'Position of alphabet: 5')
