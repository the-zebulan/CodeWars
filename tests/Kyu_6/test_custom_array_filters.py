import __builtin__
import unittest

from Kyu_6.custom_array_filters import MyList

__builtin__.list = MyList


class MyListTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(list([1, 2, 3, 4, 5]).even(), [2, 4])

    def test_equals_2(self):
        self.assertEqual(list([1, 2, 3, 4, 5]).odd(), [1, 3, 5])

    def test_equals_3(self):
        self.assertEqual(list([1, 2, 3, 4, 5]).under(4), [1, 2, 3])

    def test_equals_4(self):
        self.assertEqual(list([1, 2, 3, 4, 5]).over(4), [5])

    def test_equals_5(self):
        self.assertEqual(list([1, 2, 3, 4, 5]).in_range(1, 3), [1, 2, 3])

    def test_equals_6(self):
        self.assertEqual(list(list(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).even()).under(5), [2, 4])

    def test_equals_7(self):
        self.assertEqual(list(['a', 1, 'b', 300, 'x', 'q', 63, 122, 181, 'z',
                               0.83, 0.11]).even(), [300, 122])

    def tearDown(self):
        __builtin__.list = __builtin__.list


if __name__ == '__main__':
    unittest.main()
