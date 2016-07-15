import unittest

from katas.kyu_7.making_copies import copy_list


class CopyListTestCase(unittest.TestCase):
    def setUp(self):
        self.test = [1, 2, 3, 4]
        self.test_copy = copy_list(self.test)
        self.test[1] += 5

    def test_equals(self):
        self.assertEqual(self.test, [1, 7, 3, 4])

    def test_equals_2(self):
        self.assertEqual(self.test_copy, [1, 2, 3, 4])
