import unittest

from katas.kyu_7.every_nth_array_element_basic import every


class EveryNthElementTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = [0, 1, 2, 3, 4]
        self.lst2 = list('test')
        self.lst3 = [None, 1, ['two'], 'three', {4: 'IV'}]

    def test_equal_1(self):
        self.assertEqual(every(self.lst, 1), [0, 1, 2, 3, 4])

    def test_equal_2(self):
        self.assertEqual(every(self.lst, 2), [0, 2, 4])

    def test_equal_3(self):
        self.assertEqual(every(self.lst, 3), [0, 3])

    def test_equal_4(self):
        self.assertEqual(every(self.lst, 4), [0, 4])

    def test_equal_5(self):
        self.assertEqual(every(self.lst, 5), [0])

    def test_equal_6(self):
        self.assertEqual(every(self.lst, 1, 1), [1, 2, 3, 4])

    def test_equal_7(self):
        self.assertEqual(every(self.lst, 2, 1), [1, 3])

    def test_equal_8(self):
        self.assertEqual(every(self.lst, 3, 1), [1, 4])

    def test_equal_9(self):
        self.assertEqual(every(self.lst, 4, 1), [1])

    def test_equal_10(self):
        self.assertEqual(every(self.lst, 5, 1), [1])

    def test_equal_11(self):
        self.assertEqual(every(self.lst), [0, 1, 2, 3, 4])

    def test_equal_12(self):
        self.assertEqual(every(self.lst, 1), [0, 1, 2, 3, 4])

    def test_equal_13(self):
        self.assertEqual(every(self.lst, 2), [0, 2, 4])

    def test_equal_14(self):
        self.assertEqual(every(self.lst, 3), [0, 3])

    def test_equal_15(self):
        self.assertEqual(every(self.lst, 1, 3), [3, 4])

    def test_equal_16(self):
        self.assertEqual(every(self.lst, 3, 1), [1, 4])

    def test_equal_17(self):
        self.assertEqual(every(self.lst, 3, 4), [4])

    def test_equal_18(self):
        self.assertEqual(every(self.lst2), ['t', 'e', 's', 't'])

    def test_equal_19(self):
        self.assertEqual(every(self.lst2, 2), ['t', 's'])

    def test_equal_20(self):
        self.assertEqual(every(self.lst2, 2, 1), ['e', 't'])

    def test_equal_21(self):
        self.assertEqual(every(self.lst3, 1), self.lst3)

    def test_equal_22(self):
        self.assertEqual(every(self.lst3, 2, 2), [['two'], {4: 'IV'}])

    def test_equal_23(self):
        self.assertEqual(every([None] * 5, 2), [None] * 3)
