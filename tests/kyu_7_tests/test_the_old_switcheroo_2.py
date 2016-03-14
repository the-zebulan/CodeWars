import unittest

from katas.kyu_7.the_old_switcheroo_2 import encode


class EncodeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(encode('abc'), '123')

    def test_equals_2(self):
        self.assertEqual(encode('codewars'), '315452311819')

    def test_equals_3(self):
        self.assertEqual(encode('abc-#@5'), '123-#@5')

    def test_equals_4(self):
        self.assertEqual(encode('ABCD'), '1234')

    def test_equals_5(self):
        self.assertEqual(encode('ZzzzZ'), '2626262626')

    def test_equals_6(self):
        self.assertEqual(encode(
            'this is a long string!! Please [encode] @C0RrEctly'),
            '208919 919 1 1215147 1920189147!! 161251195 [51431545] @3018185'
            '3201225')


if __name__ == '__main__':
    unittest.main()
