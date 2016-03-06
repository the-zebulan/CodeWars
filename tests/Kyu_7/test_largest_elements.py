import unittest

from Kyu_7.largest_elements import largest


class LargestTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(largest(2, [7, 6, 5, 4, 3, 2, 1]), [6, 7])


if __name__ == '__main__':
    unittest.main()
