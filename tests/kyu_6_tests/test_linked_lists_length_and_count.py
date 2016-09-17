import unittest

from katas.kyu_6.linked_lists_length_and_count import Node, count, length
from katas.kyu_7.linked_lists_push_and_build_123 import build_one_two_three


class LinkedListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(length(None), 0)

    def test_equal_2(self):
        self.assertEqual(length(Node(99)), 1)

    def test_equal_3(self):
        self.assertEqual(length(build_one_two_three()), 3)

    def test_equal_4(self):
        self.assertEqual(count(build_one_two_three(), 1), 1)

    def test_equal_5(self):
        self.assertEqual(count(build_one_two_three(), 2), 1)

    def test_equal_6(self):
        self.assertEqual(count(build_one_two_three(), 3), 1)

    def test_equal_7(self):
        self.assertEqual(count(build_one_two_three(), 99), 0)

    def test_equal_8(self):
        self.assertEqual(count(None, 1), 0)
