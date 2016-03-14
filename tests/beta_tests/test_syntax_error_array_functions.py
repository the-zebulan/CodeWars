import unittest

from Beta.syntax_error_array_functions import Foo


class FooTestCase(unittest.TestCase):
    def setUp(self):
        self.f = Foo()

    def test_equals(self):
        self.assertEqual(self.f.convert('0', 0), 0)

    def test_equals_2(self):
        self.assertEqual(self.f.convert('0', 1), 0)


if __name__ == '__main__':
    unittest.main()
