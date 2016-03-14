import unittest

from Kyu_8.reverse_list_order import reverse_list


class ReverseListTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
