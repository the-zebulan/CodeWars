import unittest

from katas.kyu_8.sleigh_authentication import Sleigh


class SleighTestCase(unittest.TestCase):
    def setUp(self):
        self.sleigh = Sleigh()

    def test_true(self):
        self.assertTrue(self.sleigh.authenticate('Santa Claus', 'Ho Ho Ho!'))

    def test_false(self):
        self.assertFalse(self.sleigh.authenticate('Santa', 'Ho Ho Ho!'))

    def test_false_2(self):
        self.assertFalse(self.sleigh.authenticate('Santa Claus', 'Ho Ho!'))

    def test_false_3(self):
        self.assertFalse(self.sleigh.authenticate('jhoffner', 'CodeWars'))


if __name__ == '__main__':
    unittest.main()
