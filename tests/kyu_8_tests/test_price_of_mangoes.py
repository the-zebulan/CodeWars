import unittest

from katas.kyu_8.price_of_mangoes import mango


class MangoTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(mango(3, 3), 6)

    def test_equal_2(self):
        self.assertEqual(mango(9, 5), 30)
