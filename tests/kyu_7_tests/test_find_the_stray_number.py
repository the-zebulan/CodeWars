import unittest

from katas.kyu_7.find_the_stray_number import stray


class StrayTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(stray([1, 1, 2]), 2)

    def test_equal_2(self):
        self.assertEqual(stray([2, 3, 2, 2, 2]), 3)

    def test_equal_3(self):
        self.assertEqual(stray([1, 1, 1, 1, 1, 1, 2]), 2)

    def test_equal_4(self):
        self.assertEqual(stray([17, 17, 3, 17, 17, 17, 17]), 3)
