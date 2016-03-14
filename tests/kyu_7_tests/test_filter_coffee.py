import unittest

from kyu_7.filter_coffee import search


class SearchTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(search(3, [6, 1, 2, 9, 2]), '1,2,2')

    def test_equals_2(self):
        self.assertEqual(search(14, [7, 3, 23, 9, 14, 20, 7]), '3,7,7,9,14')

    def test_equals_3(self):
        self.assertEqual(search(0, [6, 1, 2, 9, 2]), '')

    def test_equals_4(self):
        self.assertEqual(search(10, []), '')

    def test_equals_5(self):
        self.assertEqual(search(24, [24, 0, 100, 2, 5]), '0,2,5,24')


if __name__ == '__main__':
    unittest.main()
