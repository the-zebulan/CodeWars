import unittest

from kyu_8.opposites_attract import lovefunc


class LoveTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(lovefunc(1, 4))

    def test_true_2(self):
        self.assertTrue(lovefunc(0, 1))

    def test_false(self):
        self.assertFalse(lovefunc(2, 2))

    def test_false_2(self):
        self.assertFalse(lovefunc(0, 0))


if __name__ == '__main__':
    unittest.main()
