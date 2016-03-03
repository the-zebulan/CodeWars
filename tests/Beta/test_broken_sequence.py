import unittest

from Beta.broken_sequence import find_missing_number


class MissingNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_missing_number('1 2 3 5'), 4)

    def test_equals_2(self):
        self.assertEqual(find_missing_number('1 3'), 2)

    def test_equals_3(self):
        self.assertEqual(find_missing_number(''), 0)


if __name__ == '__main__':
    unittest.main()
