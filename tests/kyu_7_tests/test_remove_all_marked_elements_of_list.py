import unittest

from kyu_7.remove_all_marked_elements_of_list import List


class RemoveMarkedElementsTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = List()

    def test_equals(self):
        self.assertEqual(self.lst.remove_([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]),
                         [2, 2, 4])

    def test_equals_2(self):
        self.assertEqual(self.lst.remove_(
            [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2]
        ), [5, 6, 7, 8])

    def test_equals_3(self):
        self.assertEqual(self.lst.remove_(
            [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3]
        ), [8, 7, 6, 5, 1])


if __name__ == '__main__':
    unittest.main()
