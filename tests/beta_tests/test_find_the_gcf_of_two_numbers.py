import unittest

from katas.beta.find_the_gcf_of_two_numbers import find_GCF


class FindGCFTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(find_GCF(2, 4), 2)

    def test_equal_2(self):
        self.assertEqual(find_GCF(8, 20), 4)

    def test_equal_3(self):
        self.assertEqual(find_GCF(5, 13), 1)

    def test_equal_4(self):
        self.assertEqual(find_GCF(100, 100), 100)
