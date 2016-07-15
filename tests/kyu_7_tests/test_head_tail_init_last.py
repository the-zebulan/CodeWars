import unittest

from katas.kyu_7.head_tail_init_last import head, init, last, tail


class HeadTailInitLastTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(head([5, 1]), 5)

    def test_equals_2(self):
        self.assertEqual(tail([1]), [])

    def test_equals_3(self):
        self.assertEqual(init([1, 5, 7, 9]), [1, 5, 7])

    def test_equals_4(self):
        self.assertEqual(last([7, 2]), 2)
