import unittest

from katas.kyu_7.dont_give_me_five import dont_give_me_five


class DontGiveMeFiveTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(dont_give_me_five(1, 9), 8)

    def test_equal_2(self):
        self.assertEqual(dont_give_me_five(4, 17), 12)
