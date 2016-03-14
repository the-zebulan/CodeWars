import unittest

from Beta.reverse_or_rotate import revrot


class ReverseOrRotateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(revrot('123456987654', 6), '234561876549')

    def test_equals_2(self):
        self.assertEqual(revrot('123456987653', 6), '234561356789')

    def test_equals_3(self):
        self.assertEqual(revrot('66443875', 4), '44668753')

    def test_equals_4(self):
        self.assertEqual(revrot('66443875', 8), '64438756')

    def test_equals_5(self):
        self.assertEqual(revrot('664438769', 8), '67834466')

    def test_equals_6(self):
        self.assertEqual(revrot('123456779', 8), '23456771')

    def test_equals_7(self):
        self.assertEqual(revrot('', 8), '')

    def test_equals_8(self):
        self.assertEqual(revrot('123456779', 0), '')


if __name__ == '__main__':
    unittest.main()
