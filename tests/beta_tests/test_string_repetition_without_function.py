import unittest
from types import FunctionType

from katas.beta.string_repetition_without_function import str_repeat


class StrRepeatTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(str_repeat('a', 4), 'aaaa')

    def test_equal_2(self):
        self.assertEqual(str_repeat('hello ', 3), 'hello hello hello ')

    def test_equal_3(self):
        self.assertEqual(str_repeat('abc', 2), 'abcabc')

    def test_is_instance_1(self):
        self.assertNotIsInstance(str_repeat, FunctionType)
