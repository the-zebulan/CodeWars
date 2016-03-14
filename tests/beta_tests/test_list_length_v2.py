import unittest

from beta.list_length_v2 import count


class ListLengthTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count([1, 2, 3, 4]), 4)

    def test_equals_2(self):
        self.assertEqual(count([1, 2, 3, 4, 5, 6, 7]), 7)


if __name__ == '__main__':
    unittest.main()
