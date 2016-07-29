import unittest

from katas.kyu_8.grasshopper_if_else_syntax_debug import checkAlive


class CheckAliveTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(checkAlive(1))

    def test_true_2(self):
        self.assertTrue(checkAlive(3))

    def test_false_1(self):
        self.assertFalse(checkAlive(-2))

    def test_false_2(self):
        self.assertFalse(checkAlive(0))
