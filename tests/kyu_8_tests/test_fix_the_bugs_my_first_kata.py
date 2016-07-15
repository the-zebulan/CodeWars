import unittest

from katas.kyu_8.fix_the_bugs_my_first_kata import my_first_kata


class MyFirstKataTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(my_first_kata(3, 5), (3 % 5 + 5 % 3))

    def test_equals_2(self):
        self.assertEqual(my_first_kata(314, 107), (107 % 314 + 314 % 107))

    def test_equals_3(self):
        self.assertEqual(my_first_kata(1, 32), (1 % 32 + 32 % 1))

    def test_equals_4(self):
        self.assertEqual(my_first_kata(-1, -1), (-1 % -1 + -1 % -1))

    def test_equals_5(self):
        self.assertEqual(my_first_kata(19483, 9), (9 % 19483 + 19483 % 9))

    def test_false(self):
        self.assertFalse(my_first_kata(10, False))

    def test_false_2(self):
        self.assertFalse(my_first_kata("hello", 3))

    def test_false_3(self):
        self.assertFalse(my_first_kata(67, "bye"))

    def test_false_4(self):
        self.assertFalse(my_first_kata(True, True))

    def test_false_5(self):
        self.assertFalse(my_first_kata("hello", {}))

    def test_false_6(self):
        self.assertFalse(my_first_kata([], "pippi"))
