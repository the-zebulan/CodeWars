import unittest

from Kyu_7.regexp_basics_parsing_prices import to_cents


class ToCentsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_cents('$1.23'), 123)

    def test_equals_2(self):
        self.assertEqual(to_cents('$99.99'), 9999)

    def test_equals_3(self):
        self.assertEqual(to_cents('$12345678.90'), 1234567890)

    def test_equals_4(self):
        self.assertEqual(to_cents('$9.69'), 969)

    def test_equals_5(self):
        self.assertEqual(to_cents('$9.70'), 970)

    def test_equals_6(self):
        self.assertEqual(to_cents('$9.71'), 971)

    def test_equals_7(self):
        self.assertEqual(to_cents('$0.69'), 69)

    def test_none(self):
        self.assertIsNone(to_cents(''))

    def test_none_2(self):
        self.assertIsNone(to_cents('1'))

    def test_none_3(self):
        self.assertIsNone(to_cents('1.23'))

    def test_none_4(self):
        self.assertIsNone(to_cents('$1'))

    def test_none_5(self):
        self.assertIsNone(to_cents('$1.23\n'))

    def test_none_6(self):
        self.assertIsNone(to_cents('\n$1.23'))

    def test_none_7(self):
        self.assertIsNone(to_cents('$9.69$4.3.7'))

    def test_none_8(self):
        self.assertIsNone(to_cents('$9.692'))


if __name__ == '__main__':
    unittest.main()
