import unittest

from katas.kyu_8.last import last


class LastTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(last([1, 2, 3, 4, 5]), 5)

    def test_equals_2(self):
        self.assertEqual(last('abcde'), 'e')

    def test_equals_3(self):
        self.assertEqual(last(1, 'b', 3, 'd', 5), 5)

    def test_equals_4(self):
        self.assertEqual(last((['a', 'b', 'c', 'k', 'x', 'y', 'z'],),
                              ['a', 'b', 'c', 'k', 'x', 'y', 'z']), 'z')
