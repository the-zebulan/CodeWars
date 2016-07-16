import unittest

from katas.kyu_6.custom_array_filters import MyList


class MyListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(MyList([1, 2, 3, 4, 5]).even(), [2, 4])

    def test_equal_2(self):
        self.assertEqual(MyList([1, 2, 3, 4, 5]).odd(), [1, 3, 5])

    def test_equal_3(self):
        self.assertEqual(MyList([1, 2, 3, 4, 5]).under(4), [1, 2, 3])

    def test_equal_4(self):
        self.assertEqual(MyList([1, 2, 3, 4, 5]).over(4), [5])

    def test_equal_5(self):
        self.assertEqual(MyList([1, 2, 3, 4, 5]).in_range(1, 3), [1, 2, 3])

    def test_equal_6(self):
        self.assertEqual(MyList(
            MyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).even()
        ).under(5), [2, 4])

    def test_equal_7(self):
        self.assertEqual(MyList(
            ['a', 1, 'b', 300, 'x', 'q', 63, 122, 181, 'z', 0.83, 0.11]
        ).even(), [300, 122])
