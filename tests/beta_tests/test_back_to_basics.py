import unittest

from katas.beta.back_to_basics import types


class TypesTestCase(unittest.TestCase):
    def test_equals_(self):
        self.assertEqual(types(10), 'int')

    def test_equals_2(self):
        self.assertEqual(types(9.7), 'float')

    def test_equals_3(self):
        self.assertEqual(types('&*('), 'str')

    def test_equals_4(self):
        self.assertEqual(types(True), 'bool')


if __name__ == '__main__':
    unittest.main()
