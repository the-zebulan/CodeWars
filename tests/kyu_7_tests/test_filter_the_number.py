import unittest

from kyu_7.filter_the_number import filter_string


class FilterStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(filter_string("123"), 123)

    def test_equals_2(self):
        self.assertEqual(filter_string("a1b2c3"), 123)

    def test_equals_3(self):
        self.assertEqual(filter_string("aa1bb2cc3dd"), 123)

    def test_equals_4(self):
        self.assertEqual(filter_string("aa 112 3dd"), 1123)

    def test_equals_5(self):
        self.assertEqual(filter_string("11bb2c23c3"), 112233)


if __name__ == '__main__':
    unittest.main()
