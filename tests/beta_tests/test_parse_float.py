import unittest

from katas.beta.parse_float import parse_float


class ParseFloatTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(parse_float('1.0'), 1.0)

    def test_equal_2(self):
        self.assertEqual(parse_float('234.0234'), 234.0234)

    def test_is_none_1(self):
        self.assertIsNone(parse_float('a'))
