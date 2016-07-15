import unittest

from katas.kyu_8.reverse_list_order import reverse_list


class ReverseListTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
