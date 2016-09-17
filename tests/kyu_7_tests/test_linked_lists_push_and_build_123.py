import unittest

from katas.kyu_7.linked_lists_push_and_build_123 import \
    Node, build_one_two_three, push


class LinkedListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(push(None, 1).data, 1)

    def test_equal_2(self):
        self.assertEqual(push(Node(1), 2).data, 2)

    def test_equal_3(self):
        self.assertEqual(push(Node(1), 2).next.data, 1)

    def test_equal_4(self):
        self.assertEqual(build_one_two_three().data, 1)

    def test_equal_5(self):
        self.assertEqual(build_one_two_three().next.data, 2)

    def test_equal_6(self):
        self.assertEqual(build_one_two_three().next.next.data, 3)

    def test_is_none_1(self):
        self.assertIsNone(push(None, 1).next)

    def test_is_none_2(self):
        self.assertIsNone(build_one_two_three().next.next.next)
