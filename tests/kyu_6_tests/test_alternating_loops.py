import unittest

from katas.kyu_6.alternating_loops import combine


class CombineTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(combine(['a', 'b', 'c'], [1, 2, 3]),
                         ['a', 1, 'b', 2, 'c', 3])

    def test_equals_2(self):
        self.assertEqual(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]),
                         ['a', 1, 'b', 2, 'c', 3, 4, 5])

    def test_equals_3(self):
        self.assertEqual(combine(
            ['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]),
            ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5])
