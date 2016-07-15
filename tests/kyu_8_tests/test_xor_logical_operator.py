import unittest

from katas.kyu_8.xor_logical_operator import xor


class XorTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(xor(True, False))

    def test_true_2(self):
        self.assertTrue(xor(False, True))

    def test_true_3(self):
        self.assertTrue(xor(xor(True, False), False))

    def test_true_4(self):
        self.assertTrue(xor(True, xor(True, True)))

    def test_true_5(self):
        self.assertTrue(xor(xor(False, False), xor(False, True)))

    def test_true_6(self):
        self.assertTrue(xor(xor(True, False), xor(False, False)))

    def test_true_7(self):
        self.assertTrue(xor(xor(True, True), xor(True, False)))

    def test_true_8(self):
        self.assertTrue(
            xor(xor(True, xor(True, True)), xor(xor(True, True), False))
        )

    def test_false(self):
        self.assertFalse(xor(False, False))

    def test_false_2(self):
        self.assertFalse(xor(True, True))

    def test_false_3(self):
        self.assertFalse(xor(False, xor(False, False)))

    def test_false_4(self):
        self.assertFalse(xor(xor(True, True), False))

    def test_false_5(self):
        self.assertFalse(xor(xor(False, False), xor(False, False)))

    def test_false_6(self):
        self.assertFalse(xor(xor(True, False), xor(True, False)))
