import unittest

from Kyu_6.unusual_sort import unusual_sort


class UnusualSortTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unusual_sort(['a', 'z', 'b']), ['a', 'b', 'z'])

    def test_equals_2(self):
        self.assertEqual(unusual_sort(['a', 'Z', 'B']), ['B', 'Z', 'a'])

    def test_equals_3(self):
        self.assertEqual(unusual_sort(['1', 'z', 'a']), ['a', 'z', '1'])

    def test_equals_4(self):
        self.assertEqual(unusual_sort(['1', 'Z', 'a']), ['Z', 'a', '1'])

    def test_equals_5(self):
        self.assertEqual(unusual_sort([3, 2, 1, 'a', 'z', 'b']),
                         ['a', 'b', 'z', 1, 2, 3])

    def test_equals_6(self):
        self.assertEqual(unusual_sort([3, '2', 1, 'a', 'c', 'b']),
                         ['a', 'b', 'c', 1, '2', 3])

    def test_equals_7(self):
        self.assertEqual(unusual_sort([3, '2', 1, '1', '3', 2]),
                         [1, '1', 2, '2', 3, '3'])


if __name__ == '__main__':
    unittest.main()
