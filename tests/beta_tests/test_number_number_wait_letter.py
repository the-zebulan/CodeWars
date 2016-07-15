import unittest

from katas.beta.number_number_wait_letter import do_math


class DoMathTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(do_math("24z6 1x23 y369 89a 900b"), 1299)

    def test_equal_2(self):
        self.assertEqual(do_math("24z6 1z23 y369 89z 900b"), 1414)

    def test_equal_3(self):
        self.assertEqual(do_math("10a 90x 14b 78u 45a 7b 34y"), 60)

    def test_equal_4(self):
        self.assertEqual(do_math("111a 222c 444y 777u 999a 888p"), 1459)

    def test_equal_5(self):
        self.assertEqual(do_math("1z 2t 3q 5x 6u 8a 7b"), 8)
