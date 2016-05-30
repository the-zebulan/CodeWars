import math
import re
import unittest

from katas.kyu_7.anything import anything


class AnythingTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(anything({}) != [])

    def test_true_2(self):
        self.assertTrue(anything('Hello') < 'World')

    def test_true_3(self):
        self.assertTrue(anything(80) > 81)

    def test_true_4(self):
        self.assertTrue(anything(re) >= re)

    def test_true_5(self):
        self.assertTrue(anything(re) <= math)

    def test_true_6(self):
        self.assertTrue(anything(5) == ord)

    def test_true_7(self):
        self.assertTrue(anything(10) == 10)

    def test_true_8(self):
        self.assertTrue(anything(20) == -20)

    def test_true_9(self):
        self.assertTrue(anything(30) == "-30 30")

    def test_true_10(self):
        self.assertTrue(anything(True) == False)

    def test_true_11(self):
        self.assertTrue(anything({}) == [])


if __name__ == '__main__':
    unittest.main()
