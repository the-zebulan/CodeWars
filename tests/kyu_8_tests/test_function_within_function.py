import unittest

from katas.kyu_8.function_within_function import always


class AlwaysTestCase(unittest.TestCase):
    def setUp(self):
        self.three = always(3)

    def test_equals(self):
        self.assertEqual(self.three(), 3)


if __name__ == '__main__':
    unittest.main()
