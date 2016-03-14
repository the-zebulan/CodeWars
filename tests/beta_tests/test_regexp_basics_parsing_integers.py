import unittest

from Beta.regexp_basics_parsing_integers import to_integer


class ParsingIntegersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_integer("123"), 123)

    def test_equals_2(self):
        self.assertEqual(to_integer("0x123"), 0x123)

    def test_equals_3(self):
        self.assertEqual(to_integer("0o123"), 0o123)

    def test_equals_4(self):
        self.assertEqual(to_integer("0123"), 123)

    def test_equals_5(self):
        self.assertEqual(to_integer("0b1010"), 0b1010)

    def test_equals_6(self):
        self.assertEqual(to_integer("+123"), 123)

    def test_equals_7(self):
        self.assertEqual(to_integer("-123"), -123)

    def test_equals_8(self):
        self.assertEqual(to_integer("-0x123"), -0x123)

    def test_equals_9(self):
        self.assertEqual(to_integer("-0o123"), -0o123)

    def test_equals_10(self):
        self.assertEqual(to_integer("-0123"), -123)

    def test_equals_11(self):
        self.assertEqual(to_integer("-0b1010"), -0b1010)

    def test_equals_12(self):
        self.assertEqual(to_integer("0xDEADbeef"), 0xDEADBEEF)

    def test_none(self):
        self.assertIsNone(to_integer("123 "))

    def test_none_2(self):
        self.assertIsNone(to_integer(" 123"))

    def test_none_3(self):
        self.assertIsNone(to_integer("0B1010"))

    def test_none_4(self):
        self.assertIsNone(to_integer("0b12"))

    def test_none_5(self):
        self.assertIsNone(to_integer("123\n"))

    def test_none_6(self):
        self.assertIsNone(to_integer("\n123"))

    def test_none_7(self):
        self.assertIsNone(to_integer("0X123"))

    def test_none_8(self):
        self.assertIsNone(to_integer("0O123"))

    def test_none_9(self):
        self.assertIsNone(to_integer("0o18"))


if __name__ == '__main__':
    unittest.main()
