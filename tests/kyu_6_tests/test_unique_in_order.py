import unittest

from katas.kyu_6.unique_in_order import unique_in_order


class UniqueInOrderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'),
                         ['A', 'B', 'C', 'D', 'A', 'B'])


if __name__ == '__main__':
    unittest.main()
