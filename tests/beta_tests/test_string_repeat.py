import unittest

from katas.beta.string_repeat import repeat_str


class StringRepeatTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(repeat_str(4, 'a'), 'aaaa')

    def test_equal_2(self):
        self.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')

    def test_equal_3(self):
        self.assertEqual(repeat_str(2, 'abc'), 'abcabc')
