import unittest

from beta.my_first_bug_fixing_kata import foo


class FooTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(foo(), 42)

    def test_instance(self):
        self.assertIsInstance(foo(), int)


if __name__ == '__main__':
    unittest.main()
