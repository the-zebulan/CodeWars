import unittest

from Beta.testing_123 import number


class NumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(number([]), [])

    def test_equals_2(self):
        self.assertEqual(number(['a', 'b', 'c']), ['1: a', '2: b', '3: c'])


if __name__ == '__main__':
    unittest.main()
