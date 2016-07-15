import unittest

from katas.kyu_8.training_js_7_if_else_ternary import sale_hotdogs


class HotDogsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sale_hotdogs(0), 0)

    def test_equal_2(self):
        self.assertEqual(sale_hotdogs(1), 100)

    def test_equal_3(self):
        self.assertEqual(sale_hotdogs(2), 200)

    def test_equal_4(self):
        self.assertEqual(sale_hotdogs(3), 300)

    def test_equal_5(self):
        self.assertEqual(sale_hotdogs(4), 400)

    def test_equal_6(self):
        self.assertEqual(sale_hotdogs(5), 475)

    def test_equal_7(self):
        self.assertEqual(sale_hotdogs(9), 855)

    def test_equal_8(self):
        self.assertEqual(sale_hotdogs(10), 900)

    def test_equal_9(self):
        self.assertEqual(sale_hotdogs(11), 990)

    def test_equal_10(self):
        self.assertEqual(sale_hotdogs(100), 9000)
