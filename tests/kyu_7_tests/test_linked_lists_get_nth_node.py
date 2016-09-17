import unittest

from katas.kyu_7.linked_lists_get_nth_node import get_nth
from katas.kyu_7.linked_lists_push_and_build_123 import build_one_two_three


class LinkedListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_nth(build_one_two_three(), 0).data, 1,
                         'First node should be located at index 0.')

    def test_equal_2(self):
        self.assertEqual(get_nth(build_one_two_three(), 1).data, 2,
                         'Second node should be located at index 1.')

    def test_equal_3(self):
        self.assertEqual(get_nth(build_one_two_three(), 2).data, 3,
                         'Third node should be located at index 2.')

    def test_raises_1(self):
        self.assertRaises(Exception, get_nth, build_one_two_three(), 3)

    def test_raises_2(self):
        self.assertRaises(Exception, get_nth, build_one_two_three(), -1)

    def test_raises_3(self):
        self.assertRaises(Exception, get_nth, build_one_two_three(), 100)

    def test_raises_4(self):
        self.assertRaises(Exception, get_nth, None, 0)
